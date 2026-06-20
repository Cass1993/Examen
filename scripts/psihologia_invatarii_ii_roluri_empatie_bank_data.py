"""Itemi — roluri profesionale, empatie și orientare helping (40 itemi, ID 10891–10930)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ROLURI_EMPATIE_ITEMS: List[Item] = [
    # —— 1–10: roluri profesionale ——
    {
        "stem": (
            "Modelul optim al profesorului combină empatia, competența profesională "
            "și procedurile didactice eficiente."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Rolul de profesor „Socrate” pune accentul pe:"
        ),
        "options": [
            "dialog, întrebări, dezbatere și explorarea perspectivelor",
            "conducere fermă, reguli stricte și disciplină administrativă",
            "eficiență, pragmatism și stimularea performanței măsurabile",
            "notare rapidă și acoperirea programului fără discuție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două practici aparțin rolului de profesor „Socrate”?"
        ),
        "options": [
            "formularea de întrebări care provoacă gândirea",
            "dezbaterea și explorarea mai multor perspective",
            "impunerea unui singur răspuns corect, fără argumentare",
            "evaluarea concentrată pe teste tip grilă, cu dialog redus la minimum",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul „organizator al minților” se concentrează pe:"
        ),
        "options": [
            "ordine cognitivă, structurare, clarificare și ghidarea gândirii",
            "explorare liberă fără structură sau clarificare",
            "stimularea competiției individuale, fără cooperare",
            "transmiterea mecanică a manualului, fără organizare mentală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături definesc rolul de organizator al minților?"
        ),
        "options": [
            "structurarea informației pentru claritate cognitivă",
            "ghidarea gândirii elevilor spre înțelegere ordonată",
            "renunțarea la explicații în favoarea memorării brute",
            "lăsarea clasei fără repere sau pași de lucru",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei elemente definesc rolul de profesor expert?"
        ),
        "options": [
            "competență academică solidă în domeniu",
            "modelarea muncii intelectuale — cum se gândește, verifică, argumentează",
            "respectarea rigorii și a standardelor academice în clasă",
            "conducere militară a clasei, fără raționament sau demonstrație",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Rolul de „general” în imaginea de sine profesională accentuează:"
        ),
        "options": [
            "conducere fermă, reguli, disciplină și organizare",
            "dialog socratic și explorarea perspectivelor elevilor",
            "lăsarea elevilor să stabilească singuri toate regulile clasei",
            "renunțarea la structură pentru a maximiza libertatea individuală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două componente aparțin rolului de „general”?"
        ),
        "options": [
            "stabilirea și menținerea regulilor clasei",
            "organizarea activității și a ordinii în grup",
            "concentrarea pe dezbatere liberă, cu limite procedurale minime",
            "concentrarea pe dezbatere liberă, fără limite procedurale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul în rol de „om de afaceri” pune accent pe:"
        ),
        "options": [
            "eficiență, pragmatism, rezultate și stimularea performanței",
            "explorare lentă fără obiective sau criterii clare",
            "sprijin afectiv prioritar, în detrimentul obiectivelor de învățare",
            "dialog socratic extins, fără urmărirea progresului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături definesc rolul de antrenor / coach?"
        ),
        "options": [
            "sprijin și încurajare în procesul de învățare",
            "exercițiu repetat, progres treptat și lucru în echipă",
            "impunerea unui ritm identic, fără feedback individual",
            "evaluare sumativă la final de an, fără antrenament în timpul lecției",
        ],
        "correct": "ab",
    },
    # —— 11–20: ghid, empatie ——
    {
        "stem": (
            "Rolul de „ghid de tură” se caracterizează prin:"
        ),
        "options": [
            "explorare, propunere de trasee, alternative și stimularea curiozității",
            "dictare rigidă a unui singur parcurs, fără variante",
            "concentrare pe disciplină administrativă, fără descoperire",
            "transmitere pasivă, fără orientare sau sugestii de explorare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Profesorii diferă prin combinația dintre empatie și orientare helping — "
            "pot susține elevul profund sau mai formal / procedural."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care trei practici aparțin rolului de „ghid de tură”?"
        ),
        "options": [
            "propunerea de trasee sau parcursuri de explorare",
            "oferirea de alternative și căi de descoperire",
            "stimularea curiozității și a investigării",
            "fixarea unui singur răspuns, fără posibilitate de explorare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profesorul cu empatie și orientare helping bune:"
        ),
        "options": [
            "înțelege elevul, îl susține, îl ascultă și îl ajută să se dezvolte",
            "aplică proceduri standard fără a lua în calcul starea elevului",
            "evită contactul personal pentru a păstra distanță profesională rigidă",
            "concentrează dialogul pe notare, nu pe nevoile elevului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două comportamente reflectă orientarea helping autentică?"
        ),
        "options": [
            "ascultarea activă a elevului și a dificultăților sale",
            "sprijinul orientat spre dezvoltarea și progresul elevului",
            "interacțiunea limitată la formulare tipizate, fără înțelegere",
            "concentrarea pe sancțiuni, nu pe nevoile de învățare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru perechi rol–accent principal sunt corecte?"
        ),
        "options": [
            "Socrate — dialog, întrebări, dezbatere",
            "organizator al minților — structurare, clarificare, ghidarea gândirii",
            "expert — competență academică și modelarea muncii intelectuale",
            "general — conducere fermă, reguli, disciplină, organizare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Modelarea muncii intelectuale, în rolul de profesor expert, înseamnă:"
        ),
        "options": [
            "arătarea cum se gândește, verifică și argumentează un specialist în domeniu",
            "citirea manualului în clasă, fără demonstrație de raționament",
            "lăsarea elevilor fără exemplu de rigoare intelectuală",
            "evitarea explicațiilor pentru a nu „încărca” elevii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Orientarea helping formală / procedurală se deosebește de cea profundă "
            "prin faptul că:"
        ),
        "options": [
            "respectă formele de sprijin, dar rămâne la suprafața nevoilor elevului",
            "implică înțelegere autentică, ascultare și sprijin orientat spre dezvoltare",
            "exclude orice contact cu elevul sau orice feedback",
            "înlocuiește complet competența didactică și procedurile eficiente",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Empatia fără competență didactică este suficientă pentru a produce "
            "învățare profundă la toți elevii."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Competența profesională fără empatie poate duce la:"
        ),
        "options": [
            "rigiditate și distanță relațională față de elevi",
            "climat de clasă rece, în care elevul se simte neînțeles",
            "sprijin afectiv optim și ascultare autentică",
            "flexibilitate relațională și încredere ridicată implicită",
        ],
        "correct": "a",
    },
    # —— 21–30: model optim, comparații ——
    {
        "stem": (
            "Care două componente aparțin modelului optim al profesorului?"
        ),
        "options": [
            "empatie și orientare helping autentică",
            "competență profesională și proceduri didactice eficiente",
            "memorare pasivă ca strategie principală",
            "distanță relațională maximă pentru obiectivitate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două diferențe între rolul „Socrate” și cel de „general” sunt "
            "formulate corect?"
        ),
        "options": [
            "Socrate: dialog și explorare; general: reguli și organizare fermă",
            "Socrate: întrebări și perspective; general: disciplină și conducere",
            "Socrate: eficiență pragmatică; general: dezbatere deschisă",
            "Socrate: transmitere mecanică; general: investigare liberă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei roluri profesionale și accentele lor sunt asociate corect?"
        ),
        "options": [
            "om de afaceri — eficiență, pragmatism, rezultate",
            "antrenor / coach — sprijin, exercițiu, progres, echipă",
            "ghid de tură — explorare, trasee, alternative, curiozitate",
            "expert — disciplină administrativă fără modelare intelectuală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două diferențe între antrenor / coach și ghid de tură sunt corecte?"
        ),
        "options": [
            "coach: sprijin, exercițiu repetat, progres; ghid: explorare și trasee",
            "coach: lucru în echipă și antrenament; ghid: alternative și curiozitate",
            "coach: dictare rigidă; ghid: reguli stricte de conduită",
            "coach: fără feedback; ghid: fără orientare sau sugestii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Clarificarea gândirii elevilor, în rolul de organizator al minților, "
            "presupune:"
        ),
        "options": [
            "reorganizarea ideilor, explicitarea pașilor logici și eliminarea confuziei",
            "lăsarea elevilor fără repere în fața informației nestructurate",
            "memorarea mecanică fără înțelegere a relațiilor dintre concepte",
            "evitarea întrebărilor care solicită raționament",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Sprijinul helping formal, fără empatie autentică, este echivalent cu "
            "susținerea profundă a dezvoltării elevului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care patru trăsături definesc rolul de antrenor / coach?"
        ),
        "options": [
            "sprijin și încurajare în învățare",
            "exercițiu și antrenament pentru progres",
            "lucru în echipă și cooperare",
            "urmărirea progresului individual și de grup",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Competența fără empatie poate produce distanță relațională și rigiditate "
            "în relația cu elevii."
        ),
        "options": [
            "adevărat — elevul poate simți că nu este înțeles, deși conținutul e corect",
            "fals — competența academică garantează automat climat empatic",
            "adevărat — empatia este inutilă dacă profesorul cunoaște materia",
            "fals — rigiditatea apare la empatie excesivă, nu la competență",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două obiective aparțin rolului de „om de afaceri”?"
        ),
        "options": [
            "eficiență și pragmatism în organizarea lecției",
            "stimularea performanței și urmărirea rezultatelor",
            "explorare fără obiective sau criterii de reușită",
            "dezbatere socratică extinsă, fără monitorizarea progresului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei comportamente reflectă empatia și orientarea helping bune?"
        ),
        "options": [
            "înțelegerea situației și a nevoilor elevului",
            "ascultarea activă și susținerea în dificultate",
            "ajutorul orientat spre dezvoltarea elevului, nu spre control",
            "interacțiunea limitată la proceduri administrative tipizate",
        ],
        "correct": "abc",
    },
    # —— 31–40: sinteză, grilă ——
    {
        "stem": (
            "Organizarea clasei, în rolul de „general”, include:"
        ),
        "options": [
            "stabilirea regulilor, a rutinei și a structurii activității",
            "lăsarea grupului fără repere procedurale sau temporale",
            "flexibilitate procedurală maximă, cu reguli negociate ad hoc în clasă",
            "evitarea planificării pentru a rămâne flexibil la nivel informal",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două practici aparțin explorării perspectivei în rolul „Socrate”?"
        ),
        "options": [
            "dezbaterea în care se compară argumente diferite",
            "întrebările care deschid mai multe puncte de vedere",
            "impunerea unui singur răspuns valid, fără discuție",
            "evaluarea bazată pe memorare, fără argumentare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Propunerea de alternative și de trasee, în rolul de ghid de tură, "
            "are rolul de:"
        ),
        "options": [
            "orienta explorarea și a stimula curiozitatea cognitivă",
            "fixa un singur parcurs obligatoriu, fără variante",
            "elimina nevoia de ghidare sau de feedback din partea profesorului",
            "înlocui structurarea conținutului cu activitate aleatorie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei componente definesc modelul optim al profesorului din curs?"
        ),
        "options": [
            "empatie și orientare helping",
            "competență profesională",
            "proceduri didactice eficiente",
            "memorare pasivă ca strategie centrală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Toți profesorii au aceeași combinație de empatie și orientare helping, "
            "indiferent de experiență sau formare."
        ),
        "options": [
            "adevărat — empatia e identică la toți cadrele didactice",
            "fals — profesorii diferă: sprijin profund vs formal / procedural",
            "adevărat — helpingul profund apare automat după primul an de predare",
            "fals — empatia e relevantă la consiliere, nu la predare",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care patru trăsături definesc rolul de „om de afaceri” și al celui de "
            "„expert”, în sinteza pentru grilă?"
        ),
        "options": [
            "om de afaceri: eficiență și pragmatism",
            "om de afaceri: rezultate și stimularea performanței",
            "expert: competență academică",
            "expert: modelarea muncii intelectuale",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care trei diferențe între organizator al minților, expert și general sunt "
            "corecte?"
        ),
        "options": [
            "organizator: ordine cognitivă și ghidarea gândirii",
            "expert: competență și modelare intelectuală",
            "general: reguli, disciplină și organizare fermă",
            "general: explorare liberă fără structură sau conduită",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Înțelegerea elevului, ca parte a empatiei, presupune:"
        ),
        "options": [
            "perceperea situației, a dificultăților și a nevoilor sale de învățare",
            "aplicarea aceleiași proceduri pentru toți, fără diferențiere",
            "concentrarea pe sancțiuni, nu pe motivele comportamentului",
            "evitarea dialogului pentru a menține autoritatea formală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două consecințe pot apărea când lipsește una dintre componentele "
            "modelului optim?"
        ),
        "options": [
            "empatie fără competență: sprijin afectiv insuficient pentru învățare",
            "competență fără empatie: rigiditate și distanță relațională",
            "proceduri eficiente fără empatie: climat mereu optim automat",
            "empatie fără proceduri: organizare didactică impecabilă garantată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru grilă, diferența rapidă între rolul „Socrate” și cel de "
            "„organizator al minților” este:"
        ),
        "options": [
            "Socrate: dialog, întrebări, dezbatere; organizator: structurare, "
            "clarificare, ordine cognitivă",
            "Socrate: disciplină fermă; organizator: explorare fără structură",
            "Socrate: eficiență pragmatică; organizator: stimularea performanței",
            "Socrate: modelare intelectuală; organizator: reguli administrative",
        ],
        "correct": "a",
    },
]

assert len(ROLURI_EMPATIE_ITEMS) == 40
