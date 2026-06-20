"""Itemi — Caracteristici psihometrice II, seg. 4: selecție profesională + recapitulare (40 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SELECIE_PROFESIONALA_ITEMS: List[Item] = [
    {
        "stem": "În selecția profesională, relația rxy < rtt este considerată, de regulă, respectată teoretic.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Eroarea standard de măsurare (SEM) este legată direct de validitatea criterială rxy.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Validitatea concurentă presupune, tipic, măsurarea criteriului aproximativ simultan cu predictorul.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Dacă rtt crește, iar SDt rămâne constant, SEM tinde să crească.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Fidelitatea unui test se referă, în esență, la:",
        "options": [
            "consistența rezultatelor în condiții comparabile",
            "gradul în care testul măsoară constructul intenționat",
            "relația scorului cu un criteriu extern de performanță",
            "acoperirea reprezentativă a domeniului prin itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Validitatea, în sens psihometric, indică în principal că:",
        "options": [
            "testul măsoară ceea ce pretinde că măsoară",
            "scorurile rămân stabile la retestare",
            "itemii au dificultate medie echilibrată",
            "distribuția scorurilor este normală",
        ],
        "correct": "a",
    },
    {
        "stem": "În modelul clasic X = SR + E, simbolul X reprezintă:",
        "options": [
            "scorul observat obținut la administrare",
            "scorul real al persoanei pe construct",
            "componenta de eroare aleatorie",
            "scorul estimat pe criteriu extern",
        ],
        "correct": "a",
    },
    {
        "stem": "Metoda test-retest estimează fidelitatea prin:",
        "options": [
            "eșantionare temporală a erorii",
            "eșantionare de conținut între jumătăți de test",
            "compararea a două forme paralele imediate",
            "acordul dintre evaluatori diferiți",
        ],
        "correct": "a",
    },
    {
        "stem": "Metoda half-split (jumătăți) abordează fidelitatea ca problemă de:",
        "options": [
            "eșantionare de conținut în cadrul aceluiași test",
            "eșantionare temporală între două sesiuni",
            "validitate de criteriu cu indicator extern",
            "contaminare deliberată a criteriului",
        ],
        "correct": "a",
    },
    {
        "stem": "Coeficientul Alpha Cronbach estimează, de regulă:",
        "options": [
            "consistența internă a scalei",
            "validitatea predictivă pe termen lung",
            "acordul inter-evaluator",
            "reprezentativitatea conținutului față de experți",
        ],
        "correct": "a",
    },
    {
        "stem": "Formula KR-20 se aplică, în mod tipic, la itemi:",
        "options": [
            "dicotomici (corect/greșit)",
            "cu scale Likert cu 7 trepte",
            "subiectivi, fără cheie de scorare",
            "proiectivi, interpretați clinic",
        ],
        "correct": "a",
    },
    {
        "stem": "Într-un studiu de validitate criterială, predictorul este:",
        "options": [
            "scorul obținut la testul evaluat",
            "nota medie de la un curs anterior",
            "numărul de itemi ai scalei",
            "coeficientul de consistență internă",
        ],
        "correct": "a",
    },
    {
        "stem": "Contaminarea criteriului apare când:",
        "options": [
            "evaluatorul criteriului cunoaște scorul la test",
            "criteriul este măsurat cu întârziere de un an",
            "predictorul are itemi dificili",
            "eșantionul are varianță redusă",
        ],
        "correct": "a",
    },
    {
        "stem": "Validitatea de construct vizează, în principal:",
        "options": [
            "coerența empirică a unui construct teoretic",
            "acoperirea domeniului prin judecata experților",
            "stabilitatea scorului la două săptămâni distanță",
            "raportul dintre scorul brut și numărul de itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Matricea multitrait-multimethod (MTMM) este asociată cu:",
        "options": [
            "Campbell și Fiske (1959)",
            "Thorndike (reguli pentru itemi)",
            "Lawshe (CVR)",
            "Binet (scale de inteligență)",
        ],
        "correct": "a",
    },
    {
        "stem": "Un CVR negativ în formula Lawshe indică, de regulă, că:",
        "options": [
            "mai puțin de jumătate dintre experți consideră itemul esențial",
            "toți experții consideră itemul esențial",
            "itemul a fost răspuns corect de majoritatea respondenților",
            "validitatea criterială depășește 0,70",
        ],
        "correct": "a",
    },
    {
        "stem": "Metafora lui Binet compară testul psihologic cu un cântar simplu pentru a arăta că:",
        "options": [
            "măsurarea constructelor psihologice nu este directă ca măsurarea fizică",
            "inteligența se măsoară identic cu masa corporală",
            "testele psihologice nu necesită standardizare",
            "orice test este la fel de precis ca un instrument fizic",
        ],
        "correct": "a",
    },
    {
        "stem": "Formula de corecție a ghicirii la itemi cu alegere multiplă este:",
        "options": [
            "X - W/(n-1)",
            "X + W/(n-1)",
            "X - W·n",
            "(X-W)/n",
        ],
        "correct": "a",
    },
    {
        "stem": "Pentru decizii individuale cu miză mare, orientarea uzuală privind fidelitatea este:",
        "options": [
            "rtt orientativ în jurul valorilor 0,90–0,95",
            "interpretarea scorului cu banda de eroare (SEM), nu doar valoarea punctuală",
            "rtt orientativ în jurul valorilor 0,50–0,60",
            "acceptarea oricărui rxy pozitiv, indiferent de magnitudine",
        ],
        "correct": "ab",
    },
    {
        "stem": "Intervalul aproximativ de 95% pentru scorul real poate fi estimat ca:",
        "options": [
            "scor observat ± 2·SEM",
            "necesită estimarea SEM din rtt și SDt",
            "scor observat ± 3·SEE",
            "scor observat ± 2·SEE",
        ],
        "correct": "ab",
    },
    {
        "stem": "Validitatea de conținut se bazează, în mod central, pe:",
        "options": [
            "evaluarea experților privind relevanța itemilor",
            "delimitarea domeniului și a specificațiilor de conținut",
            "corelația imediată cu un criteriu extern",
            "consistența internă dintr-o singură administrare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Validitatea predictivă implică, caracteristic:",
        "options": [
            "criteriu măsurat ulterior predictorului",
            "utilitate pentru anticiparea performanței viitoare",
            "măsurare simultană a predictorului și criteriului",
            "comparare cu un test deja validat în același moment",
        ],
        "correct": "ab",
    },
    {
        "stem": "În tabelele orientative de tip Smith, un rxy de aproximativ 0,50 sugerează:",
        "options": [
            "utilitate predictivă excelentă",
            "utilitate superioară față de valori sub 0,30",
            "utilitate predictivă acceptabilă",
            "utilitate predictivă slabă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scenariul «măsoară constructul corect și foarte bine» corespunde unui test:",
        "options": [
            "valid",
            "fidel",
            "sound (solid, credibil)",
            "invalid, dar constant",
        ],
        "correct": "abc",
    },
    {
        "stem": "Scenariul «nu măsoară ce trebuie» indică, de regulă:",
        "options": [
            "validitate scăzută sau problematică",
            "risc de interpretări greșite ale scorului",
            "fidelitate garantată automat",
            "utilitate decizională redusă pentru scopul declarat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Metoda formelor alternative imediate presupune:",
        "options": [
            "două forme paralele administrate aproape simultan",
            "eșantionare de conținut prin itemi diferiți",
            "o singură formă administrată de două ori după un an",
            "acordul dintre doi evaluatori diferiți",
        ],
        "correct": "ab",
    },
    {
        "stem": "Formula SEM = SDt·√(1−rtt) arată că:",
        "options": [
            "SEM este legată de fidelitate (rtt)",
            "rtt mai mare tinde să reducă SEM",
            "SEM este identică cu SEE",
            "SEM depinde de SDt",
        ],
        "correct": "abd",
    },
    {
        "stem": "Obligația principală a constructorului privind validitatea de conținut este:",
        "options": [
            "definirea domeniului măsurat",
            "maparea itemilor la specificații de conținut",
            "atingerea unui rxy > 0,70 înainte de pilotare",
            "revizuirea itemilor cu experți relevanți",
        ],
        "correct": "ab",
    },
    {
        "stem": "Metoda inter-rater (inter-evaluator) estimează fidelitatea din:",
        "options": [
            "diferențe între examinatori/scoreri",
            "acordul la scorare a aceleiași probe",
            "eșantionare temporală pură",
            "corelația cu un criteriu extern",
        ],
        "correct": "ab",
    },
    {
        "stem": "În selecția profesională, SEE = SDy·√(1−rxy²) exprimă:",
        "options": [
            "eroarea medie la predicția criteriului din scorul testului",
            "dependența erorii de validitatea criterială",
            "marja de incertitudine a estimării pe criteriu",
            "consistența internă a predictorului",
        ],
        "correct": "abc",
    },
    {
        "stem": "Relația dintre validitate și eroarea de estimare (SEE) este, de regulă:",
        "options": [
            "rxy mai mare → SEE mai mică",
            "rxy mai mic → predicții mai imprecise",
            "SEE crește odată cu rxy",
            "SEE este independentă de magnitudinea rxy",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tabelele Taylor-Russell sunt utile pentru a evalua:",
        "options": [
            "utilitatea practică a testului într-o decizie de selecție",
            "impactul validității asupra proporției de selecții corecte",
            "efectul ratei de bază și al proporției selectate",
            "consistența internă a itemilor dicotomici",
        ],
        "correct": "abc",
    },
    {
        "stem": "Selectează enunțurile corecte despre formulele Spearman-Brown și lungimea testului.",
        "options": [
            "half-split: rtt = 2·rhh / (1 + rhh)",
            "lungime: rnn = n·rtt / [1 + (n−1)·rtt]",
            "rtt mai mare permite atingerea aceleiași fidelitate țintă cu mai puțini itemi",
            "presupune itemi paraleli de calitate comparabilă",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce afirmații descriu corect KR-20 și Alpha?",
        "options": [
            "KR-20 folosește varianța totală și varianța itemilor dicotomici",
            "Alpha folosește varianța totală și varianțele itemilor",
            "ambele estimează consistența internă",
            "ambele măsoară validitatea criterială direct",
        ],
        "correct": "abc",
    },
    {
        "stem": "În selecție profesională, SEE mic este important pentru că:",
        "options": [
            "predicțiile criteriului sunt mai strânse în jurul valorii reale",
            "deciziile individuale devin mai puțin riscante",
            "face ca orice rxy pozitiv să fie suficient pentru decizii cu miză mare",
            "intervalul de eroare al estimării se îngustează",
        ],
        "correct": "abd",
    },
    {
        "stem": "Ce variabile influențează tipic rezultatele din tabelele Taylor-Russell?",
        "options": [
            "magnitudinea validității testului",
            "rata de bază a succesului în populație",
            "proporția persoanelor selectate",
            "numărul de itemi din half-split",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care perechi de formule sunt asociate corect cu scopul lor?",
        "options": [
            "SEM = SDt·√(1−rtt) → eroare legată de fidelitate",
            "SEE = SDy·√(1−rxy²) → eroare la predicția criteriului",
            "CVR = (Ne−N/2)/(N/2) → acordul experților privind esențialitatea itemilor",
            "X−W/(n−1) → corecția răspunsului ghicit",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Selectează afirmațiile corecte despre cele trei tipuri majore de validitate.",
        "options": [
            "conținut: acoperire reprezentativă a domeniului",
            "criteriu: legătură cu indicator extern relevant",
            "construct: coerență teoretică și empirică",
            "toate trei se reduc la aceeași corelație rxy",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce concluzii despre selecția profesională sunt susținute de analiza Taylor-Russell?",
        "options": [
            "validitatea mai mare crește proporția selecțiilor corecte",
            "rata de bază influențează utilitatea practică a testului",
            "proporția selectată modifică riscul decizional",
            "utilitatea depinde de combinația validitate–bază–proporție selectată",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care set sintetizează corect relațiile esențiale din recapitularea psihometrică?",
        "options": [
            "fidelitate = consistență; validitate = măsoară ce trebuie",
            "rxy < rtt; SEM legat de fidelitate; SEE legat de validitate",
            "test-retest → temporal; half-split → conținut; inter-rater → examinatori",
            "Alpha/KR-20 → consistență internă; MTMM → validitate de construct",
        ],
        "correct": "abcd",
    },
]


def _count_dist(rows):
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


assert len(SELECIE_PROFESIONALA_ITEMS) == 40
assert _count_dist(SELECIE_PROFESIONALA_ITEMS) == {
    "1": 14,
    "2": 10,
    "3": 8,
    "4": 4,
    "TF": 4,
}
