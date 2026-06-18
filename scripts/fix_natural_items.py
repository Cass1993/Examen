"""Aplică reformularea naturală pe fișierele băncii."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import build_index, fix_items_batch  # noqa: E402
from scripts.label_definition_index import build_label_definition_index  # noqa: E402
from scripts.natural_items import reformulate_item  # noqa: E402
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

TARGETS = [
    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
    APP_DIR / "questions_3400_merged.json",
    APP_DIR / "data" / "questions.json",
]


def patch_bank(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        return 0
    count = 0
    for i, item in enumerate(data):
        fixed, changed = reformulate_item(item)
        if changed:
            count += 1
            data[i] = fixed
    data, _ = fix_items_batch(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {count} itemi reformulați natural")
    return count


def patch_lots(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    refs = []
    for lot_name, lot_data in (data.get("lots") or {}).items():
        for q in lot_data.get("questions", []):
            rows.append(
                {
                    "id": q.get("id"),
                    "text": q.get("text"),
                    "options": q.get("options"),
                    "correct": q.get("correct"),
                    "domeniu": lot_name,
                }
            )
            refs.append(q)
    index = build_index(rows)
    label_map = build_label_definition_map(rows)
    label_index = build_label_definition_index(rows)
    count = 0
    for q, row in zip(refs, rows):
        polished = polish_question_item(row, index, label_map, label_index)
        if polished.get("text") != q.get("text") or polished.get("options") != q.get("options"):
            count += 1
        q["text"] = polished.get("text", q.get("text"))
        q["options"] = polished.get("options", q.get("options"))
        if polished.get("correct"):
            q["correct"] = polished["correct"]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {count} itemi reformulați natural")
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
