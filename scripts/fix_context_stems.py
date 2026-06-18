"""Adaugă context de domeniu enunțurilor vagi + variante omogene."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.concept_context_specs import (
    build_contextual_item,
    context_prefix_for_lot,
    lookup_context_spec,
)
from scripts.fix_tf_items import is_tf_item

HAS_CONTEXT_RE = re.compile(
    r"^(?:În |Care |Ce |Când |La |Referitor |Contribuția |Modelul |Terapia |"
    r"Psihoterapia |În abordarea |În teoria |În evaluarea |În statistica |"
    r"Dimensiunea |Stadiul |Clusterul )",
    re.IGNORECASE,
)

BARE_STEM_RE = re.compile(
    r"^(?P<label>.+?)\s+"
    r"(?P<verb>descriu?|se referă(?: cel mai bine)? la|indică|presupune|"
    r"înseamnă|exprimă|postulează|este caracterizat[ăa] prin)\s*:?\s*$",
    re.IGNORECASE,
)

# enunțuri care au deja context în subiect
EMBEDDED_CONTEXT_RE = re.compile(
    r"(?:în testarea statistică|într-un (?:studiu|test)|în condiționarea|"
    r"în evaluarea performanței|în psihoterapia|în teoria|în etica|"
    r"^Procedura |^Eroarea de tip |^Valoarea p |^Mărimea efectului )",
    re.IGNORECASE,
)

VAGUE_AUDIT_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("relații duale", re.compile(r"^Relațiile duale\s+descriu?", re.I)),
    ("transfer", re.compile(r"^Transferul\s+descriu?", re.I)),
    ("atașament", re.compile(r"^Atașamentul\s+descriu?", re.I)),
    ("validitate", re.compile(r"^Validitatea\s+descriu?", re.I)),
    ("fidelitate", re.compile(r"^Fidelitatea\s+descriu?", re.I)),
    ("criteriul", re.compile(r"^Criteriul\s+descriu?", re.I)),
    ("eșantion", re.compile(r"^Eșantionul\s+descriu?", re.I)),
    ("climat", re.compile(r"^Climatul\s+descriu?", re.I)),
    ("bare_descriu", re.compile(r"^(?!În )[^?]{3,55}\s+descriu?:\s*$", re.I)),
    ("bare_se_refera", re.compile(r"^(?!În )[^?]{3,55}\s+se referă la:\s*$", re.I)),
]


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def is_vague_stem(stem: str) -> bool:
    text = (stem or "").strip()
    if not text:
        return False
    if HAS_CONTEXT_RE.match(text):
        return False
    m = BARE_STEM_RE.match(text)
    if not m:
        return False
    label = m.group("label").strip()
    if EMBEDDED_CONTEXT_RE.search(label):
        return False
    if len(label) > 85:
        return False
    return True


def extract_bare_label(stem: str) -> Optional[str]:
    m = BARE_STEM_RE.match((stem or "").strip())
    return m.group("label").strip() if m else None


def contextualize_stem_generic(label: str, lot: str, verb: str = "se referă la") -> str:
    prefix = context_prefix_for_lot(lot, label)
    clean = label.strip().strip("«»")
    if clean and clean[0].isupper() and len(clean.split()) <= 6:
        phrase = clean[0].lower() + clean[1:]
    else:
        phrase = clean
    verb_norm = verb.lower().replace("descrie", "se referă la").replace("descriu", "se referă la")
    if not verb_norm.endswith(":"):
        verb_norm = verb_norm.rstrip(":") + ":"
    return f"{prefix}, {phrase} {verb_norm}"


def audit_vague_stems(data: Any) -> Dict[str, Any]:
    from scripts.audit_item_quality import item_id, walk_items

    report: Dict[str, Any] = {"total": 0, "vague_count": 0, "by_pattern": {}, "items": []}
    for lot, item in walk_items(data):
        report["total"] += 1
        stem = _stem(item)
        if not is_vague_stem(stem):
            continue
        report["vague_count"] += 1
        matched = [name for name, pat in VAGUE_AUDIT_PATTERNS if pat.search(stem)]
        for name in matched or ["other_vague"]:
            report["by_pattern"][name] = report["by_pattern"].get(name, 0) + 1
        report["items"].append({"id": item_id(item, lot), "lot": lot, "stem": stem[:120]})
    return report


def format_vague_audit(report: Dict[str, Any]) -> str:
    lines = [
        "=" * 72,
        "AUDIT ENUNȚURI VAGI (fără context de domeniu)",
        "=" * 72,
        f"Total itemi: {report['total']}",
        f"Enunțuri vagi: {report['vague_count']}",
        "",
    ]
    if report.get("by_pattern"):
        lines.append("--- Pattern-uri ---")
        for k, v in sorted(report["by_pattern"].items(), key=lambda x: -x[1]):
            lines.append(f"  {k}: {v}")
        lines.append("")
    for entry in report.get("items", [])[:40]:
        lines.append(f"  [{entry['id']}] {entry['stem']}")
    if report["vague_count"] == 0:
        lines.append("OK — nu mai există enunțuri vagi fără context.")
    lines.append("=" * 72)
    return "\n".join(lines)


def fix_context_stem_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    if is_tf_item(item):
        return item, False

    stem = _stem(item)
    if not is_vague_stem(stem):
        return item, False

    lot = str(item.get("domeniu") or item.get("lot") or "").strip()
    label = extract_bare_label(stem) or stem
    seed = _item_seed(item)

    built = build_contextual_item(label, lot, seed)
    if built:
        new_stem, new_opts, corr = built
        out = dict(item)
        if "intrebare" in item:
            out["intrebare"] = new_stem
        if "text" in item:
            out["text"] = new_stem
        if "variante" in item:
            out["variante"] = new_opts
        if "options" in item:
            out["options"] = new_opts
        corr_list = [str(corr).lower()]
        if "raspuns_corect" in item:
            out["raspuns_corect"] = corr_list
        if "correct" in item:
            out["correct"] = corr_list
        out["kind"] = "single"
        out["tip"] = "unic"
        return out, True

    m = BARE_STEM_RE.match(stem)
    verb = m.group("verb") if m else "se referă la"
    new_stem = contextualize_stem_generic(label, lot, verb)
    if new_stem == stem:
        return item, False

    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    return out, True
