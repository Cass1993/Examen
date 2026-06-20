"""Explicații didactice — Statistică II segment 4: tendința centrală (ID 11071–11090)."""

from __future__ import annotations

from typing import List

CENTRAL_TENDENCY_EXPLANATIONS: List[str] = [
    # 11071
    (
        "Adevărat. Mediana depinde de poziția în distribuție, nu de magnitudinea "
        "fiecărei valori — outlierii o trag mult mai puțin decât pe medie. De aceea "
        "la venituri sau timpi de reacție cu valori rare foarte mari, mediana e adesea "
        "mai informativă."
    ),
    # 11072
    (
        "Mo = valoarea cea mai frecventă. Mediana împarte la 50% ca număr de cazuri. "
        "Media = ΣX/N. Amplitudinea = max − min — indicator de dispersie, nu de centru."
    ),
    # 11073
    (
        "Modul se citește direct din frecvențe și funcționează la nominal (ex. categoria "
        "cea mai des întâlnită). Nu e stabil la extreme și nu e baza inferenței "
        "parametrice — rolul acela revine mediei."
    ),
    # 11074
    (
        "Modul poate sări de la o valoare la alta sau să devină bimodal. În inferență "
        "parametrică se lucrează cu medii, nu cu moduri. La nominal, modul rămâne "
        "util descriptiv."
    ),
    # 11075
    (
        "Adevărat. m = ΣX/N — definiția standard. Toate valorile intră în calcul cu "
        "ponderea lor, spre deosebire de mediană (poziție) sau mod (frecvență maximă)."
    ),
    # 11076
    (
        "Mediana = valoarea centrală ordonată (sau media celor două centrale la N par). "
        "50% sub, 50% deasupra — în sensul numărului de cazuri. Nu e Mo și nu e media "
        "aritmetică."
    ),
    # 11077
    (
        "Media e omniprezentă în practică și în teste parametrice (t, ANOVA), are "
        "proprietăți algebrice utile, dar outlierii o distorsionează. Egalitatea cu "
        "modul apare doar aproximativ la simetrie."
    ),
    # 11078
    (
        "Mediana rezistă la extreme și se poate estima cu ultima clasă deschisă (nu "
        "ai nevoie de capătul exact). Nu reflectă media ponderată — e un prag ordinal "
        "la 50%."
    ),
    # 11079
    (
        "Coada dreaptă cu valori mari rare ridică media peste „centrul” vizual al "
        "datelor. Mediana rămâne aproape de zona unde se află majoritatea cazurilor. "
        "Σ(X−m)=0 rămâne valabil oricum."
    ),
    # 11080
    (
        "Translația liniară: X+k → m+k. Aceasta e proprietatea 1 din listă. Nu se "
        "înmulțește cu k la adunare și nu devine automat mediana."
    ),
    # 11081
    (
        "Trei proprietăți clasice: scalarea (×c), suma abaterilor zero, minimul "
        "pătratelor abaterilor. Suma abaterilor simple nu e maximă la medie — e zero."
    ),
    # 11082
    (
        "Minimul lui Σ(X−a)² se atinge la a = m. Mediana minimizează alt tip de "
        "abateri (suma valorilor absolute), nu pe cele pătratice."
    ),
    # 11083
    (
        "Cele trei ordini din curs: simetric Mo≈Me≈M; pozitiv Mo<Me<M (coadă dreapta "
        "trage media); negativ M<Me<Mo. Ultima variantă inversează greșit asimetria "
        "pozitivă."
    ),
    # 11084
    (
        "Proprietăți liniare: translație ±k și scalare ×c se propagă identic la medie. "
        "Modul și mediana au reguli similare la translație, dar nu „doar modul” la "
        "înmulțire."
    ),
    # 11085
    (
        "Asimetrie pozitivă = coadă dreapta = valori mari rare → media e trasă la "
        "dreapta, peste mediană, peste mod. Ordinea Mo < Me < M e regula mnemotechnică "
        "din curs."
    ),
    # 11086
    (
        "Indiferent de direcția asimetriei, mediana stă între mod și medie — de "
        "exemplu la pozitiv Mo < Me < M, Me e la mijloc. Nu e mereu sub ambele sau "
        "peste ambele."
    ),
    # 11087
    (
        "Nominal → mod. Asimetrie → mediană. Inferență parametrică → medie (cu "
        "presupunerile îndeplinite). Modul nu înlocuiește media în testele clasice."
    ),
    # 11088
    (
        "La asimetrie marcată, mediana descrie „tipicul” mai bine decât media trasă "
        "de coadă. Media folosește toate valorile — tocmai asta o face vulnerabilă. "
        "Modul poate fi departe de centru în distribuții continue."
    ),
    # 11089
    (
        "Patru capcane: medie la asimetrie/outlieri; confuzie Me/Mo; simetrie "
        "presupusă peste tot; medie pe coduri nominale. Alegerea indicatorului urmează "
        "tipul scalei și forma distribuției."
    ),
    # 11090
    (
        "Sinteză completă: definiții Mo/Me/m, proprietăți ale mediei, ordinea la "
        "simetrie și asimetrie, rolul medianei între mod și medie. Baza pentru "
        "compararea distribuțiilor și pentru alegerea statisticilor ulterioare."
    ),
]

assert len(CENTRAL_TENDENCY_EXPLANATIONS) == 20
