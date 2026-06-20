"""Itemi — predare directă/indirectă, nivel conceptual (30 itemi, ID 10861–10890)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PREDARE_STILURI_ITEMS: List[Item] = [
    # —— 1–10: directă vs indirectă ——
    {
        "stem": (
            "Studiile citate în curs sugerează că predarea indirectă poate determina "
            "un nivel mai înalt al învățării decât predarea strict directă, mai ales "
            "când elevii sunt implicați activ."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Predarea directă se caracterizează prin:"
        ),
        "options": [
            "control mai mare al profesorului asupra procesului, explicații clare, "
            "structurarea sarcinii și conducere explicită a învățării",
            "lăsarea integrală a descoperirii elevului, fără ghidare sau structură",
            "renunțarea la explicații în favoarea memorării mecanice",
            "intervenția profesorului se limitează la notarea lucrărilor, fără explicații",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două elemente aparțin predării directe?"
        ),
        "options": [
            "explicații clare și structurate ale conținutului",
            "conducerea explicită a pașilor de învățare",
            "investigarea autonomă fără întrebări din partea profesorului",
            "dialog deschis în care elevul stabilește singur obiectivele lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei componente definesc predarea indirectă?"
        ),
        "options": [
            "crearea de contexte de descoperire și explorare",
            "întrebări și dialog care solicită gândirea elevului",
            "investigare și autonomie cognitivă ghidată",
            "dictarea mecanică a manualului, fără participare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Predarea indirectă presupune că profesorul:"
        ),
        "options": [
            "creează situații în care elevul descoperă, investighează și gândește activ",
            "transmite integral conținutul fără a permite întrebări",
            "renunță la feedback și la evaluarea formativă",
            "controlează pas cu pas fiecare răspuns, fără autonomie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru afirmații despre stilurile de predare sunt corecte?"
        ),
        "options": [
            "predarea directă presupune structurarea explicită a sarcinii",
            "predarea directă include explicații clare ale conținutului",
            "predarea indirectă valorifică întrebări, dialog și investigare",
            "predarea indirectă urmărește autonomie cognitivă ghidată, nu abandonul clasei",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Profesorul cu nivel conceptual scăzut percepe sarcina didactică ca:"
        ),
        "options": [
            "transmitere de conținut — elevul trebuie să memoreze pasiv",
            "dezvoltare interactivă a elevului prin întrebări și adaptare",
            "flexibilitate maximă și metode adaptate nevoilor fiecărui copil",
            "investigare autonomă fără rol al profesorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături descriu profesorul cu nivel conceptual mediu?"
        ),
        "options": [
            "percepe rolul ca interactiv — nu doar transmițător",
            "urmărește dezvoltarea elevului, nu memorarea pasivă",
            "vede elevul ca recipient pasiv al informației",
            "evită dialogul și adaptarea la reacțiile clasei",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul cu nivel conceptual înalt folosește metode adaptate nevoilor "
            "și nivelului copilului, este flexibil și eficient."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care trei trăsături definesc nivelul conceptual înalt al profesorului?"
        ),
        "options": [
            "metode adaptate nevoilor și nivelului copilului",
            "flexibilitate în alegerea strategiilor didactice",
            "eficiență în atingerea obiectivelor de învățare",
            "transmitere rigidă, identică pentru toți, fără adaptare",
        ],
        "correct": "abc",
    },
    # —— 11–20: aplicare, studii, nivele ——
    {
        "stem": (
            "Care două practici aparțin predării directe eficiente?"
        ),
        "options": [
            "structurarea clară a sarcinii și a pașilor de lucru",
            "conducerea explicită a învățării cu explicații ordonate",
            "lăsarea elevilor fără orientare pentru a descoperi singuri tot",
            "renunțarea la verificarea înțelegerii în timpul lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În predarea indirectă, rolul întrebărilor și al dialogului este:"
        ),
        "options": [
            "central — solicită gândirea, descoperirea și participarea activă",
            "secundar — profesorul explică, elevul ascultă pasiv",
            "inexistent — se evită pentru a economisi timp",
            "limitat la repetarea definițiilor din manual",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei activități reflectă predarea indirectă?"
        ),
        "options": [
            "investigare ghidată sau rezolvare de probleme deschise",
            "discuție și argumentare pe baza materialului studiat",
            "proiecte sau situații-problemă cu descoperire parțială",
            "copierea textului de pe tablă, fără procesare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "La nivel conceptual scăzut, elevul este văzut ca:"
        ),
        "options": [
            "receptor pasiv care trebuie să memoreze informația transmisă",
            "partener activ în construirea cunoștințelor",
            "cercetător autonom care își stabilește singur obiectivele",
            "co-facilitator al lecției alături de profesor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două diferențe între nivel conceptual mediu și cel scăzut sunt "
            "formulate corect?"
        ),
        "options": [
            "mediu: rol interactiv; scăzut: transmitere și memorare pasivă",
            "mediu: urmărește dezvoltarea elevului; scăzut: accent pe acumulare mecanică",
            "mediu: exclude dialogul; scăzut: pune întrebări deschise",
            "scăzut: flexibilitate maximă; mediu: rigiditate procedurală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru caracteristici aparțin predării directe?"
        ),
        "options": [
            "control mai mare al procesului de către profesor",
            "explicații clare ale conținutului",
            "structurarea sarcinii de învățare",
            "conducerea explicită a lecției",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Concluzia studiilor despre predarea indirectă, menționată în curs, este "
            "că aceasta poate produce învățare mai profundă atunci când:"
        ),
        "options": [
            "elevii sunt implicați activ — gândesc, discută, investighează",
            "profesorul renunță la structură și la obiective",
            "conținutul este eliminat în favoarea jocului liber",
            "evaluarea se limitează la teste de memorare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Nivelul conceptual înalt se distinge de cel mediu prin adaptarea fină "
            "la nevoile și nivelul fiecărui elev."
        ),
        "options": [
            "adevărat — înaltul personalizează metodele; mediul e interactiv, dar "
            "mai puțin fin adaptat",
            "fals — mediul presupune adaptare identică cu nivelul înalt",
            "adevărat — nivelul scăzut e cel mai flexibil în practică",
            "fals — nivelul înalt respinge orice explicație directă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Predarea directă este întotdeauna superioară predării indirecte, "
            "indiferent de vârsta elevilor sau de tipul conținutului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care patru elemente definesc predarea indirectă în sinteza cursului?"
        ),
        "options": [
            "contexte de descoperire",
            "întrebări și dialog",
            "investigare",
            "autonomie cognitivă ghidată",
        ],
        "correct": "abcd",
    },
    # —— 21–30: sinteză, capcane, grilă ——
    {
        "stem": (
            "Conducerea explicită a învățării, în predarea directă, înseamnă:"
        ),
        "options": [
            "profesorul orientează pașii, clarifică obiectivele și structurează parcursul",
            "elevul decide singur integral ordinea și conținutul, fără ghidare",
            "lecția se desfășoară fără plan și fără încheiere",
            "profesorul evită explicațiile pentru a nu „încărca” elevii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două avantaje potențiale ale predării indirecte sunt susținute de "
            "cercetări, când elevii participă activ?"
        ),
        "options": [
            "învățare mai profundă și retenție mai bună prin implicare cognitivă",
            "dezvoltarea autonomiei și a gândirii critice",
            "memorare mecanică mai rapidă decât la predarea directă",
            "reducerea la zero a rolului profesorului în clasă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul cu nivel conceptual scăzut consideră că metodele indirecte "
            "sunt inutile deoarece elevul trebuie să primească informația gata făcută."
        ),
        "options": [
            "adevărat — la acest nivel, sarcina e văzută ca transmitere pasivă",
            "fals — nivelul scăzut presupune flexibilitate și investigare",
            "adevărat — nivelul înalt respinge orice explicație directă",
            "fals — nivelul mediu presupune memorare fără interacțiune",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două idei descriu trecerea de la nivel conceptual scăzut la mediu?"
        ),
        "options": [
            "de la transmitere pasivă la rol interactiv al profesorului",
            "de la memorare la urmărirea dezvoltării elevului",
            "de la flexibilitate maximă la rigiditate totală",
            "de la investigare la dictare mecanică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Nivelul conceptual al profesorului este fix de la formarea inițială și "
            "nu se poate dezvolta prin experiență și reflecție."
        ),
        "options": [
            "adevărat — nivelul conceptual e determinat genetic",
            "fals — nivelul poate crește prin practică, formare și autoreflecție",
            "adevărat — stilul de predare preferat fixează nivelul conceptual pe viață",
            "fals — nivelul scăzut e superior celui înalt la examen",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care trei niveluri ale conceptualizării profesorului sunt distinse în curs?"
        ),
        "options": [
            "scăzut — transmitere, memorare pasivă",
            "mediu — rol interactiv, dezvoltarea elevului",
            "înalt — metode adaptate, flexibilitate, eficiență",
            "absent — profesorul fără reprezentări despre învățare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două situații favorizează folosirea predării indirecte?"
        ),
        "options": [
            "conținut care poate fi descoperit prin investigare sau problemă",
            "clase în care elevii pot participa la dialog și gândire activă",
            "introducerea unui concept complet nou, fără niciun reper anterior",
            "timp zero pentru pregătirea activităților de explorare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Structurarea sarcinii, în predarea directă, presupune:"
        ),
        "options": [
            "clarificarea pașilor, a materialelor și a criteriilor de reușită",
            "organizarea logică a activității pentru a facilita înțelegerea",
            "lăsarea elevilor fără orientare pentru a crește autonomia",
            "acoperirea manualului pagină cu pagină, fără obiective",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două condiții sporesc eficiența predării indirecte, conform sintezei "
            "cursului?"
        ),
        "options": [
            "implicare activă a elevilor — gândire, discuție, aplicare",
            "contexte de descoperire bine proiectate de profesor",
            "memorare pasivă fără întrebări sau investigare",
            "lecții fără obiective și fără feedback din partea profesorului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru grilă, diferența rapidă între predarea directă și cea indirectă este:"
        ),
        "options": [
            "conducere explicită și explicații structurate vs descoperire, dialog "
            "și autonomie cognitivă ghidată",
            "predare fără profesor vs predare fără elevi",
            "memorare pasivă în ambele stiluri, fără diferențe",
            "nivel conceptual scăzut vs nivel conceptual înalt ca sinonime",
        ],
        "correct": "a",
    },
]

assert len(PREDARE_STILURI_ITEMS) == 30
