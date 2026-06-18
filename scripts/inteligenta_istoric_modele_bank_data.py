"""Itemi — Inteligență: istoric și modele (lot evaluare psihologică II)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

INTELIGENTA_ITEMS: List[Item] = [
    # —— Repere istorice (1–8) ——
    {
        "stem": (
            "Care a fost ipoteza centrală a lui Francis Galton despre "
            "diferențele individuale în inteligență?"
        ),
        "options": [
            "persoanele cu intelect superior au percepții și reacții mai fine",
            "eficiența perceptiv-motorie reflectă nivelul intelectual",
            "inteligența este independentă de orice reacție fiziologică",
            "măsurarea trebuie să excludă complet reacțiile fizice",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Conform modelului lui Charles Spearman, ce distinge factorul general "
            "de factorii specifici?"
        ),
        "options": [
            "factorul general influențează performanța la mai multe sarcini cognitive",
            "factorii specifici explică variația la un singur tip de sarcină",
            "factorul general există doar la testele de memorie pe termen scurt",
            "factorii specifici înlocuiesc complet factorul general",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În Primul Război Mondial, pentru recruții cu și fără competențe "
            "de citire în engleză au fost folosite forme diferite de testare. "
            "Acestea au combinat evaluarea:"
        ),
        "options": [
            "abilităților verbale, la recruții cu competențe lingvistice",
            "abilităților nonverbale, la recruții cu limite lingvistice",
            "exclusiv a memoriei pe termen lung, în ambele forme",
            "doar a vitezei motorii fine, fără componentă cognitivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Scala Wechsler-Bellevue (1939) a marcat trecerea de la un scor verbal "
            "singular la un scor global bazat pe:"
        ),
        "options": [
            "subteste verbale și de performanță",
            "combinarea mai multor domenii cognitive",
            "un singur subtest de vocabular, fără alte probe",
            "exclusiv probe proiective nestandardizate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Testarea inteligenței este considerată, în istoria psihometriei, "
            "baza evaluării psihologice standardizate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dintre cele trei procese ale modelului lui Alfred Binet și "
            "Théodore Simon (1916) vizează verificarea și revizuirea "
            "răspunsului după rezolvare?"
        ),
        "options": [
            "direcția — ce trebuie făcut în sarcină",
            "adaptarea — strategii de rezolvare",
            "controlul — verificarea și corectarea răspunsului",
            "generalizarea — aplicarea la toate domeniile vieții",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "În modelul Binet–Simon, procesul de adaptare se referă la:"
        ),
        "options": [
            "alegerea strategiilor pentru rezolvarea problemei",
            "ajustarea răspunsului la cerințele sarcinii",
            "stabilirea scopului inițial al sarcinii",
            "evaluarea finală fără posibilitate de revizuire",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Primul test de inteligență practic a fost dezvoltat de Binet și Simon "
            "pentru identificarea copiilor cu dificultăți școlare, nu pentru măsurarea "
            "„talentului” ereditar în populația generală."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Definiții Wechsler și premise WAIS (9–16) ——
    {
        "stem": (
            "Definiția lui David Wechsler din 1944 descrie inteligența ca abilitate "
            "globală de a:"
        ),
        "options": [
            "acționa intenționat în mediu",
            "gândi rațional",
            "adapta eficient la cerințele mediului",
            "reacționa reflex la stimuli, fără planificare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Definiția lui Wechsler din 1975 extinde inteligența ca funcție a:"
        ),
        "options": [
            "întregii personalități, nu doar a cogniției",
            "componentelor afective și conative, alături de cele cognitive",
            "exclusiv a vitezei de procesare senzorială",
            "potențialului genetic, independent de experiență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce a fost dezvoltată scala Wechsler pentru adulți, în locul "
            "continuării exclusive a Scalei Stanford-Binet la adulți?"
        ),
        "options": [
            "validitatea Scalei Stanford-Binet era slabă la adulți",
            "era nevoie de un instrument mai puțin verbal și mai scurt",
            "Scala Stanford-Binet era deja optimă pentru toate vârstele adulte",
            "nu exista nicio cerere clinică pentru evaluarea adulților",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care motive clinice au orientat dezvoltarea inițială a scalei Wechsler?"
        ),
        "options": [
            "evaluarea tulburărilor mentale la adulți",
            "diferențierea funcționării cognitive în context psihiatric",
            "selecția militară exclusiv pe bază de aptitudini fizice",
            "orientarea vocațională a elevilor de liceu, ca unic scop",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Wechsler considera inteligența un rezultat al interacțiunii dintre "
            "biologie și experiență, nu doar un potențial genetic fix."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Inteligența, în perspectiva Wechsler, poate fi redusă la un singur "
            "scor ereditar, fără influența mediului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care este ordinea corectă a principalelor revizii ale scalei Wechsler "
            "pentru adulți, de la Wechsler-Bellevue la versiunea recentă?"
        ),
        "options": [
            "Wechsler-Bellevue (1939) → Wechsler Adult Intelligence Scale I (1955)",
            "Wechsler Adult Intelligence Scale IV (2008) → Wechsler Adult Intelligence Scale V (2020)",
            "Wechsler Adult Intelligence Scale III (1997) înaintea versiunii Revised (1981)",
            "Wechsler Adult Intelligence Scale V (2020) înaintea versiunii IV (2008)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Wechsler Adult Intelligence Scale Revised (1981) a apărut între "
            "prima versiune Wechsler Adult Intelligence Scale (1955) și "
            "Wechsler Adult Intelligence Scale III (1997)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Stanford-Binet: istoric și SB IV (17–26) ——
    {
        "stem": (
            "Care afirmații descriu corect istoricul Scalei Stanford-Binet în Statele Unite?"
        ),
        "options": [
            "Henry Goddard a promovat testul Binet–Simon în Statele Unite",
            "traducerea în engleză a lui Kite (1908) a precedat adaptarea Stanford",
            "testul a fost creat inițial la Stanford, fără legătură cu Binet",
            "Goddard a respins complet testele franceze de inteligență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce schimbare de scorare a introdus Stanford-Binet, ediția a patra (1985), "
            "sub coordonarea lui Thorndike, Hagen și Sattler?"
        ),
        "options": [
            "coeficientul de inteligență a fost înlocuit cu scorul standard de vârstă",
            "accent pe dezvoltarea cognitivă, nu doar pe raport mental",
            "eliminarea completă a normelor de vârstă",
            "scor unic fără profile pe subteste",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care caracteristici administrative descriu Stanford-Binet, ediția a patra?"
        ),
        "options": [
            "vârste de administrare între 2 și 23 de ani",
            "durată de aproximativ 60–90 de minute",
            "15 subteste incluse în baterie",
            "administrare exclusiv în grup, fără examinator",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care niveluri compun modelul ierarhic al Stanford-Binet, ediția a patra?"
        ),
        "options": [
            "factor general la vârf",
            "abilități cristalizate: verbal și cantitativ",
            "abilități fluide-analitice și memorie pe termen scurt",
            "doar o singură dimensiune motoră, fără verbal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În administrarea adaptivă a Stanford-Binet, ediția a patra, cum se "
            "stabilește nivelul de bază după subtestul de vocabular?"
        ),
        "options": [
            "două nivele consecutive trecute definesc baza",
            "plafonul apare după trei sau patru eșecuri consecutive",
            "toți itemii se administrează indiferent de performanță",
            "nivelul de bază se stabilește doar după ultimul subtest",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care obiective de utilizare sunt asociate Stanford-Binet, ediția a patra?"
        ),
        "options": [
            "identificarea copiilor cu întârziere mentală",
            "diferențierea dificultăților de învățare de alte cauze",
            "evaluarea talentelor și a profilului clinic",
            "diagnosticul exclusiv al tulburărilor de personalitate la adulți",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Stanford-Binet, ediția a cincea (2003), dezvoltată de Roid, folosește "
            "modelul teoretic:"
        ),
        "options": [
            "Cattell–Horn–Carroll (abilități cognitive largi)",
            "doar factorul general Spearman, fără alte dimensiuni",
            "exclusiv teoria inteligențelor multiple Gardner",
            "modelul celor cinci mari factori de personalitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care caracteristici descriu Stanford-Binet, ediția a cincea (2003)?"
        ),
        "options": [
            "vârste între 2 și 85 de ani",
            "10 subteste: 5 verbale și 5 nonverbale",
            "60 de subteste obligatorii pentru fiecare persoană",
            "administrare exclusiv computerizată, fără examinator",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La Stanford-Binet, ediția a cincea (2003), în modelul "
            "Cattell–Horn–Carroll, care tipuri de abilități cognitive largi "
            "sunt evaluate?"
        ),
        "options": [
            "raționament fluid",
            "cunoștințe cristalizate",
            "raționament cantitativ",
            "procesare vizuo-spațială și memorie pe termen scurt",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Ce tipuri de scoruri oferă Stanford-Binet, ediția a cincea?"
        ),
        "options": [
            "coeficient de inteligență pe scara completă",
            "coeficient verbal și coeficient nonverbal",
            "cinci scoruri de indice pentru fiecare domeniu larg",
            "un singur scor brut, fără profile",
        ],
        "correct": "abc",
    },
    # —— WAIS-III (27–32) ——
    {
        "stem": (
            "Care caracteristici definesc Wechsler Adult Intelligence Scale III (1997)?"
        ),
        "options": [
            "vârste de administrare între 16 și 89 de ani",
            "14 subteste obligatorii pentru coeficientul de inteligență pe scara completă",
            "4 subteste obligatorii pentru coeficientul de inteligență pe scara completă",
            "norme valabile doar pentru copii sub 12 ani",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La Wechsler Adult Intelligence Scale III (1997), care tipuri de "
            "funcții cognitive erau evaluate prin indici compoziți?"
        ),
        "options": [
            "procesarea și exprimarea informației verbale",
            "organizarea perceptuală și raționamentul nonverbal",
            "memoria de lucru",
            "viteza de procesare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Efectul Flynn, relevant la revizia Wechsler Adult Intelligence Scale III, "
            "descrie în principal:"
        ),
        "options": [
            "creșterea scorurilor la teste de-a lungul generațiilor",
            "necesitatea actualizării periodice a normelor",
            "scăderea constantă a coeficientului de inteligență cu 3 puncte pe an",
            "dispariția diferențelor între grupuri culturale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care subteste au fost introduse sau consolidate la Wechsler Adult "
            "Intelligence Scale III?"
        ),
        "options": [
            "raționament matricial",
            "căutare de simboluri",
            "secvențiere cifre-litere",
            "puzzle-uri vizuale, ca subtest de bază obligatoriu",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "La Wechsler Adult Intelligence Scale III, indicele de organizare "
            "perceptuală evalua în principal abilități vizuo-spațiale și de "
            "raționament nonverbal."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Wechsler Adult Intelligence Scale III a eliminat complet toate subtestele "
            "verbale din versiunile anterioare."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— WAIS-IV: structură și indici (33–50) ——
    {
        "stem": (
            "Ce schimbări administrative aduce Wechsler Adult Intelligence Scale IV "
            "(2008), față de versiunea anterioară?"
        ),
        "options": [
            "10 subteste de bază pentru coeficientul de inteligență pe scara completă",
            "timp de administrare redus cu aproximativ 15%",
            "20 de subteste obligatorii pentru fiecare evaluare",
            "eliminarea tuturor subtestelor cu componentă verbală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce este coeficientul de aptitudine generală (General Ability Index) "
            "la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "se bazează pe indicele de comprehensiune verbală și indicele de raționament perceptual",
            "folosește 6 subteste, fără memorie de lucru și viteză de procesare",
            "este identic cu coeficientul de inteligență pe scara completă",
            "exclude orice subtest verbal din calcul",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care subteste noi au fost introduse la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "puzzle-uri vizuale",
            "greutăți figurale",
            "barare (test de cancelare)",
            "aranjare de imagini, ca subtest nou obligatoriu",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care subteste au fost eliminate la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "asamblare de obiecte",
            "aranjare de imagini",
            "cuvinte incomplete, ca subtest obligatoriu de bază",
            "întrebări generale, ca subtest obligatoriu de bază",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce Wechsler Adult Intelligence Scale IV a redus ponderea cerințelor "
            "motorii și de viteză în unele subteste?"
        ),
        "options": [
            "pentru a evita confundarea deficitelor motorii cu deficite cognitive",
            "pentru a accentua memoria de lucru și raționamentul fluid",
            "pentru a elimina complet componenta de viteză din evaluare",
            "pentru a înlocui toate probele cu itemi proiectivi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care subteste de bază compun indicele de comprehensiune verbală "
            "la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "similitudini",
            "vocabular",
            "informații generale",
            "design cu cuburi",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care subteste de bază compun indicele de raționament perceptual "
            "la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "design cu cuburi",
            "raționament matricial",
            "puzzle-uri vizuale",
            "secvențiere cifre",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care subteste de bază compun indicele de memorie de lucru "
            "la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "secvențiere cifre",
            "aritmetică",
            "căutare de simboluri",
            "vocabular",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care subteste de bază compun indicele de viteză de procesare "
            "la Wechsler Adult Intelligence Scale IV?"
        ),
        "options": [
            "căutare de simboluri",
            "codare (transcriere de simboluri)",
            "aritmetică",
            "informații generale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un adult obține scor scăzut la indicele de memorie de lucru, dar scor "
            "mediu la indicele de comprehensiune verbală. Interpretarea cea mai "
            "adecvată presupune:"
        ),
        "options": [
            "profil diferențiat, nu un deficit global uniform",
            "analiza subtestelor care compun memoria de lucru",
            "respingerea automată a validității întregii evaluări",
            "concluzia că toate abilitățile cognitive sunt egale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Coeficientul de aptitudine generală de la Wechsler Adult Intelligence "
            "Scale IV este util când deficitele motorii sau de viteză ar putea "
            "scădea artificial coeficientul de inteligență pe scara completă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La Wechsler Adult Intelligence Scale IV, indicele de viteză de procesare "
            "măsoară în principal cunoștințele culturale acumulate pe termen lung."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Comparând Stanford-Binet, ediția a cincea, cu Wechsler Adult Intelligence "
            "Scale IV, care diferență este corectă?"
        ),
        "options": [
            "Stanford-Binet, ediția a cincea, acoperă o plajă largă de vârstă, inclusiv copii mici",
            "Wechsler Adult Intelligence Scale IV este orientată spre adulți și adolescenți",
            "ambele folosesc exact aceleași 15 subteste obligatorii",
            "doar Stanford-Binet oferă scoruri de indice",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce legătură există între modelul Cattell–Horn–Carroll și structura "
            "Stanford-Binet, ediția a cincea?"
        ),
        "options": [
            "cele cinci domenii largi corespund unor abilități cognitive distincte",
            "scorurile de indice reflectă constructe precum raționamentul fluid și cunoștințele cristalizate",
            "modelul exclude complet factorul general",
            "modelul înlocuiește nevoia de norme de vârstă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În evaluarea clinică, de ce este importantă cunoașterea istoricului și "
            "a structurii scalei Wechsler folosite?"
        ),
        "options": [
            "reviziile diferă la numărul de subteste și la indici",
            "interpretarea trebuie aliniată la manualul versiunii administrate",
            "toate versiunile au aceleași norme și aceleași subteste obligatorii",
            "versiunea administrată nu influențează raportul clinic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Testele moderne de inteligență, precum Wechsler Adult Intelligence Scale IV "
            "și Stanford-Binet, ediția a cincea, oferă atât un scor global, cât și "
            "profile pe indici sau domenii cognitive."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Army Beta a fost conceput pentru recruți care aveau dificultăți cu "
            "limba engleză, oferind o formă mai nonverbală de evaluare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "De ce administrarea adaptivă la Stanford-Binet, ediția a patra, "
            "începe frecvent cu subtestul de vocabular?"
        ),
        "options": [
            "oferă o estimare rapidă a nivelului general",
            "permite stabilirea nivelului de bază și a plafonului",
            "elimină administrarea celorlalte subteste",
            "înlocuiește normele de vârstă cu interviul clinic",
        ],
        "correct": "ab",
    },
]
