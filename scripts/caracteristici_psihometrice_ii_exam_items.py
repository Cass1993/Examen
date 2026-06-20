"""Itemi examen — Caracteristici psihometrice II."""

from __future__ import annotations

from typing import Dict, List

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Caracteristici psihometrice II"
START_ID = 11246


def build_items() -> List[Dict]:
    from scripts.caracteristici_psihometrice_ii_explanations import (
        CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS,
    )
    from scripts.caracteristici_psihometrice_ii_bank_data import (
        CARACTERISTICI_PSIHOMETRICE_II_ITEMS,
    )

    raw: List[Dict] = []
    for i, row in enumerate(CARACTERISTICI_PSIHOMETRICE_II_ITEMS):
        item = dict(row)
        if i < len(CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS):
            item["explanation"] = CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS[i]
        raw.append(item)
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
