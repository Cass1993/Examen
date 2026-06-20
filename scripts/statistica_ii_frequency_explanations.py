"""Explicații didactice — Statistică II segment 3: analiza frecvențelor (ID 11051–11070)."""

from __future__ import annotations

from typing import List

FREQUENCY_EXPLANATIONS: List[str] = [
    # 11051
    (
        "Adevărat. fa numără aparițiile unei valori sau categorii — este cel mai "
        "elementar indicator din tabelele de frecvență. Nu exprimă proporție din "
        "total; pentru aceasta folosești frecvența relativă."
    ),
    # 11052
    (
        "fa = număr de cazuri cu acea valoare. Proporția fa/N este frecvența relativă, "
        "nu fa. fc este suma cumulată. Rangul percentil se referă la poziția unui scor, "
        "nu la numărul său de apariții."
    ),
    # 11053
    (
        "Frecvența relativă ca proporție este fa/N; în procente, (fa/N)×100. "
        "Înmulțirea fa×N nu are sens. Suma proporțiilor tuturor categoriilor este 1, "
        "dar formulele de bază sunt cele două de mai sus."
    ),
    # 11054
    (
        "fa=12, fr=12/80=0,15, adică 15%. Frecvența cumulată depinde de ordinea și de "
        "valorile anterioare din tabel — nu este mereu egală cu fa pentru o valoare "
        "intermediară."
    ),
    # 11055
    (
        "fc adună fa de la prima categorie până la cea curentă, în tabel ordonat. "
        "Proporția fa/N este fr, nu fc. Diferența fa−fr nu e un indicator standard. "
        "Numărul de clase ține de date grupate, nu de fc."
    ),
    # 11056
    (
        "Adevărat. Ultima linie a frecvenței cumulate include toate cazurile — deci "
        "fc final = N. Dacă nu ajunge la N, lipsește o categorie sau calculul cumulativ "
        "e greșit."
    ),
    # 11057
    (
        "Rangul percentil = % de valori ≤ scorul dat. Percentila este valoarea "
        "corespunzătoare unui procent (ex. P90). fa e un număr brut de apariții. "
        "Diferența față de medie nu definește rangul percentil."
    ),
    # 11058
    (
        "Rang percentil = poziție relativă a scorului tău în distribuție. Percentila = "
        "scorul care marchează un prag (ex. 90% sub P90). Nu sunt același tip de "
        "măsură — una descrie unde ești, cealaltă care e pragul."
    ),
    # 11059
    (
        "Q1 ≈ percentila 25, Q2 = mediana (percentila 50). Q1 și Q2 nu sunt la distanță "
        "fixă de medie în distribuții asimetrice. Q2 împarte datele la mijlocul "
        "ordinal."
    ),
    # 11060
    (
        "Q3 corespunde aproximativ percentila 75 — sfertul superior al datelor. Q1 e "
        "la 25%, nu Q3. Media și fa a maximului nu definesc quartilele."
    ),
    # 11061
    (
        "Pentru histograme/tabel grupat, 5–15 clase cu lățime egală e orientarea "
        "clasică — suficient detaliu fără zgomot excesiv. Câte o clasă per observație "
        "sau zeci de clase la N mic fragmentează inutil datele."
    ),
    # 11062
    (
        "Clase egale, fără goluri sau suprapuneri, fiecare valoare într-o singură "
        "clasă — altfel frecvențele nu mai sumează corect la N. Limitele aparente "
        "afișate diferă de cele reale tocmai pentru a respecta aceste reguli."
    ),
    # 11063
    (
        "Aparent 125–129 → real 124,5–129,5 (regula ±0,5). 129,5 intră în clasa "
        "următoare. Fără această convenție, valorile de la capete ar fi ambigue la "
        "date continue."
    ),
    # 11064
    (
        "Convenția standard: limite reale cu jumătăți de unitate — 124,5 și 129,5. "
        "125,0–129,0 ar exclude 129,5 sau ar crea suprapuneri. 124–130 sau 125,5–128,5 "
        "nu corespund intervalului aparent 125–129."
    ),
    # 11065
    (
        "Limitele reale clarifică încadrarea la capete, evită dubla numărare și permit "
        "gruparea corectă a datelor continue. N rămâne necesar pentru fr = fa/N."
    ),
    # 11066
    (
        "20/50 = 0,40 = 40%. 2,5 ar fi 20×50 (invers). fa rămâne 20, nu 50 — N este "
        "totalul, nu fa."
    ),
    # 11067
    (
        "Trei perechi corecte: fa, fr, fc. Rangul percentil nu este fa al maximului — "
        "e procentul de valori sub un scor."
    ),
    # 11068
    (
        "N = total observații — numitorul la fr. Numărul de categorii, modul sau lățimea "
        "clasei sunt alți parametri ai tabelului."
    ),
    # 11069
    (
        "Patru capcane frecvente: fa vs fr; fc fără ordine; intervale defecte; limite "
        "reale ignorate. Verificarea sumei proporțiilor (=1) și fc final (=N) ajută la "
        "control."
    ),
    # 11070
    (
        "Sinteză: indicatorii de frecvență, poziție relativă vs percentilă, quartile, "
        "reguli pentru date grupate. Acestea sunt baza descriptivă înainte de medie, "
        "dispersie și grafice."
    ),
]

assert len(FREQUENCY_EXPLANATIONS) == 20
