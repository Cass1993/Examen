"""Audit post-rescriere — pattern-uri interzise și probleme de construcție."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from typing import Any, Dict, Generator, List, Tuple

from scripts.audit_item_quality import (
    duplicate_option_texts,
    item_id,
    option_dict,
    stem_text,
    walk_items,
)
from scripts.distractor_fix import classify_option_form, norm, options_have_duplicates

FORBIDDEN_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("care_concept_corespunde", re.compile(r"care concept corespunde descrierii", re.I)),
    ("ce_termen_descris", re.compile(r"ce termen (?:este descris|corespunde)", re.I)),
    ("apartin_domeniului", re.compile(r"aparțin domeniului", re.I)),
    ("apartin_explicit", re.compile(r"aparțin explicit", re.I)),
    ("tematica_examen", re.compile(r"tematica de examen", re.I)),
    ("in_aceasta_tematica", re.compile(r"în această tematică", re.I)),
    ("sunt_dimensiuni_big_five", re.compile(r"sunt dimensiuni Big Five", re.I)),
    ("sunt_scale_masurare", re.compile(r"sunt scale de măsurare", re.I)),
    ("genetica_comportamentala", re.compile(r"aparțin geneticii comportamentale", re.I)),
    ("relatie_terapeutica_list", re.compile(r"pot aparține relației terapeutice", re.I)),
    ("broken_category_descriu", re.compile(r"(?:în psihologia|în [^,]+,\s*).+\s+descriu?:\s*$", re.I)),
    ("afirmatia_urmatoare", re.compile(r"afirmația următoare este corectă", re.I)),
    ("ghilimele_angle", re.compile(r"«")),
]

ABSOLUTE_IN_OPTIONS = re.compile(
    r"\b(doar|exclusiv|obligatoriu|întotdeauna|niciodată)\b", re.I
)

LENGTH_RATIO = 1.75


def _similar(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def audit_forbidden(data: Any) -> Dict[str, Any]:
    """Returnează raport structurat cu toate problemele detectate."""
    report: Dict[str, Any] = {
        "total_items": 0,
        "forbidden_stem": defaultdict(list),
        "absolute_in_wrong_options": [],
        "length_imbalance": [],
        "duplicate_options": [],
        "similar_options": [],
        "heterogeneous_options": [],
        "counts": Counter(),
    }

    for lot, item in walk_items(data):
        report["total_items"] += 1
        iid = item_id(item, lot)
        stem = stem_text(item)
        opts = option_dict(item)
        correct = {str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])}

        for key, pat in FORBIDDEN_PATTERNS:
            if pat.search(stem):
                report["forbidden_stem"][key].append(iid)
                report["counts"][key] += 1

        for letter, text in opts.items():
            if letter in correct:
                continue
            if ABSOLUTE_IN_OPTIONS.search(text):
                corr_has = any(
                    ABSOLUTE_IN_OPTIONS.search(opts[c]) for c in correct if c in opts
                )
                if not corr_has:
                    report["absolute_in_wrong_options"].append(
                        {"id": iid, "letter": letter, "text": text[:120]}
                    )
                    report["counts"]["absolute_wrong"] += 1

        if len(correct) == 1 and correct & set(opts.keys()):
            c = next(iter(correct))
            corr_len = len(opts.get(c, ""))
            wrong = [len(opts[k]) for k in opts if k not in correct]
            if wrong:
                avg = sum(wrong) / len(wrong)
                if avg > 15 and corr_len > avg * LENGTH_RATIO and corr_len - avg > 35:
                    report["length_imbalance"].append(
                        {
                            "id": iid,
                            "correct_len": corr_len,
                            "avg_wrong": round(avg, 1),
                        }
                    )
                    report["counts"]["length_imbalance"] += 1

        dups = duplicate_option_texts(item)
        if dups:
            report["duplicate_options"].append({"id": iid, "duplicates": dups})
            report["counts"]["duplicate_options"] += 1

        if options_have_duplicates(opts):
            pass  # already counted

        letters = sorted(opts.keys())
        for i, la in enumerate(letters):
            for lb in letters[i + 1 :]:
                if _similar(opts[la], opts[lb]) >= 0.88:
                    report["similar_options"].append(
                        {"id": iid, "a": opts[la][:80], "b": opts[lb][:80]}
                    )
                    report["counts"]["similar_options"] += 1
                    break

        forms = {classify_option_form(v) for v in opts.values() if v}
        if len(forms) > 1:
            report["heterogeneous_options"].append(
                {"id": iid, "forms": sorted(forms), "stem": stem[:100]}
            )
            report["counts"]["heterogeneous_options"] += 1

    report["forbidden_stem"] = dict(report["forbidden_stem"])
    return report


def format_audit_report(report: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("=" * 72)
    lines.append("AUDIT BANCĂ — PATTERN-URI INTERZISE ȘI CALITATE CONSTRUCȚIE")
    lines.append("=" * 72)
    lines.append(f"Total itemi: {report['total_items']}")
    lines.append("")

    lines.append("--- Pattern-uri interzise în enunț ---")
    for key, ids in sorted(report.get("forbidden_stem", {}).items()):
        lines.append(f"  {key}: {len(ids)} itemi")
        for iid in ids[:15]:
            lines.append(f"    - {iid}")
        if len(ids) > 15:
            lines.append(f"    ... și încă {len(ids) - 15}")
    if not report.get("forbidden_stem"):
        lines.append("  (niciun pattern interzis în enunț)")
    lines.append("")

    sections = [
        ("absolute_in_wrong_options", "Absolutisme în variante greșite (fără absolut în corect)"),
        ("length_imbalance", "Răspuns corect mult mai lung decât distractorii"),
        ("duplicate_options", "Variante duplicate"),
        ("similar_options", "Variante foarte asemănătoare (≥88%)"),
        ("heterogeneous_options", "Variante din categorii logice diferite"),
    ]
    for key, title in sections:
        items = report.get(key, [])
        lines.append(f"--- {title}: {len(items)} ---")
        for entry in items[:20]:
            lines.append(f"  {entry}")
        if len(items) > 20:
            lines.append(f"  ... și încă {len(items) - 20}")
        lines.append("")

    lines.append("--- Rezumat contoare ---")
    for k, v in sorted(report.get("counts", {}).items()):
        lines.append(f"  {k}: {v}")

    total_issues = sum(report.get("counts", {}).values())
    lines.append("")
    lines.append(f"Total probleme flagate: {total_issues}")
    lines.append("=" * 72)
    return "\n".join(lines)
