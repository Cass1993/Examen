"""Corectează formulări negramaticale din lotul Psihologia dezvoltării II."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = sorted(ROOT.glob("psihologia_dezvoltarii_ii_*_bank_data.py"))
FILES = [p for p in FILES if p.name != "psihologia_dezvoltarii_ii_bank_data.py"]
FILES.append(ROOT / "psihologia_dezvoltarii_ii_bank_data.py")

PREFIX_REMOVALS = [
    "Care afirmație este corectă: ",
    "Care două elemente se aplică: ",
    "Care trei elemente se aplică: ",
]

REPLACEMENTS = [
    (":?", ":"),
    ("Care două distincție ", "Care două distincții "),
    ("Care trei distincție ", "Care trei distincții "),
    ("Care două combinație ", "Care două combinații "),
    ("Care două caracteristică ", "Care două caracteristici "),
    ("Care două afirmație ", "Care două afirmații "),
    ("Care trei sinteză ", "Care trei elemente de sinteză "),
    (
        "Care două checklist etic este corect înainte de colectarea datelor la copii?",
        "Care cerințe etice trebuie verificate înainte de colectarea datelor la copii?",
    ),
    (
        "Care afirmație metodă este cea mai potrivită",
        "Ce metodă este cea mai potrivită",
    ),
    (
        "Care combinații metodă — caracteristică principală sunt corecte?",
        "Care combinații metodă–caracteristică principală sunt corecte?",
    ),
    (
        "Care două perechi metodă — limită frecventă sunt corecte?",
        "Care perechi metodă–limită frecventă sunt corecte?",
    ),
    (
        "Care afirmație activități susțin achiziția permanenței obiectului la copilul mic?",
        "Care activități susțin achiziția permanenței obiectului la copilul mic?",
    ),
    (
        "Care distincție între iubirea narcisică și cea matură este corectă?",
        "Care este distincția dintre iubirea narcisică și cea matură?",
    ),
    (
        "Încălcări principale:",
        "Încălcările principale sunt:",
    ),
    (
        "Răspunsul pedagogic corect:",
        "Răspunsul pedagogic corect este:",
    ),
]

AGREEMENT = [
    (r"Care două distincții (.+?) este corectă\?", r"Care două distincții \1 sunt corecte?"),
    (r"Care două combinații (.+?) este corectă\?", r"Care două combinații \1 sunt corecte?"),
    (r"Care două caracteristici (.+?) descrie ", r"Care două caracteristici \1 descriu "),
    (r"Care trei distincții (.+?) este corectă\?", r"Care trei distincții \1 sunt corecte?"),
    (
        r"Care două afirmații despre metodele clinice este cea mai precisă\?",
        "Care două afirmații despre metodele clinice sunt cele mai precise?",
    ),
    (
        r"Care trei elemente de sinteză a celor cinci orientări teoretice este corectă\?",
        "Care trei elemente de sinteză ale celor cinci orientări teoretice sunt corecte?",
    ),
    (r"Care două combinații (.+?) descrie corect", r"Care două combinații \1 descriu corect"),
]


def fix_stem(stem: str) -> str:
    s = stem
    for p in PREFIX_REMOVALS:
        s = s.replace(p, "")
    for old, new in REPLACEMENTS:
        s = s.replace(old, new)
    for pat, repl in AGREEMENT:
        s = re.sub(pat, repl, s)
    return s


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        inner = m.group(1)
        fixed = fix_stem(inner)
        if fixed != inner:
            changed += 1
        escaped = fixed.replace("\\", "\\\\").replace('"', '\\"')
        return f'"stem": "{escaped}"'

    new_text = re.sub(r'"stem": "((?:[^"\\]|\\.)*)"', repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> int:
    total = 0
    for path in FILES:
        if not path.exists():
            continue
        n = process_file(path)
        if n:
            print(f"{path.name}: {n} enunțuri corectate")
            total += n
    print(f"Total: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
