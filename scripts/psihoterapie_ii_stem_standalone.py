"""Enunțuri autonome — fără referințe la itemi sau context invizibil."""

from __future__ import annotations

import re

# Începuturi de enunț care cer context din itemul anterior (neacceptabil în quiz aleator).
DANGLING_STEM_START = re.compile(
    r"^(același|aceeași|acelaşi|aceeaşi|în aceeași|in aceeasi|dar s-ar|dar ar)\b",
    re.IGNORECASE,
)

# Meta-limbaj de tip „în examen, itemul…” — interzis în enunțuri.
META_EXAM_PATTERNS = [
    re.compile(r"^În examen,\s*itemul\b", re.IGNORECASE),
    re.compile(r"^În examen,\s*confuzia\b", re.IGNORECASE),
    re.compile(r"\bitemul de examen\b", re.IGNORECASE),
    re.compile(r"\bitemul care\b", re.IGNORECASE),
    re.compile(r"^Într-o grilă,\s*", re.IGNORECASE),
    re.compile(r"^În grile,\s*", re.IGNORECASE),
    re.compile(r"^Într-un examen\b", re.IGNORECASE),
    re.compile(r"^Un examinator\b", re.IGNORECASE),
    re.compile(r"^Același enunț\b", re.IGNORECASE),
    re.compile(r"^Confuzia examenului\b", re.IGNORECASE),
]


def ensure_standalone_stem(stem: str) -> str:
    """Returnează enunțul; aruncă dacă lipsește contextul necesar."""
    text = (stem or "").strip()
    if not text:
        return text
    if DANGLING_STEM_START.match(text):
        raise ValueError(
            f"Enunț fără context (referință la item anterior): {text[:100]!r}"
        )
    for pattern in META_EXAM_PATTERNS:
        if pattern.search(text):
            raise ValueError(
                f"Enunț cu meta-limbaj de examen (reformulează direct): {text[:100]!r}"
            )
    return text


def audit_stems(stems: list[str]) -> list[str]:
    """Listează enunțurile problematice."""
    problems: list[str] = []
    for stem in stems:
        s = (stem or "").strip()
        if DANGLING_STEM_START.match(s):
            problems.append(s)
            continue
        for pattern in META_EXAM_PATTERNS:
            if pattern.search(s):
                problems.append(s)
                break
    return problems
