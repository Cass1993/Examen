"""Explicații — Caracteristici psihometrice II, seg. 4: selecție profesională (ID 11406–11445)."""

from __future__ import annotations

from typing import List

SELECIE_PROFESIONALA_EXPLANATIONS: List[str] = [
    # 11406
    (
        "Adevărat. Validitatea observată nu poate depăși, de regulă, fidelitatea "
        "predictorului: rxy ≤ rtt. În selecție, un test instabil limitează utilitatea "
        "predictivă reală."
    ),
    # 11407
    (
        "Fals. SEM = SDt·√(1−rtt) — legată de fidelitate. SEE = SDy·√(1−rxy²) — "
        "legată de validitate. Nu le confunda la decizii de selecție."
    ),
    # 11408
    (
        "Adevărat. Validitate concurentă: predictor și criteriu măsurați aproximativ "
        "simultan (ex. test nou vs test consacrat)."
    ),
    # 11409
    (
        "Fals. SEM = SDt·√(1−rtt). Când rtt crește, (1−rtt) scade → SEM scade. "
        "Fidelitate mai bună = bandă mai îngustă a scorului real."
    ),
    # 11410
    (
        "Fidelitate = consistență/stabilitate a măsurării. Validitate = măsoară ce "
        "trebuie. Criteriu și conținut sunt alte tipuri de validitate."
    ),
    # 11411
    (
        "Validitate = testul măsoară constructul intenționat și interpretările sunt "
        "susținute empiric. Stabilitatea la retest e fidelitate, nu validitate."
    ),
    # 11412
    (
        "X = scor observat (brut). SR = scor real. E = eroare. Modelul X = SR + E "
        "explică de ce scorul punctual poate devia de la nivelul adevărat."
    ),
    # 11413
    (
        "Test-retest: aceeași formă, timp diferit → eșantionare temporală a erorii "
        "(stare, practică, maturare)."
    ),
    # 11414
    (
        "Half-split: corelația între jumătăți → eșantionare de conținut în cadrul "
        "aceluiași test. Nu e temporală și nu e inter-rater."
    ),
    # 11415
    (
        "Alpha Cronbach estimează consistența internă dintr-o administrare. "
        "Inter-rater și test-retest sunt alte metode de fidelitate."
    ),
    # 11416
    (
        "KR-20 = formula pentru itemi dicotomici (0/1). Likert folosește de regulă "
        "Alpha, nu KR-20."
    ),
    # 11417
    (
        "Predictor = scorul la testul evaluat (instrumentul). Criteriu = performanță "
        "externă (job, note, diagnostic)."
    ),
    # 11418
    (
        "Contaminare: evaluatorul criteriului știe scorul la test → bias, rxy umflat "
        "artificial. Critical în selecție când interviul e influențat de test."
    ),
    # 11419
    (
        "Validitate de construct: trăsătură teoretică (inteligență, personalitate) "
        "susținută de rețea nomologică, MTMM, analiză factorială."
    ),
    # 11420
    (
        "MTMM = Campbell & Fiske (1959) — convergență și discriminare între trăsături "
        "și metode. Lawshe = CVR; Thorndike = reguli itemi."
    ),
    # 11421
    (
        "CVR = (Ne−N/2)/(N/2). Negativ când Ne < N/2 — mai puțin de jumătate "
        "consideră itemul esențial."
    ),
    # 11422
    (
        "Binet: măsurarea inteligenței nu e directă ca pe un cântar — necesită "
        "sarcini, standardizare și interpretare a constructului latent."
    ),
    # 11423
    (
        "Corecție ghicire: X − W/(n−1). W = greșeli, n = alternative. Penalizează "
        "răspunsul aleator la itemi obiectivi cu alegere multiplă."
    ),
    # 11424
    (
        "Decizii individuale cu miză mare (ex. selecție critică): rtt orientativ "
        "0,90–0,95 + interpretare cu SEM/interval, nu doar scor brut."
    ),
    # 11425
    (
        "Interval ~95% pentru scor real: X ± 2·SEM (aprox.). Necesită SDt și rtt "
        "pentru calculul SEM. SEE e pentru predicția criteriului, nu scor test."
    ),
    # 11426
    (
        "Validitate conținut: experți evaluează relevanța/esențialitatea + "
        "constructorul definește domeniul și specificațiile. Nu e corelația rxy."
    ),
    # 11427
    (
        "Predictivă: criteriu în viitor (succes job după test admitere). Concurentă "
        "e simultană; predictiva e pentru anticipare."
    ),
    # 11428
    (
        "Smith orientativ: rxy ≈ 0,50 = excelent; mult peste 0,30 (acceptabil) "
        "și 0,40 (bun). Utilitatea depinde și de scopul deciziei."
    ),
    # 11429
    (
        "Scenariul (a): măsoară corect + foarte bine = valid + fidel = test sound "
        "(solid, credibil). Nu e invalid constant."
    ),
    # 11430
    (
        "Scenariul (c): nu măsoară ce trebuie → validitate problematică, risc "
        "decizional. Poate părea fidel la constructul greșit."
    ),
    # 11431
    (
        "Forme alternative imediate: două forme paralele, aproape simultan → "
        "eșantionare de conținut. Nu e test-retest anual."
    ),
    # 11432
    (
        "SEM = SDt·√(1−rtt): legată de fidelitate; rtt ↑ → SEM ↓; depinde de SDt. "
        "Nu e identică cu SEE (validitate)."
    ),
    # 11433
    (
        "Constructor: definește domeniul + mapare item–specificații + revizuire "
        "experți. rxy > 0,70 nu e cerință pre-pilotare pentru conținut."
    ),
    # 11434
    (
        "Inter-rater: acordul/diferențele între scoreri pe aceeași probă. "
        "Sursa erorii = examinator, nu timp sau conținut."
    ),
    # 11435
    (
        "SEE = SDy·√(1−rxy²): eroare la predicția criteriului din scor test. "
        "Centrală în selecție: cât de precis estimezi succesul job din test."
    ),
    # 11436
    (
        "rxy mare → SEE mică → predicții criteriu mai precise. rxy mic → "
        "predicții împrăștiate — risc mai mare la decizii individuale."
    ),
    # 11437
    (
        "Taylor-Russell: evaluează utilitatea testului în selecție — cum validitatea, "
        "rata de bază (% succes în populație) și proporția selectată influențează "
        "% selecții corecte."
    ),
    # 11438
    (
        "Patru formule cheie: Spearman-Brown half-split; lungime test; rtt mare "
        "permite mai puțini itemi pentru aceeași fidelitate țintă; itemi paraleli "
        "de calitate comparabilă."
    ),
    # 11439
    (
        "KR-20: itemi dicotomici, varianță totală și Σpq. Alpha: varianțe itemi "
        "generale. Ambele → consistență internă, nu validitate criterială directă."
    ),
    # 11440
    (
        "SEE mic → predicții criteriu strânse, decizii mai sigure, bandă mai "
        "îngustă. rxy pozitiv mic nu e automat suficient la miză mare."
    ),
    # 11441
    (
        "Taylor-Russell depinde de: validitate (rxy), rata de bază, proporția "
        "selectată. Nu de numărul itemilor din half-split."
    ),
    # 11442
    (
        "Patru asocieri: SEM↔fidelitate; SEE↔validitate/predicție; CVR↔experți "
        "conținut; X−W/(n−1)↔corecție ghicire."
    ),
    # 11443
    (
        "Trei validități: conținut (domeniu), criteriu (extern), construct "
        "(teoretic). Nu se reduc la același rxy — întrebări diferite."
    ),
    # 11444
    (
        "Taylor-Russell: validitate ↑ → mai multe selecții corecte; rata de bază "
        "și proporția selectată modifică utilitatea practică. Utilitatea e "
        "combinația celor trei factori."
    ),
    # 11445
    (
        "Recapitulare: fidelitate=consistență; validitate=măsoară ce trebuie; "
        "rxy<rtt; SEM↔fidelitate; SEE↔validitate; test-retest temporal; "
        "half-split conținut; inter-rater examinatori; Alpha/KR-20 consistență "
        "internă; MTMM construct."
    ),
]

assert len(SELECIE_PROFESIONALA_EXPLANATIONS) == 40
