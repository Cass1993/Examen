"""Rescrie itemii tip listă administrativă în banca JSON."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.fix_admin_list_items import (  # noqa: E402
    audit_admin_list_items,
    fix_admin_list_item,
    format_admin_list_report,
    is_admin_list_item,
)
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

BANK_JSON = APP_DIR / "data" / "questions.json"
OUT_JSON = APP_DIR / "questions_clean.json"
OUT_TXT = APP_DIR / "questions_clean.txt"
OUT_AUDIT = APP_DIR / "audit_report_admin_list.txt"


def _lot_questions(block: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(block.get("questions") or block.get("items") or [])


def _set_lot_questions(block: Dict[str, Any], questions: List[Dict[str, Any]]) -> None:
    if "questions" in block:
        block["questions"] = questions
    else:
        block["items"] = questions


def _flatten(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for lot, block in (data.get("lots") or {}).items():
        for q in _lot_questions(block):
            rows.append({**q, "domeniu": lot})
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
    changes: List[Dict[str, Any]] = []
    out = copy.deepcopy(data)

    for lot, block in (out.get("lots") or {}).items():
        fixed_lot: List[Dict[str, Any]] = []
        for item in _lot_questions(block):
            current = dict(item)
            if is_admin_list_item(current):
                fixed, changed = fix_admin_list_item(current)
                if changed:
                    changes.append(
                        {
                            "id": item.get("id"),
                            "lot": lot,
                            "before": item.get("text"),
                            "after": fixed.get("text"),
                        }
                    )
                    current = fixed
            fixed_lot.append(current)
        _set_lot_questions(block, fixed_lot)

    return out, changes


def main() -> None:
    data = json.loads(BANK_JSON.read_text(encoding="utf-8"))
    before = audit_admin_list_items(_flatten(data))
    out, changes = process_bank(data)

    label_map = build_label_definition_map(_flatten(out))
    for lot, block in (out.get("lots") or {}).items():
        polished: List[Dict[str, Any]] = []
        for item in _lot_questions(block):
            row = dict(item)
            row["domeniu"] = lot
            polished.append(polish_question_item(row, None, label_map, None))
        _set_lot_questions(block, polished)

    after = audit_admin_list_items(_flatten(out))

    BANK_JSON.write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    OUT_JSON.write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    _write_txt(out, OUT_TXT)

    report_lines = [
        format_admin_list_report(before),
        "",
        f"Itemi rescriși în această rulare: {len(changes)}",
        "",
        "--- Exemple rescrieri (max 25) ---",
    ]
    for ch in changes[:25]:
        report_lines.append(f"  id={ch['id']} [{ch['lot']}]")
        report_lines.append(f"    înainte: {ch['before']}")
        report_lines.append(f"    după:    {ch['after']}")
    report_lines.append("")
    report_lines.append("--- După rescriere ---")
    report_lines.append(format_admin_list_report(after))
    OUT_AUDIT.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Rescriși: {len(changes)} itemi")
    print(f"Înainte: {before['count']} | După: {after['count']}")
    print(f"Raport: {OUT_AUDIT}")


if __name__ == "__main__":
    main()
