"""Apply precomputed rebalance assignments (run: python scripts/_apply_assignments.py)."""
from __future__ import annotations

import re
import textwrap
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
Item = Dict[str, Any]

DISTRACTORS = [
    "stadiul senzorio-motor cu reflexe dominante",
    "operații formale abstracte ca la adolescent",
    "revenirea la dependența totală de părinți",
    "exclusiv senzorio-motor, fără componentă afectivă",
    "dispariția completă a atașamentului și a intimității",
    "absența oricărei influențe a mediului social",
]

# rel_path, var_name, {index: target_n}
ASSIGNMENTS: List[Tuple[str, str, Dict[int, int]]] = [
    ("scripts/psihologia_dezvoltarii_ii_bank_data.py", "PSIHOLOGIA_DEZVOLTARII_II_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_metode_bank_data.py", "METODE_CERCETARE_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_teorii_bank_data.py", "TEORII_INVATARII_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py", "SENZORIO_MOTOR_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_limbaj_bank_data.py", "LIMBAJ_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_atasament_bank_data.py", "ATASAMENT_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_simbol_joc_bank_data.py", "SIMBOL_JOC_ITEMS", {}),
    ("scripts/psihologia_dezvoltarii_ii_scolaritate_bank_data.py", "SCOLARITATE_ITEMS", {}),
]


def load_items(path: Path, var: str) -> List[Item]:
    ns: dict = {}
    exec(path.read_text(encoding="utf-8"), ns)
    return ns[var]


def flatten_stem(stem: Any) -> str:
    if isinstance(stem, tuple):
        return " ".join(stem)
    return str(stem)


def stem_for(n: int, stem: Any) -> Any:
    s = flatten_stem(stem).strip()
    s = re.sub(r"\s+", " ", s)
    if n == 1:
        if s.startswith("Care afirmație"):
            return stem
        if s.startswith("Care "):
            return s.replace("Care ", "Care afirmație ", 1)
        return f"Care afirmație este corectă: {s.rstrip('?')}?"
    if n == 2 and "două" not in s.lower():
        if s.startswith("Care "):
            return s.replace("Care ", "Care două ", 1)
        return f"Care două elemente se aplică: {s.rstrip('?')}?"
    if n == 3 and "trei" not in s.lower():
        if s.startswith("Care "):
            return s.replace("Care ", "Care trei ", 1)
        return f"Care trei elemente se aplică: {s.rstrip('?')}?"
    if n == 4 and "patru" not in s.lower() and "toate" not in s.lower():
        if s.startswith("Care "):
            return s.replace("Care ", "Care patru ", 1)
    return stem if isinstance(stem, tuple) else s


def convert(item: Item, target: int) -> Item:
    if item.get("tf"):
        return item
    it = deepcopy(item)
    opts = list(it.get("options") or [])
    if len(opts) != 4:
        return it
    cur = "".join(sorted(set(x for x in (it.get("correct") or "abd").lower() if x in "abcd")))
    if target == 4:
        it["correct"] = "abcd"
        return it
    if len(cur) > target:
        cur = cur[:target]
    elif len(cur) < target:
        for ch in "abcd":
            if ch not in cur:
                cur += ch
            if len(cur) == target:
                break
    drop = [x for x in "abcd" if x not in cur]
    if "d" in drop:
        idx = abs(hash(flatten_stem(it["stem"]))) % len(DISTRACTORS)
        opts[3] = DISTRACTORS[idx]
    it["options"] = opts
    it["correct"] = cur
    new_stem = stem_for(target, it["stem"])
    if isinstance(it["stem"], tuple) and isinstance(new_stem, str):
        it["stem"] = tuple(textwrap.wrap(new_stem, width=72))
    else:
        it["stem"] = new_stem
    return it


def fmt_stem(stem: Any, indent: str) -> List[str]:
    if isinstance(stem, tuple):
        lines = [f'{indent}    "stem": (']
        for part in stem:
            esc = part.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{indent}        "{esc}"')
        lines.append(f"{indent}    ),")
        return lines
    esc = str(stem).replace("\\", "\\\\").replace('"', '\\"')
    return [f'{indent}    "stem": "{esc}",']


def fmt_item(item: Item, indent: str = "    ") -> str:
    lines = [f"{indent}{{"]
    lines.extend(fmt_stem(item["stem"], indent))
    if "options" in item:
        lines.append(f'{indent}    "options": [')
        for opt in item["options"]:
            esc = opt.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{indent}        "{esc}",')
        lines.append(f"{indent}    ],")
    if "correct" in item:
        lines.append(f'{indent}    "correct": "{item["correct"]}",')
    if item.get("tf"):
        lines.append(f'{indent}    "tf": True,')
        lines.append(f'{indent}    "correct_tf": {"True" if item.get("correct_tf") else "False"},')
    lines.append(f"{indent}}},")
    return "\n".join(lines)


def compute_assignments(rel: str, var: str, tgt: Tuple[int, int, int, int, int], quads: List[int]) -> Dict[int, int]:
    from scripts._apply_ii_rebalance import assign, letter_count

    path = ROOT / rel
    items = load_items(path, var)
    targets = assign(items, tgt, set(quads))
    return {i: targets[i] for i, t in enumerate(targets) if t and not items[i].get("tf")}


def populate_assignments() -> None:
    from scripts._apply_ii_rebalance import SPECS

    out: List[Tuple[str, str, Dict[int, int]]] = []
    for rel, var, tgt, quads, skip in SPECS:
        if skip:
            continue
        mapping = compute_assignments(rel, var, tgt, quads)
        out.append((rel, var, mapping))
    ASSIGNMENTS.clear()
    ASSIGNMENTS.extend(out)


def patch_file(rel: str, var: str, mapping: Dict[int, int]) -> None:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    items = load_items(path, var)
    new_items = []
    for i, it in enumerate(items):
        if it.get("tf"):
            new_items.append(it)
        elif i in mapping:
            new_items.append(convert(it, mapping[i]))
        else:
            new_items.append(it)
    marker = f"{var}: List[Item] = ["
    start = text.index(marker)
    end = text.index("\n]", start) + 2
    body = marker + "\n" + "\n".join(fmt_item(x) for x in new_items) + "\n]"
    path.write_text(text[:start] + body + text[end:], encoding="utf-8")
    print(f"Patched {rel}")


def main() -> None:
    populate_assignments()
    for rel, var, mapping in ASSIGNMENTS:
        patch_file(rel, var, mapping)


if __name__ == "__main__":
    main()
