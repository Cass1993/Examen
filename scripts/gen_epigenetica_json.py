"""Generează data/epigenetica_items.json din scripts/epigenetica_bank_data.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP))

from scripts.epigenetica_bank_data import ITEMS  # noqa: E402

OUT = APP / "data" / "epigenetica_items.json"


def main() -> None:
    OUT.write_text(json.dumps(ITEMS, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(ITEMS)} items to {OUT}")


if __name__ == "__main__":
    main()
