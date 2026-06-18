"""Aplică pipeline-ul complet de calitate pe toate fișierele băncii."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import build_index  # noqa: E402
from scripts.label_definition_index import build_label_definition_index  # noqa: E402
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

TARGETS = [
    APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",
    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
    APP_DIR / "questions_3400_merged.json",
    APP_DIR / "data" / "questions.json",
]


def _to_row(item: dict, lot: str = "") -> dict:
    return {
        "id": item.get("id"),
        "intrebare": item.get("intrebare") or item.get("text"),
        "text": item.get("text") or item.get("intrebare"),
        "variante": item.get("variante") or item.get("options"),
        "options": item.get("options") or item.get("variante"),
        "raspuns_corect": item.get("raspuns_corect") or item.get("correct"),
        "correct": item.get("correct") or item.get("raspuns_corect"),
        "explicatie": item.get("explicatie") or item.get("explanation"),
        "explanation": item.get("explanation") or item.get("explicatie"),
        "kind": item.get("kind") or item.get("tip"),
        "tip": item.get("tip") or item.get("kind"),
        "domeniu": item.get("domeniu") or item.get("lot") or lot,
        "lot": item.get("lot") or item.get("domeniu") or lot,
    }


def _apply_row(item: dict, row: dict) -> bool:
    changed = False
    pairs = (
        ("intrebare", "intrebare"),
        ("text", "text"),
        ("variante", "variante"),
        ("options", "options"),
        ("raspuns_corect", "raspuns_corect"),
        ("correct", "correct"),
        ("explicatie", "explicatie"),
        ("explanation", "explanation"),
        ("kind", "kind"),
        ("tip", "tip"),
    )
    for src, dst in pairs:
        val = row.get(dst)
        if val is None:
            val = row.get(src)
        if val is not None and item.get(src) != val:
            item[src] = val
            changed = True
    return changed


def polish_batch(items: list[dict], passes: int = 3) -> tuple[list[dict], int]:
    changed = 0
    for _ in range(max(1, passes)):
        index = build_index(items)
        label_map = build_label_definition_map(items)
        label_index = build_label_definition_index(items)
        pass_changed = 0
        for item in items:
            row = _to_row(item)
            fixed = polish_question_item(row, index, label_map, label_index)
            if _apply_row(item, fixed):
                pass_changed += 1
        changed += pass_changed
    return items, changed


def patch_bank(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print(f"SKIP (format necunoscut): {path}")
        return 0
    _, count = polish_batch(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {count} itemi îmbunătățiți")
    return count


def patch_lots(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    lots = data.get("lots") or {}
    flat: list[dict] = []
    refs: list[dict] = []
    for lot_name, lot_data in lots.items():
        for q in lot_data.get("questions", []):
            row = _to_row(q, lot_name)
            flat.append(row)
            refs.append(q)

    _, count = polish_batch(flat)
    for q, row in zip(refs, flat):
        _apply_row(q, row)

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {count} itemi îmbunătățiți")
    return count


def main() -> None:
    total = 0
    for path in TARGETS:
        if path.name == "questions.json":
            total += patch_lots(path)
        else:
            total += patch_bank(path)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
