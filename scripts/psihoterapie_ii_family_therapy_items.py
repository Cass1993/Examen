"""Itemi — terapia de familie: psihodinamică, sistemică, structurală, strategică, experiențială."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

FAMILY_THERAPY_ITEMS: List[Item] = [
    # —— Terapia de familie: fundamente (1–5) ——
    {
        "stem": "În terapia de familie, familia este văzută, de regulă, ca un sistem în care:",
        "options": [
            "membrii se influențează reciproc prin comunicare, reguli și patternuri relaționale",
            "fiecare membru funcționează complet independent, fără legături relevante",
            "simptomul aparține biologic unui singur individ, fără context relațional",
            "terapia trebuie să evite implicarea celorlalți membri ai familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Cauzalitatea circulară, în terapia de familie sistemică, presupune că:",
        "options": [
            "comportamentele membrilor se mențin reciproc într-un ciclu de interacțiuni",
            "o singură persoană este întotdeauna cauza exclusivă a problemei",
            "trecutul freudian explică singur prezentul familial",
            "simptomul nu are legătură cu comunicarea dintre membri",
        ],
        "correct": "a",
    },
    {
        "stem": "Expresia „pacientul identificat” (IP) în terapia de familie desemnează membrul care:",
        "options": [
            "aduce în vizibil simptomul unei dificultăți mai largi a sistemului familial",
            "este singurul vinovat pentru toate conflictele din familie",
            "nu necesită participarea celorlalți membri la terapie",
            "demonstrează absența oricărei influențe familiale asupra simptomului",
        ],
        "correct": "a",
    },
    {
        "stem": "Un obiectiv frecvent al terapiei de familie este:",
        "options": [
            "îmbunătățirea comunicării și clarificarea rolurilor, limitelor și alianțelor",
            "identificarea unui singur purtător al vinovăției pentru simptom",
            "păstrarea neschimbate a patternurilor disfuncționale",
            "lucrul exclusiv individual, fără context familial",
        ],
        "correct": "a",
    },
    {
        "stem": "Întrebarea „cum este menținută problema în sistem?” este preferabilă întrebării „cine este vinovat?” deoarece:",
        "options": [
            "orientarea spre patternuri relaționale evită culpabilizarea unilaterală",
            "familia funcționează fără reguli sau feedback între membri",
            "simptomul este strict biologic și nu ține de relații",
            "comunicarea trebuie redusă pentru a diminua conflictul",
        ],
        "correct": "a",
    },
    # —— Abordare psihodinamică (6–10) ——
    {
        "stem": "Abordarea psihodinamică în terapia de familie urmărește mai ales:",
        "options": [
            "influența relațiilor timpurii, a conflictelor și a transferurilor în viața familială",
            "restructurarea granițelor și a ierarhiei între subsisteme",
            "prescrierea simptomului ca intervenție principală",
            "antrenamentul de relaxare și expunerea gradată la fobii",
        ],
        "correct": "a",
    },
    {
        "stem": "Murray Bowen, în terapia de familie, este asociat cu conceptul de:",
        "options": [
            "diferențiere de sine — rămânere calmă și autonomă în relații intense",
            "enmeshment — granițe difuze între membri",
            "prescrierea simptomului — intervenție strategică",
            "restructurare cognitivă a distorsiunilor automate",
        ],
        "correct": "a",
    },
    {
        "stem": "Genograma, în abordarea lui Murray Bowen, este utilă pentru a:",
        "options": [
            "vizualiza patternuri emoționale și relaționale pe mai multe generații",
            "construi ierarhia de expunere în fobii",
            "disputa convingerile iraționale ellisiene",
            "interpreta visul în sens jungian",
        ],
        "correct": "a",
    },
    {
        "stem": "Triangularea, în teoria lui Murray Bowen, apare când:",
        "options": [
            "tensiunea dintre doi membri atrage un al treilea în conflict sau alianță",
            "un copil devine singurul responsabil pentru simptom",
            "terapeutul evită orice implicare a familiei",
            "familia nu are reguli sau feedback",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de abordarea structurală, terapia de familie psihodinamică pune mai mult accent pe:",
        "options": [
            "istoricul relațional, conflictele și transferul în familie",
            "granițele, subsistemele și ierarhia organizațională",
            "directivele paradoxale ca tehnică centrală",
            "experimentele gestaltice de contact în prezent",
        ],
        "correct": "a",
    },
    # —— Abordare sistemică (11–15) ——
    {
        "stem": "Abordarea sistemică în terapia de familie vede familia ca un sistem cu:",
        "options": [
            "reguli, feedback și tendință spre homeostazie",
            "membri complet independenți unii de alții",
            "obligația eliminării oricărei reguli implicite",
            "focus exclusiv pe un singur membru, fără context",
        ],
        "correct": "a",
    },
    {
        "stem": "Homeostazia, în terapia de familie sistemică, descrie tendința sistemului de a:",
        "options": [
            "menține echilibrul și patternurile familiare, chiar dacă unele sunt disfuncționale",
            "elimina orice regulă sau rutină familială",
            "schimba automat toate regulile la prima intervenție",
            "respinge ideea de feedback între membri",
        ],
        "correct": "a",
    },
    {
        "stem": "Schimbarea de ordinul I (first-order) în terapia de familie presupune:",
        "options": [
            "modificarea comportamentelor sau simptomelor fără schimbarea regulilor sistemului",
            "modificarea regulilor și credințelor care organizează familia",
            "interpretarea inconștientului colectiv jungian",
            "disputa convingerilor absolute din REBT",
        ],
        "correct": "a",
    },
    {
        "stem": "Schimbarea de ordinul II (second-order) în abordarea sistemică presupune:",
        "options": [
            "modificarea regulilor, credințelor sau patternurilor care mențin problema",
            "reducerea simptomului fără alterarea interacțiunilor familiale",
            "lucrul individual, fără implicarea membrilor familiei",
            "evitarea oricărei intervenții asupra comunicării",
        ],
        "correct": "a",
    },
    {
        "stem": "Un copil dezvoltă simptome când părinții sunt în conflict cronic, iar copilul devine centrul atenției familiale. Din perspectivă sistemică, acest scenariu ilustrează că:",
        "options": [
            "simptomul poate stabiliza sau reorganiza sistemul familial",
            "simptomul dovedește o boală strict individuală, fără context",
            "terapia trebuie să evite implicarea părinților",
            "restructurarea cognitivă a copilului, fără restul familiei, este suficientă",
        ],
        "correct": "a",
    },
    # —— Abordare structurală (16–20) ——
    {
        "stem": "Salvador Minuchin, în terapia de familie structurală, pune accent pe:",
        "options": [
            "granițe, subsisteme, ierarhie și organizarea relațiilor",
            "interpretarea visului ca sursă principală a simptomului",
            "acceptarea necondiționată ca singură intervenție",
            "condiționarea operantă a comportamentelor individuale",
        ],
        "correct": "a",
    },
    {
        "stem": "Enmeshment (împletirea excesivă), în abordarea structurală, se caracterizează prin:",
        "options": [
            "granițe difuze și suprareacție la distanțare emoțională",
            "granițe rigide și comunicare minimă între membri",
            "ierarhie clară și autonomie optimă a adolescenților",
            "absența oricărei emoții în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Disengagement (dezangajarea), în abordarea structurală, se caracterizează prin:",
        "options": [
            "granițe rigide, sprijin emoțional redus și comunicare limitată",
            "granițe difuze și dependență emoțională excesivă",
            "triangulare obligatorie cu copilul",
            "subsisteme parentală și conjugală clar diferențiate",
        ],
        "correct": "a",
    },
    {
        "stem": "Restructurarea, în terapia structurală a lui Salvador Minuchin, urmărește:",
        "options": [
            "modificarea alianțelor, granițelor și ierarhiei pentru a susține funcționarea familiei",
            "interpretarea simbolică a viselor părinților",
            "evitarea oricărei schimbări în organizarea familiei",
            "disputa convingerilor iraționale ale unui singur membru",
        ],
        "correct": "a",
    },
    {
        "stem": "Confuzia între abordarea structurală și cea psihodinamică se clarifică astfel:",
        "options": [
            "structurală — granițe, ierarhie, subsisteme; psihodinamică — istorie, conflicte, transfer",
            "structurală — interpretarea inconștientului; psihodinamică — restructurarea granițelor",
            "ambele resping ideea de organizare a familiei",
            "structurală — asociație liberă; psihodinamică — joining și unbalancing",
        ],
        "correct": "a",
    },
    # —— Abordare strategică (21–25) ——
    {
        "stem": "Abordarea strategică în terapia de familie (ex. Jay Haley) se caracterizează prin:",
        "options": [
            "intervenții concrete, planificate, pentru schimbarea interacțiunilor care mențin problema",
            "explorarea liberă a inconștientului fără obiectiv clar",
            "refuzul oricărei intervenții directe",
            "lucrul exclusiv individual, fără membrii familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea strategică, prescrierea simptomului urmărește, în anumite cazuri:",
        "options": [
            "să schimbe regulile interacțiunii care mențin simptomul",
            "să amplifice permanent suferința clientului",
            "să evite orice implicare a familiei în terapie",
            "să înlocuiască consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia strategică de familie este adesea:",
        "options": [
            "scurtă și orientată spre rezolvarea unei probleme concrete de interacțiune",
            "nedeterminată în durată, fără obiective clare",
            "centrată pe interpretarea visului ca prioritate",
            "limitată la restructurarea cognitivă individuală",
        ],
        "correct": "a",
    },
    {
        "stem": "Comportamentul care menține problema (problem-maintaining behavior), în abordarea strategică, se referă la:",
        "options": [
            "interacțiunile repetitive care păstrează simptomul sau conflictul în familie",
            "mecanismele de apărare freudiene din copilărie",
            "arhetipurile jungiene active în relație",
            "distorsiunile cognitive beckiene ale unui singur membru",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de abordarea experiențială, terapia strategică de familie:",
        "options": [
            "pune accent pe directive și schimbarea patternurilor, nu pe exprimarea emoțională profundă",
            "evită orice intervenție planificată",
            "lucrează doar cu inconștientul individual",
            "respinge ideea de obiective terapeutice",
        ],
        "correct": "a",
    },
    # —— Abordare experiențială (26–30) ——
    {
        "stem": "Abordarea experiențială în terapia de familie (ex. Virginia Satir, Carl Whitaker) pune accent pe:",
        "options": [
            "exprimarea emoțiilor, autenticitate și contact afectiv între membri",
            "restructurarea cognitivă individuală, fără lucrul cu relațiile",
            "pedeapsa consecventă a membrului cu simptom",
            "evitarea emoțiilor pentru a menține calmul în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Virginia Satir, în terapia de familie experiențială, este cunoscută pentru lucrul cu:",
        "options": [
            "stilurile de comunicare și creșterea stimei de sine în relații",
            "granițele difuze și ierarhia subsistemelor",
            "genograma multigenerațională boweniană",
            "prescrierea simptomului ca tehnică principală",
        ],
        "correct": "a",
    },
    {
        "stem": "Carl Whitaker, în terapia de familie experiențială, este asociat cu:",
        "options": [
            "spontaneitatea terapeutului, provocarea și explorarea simbolică a dinamicii familiale",
            "protocolul rigid de restructurare cognitivă",
            "condiționarea operantă a comportamentelor",
            "interpretarea autoritară a visului freudian",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea experiențială, clientul este încurajat să:",
        "options": [
            "exprime emoții autentice și să îmbunătățească comunicarea directă în familie",
            "evite contactul emoțional pentru a reduce conflictul",
            "accepte pasiv că simptomul nu ține de relații",
            "se concentreze doar pe interpretarea trecutului freudian",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi abordare–accent sunt corecte în terapia de familie?",
        "options": [
            "sistemică — reguli, feedback, homeostazie, cauzalitate circulară",
            "structurală — granițe, subsisteme, ierarhie (Salvador Minuchin)",
            "strategică — intervenții directe, prescrierea simptomului (Jay Haley)",
            "psihodinamică — token economy și întărire comportamentală",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un adolescent devine mesager între părinți aflați în conflict. Terapeutul structural ar observa triangulare; terapeutul strategic ar căuta comportamentul care menține problema; terapeutul experiențial ar încuraja:",
        "options": [
            "exprimarea directă a emoțiilor și a nevoilor între membri",
            "evitarea oricărei discuții despre conflict",
            "interpretarea visului adolescentului ca singură intervenție",
            "lucrul exclusiv individual, fără părinți",
        ],
        "correct": "a",
    },
]
