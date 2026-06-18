"""Formulare enunțuri + extindere prescurtări."""

from __future__ import annotations

from typing import Any, Dict, Optional

from scripts.abbreviations import expand_abbreviations
from scripts.question_wording import fix_intrebare
from scripts.romanian_grammar import fix_stem_grammar
from scripts.stem_naturalize import naturalize_item_stem


def polish_text(text: str) -> str:
    return expand_abbreviations(fix_intrebare(text))


def _item_stem(item: Dict[str, Any]) -> str:
    return str(item.get("text") or item.get("intrebare") or "").strip()


def _set_item_stem(item: Dict[str, Any], stem: str) -> Dict[str, Any]:
    out = dict(item)
    if "text" in out:
        out["text"] = stem
    if "intrebare" in out:
        out["intrebare"] = stem
    return out


def rescue_empty_stem(item: Dict[str, Any], original_stem: str) -> Dict[str, Any]:
    """Nu lăsa polish-ul fără enunț — refolosește originalul sau generează unul minim."""
    if _item_stem(item):
        return item

    orig = (original_stem or "").strip()
    if orig:
        return _set_item_stem(item, orig)

    options = dict(item.get("options") or item.get("variante") or {})
    correct = [str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])]
    if len(correct) == 1 and correct[0] in options:
        label = str(options[correct[0]]).strip()
        if label:
            from scripts.stem_templates import natural_concept_stem

            domain = str(item.get("domeniu") or item.get("lot") or "").strip()
            fallback = natural_concept_stem(label, domain).strip()
            if fallback:
                return _set_item_stem(item, fallback)
            return _set_item_stem(item, f"Care concept corespunde descrierii: {label}?")

    return item


def polish_question_item(
    item: Dict[str, Any],
    index: Optional[Any] = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Optional[Any] = None,
) -> Dict[str, Any]:
    """Polish enunț + upgrade A/F + reformulare naturală + distractori."""
    if item.get("exam_item"):
        return dict(item)

    from scripts.distractor_fix import fix_item_distractors
    from scripts.fix_tf_items import fix_tf_item, is_tf_item
    from scripts.natural_items import reformulate_item
    from scripts.reformulate_domain import (
        fix_orphan_domain_item,
        reformulate_domain_item,
    )

    original_stem = str(item.get("text") or item.get("intrebare") or "")
    out = dict(item)
    for field in ("intrebare", "text", "explicatie", "explanation"):
        if field in out and out[field]:
            out[field] = polish_text(str(out[field]))
    for key in ("variante", "options"):
        if key in out and isinstance(out[key], dict):
            out[key] = {k: polish_text(str(v)) for k, v in out[key].items()}

    from scripts.fix_incomplete_tf import fix_incomplete_tf_item, is_incomplete_tf_item

    if is_incomplete_tf_item(out):
        fixed, _ = fix_incomplete_tf_item(out)
        if fixed:
            out = fixed

    out, _ = fix_tf_item(out)
    if is_tf_item(out):
        for field in ("intrebare", "text"):
            if field in out and out[field]:
                out[field] = fix_stem_grammar(str(out[field]))
                text = str(out[field]).strip()
                if text and text[0].islower():
                    out[field] = text[0].upper() + text[1:]
        return out

    from scripts.fix_admin_list_items import (
        fix_admin_list_item,
        fix_labeled_options_in_definition_stem,
    )
    from scripts.fix_category_list_stems import (
        fix_category_list_item,
        fix_mixed_cluster_options,
    )
    from scripts.fix_context_stems import fix_context_stem_item
    from scripts.fix_genetics_epigenetics import (
        is_genetics_problem_item,
        normalize_item_terminology,
        rewrite_genetics_item,
    )

    from scripts.fix_malformed_flashcard import fix_malformed_flashcard_item

    out = normalize_item_terminology(out)
    out, _ = fix_malformed_flashcard_item(out)
    if is_genetics_problem_item(out):
        seed = int(out.get("id") or index or 0)
        fixed = rewrite_genetics_item(out, seed)
        if fixed:
            out = fixed

    out, _ = reformulate_domain_item(out, index, label_map, label_index)
    out, _ = fix_orphan_domain_item(out, index, label_map, label_index)
    out, _ = fix_category_list_item(out)
    out, _ = fix_admin_list_item(out)
    out, _ = fix_labeled_options_in_definition_stem(out)
    out, _ = fix_mixed_cluster_options(out)
    out, _ = fix_context_stem_item(out)
    out, _ = reformulate_item(out)
    if index is not None:
        from scripts.flashcard_rewrite import rewrite_flashcard_item

        out, _ = rewrite_flashcard_item(out, index, label_map, label_index)
        out, _ = fix_item_distractors(out, index)
        out, _ = naturalize_item_stem(out, index)
    if index is not None:
        from scripts.rewrite_conceptual_coherence import rewrite_item_coherence

        lot = str(out.get("domeniu") or out.get("lot") or "")
        out, _ = rewrite_item_coherence(out, index, lot)

    from scripts.association_pair_fix import (
        fix_association_pairs,
        fix_broken_association_item,
    )

    out, _ = fix_association_pairs(out)
    out, _ = fix_broken_association_item(out)
    out, _ = fix_malformed_flashcard_item(out)
    out, _ = fix_labeled_options_in_definition_stem(out)

    out, _ = fix_tf_item(out)
    for field in ("intrebare", "text"):
        if field in out and out[field]:
            out[field] = fix_stem_grammar(str(out[field]))
            text = str(out[field]).strip()
            if text and text[0].islower():
                out[field] = text[0].upper() + text[1:]
    return rescue_empty_stem(out, original_stem)
