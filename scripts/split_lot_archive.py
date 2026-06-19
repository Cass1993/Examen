"""Mută loturile fără II din questions.json în data/questions_archive.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lot_archive import (
    archive_path_for,
    ensure_archive_split,
    is_ii_lot,
    load_archive,
    split_lots,
)
from scripts.supplemental_lots import ensure_all_supplemental_lots

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    if not QUESTIONS_JSON.exists():
        print(f"Lipseste {QUESTIONS_JSON}")
        return 1

    data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    data = ensure_all_supplemental_lots(data, QUESTIONS_JSON)
    ensure_archive_split(QUESTIONS_JSON)

    active = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    archive = load_archive(archive_path_for(QUESTIONS_JSON))
    active_lots = active.get("lots") or {}
    archive_lots = archive.get("lots") or {}

    print("=== Separare loturi II / arhiva ===")
    print(f"\nActive (Alege loturile) — {len(active_lots)} loturi:")
    for name in sorted(active_lots):
        n = len(active_lots[name].get("questions") or [])
        print(f"  {name}: {n}")

    print(f"\nArhiva — {len(archive_lots)} loturi:")
    for name in sorted(archive_lots):
        n = len(archive_lots[name].get("questions") or [])
        print(f"  {name}: {n}")

    stray = [n for n in active_lots if not is_ii_lot(n)]
    if stray:
        print("\nATENTIE: inca in questions.json (non-II):")
        for name in stray:
            print(f"  - {name}")
        return 1

    print("\nOK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
