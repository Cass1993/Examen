"""Itemi — JVIS (inventar interese vocaționale Jackson), lot evaluare psihologică II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

JVIS_ITEMS: List[Item] = [
    # —— General (1–10) ——
    {
        "stem": (
            "Care este scopul principal al inventarului de interese vocaționale "
            "Jackson (JVIS)?"
        ),
        "options": [
            "măsurarea intereselor vocaționale",
            "sprijinirea consilierii vocaționale",
            "diagnosticarea tulburărilor de personalitate severe",
            "măsurarea exclusivă a coeficientului de inteligență generală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Câte perechi de afirmații și câte scale include forma standard "
            "a inventarului de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "289 perechi de afirmații",
            "34 de scale",
            "câte 17 itemi pe fiecare scală",
            "50 de scale, câte 10 itemi fiecare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În structura inventarului de interese vocaționale Jackson (JVIS), 26 de scale "
            "măsoară roluri profesionale, iar 8 scale măsoară stiluri de muncă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Pe ce eșantion s-a realizat adaptarea în limba română a inventarului "
            "de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "aproximativ 3500 de persoane",
            "un eșantion românesc utilizat pentru normare",
            "sub 100 de participanți, fără standardizare",
            "studenți la medicină din străinătate, fără alte populații",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Inventarul de interese vocaționale Jackson (JVIS) poate fi administrat:"
        ),
        "options": [
            "individual",
            "colectiv, în grup",
            "doar în cadru spitalicesc, cu observare clinică obligatorie",
            "varianta online, fără administrare pe hârtie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce tip de informație oferă inventarul de interese vocaționale Jackson (JVIS) "
            "spre deosebire de un test pur de aptitudine?"
        ),
        "options": [
            "preferințe pentru domenii și activități profesionale",
            "orientări vocaționale utile în consiliere",
            "măsurarea directă a competențelor motorii fine",
            "nivelul anxietății de performanță, fără interese vocaționale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Cum sunt organizate itemii în cadrul fiecărei scale a inventarului "
            "de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "17 itemi pe scală",
            "perechi de afirmații între care subiectul alege preferința",
            "răspuns liber scris, fără variante predefinite",
            "o singură afirmație pe scală, cu răspuns da/nu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Inventarul de interese vocaționale Jackson (JVIS) măsoară exclusiv stiluri "
            "de muncă, fără scale pentru roluri profesionale."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce este relevantă normarea pe eșantion românesc (aproximativ "
            "3500 de persoane) pentru interpretarea scorurilor?"
        ),
        "options": [
            "permite compararea rezultatelor cu o populație de referință locală",
            "sprijină utilizarea clinică și vocațională în context românesc",
            "reduce nevoia de validare a profilului, nu o elimină",
            "face inutilă analiza consistenței răspunsurilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În consilierea vocațională, inventarul de interese vocaționale "
            "Jackson (JVIS) este util deoarece:"
        ),
        "options": [
            "structurează discuția despre preferințe profesionale",
            "oferă un profil ocupațional pe multiple dimensiuni",
            "suplimentează interviul cu clientul, nu îl înlocuiește",
            "măsoară doar abilități cognitive, nu interese",
        ],
        "correct": "ab",
    },
    # —— Concepte și teme ocupaționale (11–20) ——
    {
        "stem": (
            "Ce descrie corect „profilul ocupațional” în interpretarea "
            "inventarului de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "configurația scorurilor pe dimensiuni tipice ale intereselor fundamentale",
            "imaginea preferințelor vocaționale ale persoanei evaluate",
            "un singur scor global care înlocuiește toate scalele",
            "lista simptomelor psihopatologice",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un „rol de muncă” în inventarul de interese vocaționale Jackson "
            "(JVIS) se referă la:"
        ),
        "options": [
            "un domeniu sau o ocupație, cum ar fi Dreptul sau Științele fizice",
            "preferința pentru un tip concret de activitate profesională",
            "modul preferat de organizare a timpului la birou",
            "stilul interpersonal, fără conținut ocupațional",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un „stil de muncă” în inventarul de interese vocaționale Jackson "
            "(JVIS) descrie:"
        ),
        "options": [
            "modul preferat de lucru, cum ar fi planificarea sau independența",
            "preferințe transversale, aplicabile în mai multe domenii",
            "obligatoriu o singură profesie reglementată prin lege",
            "doar interesul pentru activități artistice",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scalele au "
            "fost construite astfel încât să măsoare conceptul din denumire și "
            "să fie relativ puțin corelate între ele."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dintre următoarele sunt teme ocupaționale generale din modelul "
            "Holland extins, folosit la inventarul de interese vocaționale "
            "Jackson (JVIS)?"
        ),
        "options": [
            "expresiv și logic",
            "curios și practic",
            "comunicativ și orientat spre ajutorare",
            "paranoic și evitant",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Cele zece teme ocupaționale generale din JVIS includ, printre altele:"
        ),
        "options": [
            "asertiv, socializat, convențional",
            "întreprinzător, comunicativ",
            "expresiv, curios, practic",
            "obsesiv-compulsiv, depersonalizat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), diferența "
            "dintre un rol de muncă și un stil de muncă este că:"
        ),
        "options": [
            "rolul vizează domeniul sau ocupația concretă",
            "stilul vizează modul preferat de lucru, transversal mai multor domenii",
            "rolul și stilul sunt mereu identice ca scor",
            "stilul se măsoară doar la scalele de la 1 la 10",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul Holland extins folosit la inventarul de interese "
            "vocaționale Jackson (JVIS), un candidat atras de consiliere, "
            "asistență socială sau activități educaționale și medicale are "
            "preferință pentru:"
        ),
        "options": [
            "sprijin, consiliere sau asistență a altor persoane",
            "servicii sociale, educaționale sau medicale",
            "lucru izolat cu mașini, fără contact uman",
            "organizare strict birocratică, fără relații",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), corelarea "
            "foarte ridicată între toate scalele este un obiectiv de design "
            "al instrumentului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Exemplu de potrivire corectă între concept și scală în inventarul "
            "de interese vocaționale Jackson (JVIS):"
        ),
        "options": [
            "rol de muncă — interes pentru Drept",
            "stil de muncă — preferință pentru Planificare",
            "rol de muncă — Independență ca mod de lucru",
            "stil de muncă — interes pentru Medicină ca domeniu",
        ],
        "correct": "ab",
    },
    # —— Familii de scale și interpretare profil (21–30) ——
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scoruri ridicate "
            "la scalele de arte și activități expresive indică preferința pentru:"
        ),
        "options": [
            "expresie creativă, estetică sau performativă",
            "activități investigative de laborator",
            "lucrul birocratic cu documente",
            "activități outdoor, fără componentă artistică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), familiile de "
            "scale orientate spre știință și matematică măsoară interesul pentru:"
        ),
        "options": [
            "cercetare, analiză și rezolvare de probleme",
            "domenii investigative și tehnice",
            "activități de vânzare și negociere comercială",
            "activități artistice, fără componentă logică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un tânăr cu scoruri ridicate la scalele outdoor din JVIS preferă "
            "probabil activități:"
        ),
        "options": [
            "în aer liber, cu componentă practică și fizică",
            "activități de birou, teoretice, fără contact cu natura",
            "strict juridice sau legislative",
            "de predare universitară, fără componentă practică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele familii tematice de scale din JVIS acoperă "
            "interesul pentru servicii administrative, sănătate și afaceri?"
        ),
        "options": [
            "servicii și activități administrative",
            "domeniul medical și al sănătății",
            "afaceri, management și antreprenoriat",
            "domeniul juridic exclusiv",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scalele de "
            "stil interpersonal la locul de muncă și cele de predare/social se "
            "deosebesc prin faptul că:"
        ),
        "options": [
            "primele vizează modul de relaționare și cooperare la job",
            "cele de predare/social vizează educația, formarea sau domenii sociale",
            "ambele măsoară interesul pentru domeniul juridic",
            "niciuna nu are legătură cu relațiile interpersonale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scalele "
            "orientate spre domeniul juridic măsoară interesul pentru:"
        ),
        "options": [
            "legislație, drept și cariere juridice",
            "activități outdoor și sportive",
            "stiluri de planificare și independență la muncă",
            "domeniul medical clinic, fără alte scale JVIS",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scalele de tip "
            "academic și scalele de stil de activitate se deosebesc prin faptul că:"
        ),
        "options": [
            "scalele academice vizează cercetarea și învățământul superior",
            "scalele de stil de activitate vizează preferințe transversale de lucru",
            "ambele măsoară interesul pentru medicină",
            "scalele academice măsoară doar aptitudinea cognitivă, nu interesul",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care preferințe transversale măsoară scalele de stil de activitate "
            "la muncă din inventarul de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "independență",
            "planificare",
            "încredere interpersonală",
            "expresivitate artistică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un adolescent cu scoruri ridicate la scalele JVIS de știință/matematică "
            "și la cele academice ar putea fi orientat spre:"
        ),
        "options": [
            "facultăți cu profil analitic sau universitar",
            "cercetare sau învățământ superior",
            "doar meserii outdoor, fără componentă intelectuală",
            "domeniul juridic, fără alte scale JVIS",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scalele din "
            "familia afacerilor măsoară preferința pentru:"
        ),
        "options": [
            "management, vânzări și antreprenoriat",
            "activități comerciale și de conducere",
            "activități artistice expresive, fără componentă logică",
            "lucrul izolat în laborator, fără contact cu publicul",
        ],
        "correct": "ab",
    },
    # —— Fidelitate profil și indici administrativi (31–40) ——
    {
        "stem": (
            "Când numărul de răspunsuri nescorabile la JVIS este "
            "egal sau mai mare de 10, consecința administrativă este:"
        ),
        "options": [
            "profilul ocupațional nu se calculează",
            "rezultatele nu pot fi interpretate ca profil valid",
            "toate scalele primesc automat scor T de 50",
            "testul se consideră mereu valid, indiferent de răspunsuri",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Indicele de consistență a răspunsurilor la JVIS "
            "sub pragul de 0,50 indică:"
        ),
        "options": [
            "necesitatea interpretării cu precauție",
            "posibilă lipsă de atenție sau răspunsuri contradictorii",
            "validare automată a profilului",
            "scoruri extreme garantat corecte",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Indicele de infrecvență la JVIS reflectă:"
        ),
        "options": [
            "proporția de răspunsuri „da” neobișnuit de frecvente",
            "tendința de a accepta afirmații atipice pentru populația generală",
            "viteza de citire a subiectului",
            "coeficientul de inteligență verbală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profilul JVIS este invalidat când:"
        ),
        "options": [
            "atât consistența, cât și infrecvența sunt anormale",
            "ambele indici depășesc pragurile de invalidare stabilite",
            "doar o scală are scor T ușor peste 60",
            "subiectul completează testul în timp normal",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă un candidat are 12 răspunsuri nescorabile la JVIS, "
            "consilierul vocațional ar trebui să:"
        ),
        "options": [
            "nu calculeze sau nu interpreteze profilul ocupațional",
            "readministreze testul sau clarifice instrucțiunile",
            "emite recomandări de carieră fără a explora inconsistențele din profil",
            "convertească automat răspunsurile în scoruri T medii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un indice de consistență de 0,42 la JVIS sugerează "
            "că interpretarea profilului trebuie făcută cu precauție."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Infrecvența ridicată a răspunsurilor „da” poate indica acceptarea "
            "excesivă a afirmațiilor, ceea ce afectează validitatea profilului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care indici administrativi ai JVIS evaluează "
            "fidelitatea sau validitatea profilului înainte de interpretare?"
        ),
        "options": [
            "numărul de răspunsuri nescorabile",
            "consistența răspunsurilor",
            "infrecvența răspunsurilor",
            "lungimea exactă a fiecărui răspuns scris liber",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce se verifică validitatea profilului înainte de a interpreta "
            "scorurile T la JVIS?"
        ),
        "options": [
            "răspunsurile aleatorii sau neatenționate distorsionează profilul",
            "fără profil valid, recomandările vocaționale pot fi înșelătoare",
            "validitatea elimină nevoia de norme românești",
            "scorurile T nu se aplică niciodată după verificarea validității",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un profil cu consistență normală dar cu infrecvență extremă poate "
            "fi totuși considerat valid fără nicio rezervă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Domenii de aplicare și distorsiuni (41–50) ——
    {
        "stem": (
            "În ce contexte se aplică inventarul de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "orientare școlară și universitară",
            "consiliere vocațională",
            "recrutare și selecție de personal",
            "studii în psihologia muncii și organizațională",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În recrutare, JVIS poate ajuta la:"
        ),
        "options": [
            "evaluarea potrivirii interes–post",
            "completarea interviului de carieră cu date structurate",
            "diagnosticarea exclusivă a psihozei",
            "înlocuirea completă a probei de lucru practice",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Semnele unui profil „fake good” (prezentare socială dorită) în JVIS "
            "pot include:"
        ),
        "options": [
            "desirabilitate socială crescută",
            "profil plat, cu multe scale foarte apropiate",
            "scoruri T peste 70 la numeroase scale simultan",
            "scoruri extrem de scăzute la toate scalele",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Profilul „fake bad” (prezentare negativă exagerată) se caracterizează "
            "prin:"
        ),
        "options": [
            "simptome sau preferințe exagerate negative",
            "scoruri foarte scăzute, neobișnuit de uniforme",
            "profil plat cu toate scalele peste 70",
            "timp de completare normal și pattern coerent",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care indicii sugerează răspuns aleatoriu la JVIS?"
        ),
        "options": [
            "pattern bizar de răspunsuri (ex. aceeași opțiune repetată sistematic)",
            "timp de completare foarte scurt, neplauzibil",
            "scale contradictorii între ele, fără logică în profil",
            "consistență ridicată și infrecvență normală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Distorsiunile de tip self-report la JVIS trebuie luate "
            "în calcul pentru că pot masca interesele reale ale persoanei."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un profil plat, cu multe scale T apropiate de 50, poate sugera "
            "lipsă de diferențiere reală sau încercare de a părea „mediu” "
            "pe toate dimensiunile."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În interpretarea distorsiunilor, consilierul vocațional ar trebui să:"
        ),
        "options": [
            "coroboreze profilul cu interviul și istoricul persoanei",
            "verifice validitatea administrativă înainte de concluzii",
            "tratează indiciile de fake good ca pe zgomot de măsurare",
            "presupună automat că toate scorurile înalte sunt reale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce este util JVIS în orientarea universitară?"
        ),
        "options": [
            "ajută la identificarea domeniilor compatibile cu interesele elevului",
            "completează informațiile despre performanță școlară cu preferințe vocaționale",
            "elimină necesitatea dialogului cu consilierul",
            "măsoară doar stiluri de muncă, nu roluri profesionale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pattern-ul de răspunsuri contradictorii între scale înrudite poate "
            "indica răspuns neatenționat sau aleatoriu, nu un profil vocațional "
            "coerent."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Scoruri T și cei 5 pași de interpretare (51–60) ——
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), un scor T "
            "între 40 și 60 la o scală indică nivel mediu, în jurul aproximativ "
            "a 68% din populația de referință (± o deviație standard)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scorurile T "
            "între 60 și 70 sau între 30 și 40 sunt considerate:"
        ),
        "options": [
            "înalt sau scăzut (aproximativ ±1–2 deviații standard)",
            "prezente la circa 14% din populație, pentru fiecare capăt",
            "extreme, prezente la doar 2% din populație",
            "mereu invalide din punct de vedere administrativ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În inventarul de interese vocaționale Jackson (JVIS), scorurile T "
            "peste 70 sau sub 30:"
        ),
        "options": [
            "sunt extreme (aproximativ ±2 deviații standard)",
            "apar la circa 2% din populație și necesită atenție specială la interpretare",
            "sunt întotdeauna semn de invalidare a profilului",
            "nu au nicio relevanță pentru consilierea vocațională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care este primul pas în interpretarea profilului inventarului "
            "de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "verificarea validității profilului",
            "evaluarea răspunsurilor nescorabile, consistenței și infrecvenței",
            "emiterea imediată a recomandărilor de carieră",
            "analiza pattern-urilor între scale, fără verificări prealabile",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care secvențe respectă ordinea celor cinci pași de interpretare a "
            "profilului inventarului de interese vocaționale Jackson (JVIS)?"
        ),
        "options": [
            "validitate → scoruri relevante → grupări de scale",
            "analiză de pattern → concluzii și recomandări",
            "concluzii imediate, fără verificarea validității",
            "grupări de scale înainte de orice verificare a profilului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La interpretarea profilului inventarului de interese vocaționale "
            "Jackson (JVIS), imediat după verificarea validității profilului, "
            "următorul pas vizează:"
        ),
        "options": [
            "identificarea scorurilor cu deviații semnificative de la medie",
            "scalele relevante diagnostic, cu T înalt sau scăzut",
            "invalidarea automată a profilului",
            "raportarea scorurilor brute fără verificarea valorilor extreme",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La interpretarea profilului inventarului de interese vocaționale "
            "Jackson (JVIS), după identificarea scorurilor cu deviații "
            "semnificative, consilierul grupează scalele pe familii vocaționale "
            "pentru a:"
        ),
        "options": [
            "organizarea scalelor în familii (ex. știință, afaceri, stiluri)",
            "formularea de ipoteze pe baza familiilor de scale "
            "(arte, știință, afaceri, stiluri etc.)",
            "calcularea coeficientului de inteligență generală",
            "eliminarea scalelor cu scor mediu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La interpretarea profilului inventarului de interese vocaționale "
            "Jackson (JVIS), după pașii 1–3 (validitate, scoruri relevante, "
            "grupări de scale), pasul 4 cere analiza pattern-ului: cum se "
            "combină sau se contrazic scalele între ele în profil. Acest pas "
            "ajută la:"
        ),
        "options": [
            "înțelegerea coerenței profilului vocațional",
            "identificarea combinațiilor de interese compatibile sau contradictorii",
            "înlocuirea discuției clinice cu clientul",
            "anularea normelor românești",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La interpretarea profilului inventarului de interese vocaționale "
            "Jackson (JVIS), pasul 5 — ultimul, după analiza pattern-ului — "
            "constă în formularea concluziilor și a recomandărilor practice "
            "pentru client."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În profilul inventarului de interese vocaționale Jackson (JVIS), "
            "un scor T de 72 la scala „Știință/Matematică” și T de 28 la scala "
            "„Convențional” sugerează, după validarea profilului:"
        ),
        "options": [
            "interes extrem pentru domenii analitice",
            "dezinteres marcat pentru activități birocratice structurate",
            "profil plat, fără diferențe semnificative",
            "invalidare automată a întregului profil",
        ],
        "correct": "ab",
    },
]
