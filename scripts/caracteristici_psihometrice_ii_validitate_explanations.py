"""Explicații — Caracteristici psihometrice II, cap. 3: validitate (ID 11346–11405)."""

from __future__ import annotations

from typing import List

VALIDITATE_TEST_EXPLANATIONS: List[str] = [
    # 11346
    (
        "Adevărat. Validitatea de conținut răspunde la întrebarea: itemii acoperă "
        "domeniul? Itemii trebuie să fie un eșantion reprezentativ al universului "
        "de comportamente/conținut vizat — nu doar să fie „buni” la o altă măsură."
    ),
    # 11347
    (
        "Fals. Validitatea predictivă presupune predictor acum, criteriu ulterior "
        "(ex. test de admitere → succes la job peste un an). Dacă criteriul e "
        "măsurat înainte de predictor, logica temporală e inversată."
    ),
    # 11348
    (
        "Adevărat. În MTMM, aceeași trăsătură măsurată prin metode diferite ar "
        "trebui să coreleze puternic (convergență). Asta susține că măsurăm "
        "constructul, nu doar metoda."
    ),
    # 11349
    (
        "Adevărat. rxy (validitate) nu poate depăși rtt (fidelitatea predictorului): "
        "un test instabil nu poate corela mai mult cu criteriul decât măsoară "
        "consistent pe sine. Dacă rxy > rtt, verifică datele sau măsurile."
    ),
    # 11350
    (
        "Fals. SEE = SDy·√(1−rxy²). Când rxy crește, termenul (1−rxy²) scade, deci "
        "SEE scade. Validitate mai bună → predicție mai precisă, nu mai imprecisă."
    ),
    # 11351
    (
        "Adevărat. Contaminarea criteriului: evaluatorul criteriului știe scorul "
        "la test sau criteriul include informații din predictor → bias, rxy umflat "
        "artificial."
    ),
    # 11352
    (
        "Conținut = acoperire domeniu (itemi reprezentativi). Criteriu = legătură "
        "cu indicator extern. Fidelitate = stabilitate/consistență. Discriminarea "
        "e alt concept (item analysis)."
    ),
    # 11353
    (
        "Predictor = scorul testului evaluat (instrumentul). Criteriu = performanță "
        "externă (note, job, diagnostic). Normarea și α sunt alte variabile."
    ),
    # 11354
    (
        "Concurentă: predictor și criteriu aproximativ simultan (ex. test nou vs "
        "test deja validat). Predictivă = criteriu în viitor. Nu e doar consistență "
        "internă."
    ),
    # 11355
    (
        "Lawshe CVR: Ne = experți care marchează itemul „esențial” pentru domeniu. "
        "N = total experți. Formula: CVR = (Ne − N/2) / (N/2). Nu e nr. itemi sau "
        "respondenți."
    ),
    # 11356
    (
        "rxy = coeficient de validitate criterială (corelația predictor–criteriu). "
        "Nu e fidelitate (rtt), dificultate sau reprezentativitate normativă."
    ),
    # 11357
    (
        "Validitatea e limitată de fidelitate: rxy ≤ √rxx·√ryy (logic, rxy nu "
        "depășește rtt al predictorului). Fără măsură stabilă, legătura cu "
        "criteriul e subestimată sau zgomotoasă."
    ),
    # 11358
    (
        "Corecție ghicire grilă: Xcorectat = X − W/(n−1). W = greșeli, n = "
        "alternatives. Scade avantajul răspunsului aleator. Nu adună la scor."
    ),
    # 11359
    (
        "Thorndike: distractori plauzibili, apropiați de răspunsul corect — altfel "
        "itemul nu discriminează cunoștința reală. Evită „toate corecte”, indicii "
        "de lungime, alternanță rigidă."
    ),
    # 11360
    (
        "Construct = trăsătură teoretică (inteligență, extraversie). Validitatea "
        "de construct verifică rețeaua nomologică: ipoteze, convergență, "
        "discriminare — nu timp de completare sau normare."
    ),
    # 11361
    (
        "MTMM convergență: monotrait-heteromethod (aceeași trăsătură, metode "
        "diferite) → corelații mari. Heterotrait-monomethod mari ar sugera "
        "confundare metodă–trăsătură."
    ),
    # 11362
    (
        "Cronbach (construct): 1) ipoteze despre construct; 2) predicții "
        "testabile; 3) cercetare empirică. Nu se oprește la CVR sau la "
        "intuiție fără date."
    ),
    # 11363
    (
        "SEE = eroarea standard a estimării — marja când prezici scorul pe "
        "criteriu din predictor. Legată de validitate (rxy), nu de fidelitate "
        "(SEM e pentru fidelitate)."
    ),
    # 11364
    (
        "rxy mic → relație slabă predictor–criteriu → SEE mare → predicții "
        "împrăștiate. Analog: cu cât corelația e mai mică, cu atât banda de "
        "eroare e mai largă."
    ),
    # 11365
    (
        "Criteriu relevant = măsoară direct ce vrei să prezici (succes job, "
        "performanță clinică). Ușor de colectat sau normal distribuit nu "
        "înseamnă relevant."
    ),
    # 11366
    (
        "Criteriu contaminat = influențat de predictor (evaluator știe scorul "
        "testului). Nu e despre întârziere, obiectivitate pură sau lipsă "
        "varianță."
    ),
    # 11367
    (
        "Item obiectiv: scorare pe cheie (grilă, A/F, perechi). Semiobiectiv = "
        "răspuns scurt cu rubrică. Subiectiv = eseu, interpretare evaluator."
    ),
    # 11368
    (
        "Semiobiectiv: criterii de scorare există, dar aplicarea poate necesita "
        "judecată (ex. răspuns scurt parțial corect). Nu e scorare 100% "
        "automată ca la grilă."
    ),
    # 11369
    (
        "Subiectiv: pondere mare a interpretării evaluatorului (eseu, problemă "
        "deschisă). Scorare automată exclusivă e tipic obiectiv, nu subiectiv."
    ),
    # 11370
    (
        "Smith (orientativ): rxy mai mare → utilitate predictivă mai bună. "
        ">0,50 excelent; 0,40–0,49 bun; 0,30–0,39 acceptabil; <0,30 slab. "
        ">0,70 excepțional — verifică!"
    ),
    # 11371
    (
        "Thorndike: enunț clar, o singură problemă per item. Evită dublu "
        "negativ, amestec de cerințe, ambiguitate inutilă."
    ),
    # 11372
    (
        "Constructorul: definește domeniul, matrice specificații–conținut, "
        "itemi reprezentativi. Obligația principală la validitate de conținut — "
        "nu maximizarea nr. itemi fără relevanță."
    ),
    # 11373
    (
        "Judecători conținut: esențialitate (item necesar domeniului?) și "
        "relevanță (se potrivește domeniului?). Poziția în test sau dificultatea "
        "dorită nu sunt criterii centrale de conținut."
    ),
    # 11374
    (
        "SEE depinde de rxy și SDy — e despre validitate/predicție. SEM (fidelitate) "
        "folosește rtt. SEE ≠ rxy numeric."
    ),
    # 11375
    (
        "Perechi corecte: conținut → acoperire domeniu; criteriu → predictor–"
        "criteriu; construct → teorie + dovezi empirice. Stabilitate temporală "
        "e fidelitate test-retest, nu construct."
    ),
    # 11376
    (
        "Predictivă: timp între predictor și criteriu (viitor). Concurentă: "
        "aproximativ simultan (ex. compară cu test validat). Ambele pot folosi "
        "criterii comportamentale."
    ),
    # 11377
    (
        "Criteriu bun: relevant, fidel suficient, disponibil practic. "
        "Contaminare deliberată distorsionează validitatea — nu e dorită."
    ),
    # 11378
    (
        "Lawshe: CVR = (Ne−N/2)/(N/2). Poate fi negativ dacă <50% experți "
        "consideră esențial. Pragul depinde de N (tabele Lawshe). CVR vine "
        "de la experți, nu de la respondenți."
    ),
    # 11379
    (
        "Contaminare: criteriul include info din predictor; evaluator știe "
        "scorul testului → rxy artificial mare. Nu e dorită; reduce credibilitatea "
        "validității."
    ),
    # 11380
    (
        "rxy ≤ rtt (de regulă). Fidelitate scăzută plafonează validitatea "
        "observată. rxy > rtt nu confirmă automat calitate — e semnal de verificat."
    ),
    # 11381
    (
        "SEE = SDy·√(1−rxy²). rxy ↑ → SEE ↓. SEE nu măsoară consistența internă "
        "(α, KR-20)."
    ),
    # 11382
    (
        "MTMM discriminare: monotrait-heteromethod > heterotrait (constructe "
        "diferite nu trebuie să se confunde). Corelații mari între constructe "
        "distincte slăbesc discriminarea."
    ),
    # 11383
    (
        "Cronbach: definește constructul, derivă predicții, testează empiric. "
        "Revizuiește itemii dacă datele contrazic teoria — nu blochează "
        "permanent instrumentul."
    ),
    # 11384
    (
        "Obiectivi = cheie clară. Semiobiectivi = rubrici + judecată. "
        "Subiectivi au variabilitate între evaluatori — nu o elimină."
    ),
    # 11385
    (
        "Thorndike: fără indicii gramaticale, distractori omogeni ca lungime. "
        "Evită dublu negativ frecvent și „niciuna” ca paravan pentru itemi slabi."
    ),
    # 11386
    (
        "Conținut: delimitare domeniu + eșantionare reprezentativă + judecători. "
        "rxy ridicat e validitate de criteriu, nu de conținut."
    ),
    # 11387
    (
        "Triada judecători conținut: esențialitate, relevanță, claritate. "
        "Viteza de răspuns nu e criteriu clasic de validitate de conținut."
    ),
    # 11388
    (
        "Predictivă: criteriu ulterior; utilă pentru decizii viitoare; poate fi "
        "afectată de schimbări context (job, tratament). Tot necesită criteriu "
        "bine definit."
    ),
    # 11389
    (
        "Concurentă: simultan; compară cu instrument consacrat; nu garantează "
        "predictiv pe termen lung; nu cere obligatoriu randomizare experimentală."
    ),
    # 11390
    (
        "Smith orientativ: rxy mic → utilitate redusă; moderate → decizii de "
        "grup; mari → predicții stabile. rxy pozitiv mic nu e suficient pentru "
        "decizii individuale cu miză mare."
    ),
    # 11391
    (
        "Rețea nomologică: corelații cu variabile apropiate teoretic, "
        "diferențiere de constructe distincte, pattern conform ipotezelor. "
        "Zero relații empirice nu susține constructul."
    ),
    # 11392
    (
        "SEE în unități criteriu; scade cu rxy; mare = predicții dispersate. "
        "α măsoară consistența internă — alt construct decât SEE."
    ),
    # 11393
    (
        "X−W/(n−1): W=greșeli, n=alternatives. Penalizează ghicirea. Când erorile "
        "cresc, scorul corectat scade, nu crește."
    ),
    # 11394
    (
        "Trei tipuri: conținut (domeniu), criteriu (extern), construct (teoretic). "
        "Sunt complementare, nu interschimbabile — fiecare răspunde la o întrebare "
        "diferită despre calitatea testului."
    ),
    # 11395
    (
        "Conținut: specificații, reprezentativitate, judecători. Nu se reduce la "
        "o singură corelație — evaluarea experților e centrală."
    ),
    # 11396
    (
        "Criterial: predictor=test; criteriu=comportamental/academic/profesional; "
        "contaminare umflă rxy; interpretarea cere context (fidelitate, scop "
        "decizie, SEE)."
    ),
    # 11397
    (
        "MTMM (Campbell & Fiske): convergență = monotrait-heteromethod mare; "
        "discriminare = heterotrait relativ mic; pattern comparativ, nu o singură "
        "corelație izolată."
    ),
    # 11398
    (
        "rxy plafonat de fidelitate; fidelitate mică → validitate subestimată; "
        "SEE = f(rxy, SDy); validitate ↑ → SEE ↓. Set complet de legături "
        "predictor–criteriu."
    ),
    # 11399
    (
        "Thorndike (sinteză): enunț clar, distractori plauzibili omogeni, fără "
        "indicii formale, vocabular precis. Reguli pentru calitatea itemilor "
        "obiectivi."
    ),
    # 11400
    (
        "Obiectivi → cheie; semiobiectivi → rubrici; subiectivi → acord "
        "inter-evaluator important. Tipul de item influențează ce validări "
        "sunt fezabile."
    ),
    # 11401
    (
        "Smith: rxy se interpretează după scop (selecție individuală vs grup), "
        "context, calitate criteriu. Pragurile ghidează — nu înlocuiesc "
        "judecata profesională."
    ),
    # 11402
    (
        "Înainte de pilotare: matrice specificații–conținut, revizuire experți "
        "independenți. Eliminarea itemilor dificili sau ordonare aleatoare "
        "deteriorează validitatea de conținut."
    ),
    # 11403
    (
        "Predictor = instrumentul evaluat. Criteriu = indicator extern pentru "
        "decizie. Nu trebuie să fie aceeași măsură; criteriul nu se alege "
        "doar pentru cost mic."
    ),
    # 11404
    (
        "Anti-contaminare: surse separate, evaluatori orbi la scorul predictorului. "
        "Instruirea pe cheia predictorului sau ajustarea criteriului după test "
        "introduce bias."
    ),
    # 11405
    (
        "Prudent: rxy + consecințe decizie + fidelitate + criteriu + SEE. "
        "Nu accepta automat orice rxy pozitiv; nu ignora SEE doar pentru că "
        "rxy depășește 0,20."
    ),
]

assert len(VALIDITATE_TEST_EXPLANATIONS) == 60
