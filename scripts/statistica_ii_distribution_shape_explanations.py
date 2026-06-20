"""Explicații didactice — Statistică II segment 7: forma distribuției (ID 11131–11150)."""

from __future__ import annotations

from typing import List

DISTRIBUTION_SHAPE_EXPLANATIONS: List[str] = [
    # 11131
    (
        "Adevărat. Skewness = 0 indică simetrie (în sens statistic). Nu spune nimic "
        "despre kurtosis — o curbă poate fi simetrică și leptocurtică sau platicurtică."
    ),
    # 11132
    (
        "Zero = simetric. Plus = coadă dreapta (asimetrie pozitivă). Minus = coadă "
        "stânga. Leptocurtic ține de kurtosis, nu de skewness."
    ),
    # 11133
    (
        "Pozitiv: coadă dreapta, valori mari rare trag media → Mo < Me < M. Coada "
        "stângă și „skew negativ” la semn plus sunt erori — plus = pozitiv = dreapta."
    ),
    # 11134
    (
        "Skewness negativ = coadă stânga, adesea M < Me < Mo. Nu e simetric și nu "
        "descrie aplatizarea (kurtosis)."
    ),
    # 11135
    (
        "Adevărat. Leptocurtic = vârf înalt, valori concentrate. Opusul e platicurtic "
        "(aplatizat). Mezocurtic = referință normală."
    ),
    # 11136
    (
        "Mezocurtică = curba „normală” de referință. Platicurtică = aplatizată, "
        "dispersată. Leptocurtică = vârf ascuțit — nu e mezocurtică."
    ),
    # 11137
    (
        "Trei tipuri: lepto (concentrat), mezo (normal), plati (aplatizat). Ultima "
        "variantă inversează platicurtic cu leptocurtic — capcană frecventă."
    ),
    # 11138
    (
        "Platicurtică = aplatizare, valori mai împrăștiate. Nu are vârf înalt. "
        "Skewness poate fi oricare. s se calculează în continuare."
    ),
    # 11139
    (
        "La nominal nu are sens medie sau mediană ca „centru” al codurilor — doar "
        "modul (categoria cea mai frecventă). SD pe coduri e lipsit de sens."
    ),
    # 11140
    (
        "Media și s sunt sensibile la extreme — la asimetrie descriu slab centrul. "
        "s include și distanța outlierilor. Mediana și RQ rămân valide, nu interzise."
    ),
    # 11141
    (
        "La asimetrie/outlieri: mediana + RQ (sau IQR). Evită perechea medie + s ca "
        "descriere principală. Modul nu rezolvă singur problema scalei."
    ),
    # 11142
    (
        "Cea mai uzuală pereche descriptivă: media + abaterea standard — când "
        "scalele și forma distribuției o permit. Nu mod + V% sau doar skewness."
    ),
    # 11143
    (
        "La simetrie, media e centru algebric, s e dispersie în aceleași unități — "
        "baza inferenței parametrice. Nu funcționează pe nominal și nu elimină "
        "verificarea formei."
    ),
    # 11144
    (
        "Trei reguli din curs: nominal → mod; asimetrie → prudență cu media și s; "
        "interval/raport simetric → media + s. Ordinal nu obligă media + s oricum."
    ),
    # 11145
    (
        "Skewness ≠ kurtosis: semnul și ordinea Mo–Me–M țin de asimetrie; vârful "
        "aplatizat ține de kurtosis. Ambele pot coexista independent."
    ),
    # 11146
    (
        "Asimetria = înclinare/coadă; kurtosis = aplatizare/concentrare. Pot fi "
        "simetrică (skew 0) și totuși leptocurtică. Nu sunt mereu egale ca semn."
    ),
    # 11147
    (
        "Patru capcane: medie + s fără verificare; medie pe nominal; confundare "
        "lepto cu skew pozitiv; ignorarea modului la nominal."
    ),
    # 11148
    (
        "Trei sinteze corecte din schemă. Kurtosis nu înlocuiește centrul și "
        "dispersia — le completează ca „formă”."
    ),
    # 11149
    (
        "Patru afirmații: alegere contextuală; mediană la pozitiv; media + s la "
        "simetrie; scară + formă contează. Skewness 0 nu garantează singur "
        "reprezentativitatea — pot exista outlieri simetrici sau kurtosis extrem."
    ),
    # 11150
    (
        "Negativ: M < Me < Mo — coadă stânga trage media în jos. Pozitiv: Mo < Me < M. "
        "Simetric: Mo ≈ Me ≈ M."
    ),
]

assert len(DISTRIBUTION_SHAPE_EXPLANATIONS) == 20
