"""Itemi examen — Epigenetica II: BAZE MOLECULARE (210 itemi, ID 11726–11935)."""

from __future__ import annotations

from typing import Dict, List, Tuple

from scripts.exam_item_utils import build_items_from_bank

LOT_NAME = "Epigenetica II: BAZE MOLECULARE"
START_ID = 11726


def build_items() -> List[Dict]:
    from scripts.epigenetica_ii_baze_moleculare_bank_data import BAZE_MOLECULARE_ITEMS
    from scripts.epigenetica_ii_baze_moleculare_explanations import (
        BAZE_MOLECULARE_EXPLANATIONS,
    )
    from scripts.epigenetica_ii_patologii_genetice_bank_data import (
        PATOLOGII_GENETICE_ITEMS,
    )
    from scripts.epigenetica_ii_patologii_genetice_explanations import (
        PATOLOGII_GENETICE_EXPLANATIONS,
    )
    from scripts.epigenetica_ii_genetica_comportamentala_bank_data import (
        GENETICA_COMPORTAMENTALA_ITEMS,
    )
    from scripts.epigenetica_ii_genetica_comportamentala_explanations import (
        GENETICA_COMPORTAMENTALA_EXPLANATIONS,
    )
    from scripts.epigenetica_ii_epigenetica_bank_data import EPIGENETICA_ITEMS
    from scripts.epigenetica_ii_epigenetica_explanations import (
        EPIGENETICA_EXPLANATIONS,
    )
    from scripts.epigenetica_ii_psihologie_legatura_bank_data import (
        PSIHOLOGIE_LEGATURA_ITEMS,
    )
    from scripts.epigenetica_ii_psihologie_legatura_explanations import (
        PSIHOLOGIE_LEGATURA_EXPLANATIONS,
    )

    segments: List[Tuple[List[Dict], List[str]]] = [
        (BAZE_MOLECULARE_ITEMS, BAZE_MOLECULARE_EXPLANATIONS),
        (PATOLOGII_GENETICE_ITEMS, PATOLOGII_GENETICE_EXPLANATIONS),
        (GENETICA_COMPORTAMENTALA_ITEMS, GENETICA_COMPORTAMENTALA_EXPLANATIONS),
        (EPIGENETICA_ITEMS, EPIGENETICA_EXPLANATIONS),
        (PSIHOLOGIE_LEGATURA_ITEMS, PSIHOLOGIE_LEGATURA_EXPLANATIONS),
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
