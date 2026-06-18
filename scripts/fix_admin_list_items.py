"""Elimină itemii tip listă administrativă — rescriere conceptuală."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.admin_list_specs import (
    infer_pool_from_options,
    pick_conceptual_spec,
    resolve_pool_key,
)
from scripts.distractor_fix import FORM_DEFINITION, FORM_TERM, classify_option_form
from scripts.fix_tf_items import is_tf_item

ADMIN_MARKER_RE = re.compile(
    r"\b(?:"
    r"forme ale|tipuri (?:de|ale)|concepte din|teme (?:din|care aparțin)|"
    r"aparțin domeniului|aparțin explicit"
    r")\b",
    re.IGNORECASE,
)
LIST_PICK_STEM_RE = re.compile(
    r"^Care dintre următoarele sunt\b",
    re.IGNORECASE,
)
TOPIC_LIST_STEM_RE = re.compile(
    r"^(?:În [^,]+,\s*)?.+?\s+(?:descriu?|se referă(?: la)?)\s*:\s*$",
    re.IGNORECASE,
)
TERM_PICK_STEM_RE = re.compile(
    r"(?:"
    r"stilul parental|tipul de atașament|tipuri de atașament|"
    r"stadiul|dimensiunea|teoria învățării|scala|clusterul"
    r")\b",
    re.IGNORECASE,
)

DEFINITION_HINT_RE = re.compile(
    r"^(?:gradul|măsura|stabilitatea|acoperirea|relația|interpretarea|"
    r"posibilitatea|consistența|folosirea|căutare|pattern|minimizarea|"
    r"cunoaștere|gândire|operații|raționament|modificarea|asocierea|"
    r"clasificarea|ordinea|distanțe|sociabilitate|tendința)",
    re.IGNORECASE,
)


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def is_short_label(text: str) -> bool:
    """Variantă scurtă (etichetă), nu explicație comparabilă."""
    t = (text or "").strip()
    if not t:
        return True
    if classify_option_form(t) == FORM_DEFINITION:
        if DEFINITION_HINT_RE.match(t) or t[0].islower():
            return False
        if len(t) > 52:
            return False
    if len(t) > 58:
        return False
    if DEFINITION_HINT_RE.match(t):
        return False
    if t[0].islower():
        return False
    words = t.split()
    if len(words) <= 7 and not t.endswith("."):
        return True
    return classify_option_form(t) == FORM_TERM


def options_are_short_labels(options: Dict[str, str]) -> bool:
    vals = [str(v).strip() for v in options.values() if (v or "").strip()]
    if len(vals) < 3:
        return False
    short = sum(1 for v in vals if is_short_label(v))
    return short >= max(3, len(vals) - 1)


def is_admin_list_item(item: Dict[str, Any]) -> bool:
    """Item care cere doar recunoașterea unei liste de etichete."""
    if is_tf_item(item):
        return False
    stem = _stem(item)
    opts = _options(item)
    if len(opts) < 4 or not options_are_short_labels(opts):
        return False

    pool = resolve_pool_key(stem) or infer_pool_from_options(opts)
    if not pool:
        return False

    if ADMIN_MARKER_RE.search(stem):
        return True
    if LIST_PICK_STEM_RE.match(stem):
        return True
    if TOPIC_LIST_STEM_RE.match(stem):
        return True
    if TERM_PICK_STEM_RE.search(stem):
        return True
    if str(item.get("kind") or "").lower() == "multi":
        return True
    return False


def _apply_spec(
    item: Dict[str, Any],
    stem: str,
    options: Dict[str, str],
    correct: str,
) -> Dict[str, Any]:
    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = stem
    if "text" in item:
        out["text"] = stem
    if "variante" in item:
        out["variante"] = options
    if "options" in item:
        out["options"] = options
    corr = [correct.lower()]
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    if "correct" in item:
        out["correct"] = corr
    out["kind"] = "single"
    out["tip"] = "unic"
    out["explicatie"] = ""
    out["explanation"] = ""
    return out


DEFINITION_STEM_RE = re.compile(
    r"se caracterizează|se referă la|reflectă cel mai bine|corespunde descrierii",
    re.IGNORECASE,
)
BARE_LABELS = frozenset(
    {
        "autoritativ",
        "autoritar",
        "permisiv",
        "neglijent",
        "securizant",
        "evitant",
        "dezorganizat",
        "ambivalent",
        "rezistent",
    }
)


def has_bare_label_options(options: Dict[str, str]) -> bool:
    for val in options.values():
        key = (val or "").strip().lower()
        if key in BARE_LABELS:
            return True
    return False


def fix_labeled_options_in_definition_stem(
    item: Dict[str, Any],
) -> Tuple[Dict[str, Any], bool]:
    """Enunț cere definiție, dar variantele sunt etichete goale (autoritativ, permisiv…)."""
    if is_tf_item(item):
        return item, False
    stem = _stem(item)
    if not DEFINITION_STEM_RE.search(stem):
        return item, False
    opts = _options(item)
    if not opts:
        return item, False
    if not has_bare_label_options(opts) and not options_are_short_labels(opts):
        return item, False
    built = pick_conceptual_spec(stem, _item_seed(item), opts)
    if not built:
        return item, False
    new_stem, new_options, correct_letter = built
    return _apply_spec(item, new_stem, new_options, correct_letter), True


def fix_admin_list_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    if not is_admin_list_item(item):
        return item, False

    stem = _stem(item)
    opts = _options(item)
    seed = _item_seed(item)
    built = pick_conceptual_spec(stem, seed, opts)
    if not built:
        return item, False

    new_stem, new_options, correct_letter = built
    return _apply_spec(item, new_stem, new_options, correct_letter), True


def audit_admin_list_items(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    hits: List[Dict[str, Any]] = []
    for item in items:
        if is_admin_list_item(item):
            hits.append(
                {
                    "id": item.get("id"),
                    "stem": _stem(item)[:120],
                    "options": list(_options(item).values())[:4],
                }
            )
    return {"count": len(hits), "items": hits}


def format_admin_list_report(report: Dict[str, Any]) -> str:
    lines = [
        "=" * 72,
        "AUDIT LISTE ADMINISTRATIVE (etichete scurte, fără înțelegere)",
        "=" * 72,
        f"Itemi rămași: {report['count']}",
        "",
    ]
    for entry in report.get("items", [])[:60]:
        lines.append(f"  id={entry['id']}: {entry['stem']}")
        for opt in entry.get("options", [])[:2]:
            lines.append(f"    - {opt[:70]}")
    if report["count"] > 60:
        lines.append(f"  ... și încă {report['count'] - 60}")
    if report["count"] == 0:
        lines.append("OK — nu mai există itemi tip listă administrativă.")
    lines.append("=" * 72)
    return "\n".join(lines)
