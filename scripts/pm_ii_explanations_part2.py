"""Explicații pedagogice — Psihologia muncii II, itemi 118–234 (indici 117–233).

Conține exact 117 șiruri, corespunzând:
  • DESIGN_MUNCII_ITEMS[37:50]        — itemi 38–50 (design muncă: enrichment + JD-R)
  • SELECTIE_PERSONAL_ITEMS[0:75]     — toți cei 75 de itemi de selecție
  • PERFORMANTA_MUNCII_ITEMS[0:29]    — primii 29 de itemi de performanță
"""

from __future__ import annotations

from typing import List

PART2_EXPLANATIONS: List[str] = [
    # ── DESIGN_MUNCII itemi 38–50 (indici 117–129) ──────────────────────────

    # 117 | Design #38 — job enlargement vs job enrichment
    (
        "Job enlargement (lărgirea muncii) înseamnă adăugarea orizontală de sarcini "
        "similare la același nivel de complexitate: angajatul face mai mult, dar nu "
        "neapărat mai variat sau mai provocator. Job enrichment (îmbogățirea muncii), "
        "în schimb, vizează creșterea verticală a caracteristicilor motivaționale: "
        "autonomie, responsabilitate, feedback semnificativ și identitate a sarcinii. "
        "În modelul Hackman–Oldham, enrichment acționează direct asupra caracteristicilor "
        "centrale care generează meaningfulness, experienced responsibility și knowledge "
        "of results. Enlargement singur poate reduce monotonia, dar fără a crește "
        "indicele de potențial motivațional (MPS)."
    ),

    # 118 | Design #39 — JD-R: definire
    (
        "Modelul cerințe–resurse la locul de muncă (Job Demands-Resources — JD-R), "
        "elaborat de Demerouti și colaboratori, propune că orice caracteristică a "
        "postului poate fi clasificată în una dintre două categorii: cerințe (job "
        "demands) sau resurse (job resources). Cerințele sunt aspecte ale muncii care "
        "necesită efort susținut și pot epuiza angajatul — de exemplu, volumul de "
        "muncă ridicat sau ambiguitatea de rol. Resursele sunt aspecte care ajută la "
        "atingerea obiectivelor, reduc impactul cerințelor sau stimulează creșterea "
        "profesională — de exemplu, autonomia sau suportul colegilor. Această "
        "arhitectură duală explică de ce unele posturi duc la epuizare, iar altele "
        "la implicare ridicată."
    ),

    # 119 | Design #40 — job demands: exemple
    (
        "Cerințele muncii (job demands) sunt caracteristici ale postului care necesită "
        "efort fizic, cognitiv sau emoțional susținut și pot produce oboseală cronică. "
        "✅ Volumul mare de muncă și presiunea de timp impun procesarea rapidă a unui "
        "număr ridicat de sarcini. "
        "✅ Conflictul de rol apare când așteptările din surse diferite sunt "
        "incompatibile, generând tensiune. "
        "✅ Efortul emoțional ridicat este specific profesiilor care presupun gestionarea "
        "suferinței altora, cum ar fi asistența socială sau medicina. "
        "❌ Autonomia și feedback-ul constructiv de la șef sunt resurse, nu cerințe — "
        "ele ajută la atingerea obiectivelor și nu epuizează sistematic angajatul."
    ),

    # 120 | Design #41 — job resources: exemple
    (
        "Resursele muncii (job resources) sunt caracteristici ale postului care sprijină "
        "atingerea obiectivelor, reduc impactul cerințelor și stimulează motivația. "
        "✅ Autonomia și controlul asupra modului de lucru permit angajatului să-și "
        "organizeze activitatea în funcție de competențele proprii. "
        "✅ Feedback-ul social și suportul colegilor sau superiorilor oferă informații "
        "utile și un sentiment de siguranță psihologică. "
        "✅ Oportunitățile de dezvoltare și învățare la locul de muncă cresc sentimentul "
        "de competență și angajamentul pe termen lung. "
        "❌ Presiunea constantă și volumul excesiv de sarcini sunt cerințe care "
        "epuizează, nu resurse care mobilizează."
    ),

    # 121 | Design #42 — cerințe ridicate → burnout
    (
        "În modelul JD-R, cerințele ridicate și prelungite ale muncii — supraîncărcarea "
        "cu sarcini, presiunea cronică de timp sau efortul emoțional continuu — activează "
        "un proces de epuizare progresivă. Când angajatul nu dispune de resurse suficiente "
        "pentru a face față acestor cerințe, resursele personale și organizaționale sunt "
        "consumate treptat, ducând la burnout. Burnout-ul se manifestă prin epuizare "
        "emoțională, detașare de muncă și scăderea sentimentului de eficacitate personală. "
        "Modelul JD-R subliniază că burnout-ul nu apare din cerințe izolate, ci din "
        "dezechilibrul cronic dintre cerințe și resursele disponibile."
    ),

    # 122 | Design #43 — resurse → work engagement
    (
        "În modelul JD-R, resursele muncii sunt principalul motor al implicării (work "
        "engagement). Autonomia, feedback-ul constructiv și oportunitățile de dezvoltare "
        "alimentează motivația intrinsecă și sentimentul de auto-eficacitate. Work "
        "engagement se caracterizează prin energie, dedicare și absorbție în activitate — "
        "o stare pozitivă opusă burnout-ului. Cercetările JD-R arată că prezența "
        "resurselor, chiar și în condiții de cerințe ridicate, poate menține sau crește "
        "implicarea angajaților. Organizațiile care investesc în resurse — suport, "
        "autonomie, oportunități de formare — obțin angajați mai implicați și cu risc "
        "mai redus de epuizare."
    ),

    # 123 | Design #44 — TF: resurse duc la burnout, cerințe la engagement (FALS)
    (
        "Această afirmație este falsă deoarece inversează relațiile din modelul JD-R. "
        "Conform modelului, resursele muncii (autonomie, suport, feedback) sunt asociate "
        "cu work engagement, nu cu burnout. Burnout-ul este produs în principal de "
        "cerințele ridicate și prelungite, mai ales când resursele disponibile sunt "
        "insuficiente pentru a le gestiona. Confundarea direcțiilor de influență este "
        "o greșeală frecventă: cerințele epuizează, resursele mobilizează — nu invers."
    ),

    # 124 | Design #45 — JD-R: perechi cauzale corecte
    (
        "Modelul JD-R descrie două procese paralele și distincte. "
        "✅ Cerințele muncii ridicate și prelungite consumă resursele personale și "
        "conduc la burnout — aceasta este legătura corectă. "
        "✅ Resursele muncii alimentează work engagement — energia, dedicarea și "
        "absorbția în activitate. "
        "❌ Resursele nu conduc la burnout — ele protejează angajatul și mențin "
        "implicarea. "
        "❌ Cerințele ridicate nu produc engagement garantat — fără resurse adecvate, "
        "ele generează epuizare, nu implicare pozitivă. "
        "Aceste relații sunt susținute de meta-analize pe populații ocupaționale diverse."
    ),

    # 125 | Design #46 — asistent social: cerințe JD-R
    (
        "Volumul mare de cazuri, termenele strânse și contactul zilnic cu suferința "
        "clienților sunt exemple clasice de cerințe ale muncii (job demands) în modelul "
        "JD-R. Aceste caracteristici consumă energia cognitivă și emoțională a "
        "asistentului social, mai ales dacă sunt cronice și nu sunt compensate de resurse "
        "adecvate (suport din partea supervizorului, autonomie, formare profesională). "
        "Ele nu sunt resurse, deoarece nu ajută la atingerea obiectivelor sau la "
        "creșterea profesională — dimpotrivă, cresc riscul de burnout dacă nu există "
        "mecanisme de recuperare suficiente."
    ),

    # 126 | Design #47 — echipă: autonomie + feedback + formare = resurse JD-R
    (
        "Autonomia în programarea activităților, feedback-ul regulat din partea "
        "superiorului și accesul la formare profesională sunt resurse ale muncii (job "
        "resources) în modelul JD-R. Autonomia permite angajatului să-și adapteze "
        "ritmul și metodele la propriile puncte forte, reducând tensiunea din cerințe. "
        "Feedback-ul regulat oferă claritate despre progres și direcție, reducând "
        "ambiguitatea. Accesul la formare crește competența și sentimentul de "
        "auto-eficacitate. Împreună, aceste resurse alimentează work engagement și "
        "reduc riscul de burnout, chiar în condiții de cerințe ridicate."
    ),

    # 127 | Design #48 — diferențe Hackman-Oldham vs JD-R
    (
        "Modelul Hackman–Oldham se concentrează pe caracteristicile intrinseci ale "
        "sarcinii — varietatea abilităților, identitatea sarcinii, semnificația sarcinii, "
        "autonomia și feedback-ul — și descrie modul în care acestea generează stări "
        "psihologice critice (meaningfulness, experienced responsibility, knowledge of "
        "results) și motivație internă, cuantificate printr-un indice de potențial "
        "motivațional (MPS). Modelul JD-R, în schimb, clasifică orice caracteristică "
        "a postului în cerințe sau resurse și descrie două procese distincte: epuizarea "
        "provocată de cerințe și implicarea generată de resurse. Cele două modele sunt "
        "complementare, nu identice: Hackman–Oldham explică de ce anumite sarcini "
        "motivează, JD-R explică de ce anumite posturi produc burnout sau engagement. "
        "Hackman–Oldham nu explică burnout-ul, iar JD-R nu folosește formula MPS."
    ),

    # 128 | Design #49 — resursele atenuează cerințele
    (
        "Cercetarea din jurul modelului JD-R a demonstrat că resursele muncii pot "
        "atenua efectul negativ al cerințelor ridicate asupra bunăstării angajaților — "
        "aceasta se numește ipoteza de tampon (buffer hypothesis). Atunci când angajații "
        "dispun de autonomie, suport social sau oportunități de formare, impactul "
        "stresant al supraîncărcării sau al ambiguității de rol este redus. Implicația "
        "practică este importantă: chiar și în roluri cu cerințe ridicate, furnizarea "
        "de resurse adecvate poate preveni epuizarea. Afirmațiile că resursele produc "
        "burnout sau că cerințele garantează engagement nu sunt susținute de datele "
        "empirice — relațiile merg în direcția opusă."
    ),

    # 129 | Design #50 — consultant 5 intervenții: Hackman-Oldham + JD-R
    (
        "Intervențiile consultantului pot fi clasificate în funcție de modelul teoretic "
        "vizat. "
        "✅ Clarificarea impactului muncii asupra echipei (1) vizează semnificația "
        "sarcinii (task significance) din modelul Hackman–Oldham, care contribuie la "
        "experiența de meaningfulness. "
        "✅ Lăsarea libertății în ordinea sarcinilor (2) corespunde autonomiei (autonomy), "
        "care generează responsabilitate psihologică percepută (experienced responsibility). "
        "✅ Raportul săptămânal de rezultate (3) este un mecanism de feedback privind "
        "performanța, a treia caracteristică care completează triada Hackman–Oldham. "
        "✅ Reducerea ambiguității rolului (4) și accesul la mentorat (5) sunt resurse "
        "ale muncii în sens JD-R: prima reduce o cerință (ambiguitatea), a doua adaugă "
        "o resursă de suport și dezvoltare. "
        "❌ Mentoratul nu este o cerință — el sprijină angajatul, nu îl epuizează. "
        "Abordarea combinată Hackman–Oldham plus JD-R este mai completă decât oricare "
        "model aplicat singur."
    ),

    # ── SELECTIE_PERSONAL itemi 1–75 (indici 130–204) ───────────────────────

    # 130 | Selecție #1 — TF: selecția ca predicție (ADEVĂRAT)
    (
        "Afirmația este adevărată. În selecția personalului, niciun instrument — test "
        "de aptitudine, interviu structurat sau probă de lucru — nu observă direct "
        "performanța viitoare: el estimează probabilitatea că un candidat va reuși în "
        "rol. Această logică de predicție presupune că există o legătură statistică "
        "între scorul la instrumentul de selecție (predictor) și performanța ulterioară "
        "la job (criteriu). Validitatea acestei estimări se exprimă prin coeficientul "
        "de corelație dintre predictor și criteriu. Recunoașterea selecției ca proces "
        "de predicție, nu de certitudine, este fundamentală pentru interpretarea corectă "
        "a rezultatelor și pentru stabilirea unor așteptări realiste față de instrumentele "
        "folosite."
    ),

    # 131 | Selecție #2 — predictor vs criteriu
    (
        "Predictorul este instrumentul folosit în procesul de selecție — de exemplu, "
        "un test de aptitudini cognitive, un interviu structurat sau o probă de lucru — "
        "care servește pentru a estima potențialul de succes al candidatului înainte de "
        "angajare. Criteriul este performanța reală la job, evaluată după angajare — "
        "de exemplu, ratingul managerului la șase luni, numărul de erori sau volumul "
        "vânzărilor. Cei doi termeni nu sunt interschimbabili: predictorul precede "
        "angajarea, criteriul urmează după ea. Validitatea unui instrument de selecție "
        "se determină tocmai prin studiul corelației dintre scorul la predictor și "
        "valoarea criteriului."
    ),

    # 132 | Selecție #3 — test + interviu = predictori
    (
        "Atunci când un consultant aplică un test de aptitudine și un interviu structurat "
        "în procesul de selecție, ambele instrumente îndeplinesc rolul de predictori: "
        "ele măsoară variabile observabile în prezent pentru a estima performanța viitoare "
        "a candidaților. Predictorul nu este performanța în sine — el o anticipează "
        "pe baza unei corelații verificate empiric. Criteriile de performanță, în schimb, "
        "sunt colectate după angajare și servesc pentru a evalua cât de bine predictorul "
        "a funcționat ca instrument de prognoză. Termenul tehnic predictor subliniază "
        "scopul prospectiv al măsurătorii, spre deosebire de simpla expresie instrument "
        "de evaluare."
    ),

    # 133 | Selecție #4 — performanța la 6 luni = criteriu
    (
        "Performanța evaluată la șase luni după angajare reprezintă criteriul în studiile "
        "de validitate a selecției. Criteriul este standardul față de care verificăm dacă "
        "predictorul a funcționat: dacă scorurile obținute la selecție corelează cu "
        "performanța reală ulterioară, instrumentul are validitate predictivă. Criteriul "
        "poate lua forme diverse — ratinguri de performanță acordate de manager, indicatori "
        "obiectivi de productivitate sau evaluări comportamentale — dar în toate cazurile "
        "este măsurat după momentul angajării, nu înainte. Fără un criteriu colectat "
        "post-angajare nu se poate determina validitatea predictivă a instrumentului "
        "de selecție."
    ),

    # 134 | Selecție #5 — logica predicției: afirmații corecte
    (
        "Selecția personalului este un proces probabilistic, nu de certitudine: scorurile "
        "la instrumentele de selecție permit inferențe despre succesul viitor la job, cu "
        "o marjă de eroare inerentă. "
        "✅ Validitatea unui predictor se stabilește prin corelarea statistică a scorurilor "
        "cu criteriul de performanță colectat ulterior. "
        "✅ Fără criteriu post-angajare nu există baza necesară pentru a calibra utilitatea "
        "instrumentului. "
        "❌ Un scor bun la selecție crește probabilitatea de succes, dar nu îl garantează — "
        "factori contextuali necontrolați influențează mereu performanța. "
        "Recunoașterea caracterului probabilistic al selecției protejează atât organizațiile, "
        "cât și candidații de așteptări nerealiste."
    ),

    # 135 | Selecție #6 — interviu 10 minute nu măsoară direct
    (
        "Selecția estimează probabilitatea de succes a candidaților, nu observă direct "
        "performanța lor viitoare. Un interviu de zece minute poate oferi indicii utile "
        "despre anumite caracteristici, dar nu poate reproduce condițiile reale ale "
        "jobului pe ani de activitate. Confundarea unei estimări cu o observație directă "
        "este o eroare frecventă în practică — chiar și un interviu nestructurat, oricât "
        "de convingător, rămâne un predictor, nu o dovadă a performanței viitoare. "
        "Valoarea unui instrument de selecție se evaluează prin validitatea sa predictivă, "
        "adică prin cât de bine scorul obținut prezice performanța efectivă la job "
        "verificată ulterior."
    ),

    # 136 | Selecție #7 — TF falsă: predictor ≠ criteriu obligatoriu același test
    (
        "Afirmația că predictorul și criteriul trebuie să fie mereu același test aplicat "
        "în momente diferite este falsă. Predictorul și criteriul sunt tipuri distincte "
        "de variabile: predictorul este instrumentul de selecție (un test, un interviu, "
        "o probă de lucru), iar criteriul este performanța reală la job, evaluată prin "
        "cu totul alte mijloace — ratinguri de la manager, indicatori de productivitate "
        "sau indicatori comportamentali. Confundarea lor ar face imposibil studiul "
        "validității predictive, deoarece nu ai compara ce ai măsurat la selecție cu "
        "ce s-a întâmplat la job. Predictorii și criteriile pot fi instrumente total "
        "diferite — tocmai această diferență le conferă relevanță pentru validarea "
        "procedurii de selecție."
    ),

    # 137 | Selecție #8 — perechi predictor-criteriu corecte
    (
        "Perechile predictor–criteriu sunt corect formulate când instrumentul de selecție "
        "anticipează logic tipul de performanță evaluat ulterior. "
        "✅ Un test de integritate prezice reducerea comportamentelor contraproductive "
        "(CWB) — furt, absenteism deliberat, sabotaj — legătură confirmată empiric. "
        "✅ Aptitudinea mentală generală (GMA) prezice performanța în training și la job "
        "prin capacitatea de a învăța și rezolva probleme complexe. "
        "✅ O probă de lucru prezice calitatea lucrului prestat în rol, prin similitudinea "
        "directă cu sarcinile reale. "
        "❌ Numărul de pagini din CV nu are bază teoretică sau empirică pentru predicția "
        "coeficientului de inteligență."
    ),

    # 138 | Selecție #9 — GMA: cel mai puternic predictor
    (
        "Meta-analizele din psihologia personalului, în special cele ale lui Schmidt și "
        "Hunter, arată că aptitudinea mentală generală (GMA) este unul dintre cei mai "
        "puternici și cei mai consistenți predictori individuali ai performanței la job. "
        "Această relație se menține indiferent de domeniu ocupațional, deoarece GMA "
        "reflectă capacitatea de a procesa informații, de a rezolva probleme noi și de "
        "a învăța rapid proceduri complexe. Cu cât complexitatea jobului este mai ridicată, "
        "cu atât validitatea predictivă a GMA crește. Vârsta cronologică, culorile preferate "
        "sau numărul de hobby-uri nu sunt predictori valizi ai performanței la job "
        "conform datelor empirice."
    ),

    # 139 | Selecție #10 — conștiinciozitate: performanță mai ridicată și mai stabilă
    (
        "Conștiinciozitatea este o trăsătură de personalitate din modelul Big Five care "
        "descrie tendința de a fi organizat, perseverent, disciplinat și responsabil în "
        "îndeplinirea sarcinilor. Meta-analizele au confirmat că persoanele cu "
        "conștiinciozitate ridicată obțin, în medie, niveluri mai ridicate de performanță "
        "la job. Pe lângă nivelul mediu mai bun, conștiinciozitatea contribuie și la "
        "stabilitatea în timp: angajații conștiincioși mențin un efort constant și "
        "îndeplinesc standardele în mod regulat, reducând fluctuația performanței. "
        "Conștiinciozitatea nu reduce validitatea testelor de aptitudine — cele două "
        "măsoară constructe distincte și se pot combina cu succes în baterii de selecție."
    ),

    # 140 | Selecție #11 — teste de integritate → CWB redus
    (
        "Testele de integritate sunt instrumente de selecție proiectate să evalueze "
        "tendința candidaților spre comportamente oneste, respectuoase față de reguli "
        "și lipsa predispoziției pentru conduită contraproductivă. Meta-analizele arată "
        "că scorurile ridicate la testele de integritate prezic negativ comportamentele "
        "contraproductive la locul de muncă (CWB) — furt, absenteism deliberat, sabotaj. "
        "Totodată, ele prezic pozitiv respectarea politicilor și regulamentelor "
        "organizaționale. Aceste teste nu măsoară aptitudinea mentală generală și nu "
        "prezic fluctuația salariului de bază — sunt instrumente specifice dimensiunii "
        "de onestitate și conformitate normativă."
    ),

    # 141 | Selecție #12 — probe de lucru (work samples)
    (
        "Probele de lucru (work sample tests) sunt instrumente în care candidatul "
        "execută, în condiții controlate, sarcini reprezentative pentru rolul la care "
        "aplică. Validitatea lor predictivă este printre cele mai ridicate din bateria "
        "instrumentelor de selecție, deoarece există o similitudine directă și ridicată "
        "între sarcina din probă și sarcinile reale de la job. Probele de lucru măsoară "
        "comportamentul efectiv în context simulat — nu doar declarații despre competențe "
        "sau trăsături de personalitate. Ele nu sunt aplicabile pe hârtie fără observarea "
        "comportamentului: tocmai execuția sarcinii în fața unui evaluator le conferă "
        "validitate ridicată față de multe alte metode de selecție."
    ),

    # 142 | Selecție #13 — predictori cu utilitate empirică ridicată
    (
        "Literatura de selecție a personalului identifică mai mulți predictori cu "
        "utilitate empirică consistentă, susținută de meta-analize. "
        "✅ Aptitudinea mentală generală (GMA) prezice capacitatea de învățare și "
        "rezolvare de probleme. "
        "✅ Conștiinciozitatea prezice consecvența și autodisciplina în rol. "
        "✅ Testele de integritate reduc riscul comportamentelor contraproductive. "
        "✅ Probele de lucru, prin similitudinea cu sarcinile reale, au una dintre cele "
        "mai ridicate validități predictive. "
        "Folosiți în combinație, acești predictori pot oferi o imagine mai completă "
        "a potențialului candidaților și pot crește validitatea multiplă a bateriei "
        "de selecție."
    ),

    # 143 | Selecție #14 — furturi → teste de integritate
    (
        "Atunci când un angajator urmărește în mod specific reducerea furturilor, a "
        "absenteismului deliberat și a altor încălcări de regulament, testele de "
        "integritate sunt predictori cei mai relevanți. Aceste instrumente au fost "
        "proiectate pentru a identifica candidații predispuși la comportamente "
        "contraproductive, iar meta-analizele confirmă legătura lor cu CWB. Aptitudinea "
        "mentală generală (GMA) prezice performanța cognitivă și capacitatea de "
        "învățare, dar nu vizează specific onestitatea sau respectarea normelor "
        "organizaționale. Numărul de recomandări scrise sau preferința pentru lucru "
        "în echipă nu sunt validate ca predictori ai comportamentelor contraproductive."
    ),

    # 144 | Selecție #15 — TF: GMA nu e predictor slab (FALS)
    (
        "Această afirmație este falsă. Aptitudinea mentală generală (GMA) este, în mod "
        "constant, unul dintre cei mai puternici predictori individuali ai performanței "
        "la job în literatura de specialitate. Meta-analizele lui Schmidt și Hunter "
        "arată că GMA are validitate predictivă mai mare decât majoritatea testelor de "
        "personalitate luate individual. Testele de personalitate pot aduce valoare "
        "incrementală față de GMA (de exemplu, conștiinciozitatea adaugă informație "
        "suplimentară), dar nu o întrec ca predictor unic al performanței la job în "
        "contexte complexe. A considera GMA un predictor slab este o eroare gravă care "
        "poate duce la decizii de selecție suboptimale."
    ),

    # 145 | Selecție #16 — conștiinciozitate → stabilitatea performanței
    (
        "Persoanele cu conștiinciozitate ridicată tind să-și organizeze efortul în mod "
        "sistematic, să stabilească obiective clare și să urmeze procedurile stabilite. "
        "Această autodisciplină produce nu doar un nivel mediu mai bun al performanței, "
        "ci și o variabilitate mai redusă de la o perioadă la alta: angajatul conștiincios "
        "menține standardele în mod constant, chiar și în perioade mai dificile. "
        "Perseverența și fiabilitatea, care sunt nucleul trăsăturii, explică această "
        "stabilitate. Conștiinciozitatea nu măsoară direct coeficientul de inteligență "
        "și nu elimină nevoia de feedback sau supervizare — este o trăsătură de "
        "personalitate, nu o aptitudine cognitivă."
    ),

    # 146 | Selecție #17 — probe de lucru: exemple
    (
        "O probă de lucru este, prin definiție, o sarcină extrasă din conținutul real "
        "al rolului și administrată candidaților în condiții controlate. "
        "✅ Un candidat la un post de secretariat care redactează un document tipic în "
        "timp limitat execută exact tipul de activitate pe care o va face zilnic în rol. "
        "✅ Un programator care rezolvă o problemă reprezentativă pentru proiectul "
        "echipei este evaluat pe o sarcină similară celor reale. "
        "❌ Un chestionar despre valori personale fără sarcină de rol nu este probă de "
        "lucru — nu implică execuția comportamentului specific postului. "
        "❌ Verificarea diplomelor fără observarea comportamentului nu este probă de "
        "lucru — nu pune candidatul să execute sarcinile din post."
    ),

    # 147 | Selecție #18 — GMA vs conștiinciozitate vs integritate
    (
        "Cele trei constructe vizează dimensiuni diferite ale potențialului la job și "
        "nu sunt sinonime. "
        "✅ GMA reflectă capacitatea de procesare cognitivă: permite candidaților să "
        "proceseze informații noi, să rezolve probleme complexe și să învețe rapid. "
        "✅ Conștiinciozitatea vizează autodisciplina, organizarea, perseverența și "
        "fiabilitatea în îndeplinirea angajamentelor — este o trăsătură de personalitate. "
        "✅ Integritatea se leagă de onestitate, respectarea normelor și absența "
        "predispoziției la comportamente contraproductive. "
        "❌ Toți trei nu măsoară același construct — acoperă aspecte distincte și "
        "complementare ale succesului la job, ceea ce justifică combinarea lor în "
        "baterii de selecție."
    ),

    # 148 | Selecție #19 — r ≈ 0,30 util combinat
    (
        "Un coeficient de corelație de aproximativ 0,30 între un predictor și criteriul "
        "de performanță corespunde validității moderate în literatura de selecție a "
        "personalului. Deși nu este o corelație puternică, un predictor cu r ≈ 0,30 "
        "poate fi practic util, mai ales dacă este combinat cu alți predictori care "
        "aduc informații distincte despre candidat. Utilitatea economică a selecției "
        "depinde nu numai de magnitudinea corelației, ci și de raportul de selecție "
        "și de rata de bază. Un predictor cu validitate moderată devine cu adevărat "
        "inutil numai dacă există un altul mai valid care acoperă exact același "
        "construct, fără informație suplimentară."
    ),

    # 149 | Selecție #20 — GMA pentru sarcini complexe
    (
        "Atunci când un post implică necesitatea de a asimila rapid proceduri complexe, "
        "de a rezolva probleme noi și de a lua decizii în situații ambigue, aptitudinea "
        "mentală generală (GMA) este predictorul cel mai relevant. GMA reflectă "
        "capacitatea de a procesa informații, de a raționa logic și de a transfera "
        "cunoștințele în situații noi — exact ce necesită munca intelectuală complexă. "
        "Un test de integritate pentru retail este relevant pentru prevenirea CWB, "
        "nu pentru capacitatea de rezolvare a problemelor complexe. Măsurarea înălțimii "
        "candidaților sau a preferinței pentru lucru fizic în exterior nu au fundament "
        "empiric ca predictori ai performanței cognitive."
    ),

    # 150 | Selecție #21 — r = 0,30 = validitate moderată
    (
        "În psihologia personalului și selecției, coeficienții de corelație sunt "
        "interpretați pe o scală de convenție: un r de aproximativ 0,10 indică o "
        "validitate slabă, r de aproximativ 0,30 este considerat validitate moderată, "
        "r de aproximativ 0,50 reflectă o validitate bună, iar r de 0,70 sau mai mare "
        "semnalează o validitate foarte puternică. Aceste praguri nu sunt absolute, "
        "dar oferă un reper util pentru evaluarea instrumentelor de selecție. O "
        "validitate moderată nu înseamnă că instrumentul este inutil — în context de "
        "selecție cu raport de selecție scăzut, chiar un r de 0,30 poate aduce câștiguri "
        "practice semnificative față de selecția aleatorie."
    ),

    # 151 | Selecție #22 — praguri r: toate corecte
    (
        "Literatura de specialitate în selecția personalului folosește mai multe praguri "
        "orientative pentru interpretarea coeficienților de corelație validitate–criteriu. "
        "✅ Un r de aproximativ 0,10 este clasificat ca validitate slabă. "
        "✅ Un r de aproximativ 0,30 corespunde validității moderate. "
        "✅ Un r de aproximativ 0,50 reflectă o validitate bună. "
        "✅ Un r de 0,70 sau mai mare este clasificat ca validitate foarte puternică. "
        "Aceste repere provin din convențiile psihologiei diferențiale și permit "
        "compararea instrumentelor de selecție între ele. Utilitatea practică a unui "
        "predictor nu depinde exclusiv de magnitudinea r, ci și de contextul "
        "organizațional și de raportul de selecție."
    ),

    # 152 | Selecție #23 — validitate incrementală
    (
        "Validitatea incrementală descrie contribuția unui predictor nou la puterea "
        "predictivă totală a bateriei de selecție, dincolo de ceea ce predictorii "
        "existenți explică deja. Dacă aptitudinea mentală generală (GMA) este deja "
        "folosită și un nou test de personalitate crește proporția varianței explicate "
        "din criteriu (R pătrat), acel test are validitate incrementală — aduce "
        "informații complementare, nu redundante. "
        "✅ Validitatea incrementală crește puterea predictivă a combinației peste ce "
        "oferă fiecare singur. "
        "❌ Nu înlocuiește complet nevoia de orice alt test. "
        "❌ Nu este zero pur și simplu dacă noul predictor corelează parțial cu GMA — "
        "contează dacă adaugă ceva dincolo de suprapunerea cu GMA."
    ),

    # 153 | Selecție #24 — validitate multiplă R
    (
        "Validitatea multiplă (R) reprezintă corelația dintre combinația lineară optimă "
        "a mai multor predictori și criteriul de performanță. Spre deosebire de r simplu, "
        "care descrie relația unui singur predictor cu criteriul, R reflectă forța "
        "predictivă a unui set de instrumente folosite împreună — de exemplu, un test "
        "de aptitudini plus un interviu structurat. R este mereu cel puțin la fel de "
        "mare ca cel mai bun r individual din set și crește pe măsură ce adaugi "
        "predictori valizi cu validitate incrementală. Procentul de candidați angajați "
        "din total aplicanți — raportul de selecție — este un alt concept, fără legătură "
        "directă cu R."
    ),

    # 154 | Selecție #25 — R² = proporția varianței explicate
    (
        "Proporția varianței explicate, notată R pătrat, este pătratul coeficientului "
        "de validitate multiplă (R) și reprezintă fracțiunea din variabilitatea "
        "criteriului de performanță care este statistic asociată cu setul de predictori "
        "din modelul de selecție. De exemplu, R pătrat = 0,30 înseamnă că aproximativ "
        "30 la sută din variația performanței poate fi atribuită scorurilor combinate "
        "la predictorii folosiți. Ceilalți 70 la sută sunt explicați de alți factori "
        "neincluși: experiența anterioară, contextul organizațional, schimbări de piață "
        "sau caracteristici nemăsurate. R pătrat nu este corelația simplă r și nici "
        "raportul de selecție sau sensibilitatea procedurii."
    ),

    # 155 | Selecție #26 — TF: R² ≠ r (FALS)
    (
        "Această afirmație este falsă. Coeficientul de corelație simplă r descrie "
        "legătura liniară dintre un singur predictor și criteriu, sau, în cazul "
        "validității multiple, dintre combinația de predictori și criteriu. Proporția "
        "varianței explicate (R pătrat) este pur și simplu pătratul lui R: R pătrat "
        "= R ori R. Ele nu sunt același indicator — r (sau R) măsoară puterea și "
        "direcția relației, în timp ce R pătrat exprimă proporția varianței din criteriu "
        "explicată de predictor sau de setul de predictori. Amestecarea lor duce la "
        "interpretări eronate ale puterii unui instrument de selecție."
    ),

    # 156 | Selecție #27 — R=0,55, R²≈0,30: interpretare
    (
        "Când R = 0,55, proporția varianței explicate este R pătrat = 0,55 ori 0,55 ≈ "
        "0,30, adică aproximativ 30 la sută. Aceasta înseamnă că scorurile combinate "
        "la aptitudinea mentală generală (GMA) și interviul structurat explică statistic "
        "aproximativ 30 la sută din variabilitatea performanței observate la job. Nu "
        "înseamnă că 55 la sută dintre angajați vor performa perfect — R este un "
        "coeficient de corelație, nu o rată de succes. Cei aproximativ 70 la sută din "
        "variația performanței neexplicată reflectă factori neincluși în modelul de "
        "selecție: calitatea supervizării, cultura echipei, oportunități de formare "
        "sau evenimente neprevăzute."
    ),

    # 157 | Selecție #28 — validitate în selecție: afirmații corecte
    (
        "Interpretarea corecță a validității în selecție presupune mai multe nuanțe. "
        "✅ Un coeficient r = 0,50 reflectă o legătură predictivă bună, situată "
        "deasupra valorii moderate de 0,30 și la nivelul pragului bun din literatura "
        "de specialitate. "
        "✅ Validitatea incrementală devine relevantă când organizația dorește să adauge "
        "un nou instrument la bateria de selecție — dacă noul predictor crește R pătrat, "
        "contribuie cu informație distinctă. "
        "✅ Un r = 0,10 poate fi modest, dar nu este egal cu zero informație — în "
        "condiții de raport de selecție scăzut poate aduce totuși un câștig practic. "
        "❌ Validitatea perfectă (r = 1) nu apare la niciun instrument real — interviul "
        "nestructurat are, dimpotrivă, una dintre cele mai scăzute validități din "
        "literatura de specialitate."
    ),

    # 158 | Selecție #29 — combinare predictori crește R
    (
        "Combinarea mai multor predictori valizi poate crește validitatea multiplă (R) "
        "față de un singur instrument din două motive principale. În primul rând, "
        "predictori diferiți pot capta fațete distincte ale performanței viitoare: "
        "GMA reflectă capacitatea cognitivă, conștiinciozitatea reflectă autodisciplina, "
        "iar o probă de lucru reflectă abilitatea practică — aceste fațete sunt parțial "
        "independente. În al doilea rând, erorile de măsurare ale predictorii parțial "
        "independenți tind să se compenseze în modelul combinat, reducând zgomotul total. "
        "Combinarea nu elimină complet erorile și nu garantează că R pătrat crește "
        "infinit, dar oferă o predicție mai robustă decât orice instrument izolat."
    ),

    # 159 | Selecție #30 — r=0,25 după GMA: validitate incrementală
    (
        "Dacă un test nou corelează r = 0,25 cu performanța și adăugarea lui la modelul "
        "care conține deja GMA crește proporția varianței explicate (R pătrat), atunci "
        "testul are validitate incrementală — el aduce informații despre performanța "
        "viitoare care nu sunt deja cuprinse în GMA. Validitatea incrementală nu "
        "presupune ca noul predictor să fie mai valid decât GMA sau să nu coreleze "
        "deloc cu aceasta: chiar dacă testul și GMA corelează parțial, dacă partea "
        "unică de varianță explicată crește R pătrat, contribuția este reală și "
        "justifică includerea noului predictor în bateria de selecție."
    ),

    # 160 | Selecție #31 — diferența r vs R²
    (
        "Coeficientul de corelație r — sau R în cazul validității multiple — descrie "
        "forța și direcția relației dintre predictor și criteriu pe o scală de la -1 "
        "la 1. Proporția varianței explicate (R pătrat) este pătratul lui R și "
        "reprezintă fracțiunea din variabilitatea criteriului atribuibilă variabilității "
        "predictorilor, exprimată ca proporție cuprinsă între 0 și 1. De exemplu, "
        "R = 0,50 înseamnă R pătrat = 0,25, adică 25 la sută din varianța criteriului "
        "este explicată. Cele două nu se aplică diferit în funcție de tipul de test — "
        "se aplică la orice design de validare, indiferent dacă predictorii sunt "
        "teste de aptitudini sau teste de personalitate."
    ),

    # 161 | Selecție #32 — r=0,72 = validitate foarte puternică
    (
        "Un coeficient de corelație de 0,72 între un predictor și criteriul de "
        "performanță la job corespunde categoriei de validitate foarte puternică, "
        "conform pragurilor convenționale din psihologia selecției (r de 0,70 sau mai "
        "mare). Aceasta este o corelație remarcabilă pentru datele din selecția "
        "personalului, unde r de 0,50 este deja considerată bună. Un r de 0,72 ar "
        "plasa instrumentul respectiv printre cei mai valizi predictori disponibili. "
        "Probele de lucru pentru roluri cu conținut bine definit pot atinge uneori "
        "aceste niveluri, mai ales când postul implică sarcini cu variabilitate "
        "redusă și cerințe tehnice clare."
    ),

    # 162 | Selecție #33 — sensibilitate: reduce false negative
    (
        "Sensibilitatea unei proceduri de selecție se referă la capacitatea ei de a "
        "detecta candidații care vor reuși la job — adică de a nu-i pierde prin "
        "respingere eronată. O sensibilitate ridicată înseamnă că instrumentul "
        "identifică corect o proporție mare dintre candidații cu adevărat potriviți, "
        "reducând astfel falsele negative: situații în care un candidat competent "
        "este respins pentru că testul nu l-a recunoscut ca potrivit. Sensibilitatea "
        "nu vizează în mod direct falsele pozitive — acela este obiectivul specificității. "
        "Reducerea ratei de bază sau a coeficientului r nu este efectul direct al "
        "sensibilității ridicate."
    ),

    # 163 | Selecție #34 — specificitate: identifică și elimină nepotriviții
    (
        "Specificitatea descrie capacitatea procedurii de selecție de a identifica și "
        "elimina candidații care nu vor performa la nivelul cerut. "
        "✅ Specificitatea ridicată înseamnă că instrumentul respinge corect candidații "
        "nepotriviți, reducând falsele pozitive — angajarea greșită a unor persoane "
        "care nu ating standardele de performanță. "
        "✅ Cu cât specificitatea este mai mare, cu atât mai puțini candidați slabi "
        "trec filtrul de selecție și sunt angajați. "
        "❌ Maximizarea deliberată a falselor negative ar fi contrară obiectivului "
        "oricărei organizații care dorește să angajeze candidați buni. "
        "Specificitatea și sensibilitatea se află adesea într-un compromis: creșterea "
        "uneia fără ajustarea celeilalte poate duce la scăderea celeilalte."
    ),

    # 164 | Selecție #35 — TF: sensibilitate reduce FP (FALS)
    (
        "Această afirmație este falsă. Sensibilitatea ridicată a unui test de selecție "
        "reduce falsele negative — adică reduce riscul de a respinge candidați cu "
        "adevărat potriviți. Specificitatea ridicată reduce falsele pozitive — adică "
        "reduce riscul de a angaja candidați care nu vor performa corespunzător. "
        "Confundarea celor doi termeni este o greșeală frecventă: sensibilitatea "
        "protejează candidații buni de respingere eronată, în timp ce specificitatea "
        "protejează organizația de angajări greșite. Cele două constructe descriu "
        "tipuri diferite de erori și vizează aspecte complementare ale eficienței "
        "unui instrument de selecție."
    ),

    # 165 | Selecție #36 — perechi concepte cu efecte asupra erorilor
    (
        "Relația dintre sensibilitate, specificitate și tipul de erori în selecție "
        "urmează o logică precisă. "
        "✅ Dacă procedura detectează mai bine candidații buni — sensibilitate ridicată — "
        "mai puțini candidați buni sunt respinși eronat, adică se reduc falsele negative. "
        "✅ Dacă procedura respinge mai corect candidații slabi — specificitate ridicată — "
        "mai puțini candidați slabi sunt angajați greșit, adică se reduc falsele pozitive. "
        "❌ Sensibilitate ridicată nu reduce angajările greșite — acelea sunt false "
        "pozitive, controlate de specificitate. "
        "❌ Specificitate ridicată nu reduce respingerile greșite — acelea sunt false "
        "negative, controlate de sensibilitate."
    ),

    # 166 | Selecție #37 — candidat competent respins = false negative
    (
        "Falsul negativ în selecție apare atunci când un candidat care ar fi performat "
        "bine la job este respins de procedura de selecție din cauza unui scor "
        "insuficient la predictor. Instrumentul de selecție l-a clasificat incorect "
        "ca nepotrivit, deși în realitate era potrivit pentru rol. Aceasta este o "
        "eroare de omisiune — s-a ratat un caz real pozitiv. Falsele negative "
        "reprezintă un cost ascuns pentru organizație: aceasta pierde candidați "
        "valoroși eliminați incorect. Reducerea lor este obiectivul sensibilității "
        "ridicate a procedurii de selecție, nu al specificității."
    ),

    # 167 | Selecție #38 — angajat cu scor mare dar performanță slabă = false positive
    (
        "Falsul pozitiv apare atunci când un candidat obține un scor bun la "
        "instrumentele de selecție, este angajat, dar ulterior performează sub "
        "standardele așteptate. Instrumentul de selecție l-a clasificat incorect "
        "ca potrivit, deși în realitate nu a reușit la job. Aceasta este o eroare "
        "de includere — un caz negativ a trecut filtrul ca pozitiv. Falsele pozitive "
        "generează costuri organizaționale directe: timp și resurse investite în "
        "onboarding, performanță scăzută în echipă și eventuala necesitate a "
        "despărțirii de angajat. Reducerea falselor pozitive este obiectivul "
        "specificității ridicate a procedurii de selecție."
    ),

    # 168 | Selecție #39 — FP și FN: definiții corecte
    (
        "Falsele pozitive și falsele negative sunt două tipuri de erori opuse în "
        "selecția personalului. "
        "✅ Falsul pozitiv apare când un candidat angajat nu atinge performanța "
        "așteptată la job — a trecut filtrul, dar nu s-a dovedit potrivit. "
        "✅ Falsul negativ apare când un candidat respins ar fi reușit la job — "
        "a fost eliminat, deși era potrivit. "
        "❌ Falsul pozitiv nu este candidat respins pe nedrept — acela este falsul "
        "negativ. "
        "❌ Nici una dintre erori nu dispare automat când r depășește 0,30 — "
        "validitatea moderată reduce erorile, dar nu le elimină complet niciodată, "
        "deoarece predicția are mereu o marjă de incertitudine."
    ),

    # 169 | Selecție #40 — test strict → specificitate ridicată
    (
        "Un test de selecție cu prag foarte strict tinde să angajeze rar candidați "
        "nepotriviți, deoarece îi filtrează cu mare atenție — aceasta corespunde "
        "unei specificități ridicate. Totuși, tocmai din cauza pragului ridicat, "
        "testul poate respinge și unii candidați buni care nu ating scorul minim "
        "impus, reducând astfel sensibilitatea. Există în selecție un compromis "
        "fundamental între sensibilitate și specificitate: îmbunătățirea uneia în "
        "condiții fixe tinde să o reducă pe cealaltă. Raportul de selecție mare sau "
        "proporția varianței explicate nu sunt indicatori direcți ai specificității."
    ),

    # 170 | Selecție #41 — sensibilitate crescută fără specificitate → risc FP
    (
        "Există un compromis clasic în teoria testării între sensibilitate și "
        "specificitate. Dacă mărești sensibilitatea unui test de screening — îl "
        "ajustezi să prindă mai mulți candidați buni — fără a ajusta pragul de "
        "decizie sau specificitatea, riscul de a accepta și candidați mai puțin "
        "potriviți crește. Aceasta se traduce printr-un număr mai mare de false "
        "pozitive: mai mulți candidați vor trece filtrul, inclusiv unii care nu "
        "vor performa bine la job. Acest compromis este esențial de înțeles în "
        "proiectarea procedurilor de screening cu volum mare de aplicanți, mai "
        "ales în situații în care costul angajărilor greșite este ridicat."
    ),

    # 171 | Selecție #42 — asociere corectă sensibilitate/specificitate
    (
        "Asocierile corecte dintre concepte și efectele lor asupra erorilor de "
        "selecție sunt clare și distincte. "
        "✅ Sensibilitatea — detectează candidații buni — reduce respingerile greșite, "
        "adică falsele negative. "
        "✅ Specificitatea — elimină candidații nepotriviți — reduce angajările greșite, "
        "adică falsele pozitive. "
        "❌ A crede că eliminarea nepotriviților reduce și respingerile greșite este "
        "o inversare incorectă a logicii. "
        "❌ A crede că detectarea celor buni reduce angajările greșite confundă "
        "sensibilitatea cu specificitatea. "
        "Înțelegerea acestor asocieri este esențială pentru evaluarea eficienței "
        "instrumentelor de selecție."
    ),

    # 172 | Selecție #43 — screening: caracteristici
    (
        "Selecția de tip screening urmărește eliminarea rapidă a candidaților care "
        "nu îndeplinesc criteriile minime dintr-un pool mare de aplicanți. "
        "✅ Scopul este reducerea rapidă și eficientă a numărului de candidați. "
        "✅ Procedurile sunt relativ ieftine și scurte: filtrarea CV-urilor pe "
        "criteriile obligatorii, teste scurte online cu barem automat. "
        "✅ Instrumentele tipice sunt CV-uri, filtre inițiale și teste scurte. "
        "❌ Un centru de evaluare cu simulări complexe ca prim pas obligatoriu nu "
        "este screening — el este specific etapei comprehensive, costisitoare și "
        "aprofundate, care se aplică finaliștilor, nu pool-ului mare inițial."
    ),

    # 173 | Selecție #44 — comprehensive: caracteristici
    (
        "Selecția comprehensivă (de înaltă fidelitate) se desfășoară, de obicei, "
        "după screening și vizează alegerea celui mai potrivit candidat dintr-un "
        "grup restrâns de finaliști. "
        "✅ Scopul este diferențierea finalistilor prin proceduri elaborate. "
        "✅ Procedurile sunt mai complexe, mai costisitoare și mai lungi: centre de "
        "evaluare cu exerciții simulate, probe de lucru extinse, interviuri structurate "
        "aprofundate. "
        "✅ Centrul de evaluare cu exerciții simulate este un instrument tipic al "
        "etapei comprehensive. "
        "❌ Un simplu filtru demografic nu este o metodă comprehensivă — nu are "
        "nici complexitatea, nici validitatea necesară pentru a diferenția finaliștii."
    ),

    # 174 | Selecție #45 — TF falsă: screening ≠ comprehensive (același scop/cost)
    (
        "Afirmația că screening-ul și selecția comprehensivă au același scop, "
        "aceeași complexitate și același cost este falsă. Cele două tipuri de "
        "selecție diferă fundamental: screening-ul urmărește eliminarea rapidă a "
        "candidaților nepotriviți dintr-un pool mare, folosind proceduri ieftine "
        "și rapide; selecția comprehensivă urmărește alegerea celui mai bun candidat "
        "dintre finaliști, folosind proceduri complexe, costisitoare și mai valide. "
        "Centrul de evaluare este tipic pentru etapa comprehensivă, nu pentru "
        "screening. A le trata ca pe același lucru ar ignora diferențele esențiale "
        "de scop, cost și validitate care justifică structurarea procesului în "
        "etape distincte."
    ),

    # 175 | Selecție #46 — filtru CV + test + assessment center = lanț screening+comprehensive
    (
        "Lanțul descris — filtru pe CV, test scurt pentru toți candidații, assessment "
        "center pentru finaliști — este un exemplu clasic al procesului de selecție "
        "în două etape: screening urmat de selecție comprehensivă. Filtrarea CV-ului "
        "și testul scurt reprezintă screeningul: proceduri rapide, ieftine, orientate "
        "spre eliminarea rapidă a candidaților sub pragul minim. Assessment center-ul "
        "cu exerciții simulate, la care ajung doar finaliștii trecuți de screening, "
        "reprezintă selecția comprehensivă: proceduri mai laborioase, mai costisitoare "
        "și cu validitate mai mare, care diferențiază candidații calificați rămași."
    ),

    # 176 | Selecție #47 — screening vs comprehensive: distincție
    (
        "Screening-ul și selecția comprehensivă servesc scopuri complementare, dar "
        "diferite. "
        "✅ Screening-ul reduce pool-ul inițial de candidați prin eliminarea celor "
        "care nu îndeplinesc cerințele minime. "
        "✅ Selecția comprehensivă diferențiază finaliștii prin proceduri mai elaborate "
        "și mai costisitoare, cu scopul de a alege cel mai potrivit candidat. "
        "❌ Selecția comprehensivă nu este mai puțin validă decât un CV — dimpotrivă, "
        "centrele de evaluare și simulările au, în general, o validitate predictivă "
        "mai mare decât simpla examinare a unui CV. "
        "❌ Screening-ul nu folosește centre de evaluare — acestea sunt instrumente "
        "ale fazei comprehensive."
    ),

    # 177 | Selecție #48 — de ce combini screening cu comprehensive
    (
        "Combinarea screening-ului cu etapele comprehensive este rațională din punct "
        "de vedere economic și metodologic. Screeningul gestionează eficient volumul "
        "mare de aplicații la cost redus — este imposibil practic și prohibitiv "
        "financiar să trimiți sute sau mii de candidați direct la un centru de evaluare. "
        "Odată redus pool-ul la un număr gestionabil de finaliști, etapa "
        "comprehensivă poate aplica instrumente cu validitate mai mare (probe de "
        "lucru, simulări, interviuri structurate detaliate) pentru decizia finală. "
        "Selecția comprehensivă nu înlocuiește nevoia de criteriu de performanță "
        "ulterioară — validitatea se verifică mereu prin corelarea cu criteriul, "
        "indiferent de metodă."
    ),

    # 178 | Selecție #49 — instrumente tipice screening
    (
        "Instrumentele tipice pentru faza de screening sunt cele aplicabile rapid "
        "și la cost redus pe un pool mare de candidați. "
        "✅ Filtrarea automată a CV-urilor pe cuvinte cheie sau pe criterii minimale "
        "îndeplinește aceste criterii. "
        "✅ Testele scurte online cu barem automat pot fi administrate simultan mii "
        "de candidați la cost redus. "
        "❌ Centrele de evaluare cu simulări complexe de o zi întreagă necesită timp, "
        "resurse umane calificate și infrastructură care fac aplicarea lor pe sute "
        "de candidați imposibilă practic. "
        "❌ Interviul de selecție structurat de 2–3 ore cu exerciții simulate este "
        "specific fazei comprehensive, nu screeningului."
    ),

    # 179 | Selecție #50 — assessment center = comprehensive
    (
        "Centrul de evaluare (assessment center) cu exerciții simulate — role-play, "
        "studii de caz, exerciții de grup, prezentări, basket-uri de documente — "
        "este, prin natura sa, un instrument de selecție comprehensivă de înaltă "
        "fidelitate. El presupune observarea comportamentului candidaților în situații "
        "care simulează cerințele reale ale rolului, de obicei timp de mai multe ore, "
        "și implică mai mulți evaluatori calificați. Costul și logistica unui "
        "assessment center îl fac inadecvat ca instrument de screening pe un pool "
        "mare — el este rezervat etapei finale de diferențiere a finaliștilor "
        "calificați. Nu este un simplu filtru rapid pe date biografice și nici un "
        "instrument de măsurare a ratei de bază din populație."
    ),

    # 180 | Selecție #51 — rata de bază (base rate)
    (
        "Rata de bază (base rate) în selecția personalului exprimă probabilitatea "
        "ca o persoană aleasă aleatoriu din pool-ul de candidați sau din populația "
        "relevantă să atingă standardele de performanță satisfăcătoare, fără nicio "
        "procedură sistematică de selecție. Este un reper pentru evaluarea câștigului "
        "adus de selecție: dacă rata de bază este deja ridicată (de exemplu, 90 la "
        "sută dintre candidați ar performa bine oricum), utilitatea marginală a "
        "selecției este redusă. Rata de bază este distinctă de raportul de selecție "
        "(candidați selectați raportat la total candidați) și de coeficientul de "
        "corelație al predictorilor."
    ),

    # 181 | Selecție #52 — SR mic = selecție strictă
    (
        "Raportul de selecție (SR) se calculează ca numărul de candidați angajați "
        "împărțit la numărul total de candidați care au aplicat. Un SR mic, de "
        "exemplu 5 la sută, înseamnă că din 100 de aplicanți sunt angajate numai "
        "5 persoane — o selecție foarte strictă. Această valoare scăzută crește "
        "utilitatea selecției: organizația alege dintr-un pool mare și poate selecta "
        "candidații cu cele mai bune scoruri. Un SR mare, de exemplu 90 la sută, "
        "înseamnă că aproape toți aplicanții sunt angajați, reducând semnificativ "
        "efectul discriminator al procesului de selecție. SR mic nu înseamnă "
        "validitate negativă sau rată de bază egală cu 1."
    ),

    # 182 | Selecție #53 — Taylor-Russell: utilitate crește cu validitate mare și SR mic
    (
        "Modelul Taylor–Russell descrie utilitatea procesului de selecție ca funcție "
        "de trei variabile: validitatea predictorilor, raportul de selecție (SR) și "
        "rata de bază. "
        "✅ Utilitatea crește când validitatea predictorilor este mai mare — "
        "instrumentele prezic mai bine performanța. "
        "✅ Utilitatea crește când raportul de selecție este mai mic — organizația "
        "poate fi mai selectivă alegând dintr-un pool mai mare. "
        "❌ Rata de bază intră în calculul Taylor–Russell, nu este ignorată: la "
        "valori extreme ale ratei de bază (foarte ridicate sau foarte scăzute), "
        "câștigul marginal al selecției este mai mic. "
        "❌ Scăderea validității sau creșterea SR reduc utilitatea, nu o cresc."
    ),

    # 183 | Selecție #54 — TF falsă: utilitate maximă la validitate scăzută + SR mare
    (
        "Această afirmație este falsă. Conform modelului Taylor–Russell, utilitatea "
        "procesului de selecție este maximă atunci când validitatea predictorilor "
        "este ridicată și raportul de selecție (SR) este scăzut, nu invers. O "
        "validitate scăzută înseamnă că instrumentele prezic slab performanța "
        "viitoare, reducând câștigul de calitate al selecției. Un SR mare înseamnă "
        "că aproape toți candidații sunt angajați, eliminând practic efectul "
        "discriminator al selecției. Combinarea validității scăzute cu SR mare "
        "este cel mai defavorabil scenariu de utilitate — nu cel mai favorabil."
    ),

    # 184 | Selecție #55 — SR = 10/500 = 0,02
    (
        "Raportul de selecție (SR) se calculează ca numărul de candidați angajați "
        "împărțit la numărul total de candidați care au aplicat. Dacă o companie "
        "primește 500 de aplicații și angajează 10 persoane, SR = 10 din 500 = 0,02, "
        "adică 2 la sută. Aceasta indică o selecție foarte strictă: compania alege "
        "numai 2 la sută dintre toți cei care au aplicat. Opțiunea 500 împărțit la "
        "10 = 50 inversează numărătorul și numitorul față de definiția standard. "
        "Opțiunile 10 împărțit la 490 sau 1 minus 10 din 500 = 0,98 nu corespund "
        "definiției — formula corectă este întotdeauna selectați împărțit la total "
        "aplicanți."
    ),

    # 185 | Selecție #56 — utilitate selecție: afirmații corecte
    (
        "Componentele utilității selecției pot fi sintetizate astfel. "
        "✅ Rata de bază descrie situația ante-selecție: câți candidați ar performa "
        "satisfăcător fără nicio procedură sistematică. "
        "✅ Raportul de selecție mic înseamnă că organizația alege puțini candidați "
        "dintr-un pool mare, maximizând oportunitatea de a selecta pe cei cu "
        "scoruri ridicate. "
        "✅ Validitatea mai mare a predictorilor permite o separare mai bună a "
        "viitorilor performeri de restul candidaților. "
        "❌ Utilitatea selecției nu este independentă de validitate — fără validitate "
        "nu există câștig real față de selecția aleatorie, indiferent de numărul "
        "de aplicații."
    ),

    # 186 | Selecție #57 — firma A (r=0,50) vs firma B (r=0,15)
    (
        "Atunci când SR este identic pentru două organizații, diferența de validitate "
        "a predictorilor devine factorul determinant al utilității selecției. Firma A, "
        "cu r = 0,50, poate separa mai precis candidații performanți de cei mai puțin "
        "performanți — câștigul în calitatea angajărilor este mai mare. Firma B, cu "
        "r = 0,15, face o predicție mult mai slabă, similară aproape cu o selecție "
        "aleatorie. "
        "✅ Firma A are potențial de câștig mai mare din selecție. "
        "✅ Validitatea influențează direct cât de bine selecția îmbunătățește calitatea "
        "angajărilor. "
        "❌ Firma B nu obține aceeași precizie — o validitate mult mai scăzută "
        "înseamnă predicție mult mai slabă. "
        "❌ SR singur nu determină totul când validitățile diferă semnificativ."
    ),

    # 187 | Selecție #58 — SR mare limitează utilitatea
    (
        "Atunci când raportul de selecție este foarte mare — de exemplu, 90 la sută "
        "sau mai mult — aproape toți candidații sunt angajați, indiferent de scorurile "
        "obținute la instrumentele de selecție. În această situație, diferențierea "
        "dintre candidați pe baza predictorii nu mai are efect practic: și candidații "
        "cu scoruri mici sunt angajați. "
        "✅ Aproape nu se face o selecție reală — rămân în proces și candidații slabi. "
        "✅ Diferențierea dintre aplicanți nu mai contează practic din punct de vedere "
        "al deciziei. "
        "❌ Rata de bază nu devine automat zero — ea rămâne independentă de SR, "
        "reflectând probabilitatea de succes în absența selecției sistematice."
    ),

    # 188 | Selecție #59 — rezumat logică selecție
    (
        "Logica selecției personalului poate fi rezumată prin câteva principii esențiale. "
        "✅ Predictori validați empiric — aptitudinea mentală generală (GMA), "
        "conștiinciozitatea, testele de integritate și probele de lucru — sunt evaluați "
        "prin coeficienți r (validitate simplă), R (validitate multiplă a combinației) "
        "și R pătrat (proporția varianței explicate din criteriu). "
        "✅ Screening-ul reduce pool-ul inițial de candidați la cost redus, iar selecția "
        "comprehensivă diferențiază finaliștii prin proceduri mai elaborate. "
        "✅ Utilitatea economică crește cu validitate mai mare și cu raport de selecție "
        "mai mic. "
        "❌ Selecția nu măsoară direct performanța viitoare — o estimează cu o marjă "
        "de eroare inevitabilă, ceea ce presupune că predictorii au mereu o parte "
        "din varianța criteriului neexplicată."
    ),

    # 189 | Selecție #60 — crește R și scade SR → utilitate crescută
    (
        "Conform principiilor Taylor–Russell și ale utilității selecției, combinația "
        "dintre o baterie de predictori cu validitate mai mare și un raport de selecție "
        "mai mic tinde să crească utilitatea economică a procesului de selecție. "
        "Creșterea R de la 0,35 la 0,50 înseamnă că instrumentele prezic mai bine "
        "performanța viitoare — ierarhia scorurilor la selecție corespunde mai precis "
        "ierarhiei performanței reale. Scăderea SR de la 20 la sută la 8 la sută "
        "înseamnă că organizația devine mai selectivă: alege dintr-un pool relativ "
        "mai mare, putând opta pentru candidații cu cele mai ridicate scoruri. Cele "
        "două efecte se sumează, crescând utilitatea combinată a procesului."
    ),

    # 190 | Selecție #61 — TF falsă: screening nu alege cel mai bun din finaliști
    (
        "Afirmația este falsă. Scopul principal al screening-ului nu este să identifice "
        "cel mai bun candidat dintre finaliști — aceasta este sarcina selecției "
        "comprehensive. Screening-ul urmărește eliminarea rapidă a candidaților "
        "nepotriviți dintr-un pool mare, la cost redus, pentru a reduce numărul "
        "celor care ajung la etapele ulterioare. Simulările complexe de o zi întreagă "
        "sunt instrumente specifice fazei comprehensive, nu screeningului. "
        "Confundarea scopurilor celor două etape duce la procese de selecție "
        "ineficiente — fie prea costisitoare pentru volumul inițial de candidați, "
        "fie insuficient de riguroase pentru decizia finală."
    ),

    # 191 | Selecție #62 — 900 aplicații + CV + test scurt = screening
    (
        "Atunci când o organizație gestionează un pool mare de aplicații și aplică "
        "filtre rapide, ieftine și standardizate — eliminarea CV-urilor care nu "
        "îndeplinesc cerințele minime de studii și un test scurt online — aceasta "
        "realizează un screening. Scopul screeningului este să reducă rapid și eficient "
        "numărul de candidați la un subset mai mic care va continua în etapele "
        "ulterioare. Aceasta nu este selecție comprehensivă: nu se diferențiază "
        "finaliștii prin proceduri elaborate, ci se elimină nepotriviții din masa "
        "mare de aplicanți. Viteza, costul redus și caracterul eliminatoriu sunt "
        "trăsăturile definitorii ale acestei etape."
    ),

    # 192 | Selecție #63 — comprehensive: afirmații corecte
    (
        "Selecția comprehensivă are mai multe caracteristici distinctive. "
        "✅ Are loc de regulă după screening, pe un număr redus de finaliști calificați. "
        "✅ Folosește proceduri mai complexe și mai costisitoare decât simpla filtrare "
        "a CV-urilor. "
        "✅ Poate include centru de evaluare (assessment center) sau simulări extinse "
        "ale rolului — instrumente cu validitate predictivă ridicată. "
        "❌ Eliminarea miilor de candidați în câteva minute, fără observare detaliată, "
        "este caracteristică screeningului, nu selecției comprehensive. "
        "Investiția de timp și resurse în observarea comportamentului finaliștilor "
        "în condiții similare celor reale este esența selecției de înaltă fidelitate."
    ),

    # 193 | Selecție #64 — 35 candidați + simulare 3h + interviu = comprehensive
    (
        "Etapa în care cei 35 de candidați rămași după filtrarea CV-ului susțin o "
        "simulare de trei ore a sarcinilor din job, urmată de un interviu structurat "
        "cu comisie, corespunde selecției comprehensive de înaltă fidelitate. Aceasta "
        "diferențiază finaliștii prin proceduri elaborate, observând comportamentul "
        "în condiții care simulează cerințele reale ale rolului. Nu este un simplu "
        "screening rapid, deoarece implică investiție de timp, resurse umane și "
        "infrastructură. Nu înlocuiește nici criteriul de performanță post-angajare "
        "— validitatea se verifică în continuare prin corelarea scorurilor din "
        "selecție cu performanța reală ulterioară."
    ),

    # 194 | Selecție #65 — de ce nu toți 500 la assessment center
    (
        "Trimiterea tuturor celor 500 de aplicanți direct la un centru de evaluare "
        "cu simulări ar fi prohibitivă din punct de vedere al costului și al timpului. "
        "✅ Costul și timpul ar fi prohibitivi pentru evaluarea întregului pool. "
        "✅ Screening-ul reduce mai întâi numărul de candidați evaluați în profunzime, "
        "făcând procesul economic viabil. "
        "✅ Screening-ul gestionează volumul mare; comprehensive rămâne pentru decizia "
        "fină între puțini finaliști. "
        "❌ Centrul de evaluare nu are validitate zero față de alte instrumente — "
        "dimpotrivă, are una dintre cele mai ridicate validități predictive, tocmai "
        "de aceea este rezervat etapei finale unde investiția este justificată "
        "de numărul mic de candidați."
    ),

    # 195 | Selecție #66 — formulare diferența de scop
    (
        "Diferența de scop dintre screening și selecția comprehensivă poate fi "
        "exprimată cel mai clar prin două întrebări diferite la care răspund fiecare. "
        "Screeningul răspunde la: Cine nu ar trebui să continue în procesul de "
        "selecție? — eliminând din pool-ul mare candidații care nu îndeplinesc "
        "criteriile minime. Selecția comprehensivă răspunde la: Care este cel mai "
        "potrivit candidat dintre cei care au trecut filtrele? — diferențiind "
        "finaliștii prin proceduri elaborate și cu validitate mai mare. Inversarea "
        "logicii — screening care alege cel mai bun, comprehensive care elimină în "
        "masă — nu corespunde practicii și teoriei din domeniu."
    ),

    # 196 | Selecție #67 — instrumente screening vs comprehensive: toate
    (
        "Instrumentele de selecție pot fi clasificate în funcție de etapa căreia îi "
        "sunt destinate, pe baza complexității, costului și numărului de candidați "
        "evaluați. "
        "✅ Filtrul automat pe cuvinte cheie în CV este instrument tipic de screening "
        "— rapid, ieftin, aplicabil simultan multor candidați. "
        "✅ Testul scurt online cu barem este instrument tipic de screening. "
        "✅ Simularea de o zi întreagă a rolului este instrument tipic de selecție "
        "comprehensivă — necesită timp, resurse calificate și infrastructură. "
        "✅ Interviul de selecție structurat de 2–3 ore cu exerciții simulate este "
        "instrument al fazei comprehensive. "
        "Clasificarea corectă permite proiectarea unui proces eficient și "
        "proporțional cu resursele disponibile."
    ),

    # 197 | Selecție #68 — interviu 15 min (screening) + probă lucru 2h (comprehensive)
    (
        "Procesul cu două etape poate fi clasificat cu precizie. Interviul telefonic "
        "de 15 minute aplicat tuturor candidaților este instrument de screening: "
        "rapid, ieftin, poate elimina candidații care nu îndeplinesc criteriile de "
        "bază — disponibilitate, motivație minimă sau prezentare incorentă. "
        "✅ Interviu telefonic de 15 minute pentru toți candidații — screening. "
        "✅ Probă de lucru de 2 ore doar pentru cei 12 rămași — comprehensive, "
        "cu validitate predictivă ridicată. "
        "❌ Interviul telefonic nu este evaluare profundă a competențelor — este prea "
        "scurt și nediferențiator pentru acel rol. "
        "❌ Proba de lucru nu este filtru rapid pe pool mare — necesită resurse prea "
        "mari pentru a fi aplicată tuturor candidaților."
    ),

    # 198 | Selecție #69 — TF falsă: comprehensive nu e mai ieftin
    (
        "Afirmația este falsă. Procedurile comprehensive sunt, în mod tipic, mai "
        "costisitoare și mai consumatoare de timp decât screening-ul, nu mai ieftine "
        "și mai rapide. Această diferență de cost și durată este tocmai motivul pentru "
        "care organizațiile folosesc mai întâi screening-ul: să reducă pool-ul înainte "
        "de a investi în evaluarea profundă a finaliștilor. Aplicarea unor proceduri "
        "comprehensive simultan la sute de candidați ar fi prohibitivă financiar și "
        "logistic. Afirmația că sunt mai ieftine pentru că se aplică la mai mulți "
        "candidați simultan inversează realitatea — numărul mic de candidați evaluați "
        "complet este tocmai condiția care face procedura comprehensivă fezabilă."
    ),

    # 199 | Selecție #70 — bancă: etapele corecte
    (
        "Procesul de selecție al băncii ilustrează combinarea clasică dintre screening "
        "și selecție comprehensivă. "
        "✅ Filtrul pe criteriul studiilor obligatorii și testul scurt aplicate pe "
        "pool-ul mare de 400 de aplicanți constituie etapa de screening: rapide, "
        "ieftine, cu scop eliminatoriu. "
        "✅ Assessment center-ul cu role-play aplicat celor 40 de finaliști constituie "
        "etapa comprehensivă: complexă, costisitoare, cu scop de diferențiere fină "
        "între candidații calificați. "
        "❌ Testul scurt aplicat pe 400 de persoane nu este evaluare profundă — "
        "este screening prin definiție. "
        "❌ Role-play-ul aplicat finaliștilor nu este filtru rapid și ieftin — este "
        "procedură comprehensivă costisitoare."
    ),

    # 200 | Selecție #71 — sensibilitate ridicată → reduce false negative
    (
        "Sensibilitatea unei proceduri de selecție descrie capacitatea ei de a detecta "
        "cu acuratețe candidații care ar performa bine la job dacă ar fi angajați. "
        "Atunci când sensibilitatea este ridicată, procedura identifică corect o "
        "proporție mare a candidaților cu adevărat potriviți, reducând astfel numărul "
        "de false negative — situații în care un candidat bun este respins eronat "
        "pentru că instrumentul nu l-a recunoscut ca potrivit. Sensibilitatea nu "
        "se referă la eliminarea candidaților slabi (aceea este specificitatea) și "
        "nu reduce direct raportul de selecție sau validitatea incrementală a altor "
        "instrumente."
    ),

    # 201 | Selecție #72 — specificitate: afirmații corecte
    (
        "Specificitatea în selecția personalului are mai multe caracteristici. "
        "✅ Vizează eliminarea candidaților nepotriviți din pool-ul de selecție. "
        "✅ O specificitate ridicată conduce la mai puține false pozitive, adică mai "
        "puține angajări greșite ale candidaților care nu vor performa corespunzător. "
        "✅ Se leagă direct de respingerea celor care probabil nu ar performa — este "
        "măsura capacității instrumentului de a exclude corect cazurile negative. "
        "❌ O specificitate ridicată nu garantează automat sensibilitate maximă — "
        "între cele două există un compromis dependent de pragul de decizie ales: "
        "creșterea specificității fără ajustarea sensibilității poate crește "
        "falsele negative."
    ),

    # 202 | Selecție #73 — candidat respins de test strict = false negative
    (
        "Când un candidat competent este respins de un test de selecție care a "
        "aplicat un prag prea strict, aceasta constituie un fals negativ: candidatul "
        "era, în realitate, potrivit pentru rol, dar testul l-a clasificat incorect "
        "ca nepotrivit. Falsul negativ este o eroare de omisiune: s-a pierdut un "
        "candidat care ar fi putut performa bine. Este costisitor pentru organizație "
        "— pierde un angajat valoros — și costisitor pentru candidat, care nu obține "
        "postul pentru care era calificat. Reducerea falselor negative este obiectivul "
        "sensibilității ridicate, nu al specificității sau al validității multiple."
    ),

    # 203 | Selecție #74 — crescut specificitate → mai puțin FP, risc FN mai mare
    (
        "Atunci când mărești specificitatea unui test de screening — de exemplu, "
        "prin ridicarea pragului de acceptare — testul devine mai riguros în eliminarea "
        "candidaților nepotriviți: vor trece mai puțini candidați slabi, reducând "
        "falsele pozitive. Totuși, în absența ajustării sensibilității, un prag mai "
        "ridicat respinge și mai mulți candidați buni care nu ating noul standard, "
        "crescând riscul de false negative. Ambele tipuri de erori nu dispar simultan "
        "și automat — ele se află într-un raport de echilibru care depinde de "
        "distribuția scorurilor și de pragul ales. Raportul de selecție nu atinge "
        "automat valoarea 1 prin creșterea specificității."
    ),

    # 204 | Selecție #75 — TF: sensibilitate reduce false negative (ADEVĂRAT)
    (
        "Această afirmație este adevărată. Sensibilitatea ridicată a unui instrument "
        "de selecție reduce în principal rata falselor negative — adică reduce "
        "probabilitatea de a respinge candidați care ar fi performat bine la job. "
        "Sensibilitatea descrie capacitatea instrumentului de a detecta cu acuratețe "
        "cazurile pozitive (candidații potriviți), minimizând eroarea de omisiune. "
        "Specificitatea, în schimb, reduce falsele pozitive — angajările greșite. "
        "Înțelegerea corectă a celor doi termeni și a erorilor pe care le controlează "
        "este esențială în proiectarea procedurii de selecție și în evaluarea "
        "eficienței fiecărui instrument."
    ),

    # ── PERFORMANTA_MUNCII itemi 1–29 (indici 205–233) ──────────────────────

    # 205 | Performanță #1 — TF: performanța include comportamente + rezultate (ADEVĂRAT)
    (
        "Această afirmație este adevărată. În psihologia muncii contemporană, "
        "performanța la job este definită ca un construct multidimensional care "
        "cuprinde atât comportamentele prestate — modul în care se efectuează munca "
        "pe parcursul activității — cât și rezultatele obținute — ceea ce se produce "
        "efectiv și tangibil. Reducerea performanței exclusiv la cifrele de "
        "productivitate ignoră dimensiuni importante: cum a comunicat angajatul cu "
        "clienții, dacă a respectat procedurile de siguranță, cum a colaborat cu "
        "echipa. Această definiție largă este esențială pentru o evaluare echitabilă "
        "și comprehensivă a angajaților."
    ),

    # 206 | Performanță #2 — performanța = comportamente + rezultate
    (
        "Definiția cea mai precisă a performanței la muncă în psihologia organizațională "
        "combină două componente: comportamentele — adică modul în care angajatul "
        "acționează și lucrează pe parcursul activității — și rezultatele — adică "
        "produsele sau ieșirile tangibile ale muncii. Reducerea performanței exclusiv "
        "la rezultatele atinse omite informații importante despre procesul de muncă: "
        "un angajat poate atinge o cotă prin mijloace problematice sau nesustenabile. "
        "Invers, un angajat cu comportamente exemplare dar rezultate sub așteptări "
        "poate fi limitat de factori externi necontrolabili, nu de calitatea muncii "
        "sale. Perspectiva integrată oferă o evaluare mai corectă și mai acționabilă."
    ),

    # 207 | Performanță #3 — vânzător: cota + comportamente problematice
    (
        "Evaluarea corectă a performanței unui vânzător care atinge cota lunară, dar "
        "ignoră procedurile de raportare și refuză să ajute colegii noi, trebuie să "
        "ia în calcul ambele componente ale definiției performanței. "
        "✅ Rezultatul cantitativ — atingerea cotei de vânzări — este o dimensiune "
        "reală a performanței la sarcină care nu trebuie ignorată. "
        "✅ Comportamentele de nerespectare a procedurilor și refuzul de a colabora "
        "reprezintă deficite de performanță contextuală și, posibil, comportamente "
        "cu impact negativ asupra echipei. "
        "❌ Evaluarea limitată la contractele semnate, fără a lua în considerare "
        "comportamentele, produce o imagine incompletă și poțial distorsionată a "
        "contribuției reale a angajatului."
    ),

    # 208 | Performanță #4 — de ce rezultatele singure nu sunt suficiente
    (
        "Măsurarea performanței exclusiv prin rezultatele finale are mai multe "
        "limitări importante. "
        "✅ Același rezultat numeric poate proveni din comportamente foarte diferite: "
        "un angajat poate atinge cota prin scurtături sau practici discutabile, "
        "generând probleme pe termen lung neapărute imediat în cifre. "
        "✅ Comportamentele de colaborare, respectarea procedurilor și mentorarea "
        "colegilor nu sunt surprinse de rezultatele individuale, deși contribuie "
        "esențial la funcționarea echipei. "
        "✅ Factori externi — piața, sezonalitate, calitatea echipamentului — pot "
        "influența rezultatele independent de calitatea muncii individuale. "
        "❌ Rezultatele singure nu captează automat și comportamentele de cetățenie "
        "organizațională — acestea necesită instrumente specifice."
    ),

    # 209 | Performanță #5 — exemple comportament vs rezultat
    (
        "Performanța la muncă include atât componente comportamentale, cât și "
        "componente de rezultat, iar distingerea lor este importantă pentru o "
        "evaluare completă. "
        "✅ Respectarea procedurilor de siguranță este o componentă comportamentală "
        "— descrie cum lucrează angajatul. "
        "✅ Numărul de erori raportate la sfârșitul lunii este o componentă de "
        "rezultat — descrie o ieșire măsurabilă. "
        "✅ Modul de comunicare cu clienții este o componentă comportamentală. "
        "✅ Cota de vânzări atinsă este o componentă de rezultat. "
        "Ambele tipuri sunt necesare pentru o evaluare completă: comportamentele "
        "explică procesul, rezultatele confirmă ieșirile."
    ),

    # 210 | Performanță #6 — TF falsă: performanța nu e exclusiv cantitativă
    (
        "Afirmația este falsă. Performanța la muncă nu se definește exclusiv prin "
        "rezultatele cantitative măsurate obiectiv. Psihologia muncii contemporană "
        "recunoaște că performanța este un construct multidimensional care include "
        "atât rezultatele tangibile, cât și comportamentele prestate pe parcursul "
        "activității. Comportamentele de colaborare, adaptabilitate, respectarea "
        "standardelor de calitate și sprijinirea colegilor sunt componente ale "
        "performanței care nu apar în indicatorii cantitativ obiectivi, dar care "
        "influențează semnificativ succesul organizațional pe termen lung."
    ),

    # 211 | Performanță #7 — criteriu teoretic vs criteriu efectiv
    (
        "În evaluarea performanței, se face o distincție importantă între criteriul "
        "teoretic și criteriul efectiv. Criteriul teoretic — numit și criteriu ideal "
        "— descrie tot ceea ce ar trebui măsurat pentru a evalua performanța completă "
        "a unui angajat în rol, incluzând toate dimensiunile relevante ale jobului. "
        "Criteriul efectiv descrie ceea ce se măsoară în practică cu instrumentele "
        "disponibile — de exemplu, un rating de la supervizor sau numărul de unități "
        "produse. Această distincție nu se referă la scorul la selecție față de "
        "performanța ulterioară, ci la compararea idealului evaluativ cu realitatea "
        "instrumentelor de măsurare disponibile."
    ),

    # 212 | Performanță #8 — relevanța criteriului
    (
        "Relevanța criteriului (criterion relevance) reprezintă suprapunerea dintre "
        "criteriul efectiv (ce măsurăm în practică) și criteriul teoretic (ce ar "
        "trebui să măsurăm ideal). Porțiunea de suprapunere descrie în ce măsură "
        "instrumentul de evaluare capturează cu adevărat performanța relevantă a "
        "angajatului. Cu cât relevanța este mai mare, cu atât criteriul efectiv "
        "reflectă mai fidel constructul de performanță vizat. Deficiența este ce "
        "lipsește din criteriul efectiv față de cel teoretic, iar contaminarea este "
        "ce intră în criteriul efectiv fără să facă parte din constructul teoretic "
        "de performanță."
    ),

    # 213 | Performanță #9 — deficiența criteriului
    (
        "Deficiența criteriului apare atunci când criteriul efectiv folosit pentru "
        "evaluarea performanței nu acoperă toate dimensiunile importante ale "
        "constructului teoretic de performanță. "
        "✅ Lipsesc din măsurare aspecte relevante ale jobului pe care instrumentul "
        "de evaluare ales nu le captează. "
        "✅ Criteriul efectiv nu acoperă toate aspectele relevante ale constructului "
        "teoretic — există o lipsă, nu un exces. "
        "❌ Deficiența nu înseamnă că intră ceva nerelevant în scor — aceea este "
        "contaminarea. "
        "❌ Deficiența nu înseamnă că criteriul teoretic și cel efectiv coincid "
        "perfect — dimpotrivă, ele nu se suprapun complet. "
        "De exemplu, dacă evaluarea unui asistent medical ignoră complet calitatea "
        "comunicării cu pacienții, criteriul suferă de deficiență."
    ),

    # 214 | Performanță #10 — contaminarea criteriului
    (
        "Contaminarea criteriului apare atunci când scorul sau ratingul de performanță "
        "al unui angajat este influențat de factori care nu au legătură cu performanța "
        "reală la job. "
        "✅ Intrarea unor factori nerelevanti pentru job în scorul de performanță "
        "constituie contaminare. "
        "✅ Favoritismul supervizorului — evaluări mai bune pentru angajații simpatici "
        "sau pentru cei cu care are o relație personală — este o formă clasică de "
        "contaminare. "
        "❌ Contaminarea nu înseamnă că lipsește o dimensiune din evaluare — aceea "
        "este deficiența. "
        "❌ Un criteriu care măsoară strict sarcinile din fișa postului fără factori "
        "nerelevanți nu este contaminat — este un criteriu cu relevanță ridicată."
    ),

    # 215 | Performanță #11 — evaluator subiectiv (simpatie) = contaminare
    (
        "Situația în care un evaluator acordă note mai mari unui subordonat din motive "
        "de simpatie personală, ignorând că rezultatele obiective sunt medii, ilustrează "
        "în mod clar contaminarea criteriului. Simpatia față de o persoană este un "
        "factor exterior performanței reale la job și nu ar trebui să influențeze "
        "ratingul. Atunci când acest factor nerelevant se strecoară în scorul de "
        "evaluare, criteriul efectiv devine contaminat — el nu mai reflectă fidel "
        "performanța, ci o combinație de performanță reală și bias al evaluatorului. "
        "Deficiența criteriului ar apărea, dimpotrivă, dacă evaluarea ar omite "
        "dimensiuni importante ale rolului, nu dacă ar adăuga factori nerelevanți."
    ),

    # 216 | Performanță #12 — ignorarea colaborării = deficiența
    (
        "Evaluarea anuală care măsoară exclusiv volumul de output și ignoră în "
        "totalitate comportamentele de colaborare, respectarea procedurilor și alți "
        "indicatori comportamentali suferă de deficiență a criteriului. Criteriul "
        "efectiv (output numeric) nu acoperă întreg constructul teoretic al "
        "performanței în rol, care include și comportamentul colaborativ și respectarea "
        "standardelor de calitate. Deficiența înseamnă că lipsesc din măsurare "
        "dimensiuni esențiale. Nu este contaminare — nu intră ceva nerelevant în "
        "scor. Nu este nici relevanță ridicată — criteriul efectiv nu acoperă "
        "constructul teoretic în totalitate."
    ),

    # 217 | Performanță #13 — relevanță, deficiență, contaminare: perechi
    (
        "Triada conceptuală din evaluarea criteriului se poate descrie astfel. "
        "✅ Relevanța — porțiunea din criteriul efectiv care corespunde cu adevărat "
        "constructului teoretic: ce măsurăm este relevant și util. "
        "✅ Deficiența — porțiunea din criteriul teoretic care lipsește din criteriul "
        "efectiv: există aspecte importante ale performanței pe care nu le surprindem. "
        "✅ Contaminarea — porțiunea din criteriul efectiv care nu face parte din "
        "criteriul teoretic: ceva nerelevant a intrat în evaluare și distorsionează "
        "scorul. "
        "❌ Afirmația că criteriul efectiv este mai scurt decât cel teoretic nu descrie "
        "corect deficiența — deficiența înseamnă că lipsesc componente esențiale, "
        "nu doar că volumul documentului este mai mic."
    ),

    # 218 | Performanță #14 — relevanță vs contaminare (falsă afirmație)
    (
        "Afirmația că relevanța și contaminarea sunt același lucru, indicând același "
        "tip de problemă, este falsă. Cele două sunt concepte distincte și cu direcții "
        "opuse. Relevanța reprezintă calitatea pozitivă a criteriului efectiv: "
        "porțiunea care se suprapune corect cu criteriul teoretic și măsoară ce "
        "trebuie măsurat — este de dorit să fie cât mai mare. Contaminarea reprezintă "
        "o problemă: prezența unor factori nerelevanți în scorul de evaluare care "
        "îl distorsionează — este de dorit să fie cât mai mică. O evaluare cu "
        "relevanță ridicată este bună; una cu contaminare ridicată are o problemă "
        "de validitate a criteriului."
    ),

    # 219 | Performanță #15 — task performance: definiție
    (
        "Performanța la sarcină (task performance), în modelul elaborat de Borman și "
        "Motowidlo, se referă la activitățile care constituie nucleul tehnic al "
        "rolului — sarcinile descrise în fișa postului, legate direct de obiectivele "
        "formale ale funcției. Un contabil care întocmește bilanțuri, un programator "
        "care scrie cod sau un operator care produce conform standardelor realizează "
        "task performance. Aceste comportamente sunt esențiale pentru transformarea "
        "materiilor prime sau a informațiilor în bunuri și servicii și contribuie "
        "direct la misiunea organizației. Comportamentele de sprijin voluntar al "
        "colegilor sau de participare la inițiative organizaționale sunt parte din "
        "performanța contextuală, nu din task performance."
    ),

    # 220 | Performanță #16 — contextual performance: definiție
    (
        "Performanța contextuală (contextual performance), în modelul Borman și "
        "Motowidlo, cuprinde comportamentele care susțin mediul organizațional, "
        "social și psihologic în care se desfășoară task performance. "
        "✅ Comportamentele susțin mediul de lucru și organizația, dincolo de "
        "sarcinile tehnice. "
        "✅ Acțiunile depășesc cerințele formale minime ale rolului — sunt voluntare, "
        "nu obligatorii prin contract. "
        "✅ Comportamentele voluntare pozitive care ajută echipa sau firma sunt tipice "
        "performanței contextuale. "
        "❌ Activitățile nucleu strict din descrierea postului, măsurate pe output, "
        "sunt task performance, nu contextual performance. "
        "Comportamentele de cetățenie organizațională (OCB) reprezintă un subset "
        "al performanței contextuale."
    ),

    # 221 | Performanță #17 — ITEM 9722: exemple task vs contextual
    (
        "Modelul Borman și Motowidlo distinge performanța în muncă în două categorii "
        "fundamentale pe baza naturii comportamentelor implicate. "
        "Performanța la sarcină (task performance) cuprinde comportamentele direct "
        "legate de îndeplinirea cerințelor formale ale rolului: realizarea activităților "
        "nucleu din fișa postului, atingerea standardelor de productivitate impuse "
        "și respectarea termenelor pentru livrabilele principale. Aceste activități "
        "sunt obligatorii, prevăzute în fișa postului și legate direct de obiectivele "
        "formale ale funcției. "
        "Performanța contextuală cuprinde comportamentele care susțin mediul "
        "organizațional și social, fără a fi strict obligatorii: ajutarea voluntară "
        "a unui nou coleg să învețe procedura este un comportament de sprijin social "
        "care depășește cerințele formale; acceptarea sarcinilor neplăcute fără "
        "plângeri excesive reflectă toleranța față de inconveniențe — o formă de "
        "sportsmanship în sens OCB. "
        "Clasificând fiecare exemplu: atingerea standardelor de productivitate din "
        "fișa postului este task performance; ajutarea voluntară a noului coleg "
        "este contextual performance; respectarea termenelor pentru livrabilele "
        "principale este task performance; acceptarea sarcinilor neplăcute fără "
        "plângeri excesive este contextual performance."
    ),

    # 222 | Performanță #18 — analist: task bun, contextual redus
    (
        "Situația analistului care finalizează la timp rapoartele obligatorii, dar "
        "refuză să participe la proiecte transversale care nu îi sunt cerute explicit, "
        "ilustrează o disociere între performanța la sarcină și cea contextuală. "
        "✅ Livrarea la termen a rapoartelor obligatorii reprezintă o componentă a "
        "task performance — aceste sarcini fac parte din cerințele formale ale rolului. "
        "✅ Refuzul de a participa la proiecte transversale neobligatorii sugerează "
        "o performanță contextuală posibil redusă — angajatul nu depășește minimul "
        "formal pentru a contribui la efortul organizațional colectiv. "
        "❌ Refuzul sarcinilor neobligatorii nu este automat un comportament "
        "contraproductiv (CWB) — absența contribuției suplimentare nu echivalează "
        "cu dăunarea activă a organizației."
    ),

    # 223 | Performanță #19 — distincții task vs contextual
    (
        "Performanța la sarcină și performanța contextuală sunt distincte prin natura "
        "și sursa comportamentelor implicate. "
        "✅ Task performance înseamnă activitățile esențiale și formale ale rolului, "
        "cerute explicit în fișa postului, legate direct de obiectivele organizației. "
        "✅ Contextual performance poate include acțiuni care nu sunt obligatorii în "
        "fișa postului — comportamente voluntare de susținere a mediului de lucru. "
        "✅ Task performance se leagă de obiectivele formale ale jobului, nu de "
        "contribuțiile suplimentare. "
        "❌ Task și contextual nu sunt sinonime în modelul Borman–Motowidlo — fiecare "
        "acoperă o dimensiune distinctă a contribuției angajatului, cu precursori "
        "și consecințe parțial diferite."
    ),

    # 224 | Performanță #20 — OCB ≠ contextual performance (identice = fals)
    (
        "Afirmația că OCB și performanța contextuală sunt exact același construct, "
        "fără nicio diferență, este falsă. Comportamentele de cetățenie organizațională "
        "(OCB) reprezintă un subset al performanței contextuale — adică OCB este "
        "inclus în performanța contextuală, dar nu o epuizează. Performanța "
        "contextuală este un concept mai larg care poate cuprinde și alte tipuri "
        "de comportamente pozitive care nu se încadrează strict în definițiile "
        "clasice ale OCB (altruism, curtenie, sportsmanship, virtute civică, "
        "conștiinciozitate organizațională Organ). Ambele vizează comportamente "
        "voluntare care susțin organizația, dar performanța contextuală are o "
        "sferă mai largă de acoperire conceptuală."
    ),

    # 225 | Performanță #21 — evaluare doar contextuală = deficiență față de task
    (
        "Atunci când un superior evaluează angajații exclusiv pe baza contribuțiilor "
        "voluntare la organizație — cât de mult ajută în plus, cât de activi sunt "
        "la inițiative — și ignoră complet livrarea sarcinilor principale, evaluarea "
        "suferă de deficiență a criteriului față de performanța la sarcină (task "
        "performance). Criteriul efectiv astfel construit nu acoperă dimensiunea "
        "nucleu a performanței: activitățile formale, livrabilele obligatorii și "
        "standardele de productivitate. O evaluare echilibrată trebuie să includă "
        "ambele dimensiuni — task performance și contextual performance — pentru a "
        "reflecta fidel contribuția totală a angajatului."
    ),

    # 226 | Performanță #22 — OCB subset al performanței contextuale
    (
        "Relația dintre OCB și performanța contextuală poate fi descrisă cu precizie "
        "conceptuală. "
        "✅ OCB este un subset al performanței contextuale, nu constituie întregul "
        "concept — performanța contextuală este mai largă. "
        "✅ Performanța contextuală este mai largă decât OCB și poate include forme "
        "de comportamente pozitive neincluse strict în dimensiunile clasice ale OCB "
        "definite de Organ. "
        "✅ Ambele vizează comportamente care susțin organizația și care depășesc "
        "cerințele formale minime ale postului. "
        "❌ OCB nu acoperă toate formele de performanță contextuală fără excepție — "
        "tocmai diferența de sferă conceptuală este esențială în utilizarea corectă "
        "a acestor termeni."
    ),

    # 227 | Performanță #23 — OCB: caracteristici
    (
        "Comportamentele de cetățenie organizațională (OCB) sunt caracterizate "
        "în literatura de specialitate prin câteva trăsături definitorii. "
        "✅ Sunt voluntare — angajații le manifestă din proprie inițiativă, nu pentru "
        "că sunt obligatorii prin contract sau prin fișa postului. "
        "✅ Sunt pozitive pentru organizație sau colegi — contribuie la funcționarea "
        "eficientă a echipei sau a firmei. "
        "✅ Sunt orientate spre a ajuta funcționarea echipei sau a firmei, distingându-se "
        "prin aceasta de comportamentele contraproductive (CWB). "
        "❌ Caracterul obligatoriu nu face parte din definițiile standard — tocmai "
        "voluntarietatea este trăsătura distinctivă care separă OCB de task "
        "performance."
    ),

    # 228 | Performanță #24 — dimensiunile OCB (Organ): toate corecte
    (
        "Modelul lui Dennis Organ identifică mai multe dimensiuni ale comportamentelor "
        "de cetățenie organizațională (OCB). "
        "✅ Altruismul: ajutor direct, voluntar, acordat colegilor în situații dificile "
        "— de exemplu, sprijinirea unui coleg nou în procesul de inițiere. "
        "✅ Conștiinciozitatea organizațională: depunerea unui efort care depășește "
        "minimul cerut formal — de exemplu, venitul mai devreme pentru o sarcină "
        "importantă. "
        "✅ Sportsmanship: toleranța față de inconveniențele muncii fără plângeri "
        "excesive sau comportamente obstrucționate. "
        "✅ Curtenia (courtesy): prevenirea problemelor prin comunicare proactivă și "
        "informarea anticipată a celor care ar putea fi afectați de deciziile proprii. "
        "Fiecare dimensiune vizează un tip distinct de comportament voluntar pozitiv."
    ),

    # 229 | Performanță #25 — ajutor coleg = altruism OCB
    (
        "Un angajat care ajută voluntar un coleg blocat la un proiect, fără ca aceasta "
        "să fie cerut în fișa postului, manifestă dimensiunea de altruism din modelul "
        "OCB al lui Organ. Altruismul în sens OCB se referă specific la comportamentele "
        "de sprijin direct, proactiv și neconstrâns acordat unui alt membru al echipei "
        "în situații de dificultate sau nevoie. Aceasta nu este un comportament "
        "contraproductiv față de organizație — dimpotrivă, contribuie la funcționarea "
        "echipei și la integrarea noilor colegi. Nu este nici virtute civică (care "
        "vizează implicarea în viața organizației la nivel mai larg) și nici sportsmanship "
        "(care vizează toleranța față de inconveniențe proprii)."
    ),

    # 230 | Performanță #26 — anunță lipsa din ședință = curtenie OCB
    (
        "Comportamentul unui membru al echipei care anunță din timp colegii că va "
        "lipsi de la o ședință, permițând reprogramarea oportună, ilustrează "
        "dimensiunea de curtenie (courtesy) din taxonomia OCB a lui Organ. Curtenia "
        "constă în acțiuni preventive de comunicare destinate să reducă inconveniențele "
        "pentru ceilalți — anunțul anticipat evită pierderea de timp a colegilor și "
        "permite adaptarea rapidă a planificării. Nu este altruism (care implică "
        "ajutor direct în situație de criză activă), nu este sportsmanship (care "
        "descrie toleranța față de inconveniențe proprii) și nu este performanță "
        "la sarcină — nu face parte din cerințele formale ale rolului."
    ),

    # 231 | Performanță #27 — sportsmanship + conștiinciozitate organizațională: exemple
    (
        "Sportsmanship-ul în sens OCB se referă la toleranța față de inconveniențele "
        "și schimbările inevitabile ale muncii fără a genera negativism sau plângeri "
        "excesive. "
        "✅ Acceptarea unei schimbări de procedură fără a crea rezistență sau a "
        "contamina negativ climatul echipei ilustrează sportsmanship. "
        "✅ Venitul mai devreme pentru a termina o sarcină importantă înainte de "
        "termen ilustrează conștiinciozitatea organizațională în sens OCB — efort "
        "voluntar dincolo de minimul cerut formal. "
        "❌ Furtul de echipamente din birou este un comportament contraproductiv "
        "(CWB), opusul oricărei forme de OCB. "
        "❌ Participarea la întâlniri opționale despre direcția firmei ilustrează "
        "virtutea civică, nu sportsmanship sau conștiinciozitate organizațională."
    ),

    # 232 | Performanță #28 — virtute civică OCB
    (
        "Virtutea civică (civic virtue) este una dintre dimensiunile OCB identificate "
        "de Organ și se referă la implicarea responsabilă și constructivă a angajatului "
        "în viața organizației, dincolo de cerințele formale ale rolului. "
        "✅ Participarea la ședințe interne opționale sau la inițiative de îmbunătățire "
        "a proceselor ilustrează virtutea civică. "
        "✅ Promovarea intereselor organizației în mod constructiv — de exemplu, "
        "propunerea unor idei de îmbunătățire — reflectă același construct. "
        "❌ Sabotarea politicilor firmei pentru avantaj personal este un comportament "
        "contraproductiv (CWB), opusul virtuții civice. "
        "❌ Respectarea strictă a sarcinilor din fișa postului fără nicio implicare "
        "extra este task performance, nu virtute civică."
    ),

    # 233 | Performanță #29 — OCB nu sunt impuse contractual (falsă)
    (
        "Afirmația că OCB sunt impuse contractual ca sarcini obligatorii, identice "
        "cu livrabilele din fișa postului, este falsă. Prin definiție, comportamentele "
        "de cetățenie organizațională sunt voluntare — ele nu sunt cerute prin "
        "contract sau prin documentele formale ale postului. Tocmai voluntarietatea "
        "este trăsătura definitorie care le distinge de task performance (activitățile "
        "obligatorii din fișa postului). OCB contribuie pozitiv la organizație și "
        "pot include altruism, curtenie sau virtute civică, dar nu sunt obligatorii — "
        "angajatul le manifestă din proprie inițiativă, nu la comandă. De asemenea, "
        "ele diferă clar de comportamentele contraproductive (CWB), care au impact "
        "negativ voluntar asupra organizației sau colegilor."
    ),
]

assert len(PART2_EXPLANATIONS) == 117, (
    f"Număr greșit de explicații: {len(PART2_EXPLANATIONS)} (așteptat 117)"
)
