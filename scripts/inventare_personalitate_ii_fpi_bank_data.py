"""Itemi — Inventare de personalitate II, seg. 3: FPI Freiburg (50 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

FPI_ITEMS: List[Item] = [
    {
        "stem": (
            "Inventarul de Personalitate Freiburg (FPI) a fost elaborat de "
            "Fahrenberg, Selg și Hampel și publicat inițial în 1970."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Formatul de răspuns al FPI este, în mod clasic, Da/Nu "
            "(Adevărat/Fals)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "FPI-R conține 138 itemi scorabili plus un item de practică "
            "care nu intră în scorare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Scorurile FPI depind semnificativ de vârstă — tinerii obțin, "
            "de regulă, scoruri mai ridicate decât vârstnicii."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "FPI este un test proiectiv nestandardizat, fără scale cu scoruri "
            "numerice stabilite."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Autorii inventarului FPI sunt:",
        "options": [
            "Fahrenberg, Selg și Hampel",
            "Eysenck și Eysenck",
            "Gough",
            "Cattell",
        ],
        "correct": "a",
    },
    {
        "stem": "Versiunile principale ale familiei FPI includ:",
        "options": [
            "FPI-G, FPI-A/B/K și FPI-R",
            "EPQ-R și IVE",
            "CPI-260 și CPI-434",
            "MMPI-2 și MMPI-A",
        ],
        "correct": "a",
    },
    {
        "stem": "Timpul de administrare pentru FPI-G (versiunea clasică) este, orientativ:",
        "options": [
            "30–40 minute",
            "10–15 minute",
            "90–120 minute",
            "5–10 minute",
        ],
        "correct": "a",
    },
    {
        "stem": "Timpul de administrare pentru FPI-R este, orientativ:",
        "options": [
            "10–30 minute",
            "30–40 minute",
            "60–90 minute",
            "peste 2 ore",
        ],
        "correct": "a",
    },
    {
        "stem": "FPI poate fi administrat, de regulă, de la vârsta de:",
        "options": [
            "13–14 ani (nivel intelectual mediu+)",
            "6–8 ani",
            "18 ani (exclusiv adulți)",
            "25 ani (exclusiv populație activă)",
        ],
        "correct": "a",
    },
    {
        "stem": "FPI-R conține, în forma revizuită:",
        "options": [
            "138 itemi scorabili",
            "100 itemi (ca EPQ-R)",
            "63 itemi (ca IVE)",
            "480 itemi (ca MMPI)",
        ],
        "correct": "a",
    },
    {
        "stem": "Itemul de practică din FPI-R:",
        "options": [
            "nu este scorat",
            "determină invalidarea automată a profilului",
            "măsoară extraversiunea globală",
            "înlocuiește scala Sinceritate",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala Sat (Satisfacție față de viață) din FPI-R are, aproximativ:",
        "options": [
            "12 itemi",
            "14 itemi",
            "21 itemi",
            "32 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala Sinc (Sinceritate) din FPI-R are, aproximativ:",
        "options": [
            "14 itemi",
            "12 itemi",
            "10 itemi",
            "6 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Scalele globale Extrav (Extraversiune) și Emo (Emoționalitate) din FPI-R au, fiecare:",
        "options": [
            "14 itemi",
            "12 itemi",
            "21 itemi",
            "32 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "FPI-G (versiunea clasică) include, printre scalele de bază:",
        "options": [
            "Nervozitate, Agresivitate și Sociabilitate",
            "Sat, Real și Solic (scale FPI-R)",
            "Gi, Wb și Cm (scale CPI)",
            "P, E, N și L (scale EPQ)",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe Sat (Satisfacție față de viață) sugerează, orientativ:",
        "options": [
            "optimism și mulțumire față de viață",
            "pesimism și tendințe depresive",
            "agresivitate și dominare",
            "plângeri somatice accentuate",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe Inh (Inhibiție) indică, de regulă:",
        "options": [
            "timiditate și evitarea situațiilor sociale",
            "dezinhibiție și siguranță socială",
            "iritabilitate și impulsivitate",
            "competitivitate și ambiție",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe AcSom (Acuze somatice) reflectă:",
        "options": [
            "tendința de a raporta plângeri somatice",
            "optimism și satisfacție față de viață",
            "orientare prosocială accentuată",
            "sinceritate și deschidere în răspunsuri",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe PSan (Probleme de sănătate) este asociat, tipic, cu:",
        "options": [
            "teamă de boală și tendințe ipohondre",
            "relaxare și lipsă de solicitare",
            "dezinhibiție socială",
            "realizare profesională accentuată",
        ],
        "correct": "a",
    },
    {
        "stem": "Eșantionul normativ românesc pentru FPI include, orientativ:",
        "options": [
            "N = 2400–3161 persoane",
            "N = 408 bărbați din UK",
            "sub 200 participanți de conveniență",
            "exclusiv studenți la medicină",
        ],
        "correct": "a",
    },
    {
        "stem": "Alpha Cronbach pentru scalele FPI-R în România se situează, de regulă, între:",
        "options": [
            "0,67 și 0,84",
            "0,20 și 0,35",
            "0,95 și 0,99",
            "sub 0,40 (fidelitate inacceptabilă)",
        ],
        "correct": "a",
    },
    {
        "stem": "Corelațiile FPI-R cu CPI au raportat, în literatură, valori de ordinul:",
        "options": [
            "0,51–0,87 (mediană ~0,69)",
            "0,05–0,10 (neglijabile)",
            "0,98–1,00 (identitate perfectă)",
            "valori negative consistente",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi scor–descriere pentru Sat (Satisfacție față de viață) sunt corecte?",
        "options": [
            "Sat ↑ — optimist, mulțumit",
            "Sat ↓ — pesimist, depresiv",
            "Sat ↑ — agresiv, dominator",
            "Sat ↓ — orientare prosocială accentuată",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Soc (Orientare socială) sunt corecte?",
        "options": [
            "Soc ↑ — altruist, responsabil social",
            "Soc ↓ — individualist",
            "Soc ↑ — timid, evită contactul",
            "Soc ↓ — competitiv, ambițios",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Real (Orientare spre realizare) sunt corecte?",
        "options": [
            "Real ↑ — ambițios, competitiv",
            "Real ↓ — lipsă motivație pentru realizare",
            "Real ↑ — relaxat, fără solicitare",
            "Real ↓ — dominator, agresiv",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Exci (Excitabilitate) sunt corecte?",
        "options": [
            "Exci ↑ — iritabil, impulsiv",
            "Exci ↓ — autocontrol emoțional",
            "Exci ↑ — calm, stabil",
            "Exci ↓ — agresiv, dominator",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Agres (Agresivitate) sunt corecte?",
        "options": [
            "Agres ↑ — agresiv, dominator",
            "Agres ↓ — pasiv",
            "Agres ↑ — altruist, responsabil",
            "Agres ↓ — iritabil, impulsiv",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Solic (Solicitare/stres) sunt corecte?",
        "options": [
            "Solic ↑ — suprasolicitat, tensionat",
            "Solic ↓ — relaxat",
            "Solic ↑ — optimist, mulțumit",
            "Solic ↓ — teamă accentuată de boală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Extrav (Extraversiune) sunt corecte?",
        "options": [
            "Extrav ↑ — sociabil, activ",
            "Extrav ↓ — introvert, rezervat",
            "Extrav ↑ — anxios, instabil",
            "Extrav ↓ — agresiv, dominator",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Emo (Emoționalitate) sunt corecte?",
        "options": [
            "Emo ↑ — instabil, anxios",
            "Emo ↓ — stabil, optimist",
            "Emo ↑ — sociabil, activ",
            "Emo ↓ — iritabil, impulsiv",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scor–descriere pentru Sinc (Sinceritate) sunt corecte?",
        "options": [
            "Sinc ↑ — sincer, deschis",
            "Sinc ↓ — impresionare favorabilă / fake good",
            "Sinc ↑ — conformism social accentuat",
            "Sinc ↓ — validitate maximă garantată",
        ],
        "correct": "ab",
    },
    {
        "stem": "FPI-G include, pe lângă cele 9 scale de bază, și scalele compozite:",
        "options": [
            "Extraversiune (E)",
            "Nevrotism (N)",
            "Masculinitate (M)",
            "Satisfacție față de viață (Sat)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care scale FPI-R au câte 12 itemi, aproximativ?",
        "options": [
            "Sat, Soc, Real, Inh, Exci",
            "Agres, Solic, AcSom, PSan",
            "Sinc, Extrav și Emo",
            "Extraversiune (E) din FPI-G",
        ],
        "correct": "ab",
    },
    {
        "stem": "Despre utilizarea FPI în România, ce afirmații sunt corecte?",
        "options": [
            "peste 35 de ani de utilizare",
            "adaptări/norme asociate cu Pitariu, Ghițeanu, Mitrofan",
            "norme identice cu eșantionul german original, fără recalibrare",
            "fidelitate comparabilă cu datele din Germania",
        ],
        "correct": "ab",
    },
    {
        "stem": "Avantajele FPI-R includ, printre altele:",
        "options": [
            "structură multidimensională",
            "validitate de criteriu documentată",
            "profil rapid de interpretat",
            "necesitatea interpretării exclusiv intuitive, fără barem",
        ],
        "correct": "abc",
    },
    {
        "stem": "FPI-R este aplicabil în context:",
        "options": [
            "clinic și psihoterapeutic",
            "organizațional",
            "educațional și de consiliere",
            "exclusiv forensic, fără alte utilizări",
        ],
        "correct": "abc",
    },
    {
        "stem": "Despre fidelitatea FPI-R, ce afirmații sunt corecte?",
        "options": [
            "Alpha Cronbach 0,67–0,84 (RO, comparabil DE)",
            "test-retest stabil (ex. Inhibiție 0,84–0,85)",
            "fidelitate zero, invalidând testul",
            "consistență internă rezonabilă pentru majoritatea scalelor",
        ],
        "correct": "ab",
    },
    {
        "stem": "Despre validitatea FPI, ce afirmații sunt corecte?",
        "options": [
            "peste 1400 de referințe în literatură",
            "corelații cu CPI 0,51–0,87 (mediană ~0,69)",
            "validare peer-nomination: r = 0,51–0,87",
            "validitate convergentă cu inventare consacrate (ex. CPI)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care afirmații despre dependența scorurilor FPI de variabile demografice sunt corecte?",
        "options": [
            "scorurile depind semnificativ de vârstă",
            "tinerii obțin, de regulă, scoruri mai ridicate",
            "scorurile nu variază semnificativ după gen, educație sau reședință",
            "Emoționalitatea poate fi mai evidentă la femei",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care perechi scară–descriere pentru scoruri ridicate sunt corecte?",
        "options": [
            "Sat — optimist, mulțumit",
            "Soc — altruist, responsabil social",
            "Real — lipsă motivație realizare",
            "Inh — timid, evită social",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care perechi scară–descriere pentru scoruri scăzute sunt corecte?",
        "options": [
            "Agres — pasiv",
            "Solic — relaxat",
            "Exci — autocontrol",
            "PSan — teamă accentuată de boală",
        ],
        "correct": "abc",
    },
    {
        "stem": "Interpretarea profilului FPI presupune, de regulă:",
        "options": [
            "analiza intercorelațiilor dintre scale",
            "luarea în calcul a variabilelor demografice",
            "identificarea trăsăturilor dominante",
            "diagnosticarea automată a tulburărilor psihotice",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce elemente descriu corect FPI-R ca instrument?",
        "options": [
            "138 itemi scorabili + 1 item practică nescorat",
            "10 scale numerotate + Sinc + Extrav + Emo",
            "format Da/Nu (Adevărat/Fals)",
            "autori: Fahrenberg, Selg, Hampel (1970)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set rezumă corect psihometria FPI-R în România?",
        "options": [
            "N normativ 2400–3161",
            "α Cronbach 0,67–0,84",
            "test-retest stabil (ex. Inhibiție ~0,84–0,85)",
            "corelații CPI 0,51–0,87 (mediană ~0,69)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care domenii de aplicare sunt documentate pentru FPI?",
        "options": [
            "clinic",
            "psihoterapie",
            "organizațional",
            "educațional și consiliere",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care scale FPI-G (clasic) aparțin structurii originale?",
        "options": [
            "Nervozitate",
            "Depresie",
            "Dominare",
            "Satisfacție față de viață (Sat)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce pași orientează interpretarea profilului FPI (model cu 6 etape)?",
        "options": [
            "intercorelații între scale",
            "variabile demografice relevante",
            "trăsături dominante în profil",
            "tratarea fiecărui scor izolat, fără context",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care combinație sintetizează FPI-G și FPI-R?",
        "options": [
            "FPI-G: 9 scale + E, N, M; ~30–40 min",
            "FPI-R: revizuit, 138 itemi, ~10–30 min",
            "FPI-R: scale Sat–PSan + Sinc + Extrav + Emo",
            "FPI-G: format Likert pe 7 trepte",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce set descrie complet validitatea convergentă a FPI?",
        "options": [
            ">1400 referințe științifice",
            "corelații CPI 0,51–0,87",
            "peer-nomination r = 0,51–0,87",
            "validitate de criteriu inexistentă",
        ],
        "correct": "abc",
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


assert len(FPI_ITEMS) == 50
assert _count_dist(FPI_ITEMS) == {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}
