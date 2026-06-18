"""Itemi examen — Epigenetica (150 itemi: set principal 1–100 + recapitulare 151–200)."""
from __future__ import annotations
from typing import Dict, List, Tuple
from scripts.exam_item_utils import build_exam_item

LOT_NAME = "Epigenetica"
START_ID = 6001

_RAW: List[Tuple[str, Tuple[str, str, str, str], str]] = []


def _load_raw() -> List[Tuple[str, Tuple[str, str, str, str], str]]:
    from pathlib import Path
    import json

    app = Path(__file__).resolve().parent.parent
    data_path = app / "data" / "epigenetica_items.json"
    if data_path.exists():
        rows = json.loads(data_path.read_text(encoding="utf-8"))
        return [(r["stem"], tuple(r["options"]), r["correct"]) for r in rows]
    from scripts.epigenetica_bank_data import ITEMS

    return [(r["stem"], tuple(r["options"]), r["correct"]) for r in ITEMS]

def build_items() -> List[Dict]:
    return [
        build_exam_item(START_ID + i, stem, opts, correct, LOT_NAME)
        for i, (stem, opts, correct) in enumerate(_load_raw())
    ]

def merge_into_bank(bank_path: str) -> int:
    import json
    from pathlib import Path
    path = Path(bank_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    lots = data.setdefault("lots", {})
    if LOT_NAME in lots:
        return 0
    lots[LOT_NAME] = {"questions": build_items()}
    data["total_questions"] = sum(len(b.get("questions") or []) for b in lots.values())
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(build_items())
