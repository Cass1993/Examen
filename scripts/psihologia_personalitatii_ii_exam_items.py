"""Itemi examen — Psihologia personalității II (290 itemi, ID 11936–12225)."""

from __future__ import annotations

from typing import Dict, List, Tuple

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Psihologia personalității II"
START_ID = 11936


def build_items() -> List[Dict]:
    from scripts.psihologia_personalitatii_ii_ce_este_bank_data import (
        CE_ESTE_PERSONALITATEA_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_ce_este_explanations import (
        CE_ESTE_PERSONALITATEA_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_psihodinamica_freud_bank_data import (
        PSIHODINAMICA_FREUD_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_psihodinamica_freud_explanations import (
        PSIHODINAMICA_FREUD_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_neo_psihanalitica_bank_data import (
        NEO_PSIHANALITICA_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_neo_psihanalitica_explanations import (
        NEO_PSIHANALITICA_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_dispozitionala_trasaturi_bank_data import (
        DISPOZITIONALA_TRASATURI_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_dispozitionala_trasaturi_explanations import (
        DISPOZITIONALA_TRASATURI_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_fenomenologica_bank_data import (
        FENOMENOLOGICA_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_fenomenologica_explanations import (
        FENOMENOLOGICA_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_comportamentala_bank_data import (
        COMPORTAMENTALA_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_comportamentala_explanations import (
        COMPORTAMENTALA_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_social_cognitiva_bank_data import (
        SOCIAL_COGNITIVA_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_social_cognitiva_explanations import (
        SOCIAL_COGNITIVA_EXPLANATIONS,
    )
    from scripts.psihologia_personalitatii_ii_comparativ_capcane_bank_data import (
        COMPARATIV_CAPCANE_ITEMS,
    )
    from scripts.psihologia_personalitatii_ii_comparativ_capcane_explanations import (
        COMPARATIV_CAPCANE_EXPLANATIONS,
    )

    segments: List[Tuple[List[Dict], List[str]]] = [
        (CE_ESTE_PERSONALITATEA_ITEMS, CE_ESTE_PERSONALITATEA_EXPLANATIONS),
        (PSIHODINAMICA_FREUD_ITEMS, PSIHODINAMICA_FREUD_EXPLANATIONS),
        (NEO_PSIHANALITICA_ITEMS, NEO_PSIHANALITICA_EXPLANATIONS),
        (DISPOZITIONALA_TRASATURI_ITEMS, DISPOZITIONALA_TRASATURI_EXPLANATIONS),
        (FENOMENOLOGICA_ITEMS, FENOMENOLOGICA_EXPLANATIONS),
        (COMPORTAMENTALA_ITEMS, COMPORTAMENTALA_EXPLANATIONS),
        (SOCIAL_COGNITIVA_ITEMS, SOCIAL_COGNITIVA_EXPLANATIONS),
        (COMPARATIV_CAPCANE_ITEMS, COMPARATIV_CAPCANE_EXPLANATIONS),
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
