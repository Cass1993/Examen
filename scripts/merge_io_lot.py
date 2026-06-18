"""Adaugă lotul «Psihologia organizațională/muncii» în questions.json."""

from __future__ import annotations

import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.i_o_exam_items import LOT_NAME, build_items, merge_into_bank  # noqa: E402


def main() -> None:
    bank = APP_DIR / "data" / "questions.json"
    n = merge_into_bank(str(bank))
    if n:
        print(f"Adăugat lot «{LOT_NAME}»: {n} itemi (id {build_items()[0]['id']}–{build_items()[-1]['id']})")
    else:
        print(f"Lotul «{LOT_NAME}» există deja.")


if __name__ == "__main__":
    main()
