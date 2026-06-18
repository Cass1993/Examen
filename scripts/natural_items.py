"""Reformulare itemi în stil examen natural — enunț contextual + opțiuni omogene."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from scripts.author_knowledge import (
    build_cluster_options,
    cluster_for_author,
    format_author_option,
    lookup_author_by_stem,
    match_author,
    natural_stem_for_author,
)
from scripts.concept_clusters import (
    build_concept_item,
    extract_concept_label,
    lookup_concept,
)
from scripts.domain_item_utils import is_domain_belonging_item, labels_equivalent
from scripts.stem_templates import cap_definition as _cap_definition
from scripts.stem_templates import natural_concept_stem as _natural_concept_stem
from scripts.question_wording import (
    CONCEPT_AUTHOR_LABEL_RE,
    EXAM_META_RE,
    _classify_target,
    _stem_for_label,
)

REVERSE_CONCEPT_RE = re.compile(
    r"^Care concept este descris de formularea\s*«(.+?)»\?\s*$",
    re.IGNORECASE | re.DOTALL,
)
REVERSE_TERM_RE = re.compile(
    r"^Ce concept corespunde cel mai bine descrierii\s*«(.+?)»\?\s*$",
    re.IGNORECASE | re.DOTALL,
)
CONCEPT_MATCH_DESC_RE = re.compile(
    r"^Care concept corespunde descrierii:\s*(.+?)\?\s*$",
    re.IGNORECASE | re.DOTALL,
)
AUTHOR_STEM_RE = re.compile(
    r"^Care variantă descrie cel mai bine contribuția teoretică a lui\s+(.+?)\?\s*$",
    re.IGNORECASE,
)
LABEL_FROM_STEM_RE = re.compile(
    r"^Care variantă descrie cel mai bine\s+(?:conceptul|modelul teoretic|"
    r"instrumentul/testul psihologic|abordarea terapeutică|categoria clinică|"
    r"procedura/metoda|trăsătura psihologică)\s*«(.+?)»\?\s*$",
    re.IGNORECASE,
)

def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', item.get('id_local', ''))}|{item.get('intrebare', item.get('text', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _extract_label(stem: str) -> Optional[str]:
    for pat in (CONCEPT_AUTHOR_LABEL_RE, EXAM_META_RE, LABEL_FROM_STEM_RE):
        m = pat.match(stem.strip())
        if m:
            return m.group(1).strip()
    return None


def _try_author_cluster_item(
    stem: str,
    options: Dict[str, str],
    correct: Sequence[str],
    item: Dict[str, Any],
) -> Optional[Tuple[str, Dict[str, str], List[str]]]:
    seed = _item_seed(item)
    author: Optional[str] = lookup_author_by_stem(stem)
    correct_author: Optional[str] = None
    for letter in correct:
        opt = options.get(letter, "")
        if opt:
            correct_author = match_author(str(opt))
            if correct_author:
                break
    if correct_author:
        author = correct_author

    m = REVERSE_CONCEPT_RE.match(stem) or REVERSE_TERM_RE.match(stem)
    if m:
        author = match_author(m.group(1))
    if not author:
        m2 = AUTHOR_STEM_RE.match(stem)
        if m2:
            author = match_author(m2.group(1))
    if not author:
        author = match_author(stem)
    if not author:
        for letter in correct:
            opt = options.get(letter, "")
            if match_author(opt):
                author = match_author(opt)
                break
            if re.match(r"^[A-ZĂÂÎȘȚ]\.", opt.strip()):
                author = match_author(opt)
                if author:
                    break
    if not author:
        for opt in options.values():
            if "autor asociat" in opt.lower() or "autoare asociată" in opt.lower():
                author = match_author(opt)
                if author:
                    break

    if not author:
        return None

    cluster = cluster_for_author(author)
    if not cluster:
        return None

    built = build_cluster_options(cluster, author, seed)
    if not built:
        return None
    new_options, correct_letter = built
    new_stem = natural_stem_for_author(author) or stem
    return new_stem, new_options, [correct_letter]


def _options_are_heterogeneous(options: Dict[str, str]) -> bool:
    """Detectează opțiuni «nucă în perete» — etichete scurte sau din domenii disparate."""
    short = 0
    for opt in options.values():
        o = (opt or "").strip()
        if len(o) < 45 and not o.startswith(("mecanisme", "procese", "relația", "combinarea")):
            short += 1
        if o in {"Colaborarea", "Confidențialitatea", "Empatia", "Empatie"}:
            return True
        if re.match(r"^[A-ZĂÂÎȘȚ][a-zăâîșț]+(ul|ea|ia)?$", o) and len(o) < 25:
            short += 1
    return short >= 2


def _try_concept_cluster_item(
    stem: str,
    options: Dict[str, str],
    correct: Sequence[str],
    item: Dict[str, Any],
) -> Optional[Tuple[str, Dict[str, str], List[str]]]:
    seed = _item_seed(item)
    if len(correct) == 1 and correct[0] in options:
        answer_label = str(options[correct[0]]).strip()
        if lookup_concept(answer_label):
            built = build_concept_item(answer_label, seed)
            if built:
                new_stem, new_options, correct_letter = built
                return new_stem, new_options, [correct_letter]

    label = extract_concept_label(stem) or _extract_label(stem)
    if not label:
        m = CONCEPT_MATCH_DESC_RE.match(stem)
        if m and len(correct) == 1 and correct[0] in options:
            label = str(options[correct[0]]).strip()
    if not label:
        return None
    if _classify_target(label) == "autor":
        return None

    built = build_concept_item(label, seed)
    if not built:
        return None

    new_stem, new_options, correct_letter = built
    return new_stem, new_options, [correct_letter]


def _try_concept_definition_item(
    stem: str,
    options: Dict[str, str],
    correct: Sequence[str],
    item: Dict[str, Any],
) -> Optional[Tuple[str, Dict[str, str], List[str]]]:
    if is_domain_belonging_item(item):
        return None

    label = extract_concept_label(stem) or _extract_label(stem)
    if not label:
        return None
    if _classify_target(label) == "autor":
        return None  # handled by author cluster

    domain = str(item.get("domeniu") or item.get("lot") or "").strip()
    if labels_equivalent(label, domain):
        return None

    # Item conceptual din catalog (validitate, norme, standardizare…)
    if _options_are_heterogeneous(options):
        from scripts.domain_concept_specs import build_domain_concept_item

        seed = _item_seed(item)
        built = build_domain_concept_item(label, seed)
        if built:
            new_stem, new_options, correct_letter = built
            return new_stem, new_options, [correct_letter]
        built = build_concept_item(label, seed)
        if built:
            new_stem, new_options, correct_letter = built
            return new_stem, new_options, [correct_letter]

    new_stem = _natural_concept_stem(label, domain)

    new_options: Dict[str, str] = {}
    for letter, opt in options.items():
        new_options[letter] = _cap_definition(opt)

    if new_stem == stem and all(
        new_options[k] == options[k] for k in options
    ):
        return None

    return new_stem, new_options, list(correct)


def reformulate_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    from scripts.fix_tf_items import is_tf_item

    if is_tf_item(item):
        return item, False
    if is_domain_belonging_item(item):
        return item, False

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not stem or not options or not correct:
        return item, False

    result = _try_author_cluster_item(stem, options, correct, item)
    if not result:
        result = _try_concept_cluster_item(stem, options, correct, item)
    if not result:
        result = _try_concept_definition_item(stem, options, correct, item)
    if not result:
        return item, False

    new_stem, new_options, new_correct = result
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
        out["raspuns_corect"] = new_correct
    if "correct" in item:
        out["correct"] = new_correct
    if len(new_correct) == 1:
        out["tip"] = "unic"
        out["kind"] = "single"
    return out, True
