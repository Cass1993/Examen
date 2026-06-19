"""Transformă explicații grilă: fără litere de variantă (a/b/c/d)."""

from __future__ import annotations

import re

_VARIANT_SENTENCE = re.compile(
    r"^Varianta\s+[abcd]\b",
    re.IGNORECASE,
)
_VARIANTE_SENTENCE = re.compile(
    r"^Variantele\s+[abcd]\b",
    re.IGNORECASE,
)
_INLINE_VARIANTA = re.compile(r"\s*\(varianta\s+[abcd]\)", re.IGNORECASE)
_INLINE_OPTION_LETTER = re.compile(r"\s*\(([abcd])\)(?=\s|[,.;!?]|$)")
_HEADER_CHECK = re.compile(r"^[✅❌]")
_EMDASH_AFTER_CHECK = re.compile(r"^✅[^—\n]+—\s*(.+)$", re.DOTALL)
_META_AFTER_DASH = re.compile(
    r"^(toate variantele sunt corecte|singura variantă corectă|"
    r"variantele corecte[^.]*|variantele incompatibile[^.]*|"
    r"aceasta este (?:afirmația )?falsă[^.]*|aceasta este afirmația falsă[^.]*)\.\s*",
    re.IGNORECASE,
)
_TRAILING_VARIANTA_CLAUSE = re.compile(
    r"\s*—\s*ceea ce face varianta [abcd][^.]*\.?",
    re.IGNORECASE,
)


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


_LETTER_ONLY_SENTENCE = re.compile(r"^[abcd,\s și]+$", re.IGNORECASE)
_CORECT_LETTERS_ONLY = re.compile(
    r"^Corect:\s*[abcd,\s]+(?:\.|$)",
    re.IGNORECASE,
)
_GRESIT_LETTERS = re.compile(
    r"^Greșit[^.]*\.\s*",
    re.IGNORECASE,
)


def _strip_checkmark_headers(text: str) -> str:
    s = text.strip()
    m = _EMDASH_AFTER_CHECK.match(s)
    if m:
        rest = m.group(1).strip()
        rest = _META_AFTER_DASH.sub("", rest, count=1)
        s = rest
    while _HEADER_CHECK.match(s):
        replaced = re.sub(r"^[✅❌][^.!?]*[.!?]\s*", "", s, count=1)
        if replaced == s:
            break
        s = replaced.strip()
    return s


def _strip_metode_prefixes(sentence: str) -> str:
    s = sentence.strip()
    for _ in range(3):
        prev = s
        s = re.sub(r"^Corect:\s*", "", s, flags=re.IGNORECASE)
        s = re.sub(r"^Greșit:\s*", "", s, flags=re.IGNORECASE)
        s = re.sub(r"^Falsă este [abcd]:\s*", "Falsă este afirmația că ", s, flags=re.IGNORECASE)
        s = re.sub(r"^Capcane false:\s*", "", s, flags=re.IGNORECASE)
        s = re.sub(r"^Checklist etic:\s*", "", s, flags=re.IGNORECASE)
        s = re.sub(r"^Grilă corectă:\s*", "", s, flags=re.IGNORECASE)
        if s == prev:
            break
    return s.strip()


def _clean_sentence(sentence: str) -> str:
    s = _strip_metode_prefixes(sentence)
    if _CORECT_LETTERS_ONLY.match(s):
        return ""
    if _LETTER_ONLY_SENTENCE.match(s.rstrip(".")):
        return ""
    s = re.sub(r"^Greșit[^—\n]*—\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^[abcd] e (?:capcană|fals)[^.]*\.\s*", "", s, flags=re.IGNORECASE)
    s = _INLINE_VARIANTA.sub("", s)
    s = _INLINE_OPTION_LETTER.sub("", s)
    s = _TRAILING_VARIANTA_CLAUSE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def to_prose_explanation(text: str) -> str:
    """
    Elimină referințe la literele variantelor (a–d) și păstrează explicația
    conceptuală — util după amestecarea opțiunilor la build.
    """
    if not text or not str(text).strip():
        return text or ""

    s = _strip_checkmark_headers(str(text))
    kept: list[str] = []
    for raw in _split_sentences(s):
        if _VARIANT_SENTENCE.match(raw) or _VARIANTE_SENTENCE.match(raw):
            continue
        cleaned = _clean_sentence(raw)
        if cleaned:
            kept.append(cleaned)

    result = " ".join(kept)
    result = _GRESIT_LETTERS.sub("", result)
    result = re.sub(r"\s+", " ", result).strip()
    return result
