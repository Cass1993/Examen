"""Itemi — mecanisme de apărare/safeguarding: Jung, Adler, Horney, Klein vs Rogers și Gestalt."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

APARARE_ITEMS: List[Item] = [
    # —— Jung (1–8) ——
    {
        "stem": "La Jung, proiecția Umbrei se apropie de proiecția freudiană, dar terapeutul jungian pune accent pe:",
        "options": [
            "integrarea părților respinse și recunoașterea conținutului proiectat",
            "interpretarea sexuală directă a oricărui conflict",
            "eliminarea transferului din relația terapeutică",
            "disputa cognitivă a convingerilor absolute",
        ],
        "correct": "a",
    },
    {
        "stem": "„Posesia” de complex, în limbaj jungian, înseamnă că:",
        "options": [
            "un nucleu emoțional autonom preia parțial controlul comportamentului",
            "clientul simulează conștient o rezistență la contact gestaltică",
            "Eul freudian reușește să medieze perfect pulsiunea",
            "terapeutul rogersian oferă acceptare necondiționată",
        ],
        "correct": "a",
    },
    {
        "stem": "Persona, la Jung, funcționează ca o mască socială și poate deveni problematică atunci când:",
        "options": [
            "clientul se identifică complet cu rolul public și pierde contactul cu sinele",
            "terapeutul folosește experimente gestaltice de polaritate",
            "apare splitting-ul kleinian între obiecte bune și rele",
            "interesul social adlerian este prea dezvoltat",
        ],
        "correct": "a",
    },
    {
        "stem": "Inflația (identificarea cu o imagine arhetipală grandioasă) se deosebește de compensarea adleriană prin faptul că inflația:",
        "options": [
            "implică identificare simbolică cu o imagine de putere, nu strategie de stil de viață",
            "reprezintă interes social matur",
            "este o rezistență la contact de tip deflecție",
            "apare în terapia cognitiv-comportamentală ca etichetă principală",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client vede în toți șefii „tirani persecutori” și reacționează intens. Interpretarea jungiană prioritară:",
        "options": [
            "proiecția conținutului Umbrei neintegrat",
            "safeguarding prin distanțare adleriană",
            "externalizarea conflictului intern, în teoria Karei Horney",
            "retroflexia gestaltică a furiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul jungian, față de gestaltist, abordează proiecția mai ales prin:",
        "options": [
            "amplificare simbolică și integrare a opuselelor",
            "experiment imediat cu scaunul gol în prezent",
            "reflectarea empatică nondirectivă",
            "ierarhie de expunere comportamentală",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi concept–cadru sunt corecte pentru Jung?",
        "options": [
            "Umbra — părți respinse ale personalității",
            "complex — grup de imagini și afecte cu nucleu emoțional",
            "splitting — mecanism kleinian standard",
            "Persona — masca socială",
        ],
        "correct": "abd",
    },
    # —— Adler (9–16) ——
    {
        "stem": "Tendințele de autoprotecție (safeguarding) la Adler includ mai ales:",
        "options": [
            "agresiunea, distanțarea și inhibiția (ținerea la distanță)",
            "splitting-ul și proiecția identificatoare",
            "acceptarea necondiționată și congruența",
            "desensibilizarea sistematică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client amână constant sarcinile importante, dar oferă scuze logice. "
            "În psihologia individuală (Alfred Adler), acest comportament ar fi numit mai probabil:"
        ),
        "options": [
            "safeguarding prin inhibiție sau evitare a eșecului",
            "poziție depresivă kleiniană",
            "introiecție gestaltică a normelor familiale",
            "restructurare beckiană a gândurilor automate",
        ],
        "correct": "a",
    },
    {
        "stem": "Compensarea inferiorității la Adler se deosebește de compensarea freudiană prin faptul că adleriană:",
        "options": [
            "vizează stilul de viață și orientarea spre superioritate sau demnitate",
            "canalizează pulsul sexual spre artă",
            "aparține poziției paranoid-schizoidă",
            "este o tehnică rogersiană de reflectare",
        ],
        "correct": "a",
    },
    {
        "stem": "Safeguarding-ul adlerian prin agresiune se apropie de mecanismul de apărare prin:",
        "options": [
            "deplasare sau atac către o țintă percepută ca mai sigură",
            "sublimare artistică freudiană",
            "confluență gestaltică",
            "triangulare familială",
        ],
        "correct": "a",
    },
    {
        "stem": "Horney descrie tendința de a merge „împotriva oamenilor”. Adler o poate lega de safeguarding prin:",
        "options": [
            "agresiune și control pentru a evita sentimentul de inferioritate",
            "integrarea Umbrei jungiene",
            "jocul simbolic kleinian",
            "reflectarea sentimentelor rogersiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul adlerian răspunde safeguarding-ului mai ales prin:",
        "options": [
            "încurajare și clarificarea scopurilor realiste",
            "interpretarea autoritară a visului ca material sexual",
            "confruntarea imediată cu splitting-ul",
            "prescrierea simptomului strategic",
        ],
        "correct": "a",
    },
    {
        "stem": "„Da, dar...” ca evitare a acțiunii se apropie funcțional de:",
        "options": [
            "safeguarding adlerian prin distanțare sau inhibiție",
            "proiecția identificatoare kleiniană",
            "individuarea jungiană",
            "deflecția gestaltică prin umor",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu Adler, nu Freud clasic?",
        "options": [
            "safeguarding ca strategie de protecție a demnității",
            "stil de viață nevrotic ca organizare defensivă",
            "aparatul Sine–Eul–Supraeu ca model central",
            "compensarea sentimentului de inferioritate",
        ],
        "correct": "abd",
    },
    # —— Horney (17–24) ——
    {
        "stem": "Externalizarea, la Karen Horney, se aseamănă cu proiecția, dar accentul din teoria Karei Horney este pe:",
        "options": [
            "atribuirea conflictului intern mediului sau altor persoane",
            "canalizarea pulsului spre activități valoroase",
            "integrarea arhetipului Umbrei",
            "reflectarea empatică a mesajului",
        ],
        "correct": "a",
    },
    {
        "stem": "Soluția perfecționistă în teoria Karei Horney funcționează ca apărare prin:",
        "options": [
            "control rigid și standarde înalte pentru a evita respingerea",
            "splitting între obiecte interne bune și rele",
            "sublimare freudiană a agresivității",
            "experiment gestaltic cu polarități",
        ],
        "correct": "a",
    },
    {
        "stem": "Soluția de autocontemplare (self-effacement) în teoria Karei Horney presupune:",
        "options": [
            "retragere, dependență și evitarea asumării propriei puteri",
            "identificare cu arhetipul Eroului",
            "safeguarding adlerian prin agresiune directă",
            "retroflexie gestaltică asupra corpului",
        ],
        "correct": "a",
    },
    {
        "stem": "„Oarbă” (blind spot) în teoria Karei Horney se apropie de negarea freudiană, dar diferența este că:",
        "options": [
            "Horney o leagă de strategii nevrotice și de refuzul de a vedea conflictul intern",
            "Horney respinge orice idee de apărare",
            "negarea freudiană apare doar la copii în jocul kleinian",
            "terapia gestaltistă o numește introiecție",
        ],
        "correct": "a",
    },
    {
        "stem": "Tendința de a merge „departe de oameni” la Horney se apropie de safeguarding adlerian prin:",
        "options": [
            "distanțare și retragere pentru a reduce anxietatea bazală",
            "proiecția identificatoare kleiniană",
            "acceptarea necondiționată rogersiană",
            "amplificarea simbolică jungiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Tirania „trebuie”-urilor la Karen Horney produce apărare prin:",
        "options": [
            "distanța rigidă dintre sinele real și sinele idealizat",
            "canalizarea impulsului spre sport",
            "interpretarea visului ca text sexual",
            "confluență cu terapeutul",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea Karei Horney, terapeutul lucrează cu apărările nevrotice mai ales prin:",
        "options": [
            "clarificarea strategiilor de evitare și sprijin în redescoperirea sinelui real",
            "interpretarea splitting-ului la sugar",
            "disputa irațională ellisiană",
            "restructurarea ierarhiei generaționale",
        ],
        "correct": "a",
    },
    {
        "stem": "Care mecanisme/strategii aparțin mai degrabă Horney decât Klein?",
        "options": [
            "externalizare și puncte oarbe",
            "soluția perfecționistă și cea de autocontemplare",
            "proiecția identificatoare primitivă",
            "splitting între obiecte parțiale",
        ],
        "correct": "ab",
    },
    # —— Klein (25–32) ——
    {
        "stem": "Splitting-ul kleinian este un mecanism primitiv care:",
        "options": [
            "separă obiectul în părți bune și rele pentru a gestiona anxietatea",
            "canalizează impulsul spre activități acceptate social",
            "evită contactul prin glume și schimbarea subiectului",
            "reflectă tendința de actualizare rogersiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Proiecția identificatoare kleiniană depășește proiecția freudiană prin:",
        "options": [
            "implicarea relațională activă: clientul induce în celălalt stări proprii",
            "respingerea oricărui material din transfer",
            "lucrul cu stilul de viață adlerian",
            "reflectarea empatică nondirectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Idealizarea urmată de devalorizare bruscă sugerează la Klein:",
        "options": [
            "splitting și trecere între obiecte interne bune/rele",
            "interes social adlerian matur",
            "individuare jungiană completă",
            "deflecție gestaltică",
        ],
        "correct": "a",
    },
    {
        "stem": "Negarea kleiniană la sugar diferă de negarea freudiană la adult prin:",
        "options": [
            "caracterul mai primitiv, legat de obiecte parțiale și supraviețuire psihică",
            "absența oricărei anxietăți",
            "identitatea cu tehnica rogersiană",
            "lipsa transferului în terapie",
        ],
        "correct": "a",
    },
    {
        "stem": "Omnipotența și controlul, ca apărări kleiniene, apar mai ales când:",
        "options": [
            "anxietatea primitivă amenință integrarea obiectului",
            "clientul a atins individuarea jungiană",
            "interesul social adlerian este stabil",
            "apare congruența rogersiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul kleinian interpretează apărările primitive în:",
        "options": [
            "transfer și fantezii din joc sau asociații",
            "stadiul genital freudian ca singur cadru",
            "experimente gestaltice de polaritate",
            "disputa convingerilor absolute",
        ],
        "correct": "a",
    },
    {
        "stem": "Introiecția obiectului la Klein se deosebește de introiecția gestaltică prin faptul că la Klein:",
        "options": [
            "vizează internalizarea relațională timpurie cu obiecte parțiale",
            "înseamnă preluarea mecanică a regulilor fără contact",
            "este o tehnică rogersiană de reflectare",
            "apare doar la adulți în terapia strategică",
        ],
        "correct": "a",
    },
    {
        "stem": "Care apărări sunt mai specifice Klein decât Horney?",
        "options": [
            "splitting și proiecție identificatoare",
            "idealizare/devalorizare primitivă",
            "externalizare a conflictului, în teoria Karei Horney",
            "soluția perfecționistă în teoria Karei Horney",
        ],
        "correct": "ab",
    },
    # —— Rogers & Gestalt vs psihodinamic (33–42) ——
    {
        "stem": "La Rogers, apărarea nu este descrisă ca mecanism freudian, ci ca:",
        "options": [
            "denaturare sau respingere a experienței care amenință imaginea de sine",
            "splitting între obiecte parțiale",
            "safeguarding prin agresiune adleriană",
            "proiecție identificatoare kleiniană",
        ],
        "correct": "a",
    },
    {
        "stem": "Condițiile de valoare la Rogers produc apărare prin faptul că clientul:",
        "options": [
            "își distorsionează experiența pentru a rămâne acceptabil",
            "canalizează pulsul spre sublimare",
            "splitting-uiește obiectele interne",
            "identifică arhetipul Eroului",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul rogersian răspunde apărării mai ales prin:",
        "options": [
            "acceptare, empatie și reflectare, nu interpretarea mecanismului",
            "interpretarea autoritară a complexului Oedip",
            "analiza jocului ca la Klein",
            "confruntarea cu splitting-ul primitiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia gestaltistă nu folosește în mod obișnuit termenul „mecanism de apărare al Eului”, ci:",
        "options": [
            "rezistențe la contact care întrerup ciclul experienței",
            "splitting kleinian",
            "safeguarding adlerian",
            "soluții nevrotice descrise de Karen Horney",
        ],
        "correct": "a",
    },
    {
        "stem": "Proiecția gestaltică și proiecția kleiniană au în comun atribuirea către altul, dar gestaltul accentuează:",
        "options": [
            "întreruperea contactului în prezent și conștientizarea trăirii",
            "fantezia primitivă a sugarului",
            "interpretarea sexuală freudiană",
            "reflectarea empatică nondirectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Retroflexia gestaltică se apropie de formarea reactivă freudiană, dar diferența esențială este:",
        "options": [
            "retroflexia întoarce energia spre sine în contact, nu înlocuiește impulsul cu opusul",
            "retroflexia este mecanism kleinian de splitting",
            "formarea reactivă este o rezistență gestaltică standard",
            "ambele sunt tehnici rogersiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Introiecția gestaltică și introiecția în sensul teoriei Karei Horney (internalizare a standardelor) se pot confunda; gestaltul accentuează:",
        "options": [
            "„înghițirea” unei reguli fără asimilare în contactul prezent",
            "obiectele parțiale ale sugarului",
            "arhetipul Părintelui",
            "triada cognitivă beckiană",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client în consilierea centrată pe persoană respinge o emoție „inacceptabilă”. "
            "Terapia gestaltistă ar interveni mai probabil prin:"
        ),
        "options": [
            "experiment pentru conștientizarea blocajului în contact",
            "interpretarea splitting-ului kleinian",
            "safeguarding adlerian prin distanțare",
            "disputa irațională ellisiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații contrastează corect cadrele teoretice?",
        "options": [
            "Freud/Klein — apărări inconștiente și conflicte intrapsihice",
            "Rogers — incongruență și distorsiunea experienței",
            "Terapia gestaltistă — rezistențe la contact în aici și acum",
            "Rogers — interpretarea splitting-ului primitiv",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un client atacă constant pe alții după ce se simte umilit. Cele mai plauzibile cadre:",
        "options": [
            "safeguarding adlerian prin agresiune",
            "externalizare în teoria Karei Horney",
            "proiecția Umbrei jungiene",
            "acceptare necondiționată ca apărare rogersiană",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un client idealizează terapeutul, apoi îl devalorizează brusc. Interpretarea prioritară kleiniană:",
        "options": [
            "splitting în transfer",
            "stil de viață adlerian",
            "deflecție gestaltică",
            "triada cognitivă negativă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client idealizează terapeutul, apoi îl devalorizează brusc. "
            "Din perspectiva terapiei gestaltiste, același tipar ar putea fi explorat ca:"
        ),
        "options": [
            "oscilație între polarități neintegrate în contact",
            "sublimare freudiană",
            "interes social matur",
            "stadiul de latență freudian",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi fenomen–autor/cadru sunt greșite?",
        "options": [
            "splitting — Horney ca mecanism central",
            "safeguarding — Adler",
            "externalizare — Horney",
            "Umbra — Jung",
        ],
        "correct": "a",
    },
    {
        "stem": "Confuzia că „orice proiecție înseamnă același lucru” este respinsă deoarece:",
        "options": [
            "proiecția jungiană, kleiniană, gestaltică și freudiană diferă prin cadru și intervenție",
            "doar Freud folosește proiecția",
            "consilierea centrată pe persoană și terapia gestaltistă resping proiecția ca fenomen",
            "Adler o numește splitting",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul care interpretează apărarea ca întrerupere a contactului în prezent este:",
        "options": [
            "Terapia gestaltistă (Fritz Perls)",
            "Melanie Klein (relații obiectuale)",
            "Sigmund Freud (psihanaliză clasică)",
            "Karen Horney — anxietate interpersonală și sinel real",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul care interpretează apărarea ca strategie față de anxietatea bazală în relații este:",
        "options": [
            "Karen Horney — anxietate interpersonală și sinel real",
            "Carl Gustav Jung (psihologie analitică)",
            "behaviorist",
            "Alfred Adler — safeguarding prin agresiune",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul care lucrează cu fantezii primitive și splitting în transfer este:",
        "options": [
            "Melanie Klein (relații obiectuale)",
            "Carl R. Rogers",
            "Terapia gestaltistă (Fritz Perls)",
            "Albert Ellis (REBT)",
        ],
        "correct": "a",
    },
    {
        "stem": "Comparând toate cadrele, afirmația corectă este:",
        "options": [
            "psihodinamicii descriu apărări inconștiente; consilierea centrată pe persoană și terapia gestaltistă le reformulează în termeni de incongruență sau rezistență la contact",
            "toate cadrele folosesc identic conceptul de splitting",
            "terapia gestaltistă și consilierea centrată pe persoană interpretează apărările prin jocul kleinian",
            "Adler și Horney resping orice idee de evitare a anxietății",
        ],
        "correct": "a",
    },
    {
        "stem": "Un student spune: „Compensarea e același lucru la Freud și Adler.” Răspunsul cel mai precis:",
        "options": [
            "termenul se aseamănă, dar Adler îl leagă de inferioritate și stil de viață, nu de pulsiune freudiană",
            "Adler respinge complet ideea de compensare",
            "Freud folosește compensarea doar în terapia gestaltistă",
            "Horney a creat conceptul de compensare adleriană",
        ],
        "correct": "a",
    },
]
