"""Aplică toate remediile deterministe pe bancă și salvează JSON."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

BANK_FIX_VERSION = "38"
MAX_PASSES = 3

TEXT_KEYS = ("text", "intrebare", "explicatie", "explanation")
OPT_KEYS = ("options", "variante")

Fixer = Callable[[Dict[str, Any]], Tuple[Dict[str, Any], bool]]


def _lot_questions(block: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(block.get("questions") or block.get("items") or [])


def _set_lot_questions(block: Dict[str, Any], questions: List[Dict[str, Any]]) -> None:
    if "questions" in block:
        block["questions"] = questions
    else:
        block["items"] = questions


def patch_item_abbreviations(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    from scripts.abbreviations import collapse_nested_expansions

    out = dict(item)
    changed = False
    for key in TEXT_KEYS:
        if key in out and isinstance(out[key], str):
            fixed = collapse_nested_expansions(out[key])
            if fixed != out[key]:
                out[key] = fixed
                changed = True
    for key in OPT_KEYS:
        opts = out.get(key)
        if not isinstance(opts, dict):
            continue
        new_opts = dict(opts)
        for letter, val in opts.items():
            if isinstance(val, str):
                fixed = collapse_nested_expansions(val)
                if fixed != val:
                    new_opts[letter] = fixed
                    changed = True
        if changed:
            out[key] = new_opts
    return out, changed


def patch_genetics_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    from scripts.fix_genetics_epigenetics import (
        is_genetics_problem_item,
        normalize_item_terminology,
        rewrite_genetics_item,
    )

    row = normalize_item_terminology(item)
    if not is_genetics_problem_item(row):
        return row, row != item
    seed = int(row.get("id") or 0)
    fixed = rewrite_genetics_item(row, seed)
    if fixed:
        return fixed, True
    return row, row != item


def apply_fixes_to_item(item: Dict[str, Any], lot: str = "") -> Tuple[Dict[str, Any], bool]:
    if item.get("exam_item"):
        return item, False
    from scripts.association_pair_fix import (
        fix_association_pairs,
        fix_broken_association_item,
    )
    from scripts.fix_admin_list_items import (
        fix_admin_list_item,
        fix_labeled_options_in_definition_stem,
    )
    from scripts.fix_category_list_stems import (
        fix_category_list_item,
        fix_mixed_cluster_options,
    )
    from scripts.fix_context_stems import fix_context_stem_item
    from scripts.fix_incomplete_tf import fix_incomplete_tf_item
    from scripts.fix_malformed_flashcard import fix_malformed_flashcard_item

    row = dict(item)
    if lot:
        row["domeniu"] = lot
    changed = False

    fixers: List[Fixer] = [
        patch_item_abbreviations,
        fix_malformed_flashcard_item,
        fix_incomplete_tf_item,
        patch_genetics_item,
        fix_category_list_item,
        fix_admin_list_item,
        fix_labeled_options_in_definition_stem,
        fix_mixed_cluster_options,
        fix_context_stem_item,
        fix_broken_association_item,
        fix_association_pairs,
    ]

    for fixer in fixers:
        fixed, ch = fixer(row)
        if ch:
            row, changed = fixed, True

    return row, changed


def process_bank_data(data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
    out = copy.deepcopy(data)
    total = 0
    for _pass in range(MAX_PASSES):
        pass_count = 0
        for lot, block in (out.get("lots") or {}).items():
            questions = _lot_questions(block)
            fixed_lot: List[Dict[str, Any]] = []
            for item in questions:
                fixed, ch = apply_fixes_to_item(item, lot)
                if ch:
                    pass_count += 1
                fixed_lot.append(fixed)
            _set_lot_questions(block, fixed_lot)
        total += pass_count
        if pass_count == 0:
            break
    return out, total


def ensure_bank_fixed(bank_path: Path, marker_dir: Path) -> int:
    """Rulează o singură dată per BANK_FIX_VERSION; returnează nr. itemi modificați."""
    marker = marker_dir / f".bank_fix_{BANK_FIX_VERSION}"
    if marker.exists():
        return 0

    data = json.loads(bank_path.read_text(encoding="utf-8"))
    fixed, count = process_bank_data(data)
    bank_path.write_text(json.dumps(fixed, ensure_ascii=False, indent=2), encoding="utf-8")
    marker.write_text(str(count), encoding="utf-8")
    return count


def main() -> None:
    bank = APP_DIR / "data" / "questions.json"
    count = ensure_bank_fixed(bank, bank.parent)
    print(f"Bank fix v{BANK_FIX_VERSION}: {count} itemi rescriși în {bank}")


if __name__ == "__main__":
    main()
