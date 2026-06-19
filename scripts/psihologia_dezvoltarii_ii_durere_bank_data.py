"""Itemi — Psihologia dezvoltării II: durere și pierdere (441–460, ID 10441–10460)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

DURERE_ITEMS: List[Item] = [
    # —— 441–450: durere, atașament, existențial, dual process ——
    {
        "stem": (
            "Durerea (doliul) este un proces afectiv de adaptare la pierderea unei "
            "persoane semnificative — nu o reacție patologică obligatorie în toate "
            "formele sale."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Conform modelului atașamentului aplicat pierderii, moartea unei figuri "
            "semnificative activează în principal:"
        ),
        "options": [
            "sistemul de atașament și nevoia de apropiere sau de refacere a legăturii",
            "doar stadiul operațiilor formale piagetiene",
            "exclusiv mecanisme de condiționare operantă skinneriană",
            "dispariția completă a oricărei emoții legate de persoana pierdută",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două idei aparțin modelului atașamentului în înțelegerea durerii?"
        ),
        "options": [
            "pierderea reactivează căutarea apropiere și sprijin",
            "durerea poate include căutarea persoanei pierdute sau a unui substitut simbolic",
            "atașamentul nu are nicio legătură cu reacțiile la moarte",
            "reacțiile de durere sunt identice la toți indiferent de istoricul relațional",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Modelul existențial al durerii pune accent pe faptul că moartea:"
        ),
        "options": [
            "obligă la confruntarea cu sensul vieții, finitudinea și valorile",
            "elimină orice întrebare despre sens — doar biologia contează",
            "se explică exclusiv prin etape fixe obligatorii la toți oamenii",
            "anulează complet nevoia de relații cu ceilalți",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei descrieri se potrivesc modelului procesual dual "
            "(Stroebe & Schut) al durerii?"
        ),
        "options": [
            "oscilație între orientarea spre pierdere și cea spre restaurare",
            "orientarea spre pierdere: gânduri, amintiri, emoții legate de cel mort",
            "orientarea spre restaurare: roluri noi, activități, relații, viața cotidiană",
            "proces liniar fără alternanță — doar o singură orientare până la final",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O persoană spune imediat după moartea partenerului: „Nu e adevărat, "
            "doctorii s-au înșelat, el va reveni acasă.” Etapa Kübler-Ross ilustrată "
            "este cel mai probabil:"
        ),
        "options": [
            "negarea",
            "furie",
            "acceptarea",
            "negocierea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două afirmații despre modelul Kübler-Ross sunt corecte?"
        ),
        "options": [
            "include etape precum negare, furie, negociere, depresie, acceptare",
            "etapele nu apar obligatoriu în ordine fixă la toți oamenii",
            "fiecare persoană trece obligatoriu prin toate etapele, în aceeași secvență",
            "modelul înlocuiește complet orice altă explicație a durerii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul Kübler-Ross, etapa furiei poate include:"
        ),
        "options": [
            "protest, iritabilitate, întrebări revoltate despre „de ce”",
            "acceptare liniștită și reorganizare completă a vieții",
            "refuzul total de a recunoaște realitatea morții",
            "promisiunea logică că totul va rămâne neschimbat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei descrieri corespund etapelor Kübler-Ross?"
        ),
        "options": [
            "negociere: „dacă m-aș schimba, poate s-ar întoarce”",
            "depresie: tristețe, retragere, simțirea golului pierderii",
            "acceptare: recunoașterea realității și începutul reorganizării",
            "furie: acceptare imediată fără emoții negative",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două comportamente ilustrează orientarea spre restaurare în "
            "modelul procesual dual?"
        ),
        "options": [
            "reia treptat activități cotidiene și roluri sociale",
            "investește energie în relații noi sau proiecte practice",
            "petrece toate orele revizuind fotografii fără pauză, exclusiv",
            "refuză orice contact cu lumea exterioară timp de ani, fără alternanță",
        ],
        "correct": "ab",
    },
    # —— 451–460: capcane, sinteză, aplicare ——
    {
        "stem": (
            "Toți oamenii trec obligatoriu prin cele cinci etape Kübler-Ross, "
            "în ordinea negare → furie → negociere → depresie → acceptare, "
            "fără excepție."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "O văduvă organizează treptat bugetul, acceptă invitații la familie "
            "și, în aceeași săptămână, plânge intens când găsește obiecte ale "
            "soțului. Procesul descris se potrivește cel mai bine:"
        ),
        "options": [
            "modelului procesual dual — oscilație pierdere / restaurare",
            "modelului existențial — doar căutarea sensului, fără emoție",
            "ideii că durerea ar însemna absența completă a funcționării",
            "unui singur stadiu fix Kübler-Ross, fără variație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două reacții aparțin orientării spre pierdere în modelul dual?"
        ),
        "options": [
            "revizuirea amintirilor și a legăturii cu persoana decedată",
            "dorul intens și gândurile repetitive despre cel pierdut",
            "angajarea imediată în proiecte noi ca singură reacție, fără emoție",
            "negarea totală a oricărei tristeți ca regulă universală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei elemente diferențiază modelul atașamentului de o simplă "
            "„listă de simptome” ale durerii?"
        ),
        "options": [
            "pierderea reactivează strategiile de căutare a apropiere",
            "istoricul relațional modelează intensitatea și forma reacției",
            "durerea e văzută ca proces de adaptare la ruptura legăturii",
            "atașamentul exclude orice influență a relațiilor timpurii",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În modelul existențial, durerea poate declanșa întrebări despre:"
        ),
        "options": [
            "sensul vieții, valorile și propria finitudine",
            "doar viteza de procesare din inteligența fluidă",
            "exclusiv conservarea masei la operațiile concrete",
            "atașamentul evitant din Situația Străină la 12 luni",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru descrieri corespund etapelor Kübler-Ross (negare, furie, "
            "negociere, depresie)?"
        ),
        "options": [
            "negare: refuzul inițial de a accepta realitatea morții",
            "furie: protest și iritabilitate față de situație",
            "negociere: încercarea mentală de a „schimba” outcome-ul",
            "depresie: tristețe profundă, retragere, simțirea pierderii",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un bărbat, după moartea mamei, alternează zile în care vorbește mult "
            "despre ea cu zile în care se ocupă de reparații în casă și de nepoți. "
            "Explicația cea mai potrivită:"
        ),
        "options": [
            "oscilație normală între orientarea spre pierdere și spre restaurare",
            "lipsa completă a durerii — doar aparentă tristețe",
            "patologie obligatorie care anulează modelul atașamentului",
            "dovadă că modelul Kübler-Ross nu are nicio utilitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între durerea normală și depresia clinică severă "
            "sunt formulate corect?"
        ),
        "options": [
            "durerea e legată de pierdere și poate include fluctuații și amintiri",
            "depresia clinică poate persista fără legătură clară cu o pierdere recentă",
            "durerea exclude orice tristețe sau plâns",
            "depresia clinică și durerea sunt mereu identice ca mecanism",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei modele explicative ale durerii sunt prezentate în curs?"
        ),
        "options": [
            "modelul atașamentului — reactivarea nevoii de apropiere",
            "modelul existențial — confruntarea cu sensul și finitudinea",
            "modelul procesual dual — oscilație pierdere / restaurare",
            "modelul senzorio-motor piagetian — permanența obiectului la bebeluși",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două afirmații despre acceptare în modelul Kübler-Ross sunt corecte?"
        ),
        "options": [
            "nu înseamnă bucurie sau uitare, ci recunoașterea realității pierderii",
            "poate include începutul reorganizării vieții fără persoana pierdută",
            "presupune că durerea dispare complet și instantaneu",
            "exclude orice amintire sau emoție legată de cel mort",
        ],
        "correct": "ab",
    },
]

assert len(DURERE_ITEMS) == 20
