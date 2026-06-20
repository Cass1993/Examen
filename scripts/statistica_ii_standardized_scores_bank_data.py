"""Itemi — Statistică II, segment 8: scoruri standardizate (10 itemi, ID 11151–11160)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

STANDARDIZED_SCORES_ITEMS: List[Item] = [
    {
        "stem": (
            "După transformarea în scor z, distribuția rezultată are, în mod teoretic, "
            "media 0 și abaterea standard 1."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Formula scorului z (standardizat) este:"
        ),
        "options": [
            "z = (X − m) / s",
            "z = (X + m) / s",
            "z = m / s + X",
            "z = (m − X) / s",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre scorul T sunt corecte?"
        ),
        "options": [
            "T = 50 + 10z",
            "distribuția T are media 50 și abaterea standard 10 (când z are media 0 și s = 1)",
            "T = 100 + 15z pentru orice test psihometric",
            "T se obține prin adunarea directă a lui X cu media eșantionului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Scorul z exprimă poziția unui rezultat X față de media m și abaterea "
            "standard s, măsurată în:"
        ),
        "options": [
            "număr de abateri standard (unități z)",
            "procente din intervalul interquartilic",
            "puncte brute identice cu X",
            "grade de libertate ale eșantionului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele perechi scor standardizat–parametri (medie, SD) "
            "sunt corecte?"
        ),
        "options": [
            "QI Binet: medie 100, SD 16 → QI = 100 + 16z",
            "QI Wechsler: medie 100, SD 15 → QI = 100 + 15z",
            "QI Wechsler: medie 50, SD 10 → QI = 50 + 10z",
            "SAT: medie 500, SD 100 → SAT = 500 + 100z",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Formula scorului SAT în raport cu z este:"
        ),
        "options": [
            "SAT = 500 + 100z",
            "SAT = 100 + 15z",
            "SAT = 50 + 14z",
            "SAT = 500 − 100z pentru orice variabilă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele transformări liniare din z sunt corecte?"
        ),
        "options": [
            "T = 50 + 10z",
            "H (Hull) = 50 + 14z",
            "QI Wechsler = 100 + 15z",
            "z = 50 + 10X, fără a folosi media și abaterea standard",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Scorul H (Hull) se transformă din z prin formula H = 50 + 14z, ceea ce "
            "înseamnă că are media și abaterea standard:"
        ),
        "options": [
            "media 50, SD 14",
            "media 100, SD 15",
            "media 0, SD 1",
            "media 50, SD 10",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "La variabile precum timpul de reacție, unde un scor mai mic este mai bun, "
            "transformarea în scor T folosește adesea:"
        ),
        "options": [
            "T = 50 − 10z (semn inversat față de variabilele „mai mare = mai bun”)",
            "mai întâi se calculează z = (X − m) / s, apoi se aplică transformarea T",
            "T = 50 + 10z, identic cu toate celelalte scale",
            "QI = 100 + 16z",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele sinteze despre scorurile standardizate derivate "
            "din z sunt corecte?"
        ),
        "options": [
            "z = (X−m)/s; media 0, SD 1",
            "T = 50 + 10z; H = 50 + 14z; QI Binet = 100 + 16z; QI Wechsler = 100 + 15z",
            "SAT = 500 + 100z",
            "la timp de reacție: T = 50 − 10z, deoarece valori mai mici sunt mai bune",
        ],
        "correct": "abcd",
    },
]

assert len(STANDARDIZED_SCORES_ITEMS) == 10
