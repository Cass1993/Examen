"""Aplică fix ghilimele pe fișierele de explicații."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Înlocuiește „text" doar când " nu este ghilimea Python de la capăt de linie.
_INNER_QUOTE = re.compile(r'„([^»"\n]{1,50})"(?=\S)')
_BROKEN_EOL = re.compile(r'^(\s+"[^"]*)»(\s*)$', re.MULTILINE)
_PAREN_QUOTE = re.compile(r'\("([^"\\]{1,80})"\)')
_WRONG_CLOSE = [
    (re.compile(r"\.»,"), '.",'),
    (re.compile(r"\?»,"), '?",'),
    (re.compile(r"!»,"), '!",'),
    (re.compile(r"»\.»,"), '».",'),
    (re.compile(r"\.»»,"), '.»",'),
]
# „text?" " la capăt de linie — ghilimea Python deschisă fără închidere.
_BROKEN_QUESTION_EOL = re.compile(r'^(\s+.*\?)"\s+"\s*$', re.MULTILINE)


def fix_text(text: str) -> str:
    text = _BROKEN_EOL.sub(r'\1"\2', text)
    text = _BROKEN_QUESTION_EOL.sub(r'\1» "', text)
    for pattern, replacement in _WRONG_CLOSE:
        text = pattern.sub(replacement, text)
    text = _INNER_QUOTE.sub(r"„\1»", text)
    text = _PAREN_QUOTE.sub(r"(\1)", text)
    return text


def main() -> int:
    patterns = (
        "scripts/psihoterapie_ii_expl_part*.py",
        "scripts/pm_ii_explanations_part*.py",
        "scripts/psihopatologie_ii_expl_part*.py",
        "scripts/psihologia_dezvoltarii_ii_explanations.py",
    )
    changed: list[str] = []
    for pat in patterns:
        for path in sorted(ROOT.glob(pat)):
            original = path.read_text(encoding="utf-8")
            updated = fix_text(original)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
                changed.append(path.name)
    log = ROOT / "_quote_fix_log.txt"
    log.write_text("\n".join(changed) if changed else "no changes", encoding="utf-8")
    print(f"fixed {len(changed)} files")
    for name in changed:
        print(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
