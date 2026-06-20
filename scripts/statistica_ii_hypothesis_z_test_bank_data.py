"""Itemi — Statistică II, segment 10: ipoteze și testul z (10 itemi, ID 11176–11185)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

HYPOTHESIS_Z_TEST_ITEMS: List[Item] = [
    {
        "stem": (
            "Ipoteza nulă (H₀) afirmă, în mod obișnuit, că nu există diferență sau efect "
            "în populație (ex. μ₁ = μ₂ sau μ = o valoare de referință)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Ipoteza de cercetare (H₁) reprezintă:"
        ),
        "options": [
            "ipoteza care susține existența unei diferențe sau a unui efect",
            "ipoteza care afirmă că nu există nicio diferență",
            "nivelul de semnificație α al testului",
            "eroarea standard a mediei sm",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În exemplul clasic cu șahiștii (IQ mediu șahiști vs populație), care "
            "formulări sunt corecte?"
        ),
        "options": [
            "H₀: μșah = μpop (nu există diferență)",
            "H₁: μșah > μpop (șahiștii au IQ mediu mai mare)",
            "H₁: μșah = μpop",
            "H₀: μșah > μpop",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În testul z pentru un eșantion, primul pas după stabilirea ipotezelor este "
            "calculul erorii standard a mediei:"
        ),
        "options": [
            "sm = σ / √N",
            "sm = σ × √N",
            "z = (m − μ) / sm",
            "sm = (m − μ) / z",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Statistica z calculată pentru testul unui eșantion este:"
        ),
        "options": [
            "zcalculat = (m − μ) / sm",
            "zcalculat = (μ − m) / σ",
            "zcalculat = m / sm + μ",
            "zcalculat = sm / (m − μ)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele reguli de decizie la testarea ipotezelor sunt "
            "corecte?"
        ),
        "options": [
            "dacă p ≤ α, respingi H₀",
            "poți compara zcalculat cu zcritic (în funcție de tipul testului)",
            "dacă p > α, respingi H₀ pentru a limita riscul unei concluzii părtinitoare",
            "respingi H₀ automat ori de câte ori m ≠ μ în eșantion",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La α = 0,05 pentru un test unilateral dreapta, valoarea critică uzuală este "
            "zcritic = 1,65. Dacă zcalculat = 2,18, decizia este:"
        ),
        "options": [
            "respingi H₀ — rezultat semnificativ",
            "zcalculat ≥ zcritic, deci depășești pragul unilateral",
            "accepți H₀ pentru că m este aproape de μ",
            "nu respingi H₀ deoarece N = 30 este prea mic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În exemplul rezolvat al testului z (N = 30, m = 106, μ = 100, σ = 15), care "
            "pași intermediari sunt corecți?"
        ),
        "options": [
            "sm = 15 / √30 ≈ 2,74",
            "z = (106 − 100) / 2,74 ≈ 2,18",
            "p = 0,014 < 0,05 → respingi H₀",
            "sm = 15 × √30 → z = 0,5 → accepți H₀",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Când p > α și zcalculat nu depășește pragul critic (în testul ales), "
            "concluzia uzuală este:"
        ),
        "options": [
            "nu respingi H₀ — diferența nu e semnificativă la nivelul α",
            "accepți H₀ ca demonstrație că H₁ e falsă cu certitudine",
            "respingi H₀ pentru că eșantionul e prea mic",
            "demonstrezi că μ = m în populație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele sinteze despre ipoteze și testul z sunt corecte?"
        ),
        "options": [
            "H₀: fără diferență; H₁: există diferență/efect",
            "sm = σ/√N; zcalculat = (m−μ)/sm; compară cu zcritic sau p cu α",
            "α = 0,05 unilateral → zcritic ≈ 1,65; p ≤ α → respingi H₀",
            "dacă p > α, nu respingi H₀ (rezultat nonsignificativ)",
        ],
        "correct": "abcd",
    },
]

assert len(HYPOTHESIS_Z_TEST_ITEMS) == 10
