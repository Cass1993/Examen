"""Rescrie lotul Psihologia personalității II în questions.json."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lot_archive import write_lot_to_store
from scripts.psihologia_personalitatii_ii_exam_items import LOT_NAME, build_items

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    built = build_items()
    write_lot_to_store(LOT_NAME, built, QUESTIONS_JSON)
    with_expl = sum(1 for q in built if str(q.get("explanation") or "").strip())
    print(f"Lot: {LOT_NAME}")
    print(f"Scriere: {len(built)} itemi (cu explicație: {with_expl})")
    print(f"11936: {str(built[0].get('text', ''))[:70]}...")
    print(f"11966: {str(built[30].get('text', ''))[:70]}...")
    print(f"12016: {str(built[80].get('text', ''))[:70]}...")
    print(f"12046: {str(built[110].get('text', ''))[:70]}...")
    print(f"12096: {str(built[160].get('text', ''))[:70]}...")
    print(f"12185: {str(built[249].get('text', ''))[:70]}...")
    print(f"12186: {str(built[250].get('text', ''))[:70]}...")
    print(f"12225: {str(built[-1].get('text', ''))[:70]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
