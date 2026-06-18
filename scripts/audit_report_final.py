"""Audit final — toate regulile metodologice pentru questions_clean_final."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any, Dict, List, Tuple

from scripts.audit_item_quality import item_id, option_dict, stem_text, walk_items
from scripts.bank_audit_forbidden import audit_forbidden, format_audit_report
from scripts.distractor_fix import classify_option_form, norm
from scripts.domain_item_utils import is_domain_belonging_item
from scripts.fix_category_list_stems import is_broken_category_list_stem
from scripts.fix_context_stems import audit_vague_stems, format_vague_audit, is_vague_stem
from scripts.fix_tf_items import is_tf_item
from scripts.rewrite_conceptual_coherence import audit_bank_coherence, format_coherence_report

FINAL_FORBIDDEN: List[Tuple[str, re.Pattern[str]]] = [
    ("broken_category_stem", re.compile(r"\bdescriu?:\s*$", re.I)),
    ("afirmatia_urmatoare", re.compile(r"afirmația următoare este corectă", re.I)),
    ("in_psihologia_x_descrie", re.compile(r"în psihologia .+ descriu?:\s*$", re.I)),
]

ABSOLUTE_DISTRACTOR = re.compile(
    r"\b(doar|exclusiv|obligatoriu|întotdeauna|niciodată|complet|automat)\b",
    re.I,
)


def _tf_invalid(item: Dict[str, Any]) -> bool:
    if not is_tf_item(item):
        return False
    opts = option_dict(item)
    vals = {norm(v) for v in opts.values()}
    return vals != {"adevărat", "fals"} and vals != {"adevarat", "fals"}


def audit_final(data: Any) -> Dict[str, Any]:
    base = audit_forbidden(data)
    coherence = audit_bank_coherence(data)

    report: Dict[str, Any] = {
        "total_items": 0,
        "forbidden_stem": dict(base.get("forbidden_stem", {})),
        "final_forbidden": defaultdict(list),
        "domain_belonging": [],
        "broken_category": [],
        "tf_invalid": [],
        "vague_stems": [],
        "absolute_distractors": list(base.get("absolute_in_wrong_options", [])),
        "length_imbalance": list(base.get("length_imbalance", [])),
        "heterogeneous": list(base.get("heterogeneous_options", [])),
        "coherence_issues": coherence.get("incoherent_count", 0),
        "counts": Counter(base.get("counts", {})),
    }

    for lot, item in walk_items(data):
        report["total_items"] += 1
        iid = item_id(item, lot)
        stem = stem_text(item)

        for key, pat in FINAL_FORBIDDEN:
            if pat.search(stem):
                report["final_forbidden"][key].append(iid)
                report["counts"][key] += 1

        if is_domain_belonging_item(item):
            report["domain_belonging"].append(iid)
            report["counts"]["domain_belonging"] += 1

        if is_broken_category_list_stem(stem):
            report["broken_category"].append(iid)
            report["counts"]["broken_category"] += 1

        if _tf_invalid(item):
            report["tf_invalid"].append(iid)
            report["counts"]["tf_invalid"] += 1

        if is_vague_stem(stem):
            report["vague_stems"].append(iid)
            report["counts"]["vague_stem"] += 1

        opts = option_dict(item)
        correct = {str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])}
        for letter, text in opts.items():
            if letter in correct:
                continue
            if ABSOLUTE_DISTRACTOR.search(text):
                if not any(ABSOLUTE_DISTRACTOR.search(opts.get(c, "")) for c in correct if c in opts):
                    report["counts"]["absolute_distractor_strict"] += 1

    report["final_forbidden"] = dict(report["final_forbidden"])
    report["coherence_summary"] = coherence
    return report


def format_final_audit_report(report: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("=" * 72)
    lines.append("AUDIT FINAL — questions_clean_final")
    lines.append("=" * 72)
    lines.append(f"Total itemi: {report['total_items']}")
    lines.append("")

    lines.append("--- Pattern-uri interzise (bază) ---")
    for key, ids in sorted(report.get("forbidden_stem", {}).items()):
        lines.append(f"  {key}: {len(ids)}")
    lines.append("")

    lines.append("--- Pattern-uri interzise (final) ---")
    for key, ids in sorted(report.get("final_forbidden", {}).items()):
        lines.append(f"  {key}: {len(ids)}")
        for iid in ids[:8]:
            lines.append(f"    - {iid}")
    if not report.get("final_forbidden"):
        lines.append("  (niciunul)")
    lines.append("")

    for label, key in (
        ("Itemi «aparțin domeniului»", "domain_belonging"),
        ("Enunțuri rupte «X descriu:»", "broken_category"),
        ("Itemi A/F invalizi", "tf_invalid"),
        ("Enunțuri vagi fără context", "vague_stems"),
    ):
        items = report.get(key, [])
        lines.append(f"--- {label}: {len(items)} ---")
        for iid in items[:15]:
            lines.append(f"  - {iid}")
        if len(items) > 15:
            lines.append(f"  ... și încă {len(items) - 15}")
        lines.append("")

    lines.append(f"--- Incoerență conceptuală (variante): {report.get('coherence_issues', 0)} ---")
    lines.append(f"--- Variante eterogene (formă): {len(report.get('heterogeneous', []))} ---")
    lines.append(f"--- Răspuns corect mult mai lung: {len(report.get('length_imbalance', []))} ---")
    lines.append("")

    lines.append("--- Contoare ---")
    for k, v in sorted(report.get("counts", {}).items()):
        lines.append(f"  {k}: {v}")

    total_flags = sum(report.get("counts", {}).values())
    total_flags += len(report.get("domain_belonging", []))
    total_flags += len(report.get("broken_category", []))
    total_flags += len(report.get("tf_invalid", []))
    total_flags += report.get("coherence_issues", 0)

    lines.append("")
    lines.append(f"Total probleme flagate (aprox.): {total_flags}")
    if (
        not report.get("forbidden_stem")
        and not report.get("final_forbidden")
        and not report.get("domain_belonging")
        and not report.get("broken_category")
        and report.get("coherence_issues", 0) == 0
    ):
        lines.append("")
        lines.append("OK — banca trece auditul final de bază.")
    lines.append("=" * 72)

    lines.append("")
    lines.append(
        format_audit_report(
            {
                "total_items": report["total_items"],
                "forbidden_stem": report.get("forbidden_stem", {}),
                "counts": report.get("counts", {}),
                "absolute_in_wrong_options": report.get("absolute_distractors", []),
                "length_imbalance": report.get("length_imbalance", []),
                "duplicate_options": [],
                "similar_options": [],
                "heterogeneous_options": report.get("heterogeneous", []),
            }
        )
    )

    coh = report.get("coherence_summary")
    if coh and coh.get("incoherent_count", 0) > 0:
        lines.append("")
        lines.append(format_coherence_report(coh))

    return "\n".join(lines)
