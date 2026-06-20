"""Itemi — Inventare de personalitate II, seg. 5: comparații & recapitulare (30 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

COMPARATII_ITEMS: List[Item] = [
    {
        "stem": (
            "Psihoticismul (P) din EPQ echivalează direct cu un diagnostic "
            "psihiatric de psihoză."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Scorurile T ale NEO PI-R au media 50 și deviația standard 10."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Profilul CPI devine suspect dacă sunt lăsați necompletați peste "
            "30 de itemi."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "CPI (California Psychological Inventory) conține, în versiunile uzuale:",
        "options": [
            "260–434 itemi",
            "100 itemi (ca EPQ-R)",
            "240 itemi (ca NEO PI-R)",
            "138 itemi (ca FPI-R)",
        ],
        "correct": "a",
    },
    {
        "stem": "EPQ-R conține, în forma standard:",
        "options": [
            "100 itemi (P=32, E=23, N=24, L=21)",
            "240 itemi cu 30 fațete",
            "60 itemi (NEO-FFI)",
            "54–63 itemi (IVE)",
        ],
        "correct": "a",
    },
    {
        "stem": "Inventarul IVE conține, în funcție de versiune:",
        "options": [
            "54–63 itemi",
            "100 itemi",
            "260–434 itemi",
            "240 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "FPI-R conține, în forma revizuită:",
        "options": [
            "138 itemi scorabili",
            "100 itemi",
            "240 itemi",
            "60 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "NEO PI-R conține, în forma completă:",
        "options": [
            "240 itemi și 30 fațete (5 domenii × 6)",
            "100 itemi pe 4 scale",
            "138 itemi pe 10 scale numerotate",
            "20 scale standard + 13 speciale",
        ],
        "correct": "a",
    },
    {
        "stem": "Forma scurtă NEO-FFI conține:",
        "options": [
            "60 itemi",
            "240 itemi",
            "100 itemi",
            "24 itemi (EPQR-A)",
        ],
        "correct": "a",
    },
    {
        "stem": "Formatul de răspuns al CPI este, în mod clasic:",
        "options": [
            "Adevărat/Fals",
            "Likert (de acord total → dezacord total)",
            "Da/Nu nestandardizat",
            "răspuns liber narativ",
        ],
        "correct": "a",
    },
    {
        "stem": "Formatul de răspuns al NEO PI-R este, de regulă:",
        "options": [
            "Likert (de acord total → dezacord total)",
            "Adevărat/Fals (ca CPI)",
            "Da/Nu (ca EPQ)",
            "alegere multiplă cu o singură variantă corectă",
        ],
        "correct": "a",
    },
    {
        "stem": "Protocolul NEO PI-R devine invalid dacă sunt lăsați necompletați cel puțin:",
        "options": [
            "41 itemi (din 240)",
            "30 itemi (ca la CPI)",
            "5 itemi",
            "100 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Intervalul T 40–60 la NEO PI-R acoperă, orientativ:",
        "options": [
            "~68% din populație (nivel mediu)",
            "~2,3% din populație (extrem)",
            "~95% din populație",
            "sub 10% din populație",
        ],
        "correct": "a",
    },
    {
        "stem": "Scalele Gi, Wb și Cm aparțin inventarului:",
        "options": [
            "CPI (validitate profil)",
            "EPQ-R (scale P, E, N, L)",
            "NEO PI-R (itemi A, B, C)",
            "IVE (Impulsivitate, Aventură, Empatie)",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi inventar–scală de validitate/falsificare sunt corecte?",
        "options": [
            "EPQ-R — L (Lie / Minciună)",
            "CPI — Gi (Good impression / fake good)",
            "FPI-R — Sinc (Sinceritate)",
            "IVE — P (Psihoticism clinic)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi inventar–format de răspuns sunt corecte?",
        "options": [
            "CPI — Adevărat/Fals",
            "EPQ-R — Da/Nu (Adevărat/Fals)",
            "NEO PI-R — Likert",
            "NEO PI-R — Da/Nu (ca EPQ)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care perechi trăsătură–descriere sunt corecte?",
        "options": [
            "P (EPQ) — agresivitate, antisocial (nu diagnostic psihiatric direct)",
            "N / Nevrotism — stabilitate emoțională (invers: N↑ = instabilitate)",
            "C (NEO) — predictor puternic al performanței la job",
            "O (NEO) — predictor #1 al performanței la job (peste C)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care perechi inventar–utilizator calificat sunt corecte?",
        "options": [
            "CPI — Level B (master psihologie)",
            "NEO PI-R — Clasă B (master + training)",
            "EPQ-R — utilizator calificat (psiholog etc.)",
            "CPI — Level A (orice utilizator fără pregătire)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi inventar–populație țintă sunt corecte?",
        "options": [
            "CPI — persoane normale, 12–70 ani",
            "FPI-R — de la 13–14 ani (nivel intelectual mediu+)",
            "NEO PI-R — persoane normale (PI-3: de la 12 ani)",
            "EPQ-R — exclusiv copii sub 6 ani",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi inventar–eșantion normativ românesc sunt corecte?",
        "options": [
            "EPQ-R — N ≈ 2400–3741",
            "FPI-R — N ≈ 2400–3161",
            "NEO PI-R — N = 2200 (reprezentativ pe gen)",
            "CPI — N = 2200 (norme NEO)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi inventar–fidelitate (Alpha Cronbach) sunt corecte?",
        "options": [
            "CPI — α ≈ 0,50–0,80",
            "EPQ-R — α > 0,70 (majoritatea scalelor)",
            "FPI-R — α ≈ 0,67–0,84 (RO, comparabil DE)",
            "NEO PI-R — α ≈ 0,20–0,35 (inacceptabil)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care inventare folosesc format Da/Nu sau Adevărat/Fals (nu Likert)?",
        "options": [
            "EPQ-R",
            "IVE",
            "CPI",
            "NEO PI-R",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce măsoară scalele de validitate / falsificare din diferite inventare?",
        "options": [
            "L (EPQ) — conformism social / fake good",
            "Gi (CPI) — impresionare favorabilă exagerată",
            "Sinc (FPI-R) — sinceritate vs. impresionare favorabilă",
            "P (EPQ) — validitate protocolului (minciună socială)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre Conștiinciozitate (C) și Deschidere (O) sunt corecte?",
        "options": [
            "C (NEO) — predictor #1 performanță job și succes academic",
            "O (NEO) — creativitate, gândire divergentă",
            "C (NEO) — creativitate și nonconformism",
            "O (NEO) — stabilitate emoțională (invers nevrotism)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care numere-cheie despre structura inventarelor sunt corecte?",
        "options": [
            "CPI — 20 scale standard + 13 speciale; 4 tipuri cuboid",
            "EPQ-R — 100 itemi: P32/E23/N24/L21",
            "FPI-R — 138 itemi; 10 scale + Extrav + Emo",
            "NEO PI-R — 60 itemi (forma completă)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care criterii de invalidare a protocolului sunt corect asociați?",
        "options": [
            "CPI — >30 itemi necompletați",
            "NEO PI-R — ≥41 itemi necompletați",
            "NEO PI-R — >150 acord/acord total (acquiescence)",
            "EPQ-R — invalidare automată la orice 1 item necompletat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce set rezumă psihometria NEO PI-R în România?",
        "options": [
            "5 factori explică ~53% din varianță",
            "congruență cross-culturală ~0,98 (N, E)",
            "norme N = 2200; T: M=50, SD=10",
            "invalidare la >30 itemi necompletați (ca CPI)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care elemente descriu corect comparația CPI vs NEO PI-R?",
        "options": [
            "CPI: 260–434 itemi, A/F, 20+13 scale, Level B",
            "NEO: 240 itemi, Likert, 5 domenii × 6 fațete, Clasă B",
            "CPI: Gi/Wb/Cm validitate; NEO: itemi A,B,C + reguli protocol",
            "NEO: format A/F; CPI: format Likert",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care perechi inventar–factori/domenii principali sunt corecte?",
        "options": [
            "EPQ-R — P, E, N, L",
            "IVE — Impulsivitate, Aventură, Empatie",
            "FPI-R — Sat–PSan + Sinc + Extrav + Emo",
            "CPI — 20 scale standard + tipuri cuboid (Alpha/Beta/Gamma/Delta)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set sintetizează numerele-cheie de memorat pentru grilă?",
        "options": [
            "CPI: 20+13 scale; invalidare >30; α 0,50–0,80",
            "EPQ-R: 100 itemi; RO N≈2400–3741; α >0,70",
            "FPI-R: 138 itemi; RO N≈2400–3161; α 0,67–0,84",
            "NEO: 240 itemi, 30 fațete; FFI 60; norme 2200; invalidare ≥41; T M=50 SD=10; 68% T40–60",
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


assert len(COMPARATII_ITEMS) == 30
assert _count_dist(COMPARATII_ITEMS) == {"1": 11, "2": 7, "3": 6, "4": 3, "TF": 3}
