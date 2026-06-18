"""Reformulare itemi «tematica de examen» — itemi conceptuali contextuali pe domeniu."""

from __future__ import annotations

import hashlib
from typing import Any, Dict, List, Optional, Tuple

from scripts.author_knowledge import (
    build_cluster_options,
    cluster_for_author,
    match_author,
    natural_stem_for_author,
)
from scripts.domain_concept_specs import build_domain_concept_item
from scripts.domain_item_utils import (
    domain_from_filter_stem,
    is_domain_filter_item,
    is_orphan_domain_item,
    labels_equivalent,
)
from scripts.label_definition_index import (
    LabelIndex,
    build_contextual_definition_item,
    lookup_best_record,
)

ConceptResult = Tuple[str, Dict[str, str], str]


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', item.get('id_local', ''))}|{item.get('intrebare', item.get('text', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _try_author_item(label: str, seed: int) -> Optional[ConceptResult]:
    author = match_author(label)
    if not author:
        return None
    cluster = cluster_for_author(author)
    if not cluster:
        return None
    built = build_cluster_options(cluster, author, seed)
    if not built:
        return None
    options, correct_letter = built
    stem = natural_stem_for_author(author) or f"Contribuția teoretică asociată lui {author} este:"
    return stem, options, correct_letter


def _pick_concept_item(
    correct_labels: List[str],
    domain: str,
    seed: int,
    label_index: Optional[LabelIndex],
    bank_index: Any,
    label_map: Dict[str, str],
) -> Optional[ConceptResult]:
    if not correct_labels:
        return None

    ordered = correct_labels[seed % len(correct_labels) :] + correct_labels[
        : seed % len(correct_labels)
    ]

    for anchor in ordered:
        if labels_equivalent(anchor, domain):
            continue

        built = build_domain_concept_item(anchor, seed)
        if built:
            return built

        built = _try_author_item(anchor, seed)
        if built:
            return built

        if label_index is not None and bank_index is not None:
            built = build_contextual_definition_item(
                anchor,
                domain,
                seed,
                sibling_labels=correct_labels,
                label_index=label_index,
                bank_index=bank_index,
                label_map=label_map,
            )
            if built:
                return built

    return None


def _explanation_for_anchor(
    anchor: str, domain: str, label_index: Optional[LabelIndex]
) -> str:
    if not label_index:
        return ""
    rec = lookup_best_record(label_index, anchor, domain)
    if rec and getattr(rec, "explanation", ""):
        return rec.explanation
    return ""


def _apply_single_item(
    item: Dict[str, Any],
    stem: str,
    options: Dict[str, str],
    correct_letter: str,
    explanation: str = "",
) -> Dict[str, Any]:
    out = dict(item)
    out["tip"] = "unic"
    if "intrebare" in item:
        out["intrebare"] = stem
    if "text" in item:
        out["text"] = stem
    if "variante" in item:
        out["variante"] = options
    if "options" in item:
        out["options"] = options
    corr = [correct_letter.lower()]
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    if "correct" in item:
        out["correct"] = corr
    if "kind" in item:
        out["kind"] = "single"
    if explanation:
        out["explicatie"] = explanation
        out["explanation"] = explanation
    return out


def fix_orphan_domain_item(
    item: Dict[str, Any],
    bank_index: Any = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Optional[LabelIndex] = None,
) -> Tuple[Dict[str, Any], bool]:
    from scripts.rewrite_domain_belonging import rewrite_domain_belonging_item

    if not is_orphan_domain_item(item):
        return item, False
    return rewrite_domain_belonging_item(
        item, bank_index, label_map, label_index
    )


def reformulate_domain_item(
    item: Dict[str, Any],
    bank_index: Any = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Optional[LabelIndex] = None,
) -> Tuple[Dict[str, Any], bool]:
    from scripts.domain_item_utils import is_domain_belonging_item
    from scripts.rewrite_domain_belonging import rewrite_domain_belonging_item

    if not is_domain_belonging_item(item):
        return item, False
    return rewrite_domain_belonging_item(
        item, bank_index, label_map, label_index
    )


def reformulate_domain_batch(
    items: List[Dict[str, Any]],
    bank_index: Any = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Optional[LabelIndex] = None,
) -> Tuple[List[Dict[str, Any]], int]:
    count = 0
    out: List[Dict[str, Any]] = []
    for item in items:
        fixed, changed = reformulate_domain_item(
            item, bank_index, label_map, label_index
        )
        if not changed:
            fixed, changed = fix_orphan_domain_item(
                fixed, bank_index, label_map, label_index
            )
        if changed:
            count += 1
        out.append(fixed)
    return out, count
