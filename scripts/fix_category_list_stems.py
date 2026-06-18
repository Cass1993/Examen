"""Rescrie enunțuri rupte de tip «Stiluri parentale descriu:» în întrebări naturale."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.category_list_specs import (
    pick_cluster_disorder_spec,
    pick_spec,
    sanitize_options_for_cluster,
    topic_to_cluster,
)
from scripts.fix_tf_items import is_tf_item

BROKEN_CATEGORY_STEM_RE = re.compile(
    r"^(?:În [^,]+,\s*)?(?P<topic>.+?)\s+descriu?:\s*$",
    re.IGNORECASE,
)
BROKEN_DOMAIN_LIST_RE = re.compile(
    r"^Care dintre următoarele sunt (?:dimensiuni Big Five|scale de măsurare|"
    r"teme de epigenetică din programă|proceduri/teste parametrice menționate în tematică|"
    r"concepte asociate MCD)",
    re.IGNORECASE,
)
CLUSTER_LIST_RE = re.compile(
    r"tulburări aparțin Clusterului\s+[ABC]\b",
    re.IGNORECASE,
)


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def is_broken_category_list_stem(stem: str) -> bool:
    text = (stem or "").strip()
    if BROKEN_CATEGORY_STEM_RE.match(text):
        return True
    if BROKEN_DOMAIN_LIST_RE.match(text):
        return True
    if CLUSTER_LIST_RE.search(text):
        return True
    return False


def needs_category_list_fix(item: Dict[str, Any]) -> bool:
    if is_tf_item(item):
        return False
    return is_broken_category_list_stem(_stem(item))


def _apply_item(
    item: Dict[str, Any],
    stem: str,
    options: Dict[str, str],
    correct: List[str],
    kind: str,
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
    corr = [c.lower() for c in correct]
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    if "correct" in item:
        out["correct"] = corr
    if kind == "multi":
        out["kind"] = "multi"
        out["tip"] = "multi"
    else:
        out["kind"] = "single"
        out["tip"] = "unic"
    out["explicatie"] = ""
    out["explanation"] = ""
    return out


def fix_category_list_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    stem = _stem(item)
    if not is_broken_category_list_stem(stem):
        return item, False

    from scripts.fix_admin_list_items import fix_admin_list_item

    fixed_admin, changed_admin = fix_admin_list_item(item)
    if changed_admin:
        return fixed_admin, True

    seed = _item_seed(item)
    if CLUSTER_LIST_RE.search(stem):
        spec = pick_cluster_disorder_spec(stem, seed)
        if spec:
            options = spec["options"]
            kind = spec.get("kind", "single")
            correct = spec["correct"]
            if isinstance(correct, str):
                correct = [correct]
            return (
                _apply_item(item, spec["stem"], options, list(correct), kind),
                True,
            )

    m = BROKEN_CATEGORY_STEM_RE.match(stem)
    topic = m.group("topic").strip() if m else stem
    cluster = topic_to_cluster(topic)

    if not cluster and BROKEN_DOMAIN_LIST_RE.match(stem):
        low = stem.lower()
        if "big five" in low:
            cluster = "big_five"
        elif "scale" in low:
            cluster = "scale_masurare"

    if not cluster:
        return item, False

    spec = pick_spec(cluster, seed, prefer_multi=False)
    if not spec:
        return item, False

    options = sanitize_options_for_cluster(spec["options"], cluster)
    kind = spec.get("kind", "single")
    correct = spec["correct"]
    if isinstance(correct, str):
        correct = [correct]

    return (
        _apply_item(item, spec["stem"], options, list(correct), kind),
        True,
    )


def fix_mixed_cluster_options(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """Repară variante amestecate (ex. evitant la stiluri parentale) fără enunț rupt."""
    if is_tf_item(item):
        return item, False
    stem = _stem(item).lower()
    opts = dict(item.get("variante") or item.get("options") or {})
    if len(opts) != 4:
        return item, False

    cluster: Optional[str] = None
    if "parental" in stem or "parentale" in stem:
        cluster = "stiluri_parentale"
    elif "atașament" in stem or "atasament" in stem:
        cluster = "atașament"
    elif "piaget" in stem or "stadiu" in stem:
        cluster = "piaget_stadii"

    if not cluster:
        vals = " ".join(opts.values()).lower()
        if any(w in vals for w in ("autoritativ", "autoritar", "permisiv", "neglijent")):
            if "evitant" in vals or "securizant" in vals:
                cluster = "stiluri_parentale"

    if not cluster:
        return item, False

    new_opts = sanitize_options_for_cluster(opts, cluster)
    if new_opts == opts:
        return item, False

    out = dict(item)
    if "variante" in item:
        out["variante"] = new_opts
    if "options" in item:
        out["options"] = new_opts
    return out, True
