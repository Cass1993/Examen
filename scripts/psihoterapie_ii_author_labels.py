"""Formulări corecte pentru autori — genitiv, fără adjective improprii (horneyan etc.)."""

from __future__ import annotations

import re

# Înlocuiri în enunțuri (fraze întregi sau expresii fixe).
_STEM_PHRASES: list[tuple[str, str]] = [
    (
        "Același pattern de întârziere ar putea fi explorat de horneyan ca:",
        "Un client întârzie la ședințe când abordează tema tatălui. "
        "Din perspectiva Karei Horney, acest tipar de întârziere ar putea fi interpretat ca:",
    ),
    (
        "ar putea fi explorat de horneyan ca:",
        "ar putea fi interpretat, din perspectiva Karei Horney, ca:",
    ),
    ("Terapeutul horneyan,", "În abordarea Karei Horney, terapeutul"),
    ("Terapeutul horneyan ", "În abordarea Karei Horney, terapeutul "),
    (
        "horneyanul lucrează",
        "terapeutul în abordarea Karei Horney lucrează",
    ),
    (
        "accentul horneyan ",
        "accentul din teoria Karei Horney ",
    ),
    (
        "externalizarea horneyană",
        "externalizarea, în teoria Karei Horney,",
    ),
    (
        "externalizare horneyană",
        "externalizare, în teoria Karei Horney,",
    ),
    (
        "Soluția perfecționistă horneyană",
        "Soluția perfecționistă în teoria Karei Horney",
    ),
    (
        "soluția perfecționistă horneyană",
        "soluția perfecționistă în teoria Karei Horney",
    ),
    (
        "(self-effacement) horneyană",
        "(self-effacement) în teoria Karei Horney",
    ),
    (
        "(blind spot) horneyană",
        "(blind spot) în teoria Karei Horney",
    ),
    (
        "Tirania „trebuie”-urilor horneyene",
        "Tirania „trebuie”-urilor la Karen Horney",
    ),
    (
        "tendințe nevrotice horneyene",
        "tendințe nevrotice descrise de Karen Horney",
    ),
    (
        "tendințele horneyene",
        "tendințele descrise de Karen Horney",
    ),
    (
        "soluțiile nevrotice horneyene",
        "soluțiile nevrotice descrise de Karen Horney",
    ),
    (
        "introiecția horneyană",
        "introiecția în sensul teoriei Karei Horney",
    ),
    (
        "neo-freudiană horneyană",
        "Karen Horney",
    ),
    (
        "neo-freudiană, în tradiția Karei Horney",
        "Karen Horney",
    ),
    (
        "Karen Horney (orientare neo-freudiană)",
        "Karen Horney",
    ),
    (
        "Cele trei tendințe nevrotice horneyene",
        "Cele trei tendințe nevrotice ale Karei Horney",
    ),
    (
        "Horneyan, în procesul terapeutic",
        "Karen Horney",
    ),
]

_EXACT_LABELS: dict[str, str] = {
    "horneyan": "Karen Horney",
    "kleinian": "Melanie Klein (relații obiectuale)",
    "jungian": "Carl Gustav Jung (psihologie analitică)",
    "gestaltic": "Psihoterapia Gestalt (Fritz Perls)",
    "freudian clasic": "Sigmund Freud (psihanaliză clasică)",
    "rogersian": "Carl R. Rogers (terapie centrată pe persoană)",
    "ellisian": "Albert Ellis (terapie rațional-emotivă)",
    "adlerian": "Alfred Adler (psihologie individuală)",
    "adlerian prin safeguarding agresiv": "Alfred Adler — safeguarding prin agresiune",
}

# Corecții gramaticale (genitiv, expresii greșite).
_GRAMMAR_FIXES: list[tuple[str, str]] = [
    ("din perspectiva lui Karen Horney", "din perspectiva Karei Horney"),
    ("din teoria lui Karen Horney", "din teoria Karei Horney"),
    ("în teoria lui Karen Horney", "în teoria Karei Horney"),
    ("teoria lui Karen Horney", "teoria Karei Horney"),
    ("abordarea lui Karen Horney", "abordarea Karei Horney"),
    ("în sensul lui Karen Horney", "în sensul teoriei Karei Horney"),
    ("neo-freodiană a lui Karen Horney", "Karen Horney"),
    ("neo-freudiană a lui Karen Horney", "Karen Horney"),
    ("a lui Karen Horney", "a Karei Horney"),
    ("lui Karen Horney", "Karei Horney"),
    ("abordarea lui Melanie Klein", "abordarea Melaniei Klein"),
    ("teoria lui Melanie Klein", "teoria Melaniei Klein"),
    ("acest pattern", "acest tipar"),
    ("Același pattern", "Același tipar"),
    ("același pattern", "același tipar"),
    (
        "externalizarea în teoria Karei Horney a conflictului",
        "externalizarea conflictului, în teoria Karei Horney,",
    ),
    (
        "externalizare în teoria Karei Horney a conflictului",
        "externalizare a conflictului, în teoria Karei Horney,",
    ),
    (
        "Terapeutul în abordarea Karei Horney lucrează",
        "În abordarea Karei Horney, terapeutul lucrează",
    ),
    (
        "Terapeutul în abordarea Karei Horney, comparativ",
        "În abordarea Karei Horney, terapeutul, comparativ",
    ),
]

_HORNEY_ADJ = re.compile(r"\bhorneyan[aăe]?\b", re.IGNORECASE)


def _apply_grammar(s: str) -> str:
    for old, new in _GRAMMAR_FIXES:
        s = s.replace(old, new)
    return s


def expand_author_labels(text: str) -> str:
    if not text:
        return text
    s = text.strip()
    if s.lower() in _EXACT_LABELS:
        return _EXACT_LABELS[s.lower()]
    for old, new in _STEM_PHRASES:
        if old in s:
            s = s.replace(old, new)
    if _HORNEY_ADJ.search(s) and "Horney" not in s:
        s = _HORNEY_ADJ.sub("Karen Horney", s)
    return _apply_grammar(s)


def polish_exam_display_item(item: dict) -> dict:
    """Etichete autori + acronime la afișare (itemi exam_item din JSON)."""
    from scripts.psihoterapie_ii_acronym_expand import expand_stem_acronyms

    from scripts.psihoterapie_ii_stem_quality import reformulate_stem

    out = dict(item)
    stem = reformulate_stem(
        expand_author_labels(expand_stem_acronyms(str(item.get("text") or "")))
    )
    out["text"] = stem
    opts = item.get("options") or {}
    if opts:
        out["options"] = {
            k: reformulate_stem(expand_author_labels(str(v))) for k, v in opts.items()
        }
    return out
