"""Itemi — Psihologia dezvoltării II: mica școlaritate (281–320, ID 10281–10320)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SCOLARITATE_ITEMS: List[Item] = [
    # —— 281–288: caracter general, intrarea în școală ——
    {
        "stem": (
            "Mica școlaritate (aproximativ 6–10/11 ani) aduce pentru copil "
            "adaptare la reguli, ritm școlar, sarcini și relații noi cu colegii "
            "și profesorii."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care schimbare cognitivă apare odată cu intrarea în școală?"
        ),
        "options": [
            "sarcini cognitive și sociale mai complexe decât la grădiniță",
            "dispariția completă a jocului și a activității fizice",
            "stadiul senzorio-motor cu reflexe dominante",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături descriu dezvoltarea fizică în mica școlaritate?"
        ),
        "options": [
            "creștere corporală mai lentă decât în primii ani",
            "coordonare motorie mai bună și control postural crescut",
            "reflexe neonatale ca formă dominantă de mișcare",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La Piaget, copilul din mica școlaritate se află de regulă în "
            "stadiul:"
        ),
        "options": [
            "operațiilor concrete",
            "operațiilor formale abstracte",
            "senzorio-motor",
            "preoperațional",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două capacități definesc gândirea în operațiile concrete?"
        ),
        "options": [
            "raționează logic pe obiecte și situații concrete",
            "are dificultăți cu probleme pur abstracte, fără suport concret",
            "nu poate clasifica sau ordona obiecte reale",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care achiziții piagetiene apar în operațiile concrete?"
        ),
        "options": [
            "conservare",
            "clasificare și seriere",
            "reversibilitate și decentrare",
            "gândire ipotetico-deductive exclusiv abstractă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Copilul de 8 ani poate rezolva orice problemă abstractă cu "
            "variabile ipotetice, ca un adolescent în stadiul formal."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei dimensiuni solicită adaptarea la intrarea în școală?"
        ),
        "options": [
            "cognitivă — atenție, memorie, strategii de învățare",
            "socială — reguli de grup, prietenii, rolul de elev",
            "emoțională — anxietate, motivație, stima de sine școlară",
            "exclusiv fizică, fără componentă relațională",
        ],
        "correct": "abc",
    },
    # —— 289–296: conservare, reversibilitate, decentrare ——
    {
        "stem": (
            "Care patru idei descriu conservarea la Piaget?"
        ),
        "options": [
            "o cantitate rămâne aceeași chiar dacă forma arată diferit",
            "transformarea vizuală nu schimbă automat cantitatea",
            "lichidul turnat într-un pahar înalt nu e „mai mult” decât în cel lat",
            "copilul poate urmări mental transformarea reversibilă",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care exemplu ilustrează lipsa conservării (tipic preoperațional)?"
        ),
        "options": [
            "copilul crede că sucul e mai mult într-un pahar înalt și subțire",
            "copilul se concentrează doar pe o dimensiune (înălțime), ignorând lățimea",
            "copilul explică că au rămas aceleași bile, doar aranjate altfel",
            "copilul nu poate urmări mental transformarea reversibilă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două capacități definesc reversibilitatea în gândirea concretă?"
        ),
        "options": [
            "urmări mental operația inversă (a îndoi înapoi gândirea)",
            "înțelege că 3+2=5 implică și 5−2=3",
            "opera doar în sens unic, fără întoarcere mentală",
            "ignora complet transformările reversibile ale obiectelor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine decentrarea cognitivă?"
        ),
        "options": [
            "lua în calcul mai multe aspecte ale unei situații simultan",
            "vedea o problemă doar din propria perspectivă egocentrică",
            "se concentra exclusiv pe un singur detaliu vizibil",
            "opera doar cu reflexe neonatale, fără logică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care operații concrete sunt legate de conservare?"
        ),
        "options": [
            "clasificarea obiectelor după mai multe criterii",
            "serierea (ordonarea după mărime sau alt atribut)",
            "reversibilitatea mentală a transformărilor",
            "reflexia asupra ipotezelor științifice abstracte",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Serierea în stadiul operațiilor concrete se referă la:"
        ),
        "options": [
            "ordonarea obiectelor după mărime, greutate sau alt atribut",
            "scrierea reflexivă a propozițiilor complexe",
            "capacitatea de a ignora ordinea și a grupa aleator",
            "operații formale cu variabile ipotetice",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Conservarea apare de obicei înainte de decentrare și reversibilitate "
            "— toate trei sunt deja consolidate la 3 ani."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un copil care sortează fructele după culoare și mărime simultan "
            "demonstrează:"
        ),
        "options": [
            "clasificare pe mai multe criterii — achiziție concretă",
            "decentrare — nu se limitează la un singur atribut",
            "operații formale cu variabile abstracte",
            "centrare preoperațională exclusivă pe aspectul vizual dominant",
        ],
        "correct": "ab",
    },
    # —— 297–304: memorie, metamemorie ——
    {
        "stem": (
            "Memoria școlarului mic se dezvoltă prin:"
        ),
        "options": [
            "repetiție și exersare deliberate",
            "grupare și organizare a informației",
            "folosirea de indicii și strategii de memorare",
            "dispariția completă a memoriei pe termen scurt",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care element central definește metamemoria?"
        ),
        "options": [
            "cunoașterea propriilor capacități de memorare",
            "absența oricărei reflecții asupra modului de învățare",
            "memorarea pasivă fără monitorizare a propriului progres",
            "stocarea automată fără strategii deliberate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un elev care spune „trebuie să grupez cuvintele pe teme ca să le "
            "rețin” demonstrează:"
        ),
        "options": [
            "metamemorie — știe ce strategie folosește",
            "organizare deliberată a materialului",
            "reflex senzorio-motor fără plan",
            "absența oricărei strategii deliberate de învățare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care strategii de memorare sunt realiste pentru 7–10 ani?"
        ),
        "options": [
            "repetiția activă (recitare, rescriere)",
            "gruparea elementelor legate semantic",
            "utilizarea de imagini sau asocieri simple",
            "rezolvarea exclusivă a problemelor formale fără suport",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Metamemoria implică faptul că copilul poate evalua dacă a reținut "
            "informația și poate ajusta strategiile de învățare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre dezvoltarea memoriei la școlarul mic este "
            "corectă?"
        ),
        "options": [
            "strategiile deliberate pot îmbunătăți reținerea",
            "memoria e fixă de la naștere și nu se schimbă deloc",
            "exersarea nu influențează deloc capacitatea de memorare",
            "doar factorii biologici contează, nu strategiile învățate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două motive explică de ce gruparea informației ajută memoria?"
        ),
        "options": [
            "reduce încărcătura cognitivă prin organizare",
            "creează legături semantice între elemente",
            "elimină nevoia de repetiție oricum",
            "înlocuiește complet nevoia de atenție la sarcină",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două distincții între memorie și metamemorie sunt corecte?"
        ),
        "options": [
            "memoria: reținerea informației; metamemoria: știința despre propria memorie",
            "metamemoria: alegerea strategiilor; memoria simplă: doar stocare pasivă",
            "sunt identice — orice reținere e metamemorie",
            "metamemoria dispare odată cu intrarea în școală",
        ],
        "correct": "ab",
    },
    # —— 305–312: sinteze, capcane ——
    {
        "stem": (
            "Care descriere se confundă cel mai ușor cu conservarea corectă?"
        ),
        "options": [
            "„E mai mult pentru că paharul e mai înalt” — centrare pe o dimensiune",
            "„E aceeași cantitate, doar arată diferit” — reversibilitate mentală",
            "„Bilele sunt la fel, le-ai mutat doar locul” — conservare număr",
            "„Dacă torni înapoi, rămâne la fel” — operație inversă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre coordonarea motorie la 7–10 ani este corectă?"
        ),
        "options": [
            "susține scrierea de mână mai fluentă",
            "dispariția completă a nevoii de mișcare",
            "reflexe neonatale ca formă dominantă de mișcare",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru capacități permit copilului operațiile concrete?"
        ),
        "options": [
            "rezolvă probleme logice cu obiecte reale sau reprezentate",
            "înțelege transformări reversibile (conservare)",
            "clasifice și ordoneze după reguli consistente",
            "opereze exclusiv cu simboluri abstracte fără suport",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care două elemente definesc adaptarea socială în școală?"
        ),
        "options": [
            "respectarea regulilor clasei și ale școlii",
            "formarea prieteniilor și lucrul în echipă",
            "absența oricărui conflict sau emoție negativă",
            "dispariția completă a atașamentului față de familie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care achiziții cognitive din mica școlaritate se susțin reciproc?"
        ),
        "options": [
            "decentrarea facilitează conservarea",
            "reversibilitatea susține înțelegerea transformărilor",
            "clasificarea și serierea organizează gândirea logică",
            "reflexele neonatale fundamentează metamemoria",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care semn indică cel mai clar metamemorie la un copil de 9 ani?"
        ),
        "options": [
            "monitorizarea propriei învățări („nu știu lecția, mai repet”)",
            "operații formale abstracte ca la adolescent",
            "absența oricărei conștientizări a propriilor strategii",
            "memorare perfectă fără efort sau planificare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre creșterea fizică în mica școlaritate este corectă?"
        ),
        "options": [
            "dezvoltarea fizică continuă, dar ritmul e mai moderat decât în primii ani",
            "copilul nu mai crește deloc în înălțime până la pubertate",
            "coordonarea motorie fină încetează complet în această perioadă",
            "reflexele neonatale domină din nou mișcarea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care idee despre conservarea masei este corectă în operațiile concrete?"
        ),
        "options": [
            "modelarea plastilinei nu schimbă cantitatea de material",
            "orice schimbare de formă reduce automat masa",
            "conservarea apare doar în stadiul senzorio-motor",
            "copilul nu poate urmări mental transformarea",
        ],
        "correct": "a",
    },
    # —— 313–320: sinteză finală ——
    {
        "stem": (
            "Care formulări descriu corect mica școlaritate?"
        ),
        "options": [
            "perioadă 6–10/11 ani cu accent pe școală și operații concrete",
            "dezvoltare fizică moderată, motricitate îmbunătățită",
            "gândire logică legată de concret, nu formal abstract dominant",
            "stadiu senzorio-motor cu reflexe dominante",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profesoara îi cere elevilor să ordoneze bețișoarele după lungime. "
            "Aceasta exersează în principal:"
        ),
        "options": [
            "seriere — operație concretă",
            "gândire logică pe atribute măsurabile",
            "operații formale cu variabile ipotetice",
            "reflexe neonatale fără organizare logică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două manifestări indică metamemorie slab dezvoltată?"
        ),
        "options": [
            "supraestimarea a cât au învățat („știu tot”) fără verificare",
            "alegerea unor strategii ineficiente fără conștientizare",
            "monitorizare precisă și ajustare constantă a studiului",
            "planificare realistă a repetării înainte de test",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru beneficii aduce disciplina și ritmul școlar copilului?"
        ),
        "options": [
            "structurează timpul și responsabilitățile",
            "dezvolte autonomie în sarcini și teme",
            "se adaptează la așteptări sociale ale mediului educațional",
            "susține obiceiuri de lucru și respectarea regulilor",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine diferența preoperațional–operații concrete?"
        ),
        "options": [
            "preoperațional: centrare, lipsă conservare; concret: decentrare, conservare",
            "sunt identice ca vârstă și achiziții",
            "concret: un singur aspect vizual dominant",
            "preoperațional: logică pe obiecte reale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două efecte au repetarea, gruparea și indiciile deliberate în memorare?"
        ),
        "options": [
            "sunt strategii pe care școlarul le poate învăța progresiv",
            "se leagă de dezvoltarea metamemoriei",
            "nu au efect — doar inteligența fixă contează",
            "înlocuiesc complet nevoia de atenție la sarcină",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Conservarea, clasificarea și serierea au în comun faptul că:"
        ),
        "options": [
            "presupun gândire logică organizată pe obiecte concrete",
            "implică decentrare și reguli consistente",
            "aparțin stadiului operațiilor concrete piagetiene",
            "sunt reflexe neonatale fără componentă cognitivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație rezumă cel mai bine rolul școlii în mica școlaritate?"
        ),
        "options": [
            "context pentru reguli, sarcini cognitive, socializare și strategii de învățare",
            "loc unde dispar emoțiile și atașamentul față de familie",
            "mediu fără nicio solicitare cognitivă sau socială",
            "spațiu exclusiv de joacă liberă, fără structură",
        ],
        "correct": "a",
    },
]

assert len(SCOLARITATE_ITEMS) == 40
