"""Itemi A/F neterminați — conversie la propoziție completă sau item conceptual."""

from __future__ import annotations

import copy
import hashlib
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.fix_tf_items import TF_OPTIONS, is_tf_item
from scripts.incomplete_tf_specs import build_from_spec, lookup_incomplete_spec

INCOMPLETE_TF_RE = re.compile(
    r"(?:"
    r"este asociat[aă]|se referă la|descrie|presupune|vizează|indică|"
    r"constă în|are ca scop|este caracterizat[aă] prin"
    r")\s*:\s*\.?\s*$",
    re.IGNORECASE,
)


def _norm_stem(stem: str) -> str:
    return re.sub(r"\s+", " ", (stem or "").strip())


def is_incomplete_tf_stem(stem: str) -> bool:
    """Enunț care cere completare (termină cu două puncte), nu propoziție A/F."""
    t = _norm_stem(stem)
    t = re.sub(r"[.:?\s]+$", "", t)
    return bool(INCOMPLETE_TF_RE.search(t + ":"))


def is_incomplete_tf_item(item: Dict[str, Any]) -> bool:
    if not is_tf_item(item):
        return False
    stem = str(item.get("intrebare") or item.get("text") or "")
    return is_incomplete_tf_stem(stem)


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _apply_conceptual(item: Dict[str, Any], stem: str, options: Dict[str, str], correct: List[str]) -> Dict[str, Any]:
    out = copy.deepcopy(item)
    if "text" in out:
        out["text"] = stem
    if "intrebare" in out:
        out["intrebare"] = stem
    if "options" in out:
        out["options"] = options
    if "variante" in out:
        out["variante"] = options
    if "correct" in out:
        out["correct"] = correct
    if "raspuns_corect" in out:
        out["raspuns_corect"] = correct
    out["kind"] = "single"
    out["tip"] = "unic"
    return out


def _try_author_conceptual(item: Dict[str, Any], seed: int) -> Optional[Dict[str, Any]]:
    from scripts.author_knowledge import (
        build_cluster_options,
        cluster_for_author,
        lookup_author_by_stem,
        natural_stem_for_author,
    )

    stem = _norm_stem(str(item.get("text") or item.get("intrebare") or ""))
    author = lookup_author_by_stem(stem)
    if not author:
        return None
    cluster = cluster_for_author(author)
    if not cluster:
        return None
    built = build_cluster_options(cluster, author, seed)
    natural = natural_stem_for_author(author)
    if not built or not natural:
        return None
    options, correct_letter = built
    stem_out = natural
    if stem_out.rstrip().endswith(":"):
        stem_out = stem_out.rstrip()[:-1] + " mai ales cu:"
    return _apply_conceptual(item, stem_out, options, [correct_letter])


def fix_incomplete_tf_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """Convertește item A/F neterminat în item conceptual (preferat) sau propoziție A/F completă."""
    if not is_incomplete_tf_item(item):
        return item, False

    seed = _item_seed(item)
    stem = str(item.get("text") or item.get("intrebare") or "")

    spec = lookup_incomplete_spec(stem)
    if spec:
        new_stem, options, correct = build_from_spec(spec, seed)
        return _apply_conceptual(item, new_stem, options, correct), True

    author_item = _try_author_conceptual(item, seed)
    if author_item:
        return author_item, True

    return item, False


def audit_incomplete_tf(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    hits: List[Dict[str, Any]] = []
    for item in items:
        if is_incomplete_tf_item(item):
            hits.append(
                {
                    "id": item.get("id"),
                    "text": str(item.get("text") or item.get("intrebare") or "")[:120],
                }
            )
    return {"count": len(hits), "items": hits}


def format_incomplete_tf_report(result: Dict[str, Any], changes: List[Dict[str, Any]]) -> str:
    lines = [
        "=== Audit itemi A/F neterminați ===",
        f"Itemi problematici găsiți: {result['count']}",
        f"Itemi rescriși: {len(changes)}",
        "",
    ]
    if result["items"]:
        lines.append("--- Itemi A/F cu enunț neterminat (înainte) ---")
        for hit in result["items"]:
            lines.append(f"  id={hit['id']}: {hit['text']}")
        lines.append("")
    if changes:
        lines.append("--- Modificări ---")
        for ch in changes:
            lines.append(f"id={ch['id']}")
            lines.append(f"  înainte: {ch['before']}")
            lines.append(f"  după:   {ch['after']}")
        lines.append("")
    remaining = result["count"] - len(changes)
    if remaining <= 0:
        lines.append("OK — niciun item A/F neterminat rămas.")
    else:
        lines.append(f"ATENȚIE: {remaining} itemi încă neterminați.")
    return "\n".join(lines)
