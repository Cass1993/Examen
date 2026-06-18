"""Șabloane enunțuri contextuale — fără ghilimele «», fără importuri circulare."""

from __future__ import annotations

from typing import Dict, Optional

from scripts.question_wording import _classify_target
from scripts.romanian_grammar import agree_stem_verbs

DOMAIN_NATURAL_STEMS: Dict[str, str] = {
    "Statistică": "În statistică aplicată cercetării psihologice, {label} este:",
    "Psihologia personalității": "În psihologia personalității, {label} se referă la:",
    "Psihologia dezvoltării, educației și învățării": "În psihologia dezvoltării, {label} descrie:",
    "Psihologia dezvoltării, învățării și educației": "În psihologia dezvoltării, {label} descrie:",
    "Metodologia cercetării psihologice și evaluare psihologică": "În metodologia cercetării, {label} se referă la:",
    "Metodologie și evaluare psihologică": "În evaluarea psihologică, {label} descrie:",
    "Psihologia organizațională și a muncii": "În psihologia organizațională, {label} descrie:",
    "Psihopatologie": "În psihopatologie, {label} se referă la:",
}

FALLBACK_STEMS: Dict[str, str] = {
    "concept": "{label} descrie mai ales:",
    "autor": "Contribuția teoretică asociată lui {label} este:",
    "tulburare": "{label} este caracterizată prin:",
    "metoda": "Procedura {label} presupune:",
    "model": "Modelul {label} postulează că:",
    "instrument": "Instrumentul {label} este utilizat pentru:",
    "terapie": "Abordarea {label} se bazează pe:",
    "trasatura": "Trăsătura {label} reflectă:",
}


def cap_definition(text: str) -> str:
    t = (text or "").strip().strip("«»")
    if not t:
        return t
    if t[0].islower():
        return t[0].upper() + t[1:]
    return t


def _inline_label(label: str) -> Optional[str]:
    t = (label or "").strip().strip("«»")
    if not t:
        return None
    if len(t) > 52 or (t[0].islower() and len(t.split()) >= 5):
        return None
    return cap_definition(t)


def _stem_for_kind(inline: str, kind: str) -> str:
    """Evită dublarea articolului: Abordarea Terapia… / Abordarea Modelul…"""
    low = inline.lower()
    if kind == "terapie" or low.startswith(("terapia ", "psihoterapia ")):
        if low.startswith(("terapia ", "psihoterapia ", "abordarea ")):
            return f"{inline} se bazează pe:"
        return f"În psihoterapie, abordarea {inline.lower()} se bazează pe:"
    if kind == "model" or low.startswith("modelul "):
        if low.startswith("modelul "):
            return f"{inline} postulează că:"
        return f"Modelul {inline} postulează că:"
    template = FALLBACK_STEMS.get(kind, FALLBACK_STEMS["concept"])
    return template.format(label=inline)


def natural_concept_stem(label: str, domain: str) -> str:
    inline = _inline_label(label)
    if inline is None:
        desc = cap_definition(label.strip("«»"))
        stem = f"Care concept corespunde descrierii: {desc}?"
        return stem

    if domain in DOMAIN_NATURAL_STEMS:
        stem = DOMAIN_NATURAL_STEMS[domain].format(label=inline)
    else:
        kind = _classify_target(label)
        stem = _stem_for_kind(inline, kind)
    return agree_stem_verbs(stem, inline)
