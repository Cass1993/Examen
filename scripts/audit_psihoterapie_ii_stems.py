#!/usr/bin/env python3
"""Audit enunțuri Psihoterapie II — raportează formulări problematice."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.psihoterapie_ii_bank_data import ITEMS  # noqa: E402
from scripts.psihoterapie_ii_option_polish import polish_bank_row  # noqa: E402
from scripts.psihoterapie_ii_stem_quality import audit_all_stems, validate_stem  # noqa: E402


def main() -> int:
    raw_stems = [str(row.get("stem") or "") for row in ITEMS]
    polished = [polish_bank_row(row)["stem"] for row in ITEMS]

    print(f"Total itemi: {len(ITEMS)}")
    print()

    raw_issues = audit_all_stems(raw_stems)
    if raw_issues:
        print(f"=== Surse brute: {len(raw_issues)} probleme ===")
        for idx, stem, issues in raw_issues[:30]:
            print(f"  [{idx + 1}] {issues}")
            print(f"       {stem[:120]}")
        if len(raw_issues) > 30:
            print(f"  ... și încă {len(raw_issues) - 30}")
        print()

    post_issues: list[tuple[int, str, list[str]]] = []
    for i, stem in enumerate(polished):
        issues = validate_stem(stem)
        if issues:
            post_issues.append((i, stem, issues))

    if post_issues:
        print(f"=== După polish: {len(post_issues)} probleme ===")
        for idx, stem, issues in post_issues:
            print(f"  [{idx + 1}] {issues}")
            print(f"       {stem[:120]}")
        return 1

    print("OK — niciun enunț problematic după polish.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
