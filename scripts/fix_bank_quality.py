"""Repară banca + raport audit înainte/după."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_item_quality import audit_bank, print_report  # noqa: E402
from scripts.fix_all_distractors import TARGETS, patch_bank, patch_lots  # noqa: E402

REPORT_PATH = APP_DIR / "data" / "audit_item_quality_report.json"
QUESTIONS_PATH = APP_DIR / "data" / "questions.json"


def main() -> None:
    print("=== AUDIT ÎNAINTE ===")
    before = audit_bank(QUESTIONS_PATH)
    print_report(before)

    total = 0
    for path in TARGETS:
        if path.name == "questions.json":
            total += patch_lots(path)
        else:
            total += patch_bank(path)
    print(f"\nTotal itemi modificați: {total}")

    print("\n=== AUDIT DUPĂ ===")
    after = audit_bank(QUESTIONS_PATH)
    print_report(after)
    REPORT_PATH.write_text(
        json.dumps({"before": before, "after": after}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nRaport salvat: {REPORT_PATH}")


if __name__ == "__main__":
    main()
