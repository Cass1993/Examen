"""Itemi — tipuri și forme ale învățării (40 itemi, ID 10691–10730)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

TIPURI_FORME_ITEMS: List[Item] = [
    # —— 1–10: clasificări, cadru, conținut, mecanism ——
    {
        "stem": (
            "Învățarea poate fi analizată pedagogic după mai multe criterii: cadru "
            "(formal, informal, nonformal), conținut, mecanism și grad de implicare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care distincție între învățarea formală și cea informală este corectă?"
        ),
        "options": [
            "formală: instituționalizată, cu curriculum și evaluare; informală: din "
            "viața cotidiană, fără structură școlară planificată",
            "formală: apare spontan în joacă; informală: presupune diplomă și examene",
            "formală: se limitează la adulți; informală: este specifică sugarilor",
            "formală și informală sunt identice ca organizare și scop",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei formulări descriu corect învățarea după cadru?"
        ),
        "options": [
            "formală — școală, universitate, programe cu obiective și evaluare certificate",
            "informală — din experiențe zilnice, conversații, observare, fără programă fixă",
            "nonformală — cursuri, cluburi, ateliere organizate, dar în afara sistemului "
            "formal strict",
            "formală — activități de joacă spontană, fără curriculum școlar",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Învățarea conceptuală se referă în principal la:"
        ),
        "options": [
            "idei, relații, categorii și abstractizări — nu la reacții senzoriale izolate",
            "coordonarea mișcărilor fine și a gesturilor motorii",
            "memorarea mecanică a listelor de cuvinte fără înțelegere",
            "reflexele necondiționate la stimuli simpli",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două tipuri de învățare după conținut sunt formulate corect?"
        ),
        "options": [
            "verbală — limbaj, simboluri, comunicare",
            "afectivă — emoții, atitudini, valori",
            "socială — norme, roluri, comportamente în relație cu alții",
            "reflexivă — răspunsuri automate la stimuli fără procesare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Condiționarea clasică (pavloviană) este un mecanism de învățare în care:"
        ),
        "options": [
            "un stimul neutru, asociat repetat cu un stimul necondiționat, ajunge să "
            "declanșeze un răspuns condiționat",
            "consecințele comportamentului modifică probabilitatea repetării acestuia",
            "elevul interiorizează norme prin interacțiune cu grupul",
            "cunoștințele se organizează în scheme cognitive complexe",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două mecanisme de învățare sunt asociate cu behaviorismul operant "
            "și cu modelarea socială?"
        ),
        "options": [
            "condiționare operantă/instrumentală — consecințele întăresc sau slăbesc "
            "comportamentul",
            "învățare prin imitație/observare — comportamente noi din modele",
            "condiționare clasică — asociere stimul–stimul reflex",
            "învățare latentă tolmaniană — hărți cognitive fără recompensă imediată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea prin imitație (modelare) presupune că individul:"
        ),
        "options": [
            "observă comportamentul altora și îl reproduce sau îl adaptează",
            "formează asocieri reflexe între doi stimuli fiziologici",
            "memorează liste de cuvinte fără legătură cu un model",
            "aplică reguli abstracte fără a fi expus la exemplu concret",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între învățarea pasivă și cea activă sunt corecte?"
        ),
        "options": [
            "pasivă: receptare a informației fără procesare profundă; activă: implicare "
            "în rezolvare, discuție, aplicare",
            "activă: elevul construiește sens și participă; pasivă: ascultare "
            "neinteractivă, lectură fără sarcină",
            "pasivă: presupune autoreglare și planificare; activă: exclude colaborarea",
            "activă: se limitează la memorarea definițiilor din manual",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două forme de implicare în învățare depășesc receptarea pasivă?"
        ),
        "options": [
            "autoreglată — elevul își monitorizează și ajustează parcursul",
            "colaborativă — învățare în echipă, cu roluri și discuție comună",
            "experiențială — bazată pe experiență directă și reflecție",
            "pasivă — ascultarea neinteractivă a unei prelegeri lungi",
        ],
        "correct": "ab",
    },
    # —— 11–20: personalizată, autoreglată ——
    {
        "stem": (
            "Învățarea personalizată presupune ajustarea ritmului, conținutului, "
            "strategiilor și obiectivelor la nevoile și profilul elevului."
        ),
        "options": [
            "adevărat — parcursul se adaptează individual, nu uniform pentru toți",
            "fals — personalizarea înseamnă același plan pentru întreaga clasă",
            "adevărat — personalizarea presupune renunțarea la tehnologie digitală",
            "fals — ritmul și conținutul nu pot fi modificate în școală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două avantaje ale învățării personalizate sunt frecvent menționate?"
        ),
        "options": [
            "respectă stilul și ritmul propriu al elevului, crescând implicarea",
            "permite feedback mai rapid și monitorizare adaptată (inclusiv prin tehnologie)",
            "uniformizează toți elevii la același nivel de performanță",
            "reduce planificarea obiectivelor și a evaluării la minimum",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea autoreglată presupune că elevul își stabilește obiective, "
            "își monitorizează progresul, își ajustează strategiile și își evaluează "
            "rezultatele."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care trei procese aparțin învățării autoreglate?"
        ),
        "options": [
            "stabilirea obiectivelor de învățare",
            "monitorizarea progresului și a înțelegerii",
            "ajustarea strategiilor când apar dificultăți",
            "receptarea pasivă fără reflecție asupra propriului parcurs",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Învățarea autoreglată necesită în special:"
        ),
        "options": [
            "metacogniție, motivație și capacitate de planificare",
            "memorare mecanică fără monitorizare a progresului",
            "dependență totală de indicațiile pas cu pas ale profesorului",
            "renunțarea la evaluarea propriilor rezultate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru etape descriu ciclul învățării autoreglate?"
        ),
        "options": [
            "stabilirea obiectivelor",
            "monitorizarea progresului",
            "ajustarea strategiilor",
            "evaluarea rezultatelor",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care două idei definesc blended learning (învățarea combinată)?"
        ),
        "options": [
            "combină activități față în față cu activități online",
            "include timp în clasă, resurse digitale, ghidare și feedback",
            "înlocuiește complet prezența fizică la școală",
            "exclude resursele multimedia și platformele web",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În flipped classroom (clasă inversată), elevul:"
        ),
        "options": [
            "studiază conținutul acasă (ex. video, materiale online), iar la clasă "
            "aplică, discută și primește sprijin",
            "studiază la clasă teoria, iar acasă rezolvă teme fără feedback",
            "renunță la activități online în favoarea expunerii orale lungi",
            "memorează manualul la clasă, fără aplicare practică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două componente apar frecvent în modelul blended learning?"
        ),
        "options": [
            "activități sincrone sau față în față în clasă",
            "resurse și activități online (platforme, materiale digitale)",
            "feedback și ghidare din partea profesorului",
            "lectură pasivă, fără interacțiune digitală sau umană",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea activă presupune că elevii:"
        ),
        "options": [
            "participă prin discuții, rezolvare de probleme, studii de caz, proiecte",
            "ascultă pasiv fără sarcini de procesare sau aplicare",
            "memorează definiții fără a le folosi în exerciții",
            "evită colaborarea și investigarea",
        ],
        "correct": "a",
    },
    # —— 21–30: forme active, Kolb, socială, computerizată ——
    {
        "stem": (
            "Care formă de învățare activă presupune ca elevii să își explice "
            "reciproc conținutul și să se corecteze?"
        ),
        "options": [
            "învățarea reciprocă — elevii se instruiesc și se evaluează unii pe alții",
            "lectura pasivă a manualului fără discuție",
            "condiționarea clasică a reflexelor",
            "memorarea listelor de termeni în ordine alfabetică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două forme de învățare activă sunt enumerate corect?"
        ),
        "options": [
            "studii de caz — analiza unor situații reale sau simulate",
            "învățare prin proiecte — elaborarea unui produs sau rezolvarea unei probleme",
            "ascultarea neinteractivă a unei prelegeri de două ore",
            "copierea textului de pe tablă fără procesare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Primul pas în ciclul experiențial al lui Kolb este:"
        ),
        "options": [
            "experiența concretă — trăirea directă a unei situații",
            "aplicarea/testarea în practică a conceptelor",
            "conceptualizarea abstractă fără experiență anterioară",
            "reflecția asupra unei teorii citite pasiv",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru etape compun ciclul experiențial Kolb, în ordinea logică?"
        ),
        "options": [
            "experiență concretă",
            "reflecție observativă asupra experienței",
            "conceptualizare abstractă — generalizare, teorii",
            "aplicare activă — testare în situații noi",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care două caracteristici definesc învățarea experiențială?"
        ),
        "options": [
            "bază pe experiență directă și reflecție critică asupra ei",
            "ieșirea din zona de confort și relații semnificative în proces",
            "memorare mecanică fără legătură cu situații reale",
            "receptare pasivă a conținutului teoretic, fără aplicare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea experiențială standardizată în masă, fără reflecție individuală, "
            "este forma cea mai eficientă de dezvoltare a competențelor."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei avantaje ale învățării experiențiale sunt frecvent evocate?"
        ),
        "options": [
            "dezvoltarea autonomiei și a responsabilității în parcurs",
            "clarificarea obiectivelor prin acțiune și reflecție",
            "aplicarea practică a cunoștințelor în contexte reale",
            "uniformizarea răspunsurilor elevilor fără comunicare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Învățarea socială presupune interiorizarea, prin interacțiune, a:"
        ),
        "options": [
            "normelor, rolurilor, valorilor, atitudinilor și comportamentelor grupului",
            "reflexelor necondiționate la stimuli simpli",
            "listelor de vocabular fără context relațional",
            "formulelor matematice memorate mecanic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două forme aparțin învățării computerizate (digitale)?"
        ),
        "options": [
            "e-learning pe platforme web sau aplicații educaționale",
            "instruire prin videoclipuri, simulări și resurse interactive multimedia",
            "lecție orală în clasă, fără suport digital",
            "copierea manuală a textelor în caiet, fără tehnologie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea prin discriminare presupune că organismul sau elevul:"
        ),
        "options": [
            "diferențiază între stimuli similari și răspunde adecvat la fiecare",
            "reacționează similar la stimuli diferiți din aceeași categorie",
            "memorează texte fără a percepe diferențe contextuale",
            "reproduce comportamente observate, indiferent de potrivirea contextului",
        ],
        "correct": "a",
    },
    # —— 31–40: reguli, nonformală, sinteză ——
    {
        "stem": (
            "Învățarea prin reguli (verbal-conceptuală) presupune că elevul:"
        ),
        "options": [
            "înțelege și aplică enunțuri, principii sau algoritmi generalizabile",
            "formează reflexe la stimuli fără înțelegerea regulii",
            "copiază mecanic exemple fără a extrage principiul",
            "evită formularea verbală a cunoștințelor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei resurse sau formate sunt asociate învățării computerizate?"
        ),
        "options": [
            "platforme web și cursuri online",
            "videoclipuri educaționale și tutoriale digitale",
            "materiale interactive și multimedia",
            "dictare orală neînregistrată, fără suport digital",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Învățarea nonformală se caracterizează prin:"
        ),
        "options": [
            "organizare intenționată (cursuri, ateliere, cluburi), dar în afara "
            "sistemului formal strict de diplomă",
            "organizare facultativă, fără facilitator sau scop pedagogic clar",
            "limitare la experiențe accidentale din viața de zi cu zi",
            "identitate completă cu învățarea informală spontană",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două tipuri de învățare după conținut vizează percepția și "
            "mișcarea?"
        ),
        "options": [
            "senzorială — procesarea informației prin simțuri",
            "motrică — coordonarea mișcărilor și a gesturilor",
            "conceptuală — categorii și relații abstracte",
            "verbală — comunicare prin limbaj",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru mecanisme de învățare apar în clasificarea după mecanism?"
        ),
        "options": [
            "condiționare clasică",
            "condiționare operantă/instrumentală",
            "învățare prin imitație/modelare",
            "învățare prin reguli sau prin discriminare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Învățarea colaborativă presupune:"
        ),
        "options": [
            "lucrul în echipă, cu discuție, roluri împărțite și obiectiv comun",
            "competiția individuală fără schimb de idei",
            "memorarea separată a aceluiași text de către fiecare elev",
            "ascultarea pasivă a profesorului, fără interacțiune între colegi",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două forme de învățare activă implică adaptarea conținutului "
            "la interesele elevilor?"
        ),
        "options": [
            "curriculum emergent — teme care se dezvoltă din întrebările grupului",
            "învățare prin investigare/cercetare — elevii explorează o problemă",
            "dictarea mecanică a definițiilor din manual",
            "testarea standardizată fără activitate exploratorie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei avantaje ale blended learning sunt frecvent menționate?"
        ),
        "options": [
            "acces flexibil la resurse și ritm parțial adaptat",
            "colaborare online și feedback mai rapid prin platforme",
            "integrarea resurselor multimedia în parcurs",
            "predominanța activităților asincrone, fără întâlniri cu profesorul",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Învățarea pasivă produce, în general, retenție mai durabilă decât "
            "învățarea activă, deoarece solicită mai puțin efort cognitiv."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei elemente sunt ajustate în învățarea personalizată?"
        ),
        "options": [
            "ritmul parcursului",
            "conținutul și nivelul de dificultate",
            "strategiile de învățare",
            "absența obiectivelor — elevul învață fără direcție",
        ],
        "correct": "abc",
    },
]

assert len(TIPURI_FORME_ITEMS) == 40
