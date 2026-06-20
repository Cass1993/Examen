"""Itemi — Statistică II, segment 6: dispersia (20 itemi, ID 11111–11130)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

DISPERSION_ITEMS: List[Item] = [
    # —— 1–5: amplitudine, abatere interquartilă ——
    {
        "stem": (
            "Amplitudinea (R) a unui set de date se calculează ca diferența dintre "
            "valoarea maximă și valoarea minimă: R = Xmax − Xmin."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Amplitudinea relativă (V%) exprimă amplitudinea în raport cu media și se "
            "calculează, de regulă, astfel:"
        ),
        "options": [
            "V% = (R / m) × 100",
            "V% = (m / R) × 100",
            "V% = R − m",
            "V% = (Q3 − Q1) / m × 100",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre amplitudinea R și amplitudinea "
            "relativă sunt corecte?"
        ),
        "options": [
            "R = Xmax − Xmin",
            "R este sensibilă la valorile extreme",
            "V% compară întinderea datelor cu nivelul mediei",
            "R este robustă la outlieri la fel ca abaterea interquartilică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Abaterea interquartilică (RQ) se calculează ca:"
        ),
        "options": [
            "RQ = Q3 − Q1",
            "RQ = (Q3 − Q1) / 2",
            "RQ = Xmax − Xmin",
            "RQ = Σ|Xi − m| / N",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Abaterea semiinterquartilică (RSQ) este jumătatea intervalului "
            "interquartilic: RSQ = (Q3 − Q1) / 2."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— 6–10: abatere medie, dispersie, abatere standard ——
    {
        "stem": (
            "Abaterea medie (d) măsoară dispersia folosind:"
        ),
        "options": [
            "media valorilor absolute ale abaterilor față de medie: Σ|Xi − m| / N",
            "suma pătratelor abaterilor împărțită la N − 1",
            "diferența dintre maxim și minim",
            "raportul dintre abaterea standard și medie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele indicatori de dispersie sunt descriși ca mai "
            "robusti la valori extreme?"
        ),
        "options": [
            "abaterea interquartilică (RQ = Q3 − Q1)",
            "abaterea semiinterquartilică (RSQ)",
            "amplitudinea R = Xmax − Xmin",
            "dispersia calculată cu pătratele abaterilor față de medie, fără modificare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru un eșantion, dispersia (varianța) s² se calculează, de regulă, cu "
            "numitorul:"
        ),
        "options": [
            "N − 1 (grade de libertate ale eșantionului)",
            "N (numărul total de cazuri)",
            "N + 1",
            "Q3 − Q1",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele relații între dispersie și abatere standard sunt "
            "corecte?"
        ),
        "options": [
            "abaterea standard a eșantionului s = √s²",
            "σ (sigma) desemnează, de regulă, abaterea standard a populației",
            "s și σ sunt întotdeauna identice, indiferent de eșantion sau populație",
            "s² este dispersia (varianța) eșantionului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Formula dispersiei eșantionului s² = Σ(Xi − m)² / (N − 1) folosește N − 1 "
            "pentru că:"
        ),
        "options": [
            "estimează mai bine dispersia populației din eșantion (corcție Bessel)",
            "media a consumat un grad de libertate în calculul abaterilor",
            "N − 1 este mereu egal cu Q3 − Q1",
            "altfel abaterea standard ar fi mereu zero",
        ],
        "correct": "ab",
    },
    # —— 11–15: proprietăți s, coeficient de variație ——
    {
        "stem": (
            "Care dintre următoarele proprietăți ale abaterii standard sunt corecte?"
        ),
        "options": [
            "dacă adaugi sau scazi aceeași constantă la toate valorile, s nu se schimbă",
            "dacă înmulțești toate valorile cu o constantă nenulă, s se înmulțește cu "
            "|constantă|",
            "dacă adaugi o constantă la toate valorile, s crește cu aceeași constantă",
            "abaterea standard reflectă răspândirea în aceleași unități ca și valorile "
            "originale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă la fiecare valoare dintr-un set adaugi aceeași constantă k, abaterea "
            "standard s:"
        ),
        "options": [
            "rămâne neschimbată",
            "crește cu k",
            "scade cu k",
            "se înmulțește cu k",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Coeficientul de variație (cv) se calculează ca:"
        ),
        "options": [
            "cv = (s / m) × 100",
            "cv = (m / s) × 100",
            "cv = s² / m",
            "cv = R × 100",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele interpretări ale coeficientului de variație (cv) "
            "sunt corecte?"
        ),
        "options": [
            "cv < 15% → dispersie mică, media este foarte reprezentativă",
            "cv între 15% și 30% → dispersie medie",
            "cv > 30% → dispersie mare, media este mai puțin reprezentativă",
            "cv > 30% → dispersie mică, datele sunt foarte omogene",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un coeficient de variație cv > 30% sugerează, în interpretarea uzuală, că:"
        ),
        "options": [
            "dispersia este mare și media aritmetică descrie mai slab „tipicul”",
            "datele sunt foarte omogene în jurul mediei",
            "abaterea interquartilică este mereu zero",
            "amplitudinea R nu poate fi calculată",
        ],
        "correct": "a",
    },
    # —— 16–20: alegerea indicatorului, sinteză ——
    {
        "stem": (
            "Când există outlieri marcanți, care dintre următoarele afirmații justifică "
            "preferarea RQ față de R?"
        ),
        "options": [
            "RQ = Q3 − Q1 se bazează pe quartile, mai puțin trase de extreme",
            "R = Xmax − Xmin include automat valorile extreme în calcul",
            "RQ este mereu egală cu abaterea standard s",
            "R devine imposibil de calculat în prezența outlierilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi indicator–formulă sunt corecte?"
        ),
        "options": [
            "R = Xmax − Xmin",
            "RQ = Q3 − Q1",
            "RSQ = (Q3 − Q1) / 2",
            "d = Σ(Xi − m)² / (N − 1)",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele capcane privind indicatorii de dispersie sunt "
            "frecvente?"
        ),
        "options": [
            "confundarea R cu RQ",
            "folosirea N în loc de N − 1 la varianța eșantionului",
            "presupunerea că adăugarea unei constante modifică abaterea standard",
            "interpretarea cv fără a ține cont de pragurile orientative (15%, 30%)",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect dispersia studiată?"
        ),
        "options": [
            "R, V%, RQ, RSQ, d, s², s — indicatori cu sensuri distincte",
            "s nu se schimbă la ± constantă; se scalează la ×/÷ constantă",
            "cv = (s/m)×100; praguri orientative 15% și 30%",
            "RQ și RSQ derivă din quartile, nu din min/max brut",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre dispersie și tendința centrală "
            "sunt corecte?"
        ),
        "options": [
            "indicatorii de dispersie completează măsurile de centru (medie, mediană)",
            "o medie reprezentativă are sens doar dacă știi cât de răspândite sunt datele",
            "coeficientul de variație permite compararea variabilității la scale diferite",
            "dispersia mare face inutilă orice descriere a datelor",
        ],
        "correct": "abc",
    },
]

assert len(DISPERSION_ITEMS) == 20
