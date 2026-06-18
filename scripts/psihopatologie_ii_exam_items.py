"""Itemi examen — Psihopatologie II."""

from __future__ import annotations

from typing import Dict, List

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Psihopatologie II"
START_ID = 8001


def _load_raw():
    from pathlib import Path
    import json

    data_path = (
        Path(__file__).resolve().parent.parent / "data" / "psihopatologie_ii_items.json"
    )
    if data_path.exists():
        return json.loads(data_path.read_text(encoding="utf-8"))
    from scripts.psihopatologie_ii_bank_data import ITEMS

    return ITEMS


def build_items() -> List[Dict]:
    from scripts.psihopatologie_ii_option_polish import polish_bank_row

    raw = _load_raw()
    polished = [polish_bank_row(row) for row in raw]
    return build_items_from_bank(polished, START_ID, LOT_NAME)


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
