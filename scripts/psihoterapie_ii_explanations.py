"""Explicații pedagogice — lot Psihoterapie II (858 itemi, ID 7001–7858)."""

from __future__ import annotations

from typing import List

from scripts.psihoterapie_ii_expl_part1 import PART1_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part2 import PART2_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part3 import PART3_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part4 import PART4_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part5 import PART5_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part6 import PART6_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part7 import PART7_EXPLANATIONS
from scripts.psihoterapie_ii_expl_part8 import PART8_EXPLANATIONS

PSIHOTERAPIE_II_EXPLANATIONS: List[str] = (
    PART1_EXPLANATIONS
    + PART2_EXPLANATIONS
    + PART3_EXPLANATIONS
    + PART4_EXPLANATIONS
    + PART5_EXPLANATIONS
    + PART6_EXPLANATIONS
    + PART7_EXPLANATIONS
    + PART8_EXPLANATIONS
)

assert len(PSIHOTERAPIE_II_EXPLANATIONS) == 858, len(PSIHOTERAPIE_II_EXPLANATIONS)

EXAM_ID_START = 7001
EXAM_ID_END = 7858


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (7001–7858)."""
    if EXAM_ID_START <= int(item_id) <= EXAM_ID_END:
        idx = int(item_id) - EXAM_ID_START
        if 0 <= idx < len(PSIHOTERAPIE_II_EXPLANATIONS):
            return PSIHOTERAPIE_II_EXPLANATIONS[idx]
    return ""


def attach_explanations(items: list) -> list:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOTERAPIE_II_EXPLANATIONS):
            item["explanation"] = PSIHOTERAPIE_II_EXPLANATIONS[i]
        out.append(item)
    return out
