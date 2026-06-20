"""Itemi examen — Inventare de personalitate II."""

from __future__ import annotations

from typing import Dict, List

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Inventare de personalitate II"
START_ID = 11446


def build_items() -> List[Dict]:
    from scripts.inventare_personalitate_ii_cpi_bank_data import CPI_ITEMS
    from scripts.inventare_personalitate_ii_cpi_explanations import CPI_EXPLANATIONS
    from scripts.inventare_personalitate_ii_epq_bank_data import EPQ_IVE_ITEMS
    from scripts.inventare_personalitate_ii_epq_explanations import EPQ_IVE_EXPLANATIONS
    from scripts.inventare_personalitate_ii_fpi_bank_data import FPI_ITEMS
    from scripts.inventare_personalitate_ii_fpi_explanations import FPI_EXPLANATIONS
    from scripts.inventare_personalitate_ii_neo_bank_data import NEO_PI_R_ITEMS
    from scripts.inventare_personalitate_ii_neo_explanations import NEO_PI_R_EXPLANATIONS
    from scripts.inventare_personalitate_ii_comparatii_bank_data import COMPARATII_ITEMS
    from scripts.inventare_personalitate_ii_comparatii_explanations import COMPARATII_EXPLANATIONS

    segments = [
        (CPI_ITEMS, CPI_EXPLANATIONS),
        (EPQ_IVE_ITEMS, EPQ_IVE_EXPLANATIONS),
        (FPI_ITEMS, FPI_EXPLANATIONS),
        (NEO_PI_R_ITEMS, NEO_PI_R_EXPLANATIONS),
        (COMPARATII_ITEMS, COMPARATII_EXPLANATIONS),
    ]
    raw: List[Dict] = []
    for items, explanations in segments:
        for i, row in enumerate(items):
            item = dict(row)
            if i < len(explanations):
                item["explanation"] = explanations[i]
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
