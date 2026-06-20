"""Itemi — Statistică II, segment 5: boxplot și valori extreme (20 itemi, ID 11091–11110)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

BOXPLOT_ITEMS: List[Item] = [
    # —— 1–5: structura boxplotului ——
    {
        "stem": (
            "Într-un boxplot, „cutia” (box) se întinde de la primul quartil (Q1) la "
            "al treilea quartil (Q3) și cuprinde 50% central al datelor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În boxplot, linia trasată în interiorul cutiei reprezintă, de regulă:"
        ),
        "options": [
            "mediana (a doua quartilă, Q2)",
            "media aritmetică a tuturor valorilor",
            "primul quartil (Q1)",
            "valoarea maximă observată în eșantion",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele descrieri ale cutiei din boxplot sunt corecte?"
        ),
        "options": [
            "delimitează intervalul dintre Q1 și Q3",
            "conține 50% central al observațiilor (intervalul interquartilic vizual)",
            "se întinde întotdeauna de la valoarea minimă la cea maximă",
            "are lățimea egală cu amplitudinea totale a datelor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Intervalul interquartilic (IQR), notat uneori H în formula whiskerilor, "
            "se calculează ca:"
        ),
        "options": [
            "H = Q3 − Q1",
            "H = Q2 − Q1",
            "H = maxim − minim",
            "H = medie − mediana",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În convenția tipică a boxplotului, lungimea whiskerilor se stabilește "
            "folosind multiplul 1,5 × H, unde H = Q3 − Q1."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— 6–10: whiskers, outlieri ——
    {
        "stem": (
            "Valorile care depășesc capetele whiskerilor (în afara intervalului "
            "Q1 − 1,5H și Q3 + 1,5H) sunt marcate, de regulă, ca:"
        ),
        "options": [
            "outlieri (valori extreme)",
            "mediana distribuției",
            "limitele reale ale intervalului de clasă",
            "valorile centrale obligatorii ale cutiei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele elemente ale unui boxplot sunt descrise corect?"
        ),
        "options": [
            "cutia: de la Q1 la Q3",
            "linia din cutie: mediana",
            "whiskers: se extind până la ultima valoare non-outlier, în limitele "
            "1,5×H față de quartile",
            "fiecare punct din afara cutiei este automat o eroare de măsurare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre whiskers și outlieri sunt "
            "corecte?"
        ),
        "options": [
            "whiskers nu ajung neapărat până la minimul sau maximul brut al datelor "
            "dacă există outlieri",
            "punctele afișate dincolo de whiskers sunt valori extreme potrivit "
            "criteriului 1,5×H",
            "orice valoare sub Q1 este marcată automat ca outlier",
            "outlierii sunt întotdeauna erori de înregistrare care trebuie șterse",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În interpretarea unui boxplot, o valoare marcată individual dincolo de "
            "whisker indică:"
        ),
        "options": [
            "o observație atipică față de compactul central al distribuției",
            "obligatoriu o greșeală de tastare care trebuie eliminată",
            "media aritmetică a grupului",
            "limita inferioară a intervalului interquartilic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele relații între quartile și whiskers sunt corecte?"
        ),
        "options": [
            "H = Q3 − Q1 este baza pentru calculul limitelor whisker la 1,5×H",
            "limita superioară a whiskerului este, în convenția clasică, Q3 + 1,5H "
            "(sau ultima valoare non-outlier sub această limită)",
            "whiskers marchează întotdeauna exact minimul și maximul eșantionului",
            "Q2 este egal cu Q3 − Q1",
        ],
        "correct": "ab",
    },
    # —— 11–15: tratarea outlierilor ——
    {
        "stem": (
            "Care dintre următoarele strategii de tratare a valorilor extreme sunt "
            "discutate în analiza descriptivă?"
        ),
        "options": [
            "eliminarea cazurilor extreme (cu justificare metodologică)",
            "corectarea valorilor suspecte după verificare",
            "folosirea mediei trunchiate (ex. 5% la fiecare capăt)",
            "ignorarea automată a oricărei valori deasupra mediei",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Mediana trunchiată sau medie trunchiată la 5% înseamnă, în linii mari, "
            "că:"
        ),
        "options": [
            "se elimină o proporție mică din valorile extreme de la fiecare capăt "
            "înainte de calculul mediei",
            "se păstrează toate valorile, inclusiv outlierii, fără modificare",
            "se înlocuiesc toate valorile cu mediana",
            "se calculează media doar pe cele 5% centrale ale datelor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele transformări sunt folosite uneori pentru a reduce "
            "efectul valorilor extreme sau a asimetriei?"
        ),
        "options": [
            "transformarea logaritmică (log)",
            "transformarea radical (ex. √x)",
            "înmulțirea tuturor valorilor cu zero",
            "rotunjirea tuturor valorilor la aceeași cifră",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele precauții la tratarea outlierilor sunt corecte?"
        ),
        "options": [
            "nu elimini automat — verifică dacă sunt erori sau cazuri reale",
            "documentează decizia (eliminare, corectare, transformare)",
            "outlierii pot purta informație relevantă pentru întrebarea de cercetare",
            "prezența outlierilor face imposibilă orice analiză descriptivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce eliminarea automată a tuturor valorilor marcate ca outlier pe "
            "boxplot poate fi problematică?"
        ),
        "options": [
            "pentru că unele valori extreme pot fi reale și semnificative, nu erori",
            "pentru că poate introduce bias și reduce reprezentativitatea eșantionului",
            "pentru că outlierii confirmă întotdeauna că datele sunt invalide",
            "pentru că eliminarea lor garantează o distribuție perfect simetrică",
        ],
        "correct": "a",
    },
    # —— 16–20: interpretare, sinteză ——
    {
        "stem": (
            "Când există outlieri, whiskers pe boxplot:"
        ),
        "options": [
            "se opresc adesea la ultima valoare non-outlier din fiecare direcție",
            "ajung obligatoriu până la minimul și maximul brut, indiferent de outlieri",
            "nu se mai pot calcula, deoarece Q1 și Q3 devin egale",
            "înlocuiesc mediana din interiorul cutiei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele situații justifică, cu prudență, o transformare "
            "(log sau √) a datelor?"
        ),
        "options": [
            "distribuție puternic asimetrică cu coadă lungă",
            "valori strict pozitive pe o scară de raport (ex. timpi, venituri)",
            "date nominale codificate M/F",
            "dorința de a micșora efectul outlierilor pe variabile skewed",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care dintre următoarele capcane la citirea sau folosirea boxplotului sunt "
            "frecvente?"
        ),
        "options": [
            "confundarea liniei din cutie cu media",
            "presupunerea că whiskers = minim și maxim brut",
            "tratarea automată a punctelor externe ca erori de măsurare",
            "ignorarea faptului că cutia acoperă doar 50% central",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect boxplotul și valorile extreme?"
        ),
        "options": [
            "cutie Q1–Q3; linie = mediana; H = Q3 − Q1",
            "whiskers la ±1,5×H; dincolo → outlier",
            "tratare outlieri: eliminare/corectare/medie trunchiată/transformări",
            "outlierii se semnalează vizual; tratarea lor rămâne o decizie contextuală",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre boxplot și outlieri sunt corecte?"
        ),
        "options": [
            "boxplot evidențiază compactul central și valorile atipice",
            "criteriul 1,5×H este o convenție descriptivă, nu o regulă de eliminare "
            "obligatorie",
            "mediana din cutie este robustă la outlieri în sensul că nu îi include în "
            "calculul ei direct",
            "orice studiu cu outlieri trebuie să folosească doar modul ca indicator "
            "central",
        ],
        "correct": "ab",
    },
]

assert len(BOXPLOT_ITEMS) == 20
