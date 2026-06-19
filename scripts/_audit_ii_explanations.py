"""Find II items where explanation implies more correct answers than bank_data."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.psihologia_dezvoltarii_ii_exam_items import build_items  # noqa: E402

PAT_MULTI = re.compile(
    r"(?:Corect|Checklist|Toate patru|Capcane false):\s*([^\.]+)|"
    r"\(([a-d](?:,\s*[b-d])*)\)|"
    r"\(([a-d](?:,\s*[b-d])*)\s+adevărat\)|"
    r"\(([a-d](?:,\s*[b-d])*)\s+—",
    re.I,
)


def letters_from_exp(text: str) -> set[str] | None:
    text = text.strip()
    m = re.search(r"Corect:\s*([^\.]+)", text, re.I)
    if m:
        chunk = m.group(1)
        ls = set(re.findall(r"[a-d]", chunk.lower()))
        if ls:
            return ls
    m = re.search(r"Toate patru perechi corecte.*?\(([a-d])–([a-d])\)", text, re.I)
    if m:
        a, b = m.group(1), m.group(2)
        return set(chr(c) for c in range(ord(a), ord(b) + 1))
    m = re.search(r"\(([a-d](?:,\s*[b-d])*)\)", text)
    if m:
        ls = set(re.findall(r"[a-d]", m.group(1).lower()))
        if len(ls) >= 2:
            return ls
    return None


def main() -> int:
    items = build_items()
    bad = []
    for q in items:
        if q.get("type") == "tf":
            continue
        exp = str(q.get("explanation") or "")
        correct = str(q.get("correct") or "").lower()
        cur = set(c for c in correct if c in "abcd")
        exp_letters = letters_from_exp(exp)
        if not exp_letters:
            continue
        if exp_letters != cur and len(exp_letters) > len(cur):
            bad.append(
                (
                    q["id"],
                    "".join(sorted(cur)),
                    "".join(sorted(exp_letters)),
                    q["text"][:90],
                    exp[:120],
                )
            )
    print(f"Mismatches (exp wants more letters): {len(bad)}")
    for row in bad:
        print(f"ID {row[0]}: bank={row[1]} exp={row[2]}")
        print(f"  Q: {row[3]}")
        print(f"  E: {row[4]}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
