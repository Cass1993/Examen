"""Itemi — Statistică II, segment 7: forma distribuției (20 itemi, ID 11131–11150)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

DISTRIBUTION_SHAPE_ITEMS: List[Item] = [
    # —— 1–5: asimetrie (skewness) ——
    {
        "stem": (
            "Un coeficient de asimetrie (skewness) egal cu 0 indică, în interpretarea "
            "standard, o distribuție simetrică."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În interpretarea uzuală a skewness-ului, valoarea 0 semnifică că "
            "distribuția este:"
        ),
        "options": [
            "simetrică (fără înclinare marcată spre stânga sau dreapta)",
            "cu asimetrie pozitivă și coadă lungă spre dreapta",
            "cu asimetrie negativă și coadă lungă spre stânga",
            "leptocurtică, cu vârf foarte înalt",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele descriu asimetria pozitivă (skewness > 0)?"
        ),
        "options": [
            "coadă mai lungă spre dreapta — valori mari rare care trag media",
            "ordinea tipică a indicatorilor centrali: Mo < Me < M",
            "coadă mai lungă spre stânga, cu media sub mediană",
            "skewness negativ, deoarece semnul plus indică deficitar la stânga",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un skewness negativ (sub 0) sugerează, de regulă:"
        ),
        "options": [
            "asimetrie cu coadă mai lungă spre stânga",
            "ordinea frecventă Mo > Me > M (mod peste mediană, medie mai jos)",
            "distribuție perfect simetrică",
            "aplatizare maximă, fără legătură cu înclinarea cozii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Distribuția leptocurtică se caracterizează printr-un vârf relativ înalt "
            "și valori concentrate în jurul centrului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— 6–10: kurtosis, alegere indicatori ——
    {
        "stem": (
            "O distribuție mezocurtică corespunde, în comparație cu modelul normal, "
            "unei curbe:"
        ),
        "options": [
            "cu aplatizare „normală” (de referință mesocurtică)",
            "extrem de aplatizate, cu valori foarte dispersate",
            "cu vârf foarte ascuțit și cozi grele",
            "fără niciun vârf, complet uniformă pe interval",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele perechi tip de kurtosis–descriere sunt corecte?"
        ),
        "options": [
            "leptocurtică — vârf înalt, valori concentrate",
            "mezocurtică — formă de referință (aproximativ normală)",
            "platicurtică — curbă aplatizată, valori mai dispersate",
            "platicurtică — valori strânse în jurul mediei, vârf ascuțit",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Distribuția platicurtică se distinge prin:"
        ),
        "options": [
            "curbă mai aplatizată, cu valori relativ mai dispersate",
            "vârf foarte înalt și concentrare puternică în centru",
            "skewness obligatoriu egal cu zero",
            "imposibilitatea calculului abaterii standard",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Pentru date pe scară nominală, indicatorul de tendință centrală fezabil "
            "în mod obișnuit este:"
        ),
        "options": [
            "modul",
            "media aritmetică",
            "mediana",
            "abaterea standard",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Când distribuția este marcat asimetrică, de ce se recomandă prudență cu "
            "media și abaterea standard?"
        ),
        "options": [
            "sunt trase de valori extreme și descriu mai slab centrul tipic",
            "abaterea standard reflectă și distanța outlierilor, nu doar răspândirea "
            "„tipică”",
            "mediana și RQ devin interzise prin definiție",
            "coeficientul de variație devine automat zero",
        ],
        "correct": "ab",
    },
    # —— 11–15: alegerea indicatorilor ——
    {
        "stem": (
            "Care dintre următoarele perechi de indicatori sunt potrivite la distribuții "
            "asimetrice cu outlieri?"
        ),
        "options": [
            "mediana pentru centru",
            "abaterea interquartilică (RQ) sau intervalul interquartilic pentru "
            "împrăștiere",
            "media + abaterea standard, fără verificarea formei",
            "modul + amplitudinea R, indiferent de scară",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Perechea cea mai frecvent folosită în practică pentru descrierea "
            "simultană a centrului și a dispersiei, când datele permit, este:"
        ),
        "options": [
            "media aritmetică + abaterea standard",
            "modul + amplitudinea relativă V%",
            "mediana + modul",
            "abaterea medie d + coeficientul de asimetrie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce media și abaterea standard sunt perechea uzuală la distribuții "
            "aproximativ simetrice?"
        ),
        "options": [
            "media e centru algebric, s măsoară răspândirea în aceleași unități",
            "ambele au proprietăți matematice care susțin multe analize ulterioare",
            "funcționează optim la orice scară nominală",
            "elimină nevoia de a inspecta forma distribuției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele reguli de alegere a indicatorilor după tipul "
            "datelor sau forma distribuției sunt corecte?"
        ),
        "options": [
            "nominal → modul",
            "asimetrică marcată → evită media și SD ca descriere principală",
            "uzual la date simetrice interval/raport → media + abaterea standard",
            "ordinal → obligatoriu media + s, indiferent de skewness",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Skewness pozitiv (+) și skewness negativ (−) se deosebesc prin direcția "
            "cozii mai lungi, nu prin:"
        ),
        "options": [
            "înălțimea vârfului sau gradul de aplatizare (kurtosis)",
            "poziția medianei față de mod și medie în asimetrie",
            "faptul că semnul skewness indică direcția cozii mai lungi",
            "legătura cu ordinea Mo, Me, M la asimetrie pozitivă sau negativă",
        ],
        "correct": "ab",
    },
    # —— 16–20: capcane, sinteză ——
    {
        "stem": (
            "Care dintre următoarele distincții între asimetrie și kurtosis sunt "
            "corecte?"
        ),
        "options": [
            "asimetria (skewness) descrie înclinarea / coada distribuției",
            "kurtosis descrie aplatizarea și concentrarea în jurul vârfului",
            "skewness și kurtosis sunt mereu identice ca semn și magnitudine",
            "o distribuție poate fi simetrică ca skewness și totuși leptocurtică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele capcane privind forma distribuției și alegerea "
            "indicatorilor sunt frecvente?"
        ),
        "options": [
            "raportarea mediei + s fără a verifica asimetria",
            "calcularea mediei la date nominale",
            "confundarea leptocurtic cu asimetrie pozitivă",
            "ignorarea faptului că la nominal doar modul are sens central",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect forma distribuției studiate?"
        ),
        "options": [
            "skewness: 0 = simetric; + = pozitiv; − = negativ",
            "kurtosis: leptocurtică / mezocurtică / platicurtică",
            "nominal → mod; asimetric → prudență cu media și SD; uzual media + s",
            "kurtosis înlocuiește complet analiza tendinței centrale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre indicatori și forma distribuției "
            "sunt corecte?"
        ),
        "options": [
            "indicatorii centrali și de dispersie trebuie aleși în funcție de scară "
            "și formă",
            "asimetria pozitivă justifică adesea mediana în locul mediei",
            "perechea media + s rămâne standard când distribuția e simetrică și "
            "scalele permit",
            "alegerea indicatorilor depinde de scară și formă, nu doar de skewness",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Într-o distribuție cu asimetrie negativă marcată, ordinea tipică a "
            "indicatorilor centrali este:"
        ),
        "options": [
            "M < Me < Mo (medie < mediană < mod)",
            "Mo < Me < M",
            "Mo = Me = M",
            "Me < Mo < M",
        ],
        "correct": "a",
    },
]

assert len(DISTRIBUTION_SHAPE_ITEMS) == 20
