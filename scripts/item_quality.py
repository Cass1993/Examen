"""Remediere finală: duplicate, similitudine, explicații vechi, omogenitate."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.concept_clusters import extract_concept_label
from scripts.distractor_fix import (
    BankIndex,
    FORM_AUTHOR,
    FORM_DEFINITION,
    FORM_TERM,
    _apply_option_fix,
    _domain_pool,
    _item_seed,
    _pick,
    classify_option_form,
    fix_author_item,
    fix_heterogeneous_item,
    norm,
    options_have_duplicates,
)
from scripts.domain_concept_specs import build_domain_concept_item
from scripts.domain_item_utils import (
    ORPHAN_DOMAIN_EXPLANATION,
    is_domain_filter_item,
)
from scripts.romanian_grammar import fix_stem_grammar
from scripts.stem_naturalize import naturalize_item_stem
from scripts.term_clusters import (
    build_definition_cluster_options,
    cluster_id_for_term,
    definitions_for_cluster,
)

SIMILARITY_THRESHOLD = 0.62
STOPWORDS = frozenset(
    {
        "a", "al", "ale", "cu", "de", "din", "in", "în", "la", "pe", "pentru",
        "prin", "se", "si", "și", "un", "una", "unui", "care", "este", "sunt",
        "mai", "cel", "cea", "cei", "sau", "ca", "fi", "fie",
    }
)


def has_stale_domain_explanation(item: Dict[str, Any]) -> bool:
    expl = str(item.get("explicatie") or item.get("explanation") or "")
    return ORPHAN_DOMAIN_EXPLANATION in expl


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def _correct(item: Dict[str, Any]) -> List[str]:
    return [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]


def _token_overlap(a: str, b: str) -> float:
    ta = {
        w
        for w in re.findall(r"[a-zăâîșț0-9]+", norm(a))
        if len(w) > 2 and w not in STOPWORDS
    }
    tb = {
        w
        for w in re.findall(r"[a-zăâîșț0-9]+", norm(b))
        if len(w) > 2 and w not in STOPWORDS
    }
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / min(len(ta), len(tb))


def find_similar_option_pairs(options: Dict[str, str]) -> List[Tuple[str, str, float]]:
    letters = list(options.keys())
    pairs: List[Tuple[str, str, float]] = []
    for i, la in enumerate(letters):
        for lb in letters[i + 1 :]:
            oa, ob = options[la], options[lb]
            if not oa or not ob:
                continue
            ratio = _token_overlap(oa, ob)
            if ratio >= SIMILARITY_THRESHOLD:
                pairs.append((la, lb, ratio))
    return pairs


def _cap_explanation(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return t
    if not t.endswith("."):
        t += "."
    return t[0].upper() + t[1:] if t else t


def fix_stale_explanation(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    if not has_stale_domain_explanation(item):
        return item, False
    if is_domain_filter_item(item):
        return item, False

    options = _options(item)
    correct = _correct(item)
    if not options or not correct:
        out = dict(item)
        out["explanation"] = ""
        out["explicatie"] = ""
        return out, True

    correct_text = str(options.get(correct[0], "")).strip()
    if classify_option_form(correct_text) == FORM_DEFINITION and len(correct_text) > 20:
        new_expl = _cap_explanation(correct_text)
    elif correct_text:
        new_expl = f"Răspunsul corect: {correct_text}."
    else:
        new_expl = ""

    out = dict(item)
    out["explanation"] = new_expl
    out["explicatie"] = new_expl
    return out, True


def _try_concept_rebuild(item: Dict[str, Any], seed: int) -> Optional[Tuple[str, Dict[str, str], str]]:
    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    label = extract_concept_label(stem)
    if not label:
        return None
    built = build_domain_concept_item(label, seed)
    if built:
        return built
    return None


def _rebuild_from_definition_cluster(
    item: Dict[str, Any], index: BankIndex, seed: int
) -> Optional[Tuple[Dict[str, str], str]]:
    options = _options(item)
    correct = _correct(item)
    if len(correct) != 1 or correct[0] not in options:
        return None

    correct_text = str(options[correct[0]]).strip()
    stem = str(item.get("intrebare") or item.get("text") or "")
    explanation = str(item.get("explicatie") or item.get("explanation") or "")
    label = extract_concept_label(stem) or correct_text

    cluster_id = cluster_id_for_term(label, explanation, stem)
    pool = definitions_for_cluster(cluster_id) if cluster_id else []
    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    if len(pool) < 4:
        pool = _domain_pool(index, domain, FORM_DEFINITION)
    if len(pool) < 4:
        return None

    built = build_definition_cluster_options(pool, correct_text, seed)
    return built


def fix_duplicate_and_similar_options(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    options = _options(item)
    correct = _correct(item)
    if len(options) < 4 or not correct:
        return item, False

    similar = find_similar_option_pairs(options)
    needs = options_have_duplicates(options) or bool(similar)
    if not needs:
        return item, False

    seed = _item_seed(item)

    concept = _try_concept_rebuild(item, seed)
    if concept:
        new_stem, new_options, correct_letter = concept
        new_stem = fix_stem_grammar(new_stem)
        out = _apply_option_fix(item, new_options, [correct_letter], new_stem)
        out["tip"] = "unic"
        out["kind"] = "single"
        return out, True

    built = _rebuild_from_definition_cluster(item, index, seed)
    if built:
        new_options, correct_letter = built
        out = _apply_option_fix(item, new_options, [correct_letter])
        return out, True

    # Înlocuiește duplicate / similare din pool omogen
    correct_forms = {classify_option_form(options[c]) for c in correct if c in options}
    target = FORM_DEFINITION if FORM_DEFINITION in correct_forms else (
        correct_forms.pop() if len(correct_forms) == 1 else FORM_TERM
    )
    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    pool = _domain_pool(index, domain, target)
    if len(pool) < 4:
        return item, False

    used: Set[str] = {norm(options[c]) for c in correct if c in options}
    new_options = dict(options)
    changed = False
    seen_norms = set(used)

    for letter, opt in options.items():
        n = norm(opt)
        if letter in correct:
            if n in seen_norms and seen_norms:
                # literă corectă duplicată — păstrăm prima
                pass
            seen_norms.add(n)
            continue

        is_dup = n in seen_norms
        is_sim = any(
            _token_overlap(opt, options[other]) >= SIMILARITY_THRESHOLD
            for other in options
            if other != letter and norm(options[other]) in seen_norms
        )
        if not is_dup and not is_sim:
            seen_norms.add(n)
            continue

        replacement = _pick(pool, used, seed, ord(letter))
        if replacement and norm(replacement) not in seen_norms:
            new_options[letter] = replacement
            used.add(norm(replacement))
            seen_norms.add(norm(replacement))
            changed = True

    if not changed:
        return item, False
    return _apply_option_fix(item, new_options, correct), True


def fix_heterogeneous_if_needed(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    options = _options(item)
    if len(options) < 2:
        return item, False
    forms = {classify_option_form(str(v)) for v in options.values() if (v or "").strip()}
    if len(forms) <= 1:
        return item, False
    return fix_heterogeneous_item(item, index)


def fix_item_quality(
    item: Dict[str, Any], index: Optional[BankIndex] = None
) -> Tuple[Dict[str, Any], bool]:
    """Pas final de calitate — idempotent pe item deja parțial corectat."""
    changed = False
    out = dict(item)

    fixed, c = fix_stale_explanation(out)
    if c:
        out, changed = fixed, True

    fixed, c = fix_author_item(out)
    if c:
        out, changed = fixed, True

    if index is not None:
        fixed, c = fix_duplicate_and_similar_options(out, index)
        if c:
            out, changed = fixed, True

        fixed, c = fix_heterogeneous_if_needed(out, index)
        if c:
            out, changed = fixed, True

        # a doua trecere după înlocuiri parțiale
        fixed, c = fix_duplicate_and_similar_options(out, index)
        if c:
            out, changed = fixed, True

    if index is not None:
        fixed, c = naturalize_item_stem(out, index)
        if c:
            out, changed = fixed, True

    for field in ("intrebare", "text"):
        if field in out and out[field]:
            new = fix_stem_grammar(str(out[field]))
            if new != out[field]:
                out[field] = new
                changed = True
            text = str(out[field]).strip()
            if text and text[0].islower():
                out[field] = text[0].upper() + text[1:]
                changed = True

    return out, changed
