"""Itemi — Psihologia personalității II: SOCIAL-COGNITIVĂ (20 itemi, ID 12166–12185)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SOCIAL_COGNITIVA_ITEMS: List[Item] = [
    {
        "stem": (
            "Mischel (1973) consideră abordarea social-cognitivă "
            "idiografică — centrul e pe individualitate, nu pe legi generale exclusive."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Rotter (1954): același nivel de expectanță (E) cu valențe (V) "
            "diferite produce același comportament."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Situația psihologică (Mischel) presupune că:",
        "options": [
            "comportamentul depinde de contextul perceput, nu de obiectiv în sine",
            "comportamentul e determinat de trăsături stabile, indiferent de context",
            "realitatea e mediu subiectiv — cadru de referință intern (Rogers/Kelly)",
            "consecința după comportament determină probabilitatea repetării (Skinner)",
        ],
        "correct": "a",
    },
    {
        "stem": "Encodările/reprezentările (Mischel, variabila 1) se referă la:",
        "options": [
            "modul unic de interpretare a stimulilor (același câine = companion vs pericol)",
            "probabilitatea subiectivă de a obține un rezultat (Rotter E)",
            "cât de mult îți dorești alternativa comportamentală (Rotter V)",
            "planuri mentale și autoevaluare flexibilă (autoreglare)",
        ],
        "correct": "a",
    },
    {
        "stem": "Expectanțele la Mischel (variabila 2) pot fi:",
        "options": [
            "specifice (situație concretă) sau generalizate (LCI/LCE; autoeficacitate)",
            "fixe, moștenite biologic, fără influență a experienței",
            "echivalentul răspunsului condiționat la stimulus condiționat (Pavlov)",
            "identice cu trăsăturile cardinale care domină personalitatea (Allport)",
        ],
        "correct": "a",
    },
    {
        "stem": "Emoțiile, la Mischel (variabila 3), presupun că:",
        "options": [
            "«emoția urmează gândului»; hot cognitions despre sine/viitor",
            "emoția e reflex necondiționat anterior oricărei cogniții",
            "emoția e determinată de libido fixată în stadii psihosexuale",
            "emoția e independentă de reprezentările cognitive ale situației",
        ],
        "correct": "a",
    },
    {
        "stem": "Potențialul comportamental (Rotter, 1954) se exprimă ca:",
        "options": [
            "PC = f(E × V) — expectanță × valență",
            "PC = f(E + V) — suma liniară, fără interacțiune",
            "PC = f(SNc + SN) — asociere stimulus–răspuns (Pavlov)",
            "PC = tendința actualizantă spre autoactualizare (Rogers)",
        ],
        "correct": "a",
    },
    {
        "stem": "Expectanța E (Rotter) reprezintă:",
        "options": [
            "credința subiectivă despre cât de probabil obții rezultatul",
            "cât de mult îți dorești alternativa comportamentală (valența)",
            "modul de interpretare a stimulilor (encodare Mischel)",
            "scorul direct măsurat pe scale de trăsături (dispozițional)",
        ],
        "correct": "a",
    },
    {
        "stem": "Valența V (Rotter) reprezintă:",
        "options": [
            "cât de mult îți dorești alternativa / rezultatul comportamentului",
            "probabilitatea subiectivă de succes (expectanța E)",
            "locus of control intern vs extern (expectanță generalizată)",
            "capacitatea de a asimila evenimente noi în construct (Kelly)",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi expectanță–tip (Rotter/Mischel) sunt corecte?",
        "options": [
            "Specifică — legată de situația concretă",
            "Generalizată — locus of control intern/extern (LCI/LCE)",
            "Generalizată — valența alternativei dorite",
            "Specifică — autoeficacitate ca trăsătură cardinală Allport",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi autor–concept sunt corecte?",
        "options": [
            "Rotter — locus of control intern (LCI) vs extern (LCE)",
            "Bandura — autoeficacitate (expectanță generalizată)",
            "Rotter — autoeficacitate ca postulat fundamental",
            "Bandura — PC = f(E × V) ca formulă centrală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi variabilă Mischel–descriere sunt corecte?",
        "options": [
            "Scopuri și valori — direcție, motivație",
            "Competențe de autoreglare — planuri mentale, nișă socială",
            "Encodări — probabilitate subiectivă E × V (Rotter)",
            "Emoții — reflex necondiționat anterior cogniției",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care enunțuri despre interacțiunea E × V (Rotter) sunt corecte?",
        "options": [
            "Comportamentul se prezice din interacțiunea E × V, nu din E sau V singur",
            "Aceeași E + valențe diferite → comportamente diferite",
            "Aceeași V + expectanțe identice → comportament identic indiferent de context",
            "Valența V e redundantă dacă expectanța E e suficient de mare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi enunț–autor (social-cognitiv) sunt corecte?",
        "options": [
            "Mischel (1973) — 5 variabile-persoană",
            "Rotter (1954) — potențial comportamental PC = f(E × V)",
            "Mischel — condiționare clasică SN → SC",
            "Rotter — autoactualizare ca tendință actualizantă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care enunțuri despre cele 5 variabile-persoană (Mischel) sunt corecte?",
        "options": [
            "Encodări — interpretare unică a stimulilor",
            "Expectanțe — specifice vs generalizate (LCI/LCE, autoeficacitate)",
            "Emoții — «emoția urmează gândului»; hot cognitions",
            "Expectanțe — echivalentul SNc + SN repetat (Pavlov)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre situația psihologică și metodă (Mischel) sunt corecte?",
        "options": [
            "Comportamentul depinde de contextul perceput",
            "Abordare idiografică — individualitatea centrală",
            "100 lei ≠ același sens pentru șomer vs milionar",
            "Abordare nomotetică — legi generale, caz individual secundar",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre modelul Rotter sunt corecte?",
        "options": [
            "E = expectanță subiectivă (specifică sau generalizată)",
            "V = valență — cât de mult îți dorești alternativa",
            "PC = f(E × V) — interacțiune, nu variabile izolate",
            "PC = f(E) — valența e irelevantă dacă E e ridicată",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre autoreglare și scopuri (Mischel) sunt corecte?",
        "options": [
            "Scopuri și valori — direcție, motivație",
            "Competențe de autoreglare — planuri mentale, autoevaluare flexibilă",
            "Nișă socială — parte a competențelor de autoreglare",
            "Scopuri — echivalentul pedepsei imediate post-comportament (Skinner)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri integrează Mischel și Rotter (social-cognitiv)?",
        "options": [
            "Mischel: 5 variabile-persoană; situație psihologică; idiografic",
            "Rotter: PC = f(E × V); E subiectivă; V = valență",
            "Expectanțe generalizate: LCI/LCE (Rotter) și autoeficacitate (Bandura)",
            "100 lei — același obiectiv, sens diferit în contextul perceput",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set sintetizează abordarea social-cognitivă?",
        "options": [
            "Mischel (1973): encodări, expectanțe, emoții, scopuri, autoreglare; idiografic",
            "Situația psihologică: comportamentul depinde de contextul perceput",
            "Rotter (1954): PC = f(E × V); E specific/generalizat; V = valență",
            "Expectanțe generalizate: LCI/LCE (Rotter) + autoeficacitate (Bandura)",
        ],
        "correct": "abcd",
    },
]


def _count_dist(rows: List[Item]) -> Dict[str, int]:
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


SEG_DIST_20 = {"1": 7, "2": 5, "3": 4, "4": 2, "TF": 2}

assert len(SOCIAL_COGNITIVA_ITEMS) == 20
assert _count_dist(SOCIAL_COGNITIVA_ITEMS) == SEG_DIST_20
