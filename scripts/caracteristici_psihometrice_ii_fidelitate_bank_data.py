"""Itemi — Caracteristici psihometrice II, cap. 2: fidelitatea testului (50 itemi, ID 11296–11345)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

FIDELITATE_TEST_ITEMS: List[Item] = [
    {
        "stem": (
            "Coeficientul Alpha Cronbach (α) este un indice al fidelității prin "
            "consistență internă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Metoda test-retest evaluează fidelitatea comparând scorurile obținute "
            "la:"
        ),
        "options": [
            "aceeași formă a testului, la momente diferite",
            "două forme paralele, în aceeași zi",
            "jumătăți ale aceluiași test, într-o singură administrare",
            "acordul dintre doi examinatori independenți",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care asocieri corecte descriu metoda test-retest?"
        ),
        "options": [
            "aceeași formă, interval de timp între administrări",
            "sursa principală de eroare: eșantionare temporală",
            "sursa principală de eroare: diferențe între examinatori",
            "nu presupune readministrarea aceluiași instrument",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Formele alternative administrate imediat (paralele) evaluează fidelitatea "
            "prin:"
        ),
        "options": [
            "compararea a două forme echivalente de conținut",
            "eșantionare de conținut (itemi diferiți, construct similar)",
            "eșantionare temporală exclusivă, fără forme noi",
            "acord inter-rater al scorării",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Formele alternative cu administrare întârziată implică:"
        ),
        "options": [
            "două forme paralele",
            "interval de timp între administrări",
            "surse de eroare: timp și conținut combinate",
            "doar consistență internă într-o singură sesiune",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Metoda half-split (jumătăți) estimează fidelitatea pe baza:"
        ),
        "options": [
            "corelației dintre jumătățile aceluiași test",
            "eșantionării de conținut în cadrul unui singur test",
            "acordului între examinatori diferiți",
            "retestării aceleiași forme după o lună",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "KR-20 și Alpha Cronbach aparțin, de regulă, estimării:"
        ),
        "options": [
            "fidelității prin consistență internă",
            "validității de criteriu extern",
            "acordului inter-rater exclusiv",
            "stabilității temporale fără itemi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Metoda inter-rater evaluează fidelitatea prin:"
        ),
        "options": [
            "acordul dintre examinatori/scoreri",
            "sursa de eroare: diferențe între examinatori",
            "corelația dintre jumătățile unui test",
            "compararea a două forme paralele imediate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care perechi «metodă — sursă principală de eroare» sunt corecte?"
        ),
        "options": [
            "test-retest — eșantionare temporală",
            "forme alternative — eșantionare de conținut",
            "half-split — eșantionare de conținut",
            "inter-rater — diferențe între examinatori",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Formula Spearman-Brown pentru half-split este:"
        ),
        "options": [
            "rtt = 2·rhh / (1 + rhh)",
            "rtt = rhh / (2 − rhh)",
            "rtt = 1 − rhh²",
            "rtt = rhh + 0,50",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă rhh = 0,50, valoarea rtt obținută cu Spearman-Brown este "
            "aproximativ:"
        ),
        "options": [
            "0,66",
            "0,50",
            "0,75",
            "0,33",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Formula Spearman-Brown pentru modificarea lungimii testului are forma:"
        ),
        "options": [
            "rnn = n·rtt / [1 + (n−1)·rtt]",
            "rnn = rtt / n",
            "rnn = n + rtt",
            "rnn = rtt² · n",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un test cu 20 itemi are rtt = 0,87. Pentru a atinge aproximativ rtt = "
            "0,95, Spearman-Brown sugerează:"
        ),
        "options": [
            "o lungime de circa 56 itemi (raport n ≈ 2,82)",
            "păstrarea a 20 itemi, fără modificare",
            "reducerea la 10 itemi",
            "eliminarea jumătății itemilor pentru validitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "KR-20 se aplică, de regulă, testelor cu itemi:"
        ),
        "options": [
            "dicotomici (corect/greșit)",
            "cu scor pe Likert în 5 trepte",
            "proiective nestandardizate",
            "fără variabilitate între itemi",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Alpha Cronbach este potrivită, de regulă, pentru:"
        ),
        "options": [
            "itemi cu mai multe opțiuni de răspuns (ex. Likert)",
            "estimarea consistenței interne a scalei",
            "necesită varianță între itemi pentru calcul",
            "acordul exclusiv între doi examinatori",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Alpha Cronbach măsoară validitatea de construct, nu fidelitatea."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care elemente apar în formula KR-20 pentru itemi dicotomici?"
        ),
        "options": [
            "numărul de itemi n",
            "varianța totală a scorurilor SDt²",
            "termenul Σpq pentru itemi",
            "coeficientul de corelație cu criteriul extern rxy",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Structura formulei Alpha Cronbach include:"
        ),
        "options": [
            "factorul n/(n−1)",
            "raportul dintre suma varianțelor itemilor și varianța totală",
            "1 − Σ(SDi²) / SDt²",
            "corelația dintre jumătățile testului rhh",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În interpretare, α (Alpha) indică:"
        ),
        "options": [
            "consistența internă — fidelitatea itemilor scalei",
            "validitatea automată față de orice criteriu",
            "acordul temporal garantat la retest",
            "mărimea efectului în populație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Când rtt crește, eroarea standard a măsurării (SEM) tinde să scadă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Pentru decizii individuale cu miză mare, pragul orientativ al fidelității "
            "este:"
        ),
        "options": [
            "≥ 0,90 – 0,95",
            "0,70 – 0,80",
            "≤ 0,50",
            "exact 1,00 obligatoriu în orice context",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În cercetare, valori rtt de 0,70 – 0,80 sunt adesea considerate:"
        ),
        "options": [
            "acceptabile, în funcție de scop și consecințe",
            "identice cu cerințele pentru decizii clinice individuale",
            "inutilizabile în orice situație",
            "superioare obligatoriu valorii 0,95",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre pragurile rtt sunt corecte?"
        ),
        "options": [
            "depind de scopul utilizării testului",
            "deciziile individuale importante cer fidelitate mai mare",
            "un singur prag universal e suficient pentru orice domeniu",
            "0,70–0,80 poate fi acceptabil în cercetare exploratorie",
            "pragurile nu țin cont de consecințele deciziei",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Eroarea standard a măsurării (SEM) se calculează astfel:"
        ),
        "options": [
            "SEM = SDt · √(1 − rtt)",
            "SEM = SDt · rtt",
            "SEM = SDt / rtt",
            "SEM = √(SDt² + rtt)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă SDt = 10 și rtt = 0,80, SEM este aproximativ:"
        ),
        "options": [
            "5",
            "8",
            "10",
            "2",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Intervalul de încredere al scorului real se construiește, în linii mari, "
            "astfel:"
        ),
        "options": [
            "X ± (z · SEM)",
            "X ± SDt, indiferent de fidelitate",
            "X ± rtt",
            "SR ± rhh",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care intervale orientative pentru scorul real sunt corecte?"
        ),
        "options": [
            "95%: X ± 2·SEM",
            "99%: X ± 3·SEM",
            "95%: X ± 3·SEM",
            "99%: X ± 1·SEM",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un scor QI observat = 120, SEM = 5. Care intervale pentru scorul real "
            "sunt corecte?"
        ),
        "options": [
            "95%: aproximativ 110 – 130",
            "99%: aproximativ 105 – 135",
            "95%: 115 – 125",
            "99%: 120 – 125",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "SEM este legată direct de fidelitatea testului (rtt)."
        ),
        "options": [
            "rtt mai mare → SEM mai mic",
            "SEM reflectă imprecizia scorului observat",
            "SEM crește automat când rtt crește",
            "SEM = 0 indiferent de rtt",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Corelația rhh obținută din half-split, fără Spearman-Brown, tinde să "
            "subestimeze rtt complet al testului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Metoda test-retest este preferabilă când:"
        ),
        "options": [
            "constructul e relativ stabil în timp",
            "se acceptă interval rezonabil între administrări",
            "constructul fluctuează rapid zi de zi din definiție",
            "itemii se schimbă complet între sesiuni",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Formele alternative sunt utile când:"
        ),
        "options": [
            "vrei să reduci efectul de practică/memorare a itemilor",
            "ai două seturi paralele de itemi echivalenți",
            "scorarea e pur subiectivă fără barem",
            "nu există variabilitate între itemi",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care limitări ale test-retest sunt formulate corect?"
        ),
        "options": [
            "efect de practică sau oboseală între sesiuni",
            "schimbări reale ale trăsăturii măsurate în timp",
            "elimină complet eroarea de conținut",
            "nu e potrivit dacă constructul e instabil temporal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Inter-rater este indicat în special când:"
        ),
        "options": [
            "scorarea depinde de judecata examinatorului",
            "există risc de subiectivitate în notare",
            "testul are itemi dicotomici auto-corectați",
            "toate itemii sunt cu răspuns unic computerizat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Consistența internă (KR-20, α) se estimează, de obicei, din:"
        ),
        "options": [
            "o singură administrare a testului",
            "variația itemilor și variația totală",
            "două forme paralele la interval de o lună",
            "acordul a trei examinatori pe probe video",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Erorile de eșantionare de conținut apar în special la:"
        ),
        "options": [
            "half-split",
            "forme alternative",
            "KR-20 / Alpha",
            "test-retest cu aceeași formă identică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Eroarea de eșantionare temporală este centrală pentru:"
        ),
        "options": [
            "test-retest",
            "forme alternative întârziate",
            "inter-rater imediat",
            "Alpha într-o singură administrare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care sinteze despre metodele de fidelitate sunt corecte?"
        ),
        "options": [
            "test-retest → eșantionare temporală",
            "forme alternative → eșantionare de conținut (± timp)",
            "half-split / KR-20 / α → conținut sau consistență internă",
            "inter-rater → diferențe între examinatori",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Spearman-Brown pentru lungimea testului presupune că:"
        ),
        "options": [
            "itemii adăugați sunt paraleli cu cei existenți",
            "lungimea mai mare poate crește rtt",
            "orice item nou scade automat fidelitatea",
            "rtt scade liniar cu numărul de itemi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Când rtt crește, SEM devine obligatoriu mai mare decât SDt."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Ce indică practic un SEM mai mic?"
        ),
        "options": [
            "scor observat mai precis în jurul scorului real",
            "interval de încredere mai îngust",
            "validitate de construct garantată",
            "eroarea de măsurare devine zero",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Intervalul X ± z·SEM estimează:"
        ),
        "options": [
            "zona în care plutește probabil scorul real (SR)",
            "incertitudinea legată de fidelitatea testului",
            "diferența garantată față de media populației",
            "validitatea criteriului extern",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În half-split, rhh reprezintă:"
        ),
        "options": [
            "corelația dintre scorurile celor două jumătăți",
            "validitatea de criteriu a testului",
            "acordul inter-rater",
            "coeficientul Alpha Cronbach",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Când alegi între KR-20 și Alpha Cronbach:"
        ),
        "options": [
            "KR-20 — itemi dicotomici",
            "Alpha — itemi cu mai multe opțiuni",
            "Alpha — itemi cu varianță pe scale multi-punct",
            "KR-20 — scale Likert cu 5 trepte",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care formule și relații din capitolul fidelității sunt corecte?"
        ),
        "options": [
            "rtt = 2·rhh / (1 + rhh)",
            "rnn = n·rtt / [1 + (n−1)·rtt]",
            "SEM = SDt · √(1 − rtt)",
            "SEM = SDt · √rtt",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele recapiturează corect pragurile și scopul lor?"
        ),
        "options": [
            "decizii individuale importante: rtt ≈ 0,90–0,95",
            "cercetare: 0,70–0,80 poate fi acceptabil",
            "pragul depinde de consecințele deciziei",
            "pragurile se interpretează contextual, nu mecanic",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Procedura half-split implică, de regulă:"
        ),
        "options": [
            "împărțirea testului în două părți egale",
            "corelația rhh între jumătăți",
            "correcție Spearman-Brown pentru rtt",
            "extrapolarea rtt din rhh prin Spearman-Brown",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care sinteze despre SEM și intervalul de încredere sunt corecte?"
        ),
        "options": [
            "SEM scade când rtt crește",
            "95%: X ± 2·SEM; 99%: X ± 3·SEM",
            "ex.: QI 120, SEM 5 → 95%: 110–130",
            "intervalul elimină complet eroarea de măsurare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Despre forme paralele, care afirmații sunt plauzibile?"
        ),
        "options": [
            "itemii diferă, dar măsoară același construct",
            "echivalența perfectă e dificil de obținut",
            "administrarea imediată reduce efectul timpului",
            "garantează validitate de criteriu maximă automat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care idei despre fidelitatea testului sintetizează corect capitolul?"
        ),
        "options": [
            "metode distincte → surse de eroare diferite",
            "Spearman-Brown corectează half-split și lungimea",
            "KR-20/α pentru consistență internă",
            "SEM + interval de încredere leagă rtt de precizia scorului",
        ],
        "correct": "abcd",
    },
]


def _count_dist(rows: list) -> dict[str, int]:
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
            continue
        counts[str(len(set(row["correct"])))] += 1
    return counts


assert len(FIDELITATE_TEST_ITEMS) == 50
assert _count_dist(FIDELITATE_TEST_ITEMS) == {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}
