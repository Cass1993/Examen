"""Utilitare ușoare pentru itemii de filtru de domeniu — fără importuri circulare."""

from __future__ import annotations

import re
from typing import Any, Dict

from scripts.distractor_fix import norm
from scripts.domain_exam_topics import DOMAIN_SHORT_NAMES

DOMAIN_FILTER_RE = re.compile(
    r"^Care dintre următoarele(?: concepte sau teme| teme)? aparțin (?:domeniului|explicit)\s*"
    r"(?:«([^»]+)»|([^?]+?))(?:\s+în tematica de examen)?\?\s*$",
    re.IGNORECASE,
)

DOMAIN_BELONGING_STEM_PATTERNS: tuple = (
    re.compile(r"aparțin (?:domeniului|explicit)", re.I),
    re.compile(r"aparțin geneticii comportamentale", re.I),
    re.compile(r"sunt dimensiuni Big Five", re.I),
    re.compile(r"sunt scale de măsurare", re.I),
    re.compile(r"menționate în tematică", re.I),
    re.compile(r"din programă", re.I),
    re.compile(r"sunt concepte asociate MCD", re.I),
    re.compile(r"pot aparține relației terapeutice", re.I),
    re.compile(r"tulburări aparțin Clusterului", re.I),
    re.compile(r"care dintre următoarele teme aparțin", re.I),
    re.compile(r"care dintre următoarele concepte sau teme aparțin", re.I),
    re.compile(r"tematica de examen", re.I),
    re.compile(r"în această tematică", re.I),
)

DOMAIN_FULL_FROM_SHORT = {v.lower(): k for k, v in DOMAIN_SHORT_NAMES.items()}
ORPHAN_DOMAIN_EXPLANATION = "Răspunsurile corecte aparțin domeniului indicat"
ORPHAN_DOMAIN_EXPLANATION_ALT = (
    "Corecte sunt variantele care aparțin conceptului sau temei cerute"
)


def _trim_label(label: str) -> str:
    t = (label or "").strip()
    for sep in (" — ", " – "):
        if sep in t:
            t = t.split(sep, 1)[0].strip()
    return t


def labels_equivalent(label: str, domain: str) -> bool:
    """Eticheta tautologică — același nume ca domeniul (ex. «Psihopatologie»)."""
    if not label or not domain:
        return False
    a = norm(_trim_label(label))
    b = norm(domain)
    if a == b:
        return True
    short = DOMAIN_SHORT_NAMES.get(domain, "")
    if short and a == norm(short):
        return True
    return a == norm(_trim_label(domain))


def is_domain_filter_item(item: Dict[str, Any]) -> bool:
    stem = str(item.get("intrebare") or item.get("text") or "")
    return bool(DOMAIN_FILTER_RE.match(stem.strip()))


def is_domain_belonging_stem(stem: str) -> bool:
    text = (stem or "").strip()
    if not text:
        return False
    if DOMAIN_FILTER_RE.match(text):
        return True
    return any(p.search(text) for p in DOMAIN_BELONGING_STEM_PATTERNS)


def is_domain_belonging_item(item: Dict[str, Any]) -> bool:
    """Item care testează doar apartenența la materie/capitol/tematică."""
    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    if is_domain_belonging_stem(stem):
        return True
    return is_orphan_domain_item(item)


def domain_from_filter_stem(stem: str) -> str:
    m = DOMAIN_FILTER_RE.match(stem.strip())
    if not m:
        return ""
    raw = (m.group(1) or m.group(2) or "").strip()
    short = raw.lower()
    return DOMAIN_FULL_FROM_SHORT.get(short, raw)


def is_orphan_domain_item(item: Dict[str, Any]) -> bool:
    """Item de domeniu transformat parțial — enunț tautologic sau filtru de domeniu."""
    if is_domain_filter_item(item):
        return True

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    domain = str(item.get("domeniu") or item.get("lot") or "").strip()
    if not stem or not domain:
        return False

    m = re.search(r"«([^»]+)»", stem)
    if not m:
        return False
    label = m.group(1).strip()
    if not labels_equivalent(label, domain):
        return False

    kind = str(item.get("kind") or item.get("tip") or "").lower()
    correct = item.get("raspuns_corect") or item.get("correct") or []
    if kind in ("multi", "multiple") or len(correct) > 1:
        return True

    expl = str(item.get("explicatie") or item.get("explanation") or "")
    if ORPHAN_DOMAIN_EXPLANATION in expl or ORPHAN_DOMAIN_EXPLANATION_ALT in expl:
        options = dict(item.get("variante") or item.get("options") or {})
        if options and correct:
            from scripts.distractor_fix import classify_option_form, FORM_TERM

            short = sum(
                1 for c in correct if c in options and classify_option_form(str(options[c])) == FORM_TERM
            )
            if short == len(correct):
                return True
    return False
