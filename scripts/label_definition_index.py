"""Index etichetă → definiție din itemii existenți ai băncii."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.abbreviations import collapse_nested_expansions
from scripts.distractor_fix import BankIndex, classify_option_form, norm
from scripts.domain_exam_topics import CROSS_DOMAIN_PHRASES, TOPIC_PHRASES
from scripts.stem_templates import cap_definition as _cap_definition
from scripts.stem_templates import natural_concept_stem as _natural_concept_stem

ConceptResult = Tuple[str, Dict[str, str], str]

STEM_LABEL_RE = re.compile(
    r"«([^»]+)»\s*(?:se referă la|descrie|este|postulează că|presupune|combină)",
    re.IGNORECASE,
)
CLUSTER_STEM_RE = re.compile(
    r"care descriere se potrivește cu «([^»]+)»",
    re.IGNORECASE,
)


@dataclass
class LabelRecord:
    label: str
    domain: str
    stem: str
    correct_definition: str
    option_definitions: List[str] = field(default_factory=list)
    explanation: str = ""


LabelIndex = Dict[str, List[LabelRecord]]


def _pick(pool: List[str], used: Set[str], seed: int, offset: int = 0) -> Optional[str]:
    if not pool:
        return None
    available = [x for x in pool if norm(x) not in used]
    if not available:
        available = list(pool)
    return available[(seed + offset) % len(available)]


def shorten_label(label: str) -> str:
    """Reduce o opțiune extinsă la eticheta scurtă."""
    t = collapse_nested_expansions((label or "").strip())
    if not t:
        return t
    key = norm(t)
    for topic_key, phrase in TOPIC_PHRASES.items():
        if norm(phrase) == key:
            return topic_key[0].upper() + topic_key[1:] if topic_key else topic_key
    for topic_key, phrase in CROSS_DOMAIN_PHRASES.items():
        if norm(phrase) == key:
            return topic_key[0].upper() + topic_key[1:] if topic_key else topic_key
    if " — " in t:
        t = t.split(" — ", 1)[0].strip()
    if " – " in t:
        t = t.split(" – ", 1)[0].strip()
    m = re.match(r"^(.+?)\s+la\s+[A-ZĂÂÎȘȚ]", t)
    if m and len(m.group(1)) < len(t) - 5:
        t = m.group(1).strip()
    m = re.match(r"^(.+?)\s+în\s+(?:personalitate|evaluarea|teoria|câmpul)", t, re.I)
    if m and len(m.group(1)) < len(t) - 5:
        t = m.group(1).strip()
    return t


def _extract_label_from_stem(stem: str) -> Optional[str]:
    t = (stem or "").strip()
    m = STEM_LABEL_RE.search(t)
    if m:
        return m.group(1).strip()
    m = CLUSTER_STEM_RE.search(t)
    if m:
        return m.group(1).strip()
    return None


def build_label_definition_index(items: Sequence[Dict[str, Any]]) -> LabelIndex:
    index: LabelIndex = defaultdict(list)
    seen: Set[str] = set()

    for item in items:
        stem = str(item.get("intrebare") or item.get("text") or "").strip()
        label = _extract_label_from_stem(stem)
        if not label:
            continue

        options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
        correct = [
            str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])
        ]
        if not options or not correct or correct[0] not in options:
            continue

        correct_def = str(options[correct[0]]).strip()
        if classify_option_form(correct_def) != "definition":
            continue

        domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
        defs = [
            str(v).strip()
            for v in options.values()
            if classify_option_form(str(v)) == "definition"
        ]
        dedupe_key = f"{norm(label)}|{norm(correct_def)}|{domain}"
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)

        rec = LabelRecord(
            label=label,
            domain=domain,
            stem=stem,
            correct_definition=correct_def,
            option_definitions=defs,
            explanation=str(
                item.get("explicatie") or item.get("explanation") or ""
            ).strip(),
        )
        for alias in {label, shorten_label(label)}:
            if alias:
                index[norm(alias)].append(rec)
    return dict(index)


def lookup_best_record(
    label_index: LabelIndex, label: str, domain: str = ""
) -> Optional[LabelRecord]:
    short = shorten_label(label)
    candidates = list(label_index.get(norm(short), []))
    if norm(short) != norm(label):
        candidates.extend(label_index.get(norm(label), []))

    if not candidates:
        for key, recs in label_index.items():
            if len(key) > 5 and (key in norm(short) or norm(short) in key):
                candidates.extend(recs)

    if not candidates:
        return None

    if domain:
        same = [r for r in candidates if r.domain == domain]
        if same:
            candidates = same

    return max(candidates, key=lambda r: len(r.correct_definition))


def resolve_definition(
    label: str,
    label_index: LabelIndex,
    label_map: Dict[str, str],
    domain: str = "",
) -> Optional[str]:
    rec = lookup_best_record(label_index, label, domain)
    if rec:
        return rec.correct_definition
    short = shorten_label(label)
    for key in (norm(short), norm(label)):
        if key in label_map:
            return label_map[key]
    for k, v in label_map.items():
        if len(k) > 5 and (k in norm(short) or norm(short) in k):
            return v
    return None


def build_contextual_definition_item(
    anchor_label: str,
    domain: str,
    seed: int,
    sibling_labels: Sequence[str],
    label_index: LabelIndex,
    bank_index: BankIndex,
    label_map: Dict[str, str],
) -> Optional[ConceptResult]:
    """Item contextual unic — enunț de domeniu + definiții omogene."""
    from scripts.domain_item_utils import labels_equivalent

    short = shorten_label(anchor_label)
    if labels_equivalent(short, domain):
        return None
    rec = lookup_best_record(label_index, short, domain)

    if rec:
        stem = rec.stem
        correct_def = rec.correct_definition
    else:
        correct_def = resolve_definition(short, label_index, label_map, domain)
        if not correct_def:
            return None
        if classify_option_form(correct_def) != "definition" and len(correct_def) < 28:
            return None
        stem = _natural_concept_stem(short, domain)

    used: Set[str] = {norm(correct_def)}
    distractors: List[str] = []

    for sib in sibling_labels:
        if norm(shorten_label(sib)) == norm(short):
            continue
        sib_def = resolve_definition(sib, label_index, label_map, domain)
        if sib_def and norm(sib_def) not in used:
            distractors.append(sib_def)
            used.add(norm(sib_def))

    pool = list(bank_index.definitions_by_domain.get(domain, []))
    if rec:
        for d in rec.option_definitions:
            if norm(d) not in used and d not in pool:
                pool.append(d)

    offset = 0
    while len(distractors) < 3:
        choice = _pick(pool, used, seed, offset)
        if not choice:
            choice = _pick(bank_index.definitions_other, used, seed, offset)
        if not choice:
            break
        distractors.append(choice)
        used.add(norm(choice))
        offset += 1
        if offset > 40:
            break

    if len(distractors) < 2:
        return None

    letters = ["a", "b", "c", "d"]
    all_opts = [correct_def] + distractors[:3]
    rot = seed % 4
    ordered = all_opts[rot:] + all_opts[:rot]
    options = {letters[i]: _cap_definition(ordered[i]) for i in range(4)}
    correct_letter = letters[ordered.index(correct_def)]
    return stem, options, correct_letter
