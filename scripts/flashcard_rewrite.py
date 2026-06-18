"""Rescriere conceptuală a itemilor tip flashcard — enunțuri naturale de examen."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from scripts.concept_clusters import build_concept_item, extract_concept_label, lookup_concept
from scripts.distractor_fix import (
    BankIndex,
    FORM_AUTHOR,
    _item_seed,
    classify_option_form,
    norm,
)
from scripts.domain_concept_specs import build_domain_concept_item
from scripts.domain_item_utils import is_domain_belonging_item
from scripts.natural_items import reformulate_item
from scripts.reformulate_domain import fix_orphan_domain_item, reformulate_domain_item
from scripts.stem_naturalize import flip_reverse_desc_to_forward
FLASHCARD_STEM_PATTERNS = (
    re.compile(r"care concept corespunde descrierii", re.I),
    re.compile(r"ce termen (?:este descris|corespunde)", re.I),
    re.compile(r"care concept este descris", re.I),
    re.compile(r"cărui concept", re.I),
    re.compile(r"care descriere se potrivește", re.I),
    re.compile(r"aparțin (?:domeniului|explicit)", re.I),
    re.compile(r"tematica de examen", re.I),
    re.compile(r"în această tematică", re.I),
    re.compile(r"modelul .+ postulează că:\s*$", re.I),
    re.compile(r"«.+» descrie mai ales:\s*$", re.I),
    re.compile(r"«.+» se referă la:\s*$", re.I),
)

DOMAIN_GUILLEMET_STEM_RE = re.compile(
    r"^În [^,]+,\s*«(.+?)»\s+se referă la:\s*$", re.I
)

CLUSTER_MIXED_RE = re.compile(r"cluster(?:ul)?\s+([abc])\b", re.I)
DISORDER_IN_OPTION_RE = re.compile(r"tulburare\w*\s+\w+\s+de\s+personalitate", re.I)
CLUSTER_DESC_IN_OPTION_RE = re.compile(
    r"cluster(?:ul)?\s+[abc]\s*[—\-]\s*|^(?:ciudat|dramatic|anxios|excentric|impulsiv)",
    re.I,
)

ABSOLUTE_RE = re.compile(
    r"\b(doar|exclusiv|obligatoriu|întotdeauna|niciodată)\b", re.I
)

LENGTH_IMBALANCE_RATIO = 1.75


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def _correct(item: Dict[str, Any]) -> List[str]:
    return [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]


def is_flashcard_stem(stem: str) -> bool:
    t = (stem or "").strip()
    if not t:
        return False
    return any(p.search(t) for p in FLASHCARD_STEM_PATTERNS)


def _apply_result(
    item: Dict[str, Any],
    new_stem: str,
    new_options: Dict[str, str],
    new_correct: Sequence[str],
) -> Dict[str, Any]:
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
        out["raspuns_corect"] = list(new_correct)
    if "correct" in item:
        out["correct"] = list(new_correct)
    if len(new_correct) == 1:
        out["tip"] = "unic"
        out["kind"] = "single"
    stale = "Răspunsurile corecte aparțin domeniului indicat"
    for field in ("explicatie", "explanation"):
        if str(out.get(field) or "").strip() == stale:
            out[field] = ""
    return out


def _try_spec_from_correct(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    opts = _options(item)
    correct = _correct(item)
    if not opts or not correct:
        return None
    seed = _item_seed(item)
    labels: List[str] = []
    for letter in correct:
        if letter in opts:
            labels.append(str(opts[letter]).strip())
    if not labels:
        return None
    for label in labels:
        built = build_domain_concept_item(label, seed)
        if built:
            stem, new_opts, corr = built
            return _apply_result(item, stem, new_opts, [corr])
        built2 = build_concept_item(label, seed)
        if built2:
            stem, new_opts, corr = built2
            return _apply_result(item, stem, new_opts, [corr])
    return None


def _try_spec_from_stem(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    label = extract_concept_label(_stem(item))
    if not label:
        m = DOMAIN_GUILLEMET_STEM_RE.match(_stem(item))
        if m:
            label = m.group(1).strip()
    if not label:
        return None
    seed = _item_seed(item)
    built = build_concept_item(label, seed) or build_domain_concept_item(label, seed)
    if not built:
        return None
    stem, new_opts, corr = built
    return _apply_result(item, stem, new_opts, [corr])


def _cluster_mixed_options(options: Dict[str, str]) -> bool:
    has_disorder = any(DISORDER_IN_OPTION_RE.search(v) for v in options.values())
    has_desc = any(CLUSTER_DESC_IN_OPTION_RE.search(v) for v in options.values())
    short_cluster = sum(
        1 for v in options.values() if re.match(r"^cluster(?:ul)?\s+[abc]\b", v.strip(), re.I)
    )
    return (has_disorder and has_desc) or short_cluster >= 2


def _try_cluster_item(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    stem = _stem(item)
    opts = _options(item)
    if not opts:
        return None
    if not CLUSTER_MIXED_RE.search(stem) and not _cluster_mixed_options(opts):
        return None
    m = CLUSTER_MIXED_RE.search(stem)
    cluster_key = f"clusterul {(m.group(1) if m else 'a').lower()}"
    spec = lookup_concept(cluster_key)
    if not spec:
        return None
    seed = _item_seed(item)
    built = build_concept_item(cluster_key, seed)
    if not built:
        return None
    new_stem, new_opts, corr = built
    return _apply_result(item, new_stem, new_opts, [corr])


def _options_heterogeneous(options: Dict[str, str]) -> bool:
    forms = {classify_option_form(v) for v in options.values() if v}
    if len(forms) > 1 and FORM_AUTHOR not in forms:
        return True
    lengths = [len(v) for v in options.values() if v]
    if not lengths:
        return False
    short = sum(1 for ln in lengths if ln < 35)
    long = sum(1 for ln in lengths if ln > 90)
    return short >= 2 and long >= 1


def _correct_much_longer(item: Dict[str, Any]) -> bool:
    opts = _options(item)
    correct = _correct(item)
    if len(correct) != 1 or correct[0] not in opts:
        return False
    corr_len = len(str(opts[correct[0]]))
    wrong_lens = [len(str(opts[k])) for k in opts if k not in correct]
    if not wrong_lens:
        return False
    avg_wrong = sum(wrong_lens) / len(wrong_lens)
    if avg_wrong < 20:
        return corr_len > avg_wrong * LENGTH_IMBALANCE_RATIO
    return corr_len > avg_wrong * LENGTH_IMBALANCE_RATIO and corr_len - avg_wrong > 40


def _soften_absolute(text: str) -> str:
    t = text
    for word, repl in (
        ("exclusiv", "preponderent"),
        ("Exclusiv", "Preponderent"),
        ("doar", "în principal"),
        ("Doar", "În principal"),
        ("obligatoriu", "necesar"),
        ("Obligatoriu", "Necesar"),
        ("întotdeauna", "frecvent"),
        ("Întotdeauna", "Frecvent"),
        ("niciodată", "rar"),
        ("Niciodată", "Rar"),
    ):
        t = re.sub(rf"\b{word}\b", repl, t)
    return t


def sanitize_distractors(item: Dict[str, Any], index: BankIndex) -> Tuple[Dict[str, Any], bool]:
    """Elimină indicii evidente în distractori (absolutisme, dezechilibru de lungime)."""
    opts = _options(item)
    correct = set(_correct(item))
    if not opts or not correct:
        return item, False

    changed = False
    new_opts = dict(opts)
    corr_texts = {norm(opts[c]) for c in correct if c in opts}
    corr_has_absolute = any(ABSOLUTE_RE.search(opts[c]) for c in correct if c in opts)

    for letter, text in opts.items():
        if letter in correct:
            continue
        if ABSOLUTE_RE.search(text) and not corr_has_absolute:
            softened = _soften_absolute(text)
            if softened != text:
                new_opts[letter] = softened
                changed = True

    if _correct_much_longer(item) or _options_heterogeneous(new_opts):
        rebuilt = _try_spec_from_stem(item) or _try_spec_from_correct(item)
        if rebuilt:
            return rebuilt, True

    if changed:
        return _apply_result(item, _stem(item), new_opts, list(correct)), True
    return item, False


def rewrite_flashcard_item(
    item: Dict[str, Any],
    index: BankIndex,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Optional[Any] = None,
) -> Tuple[Dict[str, Any], bool]:
    """Rescriere conceptuală pentru itemi flashcard sau cu construcție slabă."""
    from scripts.fix_tf_items import is_tf_item

    if is_tf_item(item):
        return item, False

    original = dict(item)
    out = dict(item)

    if is_domain_belonging_item(out):
        out2, ch = reformulate_domain_item(out, index, label_map, label_index)
        if ch:
            return out2, True
        out2, ch = fix_orphan_domain_item(out, index, label_map, label_index)
        if ch:
            return out2, True

    stem = _stem(out)
    if is_flashcard_stem(stem) or "«" in stem:
        out2, ch = flip_reverse_desc_to_forward(out, index)
        if ch:
            out = out2
        else:
            rebuilt = _try_spec_from_stem(out) or _try_spec_from_correct(out)
            if rebuilt:
                out = rebuilt
            else:
                out2, ch = reformulate_item(out)
                if ch:
                    out = out2

    if _cluster_mixed_options(_options(out)) or CLUSTER_MIXED_RE.search(_stem(out)):
        rebuilt = _try_cluster_item(out)
        if rebuilt:
            out = rebuilt

    if _options_heterogeneous(_options(out)):
        rebuilt = _try_spec_from_stem(out) or _try_spec_from_correct(out)
        if rebuilt:
            out = rebuilt
        else:
            out2, ch = reformulate_item(out)
            if ch:
                out = out2

    out2, ch = sanitize_distractors(out, index)
    if ch:
        out = out2

    return out, out != original


def item_rewrite_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{_stem(item)}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)
