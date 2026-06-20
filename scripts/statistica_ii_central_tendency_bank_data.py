"""Itemi — Statistică II, segment 4: tendința centrală (20 itemi, ID 11071–11090)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

CENTRAL_TENDENCY_ITEMS: List[Item] = [
    # —— 1–5: mod, mediană, medie — definiții ——
    {
        "stem": (
            "Mediana este un indicator de tendință centrală robust la valorile extreme "
            "(outlieri), spre deosebire de media aritmetică."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Modul (Mo) al unei distribuții reprezintă:"
        ),
        "options": [
            "valoarea (sau categoria) care apare cel mai frecvent în setul de date",
            "valoarea care împarte eșantionul în două părți egale ca număr de cazuri",
            "suma tuturor valorilor împărțită la numărul de observații",
            "diferența dintre cea mai mare și cea mai mică valoare observată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele sunt avantaje ale modului ca indicator de tendință "
            "centrală?"
        ),
        "options": [
            "se calculează ușor, prin identificarea valorii celei mai frecvente",
            "poate fi folosit și la date nominale sau ordinale, nu doar la scale "
            "interval/raport",
            "este stabil la adăugarea unei valori extreme îndepărtate",
            "are proprietăți matematice ideale pentru orice test inferențial parametric",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un dezavantaj important al modului este că:"
        ),
        "options": [
            "poate fi instabil — o singură schimbare poate modifica modul sau îl poate "
            "face indefinit (mai multe valori modale)",
            "nu este indicatorul uzual ales pentru inferența statistică parametrică",
            "este mereu egal cu mediana în distribuții asimetrice",
            "nu poate fi determinat dintr-un tabel de frecvențe",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Media aritmetică (m) a unui set de date se calculează ca suma valorilor "
            "împărțită la numărul de observații: m = ΣX / N."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— 6–10: mediană, medie — avantaje și limite ——
    {
        "stem": (
            "Mediana (Me) a unui set de date ordonate este:"
        ),
        "options": [
            "valoarea (sau media celor două valori centrale) care lasă 50% din cazuri "
            "sub ea și 50% deasupra, în sens ordinal",
            "valoarea cea mai frecventă din distribuție",
            "media aritmetică a valorilor extreme",
            "diferența dintre al treilea și primul quartil",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre media aritmetică sunt corecte?"
        ),
        "options": [
            "este foarte folosită în practică și în inferența statistică parametrică",
            "are proprietăți matematice convenabile (ex. legături cu abaterile de la medie)",
            "este sensibilă la valorile extreme (outlieri)",
            "este identică cu modul în orice distribuție, indiferent de formă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele sunt avantaje ale medianei?"
        ),
        "options": [
            "este robustă la valorile extreme",
            "poate fi estimată și când ultima clasă a unui tabel grupat este deschisă",
            "este întotdeauna egală cu media aritmetică în distribuții asimetrice",
            "reflectă poziția centrală a 50% din cazuri, nu media ponderată a tuturor "
            "valorilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce media aritmetică poate fi înșelătoare ca „valoare tipică” într-o "
            "distribuție cu coadă lungă de valori mari?"
        ),
        "options": [
            "pentru că câteva valori foarte mari trag media spre dreapta, departe de "
            "majoritatea cazurilor",
            "în astfel de cazuri mediana descrie adesea mai bine centrul distribuției",
            "pentru că modul devine automat mai mare decât mediana",
            "pentru că suma abaterilor față de medie nu mai poate fi zero",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă la toate valorile unui set adaugi o constantă k, media aritmetică:"
        ),
        "options": [
            "crește (sau scade) cu exact k",
            "rămâne neschimbată",
            "se înmulțește cu k",
            "devine egală cu mediana",
        ],
        "correct": "a",
    },
    # —— 11–15: proprietăți ale mediei, asimetrie ——
    {
        "stem": (
            "Care dintre următoarele proprietăți ale mediei aritmetice sunt corecte?"
        ),
        "options": [
            "dacă înmulțești (sau împarți) toate valorile cu aceeași constantă nenulă, "
            "media se înmulțește (sau se împarte) cu aceeași constantă",
            "suma abaterilor valorilor față de medie este zero: Σ(X − m) = 0",
            "suma pătratelor abaterilor față de medie este minimă față de orice alt "
            "punct de referință",
            "suma abaterilor la medie este maximă, nu minimă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Proprietatea conform căreia suma pătratelor abaterilor Σ(X − m)² este "
            "minimă se referă la:"
        ),
        "options": [
            "media aritmetică — niciun alt număr nu minimizează mai bine abaterile "
            "pătratice totale",
            "mediana — pentru că împarte distribuția la 50%",
            "modul — pentru că este valoarea cea mai frecventă",
            "amplitudinea — diferența dintre maxim și minim",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele ordini între mod (Mo), mediană (Me) și medie (M) "
            "sunt corecte?"
        ),
        "options": [
            "distribuție simetrică: Mo ≈ Me ≈ M",
            "asimetrie pozitivă (coadă dreapta): Mo < Me < M",
            "asimetrie negativă (coadă stânga): M < Me < Mo",
            "asimetrie pozitivă: M < Me < Mo",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele proprietăți liniare ale mediei aritmetice sunt "
            "corecte?"
        ),
        "options": [
            "dacă adaugi o constantă k la fiecare valoare, mediei i se adaugă k",
            "dacă înmulțești fiecare valoare cu o constantă nenulă c, media se înmulțește "
            "cu c",
            "dacă adaugi k, mediana crește mereu cu mai mult decât media",
            "înmulțirea valorilor cu c modifică doar modul, nu și media",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Într-o distribuție cu asimetrie pozitivă (coadă spre dreapta), ordinea "
            "tipică a indicatorilor este:"
        ),
        "options": [
            "Mo < Me < M (mod < mediană < medie)",
            "M < Me < Mo",
            "Mo = Me = M",
            "Me < Mo < M",
        ],
        "correct": "a",
    },
    # —— 16–20: sinteză, alegerea indicatorului ——
    {
        "stem": (
            "În distribuții asimetrice, mediana se situează, de regulă:"
        ),
        "options": [
            "între mod și medie",
            "întotdeauna sub mod și sub medie, indiferent de tipul asimetriei",
            "peste mod și peste medie, în orice situație",
            "în afara intervalului dintre mod și medie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre alegerea indicatorului de tendință "
            "centrală sunt corecte?"
        ),
        "options": [
            "la date nominale, modul este adesea singurul indicator fezabil",
            "la asimetrie marcată, mediana descrie mai bine „centrul” decât media",
            "media rămâne centrală în multe analize inferențiale parametrice",
            "modul este preferat pentru inferență parametrică în locul mediei",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Când distribuția este marcat asimetrică, indicatorul cel mai reprezentativ "
            "pentru „valoarea tipică” este, de obicei:"
        ),
        "options": [
            "mediana",
            "media aritmetică, pentru că folosește toate valorile",
            "modul, pentru că este cel mai frecvent",
            "amplitudinea, pentru că arată întinderea datelor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele capcane privind tendința centrală sunt frecvente?"
        ),
        "options": [
            "folosirea mediei la distribuții puternic asimetrice cu outlieri",
            "confundarea medianei cu modul",
            "presupunerea că Mo = Me = M în orice distribuție",
            "calcularea mediei la date nominale fără justificare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect modul, mediana, media și asimetria?"
        ),
        "options": [
            "Mo = cea mai frecventă; Me = mijlocul ordinal (50%); m = ΣX / N",
            "proprietăți medie: ±k la valori → medie ±k; ×c → medie ×c; Σ(X−m)=0",
            "simetric: Mo ≈ Me ≈ M; pozitiv: Mo < Me < M; negativ: M < Me < Mo",
            "la asimetrie, mediana stă de regulă între mod și medie",
        ],
        "correct": "abcd",
    },
]

assert len(CENTRAL_TENDENCY_ITEMS) == 20
