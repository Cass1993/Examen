"""Itemi — Epigenetica II: PATOLOGII GENETICE (30 itemi, ID 11776–11805)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PATOLOGII_GENETICE_ITEMS: List[Item] = [
    {
        "stem": (
            "Sindromul Down este cauzat de trisomia cromozomului 21 "
            "(prezența a trei copii ale cromozomului 21)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Sindromul Turner este asociat, de regulă, cu monosomia X "
            "(cariotip 45,X)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Sindromul Klinefelter corespunde cariotipului 47,XYY "
            "(trisomia cromozomului Y)."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Cauza numerică (aneuploidie) a sindromului Down este:",
        "options": [
            "trisomia cromozomului 21",
            "monosomia cromozomului 21",
            "trisomia cromozomului 18",
            "deleția brațului lung al cromozomului 21",
        ],
        "correct": "a",
    },
    {
        "stem": "Sindromul Turner este cauzat de:",
        "options": [
            "monosomia cromozomului X (45,X)",
            "trisomia XXY",
            "trisomia cromozomului 21",
            "deleția cromozomului Y",
        ],
        "correct": "a",
    },
    {
        "stem": "Sindromul Klinefelter este asociat cariotipului:",
        "options": [
            "47,XXY",
            "45,X",
            "47,+21",
            "47,XYY",
        ],
        "correct": "a",
    },
    {
        "stem": "Aneuploidia se referă la:",
        "options": [
            "număr anormal de cromozomi (față de diploidul așteptat)",
            "schimbarea ordinii bazelor azotate într-un singur codon",
            "prezența a două linii celulare cu același cariotip",
            "repetarea unei secvențe ADN pe același cromozom",
        ],
        "correct": "a",
    },
    {
        "stem": "Mozaicismul cromozomial presupune:",
        "options": [
            "coexistența a două sau mai multe linii celulare cu cariotipuri diferite",
            "pierderea completă a unui cromozom autosomal la toate celulele",
            "transferul unei secvențe ADN pe un cromozom nehomolog",
            "prezența a trei copii ale aceluiași cromozom autosomal în fiecare celulă",
        ],
        "correct": "a",
    },
    {
        "stem": "Deleția cromozomială/structurală reprezintă:",
        "options": [
            "pierderea unui segment de ADN din cromozom",
            "repetarea unei secvențe ADN în cadrul aceluiași cromozom",
            "număr total de 47 de cromozomi în celulele somatice",
            "prezența a două linii celulare cu proporții diferite de trisomie",
        ],
        "correct": "a",
    },
    {
        "stem": "Duplicația structurală a ADN-ului înseamnă:",
        "options": [
            "repetarea (copierea suplimentară) unei secvențe de ADN",
            "pierderea parțială a unui braț cromozomial",
            "schimbul de segmente între cromozomi nehomologi",
            "absența unui cromozom sexual într-o celulă diploidă",
        ],
        "correct": "a",
    },
    {
        "stem": "Translocația cromozomială constă în:",
        "options": [
            "mutarea unei secvențe de ADN de pe un cromozom pe altul",
            "pierderea completă a cromozomului 21",
            "prezența a trei copii ale cromozomului X",
            "replicarea fidelă a genomului fără rearanjări",
        ],
        "correct": "a",
    },
    {
        "stem": "Trisomia 21 (47,+21) indică:",
        "options": [
            "trei copii ale cromozomului 21 într-o celulă care, altfel, ar fi diploidă",
            "două copii ale cromozomului 21 și lipsa cromozomului X",
            "pierderea unui segment din cromozomul 21",
            "transferul cromozomului 21 pe cromozomul 14 fără câștig numeric",
        ],
        "correct": "a",
    },
    {
        "stem": "Cariotipul 45,X este caracteristic pentru:",
        "options": [
            "sindromul Turner",
            "sindromul Klinefelter",
            "sindromul Down",
            "sindromul Patau (trisomia 13)",
        ],
        "correct": "a",
    },
    {
        "stem": "Care patologie aparține categoriei structurale (nu numerice)?",
        "options": [
            "translocația Robertsoniană 14/21",
            "trisomia 21 liberă",
            "monosomia X",
            "cariotipul 47,XXY",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi afecțiune–cauză (aneuploidie) sunt corecte?",
        "options": [
            "Sindrom Down — trisomie 21",
            "Sindrom Turner — monosomie X",
            "Sindrom Klinefelter — monosomie X",
            "Sindrom Down — monosomie 21",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre sindromul Down sunt corecte?",
        "options": [
            "este o aneuploidie (trisomie autosomală)",
            "cariotip frecvent: 47,+21",
            "rezultă din pierderea unui segment al cromozomului 21",
            "două copii ale cromozomului 21 (disomie normală)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre sindromul Turner sunt corecte?",
        "options": [
            "cariotip tipic: 45,X",
            "aparține aneuploidiilor legate de cromozomii sexuali",
            "corespunde trisomiei XXY",
            "presupune două cromozomi X funcționali (46,XX)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre sindromul Klinefelter sunt corecte?",
        "options": [
            "cariotip: 47,XXY",
            "aparține aneuploidiilor sexuale",
            "echivalent cu sindromul Turner",
            "apare la indivizi cu cariotip 45,X",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre trisomie și monosomie sunt corecte?",
        "options": [
            "trisomia presupune o copie în plus a unui cromozom",
            "monosomia presupune o copie în minus a unui cromozom",
            "ambele sunt, prin definiție, patologii structurale ale ADN-ului",
            "deleția unui segment este sinonimă cu trisomia acelui cromozom",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre mozaicism sunt corecte?",
        "options": [
            "există cel puțin două linii celulare cu cariotipuri diferite",
            "proporția fiecărei linii poate varia între țesuturi",
            "este identic cu trisomia completă la toate celulele",
            "se observă același cariotip în absolut toate celulele",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre translocație sunt corecte?",
        "options": [
            "segment de ADN se fixează pe un cromozom neoriginal",
            "poate apărea translocație Robertsoniană (ex. 14/21)",
            "este, prin definiție, monosomia cromozomului X",
            "apare la toți purtătorii ca trisomie 21 completă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi tip aberrant–definiție sunt corecte?",
        "options": [
            "Deleție — pierdere de segment ADN",
            "Duplicație — repetarea unei secvențe",
            "Translocație — mutarea secvenței între cromozomi",
            "Aneuploidie — repetarea unei secvențe pe același cromozom",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre aneuploidie sunt corecte?",
        "options": [
            "număr anormal de cromozomi față de diploidul așteptat",
            "trisomia = o copie în plus a unui cromozom",
            "monosomia = o copie în minus a unui cromozom",
            "include, ca exemplu principal, deleția unui braț cromozomial",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care patologii sunt de tip structural al ADN-ului?",
        "options": [
            "deleție",
            "duplicație",
            "translocație",
            "monosomie X (45,X)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care cariotipuri corespund corect afecțiunilor enumerate?",
        "options": [
            "47,+21 — sindrom Down",
            "45,X — sindrom Turner",
            "47,XXY — sindrom Klinefelter",
            "47,XXY — sindrom Turner",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații compară corect patologiile numerice vs structurale?",
        "options": [
            "aneuploidia = patologie numerică (ex. trisomie, monosomie)",
            "deleția = patologie structurală (pierdere segment)",
            "translocația = rearanjare între cromozomi",
            "trisomia 21 este, prin definiție, o deleție a cromozomului 21",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri descrie corect cele trei sindromuri cromozomiale numerice?",
        "options": [
            "Down — trisomie 21 (47,+21)",
            "Turner — monosomie X (45,X)",
            "Klinefelter — XXY (47,XXY)",
            "Klinefelter — monosomie X (45,X)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce set leagă corect conceptele de patologie genetică?",
        "options": [
            "Aneuploidie: număr anormal de cromozomi (trisomie/monosomie)",
            "Down — trisomie 21; Turner — monosomie X; Klinefelter — XXY",
            "Mozaicism: linii celulare cu cariotipuri diferite",
            "Deleție: pierdere de segment ADN (patologie structurală)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set sintetizează patologiile cromozomiale numerice?",
        "options": [
            "Sindrom Down — trisomie 21",
            "Sindrom Turner — monosomie X (45,X)",
            "Sindrom Klinefelter — 47,XXY",
            "Trisomia = copie în plus; monosomia = copie în minus",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set integrează patologiile numerice, structurale și mozaicismul?",
        "options": [
            "Aneuploidie: număr anormal (ex. 47,+21 sau 45,X)",
            "Structural: deleție, duplicație, translocație",
            "Mozaicism: populații celulare cu cariotipuri diferite",
            "Duplicație: repetarea unei secvențe de ADN",
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


SEG_DIST_30 = {"1": 11, "2": 7, "3": 6, "4": 3, "TF": 3}

assert len(PATOLOGII_GENETICE_ITEMS) == 30
assert _count_dist(PATOLOGII_GENETICE_ITEMS) == SEG_DIST_30
