"""Reguli de audit pentru enunțuri — Psihologia învățării II."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List

COUNT_STEM = re.compile(r"\bCare (patru|două|trei|doi|\d+)\b", re.IGNORECASE)
PSEUDO_ADJ = re.compile(
    r"\b(banduriene|bandurian|skinnerian|pavloviene|pavlovian|pavloviană|"
    r"tolmanian|thorndikian|rogersian|rogersiană|rogersiene|maslowian|maslowiane|"
    r"piagetian|piagetiană|watsonian)\b",
    re.IGNORECASE,
)
SPATIAL_GRID = re.compile(r"\b(din dreapta|din stânga|coloana dreaptă|coloana stângă)\b", re.I)
BAD_LINKED = re.compile(r"\bcorect legați\b", re.I)
ADVERB_ERROR = re.compile(
    r"\b(formulate|descrise|asociate|enumerate|menționate|evocate)\s+corecte\b",
    re.I,
)
# Stem cere „autori”, dar nu „perechi” — risc de nepotrivire cu variantele tip „Autor — idee”
AUTHOR_STEM_MISMATCH = re.compile(
    r"\bautori\b(?!.*\bperech)", re.I
)
DASH_PAIR_OPTION = re.compile(r"\s[—–-]\s")


@dataclass(frozen=True)
class StemIssue:
    rule: str
    message: str


def audit_stem(stem: str, options: Iterable[str] | None = None) -> List[StemIssue]:
    """Returnează problemele detectate pentru un enunț (+ opțional variante)."""
    issues: List[StemIssue] = []
    text = (stem or "").strip()
    if not text:
        issues.append(StemIssue("empty", "enunț gol"))
        return issues

    if COUNT_STEM.search(text):
        issues.append(
            StemIssue("count", "enunțul dezvăluie numărul de răspunsuri corecte")
        )
    if PSEUDO_ADJ.search(text):
        issues.append(
            StemIssue("pseudo_adj", "adjectiv pseudo-românesc derivat din nume de autor")
        )
    if SPATIAL_GRID.search(text):
        issues.append(
            StemIssue("spatial", "referință la „dreapta/stânga” fără context vizual în grilă")
        )
    if BAD_LINKED.search(text):
        issues.append(
            StemIssue("bad_linked", "formulare incorectă „corect legați”")
        )
    if ADVERB_ERROR.search(text):
        issues.append(
            StemIssue("grammar", "„formulate corecte” — corect: „formulate corect” sau „sunt corecte”")
        )

    opts = [str(o) for o in (options or [])]
    if opts and AUTHOR_STEM_MISMATCH.search(text):
        pair_opts = sum(1 for o in opts if DASH_PAIR_OPTION.search(o))
        if pair_opts >= 2:
            issues.append(
                StemIssue(
                    "subject_mismatch",
                    "enunțul vorbește despre „autori”, dar variantele sunt perechi autor–idee",
                )
            )

    return issues


def audit_option_text(text: str) -> List[StemIssue]:
    """Pseudo-adjective în variante — mai puțin critic, dar le semnalăm în audit strict."""
    issues: List[StemIssue] = []
    if PSEUDO_ADJ.search(text or ""):
        issues.append(
            StemIssue("pseudo_adj_option", "variantă cu adjectiv pseudo-românesc")
        )
    return issues
