"""Rescriere conceptuală completă a băncii + export questions_clean + audit."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.bank_audit_forbidden import audit_forbidden, format_audit_report  # noqa: E402
from scripts.distractor_fix import build_index  # noqa: E402
from scripts.flashcard_rewrite import rewrite_flashcard_item  # noqa: E402
from scripts.label_definition_index import build_label_definition_index  # noqa: E402
from scripts.fix_tf_items import fix_tf_item  # noqa: E402
from scripts.polish_text import polish_question_item  # noqa: E402
from scripts.rewrite_conceptual_coherence import (  # noqa: E402
    audit_bank_coherence,
    format_coherence_report,
    rewrite_bank_coherence,
    rewrite_item_coherence,
)
from scripts.rewrite_domain_belonging import (  # noqa: E402
    audit_domain_belonging,
    format_domain_audit_report,
    rewrite_domain_belonging_bank,
)
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402

DEFAULT_IN = APP_DIR / "data" / "questions.json"
OUT_JSON = APP_DIR / "questions_clean.json"
OUT_TXT = APP_DIR / "questions_clean.txt"
OUT_AUDIT = APP_DIR / "audit_report.txt"
OUT_AUDIT_CONCEPTUAL = APP_DIR / "audit_report_conceptual.txt"
OUT_AUDIT_DOMAIN = APP_DIR / "audit_report_domain_items.txt"

POLISH_PASSES = 3
REWRITE_PASSES = 2
COHERENCE_PASSES = 2


def _to_row(item: Dict[str, Any], lot: str) -> Dict[str, Any]:
    row = dict(item)
    row.setdefault("domeniu", lot)
    row.setdefault("lot", lot)
    if "text" in row and "intrebare" not in row:
        row["intrebare"] = row["text"]
    if "options" in row and "variante" not in row:
        row["variante"] = row["options"]
    if "correct" in row and "raspuns_corect" not in row:
        row["raspuns_corect"] = row["correct"]
    return row


def _from_row(row: Dict[str, Any], original: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(original)
    mapping = (
        ("text", "text"),
        ("intrebare", "intrebare"),
        ("options", "options"),
        ("variante", "variante"),
        ("correct", "correct"),
        ("raspuns_corect", "raspuns_corect"),
        ("explanation", "explanation"),
        ("explicatie", "explicatie"),
        ("kind", "kind"),
        ("tip", "tip"),
    )
    for dst, src in mapping:
        if src in row and (src in original or dst in original):
            out[dst] = row[src]
    return out


def process_bank(data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
    """Aplică polish + rescriere conceptuală pe toți itemii."""
    all_rows: List[Dict[str, Any]] = []
    for lot, item in _walk(data):
        all_rows.append(_to_row(item, lot))

    index = build_index(all_rows)
    label_map = build_label_definition_map(all_rows)
    label_index = build_label_definition_index(all_rows)

    changes = 0
    out_data = copy.deepcopy(data)

    rows0 = [_to_row(item, lot) for lot, item in _walk(out_data)]
    index0 = build_index(rows0)
    label_map0 = build_label_definition_map(rows0)
    label_index0 = build_label_definition_index(rows0)
    out_data, domain_changes, domain_log = rewrite_domain_belonging_bank(
        out_data, index0, label_map0, label_index0
    )
    changes += domain_changes

    for pass_num in range(POLISH_PASSES):
        pass_changes = 0
        rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
        index = build_index(rows)
        label_map = build_label_definition_map(rows)
        label_index = build_label_definition_index(rows)
        for lot, item in _walk(out_data):
            row = _to_row(item, lot)
            polished = polish_question_item(row, index, label_map, label_index)
            new_item = _from_row(polished, item)
            if new_item != item:
                pass_changes += 1
                _replace_item(out_data, lot, item["id"], new_item)
        changes += pass_changes

    for _pass_num in range(REWRITE_PASSES):
        pass_changes = 0
        rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
        index = build_index(rows)
        label_map = build_label_definition_map(rows)
        label_index = build_label_definition_index(rows)
        for lot, item in _walk(out_data):
            row = _to_row(item, lot)
            rewritten, ch = rewrite_flashcard_item(row, index, label_map, label_index)
            if ch:
                polished = polish_question_item(rewritten, index, label_map, label_index)
                new_item = _from_row(polished, item)
                _replace_item(out_data, lot, item["id"], new_item)
                pass_changes += 1
        changes += pass_changes

    for _co_pass in range(COHERENCE_PASSES):
        pass_changes = 0
        rows = [_to_row(item, lot) for lot, item in _walk(out_data)]
        index = build_index(rows)
        for lot, item in _walk(out_data):
            row = _to_row(item, lot)
            rewritten, ch = rewrite_item_coherence(row, index, lot)
            if ch:
                polished = polish_question_item(rewritten, index, label_map, label_index)
                new_item = _from_row(polished, item)
                _replace_item(out_data, lot, item["id"], new_item)
                pass_changes += 1
        changes += pass_changes

    # polish final + standardizare A/F
    for lot, item in _walk(out_data):
        row = _to_row(item, lot)
        polished = polish_question_item(row, index, label_map, label_index)
        fixed_row, _ = fix_tf_item(polished)
        new_item = _from_row(fixed_row, item)
        if new_item != item:
            changes += 1
            _replace_item(out_data, lot, item["id"], new_item)

    return out_data, changes, domain_log


def _walk(data: Dict[str, Any]):
    for lot_name, lot_data in (data.get("lots") or {}).items():
        for q in lot_data.get("questions", []):
            yield lot_name, q


def _replace_item(data: Dict[str, Any], lot: str, qid: int, new_item: Dict[str, Any]) -> None:
    questions = data["lots"][lot]["questions"]
    for i, q in enumerate(questions):
        if q.get("id") == qid:
            questions[i] = new_item
            return


def export_txt(data: Dict[str, Any]) -> str:
    lines: List[str] = []
    total = 0
    for lot_name, lot_data in sorted((data.get("lots") or {}).items()):
        questions = lot_data.get("questions", [])
        if not questions:
            continue
        lines.append("")
        lines.append("=" * 72)
        lines.append(f"DOMENIU: {lot_name}")
        lines.append("=" * 72)
        for q in sorted(questions, key=lambda x: x.get("id", 0)):
            total += 1
            qid = q.get("id", "?")
            text = q.get("text") or q.get("intrebare") or ""
            opts = q.get("options") or q.get("variante") or {}
            correct = q.get("correct") or q.get("raspuns_corect") or []
            kind = q.get("kind") or q.get("tip") or "single"
            lines.append("")
            lines.append(f"[{qid}] ({kind}) {text}")
            for letter in sorted(opts.keys()):
                mark = " *" if letter in correct else ""
                lines.append(f"  {letter}) {opts[letter]}{mark}")
            lines.append(f"  Barem: {', '.join(correct)}")
            expl = (q.get("explanation") or q.get("explicatie") or "").strip()
            if expl:
                lines.append(f"  Explicație: {expl}")

    header = [
        "BANCĂ ITEMI — VERSIUNE RESCRISĂ (questions_clean)",
        f"Total itemi: {total}",
        "",
    ]
    return "\n".join(header + lines)


def main() -> None:
    in_path = DEFAULT_IN
    apply_to_app = "--apply" in sys.argv
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

    print("Rescriere conceptuală (polish + flashcard rewrite)...")
    clean_data, changes, domain_log = process_bank(data)
    out_count = sum(len(lot.get("questions", [])) for lot in clean_data.get("lots", {}).values())
    print(f"Itemi după: {out_count} (modificări aplicate: {changes})")

    if out_count != in_count:
        print(f"ATENȚIE: număr itemi schimbat ({in_count} → {out_count})")

    clean_data["source_file"] = "questions_clean (rescris natural)"
    clean_data["total_questions"] = out_count

    OUT_JSON.write_text(json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Salvat: {OUT_JSON}")

    txt = export_txt(clean_data)
    OUT_TXT.write_text(txt, encoding="utf-8")
    print(f"Salvat: {OUT_TXT}")

    print("Audit post-rescriere...")
    report = audit_forbidden(clean_data)
    audit_text = format_audit_report(report)
    OUT_AUDIT.write_text(audit_text, encoding="utf-8")
    print(f"Salvat: {OUT_AUDIT}")

    coherence_report = audit_bank_coherence(clean_data)
    coherence_text = format_coherence_report(coherence_report)
    OUT_AUDIT_CONCEPTUAL.write_text(coherence_text, encoding="utf-8")
    print(f"Salvat: {OUT_AUDIT_CONCEPTUAL}")

    domain_report = audit_domain_belonging(clean_data)
    domain_text = format_domain_audit_report(domain_report, domain_log)
    OUT_AUDIT_DOMAIN.write_text(domain_text, encoding="utf-8")
    print(f"Salvat: {OUT_AUDIT_DOMAIN}")
    print()
    print(audit_text)
    print()
    print(coherence_text)

    if apply_to_app:
        app_path = APP_DIR / "data" / "questions.json"
        app_path.write_text(
            json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Aplicat în aplicație: {app_path}")


if __name__ == "__main__":
    main()
