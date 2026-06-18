"""Rescriere itemi A/F neterminați + raport audit."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.fix_incomplete_tf import (  # noqa: E402
    audit_incomplete_tf,
    fix_incomplete_tf_item,
    format_incomplete_tf_report,
    is_incomplete_tf_stem,
)
from scripts.fix_tf_items import fix_tf_item  # noqa: E402
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

BANK_JSON = APP_DIR / "data" / "questions.json"
OUT_JSON = APP_DIR / "questions_clean.json"
OUT_TXT = APP_DIR / "questions_clean.txt"
OUT_AUDIT = APP_DIR / "audit_report_incomplete_tf.txt"


def _lot_questions(block: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(block.get("questions") or block.get("items") or [])


def _set_lot_questions(block: Dict[str, Any], questions: List[Dict[str, Any]]) -> None:
    if "questions" in block:
        block["questions"] = questions
    else:
        block["items"] = questions


def _flatten(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for _lot, block in (data.get("lots") or {}).items():
        rows.extend(_lot_questions(block))
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
    changes: List[Dict[str, Any]] = []
    out = copy.deepcopy(data)

    for lot, block in (out.get("lots") or {}).items():
        fixed_lot: List[Dict[str, Any]] = []
        for item in _lot_questions(block):
            current = dict(item)
            fixed, changed = fix_incomplete_tf_item(current)
            if changed:
                changes.append(
                    {
                        "id": item.get("id"),
                        "before": item.get("text"),
                        "after": fixed.get("text"),
                    }
                )
                current = fixed
            row = dict(current)
            row["domeniu"] = lot
            row = polish_question_item(row, index=item.get("id"), label_map=label_map)
            # verificare: item A/F rămas nu trebuie să aibă enunț neterminat
            if is_incomplete_tf_stem(str(row.get("text") or "")):
                row, _ = fix_tf_item(row)
            fixed_lot.append(row)
        _set_lot_questions(block, fixed_lot)

    return out, changes


def main() -> None:
    raw = json.loads(BANK_JSON.read_text(encoding="utf-8"))
    before = audit_incomplete_tf(_flatten(raw))
    cleaned, changes = process_bank(raw)
    after = audit_incomplete_tf(_flatten(cleaned))

    OUT_JSON.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")
    BANK_JSON.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_txt(cleaned, OUT_TXT)

    report = "\n".join(
        [
            format_incomplete_tf_report(before, changes),
            "",
            "=== După rescriere ===",
            format_incomplete_tf_report(after, []),
        ]
    )
    OUT_AUDIT.write_text(report, encoding="utf-8")

    print(report)
    print(f"\nScris: {OUT_AUDIT}")


if __name__ == "__main__":
    main()
