"""Itemi — Statistică II, segment 12: ANOVA (20 itemi, ID 11226–11245)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ANOVA_ITEMS: List[Item] = [
    {
        "stem": (
            "În ANOVA unifactorială, ipoteza nulă (H₀) afirmă că mediile tuturor "
            "grupurilor comparate sunt egale în populație."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Analiza varianței (ANOVA) este folosită în principal pentru:"
        ),
        "options": [
            "compararea mediilor a trei sau mai multe grupuri sau condiții",
            "estimarea coeficientului de corelație Pearson între două variabile continue",
            "descrierea frecvențelor și procentelor pe categorii nominale",
            "compararea a exact două medii independente (în locul testului t)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care formulări ale ipotezelor într-o ANOVA unifactorială cu k grupuri "
            "sunt corecte?"
        ),
        "options": [
            "H₀: μ₁ = μ₂ = … = μₖ",
            "H₁: cel puțin o medie de grup diferă de celelalte",
            "H₁: toate mediile sunt obligatoriu diferite între ele",
            "H₀: varianta dintre grupuri este zero și varianta în grupuri este infinită",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Statistica F în ANOVA unifactorială este, în esență, raportul dintre:"
        ),
        "options": [
            "varianța (sau media pătratelor) între grupuri și varianța în grupuri",
            "media generală și abaterea standard a eșantionului",
            "suma pătratelor totale și numărul de grupuri k",
            "coeficientul de corelație și valoarea p",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele presupuneri sunt verificate înainte de interpretarea "
            "ANOVA parametrice?"
        ),
        "options": [
            "observațiile sunt independente",
            "varianțele grupurilor sunt aproximativ egale (omogenitate)",
            "variabila dependentă este aproximativ normal distribuită în fiecare grup",
            "fiecare grup trebuie să aibă exact aceeași medie înainte de test",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce nu se recomandă, de regulă, să aplici mai multe teste t independente "
            "pentru toate perechile de grupuri în loc de ANOVA?"
        ),
        "options": [
            "crește riscul erorii de tip I (respingere falsă a lui H₀)",
            "reduce probabilitatea unei semnificări false la fiecare pereche testată",
            "testul t nu poate fi calculat niciodată când există peste două grupuri",
            "ANOVA elimină complet necesitatea oricărei verificări a presupunerilor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă ANOVA unifactorială este semnificativă (p ≤ α), știi automat care "
            "pereche exactă de grupuri diferă cel mai mult, fără teste post-hoc."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care relații despre descompunerea varianței în ANOVA unifactorială sunt "
            "corecte?"
        ),
        "options": [
            "SS₍total₎ = SS₍între₎ + SS₍în₎",
            "variația totală se partitionează în componenta explicată de grup și "
            "componenta reziduală în grupuri",
            "SS₍între₎ măsoară exclusiv erorile de măsurare ale instrumentului",
            "SS₍în₎ reflectă variabilitatea dintre participanți din același grup",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "După un rezultat semnificativ la ANOVA unifactorială, pasul următor uzual "
            "pentru a identifica diferențele între perechi de medii este:"
        ),
        "options": [
            "teste post-hoc (ex. Tukey, Bonferroni)",
            "repetarea ANOVA pe fiecare pereche fără ajustare",
            "calculul mediei generale și oprirea analizei",
            "acceptarea automată că toate grupurile diferă între ele",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care distincții între ANOVA unifactorială între subiecți și ANOVA cu "
            "măsurători repetate sunt corecte?"
        ),
        "options": [
            "între subiecți: participanți diferiți în fiecare grup",
            "măsurători repetate: aceiași participanți în toate condițiile",
            "alegerea modelului depinde de modul în care sunt repartizați participanții",
            "între subiecți: aceiași persoane apar în toate nivelurile factorului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "La ANOVA unifactorială cu k grupuri și N participanți în total, gradele "
            "de libertate uzual asociate sunt:"
        ),
        "options": [
            "între grupuri: df = k − 1",
            "în grupuri (eroare): df = N − k",
            "total: df = N + k",
            "între grupuri: df = N − 1",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Eta pătrat (η²) într-o ANOVA unifactorială indică, în linii mari:"
        ),
        "options": [
            "proporția din varianța VD explicată de factorul independent",
            "mărimea efectului — cât din variabilitate e asociată grupului",
            "probabilitatea ca H₀ să fie adevărată",
            "diferența exactă în puncte brute între media celui mai mare și cel mai mic "
            "grup",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În care condiții este adecvată ANOVA unifactorială parametrică?"
        ),
        "options": [
            "VD pe scară de interval sau raport (măsură cantitativă)",
            "cel puțin trei grupuri sau condiții de comparat",
            "presupunerile de normalitate, independență și omogenitate a varianțelor "
            "sunt acceptabile",
            "VD nominală cu două categorii exclusive",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un design între subiecți (between-subjects) în contextul ANOVA "
            "înseamnă că:"
        ),
        "options": [
            "fiecare participant este reprezentat într-un singur grup al VI",
            "compararea mediilor se face pe grupuri independente de participanți",
            "aceiași participanți trec prin toate nivelurile manipulării",
            "nu există variabilitate în interiorul grupurilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Când există exact două grupuri independente, relația dintre F și t este:"
        ),
        "options": [
            "F = t² (pătratul valorii t)",
            "F = t / 2",
            "F și t nu pot fi niciodată legate",
            "F = √t",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele sinteze despre ANOVA unifactorială sunt corecte?"
        ),
        "options": [
            "test omnibus: verifică dacă există diferențe între medii, nu care pereche",
            "H₀: toate mediile egale; H₁: cel puțin una diferă",
            "F mare → varianță între grupuri mare relativ la varianța în grupuri",
            "η² estimează proporția varianței VD explicate de factorul independent",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care limitări ale interpretării unui rezultat semnificativ la ANOVA sunt "
            "formulate corect?"
        ),
        "options": [
            "nu spune singură care perechi de grupuri diferă",
            "semnificarea statistică nu echivalează automat cu un efect practic mare",
            "un F nonsignificativ demonstrează cu certitudine că mediile sunt egale",
            "mărimea efectului (ex. η²) ajută la evaluarea relevanței practicii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un psiholog compară scorurile de anxietate la trei tipuri de terapie "
            "(A, B, C). Variabila independentă are:"
        ),
        "options": [
            "3 niveluri (tip terapie)",
            "o singură categorie nominală fără grupuri",
            "2 niveluri obligatorii în orice ANOVA",
            "0 niveluri, pentru că VD e cantitativă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă obții F = 4,82, p = 0,003 la α = 0,05 într-o ANOVA unifactorială, "
            "care interpretări sunt corecte?"
        ),
        "options": [
            "respingi H₀ — există dovezi că nu toate mediile sunt egale",
            "p < α → rezultat semnificativ statistic",
            "poți concluziona direct că fiecare grup diferă de toate celelalte",
            "urmează adesea analiza post-hoc pentru perechi de grupuri",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care dintre următoarele idei despre ANOVA unifactorială sunt formulate "
            "corect?"
        ),
        "options": [
            "compară 3+ medii; la 2 grupuri independente se poate folosi testul t",
            "SS total = SS între + SS în; F = MS între / MS în",
            "presupune independență, omogenitatea varianțelor și normalitate aproximativă",
            "după F semnificativ, testele post-hoc clarifică diferențele între perechi",
        ],
        "correct": "abcd",
    },
]

assert len(ANOVA_ITEMS) == 20
