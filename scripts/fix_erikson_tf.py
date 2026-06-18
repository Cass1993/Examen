"""Corectează itemii A/F Erikson cu crize amestecate."""

from __future__ import annotations

from typing import Any, Dict, Tuple

from scripts.erikson_specs import fix_erikson_tf_stem, is_mixed_erikson_tf_stem
from scripts.fix_tf_items import TF_OPTIONS, fix_tf_item, is_tf_item


def fix_erikson_tf_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    if not is_tf_item(item):
        return item, False

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    if not is_mixed_erikson_tf_stem(stem):
        return item, False

    new_stem = fix_erikson_tf_stem(stem)
    if not new_stem:
        return item, False

    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    if "variante" in item:
        out["variante"] = dict(TF_OPTIONS)
    if "options" in item:
        out["options"] = dict(TF_OPTIONS)
    if "raspuns_corect" in item:
        out["raspuns_corect"] = ["a"]
    if "correct" in item:
        out["correct"] = ["a"]
    out["tip"] = "adevărat_fals"
    out["kind"] = "adevărat_fals"
    out["explicatie"] = ""
    out["explanation"] = ""

    return out, True


def fix_erikson_then_tf(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    fixed, ch = fix_erikson_tf_item(item)
    if ch:
        return fixed, True
    return fix_tf_item(item)
