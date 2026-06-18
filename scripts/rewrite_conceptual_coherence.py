"""Audit și rescriere — variante din aceeași familie conceptuală cu enunțul."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.audit_item_quality import walk_items
from scripts.concept_clusters import build_concept_item, lookup_concept, rotate_options
from scripts.concept_families import (
    FAMILY_DEFINITION_POOLS,
    FAMILY_TERM_POOLS,
    anchor_families,
    distractor_out_of_anchor,
    family_from_stem,
    is_cross_family_distractor,
    primary_families,
    resolve_target_family,
)
from scripts.distractor_fix import (
    BankIndex,
    FORM_AUTHOR,
    FORM_DEFINITION,
    FORM_TERM,
    classify_option_form,
    norm,
)
from scripts.domain_concept_specs import build_domain_concept_item
from scripts.association_pair_fix import fix_association_pairs, needs_association_fix
from scripts.fix_tf_items import is_tf_item
from scripts.term_clusters import (
    build_definition_cluster_options,
    build_term_cluster_options,
)

STEM_SPEC_RULES: List[Tuple[re.Pattern[str], str]] = [
    (
        re.compile(
            r"genetic[aă] comportamental|studiile gemenare|studiile de gemeni|"
            r"gemenilor monozigoți|eritabilit",
            re.I,
        ),
        "studiile gemelare",
    ),
    (re.compile(r"job enlargement|lărgirea postului|lărgire.*post", re.I), "job enlargement"),
    (re.compile(r"job enrichment|îmbogățirea postului|îmbogățire.*post", re.I), "job enrichment"),
    (re.compile(r"transdiagnostic", re.I), "abordarea transdiagnostică"),
    (re.compile(r"cluster(?:ul)?\s+a\b", re.I), "clusterul a"),
    (re.compile(r"cluster(?:ul)?\s+b\b", re.I), "clusterul b"),
    (re.compile(r"cluster(?:ul)?\s+c\b", re.I), "clusterul c"),
    (
        re.compile(r"cognitiv-comportamental|tcc\b|terapia cognitiv", re.I),
        "psihoterapia cognitiv-comportamentală",
    ),
    (re.compile(r"psihodinamic", re.I), "psihoterapia psihodinamică"),
    (re.compile(r"acceptare și angajament|\bact\b", re.I), "terapia de acceptare și angajament"),
    (re.compile(r"dialectic-comportamental|\bdbt\b", re.I), "terapia dialectic-comportamentală"),
    (
        re.compile(
            r"focalizat[aă].*emoț|abordarea terapia|procesar.*transform.*emoț",
            re.I,
        ),
        "terapia focalizată pe emoții",
    ),
    (re.compile(r"schema therapy|terapia schemelor", re.I), "terapia schemelor"),
]


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def _correct(item: Dict[str, Any]) -> List[str]:
    return [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]


def _domain(item: Dict[str, Any], lot: str = "") -> str:
    return str(item.get("domeniu") or item.get("lot") or lot or "").strip()


def _option_forms(options: Dict[str, str]) -> Set[str]:
    return {classify_option_form(v) for v in options.values() if v}


def _correct_texts(item: Dict[str, Any]) -> List[str]:
    opts = _options(item)
    return [str(opts[c]) for c in _correct(item) if c in opts]


def has_family_mismatch(item: Dict[str, Any], lot: str = "") -> bool:
    """Detectează variante din alte capitole față de enunț + răspuns corect."""
    if is_tf_item(item):
        return False
    if needs_association_fix(item):
        return True
    opts = _options(item)
    if len(opts) < 3:
        return False
    stem = _stem(item)
    domain = _domain(item, lot)
    correct = set(_correct(item))
    anchor = anchor_families(stem, domain, _correct_texts(item))
    if not anchor:
        return False
    for letter, text in opts.items():
        if letter in correct:
            continue
        if distractor_out_of_anchor(str(text), anchor, stem):
            return True
    return False


def _validate_rebuild(item: Dict[str, Any], lot: str = "") -> bool:
    """Respinge rescrieri care încă amestecă capitole."""
    return not has_family_mismatch(item, lot) and audit_item_coherence(item, lot) is None


def audit_item_coherence(
    item: Dict[str, Any], lot: str = ""
) -> Optional[Dict[str, Any]]:
    """Returnează detalii problemă sau None dacă itemul e coerent."""
    if is_tf_item(item):
        return None

    opts = _options(item)
    if len(opts) < 3:
        return None

    stem = _stem(item)
    domain = _domain(item, lot)
    correct = set(_correct(item))
    correct_texts = _correct_texts(item)
    anchor = anchor_families(stem, domain, correct_texts)
    stem_family = resolve_target_family(stem, domain, correct_texts)

    forms = _option_forms(opts)
    if len(forms) > 1 and FORM_AUTHOR in forms:
        return {
            "reason": "mixed_forms_author",
            "stem_family": stem_family,
            "forms": sorted(forms),
        }

    if len(forms) > 1:
        return {
            "reason": "mixed_forms",
            "stem_family": stem_family,
            "forms": sorted(forms),
        }

    if needs_association_fix(item):
        return {
            "reason": "association_inhomogeneous",
            "stem_family": stem_family,
        }

    bad_distractors: List[str] = []
    for letter, text in opts.items():
        if letter in correct:
            continue
        if anchor and distractor_out_of_anchor(str(text), anchor, stem):
            bad_distractors.append(f"{letter}:{str(text)[:70]}")
        elif is_cross_family_distractor(str(text), stem_family or "", stem):
            bad_distractors.append(f"{letter}:{str(text)[:70]}")

    if bad_distractors:
        return {
            "reason": "cross_chapter_distractors",
            "stem_family": stem_family,
            "anchor": sorted(anchor),
            "bad": bad_distractors,
        }

    lengths = [len(v) for v in opts.values()]
    if lengths:
        mx, mn = max(lengths), min(lengths)
        if mx > 55 and mn < 35 and mx > mn * 2.2:
            short_terms = sum(
                1 for v in opts.values() if classify_option_form(v) == FORM_TERM and len(v) < 45
            )
            long_defs = sum(1 for v in opts.values() if len(v) > 55)
            if short_terms >= 1 and long_defs >= 1:
                return {
                    "reason": "length_imbalance_mixed_register",
                    "stem_family": stem_family,
                }

    return None


def audit_bank_coherence(data: Any) -> Dict[str, Any]:
    issues: List[Dict[str, Any]] = []
    by_reason: Dict[str, int] = {}
    total = 0

    for lot, item in walk_items(data):
        total += 1
        if is_tf_item(item):
            continue
        problem = audit_item_coherence(item, lot)
        if problem:
            iid = f"{lot}#{item.get('id', '?')}"
            entry = {"id": iid, "stem": _stem(item)[:100], **problem}
            issues.append(entry)
            by_reason[problem["reason"]] = by_reason.get(problem["reason"], 0) + 1

    return {
        "total_items": total,
        "incoherent_count": len(issues),
        "by_reason": by_reason,
        "issues": issues,
    }


def format_coherence_report(report: Dict[str, Any]) -> str:
    lines = [
        "=" * 72,
        "AUDIT COERENȚĂ CONCEPTUALĂ — STEM / VARIANTE",
        "=" * 72,
        f"Total itemi parcurși: {report['total_items']}",
        f"Itemi incoerenți: {report['incoherent_count']}",
        "",
        "--- După tip de problemă ---",
    ]
    for reason, count in sorted(report.get("by_reason", {}).items()):
        lines.append(f"  {reason}: {count}")
    lines.append("")
    lines.append("--- Exemple (max 40) ---")
    for entry in report.get("issues", [])[:40]:
        lines.append(f"  [{entry['id']}] {entry.get('reason')}")
        lines.append(f"    stem: {entry.get('stem', '')}")
        if entry.get("bad"):
            for b in entry["bad"][:3]:
                lines.append(f"    ✗ {b}")
        if entry.get("forms"):
            lines.append(f"    forms: {entry['forms']}")
    if report["incoherent_count"] > 40:
        lines.append(f"  ... și încă {report['incoherent_count'] - 40}")
    lines.append("")
    if report["incoherent_count"] == 0:
        lines.append("OK — nu s-au detectat amestecuri evidente stem/variante.")
    lines.append("=" * 72)
    return "\n".join(lines)


def _lookup_stem_spec(stem: str) -> Optional[str]:
    for pattern, spec_key in STEM_SPEC_RULES:
        if pattern.search(stem):
            return spec_key
    return None


def _apply_spec(
    item: Dict[str, Any], spec_key: str, seed: int, lot: str = ""
) -> Optional[Dict[str, Any]]:
    built = build_concept_item(spec_key, seed)
    if not built:
        return None
    new_stem, new_opts, corr = built
    merged = _merge_item(item, new_stem, new_opts, [corr])
    return merged if _validate_rebuild(merged, lot) else None


def _rebuild_from_family_pool(
    item: Dict[str, Any],
    family: str,
    correct_text: str,
    seed: int,
    lot: str = "",
) -> Optional[Dict[str, Any]]:
    target_form = classify_option_form(correct_text)
    pool: List[str] = []

    if target_form == FORM_TERM:
        pool = list(FAMILY_TERM_POOLS.get(family, []))
    if len(pool) < 4:
        pool = list(FAMILY_DEFINITION_POOLS.get(family, []))
    if len(pool) < 4:
        return None

    ct = correct_text.strip()
    if ct and not any(norm(ct) == norm(p) or norm(ct) in norm(p) or norm(p) in norm(ct) for p in pool):
        pool.insert(0, ct)

    if target_form == FORM_TERM:
        built = build_term_cluster_options(pool, ct or pool[0], seed)
    else:
        built = build_definition_cluster_options(pool, ct or pool[0], seed)

    if not built:
        return None
    new_opts, corr = built
    merged = _merge_item(item, _stem(item), new_opts, [corr])
    return merged if _validate_rebuild(merged, lot) else None


def _merge_item(
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
        out["kind"] = out.get("kind") or "single"
        out["tip"] = out.get("tip") or "unic"
    return out


def rewrite_item_coherence(
    item: Dict[str, Any],
    index: Optional[BankIndex] = None,
    lot: str = "",
) -> Tuple[Dict[str, Any], bool]:
    """Rescrie item cu variante din alt capitol — păstrează conceptul testat."""
    if is_tf_item(item):
        return item, False

    needs_fix = has_family_mismatch(item, lot) or audit_item_coherence(item, lot) is not None
    if not needs_fix:
        return item, False

    fixed_assoc, ch_assoc = fix_association_pairs(item)
    if ch_assoc:
        item = fixed_assoc
        if not has_family_mismatch(item, lot) and audit_item_coherence(item, lot) is None:
            return item, True

    stem = _stem(item)
    correct_texts = _correct_texts(item)
    domain = _domain(item, lot)
    seed = _item_seed(item)

    spec_key = _lookup_stem_spec(stem)
    if spec_key:
        rebuilt = _apply_spec(item, spec_key, seed, lot)
        if rebuilt:
            return rebuilt, True

    for label in correct_texts:
        built = build_domain_concept_item(label, seed)
        if built:
            new_stem, new_opts, corr = built
            merged = _merge_item(item, new_stem, new_opts, [corr])
            if _validate_rebuild(merged, lot):
                return merged, True
        built2 = build_concept_item(label, seed)
        if built2:
            new_stem, new_opts, corr = built2
            merged = _merge_item(item, new_stem, new_opts, [corr])
            if _validate_rebuild(merged, lot):
                return merged, True

    for label in correct_texts:
        spec = lookup_concept(label)
        if spec:
            new_stem, new_opts, corr = rotate_options(spec, seed)
            merged = _merge_item(item, new_stem, new_opts, [corr])
            if _validate_rebuild(merged, lot):
                return merged, True

    family = resolve_target_family(stem, domain, correct_texts)
    if family and correct_texts:
        primary = max(correct_texts, key=len)
        rebuilt = _rebuild_from_family_pool(item, family, primary, seed, lot)
        if rebuilt:
            return rebuilt, True

    return item, False


def rewrite_bank_coherence(
    data: Any, index: Optional[BankIndex] = None
) -> Tuple[Any, int]:
    changed = 0
    if isinstance(data, dict) and "lots" in data:
        for lot_name, lot_data in data.get("lots", {}).items():
            questions = lot_data.get("questions", [])
            for i, q in enumerate(questions):
                new_q, ch = rewrite_item_coherence(q, index, lot_name)
                if ch:
                    questions[i] = new_q
                    changed += 1
    elif isinstance(data, list):
        for i, q in enumerate(data):
            new_q, ch = rewrite_item_coherence(q, index)
            if ch:
                data[i] = new_q
                changed += 1
    return data, changed
