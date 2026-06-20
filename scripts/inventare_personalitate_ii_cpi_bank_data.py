"""Itemi — Inventare de personalitate II: CPI (California Psychological Inventory), 60 itemi."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

CPI_ITEMS: List[Item] = [
    {
        "stem": (
            "CPI evaluează în principal comportamentul social al persoanelor normale, "
            "nu diagnosticul psihopatologic clinic."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Inventarul CPI a fost elaborat de Gough și publicat inițial în 1957.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Scala Gi (Good impression) reflectă tendința de a crea o impresie favorabilă exagerată.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Versiunea CPI-260 este recomandată frecvent în context organizațional, fiind mai scurtă.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Profilul CPI devine suspect dacă respondenții lasă necompletate peste 30 de itemi.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "CPI este un test proiectiv nestandardizat, fără scale cu scoruri numerice.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Formatul de răspuns al CPI este, în mod clasic:",
        "options": [
            "Adevărat/Fals pentru afirmații despre sine",
            "alegere multiplă cu patru alternative",
            "răspuns liber narativ, fără barem",
            "evaluare Likert pe 7 trepte obligatorii",
        ],
        "correct": "a",
    },
    {
        "stem": "Autorul inventarului CPI este:",
        "options": [
            "Gough",
            "Cattell",
            "Eysenck",
            "Minnesota Multiphasic (MMPI)",
        ],
        "correct": "a",
    },
    {
        "stem": "Intervalul de vârstă pentru care CPI este standardizat se extinde, de regulă, de la:",
        "options": [
            "12 la 70 de ani",
            "6 la 12 ani",
            "18 la 25 de ani",
            "25 la 55 de ani",
        ],
        "correct": "a",
    },
    {
        "stem": "CPI conține, în structura sa principală:",
        "options": [
            "20 de scale standard",
            "5 scale clinice de psihopatologie",
            "10 scale proiective interpretate global",
            "3 scale de aptitudine cognitivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Utilizarea CPI este permisă, în mod tipic, la nivelul de calificare:",
        "options": [
            "Level B (master în psihologie)",
            "Level A (orice utilizator fără pregătire)",
            "Level C (autoadministrare necalificată)",
            "fără restricții de formare profesională",
        ],
        "correct": "a",
    },
    {
        "stem": "Timpul de administrare pentru CPI-434 este, orientativ:",
        "options": [
            "45–60 minute",
            "10–15 minute",
            "90–120 minute",
            "25–40 minute",
        ],
        "correct": "a",
    },
    {
        "stem": "Timpul de administrare pentru CPI-260 este, orientativ:",
        "options": [
            "25–40 minute",
            "45–60 minute",
            "5–10 minute",
            "peste 2 ore",
        ],
        "correct": "a",
    },
    {
        "stem": "Tipul Alpha din modelul cuboid CPI este caracterizat de:",
        "options": [
            "extraversiune și adaptare socială",
            "introversiune și adaptare socială",
            "extraversiune și neadaptare",
            "introversiune și neadaptare",
        ],
        "correct": "a",
    },
    {
        "stem": "Tipul Beta din modelul cuboid CPI corespunde persoanelor:",
        "options": [
            "introvertite și adaptate social",
            "extravertite și adaptate social",
            "introvertite și neadaptate",
            "extravertite și neadaptate",
        ],
        "correct": "a",
    },
    {
        "stem": "Tipul Gamma din modelul cuboid CPI descrie, de regulă:",
        "options": [
            "extraversiune cu dificultăți de adaptare",
            "introversiune cu adaptare stabilă",
            "control impulsiv ridicat",
            "conformism strict la reguli",
        ],
        "correct": "a",
    },
    {
        "stem": "Tipul Delta din modelul cuboid CPI descrie, de regulă:",
        "options": [
            "introversiune cu dificultăți de adaptare",
            "extraversiune cu adaptare socială bună",
            "dominanță competitivă accentuată",
            "realizare academică excepțională",
        ],
        "correct": "a",
    },
    {
        "stem": "Primul pas în interpretarea CPI (Megargee/McAllister) este:",
        "options": [
            "verificarea validității profilului (Gi, Wb, Cm)",
            "interpretarea combinațiilor complexe între toate scalele",
            "calcularea coeficientului alpha Cronbach",
            "compararea directă cu MMPI fără analiză profil",
        ],
        "correct": "a",
    },
    {
        "stem": "Pe scalele T ale CPI, intervalul 40–60 indică, de regulă:",
        "options": [
            "nivel mediu, apropiat de media normativă",
            "extrem de scăzut, patologic",
            "extrem de ridicat, excepțional",
            "invaliditate automată a profilului",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe scala Do (Dominance) sugerează, de regulă:",
        "options": [
            "asertivitate și orientare competitivă",
            "retraștere și evitarea conflictului",
            "răspunsuri aleatorii la itemi",
            "prezentare negativă exagerată",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe scala Re (Responsibility) este asociat, tipic, cu:",
        "options": [
            "conștiinciozitate și fiabilitate",
            "impulsivitate și iresponsabilitate",
            "nonconformism față de reguli",
            "izolare socială marcată",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor scăzut pe scala So (Socialization) poate sugera:",
        "options": [
            "risc crescut de comportament antisocial sau delincvent",
            "adaptare socială foarte bună",
            "fake good pe scala Gi",
            "control impulsiv excesiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor scăzut pe scala Sc (Self-control) indică, de regulă:",
        "options": [
            "tendință spre impulsivitate",
            "disciplină și autocontrol ridicat",
            "empatie accentuată față de alții",
            "conformism strict la norme",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala Gi (Good impression) semnalează, de regulă:",
        "options": [
            "prezentare excesiv pozitivă (fake good)",
            "prezentare excesiv negativă (fake bad)",
            "răspunsuri la întâmplare",
            "independență față de norme sociale",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala Wb (Well-being) ridicată, în context de validitate, poate indica:",
        "options": [
            "prezentare excesiv negativă (fake bad)",
            "prezentare excesiv pozitivă (fake good)",
            "profil aleator, fără pattern",
            "adaptare socială excelentă confirmată",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala Cm (Communality) foarte atipică sugerează:",
        "options": [
            "răspunsuri posibil aleatorii sau necoerente",
            "conformism perfect la norma grupului",
            "dominanță socială excepțională",
            "realizare academică superioară",
        ],
        "correct": "a",
    },
    {
        "stem": "Pe lângă scalele standard, CPI include și:",
        "options": [
            "13 scale speciale",
            "50 scale clinice de psihoză",
            "itemi proiectivi fără scor numeric",
            "scale de aptitudine mecanică",
        ],
        "correct": "a",
    },
    {
        "stem": "CPI a fost tradus și utilizat în:",
        "options": [
            "peste 40 de limbi, inclusiv în România",
            "doar în limba engleză, fără adaptări",
            "exclusiv în contexte clinice psihiatrice",
            "maximum 3 țări europene",
        ],
        "correct": "a",
    },
    {
        "stem": "Evoluția versiunilor CPI a implicat, progresiv:",
        "options": [
            "scurtarea numărului de itemi (480 → 462 → 434 → 260)",
            "creșterea numărului de itemi la peste 600",
            "trecerea de la A/F la itemi proiectivi",
            "eliminarea scalelor de validitate",
        ],
        "correct": "ab",
    },
    {
        "stem": "Recomandările de utilizare pentru versiunile CPI sunt, de regulă:",
        "options": [
            "CPI-434 în context educațional și clinic",
            "CPI-260 în organizații și baterii de teste",
            "CPI-260 ca instrument principal de diagnostic psihiatric",
            "CPI-434 exclusiv pentru copii sub 12 ani",
        ],
        "correct": "ab",
    },
    {
        "stem": "Dezvoltarea scalelor CPI a combinat, istoric:",
        "options": [
            "metode empirice de construcție",
            "analiza consistenței interne",
            "selecția itemilor doar pe baza teoriei pure, fără date",
            "ignorarea completă a fidelității",
        ],
        "correct": "ab",
    },
    {
        "stem": "Fidelitatea scalelor CPI (Alpha Cronbach) se situează, orientativ, în intervalul:",
        "options": [
            "0,50–0,80 pentru majoritatea scalelor",
            "valori moderate, utile în practică aplicativă",
            "0,95–0,99 pentru toate scalele",
            "sub 0,30, indicând utilitate redusă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Validitatea CPI este susținută, printre altele, de:",
        "options": [
            "structura factorială în 5 factori (Gough)",
            "literatură empirică extinsă",
            "utilizare exclusivă ca test proiectiv",
            "lipsa studiilor empirice independente",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scoruri ridicate pe Cs (Conformity) și scăzute pe Cs indică, respectiv:",
        "options": [
            "Cs ridicat: respectarea regulilor și normelor",
            "Cs scăzut: tendință nonconformistă",
            "Cs ridicat: impulsivitate crescută",
            "Cs scăzut: conformism strict",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scor scăzut pe Sp (Social presence) poate sugera:",
        "options": [
            "pesimism și retragere socială",
            "prezență socială plăcută și optimism",
            "fake good pe scala Gi",
            "dominanță competitivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Modelul cuboid CPI are trei versiuni ale tipologiei, orientate spre:",
        "options": [
            "introversiune–extraversiune",
            "norme de adaptare",
            "realizare",
            "diagnosticul tulburărilor de personalitate DSM",
        ],
        "correct": "abc",
    },
    {
        "stem": "Scorurile T extreme pe CPI sunt, de regulă, interpretate ca:",
        "options": [
            "peste 70 = foarte ridicat",
            "sub 30 = foarte scăzut",
            "40–60 = întotdeauna patologice",
            "50 = invalid automat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scoruri ridicate pe Sy (Sociability) și Sp (Social presence) sugerează, de regulă:",
        "options": [
            "orientare spre contact social și prietenie",
            "prezență socială plăcută, optimism",
            "retraștere și pesimism",
            "răspunsuri aleatorii",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scoruri ridicate pe Sa (Self-acceptance) și In (Independence) indică, tipic:",
        "options": [
            "ambitie și sentiment de realizare",
            "autonomie și independență",
            "dependență față de aprobarea socială",
            "nonconformism extrem fără adaptare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scoruri ridicate pe Em (Empathy) și Re (Responsibility) sunt asociate, de regulă, cu:",
        "options": [
            "sensibilitate față de starea altora",
            "conștiinciozitate și fiabilitate",
            "distanță emoțională și iresponsabilitate",
            "impulsivitate crescută",
        ],
        "correct": "ab",
    },
    {
        "stem": "CPI este aplicabil în context educațional pentru:",
        "options": [
            "explorarea succesului școlar",
            "consiliere vocațională",
            "diagnosticul obligatoriu al psihozei",
            "înlocuirea completă a evaluării cognitive",
        ],
        "correct": "ab",
    },
    {
        "stem": "CPI este aplicabil în context organizațional pentru:",
        "options": [
            "selecție de personal",
            "promovare și planificarea succesiunii",
            "tratarea medicală a tulburărilor majore",
            "evaluarea proiectivă nestandardizată",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scoruri ridicate pe Ac (Achievement via conformance) și Ai (Achievement via independence) indică:",
        "options": [
            "succes în medii structurate, respectând reguli",
            "realizare prin creativitate și autonomie",
            "necesitate permanentă de supraveghere",
            "imposibilitatea adaptării organizaționale",
        ],
        "correct": "ab",
    },
    {
        "stem": "Pașii interpretării CPI (Megargee/McAllister) includ, printre alții:",
        "options": [
            "analiza profilului general (tip cuboid)",
            "interpretarea scalelor individuale",
            "analiza clusterelor de scale (4 grupuri)",
            "ignorarea scalelor de validitate",
        ],
        "correct": "abc",
    },
    {
        "stem": "Scalele standard Do, Cs și Sy reflectă, în principal, dimensiuni de:",
        "options": [
            "dominanță și asertivitate (Do)",
            "conformism la reguli (Cs)",
            "sociabilitate și contact social (Sy)",
            "răspunsuri aleatorii (Cm)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Interpretarea scalelor Gi, Wb și Cm este esențială pentru că:",
        "options": [
            "detectează prezentare socială distorsionată",
            "identifică răspunsuri posibil aleatorii",
            "înlocuiesc complet analiza profilului cuboid",
            "permit evaluarea credibilității profilului",
        ],
        "correct": "abd",
    },
    {
        "stem": "Scalele Ie (Intellectual efficiency), Py (Psychological mindedness) și Fx (Flexibility) vizează:",
        "options": [
            "organizare și încredere intelectuală",
            "sensibilitate la motivele altora",
            "adaptabilitate la schimbare",
            "diagnosticul proiectiv al conflictelor inconștiente",
        ],
        "correct": "abc",
    },
    {
        "stem": "La adolescenți, combinația Re + So + Sc este utilă pentru:",
        "options": [
            "evaluarea responsabilității și adaptării sociale",
            "identificarea autocontrolului",
            "predicția exclusivă a coeficientului IQ",
            "interpretarea profilului în context de dezvoltare",
        ],
        "correct": "abd",
    },
    {
        "stem": "CPI este util în context clinic, deși nu e test de psihopatologie, pentru:",
        "options": [
            "identificarea pattern-urilor maladaptative",
            "explorarea riscurilor asociate alcoolismului",
            "studiu al tendințelor delincvente",
            "diagnosticul formal al schizofreniei",
        ],
        "correct": "abc",
    },
    {
        "stem": "Calitatea psihometrică a CPI este susținută de:",
        "options": [
            "standardizare pe populații normale",
            "traducere și utilizare în peste 40 de limbi",
            "literatură de cercetare vastă",
            "norme T pe populații reprezentative",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Al cincilea pas interpretativ CPI (Megargee/McAllister) presupune:",
        "options": [
            "interpretarea combinațiilor între scale",
            "analiza configurațiilor specifice (ex. Re + So + Sc)",
            "verificarea scalelor Gi, Wb, Cm",
            "sinteza relațiilor dintre scale, nu doar scoruri izolate",
        ],
        "correct": "abd",
    },
    {
        "stem": "Scala T (Tolerance) și scorurile F/M (Femininity–Masculinity) se interpretează, de regulă:",
        "options": [
            "T ridicat = permisivitate și maturitate socială",
            "T scăzut = criticitate și distanțare",
            "F/M depinde de gen și normele aferente",
            "F/M măsoară direct coeficientul de inteligență",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care elemente descriu corect prezentarea generală a CPI?",
        "options": [
            "autor: Gough (1957)",
            "obiectiv: comportament social la persoane normale",
            "vârste: 12–70 ani",
            "format răspuns Adevărat/Fals",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care perechi tip–caracteristică din modelul cuboid CPI sunt corecte?",
        "options": [
            "Alpha: extravertit, adaptat",
            "Beta: introvertit, adaptat",
            "Gamma: extravertit, neadaptat",
            "Delta: introvertit, neadaptat",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care pași aparțin secvenței Megargee/McAllister de interpretare CPI?",
        "options": [
            "verificarea validității profilului",
            "analiza profilului general (cuboid)",
            "interpretarea scalelor individuale",
            "analiza clusterelor de scale și a combinațiilor",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care domenii de aplicare sunt consacrate pentru CPI?",
        "options": [
            "educațional (succes școlar, consiliere vocațională)",
            "organizațional (selecție, promovare, succesiune)",
            "clinic (pattern-uri maladaptative, nu diagnostic psihiatric primar)",
            "cercetare (literatură vastă, calitate psihometrică)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care scale CPI aparțin evaluării validității profilului?",
        "options": [
            "Gi — impresie favorabilă exagerată",
            "Wb — prezentare negativă exagerată",
            "Cm — răspunsuri posibil aleatorii",
            "Do — dominanță socială",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre scalele standard CPI sunt corecte?",
        "options": [
            "Do ridicat ≈ asertiv, competitiv",
            "So scăzut ≈ risc de delincvență potențială",
            "Sc scăzut ≈ impulsiv",
            "Re scăzut ≈ iresponsabil, nefiabil",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce set sintetizează corect CPI ca instrument psihologic?",
        "options": [
            "20 scale standard + 13 speciale; format A/F",
            "Level B; invalidare dacă >30 itemi necompletați",
            "CPI-260 pentru organizații; CPI-434 pentru educație/clinic",
            "scale T; model cuboid; pași Megargee/McAllister",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Al patrulea pas Megargee/McAllister presupune analiza clusterelor de scale, adică:",
        "options": [
            "gruparea celor 20 scale standard în 4 configurații",
            "identificarea pattern-urilor scalelor înrudite",
            "substituirea interpretării scalelor individuale",
            "pregătirea pasului combinațiilor inter-scale",
        ],
        "correct": "abd",
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


assert len(CPI_ITEMS) == 60
assert _count_dist(CPI_ITEMS) == {"1": 22, "2": 14, "3": 12, "4": 6, "TF": 6}
