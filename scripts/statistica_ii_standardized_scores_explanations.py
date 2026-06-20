"""Explicații didactice — Statistică II segment 8: scoruri standardizate (ID 11151–11160)."""

from __future__ import annotations

from typing import List

STANDARDIZED_SCORES_EXPLANATIONS: List[str] = [
    # 11151
    (
        "Adevărat. z = (X−m)/s centrează la 0 și scalează la SD 1 — baza tuturor "
        "celorlalte scoruri liniare. Fără acest pas, T, QI și SAT nu sunt comparabile."
    ),
    # 11152
    (
        "z = (X−m)/s — câte abateri standard ești de la medie. Semnul arată direcția "
        "(sub/peste medie). Nu aduni m la X în numărător și nu inversezi m−X decât "
        "când variabila e codificată invers intenționat."
    ),
    # 11153
    (
        "T = 50 + 10z: media 50, SD 10. E transformare liniară din z. Nu e QI Wechsler "
        "(100, 15) și nu se calculează din X fără standardizare."
    ),
    # 11154
    (
        "z măsoară distanța față de medie în unități de abatere standard — de aceea "
        "poți compara poziții relative pe teste diferite. Nu e procent IQR sau scor brut."
    ),
    # 11155
    (
        "Trei perechi corecte: Binet 100/16, Wechsler 100/15. SAT are item separat — nu "
        "face parte din acest enunț cu două răspunsuri. Wechsler nu are media 50."
    ),
    # 11156
    (
        "SAT = 500 + 100z — centru 500, pas de 100 per abatere standard z. Nu e formula "
        "QI și minusul la SAT nu e regula generală — excepția e timpul de reacție la T."
    ),
    # 11157
    (
        "Trei transformări liniare valide din z. z = 50 + 10X omit standardizarea cu m și "
        "s — greșeală de procedură."
    ),
    # 11158
    (
        "Hull: H = 50 + 14z → medie 50, SD 14. Diferit de T (SD 10) și de QI (medie 100). "
        "z rămâne 0/1 înainte de transformare."
    ),
    # 11159
    (
        "Mai întâi z din X, apoi T = 50 − 10z pentru timp de reacție — astfel performanța "
        "mai rapidă (z mic sau negativ) dă T mai mare. Nu folosești QI sau T = 50 + 10z."
    ),
    # 11160
    (
        "Patru sinteze din tabel: z de bază; familiile T/H/QI; SAT; excepția timpului "
        "de reacție. Toate sunt transformări liniare din z, cu medie și SD fixate."
    ),
]

assert len(STANDARDIZED_SCORES_EXPLANATIONS) == 10
