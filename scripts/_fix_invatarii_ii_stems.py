"""Elimină numărul de răspunsuri din enunțuri + adjective pseudo-românești din lotul II."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

# Fișiere bank + explicații segment
TARGET_GLOBS = [
    "psihologia_invatarii_ii*_bank_data.py",
    "psihologia_invatarii_ii*_explanations.py",
    "psihologia_invatarii_ii_explanations.py",
    "psihologia_invatarii_ii_bank_data.py",
]

COUNT_PATTERNS = [
    (re.compile(r"\bCare patru\b"), "Care dintre următoarele"),
    (re.compile(r"\bCare două\b"), "Care dintre următoarele"),
    (re.compile(r"\bCare trei\b"), "Care dintre următoarele"),
    (re.compile(r"\bCare doi\b"), "Care dintre următoarele"),
    # variante în enunțuri compuse
    (re.compile(r"\bcele patru procese ale modelării\b", re.I), "procesele modelării"),
    (re.compile(r"\bCele patru\b"), "Următoarele"),
    (re.compile(r"\bCele trei\b"), "Următoarele"),
    (re.compile(r"\bCele două\b"), "Următoarele"),
    (re.compile(r"\bToate patru\b"), "Toate variantele corecte"),
    (re.compile(r"\btoate patru\b"), "toate variantele corecte"),
    (re.compile(r"\bPatru afirmații\b"), "Afirmațiile"),
    (re.compile(r"\bPatru perechi\b"), "Perechile"),
    (re.compile(r"\bPatru trăsături\b"), "Trăsăturile"),
    (re.compile(r"\bPatru componente\b"), "Componentele"),
    (re.compile(r"\bPatru elemente\b"), "Elementele"),
    (re.compile(r"\bPatru roluri\b"), "Rolurile"),
    (re.compile(r"\bPatru piloni\b"), "Pilonii"),
    (re.compile(r"\bDouă perechi\b"), "Perechile"),
    (re.compile(r"\bDouă trăsături\b"), "Trăsăturile"),
    (re.compile(r"\bDouă componente\b"), "Componentele"),
    (re.compile(r"\bDouă practici\b"), "Practicile"),
    (re.compile(r"\bDouă consecințe\b"), "Consecințele"),
    (re.compile(r"\bDouă riscuri\b"), "Riscurile"),
    (re.compile(r"\bDouă beneficii\b"), "Beneficiile"),
    (re.compile(r"\bDouă diferențe\b"), "Diferențele"),
    (re.compile(r"\bDouă distincții\b"), "Distincțiile"),
    (re.compile(r"\bDouă idei\b"), "Ideile"),
    (re.compile(r"\bDouă roluri\b"), "Rolurile"),
    (re.compile(r"\bTrei dimensiuni\b"), "Dimensiunile"),
    (re.compile(r"\bTrei componente\b"), "Componentele"),
    (re.compile(r"\bTrei consecințe\b"), "Consecințele"),
    (re.compile(r"\bTrei practici\b"), "Practicile"),
    (re.compile(r"\bTrei elemente\b"), "Elementele"),
    (re.compile(r"\bTrei funcții\b"), "Funcțiile"),
    (re.compile(r"\bTrei tipuri\b"), "Tipurile"),
    (re.compile(r"\bTrei niveluri\b"), "Nivelurile"),
    (re.compile(r"\bTrei comportamente\b"), "Comportamentele"),
    (re.compile(r"\bTrei surse\b"), "Sursele"),
    (re.compile(r"\bTrei modalități\b"), "Modalitățile"),
]

ADJECTIVE_REPLACEMENTS = [
    (re.compile(r"\bbanduriene\b", re.I), "ale modelării sociale a lui Albert Bandura"),
    (re.compile(r"\bbandurian\b", re.I), "al lui Albert Bandura"),
    (re.compile(r"\bbanduriană\b", re.I), "a lui Albert Bandura"),
    (re.compile(r"\bbanduriane\b", re.I), "ale lui Albert Bandura"),
    (re.compile(r"\bskinnerian\b", re.I), "al lui B. F. Skinner"),
    (re.compile(r"\bskinneriană\b", re.I), "a lui B. F. Skinner"),
    (re.compile(r"\bskinneriene\b", re.I), "ale lui B. F. Skinner"),
    (re.compile(r"\bpavloviene\b", re.I), "ale lui Pavlov"),
    (re.compile(r"\bpavloviană\b", re.I), "a lui Pavlov"),
    (re.compile(r"\bpavlovian\b", re.I), "al lui Pavlov"),
    (re.compile(r"\btolmanian\b", re.I), "al lui Tolman"),
    (re.compile(r"\btolmaniană\b", re.I), "a lui Tolman"),
    (re.compile(r"\btolmaniene\b", re.I), "ale lui Tolman"),
    (re.compile(r"\bthorndikiană\b", re.I), "a lui Thorndike"),
    (re.compile(r"\bthorndikian\b", re.I), "al lui Thorndike"),
    (re.compile(r"\bpiagetiene\b", re.I), "ale lui Piaget"),
    (re.compile(r"\bpiagetiană\b", re.I), "a lui Piaget"),
    (re.compile(r"\brogersiană\b", re.I), "a lui Carl Rogers"),
    (re.compile(r"\brogersian\b", re.I), "al lui Carl Rogers"),
    (re.compile(r"\brogersiene\b", re.I), "ale lui Carl Rogers"),
    (re.compile(r"\bmaslowiane\b", re.I), "ale lui Abraham Maslow"),
    (re.compile(r"\bmaslowiană\b", re.I), "a lui Abraham Maslow"),
    (re.compile(r"\bwatsonian\b", re.I), "al lui Watson"),
    (re.compile(r"\bwatsoniană\b", re.I), "a lui Watson"),
    (re.compile(r"\beriksoniană\b", re.I), "a lui Erik Erikson"),
    (re.compile(r"\bconexionismului thorndikian\b", re.I), "conexionismului lui Thorndike"),
    (re.compile(r"\bînvățarea thorndikiană\b", re.I), "învățarea descrisă de Thorndike"),
    (re.compile(r"\bcomportamentalismului intențional tolmanian\b", re.I),
     "comportamentalismului intențional al lui Tolman"),
    (re.compile(r"\bteoriei hărților cognitive tolmaniene\b", re.I),
     "teoriei hărților cognitive a lui Tolman"),
    (re.compile(r"\bhărți cognitive tolmaniene\b", re.I), "hărți cognitive descrise de Tolman"),
    (re.compile(r"\bînvățare latentă tolmaniană\b", re.I), "învățare latentă descrisă de Tolman"),
    (re.compile(r"\bscopuri tolmaniene\b", re.I), "scopuri în teoria lui Tolman"),
    (re.compile(r"\bfacilitării rogersiene\b", re.I), "facilitării descrise de Carl Rogers"),
    (re.compile(r"\bmodelul facilitării rogersiene\b", re.I),
     "modelul facilitării descris de Carl Rogers"),
    (re.compile(r"\bstandardele naționale au fost elaborate direct pe modelul facilitării rogersiene\b", re.I),
     "standardele naționale au fost elaborate direct pe modelul facilitării lui Carl Rogers"),
    (re.compile(r"\bconcepte skinneriene\b", re.I), "concepte ale lui B. F. Skinner"),
    (re.compile(r"\bOperantele skinneriene\b"), "Operantele descrise de Skinner"),
    (re.compile(r"\bcondiționării clasice pavloviene\b", re.I), "condiționării clasice a lui Pavlov"),
    (re.compile(r"\bcondiționarea clasică pavloviană\b", re.I), "condiționarea clasică a lui Pavlov"),
    (re.compile(r"\bclasică pavloviană\b", re.I), "clasică descrisă de Pavlov"),
    (re.compile(r"\bexemplu clasic pavlovian\b", re.I), "exemplu clasic din experimentele lui Pavlov"),
    (re.compile(r"\breflexe salivare pavloviene\b", re.I), "reflexe salivare în experimentele lui Pavlov"),
    (re.compile(r"\breflexele necondiționate pavloviene\b", re.I),
     "reflexele necondiționate studiate de Pavlov"),
    (re.compile(r"\breflexivă pavloviană\b", re.I), "reflexivă în paradigma lui Pavlov"),
    (re.compile(r"\bpavloviană clasică\b", re.I), "clasică a lui Pavlov"),
    (re.compile(r"\bempatie rogersiană\b", re.I), "empatie în abordarea lui Carl Rogers"),
    (re.compile(r"\bProfesorul rogersian\b"), "Profesorul în abordarea lui Carl Rogers"),
    (re.compile(r"\bUn profesor rogersian\b"), "Un profesor în abordarea lui Carl Rogers"),
    (re.compile(r"\bfacilitării rogersiene\b", re.I), "facilitării lui Carl Rogers"),
    (re.compile(r"\bFacilitarea rogersiană\b"), "Facilitarea descrisă de Carl Rogers"),
    (re.compile(r"\brogersian sunt corecte\b", re.I), "lui Carl Rogers sunt corecte"),
    (re.compile(r"\brogersiană\?\b"), "a lui Carl Rogers?"),
    (re.compile(r"\bînvățare semnificativă rogersiană\b", re.I),
     "învățare semnificativă în abordarea lui Carl Rogers"),
    (re.compile(r"\bexperiențe culminante maslowiene\b", re.I),
     "experiențe culminante în teoria lui Abraham Maslow"),
    (re.compile(r"\bierarhia maslowiană\b", re.I), "ierarhia lui Abraham Maslow"),
    (re.compile(r"\btrebuințele maslowiene\b", re.I), "trebuințele din teoria lui Abraham Maslow"),
    (re.compile(r"\blegături între trebuințele maslowiene\b", re.I),
     "legături între trebuințele din teoria lui Abraham Maslow"),
    (re.compile(r"\bînvățare latentă tolmaniană\b", re.I), "învățare latentă a lui Tolman"),
    (re.compile(r"\bînvățare latentă în labirint; Hull: behaviorism watsonian strict\b"),
     "învățare latentă în labirint; Hull: behaviorism strict al lui Watson"),
    (re.compile(r"\bîntărirea vicariantă e banduriană\b", re.I),
     "întărirea vicariantă apare în teoria lui Bandura"),
    (re.compile(r"\bmodelul bandurian\b", re.I), "modelul lui Albert Bandura"),
    (re.compile(r"\bteoria facilitării rogersiene\b", re.I), "teoria facilitării lui Carl Rogers"),
    (re.compile(r"\bcondiționării clasice pavloviene\b", re.I), "condiționării clasice a lui Pavlov"),
    (re.compile(r"\bcomportament operant skinnerian\b", re.I), "comportament operant în paradigma lui Skinner"),
    (re.compile(r"\babordarea skinneriană\b", re.I), "abordarea lui B. F. Skinner"),
    (re.compile(r"\bconcept skinnerian\b", re.I), "concept al lui B. F. Skinner"),
    (re.compile(r"\be skinneriană\b", re.I), "e în paradigma lui Skinner"),
    (re.compile(r"\bîn analiza skinneriană\b"), "în analiza lui Skinner"),
    (re.compile(r"\bwatssonian timpuriu\b", re.I), "watsonian timpuriu al lui Watson"),
]

SPECIAL_STEMS = [
    (
        re.compile(
            r"Care dintre următoarele procese trebuie să aibă loc, în ordinea logică a modelării "
            r"ale modelării sociale a lui Albert Bandura",
            re.S,
        ),
        "Ce procese trebuie să aibă loc, în ordinea logică a modelării sociale a lui Albert Bandura",
    ),
]


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    for pat, repl in COUNT_PATTERNS:
        new, n = pat.subn(repl, text)
        if n:
            changes += n
            text = new
    for pat, repl in ADJECTIVE_REPLACEMENTS:
        new, n = pat.subn(repl, text)
        if n:
            changes += n
            text = new
    for pat, repl in SPECIAL_STEMS:
        new, n = pat.subn(repl, text)
        if n:
            changes += n
            text = new
    # curățare dubluri accidentale
    fixes = [
        ("Care dintre următoarele procese trebuie să aibă loc, în ordinea logică a modelării "
         "ale modelării sociale a lui Albert Bandura",
         "Ce procese trebuie să aibă loc, în ordinea logică a modelării sociale a lui Albert Bandura"),
        ("determinismul reciproc al lui Albert Bandura", "determinismul reciproc descris de Albert Bandura"),
        ("Care dintre următoarele etape compun ciclul experiențial Kolb, în ordinea logică?",
         "Ce etape compun ciclul experiențial Kolb, în ordinea logică?"),
    ]
    for old, new in fixes:
        if old in text:
            text = text.replace(old, new)
            changes += 1
    return text, changes


def collect_files() -> list[Path]:
    seen: set[Path] = set()
    for pattern in TARGET_GLOBS:
        for p in SCRIPTS.glob(pattern):
            seen.add(p.resolve())
    return sorted(seen)


def main() -> int:
    total_changes = 0
    files_changed = 0
    remaining: list[str] = []

    for path in collect_files():
        original = path.read_text(encoding="utf-8")
        fixed, n = fix_text(original)
        if n:
            path.write_text(fixed, encoding="utf-8")
            total_changes += n
            files_changed += 1
            print(f"{path.name}: {n} înlocuiri")

        for m in re.finditer(r"\bCare (patru|două|trei|doi)\b", fixed):
            line = fixed[: m.start()].count("\n") + 1
            remaining.append(f"{path.name}:{line}: {m.group()}")

    print(f"\nTotal: {total_changes} înlocuiri în {files_changed} fișiere")
    if remaining:
        print(f"\nRămân {len(remaining)} enunțuri cu număr explicit:")
        for r in remaining[:30]:
            print(f"  - {r}")
        if len(remaining) > 30:
            print(f"  ... și încă {len(remaining) - 30}")
        return 1
    print("OK: niciun 'Care patru/două/trei/doi' rămas în fișierele țintă.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
