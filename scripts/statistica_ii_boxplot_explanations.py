"""Explicații didactice — Statistică II segment 5: boxplot și outlieri (ID 11091–11110)."""

from __future__ import annotations

from typing import List

BOXPLOT_EXPLANATIONS: List[str] = [
    # 11091
    (
        "Adevărat. Cutia vizualizează intervalul interquartilic: de la Q1 la Q3 sunt "
        "50% din cazuri (centrul distribuției). Nu include automat outlierii — aceștia "
        "apar separat."
    ),
    # 11092
    (
        "Linia din cutie = mediana (Q2), nu media. Media ar fi atrasă de outlieri; "
        "boxplot-ul standard evidențiază mediana. Q1 e marginea inferioară a cutiei."
    ),
    # 11093
    (
        "Cutia = Q1–Q3 = nucleul central. Whiskers și puncte externe se calculează "
        "separat — cutia nu merge de la min la max."
    ),
    # 11094
    (
        "H sau IQR = Q3 − Q1 — lățimea cutiei. Nu e Q2−Q1, amplitudinea totală sau "
        "diferența medie–mediană. Din H derivă limitele whisker la 1,5×H."
    ),
    # 11095
    (
        "Adevărat. Regula 1,5×H (convenție Tukey) definește unde se termină whiskers "
        "și ce depășiri sunt marcate ca outlieri. E criteriu descriptiv, nu test "
        "inferențial."
    ),
    # 11096
    (
        "Punctele dincolo de whiskers = outlieri potrivit criteriului 1,5×H. Nu sunt "
        "automat erori — pot fi cazuri reale extreme. Nu confunda cu Q1 sau mediana."
    ),
    # 11097
    (
        "Trei elemente corecte: cutie Q1–Q3, linie mediană, whiskers până la ultima "
        "valoare non-outlier în limitele 1,5×H. Punctul extern nu e automat eroare de "
        "măsurare."
    ),
    # 11098
    (
        "Whiskers se opresc la valori non-outlier — de aceea nu ajung la min/max brut "
        "când există extreme. Punctele separate sunt outlieri. Sub Q1 nu e automat "
        "outlier — doar sub Q1−1,5H."
    ),
    # 11099
    (
        "Outlier = atipic față de compactul central, nu obligatoriu greșeală. Verifici "
        "sursa datelor înainte de eliminare. Nu e media și nu e Q1."
    ),
    # 11100
    (
        "H = Q3−Q1 baza limitei Q3+1,5H și Q1−1,5H. Whiskerul superior folosește "
        "această regulă sau ultima valoare validă sub limită. Nu marchează mereu "
        "min/max brut; Q2 ≠ H."
    ),
    # 11101
    (
        "Patru strategii din curs: eliminare justificată, corectare după verificare, "
        "medie trunchiată, transformări. Nu elimini tot ce e peste medie — mediana e "
        "deja robustă."
    ),
    # 11102
    (
        "Medie trunchiată 5%: tai ~5% din fiecare capăt, apoi calculezi media pe "
        "restul — compromis între robustețe și folosirea majorității datelor. Nu "
        "înseamnă media doar pe 5% centrale."
    ),
    # 11103
    (
        "log și √ comprimă cozile lungi — utile la venituri, timpi de reacție skewed. "
        "Nu aplici pe nominal și nu „înmulțești cu zero” — distruge datele."
    ),
    # 11104
    (
        "Verifică, documentează, păstrează outlieri reali dacă sunt relevanți. "
        "Analiza descriptivă rămâne posibilă — chiar boxplotul îi evidențiază."
    ),
    # 11105
    (
        "Eliminarea automată poate șterge cazuri reale (ex. performanță excepțională) "
        "și introduce bias. Nu garantează simetrie și nu confirmă invaliditatea datelor."
    ),
    # 11106
    (
        "Whiskers = ultima valoare non-outlier pe fiecare direcție, nu min/max brut "
        "când există puncte externe. Q1 și Q3 rămân marginile cutiei; mediana rămâne "
        "în interior."
    ),
    # 11107
    (
        "Transformări log/√ pentru asimetrie și valori pozitive pe scară de raport. "
        "Nu pentru nominal M/F. Pot reduce influența outlierilor pe scale skewed."
    ),
    # 11108
    (
        "Patru capcane frecvente la citire: linie ≠ medie; whiskers ≠ min/max; "
        "outlier ≠ automat eroare; cutia = doar 50% central, nu toată distribuția."
    ),
    # 11109
    (
        "Patru sinteze corecte: structură boxplot, regula 1,5×H, strategii de "
        "tratare, decizie contextuală. Boxplotul completează, nu înlocuiește analiza "
        "dispersiei."
    ),
    # 11110
    (
        "Boxplotul arată centrul compact și extremele. 1,5×H e convenție vizuală. "
        "Mediana e robustă — nu e calculată cu outlierii, dar îi poți vedea separat. "
        "Modul nu devine obligatoriu la orice outlier."
    ),
]

assert len(BOXPLOT_EXPLANATIONS) == 20
