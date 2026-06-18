"""Itemi — Inteligență emoțională (lot evaluare psihologică II)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

INTELIGENTA_EMOTIONALA_ITEMS: List[Item] = [
    # —— Inteligență cognitivă versus emoțională (1–10) ——
    {
        "stem": (
            "Care diferență descrie corect raportul dintre inteligența cognitivă "
            "și inteligența emoțională, în termeni de orientare temporală?"
        ),
        "options": [
            "inteligența cognitivă este mai strategică, pe termen lung",
            "inteligența emoțională este mai tactică, orientată spre situația imediată",
            "ambele sunt exclusiv tactice, fără planificare",
            "inteligența emoțională exclude orice componentă de adaptare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care structuri cerebrale sunt asociate, în principal, cu inteligența "
            "emoțională, spre deosebire de cortexul prefrontal al inteligenței cognitive?"
        ),
        "options": [
            "amigdala",
            "cortexul cingulat anterior",
            "talamusul, în procesarea stimulilor relevanți emoțional",
            "cerebelul, ca unic sediu al raționamentului abstract",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Inteligența cognitivă este legată în principal de cortexul prefrontal "
            "și de raționament, în timp ce inteligența emoțională sprijină "
            "supraviețuirea și adaptarea la mediu."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Inteligența emoțională și inteligența cognitivă folosesc aceleași "
            "rețele neuronale, fără implicarea amigdalei sau a cortexului cingulat."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce se spune că inteligența emoțională are o componentă tactică, "
            "immediată?"
        ),
        "options": [
            "emoțiile semnalează rapid amenințări sau oportunități în mediu",
            "reglarea emoțională sprijină răspunsul adaptat în situația prezentă",
            "exclude planificarea pe termen lung a obiectivelor",
            "suplimentează judecata rațională din cortexul prefrontal",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un student își planifică cariera pe cinci ani folosind analiză logică "
            "și teste de aptitudine; în același timp, își recunoaște anxietatea "
            "înaintea examenului și o reglează. Aceasta ilustrează:"
        ),
        "options": [
            "inteligență cognitivă pentru planificare strategică",
            "inteligență emoțională pentru gestionarea stării imediate",
            "lipsa diferențelor clare între cele două constructe",
            "faptul că doar inteligența cognitivă contează clinic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care scop este asociat, în principal, inteligenței cognitive, "
            "respectiv inteligenței emoționale?"
        ),
        "options": [
            "raționament și rezolvare de probleme — cognitiv",
            "supraviețuire și adaptare la context — emoțional",
            "raționament — emoțional; supraviețuire — cognitiv",
            "ambele au exclusiv scopul măsurării trăsăturilor de personalitate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații descriu corect limitele evaluării inteligenței emoționale "
            "doar prin coeficient de inteligență verbal?"
        ),
        "options": [
            "coeficientul de inteligență nu măsoară reglarea emoțională",
            "sunt necesare instrumente specifice emoțiilor",
            "coeficientul verbal înlocuiește complet testul Mayer–Salovey–Caruso",
            "inteligența emoțională este identică cu inteligența generală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Cum se completează, în practică, inteligența cognitivă și cea emoțională?"
        ),
        "options": [
            "cognitivul sprijină înțelegerea și planificarea",
            "emoționalul sprijină reglarea și relaționarea în situații concrete",
            "unul îl anulează pe celălalt în orice context clinic",
            "doar cognitivul este relevant în psihologia aplicată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Talamusul poate fi implicat în inteligența emoțională prin rolul său "
            "în transmiterea și integrarea informației senzoriale relevante pentru "
            "semnificația emoțională a stimulilor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Modele de inteligență emoțională (11–22) ——
    {
        "stem": (
            "Modelul abilității Mayer și Salovey descrie capacități cognitive "
            "legate de emoții. Care procese sunt incluse în acest model?"
        ),
        "options": [
            "percepția emoțiilor",
            "utilizarea emoțiilor pentru a facilita gândirea",
            "înțelegerea emoțiilor și gestionarea emoțiilor",
            "măsurarea exclusivă a trăsăturilor de personalitate stabile",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce tip de instrument este caracteristic modelului abilității "
            "Mayer–Salovey–Caruso?"
        ),
        "options": [
            "sarcini de performanță cu barem obiectiv pentru probleme emoționale",
            "chestionar de auto-raportare a trăsăturilor emoționale stabile",
            "inventarul de inteligență emoțională Bar-On, ca unic instrument valid",
            "scala de aptitudini cognitive Wechsler, fără componentă emoțională",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Konstantinos Petrides propune un model în care inteligența emoțională "
            "se aseamănă unor dispoziții relativ stabile. Ce tip de instrument "
            "este caracteristic acestui model?"
        ),
        "options": [
            "chestionar de auto-raportare a preferințelor și dispozițiilor emoționale",
            "sarcini de performanță cu barem obiectiv pentru emoții",
            "inventarul multifazic de personalitate Minnesota",
            "testul de pată de cerneală Rorschach",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care factori globali include chestionarul de inteligență emoțională "
            "ca trăsătură (Petrides)?"
        ),
        "options": [
            "bunăstare",
            "autocontrol",
            "emoționalitate și sociabilitate",
            "raționament fluid și cunoștințe cristalizate",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Modelele mixte de inteligență emoțională, cum ar fi cele ale lui "
            "Reuven Bar-On sau Daniel Goleman, combină:"
        ),
        "options": [
            "componente de abilitate",
            "componente de trăsătură și competență emoțională",
            "scorul la testul de inteligență generală",
            "doar auto-raportarea, fără nicio abilitate măsurabilă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Inventarul de inteligență emoțională Bar-On (EQ-i) este asociat, "
            "în principal, cu un model:"
        ),
        "options": [
            "mixt, ce include trăsături și competențe emoționale",
            "strict de abilitate pură, fără auto-raportare",
            "exclusiv psihanalitic, fără standardizare",
            "identic cu testul Mayer–Salovey–Caruso",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Testul Mayer–Salovey–Caruso măsoară în principal abilități de rezolvare "
            "a sarcinilor legate de emoții, nu doar autopercepția trăsăturilor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Chestionarul Petrides și testul Mayer–Salovey–Caruso măsoară exact "
            "același construct, cu aceeași metodă de administrare."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Ce a contribuit Daniel Goleman la dezvoltarea conceptului de inteligență "
            "emoțională în cultura largă?"
        ),
        "options": [
            "popularizarea ideii în context organizațional și educațional",
            "integrarea perspectivei de abilitate, trăsătură și competență emoțională",
            "eliminarea distincției dintre abilitate și trăsătură în cercetare",
            "respingerea oricărui model mixt de inteligență emoțională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care pereche asociază corect modelul cu tipul de măsurare?"
        ),
        "options": [
            "Mayer–Salovey — abilitate, sarcini cu barem de performanță",
            "Petrides — trăsătură, auto-raportare pe chestionar",
            "Mayer–Salovey — trăsătură stabilă, fără sarcini de performanță",
            "Petrides — abilitate pură, identică cu testul Mayer–Salovey–Caruso",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce modelele mixte sunt criticate în literatura științifică?"
        ),
        "options": [
            "combină constructe diferite într-un singur scor",
            "pot confunda abilitatea reală cu autopercepția sau trăsăturile",
            "sunt întotdeauna superioare modelului de abilitate pur",
            "exclud complet componenta emoțională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Utilizarea emoțiilor pentru a facilita gândirea, în modelul Mayer–Salovey, "
            "înseamnă folosirea stărilor emoționale pentru a îmbunătăți rezolvarea "
            "problemelor și creativitatea."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Competență emoțională: Saarni, Bulgac (23–34) ——
    {
        "stem": (
            "Competența emoțională, în perspectiva lui Carolyn Saarni, este mai "
            "bine definită decât inteligența emoțională deoarece include:"
        ),
        "options": [
            "eficiență motivațională în situații emoționale",
            "contextul social și valorile persoanei",
            "scorul la testul de inteligență generală",
            "lipsa componentei comportamentale în modelul descris",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care componente fac parte din cele opt dimensiuni ale competenței "
            "emoționale (Saarni)?"
        ),
        "options": [
            "conștientizarea proprie a emoțiilor",
            "discernarea emoțiilor la ceilalți",
            "vocabular emoțional și empatie",
            "raționament cantitativ și memorie de lucru",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Competența emoțională se referă la eficiența comportamentală și "
            "motivațională în situații emoționale, nu doar la capacitatea "
            "cognitivă de a recunoaște emoțiile."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În modelul Bulgac (2018), variabilele predictor din inventarul "
            "Bar-On (conștiință de sine, toleranță la stres, relații interpersonale) "
            "influențează mediatoarele:"
        ),
        "options": [
            "inteligența emoțională intrapersonală și interpersonală",
            "profilul eficienței emoționale",
            "adaptarea comportamentală măsurată cu scala de evaluare a comportamentului",
            "coeficientul de inteligență general, ca singur mediator",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul Bulgac (2018), variabila criteriu (rezultatul final) este "
            "adaptarea comportamentală evaluată cu:"
        ),
        "options": [
            "scala de evaluare a comportamentului la copii și adolescenți, a doua ediție",
            "testul Mayer–Salovey–Caruso de inteligență emoțională",
            "inventarul multifazic de personalitate Minnesota",
            "scala Wechsler de inteligență pentru adulți",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Profilul eficienței emoționale (Mikolajczak) include trei nivele:"
        ),
        "options": [
            "cunoștințe despre emoții",
            "abilități de gestionare emoțională",
            "dispoziție sau tendință de a aplica abilitățile",
            "coeficient de inteligență verbal, ca nivel principal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Cele zece dimensiuni ale profilului eficienței emoționale (Mikolajczak) "
            "reflectă o structură de tip:"
        ),
        "options": [
            "cinci domenii aplicate la sine și la ceilalți",
            "cinci ori două — eu și alții",
            "zece abilități cognitive generale, fără componentă socială",
            "două singure dimensiuni: verbal și performanță",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce include modelul Bulgac atât inventarul Bar-On, cât și profilul "
            "eficienței emoționale ca variabile mediatoare?"
        ),
        "options": [
            "pentru a lega trăsăturile emoționale de abilitățile intra- și interpersonale",
            "pentru a explica legătura dintre predictor și adaptarea comportamentală",
            "pentru a elimina nevoia de orice variabilă criteriu",
            "pentru a înlocui complet evaluarea clinică cu un singur chestionar",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Vocabularul emoțional, ca dimensiune a competenței emoționale, "
            "facilitează etichetarea precisă a stărilor afective și comunicarea "
            "despre emoții."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație descrie corect empatia în cadrul competenței emoționale?"
        ),
        "options": [
            "include discernerea emoțiilor celuilalt, nu doar simpatia pasivă",
            "sprijină relaționarea adaptivă în context social",
            "exclude recunoașterea stărilor afective ale altora",
            "este identică cu raționamentul cantitativ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un copil cu scor ridicat la conștiință de sine (inventar Bar-On), dar "
            "scor scăzut la profilul eficienței emoționale intrapersonale, poate "
            "avea în continuare dificultăți de adaptare la școală. Modelul Bulgac "
            "explică acest lucru prin:"
        ),
        "options": [
            "medierea prin profilul eficienței emoționale între predictor și criteriu",
            "faptul că trăsăturile emoționale nu se traduc automat în abilități aplicate",
            "lipsa oricărei legături între emoții și comportament",
            "identitatea perfectă între inventarul Bar-On și adaptarea comportamentală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care componentă Saarni vizează capacitatea de a distinge emoțiile "
            "proprii de cele ale altora?"
        ),
        "options": [
            "conștientizarea proprie",
            "discernerea emoțiilor la ceilalți",
            "raționamentul cantitativ",
            "toleranța la frustrare motorie",
        ],
        "correct": "b",
    },
    # —— Limite și instrumente (35–50) ——
    {
        "stem": (
            "Care critici sunt frecvent formulate în literatura de specialitate "
            "privind constructul de inteligență emoțională?"
        ),
        "options": [
            "definiție insuficient de precisă, cu suprapuneri între modele",
            "multe chestionare măsoară mai degrabă trăsături de personalitate",
            "validitate perfectă și consens universal între toți cercetătorii",
            "absența oricărui instrument standardizat de măsurare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce se afirmă adesea că chestionarele de inteligență emoțională "
            "se aseamănă cu măsurători de trăsături de personalitate?"
        ),
        "options": [
            "folosesc auto-raportarea stilurilor și tendințelor stabile",
            "măsoară percepția de sine, nu întotdeauna performanța reală",
            "exclud complet orice item legat de emoții",
            "sunt identice cu testele de aptitudini cognitive",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care instrumente sunt folosite frecvent în cercetarea și practica "
            "inteligenței emoționale?"
        ),
        "options": [
            "testul Mayer–Salovey–Caruso de inteligență emoțională",
            "inventarul de inteligență emoțională Bar-On",
            "chestionarul de inteligență emoțională ca trăsătură Petrides",
            "scala Rorschach, ca instrument principal al inteligenței emoționale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce este testul Mayer–Salovey–Caruso preferat de susținătorii "
            "modelului abilității?"
        ),
        "options": [
            "evaluează performanța la sarcini cu barem",
            "reduce dependența de auto-raportarea trăsăturilor",
            "măsoară exclusiv desirabilitatea socială",
            "este identic cu chestionarul Petrides",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care instrumente se bazează în principal pe auto-raportare?"
        ),
        "options": [
            "inventarul de inteligență emoțională Bar-On",
            "chestionarul de inteligență emoțională ca trăsătură Petrides",
            "testul Mayer–Salovey–Caruso de inteligență emoțională",
            "scala Wechsler de inteligență pentru adulți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Constructul de inteligență emoțională este definit unanim în literatura "
            "științifică, fără dezbateri între modelele de abilitate, trăsătură "
            "și mixte."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Ce distinge măsurarea abilității de măsurarea trăsăturii în "
            "inteligența emoțională?"
        ),
        "options": [
            "abilitatea — sarcini cu răspuns corect sau greșit, evaluat de barem",
            "trăsătura — chestionar despre tendințe și stiluri auto-raportate",
            "abilitatea — exclusiv auto-raportare pe scală Likert",
            "trăsătura — exclusiv test de performanță cu timp limitat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un manager obține scor mare la inventarul Bar-On, dar colegii raportează "
            "că nu gestionează bine conflictele. Aceasta ilustrează o limită frecventă:"
        ),
        "options": [
            "discrepanța între auto-raportare și comportament observat",
            "suprapunerea cu trăsături de sociabilitate sau desirabilitate socială",
            "validitate perfectă a oricărui chestionar de inteligență emoțională",
            "imposibilitatea evaluării emoțiilor în context organizațional",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profilul eficienței emoționale diferențiază nivelul de cunoștințe de "
            "cel de abilități și dispoziție, pentru a explica de ce unele persoane "
            "„știu” regulile emoționale, dar nu le aplică."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Ce ilustrează modelul Bulgac privind variabila criteriu?"
        ),
        "options": [
            "adaptarea comportamentală este rezultatul final evaluat",
            "scala pentru copii și adolescenți măsoară criteriul, nu predictorul direct",
            "inventarul Bar-On este singura variabilă criteriu",
            "profilul eficienței emoționale înlocuiește orice evaluare comportamentală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație descrie corect relația dintre inteligența emoțională "
            "și competența emoțională?"
        ),
        "options": [
            "competența emoțională pune accent pe eficacitate în context și valori",
            "inteligența emoțională poate fi un predictor al competenței, dar nu este identică cu ea",
            "sunt termeni complet interschimbabili, fără diferențe teoretice",
            "competența emoțională exclude orice componentă motivațională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce include gestionarea emoțiilor în modelul Mayer–Salovey?"
        ),
        "options": [
            "reglarea propriilor emoții",
            "influențarea emoțiilor celorlalți, în limite adaptative",
            "reducerea emoțiilor negative, nu eliminarea lor",
            "evaluarea competențelor emoționale doar prin auto-raportare izolată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce rol are cortexul prefrontal în raportul dintre inteligența cognitivă "
            "și cea emoțională?"
        ),
        "options": [
            "sprijină raționamentul și controlul executiv",
            "poate modera răspunsurile emoționale generate de amigdală",
            "nu are nicio legătură cu reglarea emoțională",
            "suplimentează funcțiile amigdalei în reglarea emoțională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un cercetător compară scorurile la testul Mayer–Salovey–Caruso cu "
            "rezultatele la inventarul Bar-On și constată corelații moderate. "
            "Interpretarea cea mai prudentă este:"
        ),
        "options": [
            "cele două instrumente măsoară constructe parțial suprapuse",
            "abilitatea măsurată prin performanță nu este identică cu auto-raportarea trăsăturilor",
            "corelația perfectă demonstrează că sunt același test",
            "lipsa corelației ar fi dovada validității maxime",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care rol are toleranța la stres în modelul Bulgac?"
        ),
        "options": [
            "predictor din inventarul Bar-On",
            "poate influența profilul eficienței emoționale și adaptarea indirect",
            "variabilă criteriu măsurată cu scala pentru copii și adolescenți",
            "construct fără legătură cu inteligența emoțională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru o evaluare comprehensivă a inteligenței emoționale, este "
            "recomandabil să se combine:"
        ),
        "options": [
            "măsuri de abilitate și de trăsătură, cu interpretare critică",
            "date din teste de performanță și chestionare, plus observație comportamentală",
            "un singur chestionar, fără verificare externă",
            "exclusiv coeficientul de inteligență general, ca substitut",
        ],
        "correct": "ab",
    },
]
