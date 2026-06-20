"""Itemi — Statistică II, segment 3: analiza frecvențelor (20 itemi, ID 11051–11070)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

FREQUENCY_ITEMS: List[Item] = [
    # —— 1–5: frecvență absolută, relativă ——
    {
        "stem": (
            "Frecvența absolută (fa) a unei valori sau categorii indică de câte ori "
            "aceasta apare în setul de date analizat."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În analiza frecvențelor, frecvența absolută (fa) reprezintă:"
        ),
        "options": [
            "numărul de cazuri în care apare o anumită valoare sau categorie",
            "proporția fa din totalul de observații (N)",
            "suma frecvențelor absolute până la o anumită valoare inclusiv",
            "procentul cazurilor a căror valoare este mai mică sau egală cu un scor dat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele formule sau relații despre frecvența relativă "
            "sunt corecte?"
        ),
        "options": [
            "frecvența relativă (ca proporție) = fa / N",
            "frecvența relativă procentuală = (fa / N) × 100",
            "frecvența relativă = fa × N",
            "suma tuturor frecvențelor relative (ca proporții) pentru toate categoriile "
            "distincte este 1 (sau 100%, dacă e exprimată procentual)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă într-un eșantion N = 80 apar 12 cazuri cu valoarea „2”, care "
            "afirmații despre această valoare sunt corecte?"
        ),
        "options": [
            "fa = 12",
            "frecvența relativă ca proporție este 12/80",
            "frecvența cumulată pentru „2” este 12, indiferent de celelalte valori din "
            "tabel",
            "frecvența relativă procentuală este 15%",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Frecvența cumulată (fc) a unei valori, într-un tabel ordonat crescător, "
            "reprezintă:"
        ),
        "options": [
            "suma frecvențelor absolute de la prima categorie până la categoria "
            "respectivă inclusiv",
            "proporția cazurilor care au exact acea valoare",
            "diferența dintre frecvența absolută și frecvența relativă",
            "numărul de clase folosite la gruparea datelor continue",
        ],
        "correct": "a",
    },
    # —— 6–10: percentila, quartile ——
    {
        "stem": (
            "Într-un tabel de frecvențe cumulate ordonat, ultima frecvență cumulată "
            "este egală cu N (totalul cazurilor)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Rangul percentil al unui scor indică:"
        ),
        "options": [
            "procentul de valori din eșantion care sunt mai mici sau egale cu acel scor",
            "valoarea numerică care împarte datele la un anumit procent fix",
            "frecvența absolută a scorului respectiv",
            "diferența dintre scor și medie, exprimată în procente",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între rang percentil și percentilă "
            "sunt corecte?"
        ),
        "options": [
            "rangul percentil descrie poziția relativă a unui scor în distribuție",
            "percentila este valoarea care corespunde unui anumit rang percentil",
            "rangul percentil și percentila sunt același tip de măsură, cu alt nume",
            "percentila 90 este scorul sub care se află aproximativ 90% din valori",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Despre primul și al doilea quartil (Q1 și Q2) al unei distribuții se "
            "poate afirma corect că:"
        ),
        "options": [
            "Q1 corespunde aproximativ rangului percentil 25",
            "Q2 coincide cu mediana distribuției",
            "Q1 și Q2 sunt întotdeauna la distanță egală de medie în orice distribuție",
            "Q2 marchează mijlocul ordinal al datelor (50%)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Al treilea quartil (Q3) al unei distribuții corespunde, în mod obișnuit, "
            "aproximativ:"
        ),
        "options": [
            "rangului percentil 75",
            "primului quartil (Q1)",
            "mediei aritmetice a tuturor valorilor",
            "frecvenței absolute a valorii maxime",
        ],
        "correct": "a",
    },
    # —— 11–15: frecvențe grupate, limite ——
    {
        "stem": (
            "La construirea unui tabel de frecvențe pentru date continue grupate, "
            "orientarea frecventă pentru numărul de clase este:"
        ),
        "options": [
            "în jur de 5–15 clase, cu intervale de lățime egală",
            "exact câte clase câte observații unice, indiferent de N",
            "cel mult 3 clase, pentru a păstra tabelele foarte simple",
            "peste 25 de clase, chiar și la eșantioane mici",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele cerințe pentru intervalele de clasă la frecvențe "
            "grupate sunt corecte?"
        ),
        "options": [
            "intervalele au, de regulă, aceeași lățime",
            "nu trebuie să existe goluri sau suprapuneri între intervale",
            "fiecare valoare se încadrează într-un singur interval",
            "limitele aparente și cele reale coincid mereu, fără ajustare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Pentru intervalul aparent 125–129 dintr-un tabel de frecvențe grupate, "
            "care afirmații sunt corecte?"
        ),
        "options": [
            "limitele reale sunt, de regulă, 124,5 și 129,5",
            "125 și 129 sunt limitele aparente afișate în tabel",
            "valoarea 129,5 aparține, de regulă, intervalului următor",
            "limitele reale coincid exact cu 125,0 și 129,0, fără corecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Intervalul de clasă aparent „125–129” are, în convenția obișnuită cu "
            "jumătăți de unitate, limitele reale:"
        ),
        "options": [
            "124,5 și 129,5",
            "125,0 și 129,0",
            "124,0 și 130,0",
            "125,5 și 128,5",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele motive justifică folosirea limitelor reale la "
            "frecvențele grupate?"
        ),
        "options": [
            "evită ambiguitatea la valorile de la capetele intervalelor",
            "previne numărarea aceleiași valori în două clase diferite",
            "permite încadrarea corectă a datelor continue în clase",
            "face inutilă cunoașterea numărului total N de cazuri",
        ],
        "correct": "abc",
    },
    # —— 16–20: capcane, sinteză ——
    {
        "stem": (
            "Dacă fa = 20 și N = 50, care dintre următoarele afirmații sunt corecte?"
        ),
        "options": [
            "frecvența relativă ca proporție este 0,40",
            "frecvența relativă procentuală este 40%",
            "frecvența relativă ca proporție este 2,5",
            "frecvența absolută este 50",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi indicator–definiție sunt corecte?"
        ),
        "options": [
            "fa — de câte ori apare o valoare sau categorie",
            "fr (proporție) — fa împărțit la N",
            "fc — suma frecvențelor absolute până la o anumită valoare (în tabel ordonat)",
            "rang percentil — frecvența absolută a valorii maxime",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În formula frecvenței relative fa / N, simbolul N reprezintă:"
        ),
        "options": [
            "numărul total de observații (cazuri) din eșantionul analizat",
            "numărul de categorii distincte din tabel",
            "frecvența celei mai frecvente valori",
            "lățimea unui interval de clasă la date grupate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele capcane în analiza frecvențelor sunt frecvente?"
        ),
        "options": [
            "confundarea frecvenței absolute cu cea relativă",
            "calcularea frecvenței cumulate fără ordonarea valorilor",
            "intervale de clasă cu goluri sau suprapuneri",
            "ignorarea regulii jumătăților de unitate la limitele reale",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect analiza frecvențelor studiate?"
        ),
        "options": [
            "fa, fr (proporție și procent), fc pentru distribuții ordonate",
            "rang percentil și percentilă — poziție relativă vs valoare-corespondentă",
            "quartile: Q1 ≈ 25%, Q2 = mediana, Q3 ≈ 75%",
            "date grupate: 5–15 clase egale, limite aparente vs reale (ex. 125–129)",
        ],
        "correct": "abcd",
    },
]

assert len(FREQUENCY_ITEMS) == 20
