"""Înlocuiește adjective pseudo-românești în lotul Psihologia învățării II."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

REPLACEMENTS = [
    (r"\bcondiționarea clasică pavloviană\b", "condiționarea clasică a lui Pavlov"),
    (r"\bcondiționării clasice pavloviene\b", "condiționării clasice a lui Pavlov"),
    (r"\bclasică pavloviană\b", "clasică a lui Pavlov"),
    (r"\bclasică descrisă de Pavlovă\b", "clasică a lui Pavlov"),
    (r"\bextincția clasică pavloviană\b", "extincția în paradigma clasică a lui Pavlov"),
    (r"\bexemplu clasic pavlovian\b", "exemplu clasic din experimentele lui Pavlov"),
    (r"\breflexe salivare pavloviene\b", "reflexe salivare în experimentele lui Pavlov"),
    (r"\brăspuns condiționat pavlovian\b", "răspuns condiționat în paradigma lui Pavlov"),
    (r"\breflexivă pavloviană\b", "reflexivă în paradigma lui Pavlov"),
    (r"\bpavloviană clasică\b", "clasică a lui Pavlov"),
    (r"\b\(pavloviană\)", "(clasică a lui Pavlov)"),
    (r"\bmemoria reflexă pavloviană\b", "memoria reflexă din paradigma clasică"),
    (r"\bReflexul pavlovian\b", "Reflexul condiționat clasic"),
    (r"\bsens pavlovian pur\b", "sens clasic pavlovian (S–R)"),
    (r"\breorganizare piagetiană\b", "reorganizare a schemei în teoria lui Piaget"),
    (r"\basimilarea piagetiană\b", "asimilarea în teoria lui Piaget"),
    (r"\bstadiul senzorio-motor piagetian\b", "stadiul senzorio-motor din teoria lui Piaget"),
    (r"\bstadială piagetiană\b", "stadială în teoria lui Piaget"),
    (r"\bAsimilarea piagetiană\b", "Asimilarea în teoria lui Piaget"),
    (r"\bfacilitării rogersiene\b", "facilitării descrise de Carl Rogers"),
    (r"\bfacilitatoare sunt rogersiene\b", "facilitatoare sunt cele ale lui Carl Rogers"),
    (r"\bînvățării semnificative rogersiene\b", "învățării semnificative în abordarea lui Carl Rogers"),
    (r"\bmodelul facilitării rogersiene\b", "modelul facilitării descrise de Carl Rogers"),
    (r"\bstandardele naționale au fost elaborate direct pe modelul facilitării rogersiene\b",
     "standardele naționale au fost elaborate direct pe modelul facilitării lui Carl Rogers"),
    (r"\bteoriei facilitării rogersiene\b", "teoriei facilitării descrise de Carl Rogers"),
]


def main() -> int:
    patterns = [(re.compile(p, re.I), r) for p, r in REPLACEMENTS]
    globs = list(SCRIPTS.glob("psihologia_invatarii_ii*.py"))
    total = 0
    for path in globs:
        text = path.read_text(encoding="utf-8")
        original = text
        for pat, repl in patterns:
            text, n = pat.subn(repl, text)
            total += n
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"updated {path.name}")
    print(f"Total replacements: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
