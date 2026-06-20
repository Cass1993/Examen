"""Detectează meta-limbaj de tip „pentru grilă” în enunțuri — loturi II."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List

# Nu flagăm „teste tip grilă” în opțiuni — doar enunțuri cu meta-referință la format.
GRILA_META_STEM = re.compile(
    r"(?:"
    r"\b(?:pentru|în|la|din)\s+gril[ăa]\b"
    r"|\bgril[ăa](?:le)?\s+de\s+(?:examen|capcane|selecție|măsurare|EPP)\b"
    r"|\bsinteza\s+pentru\s+gril[ăa]\b"
    r"|\bclasificarea\s+pentru\s+gril[ăa]\b"
    r"|\bajută\s+la\s+gril[ăa]\b"
    r"|\bconfuzie\s+de\s+gril[ăa]\b"
    r"|\bdiferențiate\s+la\s+gril[ăa]\b"
    r"|\b(?:frecvente|corecte)\s+la\s+gril[ăa]\b"
    r")",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class GrilaMetaIssue:
    rule: str
    message: str


def audit_grila_meta_stem(stem: str) -> List[GrilaMetaIssue]:
    text = (stem or "").strip()
    if not text:
        return []
    if GRILA_META_STEM.search(text):
        return [
            GrilaMetaIssue(
                "grila_meta",
                "enunțul menționează formatul de grilă/examen — elimină meta-referința",
            )
        ]
    return []


def find_grila_meta_in_stems(
    items: Iterable[dict], *, id_key: str = "id", text_key: str = "text"
) -> List[str]:
    """Returnează linii raport pentru itemi cu meta-limbaj grilă."""
    issues: List[str] = []
    for q in items:
        qid = q.get(id_key, "?")
        stem = str(q.get(text_key) or q.get("stem") or "").strip()
        for issue in audit_grila_meta_stem(stem):
            issues.append(f"{qid}: [{issue.rule}] {issue.message} — «{stem[:100]}»")
    return issues
