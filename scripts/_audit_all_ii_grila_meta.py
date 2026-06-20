"""Audit meta-limbaj „grilă” în enunțuri — toate loturile II."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.ii_grila_meta_audit import find_grila_meta_in_stems  # noqa: E402

II_LOTS = (
    ("Psihologia învățării II", "scripts.psihologia_invatarii_ii_exam_items"),
    ("Psihologia dezvoltării II", "scripts.psihologia_dezvoltarii_ii_exam_items"),
    ("Psihologia muncii II", "scripts.psihologia_muncii_ii_exam_items"),
    ("Psihoterapie II", "scripts.psihoterapie_ii_exam_items"),
    ("Psihopatologie II", "scripts.psihopatologie_ii_exam_items"),
    ("Evaluare psihologică II", "scripts.evaluare_psihologica_ii_exam_items"),
    ("Statistică II", "scripts.statistica_ii_exam_items"),
)


def main() -> int:
    total = 0
    for label, module_path in II_LOTS:
        mod = __import__(module_path, fromlist=["build_items"])
        items = mod.build_items()
        lot_issues = find_grila_meta_in_stems(items)
        if lot_issues:
            print(f"\n=== {label} ({len(lot_issues)} probleme) ===")
            for line in lot_issues:
                print(line)
            total += len(lot_issues)
        else:
            print(f"OK: {label} ({len(items)} itemi)")

    if total:
        print(f"\nTotal: {total} enunțuri cu meta-referință grilă.")
        return 1
    print("\nToate loturile II: fără meta-limbaj grilă în enunțuri.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
