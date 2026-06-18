"""Audit itemi Adevărat/Fals — verifică standardizarea."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_item_quality import walk_items  # noqa: E402
from scripts.fix_tf_items import TF_OPTIONS, is_tf_item, norm  # noqa: E402

DEFAULT_PATH = APP_DIR / "data" / "questions.json"
OUT_PATH = APP_DIR / "audit_tf_report.txt"

BAD_PREFIX = re.compile(
    r"Afirmația următoare este corectă|"
    r"Este adevărat că|"
    r"Este fals că|"
    r"Alege adevărat sau fals|"
    r"Se poate afirma că|"
    r"Adevărat sau fals:",
    re.I,
)

CONCEPT_OPTION_RE = re.compile(
    r"^(Psihoterapia|Eritabilitatea|Validitatea|Psihanaliza|Terapia|Atașamentul|"
    r"Clusterul|Abordarea|Modelul|Scala|Testul|Variabila|Mediana|Populația)",
    re.I,
)


def audit_tf_bank(data: Any) -> Dict[str, List[Dict[str, str]]]:
    issues: Dict[str, List[Dict[str, str]]] = {
        "bad_prefix": [],
        "wrong_options": [],
        "four_options": [],
        "concept_in_option": [],
        "not_tf_marked": [],
    }

    for lot, item in walk_items(data):
        if not is_tf_item(item):
            continue
        iid = f"{lot}#{item.get('id', '?')}"
        stem = str(item.get("text") or item.get("intrebare") or "")
        opts = dict(item.get("options") or item.get("variante") or {})

        if BAD_PREFIX.search(stem):
            issues["bad_prefix"].append({"id": iid, "stem": stem[:120]})

        if len(opts) != 2:
            issues["four_options"].append({"id": iid, "count": str(len(opts))})
        elif opts != TF_OPTIONS and {norm(v) for v in opts.values()} != {norm(v) for v in TF_OPTIONS.values()}:
            issues["wrong_options"].append({"id": iid, "options": str(opts)})

        for letter, val in opts.items():
            if norm(val) not in {norm(v) for v in TF_OPTIONS.values()}:
                if CONCEPT_OPTION_RE.match(str(val).strip()) or len(str(val)) > 12:
                    issues["concept_in_option"].append(
                        {"id": iid, "letter": letter, "text": str(val)[:80]}
                    )

        kind = str(item.get("kind") or item.get("tip") or "")
        if kind not in {"adevărat_fals", "adevarat_fals", "tf"}:
            issues["not_tf_marked"].append({"id": iid, "kind": kind})

    return issues


def format_report(issues: Dict[str, List], total_tf: int) -> str:
    lines = [
        "=" * 72,
        "AUDIT ITEMI ADEVĂRAT/FALS",
        "=" * 72,
        f"Total itemi A/F detectați: {total_tf}",
        "",
    ]
    titles = {
        "bad_prefix": 'Enunțuri cu "Afirmația următoare este corectă" etc.',
        "wrong_options": "Variante diferite de Adevărat/Fals",
        "four_options": "Itemi A/F cu != 2 variante",
        "concept_in_option": "Variante conceptuale la itemi A/F",
        "not_tf_marked": "Itemi A/F fără kind adevărat_fals",
    }
    total_problems = 0
    for key, title in titles.items():
        items = issues.get(key, [])
        total_problems += len(items)
        lines.append(f"--- {title}: {len(items)} ---")
        for entry in items[:25]:
            lines.append(f"  {entry}")
        if len(items) > 25:
            lines.append(f"  ... și încă {len(items) - 25}")
        lines.append("")

    lines.append(f"Total probleme: {total_problems}")
    if total_problems == 0:
        lines.append("OK — toți itemii A/F respectă standardul.")
    lines.append("=" * 72)
    return "\n".join(lines)


def main() -> None:
    path = DEFAULT_PATH
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        path = Path(sys.argv[1])

    data = json.loads(path.read_text(encoding="utf-8"))
    total_tf = sum(1 for _, item in walk_items(data) if is_tf_item(item))
    issues = audit_tf_bank(data)
    report = format_report(issues, total_tf)
    OUT_PATH.write_text(report, encoding="utf-8")
    print(report)
    print(f"Raport salvat: {OUT_PATH}")


if __name__ == "__main__":
    main()
