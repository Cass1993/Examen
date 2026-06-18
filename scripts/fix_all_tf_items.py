"""Aplică standardizarea A/F pe data/questions.json (+ opțional questions_clean.json)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_tf_items import audit_tf_bank, format_report  # noqa: E402
from scripts.audit_item_quality import walk_items  # noqa: E402
from scripts.fix_tf_items import fix_tf_item, is_tf_item  # noqa: E402

TARGETS = [
    APP_DIR / "data" / "questions.json",
    APP_DIR / "questions_clean.json",
]


def process_file(path: Path) -> int:
    if not path.exists():
        print(f"SKIP (lipsește): {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0

    if "lots" in data:
        for lot_name, lot_data in data.get("lots", {}).items():
            questions = lot_data.get("questions", [])
            for i, q in enumerate(questions):
                fixed, ch = fix_tf_item(q)
                if ch:
                    questions[i] = fixed
                    changed += 1
    elif isinstance(data, list):
        for i, q in enumerate(data):
            fixed, ch = fix_tf_item(q)
            if ch:
                data[i] = fixed
                changed += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tf_count = sum(1 for _, item in walk_items(data) if is_tf_item(item))
    issues = audit_tf_bank(data)
    report = format_report(issues, tf_count)
    audit_path = path.parent / f"audit_tf_{path.stem}.txt"
    audit_path.write_text(report, encoding="utf-8")

    print(f"{path.name}: {changed} itemi modificați")
    print(report)
    print(f"Audit: {audit_path}")
    return changed


def main() -> None:
    total = 0
    for path in TARGETS:
        total += process_file(path)
    print(f"Total modificări: {total}")


if __name__ == "__main__":
    main()
