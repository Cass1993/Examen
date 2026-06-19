"""Verifică consistența itemilor Psihologia dezvoltării II (răspuns vs explicație)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.explanation_prose import to_prose_explanation  # noqa: E402
from scripts.psihologia_dezvoltarii_ii_exam_items import build_items  # noqa: E402

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)


def main() -> int:
    items = build_items()
    issues: list[str] = []

    for q in items:
        qid = int(q["id"])
        correct = sorted(str(x).lower() for x in (q.get("correct") or []))
        expl = str(q.get("explanation") or "")
        prose = to_prose_explanation(expl)
        opts = q.get("options") or {}

        if LETTER_MARKERS.search(expl):
            issues.append(f"{qid}: explicație cu litere a/b/c/d în sursă")

        if LETTER_MARKERS.search(prose):
            issues.append(f"{qid}: explicație cu litere după to_prose")

        # Explicație spune „nu validitate internă” dar o marchează corectă
        if "nu validitate intern" in prose.lower() or "nu validitate internă" in prose.lower():
            for letter in correct:
                text = str(opts.get(letter, "")).lower()
                if "validitate" in text and "intern" in text:
                    issues.append(
                        f"{qid}: marchează corect validitatea internă, dar explicația o exclude"
                    )

        # Întrebare la singular („riscul principal”) cu mai multe răspunsuri
        stem = str(q.get("text") or "").lower()
        if re.search(r"\b(riscul principal|cel mai probabil|ilustrează mai ales)\b", stem):
            if len(correct) > 1:
                issues.append(
                    f"{qid}: enunț sugerează un răspuns, dar correct={correct}"
                )

    if not issues:
        print(f"OK: {len(items)} itemi, fără probleme detectate.")
        return 0

    print(f"Probleme ({len(issues)}):")
    for line in issues[:80]:
        print(f"  - {line}")
    if len(issues) > 80:
        print(f"  ... și încă {len(issues) - 80}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
