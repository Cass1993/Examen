"""Rulează remedierea completă a băncii și scrie raport în data/."""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

REPORT = APP_DIR / "data" / "comprehensive_fix_report.txt"


def main() -> None:
    lines: list[str] = []
    try:
        from scripts.apply_all_bank_fixes import (
            BANK_FIX_VERSION,
            ensure_bank_fixed,
            process_bank_data,
        )
        from scripts.audit_item_quality import walk_items
        from scripts.association_pair_fix import (
            is_broken_association_item,
            needs_association_fix,
        )
        from scripts.fix_admin_list_items import is_admin_list_item
        from scripts.fix_malformed_flashcard import is_malformed_flashcard_item

        bank = APP_DIR / "data" / "questions.json"
        marker_dir = APP_DIR / "data"
        marker = marker_dir / f".bank_fix_{BANK_FIX_VERSION}"
        for old in marker_dir.glob(".bank_fix_*"):
            if old.name != f".bank_fix_{BANK_FIX_VERSION}":
                old.unlink(missing_ok=True)
        if marker.exists():
            marker.unlink()

        data_before = json.loads(bank.read_text(encoding="utf-8"))
        before = {
            "malformed_flashcard": sum(
                1 for _, q in walk_items(data_before) if is_malformed_flashcard_item(q)
            ),
            "admin_list": sum(1 for _, q in walk_items(data_before) if is_admin_list_item(q)),
            "broken_assoc": sum(
                1 for _, q in walk_items(data_before) if is_broken_association_item(q)
            ),
            "needs_assoc": sum(
                1 for _, q in walk_items(data_before) if needs_association_fix(q)
            ),
        }

        count = ensure_bank_fixed(bank, APP_DIR / "data")

        data_after = json.loads(bank.read_text(encoding="utf-8"))
        after = {
            "malformed_flashcard": sum(
                1 for _, q in walk_items(data_after) if is_malformed_flashcard_item(q)
            ),
            "admin_list": sum(1 for _, q in walk_items(data_after) if is_admin_list_item(q)),
            "broken_assoc": sum(
                1 for _, q in walk_items(data_after) if is_broken_association_item(q)
            ),
            "needs_assoc": sum(
                1 for _, q in walk_items(data_after) if needs_association_fix(q)
            ),
        }

        lines.extend(
            [
                f"Bank fix v{BANK_FIX_VERSION}",
                f"Items changed: {count}",
                f"Before: {before}",
                f"After: {after}",
                "OK",
            ]
        )
    except Exception:
        lines.append("ERROR")
        lines.append(traceback.format_exc())

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
