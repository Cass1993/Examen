"""Itemi — Psihologia dezvoltării II: dezvoltarea limbajului (itemi 181–210, ID 10181–10210)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

LIMBAJ_ITEMS: List[Item] = [
    # —— 181–188: Chomsky, Skinner, Piaget ——
    {
        "stem": (
            "Conform lui Noam Chomsky, achiziția limbajului are o bază înnăscută "
            "și presupune o predispoziție biologică a copilului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre perspectiva nativistă (Chomsky) este corectă?"
        ),
        "options": [
            "există o predispoziție biologică pentru achiziția limbajului",
            "orice cuvânt nou apare doar prin pedeapsă și recompensă skinneriană",
            "limbajul se explică exclusiv prin imitație mecanică fără structură înnăscută",
            "copilul nu are capacități înnăscute relevante pentru limbaj",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "B. F. Skinner explică achiziția limbajului în principal prin:"
        ),
        "options": [
            "întărire și condiționare a răspunsurilor verbale",
            "maturare biologică independentă de mediu",
            "reorganizare piagetiană a operațiilor formale",
            "atașament exclusiv, fără feedback din mediu",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "La Piaget, dezvoltarea limbajului este strâns legată în principal de:"
        ),
        "options": [
            "dezvoltarea gândirii și a simbolizării",
            "condiționarea reflexelor incondiționate neonatale ca singur mecanism",
            "absența oricărei influențe a schemei cognitive",
            "operațiile formale abstracte de la naștere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între Chomsky și Skinner privind limbajul sunt corecte?"
        ),
        "options": [
            "Chomsky: predispoziție înnăscută; Skinner: învățare prin consecințe",
            "Chomsky: mecanisme biologice; Skinner: întărire și modelare",
            "Chomsky: limbaj doar prin pedeapsă; Skinner: capacitate înnăscută exclusivă",
            "Skinner: comportament verbal modelat de mediu; Chomsky: limite ale explicației pure behavioriste",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru descrieri despre ordinea achiziției timpurii a limbajului sunt corecte?"
        ),
        "options": [
            "vocalizările neonatale preced gânguritul",
            "gânguritul precede de regulă primele cuvinte cu referință",
            "propozițiile de două cuvinte preced adesea limbajul telegrafic",
            "de la sunete la silabe, apoi cuvinte și propoziții simple",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Skinner consideră că limbajul este exclusiv înnăscut, fără nicio "
            "influență a întăririi din mediu."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— 189–196: stadii, explozia vocabularului ——
    {
        "stem": (
            "Primele cuvinte cu referință la obiecte sau persoane apar, de regulă, "
            "în jurul vârstei de:"
        ),
        "options": [
            "12 luni (cu variații individuale)",
            "3–4 ani, odată cu operațiile formale",
            "la naștere, ca reflexe articulate complete",
            "doar după șase ani, la intrarea în școală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături definesc propozițiile de două cuvinte și limbajul telegrafic?"
        ),
        "options": [
            "combinarea a două cuvinte pentru a transmite o idee simplă (ex. „mama vin”)",
            "omisiunea unor cuvinte gramaticale, păstrând sensul de bază",
            "propoziții complexe cu subordonate și ipoteze abstracte",
            "dicție adultă completă de la primele luni",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre explozia vocabularului de la ~18 luni este corectă?"
        ),
        "options": [
            "creștere rapidă a numărului de cuvinte înțelese și folosite",
            "dispariția completă a comunicării nonverbale",
            "apariție exclusiv după operațiile formale",
            "vocabular fix care nu se mai extinde",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație descrie faza în care un singur cuvânt exprimă o "
            "propoziție întreagă (holofrază)?"
        ),
        "options": [
            "copilul folosește un cuvânt pentru mai multe intenții, în context",
            "apare doar la adolescență, odată cu operațiile formale",
            "exclude complet comunicarea nonverbală",
            "înseamnă deja gramatică adultă completă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei afirmații despre legătura piagetiană limbaj–gândire sunt corecte?"
        ),
        "options": [
            "limbajul reflectă și susține dezvoltarea simbolizării",
            "gândirea senzorio-motoră timpurie pregătește reprezentările folosite în limbaj",
            "jocul simbolic și cuvintele sunt ambele forme de reprezentare",
            "limbajul apare complet separat de orice reorganizare cognitivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre plânsul în primele luni este corectă?"
        ),
        "options": [
            "semnalează foame, durere sau disconfort fizic",
            "comunică nevoie de contact și consolare",
            "manipulare formală deliberată a variabilelor logice",
            "apare doar după operațiile formale",
        ],
        "correct": "a",
    },
    # —— 197–204: zâmbet social, vocalizări, gângurit ——
    {
        "stem": (
            "Care două efecte are zâmbetul social asupra comunicării timpurii?"
        ),
        "options": [
            "întărește schimbul afectiv copil–adult",
            "răspunde la vocea sau figura umană",
            "apare doar la stimuli mecanici, fără recunoaștere umană",
            "substituie complet plânsul ca unic semnal de nevoie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care descrieri despre zâmbetul social sunt corecte?"
        ),
        "options": [
            "apare ca răspuns la fața sau vocea unei persoane",
            "diferă de zâmbetul reflex neonatal, mai puțin dependent de stimul intern",
            "întărește schimbul afectiv și comunicarea timpurie",
            "apare exclusiv după primul cuvânt rostit",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care trei descrieri despre zâmbetul social sunt corecte?"
        ),
        "options": [
            "apare ca răspuns la fața sau vocea unei persoane",
            "diferă de zâmbetul reflex neonatal",
            "întărește schimbul afectiv și comunicarea timpurie",
            "apare exclusiv după primul cuvânt rostit",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care elemente aparțin dezvoltării timpurii a limbajului înainte de "
            "propoziții elaborate?"
        ),
        "options": [
            "vocalizări — sunete variate în primele luni",
            "gângurit — silabe repetate (ba-ba, ma-ma) în jurul a 6–9 luni",
            "primele cuvinte cu referință la obiecte sau persoane",
            "dicție perfectă și gramatică adultă de la naștere",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două funcții are gânguritul (babbling)?"
        ),
        "options": [
            "antrenează articularea sunetelor și pregătește producerea vorbirii",
            "reprezintă joc vocal care precede cuvintele cu sens",
            "dovedește deja operații formale abstracte",
            "substituie definitiv comunicarea nonverbală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care mecanisme skinneriene se aplică achiziției limbajului?"
        ),
        "options": [
            "întărirea răspunsurilor verbale corecte de către adult",
            "modelarea — copilul imită structuri auzite în mediu",
            "pedeapsa sau ignorarea pot reduce anumite forme verbale",
            "capacitate înnăscută de gramatică universală, fără input social",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Plânsul nu are funcție socială — este doar un reflex fiziologic "
            "imposibil de interpretat de adult."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care două trăsături definesc limbajul telegrafic al copilului mic?"
        ),
        "options": [
            "puține cuvinte esențiale, sens transmis în context",
            "omiterea unor cuvinte gramaticale cu păstrarea mesajului",
            "propoziții adulte complete de la primele cuvinte",
            "dispariția oricărei comunicări nonverbale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Înainte de primele cuvinte, copilul comunică prin:"
        ),
        "options": [
            "plâns diferențiat în funcție de nevoie",
            "zâmbet social și contact vizual",
            "vocalizări și gângurit progresiv",
            "eseuri scrise și propoziții complexe",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care teoretician leagă explozia vocabularului de maturarea "
            "cognitivă și simbolizare, nu doar de întărire?"
        ),
        "options": [
            "Piaget — limbajul urmează dezvoltării reprezentării",
            "Skinner — exclusiv condiționare fără scheme cognitive",
            "Chomsky — predispoziție înnăscută pentru structura limbajului",
            "Freud — interpretarea viselor ca formă de comunicare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru perechi teoretician–idee despre limbaj sunt corecte?"
        ),
        "options": [
            "Chomsky — predispoziție biologică pentru achiziție",
            "Skinner — întărire și condiționare a comportamentului verbal",
            "Piaget — limbaj legat de gândire și simbolizare",
            "dezvoltare treptată de la vocalizări la propoziții — perspectivă evolutivă",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care două etape vocale preced de obicei primele cuvinte?"
        ),
        "options": [
            "vocalizările — sunete variate din primele luni",
            "gânguritul — silabe combinate în jurul a 6–9 luni",
            "gânguritul apare înaintea vocalizărilor neonatale",
            "operațiile formale abstracte",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre zâmbetul social este corectă?"
        ),
        "options": [
            "încurajează interacțiunea și schimbul afectiv copil–adult",
            "înlocuiește complet nevoia de contact fizic",
            "apare exclusiv după explozia vocabularului",
            "nu are nicio funcție în comunicarea timpurie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru formulări descriu corect dezvoltarea timpurie a limbajului?"
        ),
        "options": [
            "de la vocalizări la gângurit, apoi cuvinte și propoziții simple",
            "explozie vocabular în jurul a 18 luni la mulți copii",
            "comunicare nonverbală (plâns, zâmbet) înainte de cuvinte",
            "progresie treptată, nu apariție bruscă a limbajului adult",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un adult răspunde cu entuziasm când copilul rostește un cuvânt nou. "
            "Din perspectiva lui Skinner, acest lucru:"
        ),
        "options": [
            "întărește probabilitatea repetării acelui răspuns verbal",
            "modelează achiziția limbajului prin consecințe sociale",
            "dovedește capacitatea înnăscută de gramatică universală ca singură cauză",
            "nu are nicio legătură cu învățarea limbajului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "După limbajul telegrafic, dezvoltarea lexicală tipică include:"
        ),
        "options": [
            "vocabular tot mai extins și propoziții mai complete",
            "păstrarea permanentă a propozițiilor de un singur cuvânt ca formă dominantă",
            "dispariția comunicării nonverbale",
            "apariția exclusivă a gândirii formale abstracte",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre plânsul ca comunicare timpurie este corectă?"
        ),
        "options": [
            "adultul poate diferenția treptat tipuri de plâns",
            "nu are nicio funcție socială până la primul cuvânt",
            "apare doar după operațiile formale",
            "semnalează exclusiv durere fizică, niciodată nevoi afective",
        ],
        "correct": "a",
    },
]

assert len(LIMBAJ_ITEMS) == 30
