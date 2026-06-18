"""Enunțuri naturale — fără ghilimele «», cu majusculă la început."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.distractor_fix import (
    BankIndex,
    FORM_DEFINITION,
    FORM_TERM,
    _domain_pool,
    _item_seed,
    classify_option_form,
    norm,
)
from scripts.concept_clusters import build_concept_item, lookup_concept
from scripts.stem_templates import cap_definition, natural_concept_stem
from scripts.term_clusters import (
    build_definition_cluster_options,
    cluster_id_for_term,
    definitions_for_cluster,
)

REVERSE_DESC_RE = re.compile(
    r"^«(.+?)»\s*descrie(?: mai ales)?:\s*$", re.IGNORECASE
)
CONCEPT_MATCH_DESC_RE = re.compile(
    r"^Care concept corespunde descrierii:\s*(.+?)\?\s*$", re.IGNORECASE | re.DOTALL
)
CONCEPT_MATCH_TERM_RE = re.compile(
    r"^Ce (?:termen|concept) (?:este descris|corespunde).+?:\s*(.+?)\?\s*$",
    re.IGNORECASE | re.DOTALL,
)
DOMAIN_GUILLEMET_RE = re.compile(
    r"^(În [^,]+,\s*)«([^»]+)»\s*(descrie|se referă la|este)\s*:?\s*$",
    re.IGNORECASE,
)
ANY_GUILLEMET_RE = re.compile(r"«([^»]+)»")


def capitalize_sentence(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return t
    if t[0].islower():
        return t[0].upper() + t[1:]
    return t


def is_definition_phrase(text: str) -> bool:
    """Text lung / cu literă mică = definiție, nu etichetă de concept."""
    t = (text or "").strip().strip("«»")
    if not t:
        return False
    if len(t) > 48:
        return True
    if t[0].islower() and len(t.split()) >= 4:
        return True
    return False


def format_concept_label(label: str) -> str:
    """Etichetă scurtă pentru enunț — fără ghilimele."""
    return cap_definition((label or "").strip().strip("«»"))


def naturalize_stem_text(stem: str) -> str:
    """Elimină « » și pune majusculă; nu schimbă logica itemului."""
    text = (stem or "").strip()
    if not text:
        return text

    m = DOMAIN_GUILLEMET_RE.match(text)
    if m:
        prefix, label, verb = m.groups()
        return f"{prefix}{format_concept_label(label)} {verb.lower()}:"

    if "«" in text:

        def _repl(match: re.Match[str]) -> str:
            inner = match.group(1).strip()
            if is_definition_phrase(inner):
                return format_concept_label(inner)
            return format_concept_label(inner)

        text = ANY_GUILLEMET_RE.sub(_repl, text)

    result = capitalize_sentence(text)
    return result if (result or "").strip() else text


def _flip_desc_to_forward_definitions(
    item: Dict[str, Any],
    index: BankIndex,
    desc: str,
) -> Tuple[Dict[str, Any], bool]:
    """«definiție» / descriere flashcard + răspuns etichetă → enunț conceptual + 4 definiții."""
    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not options or len(correct) != 1 or correct[0] not in options:
        return item, False

    primary = str(options[correct[0]]).strip()
    if classify_option_form(primary) != FORM_TERM:
        return item, False

    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    seed = _item_seed(item)

    if lookup_concept(primary):
        built = build_concept_item(primary, seed)
        if built:
            new_stem, new_options, new_corr = built
            out = dict(item)
            if "intrebare" in item:
                out["intrebare"] = new_stem
            if "text" in item:
                out["text"] = new_stem
            if "variante" in item:
                out["variante"] = new_options
            if "options" in item:
                out["options"] = new_options
            if "raspuns_corect" in item:
                out["raspuns_corect"] = [new_corr]
            if "correct" in item:
                out["correct"] = [new_corr]
            out["tip"] = "unic"
            out["kind"] = "single"
            return out, True

    new_stem = natural_concept_stem(primary, domain)
    correct_def = cap_definition(desc.strip().strip("«»"))

    cluster_id = cluster_id_for_term(primary, "", desc)
    pool = list(definitions_for_cluster(cluster_id)) if cluster_id else []
    if len(pool) < 4:
        pool = list(_domain_pool(index, domain, FORM_DEFINITION))
    if correct_def not in pool and not any(norm(p) == norm(correct_def) for p in pool):
        pool.insert(0, correct_def)
    if len(pool) < 4:
        return item, False

    built = build_definition_cluster_options(pool, correct_def, seed)
    if not built:
        return item, False

    new_options, new_corr = built
    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    if "variante" in item:
        out["variante"] = new_options
    if "options" in item:
        out["options"] = new_options
    if "raspuns_corect" in item:
        out["raspuns_corect"] = [new_corr]
    if "correct" in item:
        out["correct"] = [new_corr]
    out["tip"] = "unic"
    out["kind"] = "single"
    return out, True


def flip_reverse_desc_to_forward(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    """
    «definiție lungă» descrie mai ales: + răspuns etichetă scurtă
    → În domeniu, Conceptul X se referă la: + 4 definiții.
    """
    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    m = REVERSE_DESC_RE.match(stem)
    if m:
        return _flip_desc_to_forward_definitions(item, index, m.group(1))

    m2 = CONCEPT_MATCH_DESC_RE.match(stem)
    if m2:
        return _flip_desc_to_forward_definitions(item, index, m2.group(1))

    m3 = CONCEPT_MATCH_TERM_RE.match(stem)
    if m3:
        return _flip_desc_to_forward_definitions(item, index, m3.group(1))

    return item, False


def naturalize_item_stem(
    item: Dict[str, Any], index: Optional[BankIndex] = None
) -> Tuple[Dict[str, Any], bool]:
    """Pas final: fără ghilimele, majusculă, flip reverse-desc când e cazul."""
    if index is not None:
        flipped, changed = flip_reverse_desc_to_forward(item, index)
        if changed:
            item = flipped

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    new_stem = naturalize_stem_text(stem)
    if new_stem == stem:
        return item, False

    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    return out, True
