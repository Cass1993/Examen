"""Standalone genetics rewrite — no package imports beyond stdlib."""
from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP))

# Reuse project modules when available (same logic as rewrite_genetics_epigenetics.py)
from scripts.audit_genetics_epigenetics import audit_genetics_items, format_genetics_audit_report
from scripts.fix_genetics_epigenetics import apply_genetics_fixes, normalize_item_terminology
from scripts.label_definition_index import build_label_definition_index
from scripts.polish_text import polish_question_item
from scripts.upgrade_tf_items import build_label_definition_map

DEFAULT_IN = APP / "data" / "questions.json"
OUT_JSON = APP / "questions_clean.json"
OUT_TXT = APP / "questions_clean.txt"
OUT_AUDIT = APP / "audit_report_genetica_epigenetica.txt"
POLISH_PASSES = 2


def _lot_questions(block: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(block.get("questions") or block.get("items") or [])


def _set_lot_questions(block: Dict[str, Any], questions: List[Dict[str, Any]]) -> None:
    if "questions" in block:
        block["questions"] = questions
    else:
        block["items"] = questions


def _flatten_items(data: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any]]]:
    rows: List[Tuple[str, Dict[str, Any]]] = []
    for lot, block in (data.get("lots") or {}).items():
        for item in _lot_questions(block):
            rows.append((lot, item))
    return rows


def _write_txt(data: Dict[str, Any], path: Path) -> None:
    lines: List[str] = []
    for lot, block in (data.get("lots") or {}).items():
        lines.append(f"=== {lot} ===")
        for item in _lot_questions(block):
            lines.append(f"\n[{item.get('id')}] {item.get('text', '')}")
            opts = item.get("options") or {}
            for k in sorted(opts.keys()):
                mark = "*" if k in (item.get("correct") or []) else " "
                lines.append(f"  ({k}){mark} {opts[k]}")
    path.write_text("\n".join(lines), encoding="utf-8")


def process_bank(data: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    label_map = build_label_definition_map(data)
    label_index = build_label_definition_index(data)
    all_changes: List[Dict[str, Any]] = []
    out = copy.deepcopy(data)
    for lot, block in (out.get("lots") or {}).items():
        items = _lot_questions(block)
        fixed_items, changes = apply_genetics_fixes(items)
        all_changes.extend(changes)
        polished: List[Dict[str, Any]] = []
        for i, item in enumerate(fixed_items):
            row = dict(item)
            row["domeniu"] = lot
            row["lot"] = lot
            for _ in range(POLISH_PASSES):
                row = polish_question_item(
                    row,
                    index=int(item.get("id") or i),
                    label_map=label_map,
                    label_index=label_index,
                )
            polished.append(normalize_item_terminology(row))
        _set_lot_questions(block, polished)
    return out, all_changes


def main() -> None:
    raw = json.loads(DEFAULT_IN.read_text(encoding="utf-8"))
    before_items = [item for _, item in _flatten_items(raw)]
    audit_before = audit_genetics_items(before_items)
    cleaned, changes = process_bank(raw)
    after_items = [item for _, item in _flatten_items(cleaned)]
    audit_after = audit_genetics_items(after_items)

    OUT_JSON.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_txt(cleaned, OUT_TXT)

    report_lines = [
        format_genetics_audit_report(audit_before),
        "",
        f"Itemi rescriși în această rulare: {len(changes)}",
        "",
        "--- Exemple modificări ---",
    ]
    for ch in changes[:30]:
        report_lines.append(f"id={ch['id']}")
        report_lines.append(f"  înainte: {ch['before']}")
        report_lines.append(f"  după:   {ch['after']}")
    if len(changes) > 30:
        report_lines.append(f"... și încă {len(changes) - 30} modificări")
    report_lines.extend(["", "=== După rescriere ===", format_genetics_audit_report(audit_after)])
    OUT_AUDIT.write_text("\n".join(report_lines), encoding="utf-8")

    text = OUT_JSON.read_text(encoding="utf-8")
    print(f"Scris: {OUT_JSON}")
    print(f"Scris: {OUT_TXT}")
    print(f"Scris: {OUT_AUDIT}")
    print(f"Modificări: {len(changes)}")
    print(f"Pattern interzise înainte: {len(audit_before['forbidden_hits'])}")
    print(f"Pattern interzise după: {len(audit_after['forbidden_hits'])}")
    print(f"Count Concepte genetice: {text.count('Concepte genetice')}")
    print(f"Count modelul modelul: {text.count('modelul modelul')}")
    print(f"Count mediu unic: {text.count('mediu unic')}")


if __name__ == "__main__":
    main()
