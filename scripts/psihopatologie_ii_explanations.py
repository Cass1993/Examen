"""Explicații pedagogice — lot examen Psihopatologie II (360 itemi, ID 8001–8360)."""

from __future__ import annotations

from typing import List

from scripts.psihopatologie_ii_expl_part1 import PART1_EXPLANATIONS
from scripts.psihopatologie_ii_expl_part2 import PART2_EXPLANATIONS
from scripts.psihopatologie_ii_expl_part3 import PART3_EXPLANATIONS
from scripts.psihopatologie_ii_expl_part4 import PART4_EXPLANATIONS

PSIHOPATOLOGIE_II_EXPLANATIONS: List[str] = (
    PART1_EXPLANATIONS
    + PART2_EXPLANATIONS
    + PART3_EXPLANATIONS
    + PART4_EXPLANATIONS
)

assert len(PSIHOPATOLOGIE_II_EXPLANATIONS) == 360, len(PSIHOPATOLOGIE_II_EXPLANATIONS)

EXAM_ID_START = 8001
EXAM_ID_END = 8360


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (8001–8360)."""
    if EXAM_ID_START <= int(item_id) <= EXAM_ID_END:
        idx = int(item_id) - EXAM_ID_START
        if 0 <= idx < len(PSIHOPATOLOGIE_II_EXPLANATIONS):
            return PSIHOPATOLOGIE_II_EXPLANATIONS[idx]
    return ""


def attach_explanations(items: list) -> list:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOPATOLOGIE_II_EXPLANATIONS):
            item["explanation"] = PSIHOPATOLOGIE_II_EXPLANATIONS[i]
        out.append(item)
    return out
