"""Explicații pedagogice — lot examen Psihologia muncii II (470 itemi)."""

from __future__ import annotations

from typing import List

from scripts.pm_ii_explanations_part1 import PART1_EXPLANATIONS
from scripts.pm_ii_explanations_part2 import PART2_EXPLANATIONS
from scripts.pm_ii_explanations_part3 import PART3_EXPLANATIONS
from scripts.pm_ii_explanations_part4 import PART4_EXPLANATIONS

PSIHOLOGIA_MUNCII_EXPLANATIONS: List[str] = (
    PART1_EXPLANATIONS
    + PART2_EXPLANATIONS
    + PART3_EXPLANATIONS
    + PART4_EXPLANATIONS
)

assert len(PSIHOLOGIA_MUNCII_EXPLANATIONS) == 470, len(PSIHOLOGIA_MUNCII_EXPLANATIONS)


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (9501–9970), independent de questions.json."""
    if 9501 <= int(item_id) <= 9970:
        idx = int(item_id) - 9501
        if 0 <= idx < len(PSIHOLOGIA_MUNCII_EXPLANATIONS):
            return PSIHOLOGIA_MUNCII_EXPLANATIONS[idx]
    return ""


def attach_explanations(items: list) -> list:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOLOGIA_MUNCII_EXPLANATIONS):
            item["explanation"] = PSIHOLOGIA_MUNCII_EXPLANATIONS[i]
        out.append(item)
    return out
