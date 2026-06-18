"""Analiză itemi «descrie mai ales» — coverage clusters."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import (  # noqa: E402
    REVERSE_DESC_RE,
    classify_option_form,
    fix_reverse_desc_item,
    build_index,
    norm,
)
from scripts.term_clusters import cluster_for_term, cluster_id_for_term  # noqa: E402

DATA = APP_DIR / "data" / "questions.json"


def walk(obj):
    if isinstance(obj, dict) and "text" in obj and "options" in obj:
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for x in obj:
            yield from walk(x)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    items = list(walk(data))
    rev = [i for i in items if REVERSE_DESC_RE.match(str(i.get("text", "")).strip())]
    print(f"reverse_desc items: {len(rev)}")

    no_cluster = 0
    heterogeneous = 0
    stem_counter: Counter = Counter()
    wrong_forms: Counter = Counter()

    for it in rev:
        stem = str(it.get("text", "")).strip()
        m = REVERSE_DESC_RE.match(stem)
        desc = m.group(1)[:60] if m else ""
        stem_counter[desc] += 1
        opts = it.get("options", {})
        corr = [str(c).lower() for c in it.get("correct", [])]
        correct_labels = [opts[c] for c in corr if c in opts]
        cid = None
        for lab in correct_labels:
            cid = cluster_id_for_term(lab, it.get("explanation", ""))
            if cid:
                break
        if not cid:
            no_cluster += 1
        for letter, opt in opts.items():
            if letter in corr:
                continue
            wrong_forms[classify_option_form(str(opt))] += 1
            if classify_option_form(str(opt)) in ("author", "definition"):
                heterogeneous += 1
                break
            if cid:
                cl = cluster_for_term(correct_labels[0]) or []
                if cl and norm(opt) not in {norm(x) for x in cl}:
                    heterogeneous += 1
                    break

    rows = list(walk(data))
    index = build_index(rows)
    fixed = 0
    for it in rev:
        out, ch = fix_reverse_desc_item(it, index)
        if ch:
            fixed += 1
    print(f"no cluster id: {no_cluster}")
    print(f"heterogeneous (est): {heterogeneous}")
    print(f"would fix now: {fixed}/{len(rev)}")
    print("top stems:", stem_counter.most_common(25))


if __name__ == "__main__":
    main()
