"""Itemi conceptuali pentru enunțuri neterminate (fost A/F)."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.concept_clusters import rotate_options

ConceptSpec = Dict[str, Any]

# potrivire fragment enunț (normalizat) → item conceptual
INCOMPLETE_SPECS: List[Tuple[re.Pattern[str], ConceptSpec]] = [
    (
        re.compile(r"orientarea centrat[aă] pe persoan[aă]", re.I),
        {
            "stem": "În abordarea umanistă a învățării, orientarea centrată pe persoană este asociată mai ales cu:",
            "options": {
                "a": "Carl R. Rogers și accentul pus pe experiența subiectivă, autonomie și climat suportiv",
                "b": "B. F. Skinner și controlul comportamentului prin întăriri externe",
                "c": "Ivan P. Pavlov și asocierea dintre stimul condiționat și răspuns reflex",
                "d": "Jean Piaget și succesiunea stadiilor dezvoltării cognitive",
            },
            "correct": "a",
        },
    ),
    (
        re.compile(r"teoria ata[sș]amentului", re.I),
        {
            "stem": "În psihologia dezvoltării timpurii, teoria atașamentului este asociată mai ales cu:",
            "options": {
                "a": "John Bowlby și legătura emoțională timpurie copil–îngrijitor",
                "b": "B. F. Skinner și condiționarea operantă prin consecințe",
                "c": "Jean Piaget și stadiile dezvoltării cognitive",
                "d": "Albert Bandura și învățarea prin observare",
            },
            "correct": "a",
        },
    ),
]


def lookup_incomplete_spec(stem: str) -> Optional[ConceptSpec]:
    low = re.sub(r"\s+", " ", (stem or "").strip().lower())
    for pat, spec in INCOMPLETE_SPECS:
        if pat.search(low):
            return spec
    return None


def build_from_spec(spec: ConceptSpec, seed: int) -> Tuple[str, Dict[str, str], List[str]]:
    stem, opts, letter = rotate_options(spec, seed)
    return stem, opts, [letter]
