"""Rescrie lotul Epigenetica II: BAZE MOLECULARE în questions_archive.json."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.epigenetica_ii_baze_moleculare_exam_items import LOT_NAME, build_items
from scripts.lot_archive import write_lot_to_store

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    built = build_items()
    write_lot_to_store(LOT_NAME, built, QUESTIONS_JSON)
    with_expl = sum(1 for q in built if str(q.get("explanation") or "").strip())
    print(f"Lot: {LOT_NAME}")
    print(f"Scriere arhivă: {len(built)} itemi (cu explicație: {with_expl})")
    print(f"11856: {str(built[130].get('text', ''))[:70]}...")
    print(f"11906: {str(built[180].get('text', ''))[:70]}...")
    print(f"11935: {str(built[-1].get('text', ''))[:70]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
