"""Itemi — Interese (Curs 11), lot evaluare psihologică II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

INTERESE_ITEMS: List[Item] = [
    # —— Definiții (1–10) ——
    {
        "stem": (
            "Conform lui James Rounds și Rong Su, interesele sunt preferințe "
            "asemănătoare trăsăturilor pentru activități sau contexte care:"
        ),
        "options": [
            "vizează domenii sau sarcini cu semnificație personală",
            "motivează comportament orientat spre obiective",
            "sunt identice cu abilitățile cognitive măsurate la un test de aptitudine",
            "exclud complet influența alegerilor individuale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În literatura despre interese, atitudinea se referă în principal la "
            "nevoia sau dorința de:"
        ),
        "options": [
            "atenție selectivă la aspecte cu semnificație personală",
            "orientare către conținuturi sau activități relevante pentru sine",
            "evitarea oricărei evaluări a propriilor preferințe",
            "atenție egală la toți stimulii, indiferent de relevanță",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine interesele ca construct "
            "motivațional?"
        ),
        "options": [
            "sunt intrinseci și specifici conținutului sau activității",
            "sunt pur biologice, fără componentă psihologică sau de dezvoltare",
            "sunt identice cu orice stimul extern de recompensă",
            "sunt interese generale, abstracte, fără legătură cu un domeniu concret",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Întrebarea „Ce vrei să faci când te faci mare?” ilustrează în "
            "evaluarea intereselor orientarea către:"
        ),
        "options": [
            "preferințe relativ stabile pentru domenii de activitate sau carieră",
            "măsurarea exclusivă a memoriei pe termen scurt",
            "lipsa componentei motivaționale în modelul descris",
            "doar reacții situaționale la un singur stimul captivant",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Interesele se aseamănă trăsăturilor de personalitate prin faptul că "
            "sunt relativ stabile în timp, dar diferă prin orientarea lor spre "
            "obiecte sau activități concrete."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Interesele sunt doar stări situaționale trecătoare, fără nicio "
            "componentă relativ stabilă comparabilă trăsăturilor."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care dintre următoarele caracterizează corect interesele, spre "
            "deosebire de simple reacții reflexe?"
        ),
        "options": [
            "pot fi relativ stabile, asemănător trăsăturilor",
            "sunt orientate contextual spre un obiect sau o activitate concretă",
            "joacă un rol în motivație și în alegerile individuale",
            "sunt complet independente de context și de conținut",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În studiul intereselor, distincția fundamentală este între:"
        ),
        "options": [
            "stări situaționale, cum ar fi curiozitatea de moment",
            "dispoziții stabile, orientate spre domenii sau activități",
            "doar factori genetici, fără influență a mediului",
            "interese măsurate prin teste de viteză perceptivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un elev simte curiozitate doar în timpul unui experiment captivant, "
            "dar în rest nu manifestă interes pentru știință. Aceasta ilustrează "
            "mai ales:"
        ),
        "options": [
            "interesul situațional",
            "interesul individual bine dezvoltat",
            "lipsa componentei afective în modelul explicat",
            "o dispoziție stabilă pentru domeniul științific",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un adolescent care de ani de zile citește despre biologie, alege "
            "opționale în domeniu și își imaginează o carieră în cercetare "
            "manifestă mai ales:"
        ),
        "options": [
            "o dispoziție stabilă de interes pentru un domeniu concret",
            "doar curiozitate declanșată de un singur stimul izolat",
            "lipsa oricărei legături cu alegerile individuale",
            "interes situațional declanșat de un experiment unic",
        ],
        "correct": "a",
    },
    # —— Rolul intereselor (11–20) ——
    {
        "stem": (
            "Care beneficii ale intereselor în procesul de învățare sunt "
            "susținute de literatura de specialitate?"
        ),
        "options": [
            "susțin învățarea profundă, nu doar memorarea superficială",
            "beneficiază atenția, memoria, motivația și implicarea",
            "favorizează explorarea voluntară a conținutului",
            "susțin alegeri individuale legate de parcurs educațional",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Interesele implică componente afective și cognitive care:"
        ),
        "options": [
            "funcționează ca sisteme distincte, dar care interacționează",
            "sunt mereu identice și indistinguibile în practică",
            "exclud complet orice procesare cognitivă",
            "depind doar de recompense externe materiale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Interesul pentru un domeniu este rezultatul interacțiunii dintre:"
        ),
        "options": [
            "caracteristicile persoanei și proprietățile conținutului sau activității",
            "doar factori biologici, fără influența mediului sau a experienței",
            "un scor unic de aptitudine, independent de preferințe",
            "contextul social, fără nicio influență a conținutului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Conform lui Suzanne Hidi și K. Ann Renninger, interesele pot fi "
            "dezvoltate în timp prin experiențe repetate și susținere contextuală."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Interesele sunt fixe de la naștere și nu pot fi cultivate prin "
            "experiență educațională sau prin provocări graduale."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce beneficiază memoria atunci când interesul pentru conținut "
            "este ridicat?"
        ),
        "options": [
            "atenția selectivă filtrează informația relevantă",
            "implicarea emoțională și cognitivă susține codarea și reținerea",
            "interesul reduce nevoia de repetiție sau de practică",
            "memoria nu este influențată de interese, doar de aptitudine",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un student urmărește un curs nu doar pentru notă, ci pentru că "
            "subiectul îi trezește plăcere și dorința de a aprofunda. Aceasta "
            "reflectă rolul intereselor în:"
        ),
        "options": [
            "motivație intrinsecă orientată spre conținut",
            "eliminarea oricărei componente cognitive",
            "absența alegerilor individuale",
            "motivație extrinsecă bazată pe recompense",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație descrie corect relația dintre componenta afectivă "
            "și cea cognitivă a interesului?"
        ),
        "options": [
            "sunt sisteme separate care se influențează reciproc",
            "componenta cognitivă exclude orice emoție",
            "doar una dintre componente contează în dezvoltarea interesului",
            "afectul și cogniția sunt mereu identice și indistinguibile",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Interacțiunea persoană–conținut în formarea interesului înseamnă că:"
        ),
        "options": [
            "același material poate trezi interes la unii elevi, nu la alții",
            "interesul depinde doar de dificultatea maximă a sarcinii",
            "conținutul nu contează dacă elevul are aptitudine înaltă",
            "toți elevii reacționează identic la aceeași lecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Ce proces cognitiv este facilitat în primul rând când interesul "
            "pentru o temă este ridicat?"
        ),
        "options": [
            "atenția selectivă la informația relevantă",
            "evitarea oricărei procesări profunde",
            "reducerea motivației pentru explorare",
            "memorarea mecanică fără înțelegere",
        ],
        "correct": "a",
    },
    # —— Modelul în patru faze Hidi & Renninger (21–32) ——
    {
        "stem": (
            "Care este prima fază din modelul de dezvoltare a interesului "
            "propus de Suzanne Hidi și K. Ann Renninger?"
        ),
        "options": [
            "interesul situațional declanșat",
            "interesul individual bine dezvoltat",
            "interesul situațional susținut",
            "interesul individual emergent",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care este ordinea corectă a fazelor din modelul Hidi și Renninger?"
        ),
        "options": [
            "declanșat → susținut → individual emergent → individual bine dezvoltat",
            "susținut → declanșat → individual emergent → individual bine dezvoltat",
            "declanșat → individual emergent → susținut → individual bine dezvoltat",
            "individual bine dezvoltat → individual emergent → susținut → declanșat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Ce caracterizează faza „interesului situațional declanșat”?"
        ),
        "options": [
            "apariția curiozității sau a atenției datorită unui stimul captivant",
            "deja o identitate stabilă de „pasionat” al domeniului",
            "lipsa componentei afective în modelul explicat",
            "cunoștințe consolidate și valoare personală profundă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Interesul situațional susținut se diferențiază de cel declanșat "
            "prin faptul că:"
        ),
        "options": [
            "persistă dincolo de stimulul inițial, în context educațional",
            "reprezintă deja interes individual bine consolidat",
            "nu necesită implicarea profesorului sau a mediului",
            "apare doar o dată, la primul contact cu materia",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Ce descrie faza „interesului individual emergent”?"
        ),
        "options": [
            "apariția unei preferințe personale pentru domeniu",
            "doar reacția la un singur truc sau stimul izolat",
            "lipsa oricărei valori personale atribuite domeniului",
            "lipsa repetării voluntare a activității în model",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Interesul individual bine dezvoltat implică în principal:"
        ),
        "options": [
            "valoare personală atribuită activității și cunoștințe consolidate",
            "doar curiozitate trecătoare, fără angajament",
            "absența efortului sau a provocărilor",
            "reacție la un singur stimul captivant, de scurtă durată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care elemente sunt necesare pentru trecerea spre interesul individual "
            "bine dezvoltat, conform modelului Hidi și Renninger?"
        ),
        "options": [
            "componenta afectivă",
            "cunoștințe despre domeniu",
            "valoare personală percepută",
            "doar recompense externe, fără implicare cognitivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dezvoltarea interesului poate fi susținută de efortul altora "
            "(profesori, colegi) și de provocări adecvate nivelului elevului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În modelul în patru faze, interesul individual emergent apare "
            "înaintea interesului situațional susținut."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un elev care revine voluntar la bibliotecă pentru aceeași temă, "
            "după ce profesorul a menținut activități captivante timp de săptămâni, "
            "se apropie de faza:"
        ),
        "options": [
            "interesului individual emergent",
            "interesului situațional declanșat izolat",
            "absenței oricărui interes",
            "interesului individual bine dezvoltat deja consolidat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un cercetător adult care investește ani în domeniu, își asumă "
            "provocări dificile și atribuie domeniului valoare personală "
            "profundă ilustrează:"
        ),
        "options": [
            "interesul individual bine dezvoltat",
            "doar interes situațional declanșat de un stimul unic",
            "lipsa oricărei dispoziții stabile",
            "interes situațional susținut, ca fază inițială",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care factor favorizează cel mai direct trecerea de la interes "
            "situational la interes individual, conform modelului Hidi și Renninger?"
        ),
        "options": [
            "provocări graduale și feedback în context educațional",
            "context educațional care menține implicarea",
            "izolarea completă a elevului de orice suport social",
            "recompense externe fără implicare în conținut",
        ],
        "correct": "ab",
    },
    # —— Holland RIASEC (33–42) ——
    {
        "stem": (
            "Modelul Holland clasifică interesele vocaționale în șase tipuri "
            "fundamentale (acronim RIASEC). Care dintre următoarele NU este un "
            "astfel de tip de interes?"
        ),
        "options": [
            "realistic — lucrul practic cu obiecte, mașini sau natură",
            "investigativ — cercetare, analiză, rezolvare de probleme",
            "artistic — expresie creativă, estetică, originalitate",
            "coeficient de inteligență generală măsurat la un test cognitiv",
        ],
        "correct": "d",
    },
    {
        "stem": (
            "În modelul Holland, tipul de interes „social” se caracterizează "
            "prin preferința pentru:"
        ),
        "options": [
            "ajutorarea, învățarea sau consilierea altor persoane",
            "activități de relaționare și cooperare",
            "lucrul izolat cu date tehnice, fără contact uman",
            "organizarea strictă a documentelor, fără interacțiune",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tipul de interes „antreprenorial” (enterprising) în modelul Holland "
            "vizează preferința pentru:"
        ),
        "options": [
            "conducere, persuasiune și inițiativă",
            "vânzare, negociere sau influențare",
            "activități repetitive de birou, fără asumare de risc",
            "cercetare de laborator izolată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tipul de interes „convențional” în modelul Holland se asociază cu:"
        ),
        "options": [
            "organizare, ordine și respectarea regulilor",
            "lucrul structurat cu date, înregistrări sau proceduri",
            "expresie artistică liberă, fără structură",
            "explorare științifică neconvențională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele enumeră combinații valide de tipuri din "
            "acronimul RIASEC al modelului Holland?"
        ),
        "options": [
            "Realistic, Investigativ, Artistic",
            "Social, Antreprenorial, Convențional",
            "Romantic, Intuitiv, Analitic",
            "Extrovertit, Agresiv, Conformist",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Modelul Holland sugerează că potrivirea între tipul de interes "
            "al persoanei și mediul de lucru influențează satisfacția și "
            "performanța vocațională."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În modelul Holland, tipurile de interes sunt complet independente "
            "unul de altul, fără posibilitate de combinații sau proximitate "
            "între ele."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un adolescent atras de repararea bicicletelor, construcții practice "
            "și activități în aer liber are profil dominant de interes:"
        ),
        "options": [
            "realistic",
            "artistic-expresiv",
            "convențional-birocratic",
            "investigativ-analitic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un tânăr pasionat de experimente, teorie și analiză de date "
            "se potrivește mai ales tipului de interes:"
        ),
        "options": [
            "investigativ",
            "social-relational",
            "convențional-administrativ",
            "realistic-practic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce este util modelul Holland în consilierea vocațională?"
        ),
        "options": [
            "ajută la potrivirea persoană–mediu profesional",
            "măsoară direct performanța la locul de muncă, fără alte variabile",
            "exclude rolul intereselor în alegerile de carieră",
            "suplimentează interviul clinic de consiliere, nu îl înlocuiește",
        ],
        "correct": "a",
    },
    # —— Interes–abilitate și emoții epistemice (43–50) ——
    {
        "stem": (
            "Conform lui Phillip Ackerman (1996) și John Holland (1973), relația "
            "dintre interese și abilități este:"
        ),
        "options": [
            "reciprocă — interesele și abilitățile se susțin mutual",
            "interesele pot orienta investiția de timp care dezvoltă abilități",
            "abilitățile nu influențează niciodată formarea intereselor",
            "interesele înlocuiesc complet nevoia de practică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Lanțul influenței intereselor asupra parcursului profesional include, "
            "în mod tipic:"
        ),
        "options": [
            "alegeri la liceu",
            "alegeri la facultate și în carieră",
            "performanța la locul de muncă",
            "doar rezultate la teste de memorie pe termen scurt, fără legătură vocațională",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele emoții sunt legate de căutarea și "
            "procesarea cunoașterii, nu de agresiune interpersonală?"
        ),
        "options": [
            "curiozitatea",
            "interesul",
            "surpriza",
            "furie agresivă orientată spre pedepsire",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Surpriza, ca emoție epistemică, apare când există o discrepanță "
            "între așteptare și realitate și poate declanșa învățare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Emoțiile epistemice sunt complet separate de procesarea cognitivă "
            "și nu influențează explorarea sau învățarea."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Ce descrie studiul MagicCATs (Ozono și colaboratorii, 2020) despre "
            "curiozitatea experimentală?"
        ),
        "options": [
            "măsurarea curiozității într-un cadru experimental controlat",
            "utilizarea de stimuli nonverbali, cum ar fi trucuri de magie",
            "măsurarea exclusivă a intereselor vocaționale prin interviu clinic",
            "demonstrarea că surpriza inhibă orice învățare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un elev care se miră când un experiment iese diferit de predicție "
            "și apoi caută explicații manifestă legătura dintre:"
        ),
        "options": [
            "surpriză epistemică și discrepanță așteptare–realitate",
            "lipsa oricărei curiozități cognitive",
            "interes convențional pentru birocrație",
            "tip de interes realistic din modelul Holland",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Integrarea perspectivei Holland, a modelului Hidi și Renninger și "
            "a emoțiilor epistemice permite în principal:"
        ),
        "options": [
            "o imagine completă a interesului în învățare și în alegeri vocaționale",
            "reducerea interesului la un singur scor de aptitudine",
            "consiliere vocațională bazată doar pe profilul RIASEC, fără context școlar",
            "înlocuirea evaluării psihologice cu un singur test cognitiv",
        ],
        "correct": "ab",
    },
]
