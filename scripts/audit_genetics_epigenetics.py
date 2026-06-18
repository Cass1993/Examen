"""Audit itemi genetică comportamentală / epigenetică."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

FORBIDDEN_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("concepte genetice și epigenetice", re.compile(r"concepte\s+genetice\s+și\s+epigenetice", re.I)),
    ("genetice și epigenetice se referă", re.compile(r"genetice\s+și\s+epigenetice\s+se\s+referă", re.I)),
    ("modelul modelul", re.compile(r"modelul\s+modelul", re.I)),
    ("modelul genetic aditiv (titlu)", re.compile(r"modelul\s+genetic\s+aditiv,\s*mediu\s+comun", re.I)),
    ("mediu unic", re.compile(r"\bmediu\s+unic\b", re.I)),
    ("mediu necomun", re.compile(r"\bmediu\s+necomun\b", re.I)),
    ("genetica se referă la (vag)", re.compile(r"genetica\s+se\s+referă\s+la", re.I)),
    ("aparțin geneticii comportamentale", re.compile(r"aparțin\s+geneticii\s+comportamentale", re.I)),
    ("enunț gol Epigenetica descrie", re.compile(r"^Epigenetica\s+descriu?:\s*$", re.I)),
]

CROSS_FAMILY_DISTRACTORS = re.compile(
    r"atașament|validitate de criteriu|psihoterapie|analiza muncii|"
    r"zona proximă|big five|stadii psihosexual|stadii psihosocial|conservarea cantității",
    re.I,
)

GENETICS_MARKER = re.compile(
    r"genetic|epigenet|gemen|eritabil|model\s*ace|mediu\s+comun|gwas|metilare|polimorfism",
    re.I,
)


def _blob(item: Dict[str, Any]) -> str:
    parts = [str(item.get("text") or item.get("intrebare") or "")]
    opts = item.get("options") or item.get("variante") or {}
    if isinstance(opts, dict):
        parts.extend(str(v) for v in opts.values())
    return " ".join(parts)


def audit_genetics_items(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    forbidden_hits: List[Dict[str, Any]] = []
    cross_family: List[Dict[str, Any]] = []
    genetics_count = 0

    for item in items:
        blob = _blob(item)
        if not GENETICS_MARKER.search(blob):
            continue
        genetics_count += 1
        text = str(item.get("text") or item.get("intrebare") or "")
        for label, pat in FORBIDDEN_PATTERNS:
            if pat.search(blob) or pat.search(text):
                forbidden_hits.append(
                    {
                        "id": item.get("id"),
                        "pattern": label,
                        "text": text[:120],
                    }
                )
                break
        if GENETICS_MARKER.search(blob) and CROSS_FAMILY_DISTRACTORS.search(blob):
            # exclude when stem explicitly about personality models with genetics option
            if not re.search(r"big five|modelul celor cinci", text, re.I):
                cross_family.append(
                    {
                        "id": item.get("id"),
                        "text": text[:120],
                    }
                )

    return {
        "genetics_items": genetics_count,
        "forbidden_hits": forbidden_hits,
        "cross_family_distractors": cross_family,
    }


def format_genetics_audit_report(result: Dict[str, Any]) -> str:
    lines = [
        "=== Audit genetică comportamentală / epigenetică ===",
        f"Itemi marcați genetică/epigenetică: {result['genetics_items']}",
        f"Încălcări pattern interzis: {len(result['forbidden_hits'])}",
        f"Distractori din capitole diferite: {len(result['cross_family_distractors'])}",
        "",
    ]
    if result["forbidden_hits"]:
        lines.append("--- Pattern-uri interzise rămase ---")
        for hit in result["forbidden_hits"][:80]:
            lines.append(f"  id={hit['id']} [{hit['pattern']}]: {hit['text']}")
        if len(result["forbidden_hits"]) > 80:
            lines.append(f"  ... și încă {len(result['forbidden_hits']) - 80}")
        lines.append("")
    if result["cross_family_distractors"]:
        lines.append("--- Distractori cross-family ---")
        for hit in result["cross_family_distractors"][:40]:
            lines.append(f"  id={hit['id']}: {hit['text']}")
        lines.append("")
    if not result["forbidden_hits"] and not result["cross_family_distractors"]:
        lines.append("OK — niciun pattern interzis detectat în itemii genetici.")
    return "\n".join(lines)
