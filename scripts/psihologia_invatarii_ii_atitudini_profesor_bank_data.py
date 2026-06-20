"""Itemi — atitudinile și tipurile de profesor (40 itemi, ID 10821–10860)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ATITUDINI_PROFESOR_ITEMS: List[Item] = [
    # —— 1–10: atitudini, predare, elev, nonverbal ——
    {
        "stem": (
            "Atitudinile profesorului față de predare și învățare pot orienta stilul "
            "didactic — spre profesie, spre elev sau spre sine."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care trei orientări ale atitudinii profesorului sunt frecvent distinse "
            "în literatura didactică?"
        ),
        "options": [
            "față de profesie — identitate, standarde, responsabilitate profesională",
            "față de elev — respect, încredere, sprijin pentru participare",
            "față de sine — autoreflecție, dezvoltare personală, echilibru",
            "față de notă — concentrare pe cifre, fără relație cu învățarea",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două componente aparțin atitudinii față de predare?"
        ),
        "options": [
            "corectitudinea informațiilor transmise elevilor",
            "organizarea conținutului și claritatea instruirii",
            "gestionarea disciplinei prin pedeapsă publică ca metodă principală",
            "renunțarea la planificare în favoarea improvizației totale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei efecte ale atitudinii profesorului față de elev sunt evocate "
            "în psihopedagogie?"
        ),
        "options": [
            "climatul afectiv al clasei",
            "încrederea elevilor și sentimentul de siguranță",
            "disponibilitatea de participare la activitate",
            "memorarea mecanică fără implicare afectivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Elevii receptează frecvent mesajele nonverbale ale profesorului — mimică, "
            "ton, postură — uneori mai puternic decât cuvintele. Care formulare este "
            "corectă?"
        ),
        "options": [
            "adevărat — nonverbalul poate întări sau contrazice mesajul verbal",
            "fals — elevii iau în seamă aproape doar cuvintele rostite",
            "adevărat — nonverbalul înlocuiește complet nevoia de explicație clară",
            "fals — și adolescenții percep tonul, postura și mimică profesorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două canale nonverbale transmit atitudinea profesorului în clasă?"
        ),
        "options": [
            "mimica și expresia facială — plictiseală, interes, dezaprobare",
            "tonul vocii și postura — siguranță, descurajare, disponibilitate",
            "conținutul manualului scris, fără prezența fizică a profesorului",
            "nota din catalog, fără feedback în timpul lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul centrat pe conținut se caracterizează prin:"
        ),
        "options": [
            "selectarea informațiilor esențiale și transmiterea lor structurată",
            "analiza nevoilor fiecărui elev înainte de fiecare activitate",
            "renunțarea la organizarea conținutului în favoarea jocului liber",
            "predare fără obiective sau fără structură logică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două observații despre profesorul centrat pe conținut sunt corecte?"
        ),
        "options": [
            "valorizează rigoarea și claritatea transmiterii materiei",
            "risc: poate neglija relația profesor–elev și climatul afectiv",
            "ignoră în mod necesar corectitudinea informațiilor",
            "exclude structurarea conținutului în lecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul centrat pe interacțiune construiește mediul de învățare "
            "prin relația profesor–elev și prin participarea activă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Profesorul centrat pe elev:"
        ),
        "options": [
            "analizează nevoile elevului, pune întrebări și susține descoperirea",
            "transmite mecanic manualul, fără a ține cont de reacțiile clasei",
            "evită adaptarea personală și diferențierea",
            "se concentrează pe proceduri rigide, fără dialog",
        ],
        "correct": "a",
    },
    # —— 11–20: tipuri de profesor, inițiativă ——
    {
        "stem": (
            "Care două practici reflectă orientarea profesorului centrat pe elev?"
        ),
        "options": [
            "întrebări deschise care solicită gândirea și descoperirea",
            "adaptarea exemplelor și a sprijinului la nevoile elevilor",
            "dictarea integrală a manualului, fără pauze de verificare",
            "compararea publică constantă a elevilor slabi cu cei buni",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul centrat pe interacțiune pune accentul pe:"
        ),
        "options": [
            "construirea mediului de învățare prin relație și participare activă",
            "transmiterea unidirecțională, fără schimb cu elevii",
            "memorarea listelor de definiții, fără activitate de grup",
            "evaluarea sumativă ca singur moment de comunicare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei trăsături descriu profesorul cu inițiativă ridicată?"
        ),
        "options": [
            "organizează flexibil activitatea, în funcție de progresul clasei",
            "stimulează alegerea și implicarea elevilor",
            "dezvoltă responsabilitatea și autonomia în învățare",
            "urmează proceduri rigide, fără ajustare după feedback",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profesorul cu inițiativă scăzută se caracterizează prin:"
        ),
        "options": [
            "predare mai formală, rigidă, centrată pe proceduri și control extern",
            "organizare flexibilă și stimularea alegerilor elevilor",
            "accent pe descoperirea ghidată și pe întrebările elevilor",
            "construirea deliberată a participării active în grup",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două diferențe între profesorul cu inițiativă ridicată și cel cu "
            "inițiativă scăzută sunt corecte?"
        ),
        "options": [
            "ridicată: flexibilitate și stimularea responsabilității elevilor",
            "scăzută: formalism, proceduri fixe, control extern accentuat",
            "ridicată: evită orice planificare sau structură",
            "scăzută: pune întrebări deschise și susține descoperirea",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru tipuri de profesor din clasificarea pentru grilă sunt "
            "descrise corect?"
        ),
        "options": [
            "centrat pe conținut — selectează și structurează informația esențială",
            "centrat pe elev — analizează nevoile, susține descoperirea",
            "centrat pe interacțiune — relație și participare activă",
            "cu inițiativă ridicată — flexibilitate, alegere, responsabilitate",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un ton monoton, postură închisă și mimică de plictiseală transmit "
            "elevilor, în principal, mesaje de:"
        ),
        "options": [
            "descurajare sau dezinteres față de lecție",
            "respect și siguranță emoțională",
            "disponibilitate pentru întrebări și sprijin",
            "încurajare activă a participării",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două atitudini nonverbale susțin climatul afectiv pozitiv?"
        ),
        "options": [
            "contact vizual adecvat și postură deschisă",
            "ton calm, respectuos, care transmite siguranță",
            "suspin repetat și întoarcerea spre tablă, evitând privirea elevilor",
            "brațele încrucișate și răspunsuri uscate la întrebări",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Elevii percep în principal mesajele verbale ale profesorului; "
            "canalele nonverbale au impact minor în clasă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei componente aparțin atitudinii față de predare?"
        ),
        "options": [
            "corectitudinea informațiilor",
            "organizarea conținutului",
            "claritatea instruirii",
            "pedeapsa publică ca metodă principală de motivare",
        ],
        "correct": "abc",
    },
    # —— 21–30: efecte, comparări, capcane ——
    {
        "stem": (
            "Disponibilitatea de participare a elevilor crește cel mai probabil când "
            "profesorul transmite, prin atitudine:"
        ),
        "options": [
            "respect, siguranță și deschidere la întrebări",
            "plictiseală, dezaprobare sau dezinteres vizibil",
            "comparare constantă cu colegii mai performanți",
            "tăcere impusă, fără posibilitate de răspuns",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două caracteristici definesc atitudinea orientată față de profesie?"
        ),
        "options": [
            "respectul pentru standardele și etica meseriei",
            "responsabilitatea pentru calitatea predării și a informației",
            "neglijarea conținutului în favoarea notei finale",
            "lipsa autoreflecției profesionale și a feedback-ului de la colegi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei mesaje nonverbale pot transmite respect și siguranță?"
        ),
        "options": [
            "ascultarea activă a întrebării elevului",
            "ton încurajator, fără umilire publică",
            "postură deschisă și prezență atentă în clasă",
            "evitarea privirii și răspunsuri grăbite, respingătoare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profesorul cu inițiativă scăzută este același lucru cu profesorul centrat "
            "pe elev, deoarece ambii evită controlul rigid. Care răspuns este corect?"
        ),
        "options": [
            "adevărat — inițiativă scăzută și centrat pe elev sunt sinonime",
            "fals — inițiativă scăzută înseamnă rigiditate; centrat pe elev înseamnă "
            "adaptare și descoperire",
            "adevărat — ambii tipuri exclud structurarea conținutului",
            "fals — centrat pe elev presupune formalism și proceduri fixe",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care două diferențe între profesorul centrat pe conținut și cel centrat "
            "pe elev sunt corecte?"
        ),
        "options": [
            "conținut: prioritate la structurarea materiei; elev: prioritate la nevoi "
            "și descoperire",
            "conținut: risc de neglijare a relației; elev: accent pe adaptare personală",
            "conținut: exclude corectitudinea informațiilor; elev: exclude întrebările",
            "ambii renunță la organizarea lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru efecte ale atitudinii profesorului față de elev sunt "
            "enumerate în sinteza cursului?"
        ),
        "options": [
            "climatul afectiv al clasei",
            "încrederea elevilor",
            "sentimentul de siguranță",
            "disponibilitatea de participare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Claritatea instruirii, în cadrul atitudinii față de predare, presupune:"
        ),
        "options": [
            "explicații inteligibile, exemple potrivite, structură logică a lecției",
            "volum maxim de text dictat, fără verificarea înțelegerii",
            "terminologie obscură pentru a filtra elevii slabi",
            "lecție fără obiective comunicate elevilor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două practici reflectă profesorul centrat pe interacțiune?"
        ),
        "options": [
            "activități în perechi sau grupuri cu roluri clare",
            "dialog și feedback continuu între profesor și elevi",
            "monolog de o oră, fără întrebări din partea clasei",
            "evaluare finală fără nicio discuție în timpul lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul centrat pe elev ignoră conținutul curricular și renunță la "
            "transmiterea informațiilor esențiale. Care răspuns este corect?"
        ),
        "options": [
            "adevărat — centrat pe elev înseamnă fără materie și fără structură",
            "fals — centrat pe elev adaptează predarea, dar nu exclude conținutul",
            "adevărat — elevul alege integral programa, fără obiective comune",
            "fals — centrat pe conținut este singurul tip care păstrează curriculumul",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care trei orientări pot modela stilul didactic al profesorului?"
        ),
        "options": [
            "atitudinea față de profesie",
            "atitudinea față de elev",
            "atitudinea față de sine",
            "atitudinea față de pedeapsă ca unic instrument",
        ],
        "correct": "abc",
    },
    # —— 31–40: sinteză, atitudine sine, nonverbal ——
    {
        "stem": (
            "Atitudinea față de sine a profesorului poate include:"
        ),
        "options": [
            "autoreflecție, dezvoltare profesională continuă și echilibru personal",
            "renunțarea la standardele etice ale meseriei",
            "evitarea feedback-ului de la colegi sau mentori",
            "concentrarea pe controlul rigid al clasei, fără reflecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două capcane trebuie evitate când interpretezi tipurile de profesor?"
        ),
        "options": [
            "centrat pe conținut nu înseamnă automat lipsă de respect față de elevi",
            "centrat pe elev nu înseamnă renunțarea la structură și la conținut",
            "inițiativă ridicată înseamnă absența regulilor în clasă",
            "inițiativă scăzută înseamnă competență pedagogică superioară",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru perechi tip de profesor–accent sunt potrivite pentru grilă?"
        ),
        "options": [
            "centrat pe conținut — informație esențială, structurată",
            "centrat pe elev — nevoi, întrebări, descoperire",
            "centrat pe interacțiune — relație, participare activă",
            "inițiativă scăzută — formal, rigid, control extern",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Organizarea conținutului, ca parte a atitudinii față de predare, "
            "înseamnă:"
        ),
        "options": [
            "selecția esențialului, progresie logică și legături între idei",
            "acoperirea mecanică a tuturor paginilor din manual, fără ierarhie",
            "renunțarea la obiective pentru a urmări reacțiile elevilor, fără structură",
            "predare fără plan și fără încheiere de lecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături ale profesorului cu inițiativă ridicată susțin "
            "autonomia elevilor?"
        ),
        "options": [
            "oferirea unor opțiuni reale sau parțiale în modul de lucru",
            "stimularea responsabilității pentru propriul parcurs de învățare",
            "controlul pas cu pas al fiecărui răspuns, fără alegere",
            "predare rigidă după script, fără deviații",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei semnale nonverbale pot reduce participarea elevilor?"
        ),
        "options": [
            "pliciseală vizibilă — căscături, privire la ceas",
            "descurajare — ridicarea ochilor, ton disprețuitor",
            "postură închisă și evitarea contactului vizual",
            "ascultare atentă și încurajare prin gesturi pozitive",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profesorul centrat pe interacțiune și cel cu inițiativă ridicată sunt "
            "identici — amândoi exclud structurarea conținutului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Corectitudinea informațiilor, în atitudinea față de predare, presupune:"
        ),
        "options": [
            "transmiterea fidelă a conținutului științific, fără erori grave",
            "recunoașterea limitelor proprii și corectarea greșelilor când apar",
            "simplificarea până la distorsiunea faptelor pentru a obține note mari",
            "evitarea actualizării cunoștințelor după formarea inițială",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei idei sintetizează rolul atitudinilor profesorului în clasă?"
        ),
        "options": [
            "atitudinile orientează stilul didactic (profesie, elev, sine)",
            "atitudinea față de elev modelează climatul și participarea",
            "mesajele nonverbale transmit adesea mai mult decât cuvintele",
            "atitudinile sunt irelevante dacă manualul este bine structurat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Pentru grilă, diferența rapidă între profesorul cu inițiativă ridicată "
            "și cel cu inițiativă scăzută este:"
        ),
        "options": [
            "flexibilitate, stimularea alegerii și a responsabilității vs formalism "
            "rigid și control extern",
            "transmitere structurată a conținutului vs analiza nevoilor elevului",
            "relație și participare activă vs selectarea informației esențiale",
            "empatie rogersiană vs condiționare operantă skinneriană",
        ],
        "correct": "a",
    },
]

assert len(ATITUDINI_PROFESOR_ITEMS) == 40
