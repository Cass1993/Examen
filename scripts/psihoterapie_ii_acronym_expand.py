"""Extinde prescurtările din enunțuri — format: denumire completă (ABREV)."""

from __future__ import annotations

import re

_ABC_FULL = "Activator, Beliefs, Consequences (A-B-C)"
_CBT_FULL = "terapia cognitiv-comportamentală (CBT)"
_AT_FULL = "analiza tranzacțională (AT)"


def expand_stem_acronyms(stem: str) -> str:
    """Returnează enunțul cu acronimele extinse la prima apariție relevantă."""
    if not stem:
        return stem

    s = stem.strip()

    if "A-B-C" in s and "Activator, Beliefs, Consequences" not in s:
        s = s.replace("Modelul A-B-C la Ellis", f"Modelul {_ABC_FULL} la Ellis")
        s = s.replace("modelul A-B-C al lui Ellis", f"modelul {_ABC_FULL} al lui Ellis")
        s = re.sub(r"\bmodelul A-B-C\b", f"modelul {_ABC_FULL}", s, flags=re.IGNORECASE)

    if "(CBT)" not in s:
        if re.search(r"\bCBT\b", s):
            s = re.sub(r"\bîn CBT\b", f"în {_CBT_FULL}", s)
            s = re.sub(r"\bclient CBT\b", f"client în {_CBT_FULL}", s)
            s = re.sub(r"\bde CBT\b", f"de {_CBT_FULL}", s)
        elif re.search(r"\bterapia cognitiv-comportamentală\b", s, re.IGNORECASE):
            s = re.sub(
                r"\bterapia cognitiv-comportamentală\b",
                _CBT_FULL,
                s,
                count=1,
                flags=re.IGNORECASE,
            )

    if "(AT)" not in s:
        s = re.sub(r"\bÎn AT\b", f"În {_AT_FULL}", s)
        s = re.sub(r"\banaliza tranzacțională\b", _AT_FULL, s, flags=re.IGNORECASE)

    if "first-order" not in s:
        s = re.sub(r"\bordinul I\b(?!\s*\()", "ordinul I (first-order)", s)

    if "second-order" not in s:
        s = re.sub(r"\bordinul II\b(?!\s*\()", "ordinul II (second-order)", s)

    if "Parent, Adult" in s and "Parent (Părinte)" not in s:
        s = s.replace(
            "stările ego Parent, Adult și Copil",
            "stările ego Parent (Părinte), Adult și Copil (Copil)",
        )

    if "(IP)" not in s and re.search(r"client identificat", s, re.IGNORECASE):
        s = re.sub(
            r"expresia „client identificat”",
            "expresia „pacientul identificat” (IP)",
            s,
            flags=re.IGNORECASE,
        )

    if "(REBT)" not in s:
        s = s.replace(
            "Terapia rațional-emotivă (Ellis)",
            "Terapia rațional-emotivă (REBT) a lui Ellis",
        )
        if re.search(r"\bterapia rațional-emotivă\b", s, re.IGNORECASE):
            s = re.sub(
                r"\bterapia rațional-emotivă\b",
                "terapia rațional-emotivă (REBT)",
                s,
                count=1,
                flags=re.IGNORECASE,
            )

    if "Enmeshment" in s and "împletire" not in s:
        s = s.replace("Enmeshment", "Enmeshment (împletirea excesivă)")

    if re.search(r"\bdisengagement\b", s, re.IGNORECASE) and "dezangajare" not in s.lower():
        s = re.sub(r"\bdisengagement\b", "Disengagement (dezangajarea)", s, flags=re.IGNORECASE)

    return s
