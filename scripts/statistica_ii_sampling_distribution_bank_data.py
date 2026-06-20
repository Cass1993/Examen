"""Itemi — Statistică II, segment 9: distribuția de eșantionare și TLC (15 itemi, ID 11161–11175)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SAMPLING_DISTRIBUTION_ITEMS: List[Item] = [
    {
        "stem": (
            "În distribuția de eșantionare a mediilor, media teoretică a mediilor "
            "eșantioanelor (μm) este egală cu media populației (μ)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Distribuția de eșantionare a mediilor reprezintă:"
        ),
        "options": [
            "distribuția valorilor mediei pentru toate eșantioanele posibile de "
            "mărime N, extrase din populație",
            "distribuția valorilor individuale X dintr-un singur eșantion",
            "histograma frecvențelor dintr-un tabel nominal",
            "aceeași curbă ca distribuția populației, indiferent de mărimea N",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre distribuția de eșantionare a "
            "mediilor sunt corecte?"
        ),
        "options": [
            "μm = μ (media distribuției de eșantionare este media populației)",
            "dispersia mediilor eșantioanelor este mai mică decât dispersia populației",
            "dispersia mediilor eșantioanelor este mereu egală cu σ²",
            "media eșantionului unui singur extras este mereu egală cu μ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Eroarea standard a mediei (sm), când σ populației este cunoscută, se "
            "calculează:"
        ),
        "options": [
            "sm = σ / √N",
            "sm = σ × √N",
            "sm = σ / N",
            "sm = σ² / N",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Teorema limită centrală se referă, în principal, la distribuția:"
        ),
        "options": [
            "mediilor eșantioanelor de mărime N",
            "valorilor individuale X dintr-un singur caz",
            "modului populației",
            "erorii standard a fiecărui scor în parte",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Când abaterea standard a populației (σ) este necunoscută, eroarea standard "
            "a mediei se estimează cu:"
        ),
        "options": [
            "sm = s / √N (abaterea standard a eșantionului)",
            "sm = s × √N",
            "sm = σ / N",
            "sm = s² / (N − 1)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele relații între mărimea eșantionului (N) și eroarea "
            "standard a mediei (sm) sunt corecte?"
        ),
        "options": [
            "când N crește, sm scade",
            "un sm mai mic înseamnă o estimare mai precisă a mediei populației",
            "când N crește, sm crește proporțional cu N",
            "sm nu depinde de N dacă populația este normală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele condiții sunt importante pentru aplicarea teoremei "
            "limite centrale?"
        ),
        "options": [
            "eșantionare aleatoare",
            "observații independente între ele",
            "aceeași mărime a eșantionului N (în planul de eșantionare)",
            "populația trebuie să fie obligatoriu distribuită normal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Scorul z pentru media unui eșantion, în raport cu media populației, se "
            "calculează:"
        ),
        "options": [
            "z = (m − μ) / sm",
            "z = (m − μ) / σ",
            "z = (X − μ) / sm",
            "z = m / sm − μ",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele enunțuri despre teorema limită centrală sunt "
            "corecte?"
        ),
        "options": [
            "cu cât extragi mai multe eșantioane, media mediilor tinde spre μ",
            "distribuția mediilor eșantioanelor devine aproximativ normală la N mare",
            "populația trebuie neapărat normală pentru orice N mic",
            "TLC garantează că fiecare eșantion are media exact egală cu μ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Regula orientativă „eșantion mare” folosită frecvent în curs pentru aplicarea "
            "TLC este:"
        ),
        "options": [
            "N ≥ 30",
            "N < 5",
            "N = 1",
            "N ≥ σ²",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre TLC și forma populației sunt "
            "corecte?"
        ),
        "options": [
            "TLC se referă la distribuția mediilor eșantioanelor, nu la valorile individuale",
            "la N suficient de mare, forma populației poate fi non-normală",
            "curba normală a mediilor apare pentru că N este mare, nu pentru că X e normal",
            "dacă populația nu e normală, TLC nu se aplică niciodată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce creșterea lui N face estimarea mediei populației mai precisă?"
        ),
        "options": [
            "pentru că sm = σ/√N (sau s/√N) devine mai mic",
            "pentru că variabilitatea mediilor eșantioanelor scade",
            "pentru că σ populației devine zero",
            "pentru că μ se schimbă odată cu N",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele sinteze despre distribuția de eșantionare și TLC "
            "sunt corecte?"
        ),
        "options": [
            "distribuția mediilor: μm = μ; dispersia mediilor < dispersia populației",
            "sm = σ/√N sau s/√N; N ↑ → sm ↓",
            "TLC: mediile → normal la N mare; condiții: aleator, independent, același N",
            "z pentru media eșantionului: z = (m − μ) / sm",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele capcane privind distribuția de eșantionare și TLC "
            "sunt frecvente?"
        ),
        "options": [
            "confundarea σ cu sm în formula z",
            "folosirea TLC pentru valori individuale X în loc de medii",
            "presupunerea că un singur eșantion mic are mereu media = μ",
            "ignorarea faptului că N mare reduce sm, nu σ",
        ],
        "correct": "abc",
    },
]

assert len(SAMPLING_DISTRIBUTION_ITEMS) == 15
