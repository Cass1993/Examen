"""Itemi — Introducere în evaluarea psihologică II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

EVALUARE_ITEMS: List[Item] = [
    # —— Necesitatea evaluării (1–5) ——
    {
        "stem": "Evaluarea psihologică răspunde, în principal, nevoii de:",
        "options": [
            "decizii informate privind diferențele individuale",
            "decizii cât mai obiective, pe baza datelor sistematice",
            "descrierea aleatoare a comportamentului, fără standarde",
            "eliminarea oricărei variabilități individuale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Conform definiției lui Urbina, testele psihometrice sunt proceduri "
            "sistematice care eșantionează comportamente relevante pentru:"
        ),
        "options": [
            "funcționarea cognitivă",
            "funcționarea afectivă",
            "orice comportament, indiferent de relevanță",
            "doar performanța fizică, fără componentă psihologică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un element esențial al testelor psihometrice este evaluarea după "
            "standarde explicite, nu după impresii nesistematice."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Evaluarea psihologică înlocuiește complet judecata clinică sau "
            "organizațională, fără a mai fi nevoie de context."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Prin ce se realizează compararea rezultatelor între persoane sau "
            "între momente diferite în evaluarea sistematică?"
        ),
        "options": [
            "standardizarea administrării și a baremului",
            "replicabilitatea deciziilor între evaluatori",
            "reducerea subiectivității prin proceduri standardizate, nu eliminarea ei",
            "prioritizarea unui singur instrument standardizat, fără triangulare",
        ],
        "correct": "ab",
    },
    # —— Domenii aplicative (6–12) ——
    {
        "stem": "În domeniul clinic, evaluarea psihologică poate avea scopuri de:",
        "options": [
            "diagnostic și formulare de ipoteze clinice",
            "prognostic și monitorizare a evoluției",
            "validare a intervențiilor, inclusiv prin design de tip test–retest",
            "screening rapid pe baza unui singur interviu nestructurat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Exemple de instrumente folosite frecvent în evaluarea clinică:",
        "options": [
            "Inventarul Multifazic de Personalitate Minnesota",
            "Inventarul Clinic Multiaxial Millon",
            "Testul de pată de cerneală Rorschach, ca instrument proiectiv",
            "Scala de inteligență pentru copii, ca singur instrument obligatoriu",
        ],
        "correct": "abc",
    },
    {
        "stem": "În domeniul organizațional, evaluarea urmărește adesea:",
        "options": [
            "selecția pe baza performanței prezente sau viitoare",
            "relația dintre variabila de predicție și criteriul de performanță",
            "utilizarea centrelor de evaluare a competențelor",
            "orientarea vocațională a elevilor de liceu",
        ],
        "correct": "abc",
    },
    {
        "stem": "În domeniul educațional, evaluarea psihologică poate sprijini:",
        "options": [
            "orientarea vocațională și consilierea școlară",
            "identificarea maladaptării sau a dificultăților de învățare",
            "selecția managerială în companii private",
            "clasificarea tulburărilor de învățare fără evaluare psihologică",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce include scopul prognostic în evaluarea clinică?",
        "options": [
            "estimarea cursului posibil al unei probleme",
            "identificarea factorilor de risc sau de protecție",
            "descrierea simptomelor actuale, fără estimarea evoluției",
            "înlocuirea diagnosticului prin etichetare statică",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce metode pot combina centrele de evaluare a competențelor?",
        "options": [
            "simulări de lucru și exerciții structurate",
            "interviu și teste standardizate",
            "o singură probă scrisă, fără observare comportamentală",
            "chestionare de personalitate aplicate fără criteriu de job",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Validarea unei intervenții clinice prin design de tip test–retest presupune:"
        ),
        "options": [
            "administrarea aceluiași instrument în momente diferite",
            "compararea rezultatelor înainte și după intervenție",
            "utilizarea unui instrument diferit la fiecare administrare",
            "absența oricărui criteriu de schimbare în timp",
        ],
        "correct": "ab",
    },
    # —— Predictor–criteriu și erori (13–24) ——
    {
        "stem": (
            "În tabelul predictor–criteriu, combinațiile corecte sau dezirabile "
            "pentru selecție includ:"
        ),
        "options": [
            "scor înalt la test și performanță înaltă la criteriu",
            "scor scăzut la test și performanță scăzută la criteriu",
            "scor înalt la test și performanță scăzută la criteriu",
            "scor scăzut la test și performanță înaltă la criteriu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un candidat obține scor înalt la test, dar are performanță scăzută "
            "la locul de muncă. Aceasta reprezintă:"
        ),
        "options": [
            "o predicție pozitivă greșită în selecție",
            "eroarea echivalentă erorii de tip I în selecție",
            "respingerea unei persoane potrivite",
            "validitate predictivă ideală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un candidat obține scor scăzut la test, dar ar fi avut performanță "
            "înaltă dacă ar fi fost angajat. Aceasta reprezintă:"
        ),
        "options": [
            "o predicție negativă greșită în selecție",
            "eroarea echivalentă erorii de tip II în selecție",
            "angajarea unei persoane nepotrivite",
            "corespondență perfectă predictor–criteriu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În selecție, respingerea unui candidat cu scor scăzut la test care "
            "ar fi avut performanță slabă este, în general, o decizie corectă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În selecție, respingerea unui candidat cu scor scăzut la test care "
            "ar fi avut performanță bună reprezintă o eroare de tip I."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Eroarea de tip I, în testarea ipotezelor, înseamnă:",
        "options": [
            "respingerea ipotezei nule când ipoteza nulă este adevărată",
            "concluzionarea că există un efect care, de fapt, nu există",
            "acceptarea ipotezei nule când ipoteza nulă este falsă",
            "raterea unui efect real",
        ],
        "correct": "ab",
    },
    {
        "stem": "Eroarea de tip II, în testarea ipotezelor, înseamnă:",
        "options": [
            "acceptarea ipotezei nule când ipoteza nulă este falsă",
            "raterea unui efect sau a unei diferențe reale",
            "respingerea ipotezei nule când ipoteza nulă este adevărată",
            "concluzionarea falsă că există un efect",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă un test de selecție este făcut foarte strict pentru a evita "
            "angajările greșite, consecința frecventă este:"
        ),
        "options": [
            "scăderea erorilor de tip I în selecție",
            "creșterea erorilor de tip II în selecție",
            "reducerea ambelor tipuri de erori simultan, fără compromis",
            "dispariția necesității unui criteriu de performanță",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă un test de selecție este foarte permisiv și angajează aproape "
            "pe toată lumea, consecința frecventă este:"
        ),
        "options": [
            "creșterea erorilor de tip I în selecție",
            "scăderea erorilor de tip II în selecție",
            "absența oricărei angajări greșite",
            "validitate predictivă garantată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce indică un coeficient de corelație apropiat de zero între test și criteriu?"
        ),
        "options": [
            "scorul la test nu se leagă semnificativ de performanță",
            "deciziile bazate pe test pot semăna cu un proces aleatoriu",
            "testul prezice perfect performanța la criteriu",
            "relația predictor–criteriu este ideală pentru selecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care combinație descrie corect relația dintre eroare, selecție și ipoteză?"
        ),
        "options": [
            "tip I — respingerea ipotezei nule când aceasta este adevărată",
            "tip II — acceptarea ipotezei nule când aceasta este falsă",
            "în selecție: scor înalt + performanță slabă ≈ eroare de tip I",
            "în selecție: scor scăzut + performanță înaltă ≈ eroare de tip I",
        ],
        "correct": "abc",
    },
    # —— Cantitativ versus calitativ; obiectiv versus subiectiv (25–36) ——
    {
        "stem": (
            "Metodele cantitative de evaluare se caracterizează, în general, prin:"
        ),
        "options": [
            "date numerice și comparabilitate între persoane",
            "reguli explicite de administrare și notare",
            "explorarea liberă a sensurilor, fără barem",
            "accent pe impresia clinică a evaluatorului, fără barem",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Metodele calitative de evaluare se caracterizează, în general, prin:"
        ),
        "options": [
            "accent exploratoriu și contextual",
            "interviu, observație sau grup focal",
            "scoruri standardizate obligatorii pentru fiecare răspuns",
            "lipsa oricărei interpretări umane",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Metodele cantitative sunt întotdeauna mai valide decât metodele "
            "calitative, indiferent de scopul evaluării."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Cum poate arăta combinarea metodelor cantitative și calitative într-o evaluare?"
        ),
        "options": [
            "teste standardizate plus interviu clinic",
            "chestionar numeric plus observație sistematică",
            "o singură metodă standardizată, fără triangulare",
            "doar tehnici proiective, fără criterii explicite",
        ],
        "correct": "ab",
    },
    {
        "stem": "Un rezultat obiectiv în evaluare este acela care:",
        "options": [
            "nu depinde de interpretarea unui singur evaluator",
            "poate fi reprodus de alți evaluatori folosind aceleași reguli",
            "depinde de impresia clinică a unui singur evaluator",
            "nu poate fi niciodată cuantificat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care exemple ilustrează un rezultat subiectiv în evaluare?",
        "options": [
            "interpretarea liberă a unor subteste deschise",
            "analiza proiectivă fără barem fix",
            "notarea automată a unui test cu răspunsuri închise",
            "scorul obținut la un test de aptitudini cu cheie unică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Unele subteste deschise de la scala de inteligență Wechsler pentru "
            "adulți pot avea o componentă subiectivă în notare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "De ce chestionarele standardizate cu barem fix sunt mai obiective "
            "decât interviul nestructurat?"
        ),
        "options": [
            "notarea urmează reguli explicite",
            "rezultatul este mai puțin dependent de un singur evaluator",
            "reduce nevoia de validare prin standardizare",
            "sunt întotdeauna calitative, nu cantitative",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care pereche distinge corect o metodă cantitativă de una calitativă?"
        ),
        "options": [
            "test de aptitudini — scor numeric standardizat",
            "grup focal — discuție exploratorie structurată",
            "interviu nestructurat — colectare de date contextuale",
            "observația sistematică cu barem — metodă mixtă cantitativ-calitativă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce instrumentele psihometrice și chestionarele standardizate sunt "
            "încadrate, de regulă, la metode cantitative?"
        ),
        "options": [
            "produc scoruri comparabile între persoane",
            "folosesc proceduri sistematice de administrare",
            "exclud orice formă de cuantificare",
            "sunt identice cu tehnicile proiective nestandardizate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce tehnicile proiective au adesea o componentă calitativă și subiectivă?"
        ),
        "options": [
            "interpretarea depinde de formarea evaluatorului",
            "stimulii ambigui invită la elaborare personală",
            "baremul este adesea parțial automatizat, nu integral",
            "rezultatul este independent de contextul clinic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Cum poate observația sistematică cu fișă de codare produce date cantitative?"
        ),
        "options": [
            "frecvențe sau durate înregistrate pe categorii prestabilite",
            "posibilitatea comparării între observații sau persoane",
            "imposibilitatea oricărei cuantificări a comportamentului",
            "lipsa oricărui protocol sau a oricărei fișe de observare",
        ],
        "correct": "ab",
    },
    # —— Etic versus emic (37–44) ——
    {
        "stem": "Abordarea etică în evaluare presupune:",
        "options": [
            "construcții considerate universale, comparabile între culturi",
            "utilizarea unor modele transversale, cum ar fi modelul celor cinci mari factori",
            "instrumente create doar pentru o singură cultură, fără comparabilitate",
            "respingerea oricărei standardizări",
        ],
        "correct": "ab",
    },
    {
        "stem": "Abordarea emică în evaluare presupune:",
        "options": [
            "construcții și instrumente specifice unei culturi",
            "dezvoltarea de măsuri indigene, nu doar traduse în mod mecanic",
            "aplicarea identică a unui test fără adaptare culturală",
            "interpretarea scorurilor cu bareme internaționale nemodificate local",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Abordarea etică presupune dezvoltarea exclusivă de măsuri indigene "
            "pentru fiecare cultură, fără comparabilitate între grupuri."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Abordarea emică presupune înțelegerea comportamentului în logica "
            "proprie culturii, nu doar aplicarea mecanică a unui test tradus."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmații descriu corect abordarea etică, nu pe cea emică?"
        ),
        "options": [
            "comparabilitate cross-culturală între grupuri",
            "utilizarea constructelor considerate universale",
            "măsuri dezvoltate local, fără validare în altă cultură",
            "accent pe sensurile specifice unei singure comunități",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații descriu corect abordarea emică, nu pe cea etică?"
        ),
        "options": [
            "instrumente adaptate culturii în care sunt folosite",
            "validare locală, nu doar traducere literală",
            "aplicarea identică a unui test occidental peste tot",
            "respingerea contextului cultural al comportamentului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un cercetător aplică în România un inventar de personalitate tradus "
            "literal, fără studii de validare locală. Riscul principal este:"
        ),
        "options": [
            "compararea directă a scorurilor între culturi fără validare locală",
            "interpretarea greșită a unor itemi sau construcții",
            "comparabilitate perfectă cu toate culturile",
            "eliminarea automată a erorilor de măsurare",
        ],
        "correct": "ab",
    },
    {
        "stem": "De ce modelul celor cinci mari factori este asociat cu abordarea etică?",
        "options": [
            "permite comparații între grupuri culturale diferite",
            "operează cu construcții considerate relativ universale",
            "exclude nevoia de adaptare locală în orice situație",
            "suplimentează, nu înlocuiește, metodele calitative de explorare",
        ],
        "correct": "ab",
    },
    # —— Surse multiple și sinteză (45–50) ——
    {
        "stem": "Strategia multimodală în evaluare presupune:",
        "options": [
            "combinarea interviului, observației și testelor",
            "verificarea convergenței între metode diferite",
            "utilizarea unei singure metode pentru toate deciziile",
            "modelul multitraită-multimetodă al lui Campbell și Fiske",
        ],
        "correct": "abd",
    },
    {
        "stem": "Strategia cu mai mulți evaluatori presupune:",
        "options": [
            "colectarea datelor de la mai mulți informatori",
            "evaluarea din perspectiva a trei sute șaizeci de grade, în context organizațional",
            "raportarea doar de către persoana evaluată",
            "combinarea perspectivei părinților și a profesorilor, în context școlar",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care este scopul modelului multitraită-multimetodă al lui Campbell și Fiske?"
        ),
        "options": [
            "aceeași trăsătură măsurată prin metode diferite",
            "metode diferite pentru a verifica dacă măsoară același construct",
            "o singură metodă, fără verificare încrucișată",
            "confundarea permanentă a metodei cu trăsătura reală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un psiholog organizează un interviu semi-structurat pentru a înțelege "
            "experiența unui adolescent, apoi aplică un chestionar standardizat "
            "pentru a compara scorul cu normele. Aceasta ilustrează:"
        ),
        "options": [
            "combinarea metodelor calitative și cantitative",
            "triangularea datelor din surse și metode diferite",
            "aplicarea unei abordări etice fără adaptare emică locală",
            "renunțarea la orice standardizare sau comparabilitate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În evaluarea clinică, un inventar de personalitate poate fi foarte util, "
            "dar nu înlocuiește singur interviul și observarea clinică."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Cum reduce o evaluare cu surse multiple părtinirea unei singure metode?"
        ),
        "options": [
            "interviu plus teste plus observație",
            "date de la mai mulți informatori sau evaluatori",
            "o singură probă, administrată o singură dată",
            "auto-raportarea fără verificare din observație sau interviu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un inventar de personalitate standardizat poate înlocui complet "
            "interviul clinic, observarea și contextul, fără pierdere de informație."
        ),
        "tf": True,
        "correct_tf": False,
    },
]

from scripts.perspectiva_psihometrica_bank_data import PSIHOMETRIC_ITEMS

EVALUARE_ITEMS.extend(PSIHOMETRIC_ITEMS)

from scripts.inteligenta_istoric_modele_bank_data import INTELIGENTA_ITEMS

EVALUARE_ITEMS.extend(INTELIGENTA_ITEMS)

from scripts.inteligenta_emotionala_bank_data import INTELIGENTA_EMOTIONALA_ITEMS

EVALUARE_ITEMS.extend(INTELIGENTA_EMOTIONALA_ITEMS)

from scripts.motivatie_bank_data import MOTIVATIE_ITEMS

EVALUARE_ITEMS.extend(MOTIVATIE_ITEMS)

from scripts.interese_bank_data import INTERESE_ITEMS

EVALUARE_ITEMS.extend(INTERESE_ITEMS)

from scripts.jvis_bank_data import JVIS_ITEMS

EVALUARE_ITEMS.extend(JVIS_ITEMS)
