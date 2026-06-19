"""Apply answer-distribution rebalance to Psihologia dezvoltarii II bank_data files."""
from __future__ import annotations

import re
import textwrap
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
Item = Dict[str, Any]

SPECS: List[Tuple[str, str, Tuple[int, int, int, int, int], List[int], bool]] = [
    ("scripts/psihologia_dezvoltarii_ii_tinereete_bank_data.py", "TINERETE_ITEMS", (14, 11, 8, 3, 4), [0, 13, 22], True),
    ("scripts/psihologia_dezvoltarii_ii_adolescenta_bank_data.py", "ADOLESCENTA_ITEMS", (14, 11, 8, 3, 4), [5, 22, 35], True),
    ("scripts/psihologia_dezvoltarii_ii_scolaritate_bank_data.py", "SCOLARITATE_ITEMS", (14, 11, 8, 3, 4), [0, 12, 35], True),
    ("scripts/psihologia_dezvoltarii_ii_simbol_joc_bank_data.py", "SIMBOL_JOC_ITEMS", (14, 11, 8, 3, 4), [4, 13, 33], True),
    ("scripts/psihologia_dezvoltarii_ii_limbaj_bank_data.py", "LIMBAJ_ITEMS", (10, 8, 6, 3, 3), [0, 9, 24], True),
    ("scripts/psihologia_dezvoltarii_ii_atasament_bank_data.py", "ATASAMENT_ITEMS", (10, 8, 6, 3, 3), [6, 14, 25], True),
    ("scripts/psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py", "SENZORIO_MOTOR_ITEMS", (14, 11, 8, 3, 4), [0, 11, 37], True),
    ("scripts/psihologia_dezvoltarii_ii_teorii_bank_data.py", "TEORII_INVATARII_ITEMS", (14, 11, 8, 3, 4), [0, 4, 36], True),
    ("scripts/psihologia_dezvoltarii_ii_metode_bank_data.py", "METODE_CERCETARE_ITEMS", (17, 13, 11, 4, 5), [19, 38, 47], False),
    ("scripts/psihologia_dezvoltarii_ii_bank_data.py", "PSIHOLOGIA_DEZVOLTARII_II_ITEMS", (17, 13, 11, 4, 5), [1, 7, 44], True),
]

DISTRACTORS = [
    "stadiul senzorio-motor cu reflexe dominante",
    "operații formale abstracte ca la adolescent",
    "revenirea la dependența totală de părinți",
    "exclusiv senzorio-motor, fără componentă afectivă",
    "dispariția completă a atașamentului și a intimității",
    "absența oricărei influențe a mediului social",
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


def letter_count(item: Item) -> int:
    if item.get("tf"):
        return 0
    c = (item.get("correct") or "").lower()
    return len("".join(sorted(set(x for x in c if x in "abcd"))))


def convert(item: Item, target: int, keep_quad: bool) -> Item:
    if item.get("tf"):
        return item
    it = deepcopy(item)
    opts = list(it.get("options") or [])
    if len(opts) != 4:
        return it
    cur = "".join(sorted(set(x for x in (it.get("correct") or "abd").lower() if x in "abcd")))
    if keep_quad or target == 4:
        it["correct"] = "abcd" if target == 4 else cur[:4]
        if len(it["correct"]) < 4:
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
    elif "c" in drop:
        idx = abs(hash(flatten_stem(it["stem"]) + "c")) % len(DISTRACTORS)
        opts[2] = DISTRACTORS[idx]
    it["options"] = opts
    it["correct"] = cur
    new_stem = stem_for(target, it["stem"])
    if isinstance(it["stem"], tuple) and isinstance(new_stem, str):
        it["stem"] = tuple(textwrap.wrap(new_stem, width=72))
    else:
        it["stem"] = new_stem
    return it


def assign(items: List[Item], tgt: Tuple[int, int, int, int, int], quads: set[int]) -> List[int]:
    t1, t2, t3, t4, _ttf = tgt
    mc = [i for i, x in enumerate(items) if not x.get("tf")]
    out = [0] * len(items)
    valid_quads = {i for i in quads if i in mc}
    assigned: Dict[int, int] = {i: 4 for i in valid_quads}
    pool = [i for i in mc if i not in assigned]
    pool.sort(key=lambda i: (-letter_count(items[i]), i))
    buckets = {4: max(0, t4 - len(assigned)), 3: t3, 2: t2, 1: t1}
    for n in (3, 2, 1):
        for i in list(pool):
            if buckets[n] <= 0:
                break
            if i in assigned:
                continue
            assigned[i] = n
            pool.remove(i)
            buckets[n] -= 1
    while buckets[4] > 0 and pool:
        assigned[pool.pop(0)] = 4
        buckets[4] -= 1
    # restante → răspuns simplu (cel mai frecvent)
    for i in pool:
        assigned[i] = 1
    for i in mc:
        out[i] = assigned.get(i, 1)
    return out


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


def patch(rel: str, var: str, tgt: Tuple[int, int, int, int, int], quads: List[int], skip: bool) -> None:
    if skip:
        print(f"Skip {rel}")
        return
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    items = load_items(path, var)
    targets = assign(items, tgt, set(quads))
    new_items = [
        it if it.get("tf") else convert(it, targets[i], i in set(quads))
        for i, it in enumerate(items)
    ]
    marker = f"{var}: List[Item] = ["
    start = text.index(marker)
    end = text.index("\n]", start) + 2
    body = marker + "\n" + "\n".join(fmt_item(x) for x in new_items) + "\n]"
    path.write_text(text[:start] + body + text[end:], encoding="utf-8")
    print(f"Patched {rel}")


def main() -> None:
    for rel, var, tgt, quads, skip in SPECS:
        patch(rel, var, tgt, quads, skip)


if __name__ == "__main__":
    main()
