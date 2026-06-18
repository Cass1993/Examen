"""Rescriere metodologică finală → questions_clean_final.json"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_report_final import audit_final, format_final_audit_report  # noqa: E402
from scripts.distractor_fix import build_index  # noqa: E402
from scripts.fix_category_list_stems import (  # noqa: E402
    fix_category_list_item,
    fix_mixed_cluster_options,
)
from scripts.fix_context_stems import fix_context_stem_item  # noqa: E402
from scripts.fix_tf_items import fix_tf_item  # noqa: E402
from scripts.label_definition_index import build_label_definition_index  # noqa: E402
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.rewrite_bank_natural import (  # noqa: E402
    _from_row,
    _replace_item,
    _to_row,
    _walk,
    export_txt,
)
from scripts.rewrite_conceptual_coherence import rewrite_item_coherence  # noqa: E402
from scripts.rewrite_domain_belonging import rewrite_domain_belonging_bank  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

DEFAULT_IN = APP_DIR / "data" / "questions.json"
OUT_JSON = APP_DIR / "questions_clean_final.json"
OUT_TXT = APP_DIR / "questions_clean_final.txt"
OUT_AUDIT = APP_DIR / "audit_report_final.txt"

PASSES = 4


def _category_fix_pass(data: Dict[str, Any]) -> int:
    changes = 0
    for lot, item in _walk(data):
        fixed, ch = fix_category_list_item(item)
        if ch:
            item.clear()
            item.update(fixed)
            changes += 1
            continue
        fixed2, ch2 = fix_mixed_cluster_options(item)
        if ch2:
            item.clear()
            item.update(fixed2)
            changes += 1
            continue
        fixed3, ch3 = fix_context_stem_item(item)
        if ch3:
            item.clear()
            item.update(fixed3)
            changes += 1
    return changes


def process_bank_final(data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
    out_data = copy.deepcopy(data)
    total_changes = 0

    rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
    index = build_index(rows)
    label_map = build_label_definition_map(rows)
    label_index = build_label_definition_index(rows)

    out_data, domain_ch, _ = rewrite_domain_belonging_bank(
        out_data, index, label_map, label_index
    )
    total_changes += domain_ch

    for _ in range(PASSES):
        pass_ch = 0
        pass_ch += _category_fix_pass(out_data)

        rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
        index = build_index(rows)
        label_map = build_label_definition_map(rows)
        label_index = build_label_definition_index(rows)

        for lot, item in _walk(out_data):
            row = _to_row(item, lot)
            polished = polish_question_item(row, index, label_map, label_index)
            fixed_row, _ = fix_tf_item(polished)
            new_item = _from_row(fixed_row, item)
            if new_item != item:
                _replace_item(out_data, lot, item["id"], new_item)
                pass_ch += 1

        for lot, item in _walk(out_data):
            row = _to_row(item, lot)
            rewritten, ch = rewrite_item_coherence(row, index, lot)
            if ch:
                polished = polish_question_item(rewritten, index, label_map, label_index)
                new_item = _from_row(polished, item)
                _replace_item(out_data, lot, item["id"], new_item)
                pass_ch += 1

        pass_ch += _category_fix_pass(out_data)
        total_changes += pass_ch

    # polish final
    rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
    index = build_index(rows)
    label_map = build_label_definition_map(rows)
    label_index = build_label_definition_index(rows)
    for lot, item in _walk(out_data):
        row = _to_row(item, lot)
        polished = polish_question_item(row, index, label_map, label_index)
        fixed_row, _ = fix_tf_item(polished)
        new_item = _from_row(fixed_row, item)
        if new_item != item:
            _replace_item(out_data, lot, item["id"], new_item)
            total_changes += 1

    return out_data, total_changes


def main() -> None:
    in_path = DEFAULT_IN
    apply_app = "--apply" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        in_path = Path(args[0])

    if not in_path.exists():
        print(f"ERROR: {in_path} not found")
        sys.exit(1)

    print(f"Încărcare: {in_path}")
    data = json.loads(in_path.read_text(encoding="utf-8"))
    in_count = sum(len(lot.get("questions", [])) for lot in data.get("lots", {}).values())
    print(f"Itemi înainte: {in_count}")

    pre = audit_final(data)
    print(f"Probleme înainte: ~{pre['total_items']} itemi, flags={sum(pre.get('counts', {}).values())}")

    print("Rescriere metodologică finală...")
    clean_data, changes = process_bank_final(data)
    out_count = sum(len(lot.get("questions", [])) for lot in clean_data.get("lots", {}).values())
    print(f"Itemi după: {out_count} (modificări: {changes})")

    clean_data["source_file"] = "questions_clean_final (rescriere metodologică)"
    clean_data["total_questions"] = out_count

    OUT_JSON.write_text(
        json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    OUT_TXT.write_text(export_txt(clean_data), encoding="utf-8")
    print(f"Salvat: {OUT_JSON}")
    print(f"Salvat: {OUT_TXT}")

    post = audit_final(clean_data)
    audit_text = format_final_audit_report(post)
    OUT_AUDIT.write_text(audit_text, encoding="utf-8")
    print(f"Salvat: {OUT_AUDIT}")
    print()
    print(audit_text[:4000])

    if apply_app:
        app_path = APP_DIR / "data" / "questions.json"
        app_path.write_text(
            json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Aplicat în aplicație: {app_path}")


if __name__ == "__main__":
    main()
