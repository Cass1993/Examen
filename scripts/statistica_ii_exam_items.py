"""Itemi examen — Statistică II."""

from __future__ import annotations

from typing import Dict, List

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Statistică II"
START_ID = 10961


def build_items() -> List[Dict]:
    from scripts.statistica_ii_explanations import attach_explanations
    from scripts.statistica_ii_bank_data import STATISTICA_II_ITEMS

    raw = attach_explanations(list(STATISTICA_II_ITEMS))
    return build_items_from_bank(raw, START_ID, LOT_NAME)


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
