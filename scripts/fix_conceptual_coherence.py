"""Rescriere coerență conceptuală pe questions.json + audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_item_quality import walk_items  # noqa: E402
from scripts.distractor_fix import build_index  # noqa: E402
from scripts.association_pair_fix import fix_association_pairs  # noqa: E402
from scripts.rewrite_conceptual_coherence import (  # noqa: E402
    audit_bank_coherence,
    format_coherence_report,
    rewrite_item_coherence,
)

TARGETS = [
    APP_DIR / "data" / "questions.json",
    APP_DIR / "questions_clean.json",
]


def process(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for lot, item in walk_items(data):
        row = dict(item)
        row["domeniu"] = lot
        row["lot"] = lot
        rows.append(row)
    index = build_index(rows)

    changed = 0
    if "lots" in data:
        for _pass in range(3):
            pass_changed = 0
            for lot_name, lot_data in data["lots"].items():
                for i, q in enumerate(lot_data.get("questions", [])):
                    q2, ch0 = fix_association_pairs(q)
                    fixed, ch = rewrite_item_coherence(q2, index, lot_name)
                    if ch0 or ch:
                        lot_data["questions"][i] = fixed
                        pass_changed += 1
            changed += pass_changed
            if pass_changed == 0:
                break

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    report = audit_bank_coherence(data)
    audit_path = path.parent / f"audit_report_conceptual_{path.stem}.txt"
    audit_path.write_text(format_coherence_report(report), encoding="utf-8")

    print(f"{path.name}: {changed} itemi rescriși")
    print(format_coherence_report(report))
    print(f"Audit: {audit_path}")
    return changed


def main() -> None:
    total = sum(process(p) for p in TARGETS)
    print(f"Total modificări: {total}")


if __name__ == "__main__":
    main()
