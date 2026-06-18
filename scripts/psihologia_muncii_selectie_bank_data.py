"""Itemi — Selecția personalului, lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SELECTIE_PERSONAL_ITEMS: List[Item] = [
    # —— Definiție, predictor–criteriu (1–8) ——
    {
        "stem": (
            "Selecția personalului este, în esență, un proces de predicție: "
            "instrumentele folosite estimează performanța viitoare la job, nu o "
            "măsoară direct în momentul selecției."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care distincție descrie corect relația dintre predictor și criteriu "
            "în selecția personalului?"
        ),
        "options": [
            "predictorul = instrumentul de selecție (test, interviu, probă de lucru); "
            "criteriul = performanța reală după angajare",
            "predictorul = performanța curentă la job; criteriul = scorul la test",
            "predictorul și criteriul sunt mereu același construct măsurat în "
            "momente diferite",
            "criteriul = CV-ul candidatului; predictorul = decizia de angajare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un consultant folosește un test de aptitudine și un interviu "
            "structurat pentru a estima cine va reuși în rol. În limbajul "
            "selecției, testul și interviul sunt:"
        ),
        "options": [
            "predictori (instrumente de măsurare a variabilei de predicție)",
            "criterii de performanță ulterioară",
            "indicatori ai ratei de bază (base rate) din populația generală",
            "substituenți ai raportului de selecție (SR)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Performanța evaluată la 6 luni după angajare, folosită pentru a verifica "
            "dacă testul de selecție a funcționat, reprezintă:"
        ),
        "options": [
            "criteriul (criterion) — rezultatul real pe care îl prognozează predictorul",
            "predictorul — instrumentul aplicat în faza de recrutare",
            "validitatea de fațadă a interviului nestructurat",
            "raportul de selecție (SR) al companiei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații descriu corect logica selecției ca proces de predicție?"
        ),
        "options": [
            "scorurile la selecție permit inferențe despre performanța viitoare, "
            "cu o marjă de eroare",
            "validitatea predictorului se evaluează prin corelația cu criteriul",
            "un scor bun la selecție garantează performanță perfectă la job",
            "fără criteriu post-angajare nu poți calibra utilitatea predictorului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Dacă un manager crede că un interviu de 10 minute „măsoară direct” cum "
            "va lucra cineva timp de ani, greșește pentru că selecția:"
        ),
        "options": [
            "estimează probabilitatea de succes, nu observă performanța viitoare în "
            "integralitate",
            "nu poate folosi niciun instrument standardizat",
            "exclude neapărat orice formă de validitate statistică",
            "înlocuiește analiza postului cu impresii subiective",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre relația predictor–criteriu este falsă?"
        ),
        "options": [
            "predictorul și criteriul trebuie să fie mereu același test aplicat "
            "în momente diferite",
            "predictorul este instrumentul de selecție; criteriul este performanța "
            "după angajare",
            "validitatea se studiază prin legătura dintre predictor și criteriu",
            "probele de lucru pot servi drept predictori ai performanței ulterioare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi predictor → criteriu sunt formulate corect?"
        ),
        "options": [
            "scor la test de integritate → comportamente contraproductive la locul "
            "de muncă (CWB)",
            "scor la aptitudinea mentală generală (GMA) → performanță în training și la job",
            "număr de pagini din CV → coeficientul de inteligență măsurat clinic",
            "probă de lucru (work sample) → calitatea lucrului prestat în rol",
        ],
        "correct": "abd",
    },
    # —— Predictori principali (9–20) ——
    {
        "stem": (
            "În meta-analizele din psihologia personalului, care predictor individual "
            "are, în mod constant, una dintre cele mai puternice legături cu "
            "performanța la job?"
        ),
        "options": [
            "aptitudinea mentală generală (GMA)",
            "vârsta cronologică a candidatului",
            "preferința pentru o anumită culoare în CV",
            "numărul de hobby-uri listate în autobiografie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Conștiinciozitatea (conscientiousness) ca predictor al performanței la "
            "muncă este asociată, în mod tipic, cu:"
        ),
        "options": [
            "niveluri mai ridicate de performanță",
            "fluctuație mai redusă a performanței în timp",
            "scăderea automată a validității testelor de aptitudine",
            "creșterea comportamentelor contraproductive la locul de muncă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Testele de integritate (integrity tests) în selecție sunt folosite "
            "mai ales pentru a prezice:"
        ),
        "options": [
            "reducerea comportamentelor contraproductive la locul de muncă (CWB)",
            "respectarea regulilor și politicilor organizaționale",
            "nivel maxim de aptitudine mentală generală (GMA)",
            "fluctuația lunară a salariului de bază",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Probele de lucru (work sample tests) — în care candidatul execută "
            "sarcini reprezentative pentru rol — se caracterizează prin:"
        ),
        "options": [
            "validitate predictivă foarte ridicată față de multe alte metode",
            "ancorare directă în conținutul sarcinilor din job",
            "cost redus și aplicare pe hârtie, fără observarea comportamentului la sarcină",
            "lipsa oricărei legături cu criteriul de performanță",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care predictori sunt recunoscuți în literatura de selecție pentru "
            "utilitate empirică ridicată sau consistentă?"
        ),
        "options": [
            "aptitudinea mentală generală (GMA)",
            "conștiinciozitatea",
            "teste de integritate",
            "probe de lucru (work samples)",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un angajator prioritizează reducerea furturilor și a încălcărilor de "
            "regulament. Care predictor este cel mai relevant în acest scop?"
        ),
        "options": [
            "teste de integritate",
            "aptitudine mentală generală (GMA) ridicată, indiferent de onestitate",
            "numărul de recomandări scrise",
            "preferința pentru lucru în echipă, fără măsură a conformității",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Aptitudinea mentală generală (GMA) este un predictor slab al performanței "
            "la job comparativ cu majoritatea testelor de personalitate."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce conștiinciozitatea poate reduce fluctuația performanței, nu "
            "doar nivelul mediu?"
        ),
        "options": [
            "persoanele conștiincioase își organizează mai constant efortul și "
            "respectă standardele",
            "trăsătura vizează perseverența și fiabilitatea în îndeplinirea sarcinilor",
            "conștiinciozitatea măsoară direct coeficientul de inteligență",
            "trăsătura elimină nevoia de feedback de la supervizor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care scenariu ilustrează cel mai bine o probă de lucru (work sample)?"
        ),
        "options": [
            "un candidat la secretariat redactează un document tipic în timp limitat",
            "un programator rezolvă o problemă reprezentativă pentru proiect",
            "candidatul completează un chestionar despre valori personale, fără "
            "sarcină de rol",
            "recrutorul evaluează doar diplomele, fără observarea comportamentului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un specialist în resurse umane (HR) compară aptitudinea mentală generală "
            "(GMA), conștiinciozitatea și integritatea. Care "
            "afirmații sunt corecte?"
        ),
        "options": [
            "aptitudinea mentală generală (GMA) prezice în special capacitatea de "
            "învățare și rezolvare de probleme",
            "conștiinciozitatea vizează organizare, perseverență și fiabilitate",
            "integritatea se leagă mai ales de comportamente contraproductive și "
            "respectarea regulilor",
            "toți trei măsoară același construct psihologic sub denumiri diferite",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre validitatea moderată în selecție este corectă?"
        ),
        "options": [
            "un predictor cu r ≈ 0,30 poate fi util, mai ales combinat cu alții",
            "validitatea moderată devine inutilă indiferent de context",
            "r ≈ 0,30 înseamnă același lucru cu validitate foarte puternică",
            "combinarea predictorilor scade întotdeauna validitatea totală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care predictor este cel mai potrivit când postul cere învățare rapidă "
            "a procedurilor complexe și rezolvare de probleme noi?"
        ),
        "options": [
            "aptitudinea mentală generală (GMA)",
            "test de integritate pentru retail",
            "măsurarea înălțimii candidatului",
            "preferința pentru lucru fizic în exterior",
        ],
        "correct": "a",
    },
    # —— Validitate, r, R, R², incrementală (21–32) ——
    {
        "stem": (
            "În selecția personalului, un coeficient de corelație r = 0,30 între "
            "predictor și criteriu este interpretat, de regulă, ca validitate:"
        ),
        "options": [
            "moderată",
            "foarte slabă, fără utilitate practică",
            "foarte puternică, peste pragul de 0,70",
            "negativă, indicând relație inversă obligatorie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care praguri pentru coeficientul r (validitate predictivă) sunt "
            "folosite frecvent în psihologia personalului?"
        ),
        "options": [
            "r ≈ 0,10 — validitate slabă",
            "r ≈ 0,30 — validitate moderată",
            "r ≈ 0,50 — validitate bună",
            "r ≈ 0,70 sau mai mare — validitate foarte puternică",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Validitatea incrementală a unui predictor nou înseamnă că:"
        ),
        "options": [
            "aduce informație suplimentară față de predictori deja folosiți "
            "(ex. aptitudinea mentală generală — GMA)",
            "crește puterea predictivă a combinației de instrumente peste ce "
            "oferă fiecare singur",
            "înlocuiește complet nevoia de orice alt test",
            "este zero dacă noul predictor corelează parțial cu aptitudinea mentală "
            "generală (GMA)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În selecție, validitatea multiplă a predictorilor combinați (R) desemnează "
            "adesea:"
        ),
        "options": [
            "validitatea predictivă a combinației de predictori (ex. test + interviu)",
            "coeficientul de corelație al unui singur test cu criteriul",
            "procentul de candidați angajați din totalul aplicanților",
            "probabilitatea de succes fără nicio procedură de selecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Proporția varianței explicate (R²) în contextul validității multiple "
            "a predictorilor indică:"
        ),
        "options": [
            "proporția variației din criteriu explicată de setul de predictori",
            "coeficientul de corelație simplă între un singur test și criteriu",
            "raportul dintre candidații selectați și totalul aplicanților",
            "sensibilitatea procedurii de screening",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Proporția varianței explicate (R²) este același lucru cu coeficientul "
            "de corelație (r) — ambele măsoară corelația liniară între "
            "un singur predictor și criteriu."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "O companie folosește aptitudinea mentală generală (GMA) și un interviu "
            "structurat. Validitatea multiplă (R) = 0,55, deci proporția varianței "
            "explicate (R²) ≈ 0,30. Ce înseamnă pentru performanță?"
        ),
        "options": [
            "aproximativ 30% din variația performanței este asociată cu scorurile "
            "combinate la selecție",
            "55% din angajați vor avea performanță perfectă",
            "interviul este de 55 de ori mai valid decât aptitudinea mentală generală "
            "(GMA)",
            "restul de 70% din variație este mereu măsurată direct la job",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre validitatea în selecție sunt corecte?"
        ),
        "options": [
            "r = 0,50 indică o legătură predictivă bună între predictor și criteriu",
            "validitatea incrementală e relevantă când adaugi un nou instrument",
            "r = 0,10 poate fi totuși informativ în anumite contexte, dar e slab",
            "validitatea perfectă (r = 1) apare frecvent la interviul nestructurat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce combinarea mai multor predictori valizi poate crește validitatea "
            "multiplă (R) față de "
            "un singur instrument?"
        ),
        "options": [
            "fiecare predictor poate captura aspecte diferite ale performanței "
            "viitoare",
            "erorile de măsurare parțial independente se compensează în modelul "
            "combinat",
            "combinarea elimină automat orice eroare de selecție",
            "Proporția varianței explicate (R²) scade mereu când adaugi predictori, "
            "deci e inutil să combini",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un test nou corelează r = 0,25 cu performanța după ce aptitudinea "
            "mentală generală (GMA) este deja folosită și crește proporția varianței "
            "explicate (R²) al modelului. Acest rezultat sugerează:"
        ),
        "options": [
            "validitate incrementală a noului predictor",
            "că testul nu aduce nicio informație suplimentară",
            "că aptitudinea mentală generală (GMA) trebuie eliminată din bateria de "
            "selecție",
            "validitate de fațadă negativă a criteriului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În interpretarea validității, diferența dintre coeficientul de corelație "
            "(r) și proporția varianței explicate (R²) este că:"
        ),
        "options": [
            "r descrie legătura unui predictor (sau combinație) cu criteriul; "
            "proporția varianței explicate (R²) = r² și arată proporția varianței "
            "explicate",
            "proporția varianței explicate (R²) este mereu mai mare decât 1 pentru "
            "combinații complexe",
            "coeficientul de corelație (r) se aplică doar testelor de personalitate; "
            "proporția varianței explicate (R²) doar la aptitudinea mentală generală "
            "(GMA)",
            "ambele măsoară raportul de selecție (SR), nu validitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un coeficient r = 0,72 între predictor și criteriu de performanță "
            "indică validitate:"
        ),
        "options": [
            "foarte puternică",
            "moderată",
            "slabă",
            "nulă",
        ],
        "correct": "a",
    },
    # —— Sensibilitate, specificitate, erori (33–42) ——
    {
        "stem": (
            "Sensibilitatea unei proceduri de selecție se referă la capacitatea de "
            "a detecta candidații care ar performa bine — adică reduce riscul de:"
        ),
        "options": [
            "false negative (respingere greșită a unui candidat bun)",
            "false positive (angajare greșită a unui candidat slab)",
            "creșterea ratei de bază (base rate) în populație",
            "scăderea coeficientului de corelație (r) ca validitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Specificitatea unei proceduri de selecție vizează în principal:"
        ),
        "options": [
            "identificarea și eliminarea candidaților nepotriviți",
            "reducerea false positive (angajarea celor care nu vor performa)",
            "maximizarea false negative pentru a angaja mai mulți candidați",
            "creșterea raportului de selecție (SR) peste 0,90",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Sensibilitatea ridicată a unui test de selecție reduce în principal "
            "rata falselor pozitive."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care perechi corectează conceptul cu efectul asupra erorilor de "
            "selecție?"
        ),
        "options": [
            "procedura prinde mai bine candidații buni → mai puține respingeri greșite",
            "procedura respinge mai bine candidații slabi → mai puține angajări greșite",
            "procedura prinde mai bine candidații buni → mai puține angajări greșite",
            "procedura respinge candidații slabi → garantat mai multe respingeri greșite",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un candidat competent este respins deoarece testul nu l-a identificat "
            "corect. Aceasta este o eroare de tip:"
        ),
        "options": [
            "false negative",
            "false positive",
            "validitate incrementală",
            "raport de selecție (SR) scăzut",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "O firmă angajează pe cineva care obține scor mare la selecție, dar "
            "performează slab la job. Aceasta ilustrează:"
        ),
        "options": [
            "false positive",
            "false negative",
            "rată de bază (base rate) ridicată",
            "validitate foarte puternică a predictorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre false positive și false negative în selecție "
            "sunt corecte?"
        ),
        "options": [
            "false positive = candidat angajat care nu atinge performanța așteptată",
            "false negative = candidat respins care ar fi reușit la job",
            "false positive = candidat respins pe nedrept",
            "ambele erori dispar automat când r > 0,30",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un test foarte strict care respinge mulți candidați buni, dar rar "
            "angajează pe cineva nepotrivit, tinde să aibă:"
        ),
        "options": [
            "specificitate ridicată, sensibilitate posibil mai scăzută",
            "sensibilitate maximă și specificitate zero",
            "raport de selecție (SR) mare și rată de bază (base rate) scăzută",
            "validitate negativă și proporție a varianței explicate (R²) peste 1",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă crești sensibilitatea unui test de screening fără a ajusta "
            "specificitatea, ce risc poate crește?"
        ),
        "options": [
            "riscul de false positive (angajarea candidaților nepotriviți)",
            "riscul de false negative (respingerea candidaților buni)",
            "raportul de selecție (SR) devine automat zero",
            "coeficientul de corelație (r) devine negativ ca validitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În logică de testare, asocierea corectă este:"
        ),
        "options": [
            "detectează pe cei buni; reduce respingerile greșite",
            "elimină pe cei nepotriviți; reduce angajările greșite",
            "elimină pe cei nepotriviți; reduce respingerile greșite",
            "detectează pe cei buni; reduce angajările greșite",
        ],
        "correct": "ab",
    },
    # —— Screening vs comprehensive (43–50) ——
    {
        "stem": (
            "Care caracteristici descriu mai bine selecția de tip screening?"
        ),
        "options": [
            "elimină rapid candidații nepotriviți",
            "proceduri relativ ieftine și scurte",
            "CV-uri, filtre inițiale, teste scurte",
            "centre de evaluare (assessment center) cu simulări complexe ca prim pas "
            "obligatoriu",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care caracteristici descriu mai bine selecția comprehensive "
            "(de înaltă fidelitate)?"
        ),
        "options": [
            "identifică cel mai potrivit candidat dintre finaliști",
            "proceduri mai complexe, mai costisitoare, mai lungi",
            "centru de evaluare (assessment center), simulări de lucru, probe extinse",
            "doar trierea pe baza unui singur filtru demografic",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre screening și selecția comprehensive este falsă?"
        ),
        "options": [
            "screening-ul și comprehensive au același scop, complexitate și cost",
            "screening-ul elimină rapid candidații nepotriviți la cost redus",
            "comprehensive diferențiază finaliștii prin proceduri mai elaborate",
            "centrul de evaluare (assessment center) este tipic pentru etapa comprehensive",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un angajator aplică mai întâi un filtru pe CV, apoi un test scurt, "
            "iar finaliștii trec prin centru de evaluare (assessment center). Aceasta "
            "ilustrează:"
        ),
        "options": [
            "lanț screening (rapid, eliminatoriu) urmat de selecție comprehensive",
            "doar screening, fără etapă de înaltă fidelitate",
            "doar comprehensive, deoarece CV-ul este complex",
            "inversarea predictorului cu criteriul",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care distincție între screening și comprehensive este corectă?"
        ),
        "options": [
            "screening — reduce pool-ul de candidați; comprehensive — diferențiază "
            "finaliștii",
            "screening — cost și timp reduse; comprehensive — cost și timp mai mari",
            "comprehensive — mereu mai puțin valid decât un CV",
            "screening — folosește doar centru de evaluare (assessment center)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce are sens să combini screening cu etape comprehensive?"
        ),
        "options": [
            "screeningul gestionează volumul mare de aplicații la cost redus",
            "etapa comprehensive oferă validitate mai mare pentru decizia finală",
            "comprehensive înlocuiește nevoia de orice criteriu de performanță",
            "screeningul garantează r > 0,70 pentru orice post",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care instrument este mai tipic pentru faza de screening decât pentru "
            "decizia finală comprehensive?"
        ),
        "options": [
            "filtrarea inițială a CV-urilor",
            "test scurt online cu barem automat",
            "centru de evaluare (assessment center) cu mai multe exerciții simulate",
            "simulare de o zi întreagă a rolului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Centrul de evaluare (assessment center) cu exerciții simulate este "
            "clasificat, de regulă, "
            "ca metodă:"
        ),
        "options": [
            "comprehensive (de înaltă fidelitate), nu simplu screening",
            "screening rapid pe CV, fără observare comportamentală",
            "de măsurare a ratei de bază (base rate) din populație",
            "echivalent cu un singur filtru demografic",
        ],
        "correct": "a",
    },
    # —— Utilitate, base rate, selection ratio, Taylor–Russell (51–60) ——
    {
        "stem": (
            "Rata de bază (base rate) în selecția personalului se referă la:"
        ),
        "options": [
            "probabilitatea de succes (performanță satisfăcătoare) fără o procedură "
            "de selecție sistematică",
            "raportul dintre candidații angajați și totalul aplicanților (SR)",
            "coeficientul de corelație între aptitudinea mentală generală (GMA) și "
            "integritate",
            "procentul de varianță explicat de proporția varianței explicate (R²)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Raportul de selecție (SR) = candidați selectați / total candidați. Un SR "
            "mic (ex. 5%) indică:"
        ),
        "options": [
            "selecție strictă — se alege o mică fracțiune din aplicanți",
            "selecție permisivă — se angajează aproape toți cei care aplică",
            "validitate negativă a predictorului",
            "rată de bază (base rate) egală cu 1",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Conform logicii Taylor–Russell, utilitatea economică a selecției crește "
            "când:"
        ),
        "options": [
            "validitatea predictorilor este mai mare",
            "raportul de selecție (SR) este mai mic (selecție mai strictă)",
            "rata de bază (base rate) nu intră în calculul utilității",
            "validitatea scade, dar raportul de selecție (SR) crește",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul Taylor–Russell, utilitatea selecției este maximă când "
            "validitatea este scăzută și raportul de selecție (SR) este foarte mare."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "O companie primește 500 de aplicații și angajează 10 persoane. "
            "Raportul de selecție (SR) este:"
        ),
        "options": [
            "10/500 = 0,02 (2%)",
            "500/10 = 50",
            "10/490",
            "1 − 10/500",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre utilitatea selecției sunt corecte?"
        ),
        "options": [
            "rata de bază (base rate) descrie situația fără selecție sistematică",
            "raport de selecție (SR) mic înseamnă că alegi puțini din mulți candidați",
            "validitate mai mare permite separarea mai bună a viilor performeri",
            "utilitatea nu depinde de validitate, doar de numărul de aplicații",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Două firme au același raport de selecție (SR). Firma A folosește "
            "predictori cu r = 0,50, "
            "firma B cu r = 0,15. Conform principiilor utilității selecției:"
        ),
        "options": [
            "firma A are potențial de câștig mai mare din selecție",
            "firma B obține aceeași precizie indiferent de validitate",
            "validitatea influențează cât de bine selecția îmbunătățește calitatea "
            "angajărilor",
            "raportul de selecție (SR) singur determină totul, validitatea e irelevantă",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "De ce un raport de selecție (SR) foarte mare (aproape toți sunt "
            "angajați) limitează "
            "utilitatea selecției, chiar dacă validitatea e moderată?"
        ),
        "options": [
            "aproape nu se face o selecție reală — rămân și candidații slabi",
            "diferențierea dintre aplicanți nu mai contează practic",
            "rata de bază (base rate) devine automat zero",
            "proporția varianței explicate (R²) trebuie să fie egală cu raportul de "
            "selecție (SR)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații rezumă corect logica selecției personalului?"
        ),
        "options": [
            "predictorii — aptitudinea mentală generală (GMA), conștiinciozitate, "
            "integritate, probe de lucru — se evaluează prin validitate (coeficientul "
            "de corelație r, validitatea multiplă R, proporția varianței explicate R²)",
            "screening-ul reduce pool-ul; comprehensive alege între finaliști",
            "utilitatea crește cu validitatea mai mare și cu raport de selecție (SR) "
            "mai mic",
            "selecția măsoară direct performanța viitoare, fără eroare de predicție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un specialist în resurse umane (HR) vrea să maximizeze utilitatea: ridică "
            "validitatea bateriei de teste (validitatea multiplă R crește de la 0,35 "
            "la 0,50) și reduce raportul de selecție (SR) de la 20% la 8%. "
            "Conform Taylor–Russell și a logicii selecției, această combinație:"
        ),
        "options": [
            "tinde să crească utilitatea economică a procesului de selecție",
            "reduce utilitatea, deoarece raportul de selecție (SR) mai mic înseamnă "
            "mai puțini angajați de calitate",
            "anulează efectul validității prin rata de bază (base rate)",
            "face inutil screening-ul inițial pe CV",
        ],
        "correct": "a",
    },
    # —— Screening vs comprehensive — aprofundare (61–70) ——
    {
        "stem": (
            "Scopul principal al screening-ului în selecție este să identifice "
            "cel mai bun candidat dintre cei 5–10 finaliști, folosind simulări "
            "complexe de o zi întreagă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "O firmă primește 900 de aplicații. Resursele umane (HR) elimină mai "
            "întâi CV-urile fără studiile minime cerute, apoi aplică un test scurt "
            "online. Această etapă inițială este, în mod tipic:"
        ),
        "options": [
            "screening — rapidă, ieftină, orientată spre eliminarea nepotriviților "
            "dintr-un pool mare",
            "selecție comprehensive — alege cel mai bun dintre finaliști",
            "măsurarea ratei de bază (base rate) a performanței în populație",
            "validitate incrementală a aptitudinii mentale generale (GMA)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații descriu corect selecția comprehensive (de înaltă "
            "fidelitate)?"
        ),
        "options": [
            "are loc de regulă după screening, pe un număr redus de finaliști",
            "folosește proceduri mai complexe și mai costisitoare decât un filtru "
            "pe CV",
            "elimină mii de candidați în câteva minute, fără observare detaliată",
            "poate include centru de evaluare (assessment center) sau simulări "
            "extinse ale rolului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "După un filtru pe CV rămân 35 de candidați. Fiecare susține o simulare "
            "de 3 ore a sarcinilor din job, urmată de interviu structurat cu "
            "comisie. Această etapă este cel mai bine încadrată ca:"
        ),
        "options": [
            "selecție comprehensive — diferențiază finaliștii cu proceduri bogate",
            "screening simplu — doar triere rapidă pe date biografice",
            "măsurare directă a performanței la job, fără eroare de predicție",
            "înlocuirea criteriului de performanță cu scorul la CV",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care motive explică de ce organizațiile nu trimit direct toți cei "
            "500 de aplicanți la un centru de evaluare (assessment center)?"
        ),
        "options": [
            "costul și timpul ar fi prohibitivi pentru întregul pool",
            "screening-ul reduce mai întâi numărul de candidați evaluați în "
            "profunzime",
            "centrul de evaluare (assessment center) are validitate zero față de "
            "orice alt instrument",
            "screening-ul gestionează volumul mare; comprehensive rămâne pentru "
            "decizia fină între puțini finaliști",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care formulare surprinde cel mai bine diferența de scop între cele "
            "două tipuri de selecție?"
        ),
        "options": [
            "screening: „cine nu trebuie să continue?” — comprehensive: „cine este "
            "cel mai potrivit dintre cei rămași?”",
            "screening: alege cel mai bun — comprehensive: elimină pe toți "
            "nepotriviții dintr-o singură etapă",
            "ambele au același cost, timp și grad de complexitate",
            "screening folosește doar simulări lungi; comprehensive doar CV-uri",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care instrumente sunt asociate mai frecvent cu screening, respectiv "
            "cu selecție comprehensive?"
        ),
        "options": [
            "filtru automat pe cuvinte cheie în CV",
            "test scurt online cu barem",
            "simulare de o zi întreagă a rolului",
            "interviu de selecție structurat pe 2–3 ore cu exerciții simulate",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un proces are două etape: (1) interviu telefonic de 15 minute pentru "
            "toți candidații; (2) probă de lucru de 2 ore doar pentru cei 12 "
            "rămași. Care încadrări sunt corecte?"
        ),
        "options": [
            "interviu telefonic de 15 minute pentru toți candidații",
            "probă de lucru de 2 ore doar pentru cei 12 rămași",
            "interviu telefonic ca evaluare profundă a competențelor",
            "probă de lucru ca filtru rapid pe pool mare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Procedurile comprehensive sunt, în mod tipic, mai ieftine și mai "
            "rapide decât screening-ul pe CV, pentru că se aplică la mai mulți "
            "candidați simultan."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "O bancă angajează 8 casieri din 400 de aplicații. Lanțul: filtru "
            "studii + test scurt → 40 finaliști → assessment center cu role-play "
            "→ 8 angajați. Care perechi etapă–tip selecție sunt corecte?"
        ),
        "options": [
            "filtru studii + test scurt pe pool mare",
            "assessment center cu role-play pe finaliști",
            "test scurt pe 400 de persoane ca evaluare profundă",
            "role-play pe finaliști ca filtru rapid și ieftin",
        ],
        "correct": "ab",
    },
    # —— Sensibilitate / specificitate — aprofundare (71–75) ——
    {
        "stem": (
            "Sensibilitatea unei proceduri de selecție descrie capacitatea de a "
            "prinde candidații care ar reuși la job. Prin urmare, sensibilitate "
            "ridicată tinde să reducă:"
        ),
        "options": [
            "falsul negativ (respingerea unui candidat bun)",
            "falsul pozitiv (angajarea unui candidat slab)",
            "raportul de selecție (SR)",
            "validitatea incrementală a testelor de integritate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre specificitate în selecția personalului sunt "
            "corecte?"
        ),
        "options": [
            "vizează eliminarea candidaților nepotriviți din pool",
            "ridicată → mai puține angajări greșite (fals pozitiv)",
            "ridicată → garantează automat sensibilitate maximă",
            "se leagă de respingerea celor care probabil nu ar performa",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un candidat competent este respins pentru că testul de selecție era "
            "prea strict și nu l-a „prins”. Eroarea comisă este:"
        ),
        "options": [
            "fals negativ (false negative)",
            "fals pozitiv (false positive)",
            "rată de bază (base rate) ridicată",
            "validitate multiplă (R) negativă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă mărești specificitatea unui test de screening fără să ajustezi "
            "sensibilitatea, efectul tipic asupra erorilor este:"
        ),
        "options": [
            "mai puține fals pozitive, dar risc mai mare de fals negative",
            "mai puține fals negative, dar risc mai mare de fals pozitive",
            "dispar ambele tipuri de erori automat",
            "crește raportul de selecție (SR) la valoarea 1",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Sensibilitatea ridicată a unui instrument de selecție reduce în "
            "principal rata falselor negative."
        ),
        "tf": True,
        "correct_tf": True,
    },
]
