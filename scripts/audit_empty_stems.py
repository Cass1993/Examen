"""Raportează itemi fără enunț după polish (runtime)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import build_index
from scripts.label_definition_index import build_label_definition_index
from scripts.polish_text import polish_question_item, _item_stem
from scripts.upgrade_tf_items import build_label_definition_map

DATA = APP_DIR / "data" / "questions.json"
REPORT = APP_DIR / "audit_report_empty_stems.txt"


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    rows = []
    for lot_name, lot_data in (data.get("lots") or {}).items():
        for q in lot_data.get("questions") or []:
            rows.append(
                {
                    "id": q.get("id"),
                    "text": q.get("text"),
                    "options": q.get("options"),
                    "correct": q.get("correct"),
                    "domeniu": lot_name,
                }
            )

    index = build_index(rows)
    label_map = build_label_definition_map(rows)
    label_index = build_label_definition_index(rows)

    empty_after = []
    for raw in rows:
        original = str(raw.get("text") or "").strip()
        fixed = polish_question_item(dict(raw), index, label_map, label_index)
        stem = _item_stem(fixed)
        if not stem:
            empty_after.append(
                {
                    "id": raw.get("id"),
                    "lot": raw.get("domeniu"),
                    "original": original[:120],
                }
            )

    lines = [
        "=" * 72,
        "AUDIT ENUNȚURI GOALE DUPĂ POLISH",
        "=" * 72,
        f"Total itemi: {len(rows)}",
        f"Fără enunț după polish: {len(empty_after)}",
        "",
    ]
    for entry in empty_after[:50]:
        lines.append(f"  id={entry['id']} lot={entry['lot']}")
        lines.append(f"    original: {entry['original']}")
    if len(empty_after) > 50:
        lines.append(f"  ... și încă {len(empty_after) - 50}")
    lines.append("=" * 72)

    text = "\n".join(lines)
    REPORT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
