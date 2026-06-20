"""Explicații didactice — Statistică II segment 6: dispersia (ID 11111–11130)."""

from __future__ import annotations

from typing import List

DISPERSION_EXPLANATIONS: List[str] = [
    # 11111
    (
        "Adevărat. R = Xmax − Xmin măsoară întinderea totală. E simplă, dar un singur "
        "outlier o poate umfla enorm — de aceea există și indicatori bazați pe quartile."
    ),
    # 11112
    (
        "V% = (R/m)×100 pune amplitudinea în raport cu nivelul mediei — util la comparări "
        "relative. Nu inversa m/R și nu confunda cu RQ/m."
    ),
    # 11113
    (
        "R și sensibilitatea la extreme sunt corecte. V% e tot adevărat ca formulă, dar "
        "enunțul cere perechi despre R — nu include V% în răspuns. R nu e robustă ca RQ."
    ),
    # 11114
    (
        "RQ = Q3 − Q1 = IQR — lățimea cutiei din boxplot. RSQ e jumătate. d folosește "
        "module, nu pătrate. R e max − min."
    ),
    # 11115
    (
        "Adevărat. RSQ = (Q3−Q1)/2 — jumătatea distanței interquartilice. Nu e același "
        "lucru cu RQ, deși derivă din aceleași quartile."
    ),
    # 11116
    (
        "Abaterea medie d folosește valori absolute — mai puțin sensibilă la outlieri "
        "decât pătratele, dar mai puțin folosită decât s. s² folosește pătrate; cv = "
        "s/m."
    ),
    # 11117
    (
        "RQ și RSQ se bazează pe quartile — outlierii extreme nu le modifică direct ca "
        "pe R. Amplitudinea și varianța brută sunt trase de extreme."
    ),
    # 11118
    (
        "La eșantion, N−1 (grade de libertate) corectează estimarea varianței "
        "populației. Cu N la numitor subestimezi dispersia. Nu are legătură cu Q3−Q1."
    ),
    # 11119
    (
        "s = √s²; σ = abatere standard populație, s = eșantion. s² este varianța "
        "eșantionului. σ și s coincid doar dacă ai întreaga populație."
    ),
    # 11120
    (
        "N−1 corectează bias-ul estimatorului (Bessel) — media fixată consumă un grad "
        "de libertate. Nu face s zero și nu e legat de quartile."
    ),
    # 11121
    (
        "Translația ±k nu schimbă distanțele între valori → s constant. Scalarea ×c "
        "scalează și s cu |c|. s are aceleași unități ca X — de aceea e interpretabilă."
    ),
    # 11122
    (
        "Adunarea unei constante mută toate valorile egal — dispersia relativă între ele "
        "nu se schimbă. Media crește cu k, dar s rămâne aceeași."
    ),
    # 11123
    (
        "cv = (s/m)×100 — variabilitate relativă, util când compari grupuri cu medii "
        "diferite. Nu inversa și nu confunda cu V% (bazat pe R)."
    ),
    # 11124
    (
        "Praguri orientative din curs: sub 15% variabilitate mică; 15–30% medie; peste "
        "30% mare — media descrie mai slab tipicul. Peste 30% nu înseamnă omogenitate."
    ),
    # 11125
    (
        "cv > 30% = dispersie mare relativ la medie — interpreti media cu prudență. "
        "Nu înseamnă RQ=0 sau imposibilitatea calculului R."
    ),
    # 11126
    (
        "RQ ignoră min/max brut; R îi include pe ambele. De aceea la outlieri RQ e "
        "preferată descriptiv. Nu egalează s și nu înlocuiește media."
    ),
    # 11127
    (
        "Trei formule corecte: R, RQ, RSQ. d = Σ|Xi−m|/N, nu pătrate. Varianța folosește "
        "pătratele abaterilor."
    ),
    # 11128
    (
        "Patru capcane: R vs RQ; N vs N−1; s la translație; cv fără praguri. Verifică "
        "unitățile și tipul indicatorului (absolut vs relativ)."
    ),
    # 11129
    (
        "Patru sinteze: familia indicatorilor; proprietăți ale s; cv și praguri; "
        "originea quartilică a RQ/RSQ. σ populație ≠ s eșantion fără estimare."
    ),
    # 11130
    (
        "Centru + dispersie merg împreună: media fără s sau cv spune puțin. cv ajută la "
        "compararea grupurilor. Dispersia mare nu anulează descrierea — o califică."
    ),
]

assert len(DISPERSION_EXPLANATIONS) == 20
