"""Raportează itemi cu distractori încă eterogeni după fix."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import (  # noqa: E402
    AUTHOR_IN_OPTION_RE,
    REFER_CEL_MAI_BINE_RE,
    REVERSE_DESC_RE,
    build_index,
    classify_option_form,
    fix_item_distractors,
    norm,
)


def walk(obj):
    if isinstance(obj, dict) and "text" in obj and "options" in obj:
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for x in obj:
            yield from walk(x)


def is_bad_item(item: dict) -> bool:
    opts = item.get("options") or {}
    correct = [str(c).lower() for c in item.get("correct") or []]
    if not opts or not correct:
        return False
    forms = [classify_option_form(str(opts[c])) for c in correct if c in opts]
    if not forms or len(set(forms)) != 1:
        return False
    target = forms[0]
    for letter, opt in opts.items():
        if letter in correct:
            continue
        o = str(opt)
        if AUTHOR_IN_OPTION_RE.match(o.strip()):
            return True
        if classify_option_form(o) != target:
            return True
    return False


def main() -> None:
    path = APP_DIR / "data" / "questions.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    items = list(walk(data))
    index = build_index(items)

    kinds = Counter()
    bad_after = []
    for it in items:
        stem = str(it.get("text", ""))
        if REVERSE_DESC_RE.match(stem):
            kinds["reverse_desc"] += 1
        elif REFER_CEL_MAI_BINE_RE.match(stem):
            kinds["refer"] += 1
        fixed, _ = fix_item_distractors(it, index)
        if is_bad_item(fixed):
            bad_after.append(stem[:80])

    print(f"Total itemi: {len(items)}")
    print(f"reverse_desc: {kinds['reverse_desc']}, refer: {kinds['refer']}")
    print(f"Încă eterogene după fix: {len(bad_after)}")
    for s in bad_after[:20]:
        print(f"  - {s}")


if __name__ == "__main__":
    main()
