"""Itemi — Performanța în muncă, lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PERFORMANTA_MUNCII_ITEMS: List[Item] = [
    # —— Definiție, comportamente + rezultate (1–6) ——
    {
        "stem": (
            "În psihologia muncii, performanța la job include atât comportamentele "
            "prestate, cât și rezultatele obținute — nu doar cifrele finale de "
            "productivitate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre performanța în muncă este cea mai precisă?"
        ),
        "options": [
            "performanța combină modul în care lucrezi (comportamente) cu ce "
            "producești (rezultate)",
            "performanța se reduce la obiectivele atinse, indiferent de "
            "comportamentul de pe parcurs",
            "rezultatele singure sunt suficiente dacă șeful este mulțumit de cifre",
            "comportamentele la job nu contează dacă vânzările sunt mari",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un vânzător atinge cota lunară, dar ignoră procedurile de raportare și "
            "refuză să ajute colegii noi. Conform definiției largi a performanței, "
            "evaluarea lui ar trebui să ia în calcul:"
        ),
        "options": [
            "rezultatul la cota de vânzări",
            "comportamentele de colaborare și respectarea procedurilor, nu doar cifra",
            "doar numărul de contracte, deoarece rezultatul anulează comportamentul",
            "exclusiv feedback-ul informal al colegilor, fără rezultate obiective",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce nu este suficient să măsori performanța doar prin rezultate "
            "finale (ex. piese produse, vânzări)?"
        ),
        "options": [
            "același rezultat poate veni din comportamente diferite (corecte vs "
            "scurtături)",
            "comportamentele explică cum s-a ajuns la rezultat și ce se poate "
            "susține pe termen lung",
            "rezultatele singure captează automat și comportamentele de cetățenie "
            "organizațională (OCB)",
            "factori externi pot influența rezultatul fără a reflecta calitatea "
            "muncii individuale",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care exemple ilustrează componenta de comportament, respectiv de "
            "rezultat, în performanța la muncă?"
        ),
        "options": [
            "respectarea procedurilor de siguranță",
            "numărul de erori raportate la sfârșitul lunii",
            "modul de comunicare cu clienții",
            "cota de vânzări atinsă",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Performanța la muncă se definește exclusiv prin rezultatele cantitative "
            "măsurate obiectiv, fără componentă comportamentală."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Criteriu, relevance, deficiency, contamination (7–14) ——
    {
        "stem": (
            "În evaluarea performanței, distincția dintre criteriu teoretic (ideal) "
            "și criteriu efectiv (măsurat) se referă la:"
        ),
        "options": [
            "ce ar trebui măsurat ideal vs ce măsurăm de fapt în practică",
            "scorul la selecție vs performanța după angajare",
            "performanța la sarcină vs performanța contextuală",
            "ratingul superiorului vs autoevaluarea angajatului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care concept descrie partea din criteriul efectiv care corespunde "
            "corect cu ceea ce vrem să măsurăm (intersecția teoretic–efectiv)?"
        ),
        "options": [
            "relevanța criteriului (relevance)",
            "deficiența criteriului (deficiency)",
            "contaminarea criteriului (contamination)",
            "validitatea incrementală a selecției",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Deficiența criteriului (criterion deficiency) înseamnă că:"
        ),
        "options": [
            "lipsește din măsurare ceva important din constructul teoretic al "
            "performanței",
            "criteriul efectiv nu acoperă toate aspectele relevante ale jobului",
            "apare în evaluare ceva nerelevant (ex. simpatie față de angajat)",
            "criteriul teoretic și cel efectiv coincid perfect",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Contaminarea criteriului (criterion contamination) apare când:"
        ),
        "options": [
            "în scorul de performanță intră factori care nu țin de job",
            "supervizorul lasă favoritismul sau simpatia să influențeze ratingul",
            "lipsește din evaluare o dimensiune esențială a rolului",
            "criteriul măsoară strict sarcinile din fișa postului, fără zgomot",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un evaluator îi dă note mari unui subordonat pentru că îi place "
            "personal, deși rezultatele obiective sunt medii. Aceasta ilustrează "
            "cel mai clar:"
        ),
        "options": [
            "contaminarea criteriului (criterion contamination)",
            "deficiența criteriului (criterion deficiency)",
            "relevanța perfectă între criteriu teoretic și efectiv",
            "performanță la sarcină (task performance) în sens Borman–Motowidlo",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Evaluarea anuală ignoră complet comportamentele de colaborare și "
            "respectarea procedurilor, măsurând doar volumul de output. Aceasta "
            "sugerează:"
        ),
        "options": [
            "deficiență a criteriului — lipsește o parte importantă din performanță",
            "relevanță ridicată — criteriul efectiv acoperă tot constructul teoretic",
            "contaminare — intră factori nerelevanți în scor",
            "validitate predictivă foarte puternică a instrumentului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi asociază corect conceptul cu descrierea lui?"
        ),
        "options": [
            "ce măsurăm din performanță este cu adevărat relevant",
            "lipsește ceva important din măsurare",
            "apare ceva nerelevant în scorul de performanță",
            "criteriul efectiv este mai scurt decât cel teoretic",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre relevanță și contaminare în evaluarea performanței "
            "este falsă?"
        ),
        "options": [
            "relevanța și contaminarea sunt același lucru — ambele indică același tip "
            "de problemă",
            "relevanța vizează ce din măsurare este cu adevărat util",
            "contaminarea apare când intră factori nerelevanți în scor",
            "deficiența înseamnă că lipsește ceva important din criteriu",
        ],
        "correct": "a",
    },
    # —— Borman & Motowidlo: task vs contextual (15–22) ——
    {
        "stem": (
            "În modelul lui Borman și Motowidlo, performanța la sarcină (task "
            "performance) se referă în principal la:"
        ),
        "options": [
            "activitățile esențiale ale rolului, legate de obiectivele din fișa "
            "postului",
            "comportamente suplimentare care susțin organizația, dar nu sunt în "
            "sarcina formală",
            "comportamente contraproductive la locul de muncă (CWB)",
            "doar comportamente de cetățenie organizațională (OCB)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Performanța contextuală (contextual performance), în modelul Borman "
            "și Motowidlo, include:"
        ),
        "options": [
            "comportamente care susțin mediul de lucru și organizația",
            "acțiuni care depășesc cerințele formale minime ale rolului",
            "activitățile nucleu din descrierea postului, măsurate strict pe output",
            "comportamente voluntare pozitive care ajută echipa sau firma",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care exemple corespund performanței la sarcină (task performance), "
            "respectiv performanței contextuale?"
        ),
        "options": [
            "un operator atinge standardele de productivitate din fișa postului",
            "un coleg ajută voluntar un nou angajat să învețe procedura",
            "respectarea termenelor pentru livrabilele principale",
            "acceptarea sarcinilor neplăcute fără plângeri excesive",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un analist finalizează la timp rapoartele obligatorii, dar refuză să "
            "participe la proiecte transversale care nu îi sunt cerute explicit. "
            "Care evaluare este mai precisă?"
        ),
        "options": [
            "performanță la sarcină (task) probabil bună pe livrabile obligatorii",
            "performanță contextuală posibil redusă pe comportamente suplimentare",
            "ambele dimensiuni sunt identice — dacă task e bun, contextual e automat "
            "bun",
            "refuzul proiectelor transversale este mereu comportament "
            "contraproductiv (CWB)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care distincții între performanța la sarcină și cea contextuală sunt "
            "corecte?"
        ),
        "options": [
            "task = activități esențiale din rol; contextual = comportamente care "
            "susțin organizația",
            "contextual poate include acțiuni care nu sunt obligatorii în fișa "
            "postului",
            "task și contextual sunt sinonime în modelul Borman–Motowidlo",
            "task se leagă de obiectivele formale ale jobului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre relația dintre comportamentele de cetățenie "
            "organizațională (OCB) și performanța contextuală este falsă?"
        ),
        "options": [
            "OCB și performanța contextuală sunt exact același construct, fără nicio "
            "diferență",
            "OCB este un subset al performanței contextuale",
            "performanța contextuală poate include comportamente dincolo de OCB",
            "ambele vizează comportamente care susțin organizația",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un șef evaluează doar „cât de mult ajută oamenii organizația în plus”, "
            "ignorând livrarea sarcinilor principale. Riscul principal este:"
        ),
        "options": [
            "deficiență a criteriului față de performanța la sarcină (task)",
            "contaminare prin favoritism",
            "confundarea performanței contextuale cu comportamente contraproductive "
            "(CWB)",
            "supraevaluarea performanței la sarcină (task)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre relația dintre performanța contextuală și "
            "comportamentele de cetățenie organizațională (OCB) sunt corecte?"
        ),
        "options": [
            "OCB este un subset al performanței contextuale, nu sinonimul ei",
            "performanța contextuală este mai largă decât OCB",
            "OCB acoperă toate formele de performanță contextuală, fără excepție",
            "ambele vizează comportamente care susțin organizația, dar OCB este o "
            "categorie mai îngustă",
        ],
        "correct": "abd",
    },
    # —— OCB: natură și dimensiuni (23–32) ——
    {
        "stem": (
            "Comportamentele de cetățenie organizațională (OCB) sunt, în mod "
            "tipic:"
        ),
        "options": [
            "voluntare — nu sunt strict obligatorii în contract",
            "pozitive pentru organizație sau colegi",
            "obligatorii prin fișa postului, ca sarcinile principale",
            "orientate spre a ajuta funcționarea echipei sau a firmei",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care dimensiuni ale comportamentelor de cetățenie organizațională "
            "(OCB) sunt recunoscute în literatura clasică (Organ)?"
        ),
        "options": [
            "altruism — ajutor direct acordat colegilor",
            "conștiinciozitate organizațională — depunere de efort dincolo de minim",
            "sportsmanship — toleranța față de inconveniente fără plângeri excesive",
            "curtenie (courtesy) — prevenirea problemelor prin comunicare preventivă",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un angajat îl ajută pe un coleg blocat la un proiect, deși nu i se "
            "cere în fișa postului. Aceasta ilustrează cel mai direct dimensiunea "
            "OCB numită:"
        ),
        "options": [
            "altruism",
            "sportsmanship",
            "virtute civică (civic virtue)",
            "comportament contraproductiv (CWB) spre organizație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un membru al echipei anunță din timp colegii când va lipsi de la o "
            "ședință, ca să poată reprograma. Aceasta corespunde dimensiunii OCB:"
        ),
        "options": [
            "curtenie (courtesy)",
            "altruism",
            "sportsmanship",
            "performanță la sarcină (task performance)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care exemple ilustrează sportsmanship și, respectiv, conștiinciozitate "
            "organizațională în sens OCB?"
        ),
        "options": [
            "acceptă schimbarea procedurii fără a sabota atmosfera",
            "vine mai devreme pentru a termina o sarcină importantă",
            "fură echipamente din birou",
            "participă la întâlniri opționale despre direcția firmei",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Virtutea civică (civic virtue) în cadrul OCB se referă la:"
        ),
        "options": [
            "implicarea responsabilă în viața organizației (ex. participare la "
            "inițiative interne)",
            "promovarea intereselor organizației în mod constructiv",
            "sabotarea politicilor firmei pentru avantaj personal",
            "respectarea strictă doar a sarcinilor din job description, fără implicare "
            "extra",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre comportamentele de cetățenie organizațională "
            "(OCB) este falsă?"
        ),
        "options": [
            "OCB sunt impuse contractual ca sarcini obligatorii, identice cu "
            "livrabilele din fișa postului",
            "OCB sunt voluntare și pozitive pentru organizație",
            "OCB pot include altruism, curtenie sau virtute civică",
            "OCB diferă de comportamentele contraproductive (CWB)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre predictori ai comportamentelor de cetățenie "
            "organizațională (OCB) sunt susținute de cercetare?"
        ),
        "options": [
            "conștiinciozitatea (conscientiousness) — asociată pozitiv cu OCB",
            "agreabilitatea (agreeableness) — asociată pozitiv cu OCB",
            "satisfacția la locul de muncă — predictor al OCB",
            "justiția organizațională percepută — legată pozitiv de OCB",
            "neuroticismul ridicat — predictor consistent al OCB",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "De ce justiția organizațională percepută poate crește comportamentele "
            "de cetățenie organizațională (OCB)?"
        ),
        "options": [
            "angajații reciprocă tratamentul echitabil prin efort suplimentar "
            "voluntar",
            "percepția de corectitudine crește motivația de a ajuta organizația",
            "justiția organizațională elimină nevoia de performanță la sarcină",
            "OCB devine obligatoriu legal când justiția este ridicată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un angajat cu agreabilitate (agreeableness) scăzută va manifesta, în "
            "mod tipic, mai multe comportamente de cetățenie organizațională "
            "(OCB) decât un coleg cu agreabilitate ridicată."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— CWB și distincții OCB–CWB (33–40) ——
    {
        "stem": (
            "Comportamentele contraproductive la locul de muncă (CWB) se "
            "caracterizează prin:"
        ),
        "options": [
            "sunt voluntare (nu doar erori accidentale)",
            "au impact negativ asupra organizației sau persoanelor",
            "sunt identice cu lipsa performanței la sarcină (task)",
            "pot viza organizația sau colegii/clienții",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care exemple sunt comportamente contraproductive (CWB) orientate spre "
            "organizație, respectiv spre persoane?"
        ),
        "options": [
            "furt de materiale din firmă",
            "sabotaj intenționat al echipamentului",
            "absenteism deliberat fără motiv legitim",
            "agresivitate sau bullying la colegi",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care trăsături de personalitate sunt asociate în mod tipic cu mai multe "
            "comportamente contraproductive la locul de muncă (CWB)?"
        ),
        "options": [
            "neuroticism (N) ridicat",
            "conștiinciozitate (C) scăzută",
            "agreabilitate (A) scăzută",
            "conștiinciozitate (C) ridicată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care factori situaționali pot crește comportamentele contraproductive "
            "(CWB)?"
        ),
        "options": [
            "percepția de injustiție organizațională",
            "frustrare la locul de muncă",
            "justiție organizațională ridicată și recunoaștere echitabilă",
            "lipsa controlului asupra propriului rol, în anumite contexte",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un coleg împrumută fără permisiune echipament de la firmă și îl folosește "
            "acasă. Aceasta este un exemplu de:"
        ),
        "options": [
            "comportament contraproductiv (CWB) orientat spre organizație",
            "comportament de cetățenie organizațională (OCB) — altruism",
            "performanță contextuală pozitivă",
            "performanță la sarcină (task performance)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Comportamentele de cetățenie organizațională (OCB) și comportamentele "
            "contraproductive (CWB) sunt poli opuși pe aceeași scală, deci un "
            "angajat cu OCB ridicat nu poate manifesta niciodată CWB."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care distincții între OCB și CWB sunt corecte?"
        ),
        "options": [
            "OCB = voluntar, pozitiv; CWB = voluntar, negativ",
            "OCB ajută organizația; CWB dăunează organizației sau persoanelor",
            "OCB și CWB sunt același construct măsurat invers",
            "lipsa OCB nu este automat CWB — poți fi neutru, fără extra ajutor "
            "sau fără dăunare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un angajat nu ajută colegii în plus (OCB scăzut), dar nici nu fură sau "
            "agresează. Evaluarea corectă este:"
        ),
        "options": [
            "absența OCB nu înseamnă automat CWB",
            "poate avea performanță la sarcină (task) acceptabilă, dar contextuală "
            "redusă",
            "trebuie clasificat automat ca CWB pentru indiferență",
            "OCB scăzut echivalează cu sabotaj organizațional",
        ],
        "correct": "ab",
    },
    # —— Performanță adaptivă, măsurare (41–50) ——
    {
        "stem": (
            "Performanța adaptivă (adaptive performance) se referă la capacitatea "
            "de a:"
        ),
        "options": [
            "răspunde eficient la schimbări la locul de muncă",
            "învăța proceduri noi și a te ajusta la cerințe în evoluție",
            "menține rigid aceleași obiceiuri, indiferent de context",
            "refuza orice modificare a sarcinilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care predictori sunt asociați în mod tipic cu performanța adaptivă?"
        ),
        "options": [
            "aptitudinea mentală generală (GMA)",
            "deschiderea către experiență (openness)",
            "neuroticismul ridicat ca principal predictor pozitiv",
            "agreabilitatea scăzută ca predictor central",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "După restructurare, un tehnician învață rapid noul software și propune "
            "îmbunătățiri de proces. Aceasta ilustrează cel mai bine:"
        ),
        "options": [
            "performanță adaptivă (adaptive performance)",
            "comportament contraproductiv (CWB)",
            "doar performanță la sarcină statică, fără componentă de schimbare",
            "contaminare a criteriului de evaluare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre măsurarea obiectivă vs subiectivă a performanței "
            "sunt corecte?"
        ),
        "options": [
            "măsurarea obiectivă (ex. vânzări, erori) reduce parțial subiectivitatea",
            "măsurarea subiectivă (ex. rating de la superior) poate capta comportamente "
            "greu de numărat",
            "măsurarea obiectivă captează automat toate dimensiunile OCB",
            "ratingul superiorului este flexibil, dar vulnerabil la favoritism "
            "(contaminare)",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un manager evaluează performanța doar prin numărul de apeluri preluate, "
            "ignorând calitatea comunicării cu clienții. Problema principală este:"
        ),
        "options": [
            "deficiență a criteriului — lipsește calitatea/comportamentul relevant",
            "criteriu prea larg care include factori nerelevanți",
            "contaminare prin simpatie",
            "supra-măsurare a performanței contextuale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre măsurarea obiectivă a performanței este "
            "exagerată (deci greșită)?"
        ),
        "options": [
            "măsurarea obiectivă elimină complet orice eroare și este mereu "
            "superioară celei subiective",
            "indicatorii obiectivi (vânzări, erori) pot reduce subiectivitatea",
            "ratingul superiorului poate capta comportamente greu de numărat",
            "măsurarea subiectivă poate fi afectată de favoritism (contaminare)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care scenarii ilustrează corect contaminarea vs deficiența criteriului?"
        ),
        "options": [
            "nota crește din cauza prieteniei cu șeful",
            "evaluarea ignoră comportamentele de colaborare",
            "criteriul include doar sarcinile relevante din job",
            "în scor intră performanța echipei, nu a individului evaluat",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații rezumă corect modelul performanței în muncă prezentat "
            "în curs?"
        ),
        "options": [
            "performanța = comportamente + rezultate",
            "Borman–Motowidlo: task performance vs contextual performance; OCB ⊂ "
            "contextual",
            "OCB (pozitiv, voluntar) ≠ CWB (negativ, voluntar)",
            "relevanță, deficiență, contaminare — calitatea criteriului efectiv față "
            "de cel teoretic",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un angajat are performanță la sarcină (task) excelentă, OCB moderat și "
            "niciun CWB. Un evaluator îi scade nota pentru că „nu e suficient de "
            "entuziast la petreceri”. Aceasta sugerează:"
        ),
        "options": [
            "contaminare — criteriu influențat de factori nerelevanți",
            "confundare între OCB opțional și cerințe formale de task",
            "deficiență — lipsește măsurarea sarcinilor principale",
            "validitate incrementală ridicată a criteriului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În evaluarea performanței, criteriul teoretic descrie ce ar trebui "
            "măsurat ideal, iar criteriul efectiv descrie ce măsurăm în practică — "
            "relevanța este partea utilă, deficiența ce lipsește, contaminarea ce "
            "nu ar trebui să intre."
        ),
        "tf": True,
        "correct_tf": True,
    },
]
