"""Explicații pedagogice — Psihologia muncii II, itemi 235–351 (exam ID 9735–9851).

Conține exact 117 șiruri, corespunzând:
  • PERFORMANTA_MUNCII_ITEMS[29:50]               — itemi 30–50 (OCB, CWB, performanță adaptivă, măsurare)
  • FLUCTUATIE_SATISFACTIE_MUNCII_ITEMS[0:60]     — toți cei 60 de itemi fluctuație & satisfacție
  • VALUE_FIT_STRES_ITEMS[0:36]                    — itemi 1–36 (value fit, Schwartz, stres, Selye, P–E Fit, Karasek, Lazarus)
"""

from __future__ import annotations

from typing import List

PART3_EXPLANATIONS: List[str] = [

    # ══════════════════════════════════════════════════════
    # PERFORMANȚĂ — itemi 30–50 (indici globali 234–254)
    # ══════════════════════════════════════════════════════

    # 234 | Performanță #30 — predictori OCB: conștiinciozitate, agreabilitate, satisfacție, justiție
    (
        "Cercetarea identifică patru predictori susținuți empiric ai comportamentelor "
        "de cetățenie organizațională (OCB).\n\n"
        "✅ Conștiinciozitatea (Conscientiousness) prezice OCB deoarece persoanele "
        "conștiincioase sunt orientate spre îndatorire și depun efort dincolo de minimul "
        "obligatoriu.\n"
        "✅ Agreabilitatea (Agreeableness) facilitează comportamentele de ajutor față de "
        "colegi și cooperarea voluntară, trăsături direct legate de OCB.\n"
        "✅ Satisfacția la locul de muncă crește disponibilitatea de a contribui în plus "
        "față de cerințele formale — angajatul mulțumit tinde să reciprocheze pozitiv.\n"
        "✅ Justiția organizațională percepută stimulează reciprocitatea: angajatul tratat "
        "echitabil oferă mai mult voluntar organizației.\n\n"
        "❌ Neuroticismul ridicat nu este un predictor pozitiv consistent al OCB — "
        "cercetările arată mai degrabă o asociere neutră sau negativă, nu o relație "
        "pozitivă cu comportamentele de cetățenie."
    ),

    # 235 | Performanță #31 — de ce justiția percepută crește OCB
    (
        "Justiția organizațională percepută crește OCB prin mecanismul reciprocității "
        "sociale.\n\n"
        "✅ Angajații care percep că sunt tratați echitabil tind să răspundă cu efort "
        "suplimentar voluntar față de organizație — un schimb social implicit bazat pe "
        "norma reciprocității.\n"
        "✅ Percepția de corectitudine (procedurală, distributivă, interpersonală) crește "
        "motivația de a ajuta organizația dincolo de cerințele formale ale rolului.\n\n"
        "❌ Justiția organizațională nu elimină nevoia de performanță la sarcină (task) — "
        "cele două dimensiuni coexistă și nu se înlocuiesc reciproc.\n"
        "❌ OCB nu devine obligatoriu legal indiferent de context — rămâne un comportament "
        "voluntar, chiar și în organizații cu climat de echitate ridicat."
    ),

    # 236 | Performanță #32 — TF: agreabilitate scăzută → mai mult OCB (FALS)
    (
        "Fals. Afirmația inversează relația reală dintre agreabilitate și comportamentele "
        "de cetățenie organizațională. "
        "Agreabilitatea (Agreeableness) descrie tendința spre bunăvoință, cooperare și "
        "ajutor față de ceilalți — trăsătură care facilitează exact OCB. "
        "Cercetările confirmă că persoanele cu agreabilitate ridicată manifestă mai mult "
        "altruism, curtoazie și comportamente prosociale la locul de muncă, nu mai puțin. "
        "Persoanele cu agreabilitate scăzută sunt mai competitive, mai puțin empatice "
        "și mai puțin predispuse să ajute voluntar colegii sau organizația."
    ),

    # 237 | Performanță #33 — CWB: caracteristici
    (
        "Comportamentele contraproductive la locul de muncă (CWB) se definesc prin "
        "trei caracteristici esențiale.\n\n"
        "✅ Sunt voluntare — nu reprezintă erori accidentale sau omisiuni neintenționante, "
        "ci acte deliberate care dăunează organizației sau persoanelor.\n"
        "✅ Au impact negativ asupra organizației (furt, sabotaj, absenteism deliberat) "
        "sau asupra colegilor și clienților (agresivitate, bullying).\n"
        "✅ Pot viza fie organizația ca entitate (CWB-O), fie persoanele din cadrul ei "
        "(CWB-P) — aceasta este distincția clasică în literatura de specialitate.\n\n"
        "❌ CWB nu sunt identice cu lipsa performanței la sarcină (task) — performanța "
        "la sarcină vizează livrarea sarcinilor formale, în timp ce CWB reprezintă acte "
        "active de daune, conceptual distincte."
    ),

    # 238 | Performanță #34 — exemple CWB spre organizație vs persoane
    (
        "Toate cele patru exemple ilustrează comportamente contraproductive, "
        "distribuite între cele două subcategorii principale.\n\n"
        "✅ Furtul de materiale din firmă și sabotajul intenționat al echipamentelor "
        "sunt CWB orientate spre organizație (CWB-O) — produc pierderi materiale sau "
        "perturbă procesele organizaționale.\n"
        "✅ Absenteismul deliberat fără motiv legitim este tot CWB-O: subminează "
        "productivitatea și implică o alegere conștientă de a nu contribui.\n"
        "✅ Agresivitatea și bullying-ul față de colegi sunt CWB orientate spre persoane "
        "(CWB-P) — dăunează direct indivizilor din organizație.\n"
        "Această clasificare ajută HR-ul să identifice tipul de intervenție preventivă "
        "cel mai potrivit pentru fiecare categorie."
    ),

    # 239 | Performanță #35 — trăsături de personalitate asociate cu mai multe CWB
    (
        "Cercetarea privind predictori de personalitate ai CWB identifică trei trăsături "
        "Big Five asociate pozitiv cu comportamentele contraproductive.\n\n"
        "✅ Neuroticismul (N) ridicat crește instabilitatea emoțională, frustrarea și "
        "impulsivitatea, toate mărind riscul de acte contraproductive la locul de muncă.\n"
        "✅ Conștiinciozitatea (C) scăzută înseamnă mai puțin autocontrol și orientare "
        "spre îndatorire, ceea ce reduce inhibiția față de comportamente dăunătoare.\n"
        "✅ Agreabilitatea (A) scăzută implică mai puțină bunăvoință față de ceilalți "
        "și mai multă ostilitate sau indiferență față de impactul acțiunilor proprii.\n\n"
        "❌ Conștiinciozitatea (C) ridicată este asociată cu mai puține CWB — persoanele "
        "conștiincioase au autocontrol mai bun și respectă normele organizaționale."
    ),

    # 240 | Performanță #36 — factori situaționali care cresc CWB
    (
        "Factorii situaționali care cresc CWB implică percepții de nedreptate și "
        "lipsă de control.\n\n"
        "✅ Percepția de injustiție organizațională (procedurală sau distributivă) poate "
        "motiva angajații să se „răzbune» prin acte deliberate de daune — un răspuns "
        "de represalii față de tratamentul inechitabil perceput.\n"
        "✅ Frustrarea la locul de muncă — blocarea obiectivelor sau a nevoilor — crește "
        "impulsivitatea și probabilitatea unor reacții contraproductive.\n"
        "✅ Lipsa controlului asupra propriului rol poate genera resentiment și "
        "comportamente de sabotaj indirect sau retragere deliberată.\n\n"
        "❌ Justiția organizațională ridicată și recunoașterea echitabilă reduc CWB, "
        "nu le cresc — tratamentul echitabil diminuează motivația pentru comportamente "
        "de represalii."
    ),

    # 241 | Performanță #37 — împrumut neautorizat de echipament = CWB-O
    (
        "Împrumutarea fără permisiune a echipamentului firmei pentru uz personal este "
        "un comportament contraproductiv (CWB) orientat spre organizație. "
        "Acesta este un act voluntar care aduce beneficiu angajatului în detrimentul "
        "resurselor organizației, fără acordul acesteia. "
        "Nu se califică drept comportament de cetățenie organizațională (OCB) — OCB "
        "implică acțiuni voluntare pozitive care ajută organizația sau colegii, nu "
        "acte de însușire a bunurilor firmei. "
        "Nu reprezintă nici performanță contextuală pozitivă sau performanță la sarcină, "
        "deoarece nu contribuie la obiectivele organizaționale, ci le subminează."
    ),

    # 242 | Performanță #38 — TF: OCB și CWB sunt poli opuși (FALS)
    (
        "Fals. OCB și CWB nu sunt poli opuși ai aceleiași dimensiuni unidimensionale. "
        "Cercetările arată că cele două constructe sunt relativ independente: un angajat "
        "poate manifesta atât comportamente de cetățenie organizațională (de exemplu, "
        "ajutând colegii), cât și comportamente contraproductive (de exemplu, absentând "
        "deliberat) — nu neapărat în același timp, dar în pattern-uri comportamentale "
        "complexe. "
        "Absența OCB nu înseamnă automat prezența CWB, iar prezența OCB ridicat nu "
        "exclude complet apariția unor CWB. "
        "Modelarea lor ca dimensiuni distincte permite o evaluare mai fidelă a "
        "comportamentului organizațional."
    ),

    # 243 | Performanță #39 — distincții corecte OCB vs CWB
    (
        "Distincția dintre OCB și CWB se bazează pe direcția intenției și pe "
        "impactul comportamentului.\n\n"
        "✅ OCB sunt voluntare și pozitive; CWB sunt voluntare și negative — ambele sunt "
        "acte intenționante, dar cu efecte opuse pentru organizație.\n"
        "✅ OCB ajută organizația sau persoanele din ea; CWB dăunează organizației sau "
        "persoanelor — aceasta este diferența funcțională esențială.\n"
        "✅ Lipsa OCB nu este automat echivalentă cu CWB — un angajat neutru care nu "
        "ajută în plus, dar nici nu dăunează, nu se încadrează în niciuna din categorii.\n\n"
        "❌ OCB și CWB nu sunt același construct măsurat invers — sunt dimensiuni "
        "conceptual și empiric distincte, cu corelații diferite cu predictori."
    ),

    # 244 | Performanță #40 — angajat fără OCB și fără CWB
    (
        "Angajatul descris se află într-o zonă de performanță comportamentală neutră — "
        "fără efort suplimentar voluntar, dar și fără daune active.\n\n"
        "✅ Absența OCB (nu ajută în plus) nu înseamnă automat prezența CWB — persoana "
        "nu fură, nu agresează și nu sabotează, deci nu se califică pentru categoria "
        "comportamentelor contraproductive.\n"
        "✅ Poate avea performanță la sarcină (task) acceptabilă sau bună, dar "
        "performanța contextuală este probabil redusă, deoarece nu contribuie voluntar "
        "la susținerea echipei sau organizației.\n\n"
        "❌ Nu trebuie clasificat automat ca CWB pentru indiferență — indiferența față "
        "de colegi nu echivalează cu un act deliberat de daune.\n"
        "❌ OCB scăzut nu este sinonim cu sabotaj organizațional."
    ),

    # 245 | Performanță #41 — performanța adaptivă: definiție
    (
        "Performanța adaptivă (adaptive performance) descrie capacitatea angajatului "
        "de a răspunde eficient la schimbări și de a-și ajusta comportamentul la "
        "cerințe noi sau în evoluție.\n\n"
        "✅ Răspunsul eficient la schimbările de la locul de muncă — restructurări, "
        "tehnologii noi, sarcini modificate — este nucleul conceptului.\n"
        "✅ Învățarea procedurilor noi și ajustarea la cerințe în evoluție include "
        "flexibilitate cognitivă și disponibilitate față de schimbare.\n\n"
        "❌ Menținerea rigidă a acelorași obiceiuri, indiferent de context, este "
        "opusul performanței adaptive — descrie inflexibilitate comportamentală.\n"
        "❌ Refuzul oricărei modificări a sarcinilor nu caracterizează performanța "
        "adaptivă, ci rezistența activă la schimbare."
    ),

    # 246 | Performanță #42 — predictori ai performanței adaptive: GMA, Openness
    (
        "Cercetarea privind predictori ai performanței adaptive identifică doi factori "
        "principali susținuți empiric.\n\n"
        "✅ Aptitudinea mentală generală (GMA) facilitează învățarea rapidă a "
        "procedurilor noi și adaptarea cognitivă la situații neprevăzute — procese "
        "centrale în performanța adaptivă.\n"
        "✅ Deschiderea față de experiență (Openness) din modelul Big Five este "
        "asociată cu curiozitate intelectuală, toleranță la ambiguitate și dorință de "
        "explorare — caracteristici care susțin flexibilitatea și adaptabilitatea.\n\n"
        "❌ Neuroticismul ridicat nu este un predictor pozitiv consistent al performanței "
        "adaptive — poate reduce eficiența în situații de incertitudine și schimbare.\n"
        "❌ Agreabilitatea scăzută nu este identificată drept predictor central al "
        "performanței adaptive în literatura de specialitate."
    ),

    # 247 | Performanță #43 — tehnician după restructurare = performanță adaptivă
    (
        "Scenariul tehnicianului care, după restructurare, învață rapid noul software "
        "și propune îmbunătățiri de proces ilustrează cel mai bine performanța adaptivă. "
        "Aceasta implică nu doar asimilarea de cunoștințe tehnice noi, ci și inițiativa "
        "proactivă de a propune îmbunătățiri — un comportament de adaptare la schimbarea "
        "organizațională care depășește simpla conformare la noile cerințe. "
        "Nu este un comportament contraproductiv (CWB), nu este o performanță statică "
        "la sarcini identice, și nici nu implică vreo eroare de evaluare a criteriului. "
        "Performanța adaptivă este considerată a treia dimensiune importantă, alături "
        "de performanța la sarcină și cea contextuală."
    ),

    # 248 | Performanță #44 — măsurare obiectivă vs subiectivă
    (
        "Evaluarea performanței prin metode obiective și subiective prezintă avantaje "
        "și limitări complementare.\n\n"
        "✅ Măsurarea obiectivă (vânzări, număr de erori, producție) reduce parțial "
        "subiectivitatea evaluatorului și oferă date verificabile independent.\n"
        "✅ Măsurarea subiectivă (ratingul superiorului) poate capta comportamente "
        "interpersonale, contextuale sau calitative dificil de cuantificat obiectiv.\n"
        "✅ Ratingul superiorului este flexibil, dar vulnerabil la erori sistematice, "
        "inclusiv favoritismul și simpatia personală — forme de contaminare a criteriului.\n\n"
        "❌ Măsurarea obiectivă nu captează automat toate dimensiunile OCB — "
        "comportamentele de cetățenie organizațională sunt prin natura lor greu de "
        "transpus în indicatori cantitativi."
    ),

    # 249 | Performanță #45 — manager: doar număr apeluri = deficiență criteriu
    (
        "Evaluarea exclusiv prin numărul de apeluri preluate, fără a lua în considerare "
        "calitatea comunicării cu clienții, ilustrează deficiența criteriului (criterion "
        "deficiency). "
        "Criteriul efectiv (numărul de apeluri) este mai îngust decât criteriul teoretic "
        "ideal al performanței agentului de call center, care ar trebui să includă și "
        "calitatea relațiilor cu clienții, rezolvarea eficientă a problemelor și "
        "satisfacția clientului. "
        "Nu este un criteriu prea larg (nu sunt incluși factori nerelevanți), nu implică "
        "contaminare prin simpatie (nu apare o sursă de zgomot afectiv), și nu "
        "supra-măsoară performanța contextuală."
    ),

    # 250 | Performanță #46 — afirmație exagerată: măsurarea obiectivă e mereu superioară
    (
        "Afirmația că măsurarea obiectivă elimină complet orice eroare și este "
        "întotdeauna superioară celei subiective este exagerată și greșită. "
        "Indicatorii obiectivi (vânzări, producție, erori) reduc parțial subiectivitatea, "
        "dar nu elimină surse de eroare precum factorii externi — condițiile pieței, "
        "echipamentul disponibil, cooperarea colegilor — care pot influența rezultatele "
        "independent de efortul individual (contaminare prin context). "
        "Ratingul subiectiv al superiorului rămâne util pentru a capta comportamente "
        "interpersonale sau contextuale imposibil de cuantificat obiectiv. "
        "Nicio metodă de măsurare nu este perfect superioară în orice context."
    ),

    # 251 | Performanță #47 — scenarii contaminare vs deficiență
    (
        "Contaminarea și deficiența criteriului sunt tipuri distincte de erori în "
        "evaluarea performanței.\n\n"
        "✅ Nota crește din cauza prieteniei cu șeful — aceasta este contaminare: "
        "în scorul de performanță intră un factor nerelevant (simpatia personală).\n"
        "✅ Evaluarea ignoră comportamentele de colaborare — aceasta este deficiență: "
        "criteriul efectiv nu acoperă o parte importantă din criteriul teoretic.\n"
        "✅ În scor intră performanța echipei, nu a individului evaluat — tot contaminare: "
        "scorul individual reflectă un factor extern (performanța colectivă).\n\n"
        "❌ Criteriul care include strict sarcinile relevante din job descrie situația "
        "ideală de relevanță ridicată, nu un exemplu de contaminare sau deficiență."
    ),

    # 252 | Performanță #48 — rezumat corect al modelului performanței
    (
        "Toate cele patru afirmații rezumă corect modelul integrat al performanței "
        "în muncă.\n\n"
        "✅ Performanța combină atât comportamentele prestate, cât și rezultatele "
        "obținute — definiția largă acceptată în psihologia muncii.\n"
        "✅ Modelul Borman–Motowidlo distinge performanța la sarcină (activitățile "
        "esențiale din fișa postului) de performanța contextuală (comportamente "
        "suplimentare care susțin organizația), iar OCB este un subset al celei "
        "contextuale.\n"
        "✅ OCB (pozitiv, voluntar) și CWB (negativ, voluntar) sunt distincte conceptual "
        "și nu sunt polii aceleiași dimensiuni unidimensionale.\n"
        "✅ Relevanța, deficiența și contaminarea descriu calitatea criteriului efectiv "
        "față de criteriul teoretic ideal al evaluării."
    ),

    # 253 | Performanță #49 — scădere notă pentru „lipsă entuziasm la petreceri»
    (
        "Scăderea notei pentru că angajatul „nu e suficient de entuziast la petreceri» "
        "ridică două probleme simultane.\n\n"
        "✅ Contaminarea criteriului — entuziasmul la petreceri este un factor nerelevant "
        "pentru performanța la job, dar influențează scorul de performanță al "
        "angajatului, degradând criteriul efectiv.\n"
        "✅ Confundarea dintre OCB opțional (participarea entuziastă la petreceri nu "
        "este obligatorie) și cerințele formale de task — evaluatorul penalizează "
        "lipsa unui comportament voluntar de parcă ar fi o obligație contractuală.\n\n"
        "❌ Nu este deficiență a criteriului — criteriul pare să acopere task-ul, "
        "dar adaugă factori nerelevanți (contaminare).\n"
        "❌ Nu indică validitate incrementală ridicată — dimpotrivă, criteriul este "
        "degradat prin introducerea unui element nerelevant."
    ),

    # 254 | Performanță #50 — TF: criteriu teoretic vs efectiv, relevanță/deficiență/contaminare (ADEVĂRAT)
    (
        "Adevărat. Această afirmație rezumă corect distincția tripartită a calității "
        "criteriilor de evaluare a performanței. "
        "Criteriul teoretic descrie constructul ideal al performanței — tot ceea ce ar "
        "trebui evaluat pentru a capta fidel munca angajatului. "
        "Criteriul efectiv descrie ce măsurăm în practică — de regulă o aproximare a "
        "celui teoretic. "
        "Relevanța reprezintă intersecția utilă dintre cele două, deficiența este partea "
        "din criteriul teoretic care lipsește din cel efectiv, iar contaminarea este "
        "ceea ce intră în criteriul efectiv fără a face parte din cel teoretic. "
        "Maximizarea relevanței și minimizarea deficienței și contaminării sunt "
        "obiectivele unui sistem de evaluare bine construit."
    ),

    # ══════════════════════════════════════════════════════
    # FLUCTUAȚIE & SATISFACȚIE — 60 itemi (indici globali 255–314)
    # ══════════════════════════════════════════════════════

    # 255 | Fluctuație #1 — TF: turnover = plecare voluntară sau involuntară (ADEVĂRAT)
    (
        "Adevărat. Turnover-ul, sau fluctuația personalului, definește în sens larg "
        "orice plecare a unui angajat din organizație, indiferent de cine a inițiat "
        "separarea. "
        "Turnover-ul voluntar apare când angajatul ia decizia de a demisiona sau de a "
        "căuta un alt angajator, din proprie inițiativă. "
        "Turnover-ul involuntar apare când organizația pune capăt relației de muncă "
        "prin concediere, restructurare sau neînnoirea contractului. "
        "Ambele tipuri generează costuri și consecințe pentru organizație, dar natura "
        "și magnitudinea lor diferă în funcție de cine pleacă și de ce."
    ),

    # 256 | Fluctuație #2 — voluntar vs involuntar: distincție corectă
    (
        "Distincția corectă este că în turnover-ul voluntar angajatul inițiază plecarea, "
        "iar în cel involuntar organizația pune capăt contractului. "
        "Această distincție este esențială pentru analiza cauzelor și intervenția HR: "
        "turnover-ul voluntar semnalează probleme de satisfacție, climat sau carieră "
        "pe care organizația le poate adresa proactiv, în timp ce cel involuntar este "
        "inițiat de firmă din motive disciplinare, economice sau de restructurare. "
        "Celelalte variante sunt incorecte deoarece descriu fie transferuri interne "
        "(care nu sunt turnover), fie absențe sau concedii medicale care nu constituie "
        "separări permanente de organizație."
    ),

    # 257 | Fluctuație #3 — TF: funcțional (pleacă slabi) vs disfuncțional (pleacă valoroși) (ADEVĂRAT)
    (
        "Adevărat. Distincția funcțional-disfuncțional completează analiza turnover-ului "
        "dincolo de simpla rată de fluctuație. "
        "Turnover-ul funcțional — când pleacă angajații cu performanță slabă sau cu "
        "potrivire redusă cu organizația — poate fi benefic, eliberând posturi pentru "
        "persoane mai potrivite și îmbunătățind calitatea medie a echipei. "
        "Turnover-ul disfuncțional — când pleacă performanții sau angajații cu know-how "
        "critic — este considerat cel mai problematic: organizația pierde capital uman "
        "valoros, suportă costuri de înlocuire ridicate și poate pierde avantaje "
        "competitive pe termen lung."
    ),

    # 258 | Fluctuație #4 — IT: pierde 3 programatori de top = turnover disfuncțional
    (
        "Cel mai îngrijorător tip de turnover din scenariul descris este cel disfuncțional "
        "— plecarea celor trei programatori de top. "
        "Pierderea angajaților valoroși înseamnă pierdere de expertiză, de relații cu "
        "clienții și de cunoștințe organizaționale greu de înlocuit rapid sau ieftin. "
        "Concedierea celor doi angajați cu performanță sub așteptări reprezintă turnover "
        "funcțional sau involuntar funcțional — un rezultat neutru sau chiar pozitiv. "
        "Distincția voluntar-involuntar nu captează esența problemei — contează mai mult "
        "cine pleacă (performanți valoroși vs neperformanți) decât cine a inițiat separarea."
    ),

    # 259 | Fluctuație #5 — funcțional + disfuncțional: afirmații corecte
    (
        "Primele trei afirmații descriu corect natura și consecințele turnover-ului "
        "funcțional și disfuncțional.\n\n"
        "✅ Turnover-ul funcțional implică plecarea angajaților cu performanță slabă, "
        "ceea ce poate îmbunătăți calitatea medie a echipei și elibera resurse pentru "
        "recrutare mai potrivită.\n"
        "✅ Turnover-ul disfuncțional implică pierderea performanților, cu consecințe "
        "directe: pierdere de know-how, costuri de înlocuire și impact negativ asupra "
        "moralului echipei.\n"
        "✅ Disfuncționalul este considerat cel mai problematic, deoarece dăunează "
        "capacității organizației pe termen lung.\n\n"
        "❌ Turnover-ul funcțional nu este întotdeauna de dorit în orice volum sau "
        "context — o rată ridicată de fluctuație, chiar dacă „funcțională», generează "
        "instabilitate și costuri de recrutare repetate."
    ),

    # 260 | Fluctuație #6 — afirmație falsă: disfuncțional e preferabil
    (
        "Afirmația că turnover-ul disfuncțional este preferabil pentru că eliberează "
        "posturi de neperformanți este fundamental greșită — confundă termenii. "
        "Prin definiție, turnover-ul disfuncțional înseamnă că pleacă angajații "
        "valoroși, nu neperformanții. "
        "Eliberarea posturilor de neperformanți descrie exact turnover-ul funcțional, "
        "care poate fi benefic. "
        "Disfuncționalul este considerat cel mai problematic tip de fluctuație tocmai "
        "pentru că organizația pierde resursele umane de care are cea mai mare nevoie "
        "pentru susținerea performanței."
    ),

    # 261 | Fluctuație #7 — scenarii voluntar/involuntar
    (
        "Toate cele patru scenarii ilustrează corect tipurile de turnover.\n\n"
        "✅ Angajatul care demisionează pentru un salariu mai bun și cel care pleacă "
        "după ce a găsit alt job sunt exemple de turnover voluntar — angajatul a "
        "inițiat decizia de a pleca.\n"
        "✅ Concedierea pentru abateri repetate și neînnoirea contractului la inițiativa "
        "angajatorului sunt exemple de turnover involuntar — organizația a terminat "
        "relația de muncă.\n"
        "Această varietate de scenarii arată că tipologia turnover-ului surprinde "
        "situații reale diverse și ajută HR-ul să aleagă intervențiile corecte în "
        "funcție de tipul și cauza fluctuației."
    ),

    # 262 | Fluctuație #8 — de ce nu ajunge să raportezi doar rata de fluctuație
    (
        "Raportarea exclusivă a ratei de fluctuație fără a distinge tipul de turnover "
        "poate induce în eroare diagnosticul organizațional.\n\n"
        "✅ Aceeași rată poate ascunde situații complet diferite: dacă pleacă performanții "
        "(disfuncțional), organizația are o problemă critică; dacă pleacă neperformanții "
        "(funcțional), situația poate fi neutră sau chiar pozitivă.\n"
        "✅ Costurile și implicațiile strategice diferă radical după profilul și motivele "
        "celor care pleacă — pierderea unui specialist-cheie este incomparabil mai "
        "costisitoare decât plecarea unui angajat cu performanță slabă.\n"
        "✅ Distincția voluntar-involuntar ajută la înțelegerea cauzelor și la "
        "calibrarea intervențiilor HR (îmbunătățirea climatului vs selecție mai riguroasă).\n\n"
        "❌ Nu toate tipurile de turnover au același impact — distincția nu este "
        "decorativă, ci esențială pentru prioritizarea resurselor HR."
    ),

    # 263 | Fluctuație #9 — TF: Withdrawal Model = lanț insatisfacție→...→plecare (ADEVĂRAT)
    (
        "Adevărat. Modelul retragerii (Withdrawal Model) descrie o secvență logică "
        "de etape prin care insatisfacția la muncă se transformă treptat în comportament "
        "de plecare efectivă. "
        "Procesul nu este imediat sau brusc: angajatul parcurge mai întâi gânduri despre "
        "plecare, apoi caută activ alternative de angajare și, în final, formează o "
        "intenție clară de a pleca, înainte de a demisiona efectiv. "
        "Această progresie graduală explică de ce intenția de plecare este cel mai bun "
        "predictor al turnover-ului și de ce intervențiile HR la etapele timpurii pot "
        "preveni plecările."
    ),

    # 264 | Fluctuație #10 — ordinea corectă în Withdrawal Model
    (
        "Ordinea corectă în modelul retragerii (Withdrawal Model) este: insatisfacție "
        "la muncă, urmată de gânduri despre plecare, căutare de alternative de angajare, "
        "formare a intenției de plecare și, în final, plecarea efectivă. "
        "Această secvență reflectă o escaladare treptată a dezangajamentului, nu o "
        "decizie bruscă. "
        "Nicio altă ordine nu este susținută de model: plecarea nu precede intenția, "
        "iar căutarea de alternative nu apare înaintea insatisfacției percepute."
    ),

    # 265 | Fluctuație #11 — intenția de plecare = cel mai bun predictor al turnover-ului
    (
        "Intenția de plecare este cel mai bun predictor individual al turnover-ului "
        "efectiv — aceasta este concluzia susținută cel mai consistent de meta-analizele "
        "din domeniu. "
        "Intenția capturează etapa imediat anterioară plecării în modelul retragerii și "
        "reflectă o decizie deja parțial formată, cu motivații și alternative deja "
        "evaluate. "
        "Absențele recente pot fi simptome ale dezangajamentului, dar nu prezic "
        "sistematic mai bine decât intenția declarată. "
        "Vârsta cronologică singură are o relație slabă și inconsistentă cu turnover-ul, "
        "iar satisfacția raportată în urmă cu cinci ani are relevanță predictivă mult "
        "mai redusă decât starea actuală a angajatului."
    ),

    # 266 | Fluctuație #12 — angajat care caută job = etapa de intenție de plecare
    (
        "Angajatul descris — nemulțumit, căutând activ joburi și declarând intenția de "
        "a pleca — se află cel mai probabil la etapa de intenție de plecare din modelul "
        "retragerii, nu la turnover efectiv. "
        "El nu a demisionat încă — vine la serviciu, deci plecarea nu s-a produs. "
        "Prezența căutării active și intenției declarate explicit sunt indicatori "
        "puternici ai etapei pre-plecare din model. "
        "Nu este vorba despre turnover involuntar, deoarece organizația nu a inițiat "
        "nicio procedură de separare."
    ),

    # 267 | Fluctuație #13 — sindromul hobo: definiție
    (
        "Sindromul hobo (Hobo Syndrome) descrie tendința ca istoricul de schimbare "
        "repetată a locurilor de muncă să prezică turnover viitor la aceeași persoană. "
        "Cu alte cuvinte, angajații cu un pattern de joburi scurte în trecut prezintă "
        "un risc mai mare de a schimba și jobul actual față de angajații cu stabilitate "
        "anterioară. "
        "Nu are legătură cu predarea laptopului la demisie (obligație administrativă), "
        "cu transferul satisfacției de la muncă la viața personală (spill-over) sau cu "
        "angajamentul afectiv față de organizație."
    ),

    # 268 | Fluctuație #14 — factori asociați cu turnover/intenție de plecare
    (
        "Cercetarea identifică mai mulți factori organizaționali și contextuali care "
        "prezic turnover-ul sau intenția de plecare.\n\n"
        "✅ Salariul și perspectivele de promovare sunt factori clasici de atracție "
        "sau retenție — insatisfacția față de remunerare sau lipsa avansării cresc "
        "intenția de plecare.\n"
        "✅ Suportul șefului și climatul organizațional influențează direct percepția "
        "zilnică a angajatului și satisfacția față de mediul de muncă.\n"
        "✅ Stilul de leadership perceput afectează relația cu supervizorul, autonomia "
        "și sentimentul de recunoaștere — toate legate de decizia de a rămâne sau pleca.\n\n"
        "❌ Descrierea postului din analiza orientată spre sarcină este un document "
        "tehnic de resurse umane și nu prezice direct decizia individuală de a pleca."
    ),

    # 269 | Fluctuație #15 — personalitate și fluctuație: N, C, Openness
    (
        "Cercetarea privind relația dintre personalitate și fluctuație identifică trei "
        "tendințe relativ consistente.\n\n"
        "✅ Neuroticismul (N) mai ridicat este asociat cu mai mult turnover sau intenție "
        "de plecare — persoanele cu instabilitate emoțională mai pronunțată percep mai "
        "intens insatisfacțiile și reacționează mai rapid prin căutarea de alternative.\n"
        "✅ Conștiinciozitatea (C) mai ridicată este asociată cu mai puțin turnover — "
        "persoanele conștiincioase tind să respecte angajamentele și să investească "
        "în rolul actual.\n"
        "✅ Deschiderea față de experiență (Openness) poate fi asociată cu mai multă "
        "schimbare de job, din căutarea de varietate, noutate și provocări intelectuale.\n\n"
        "❌ Extraversiunea nu elimină complet intenția de plecare — efectul ei asupra "
        "turnover-ului este modest și dependent de context."
    ),

    # 270 | Fluctuație #16 — etapele din Withdrawal Model înainte de plecare
    (
        "Toate cele patru etape — insatisfacție la muncă, gânduri despre plecare, "
        "căutare de alternative de angajare și intenție de plecare — intervin înainte "
        "de plecarea efectivă în modelul retragerii. "
        "Modelul descrie un lanț secvențial și progresiv în care dezangajamentul se "
        "acumulează treptat. "
        "Intervențiile HR care adresează oricare dintre primele etape — reducerea "
        "insatisfacției sau crearea perspectivelor de carieră — pot întrerupe lanțul "
        "înainte ca angajatul să ajungă la plecarea efectivă."
    ),

    # 271 | Fluctuație #17 — TF: intenția de plecare = predictor slab (FALS)
    (
        "Fals. Intenția de plecare este, dimpotrivă, cel mai bun predictor individual "
        "al turnover-ului efectiv — una dintre concluziile cele mai stabile din "
        "literatura de resurse umane. "
        "Meta-analizele arată că o proporție semnificativă a celor care declară intenție "
        "de plecare pleacă efectiv, mai ales atunci când există și alternative de "
        "angajare disponibile. "
        "Afirmația că „majoritatea rămân definitiv în firmă» contrazice datele de "
        "cercetare și ar sugera că sondajele de intenție sunt inutile — ceea ce nu "
        "corespunde practicii HR eficiente."
    ),

    # 272 | Fluctuație #18 — 6 joburi în 8 ani = sindromul hobo
    (
        "Candidatul cu șase joburi în opt ani, fiecare sub un an, ilustrează sindromul "
        "hobo — tendința ca schimbarea repetată a locurilor de muncă din trecut să "
        "prezică același comportament în viitor. "
        "Istoricul de fluctuație este unul dintre cei mai buni predictori ai fluctuației "
        "viitoare, mai ales când pattern-ul este consistent și nu există justificări "
        "contextuale clare (ex. restructurări masive sau industrie sezonieră). "
        "Nu este vorba despre spill-over (transfer intra-personal al stresului), nici "
        "despre turnover funcțional (pleacă neperformanții) sau cross-over (influența "
        "stării afective a partenerului)."
    ),

    # 273 | Fluctuație #19 — definiție satisfacție muncii
    (
        "Satisfacția muncii se definește cel mai precis prin două componente "
        "complementare.\n\n"
        "✅ Evaluarea afectivă a experienței profesionale — starea de bine sau "
        "disconfort emoțional față de job în ansamblu sau față de aspecte specifice "
        "ale acestuia.\n"
        "✅ Compararea așteptărilor cu realitatea de la job — discrepanța dintre ce "
        "aștepta angajatul și ce găsește efectiv în rol influențează direct nivelul "
        "de satisfacție.\n\n"
        "❌ Numărul de ore suplimentare lucrate lunar este un indicator de volum de "
        "muncă, nu o definiție a satisfacției.\n"
        "❌ Scorul la un test de inteligență generală (GMA) măsoară o aptitudine "
        "cognitivă, fără legătură directă cu evaluarea afectivă a jobului."
    ),

    # 274 | Fluctuație #20 — definiție satisfacție muncii (variantă)
    (
        "Satisfacția muncii este definită cel mai bine prin combinarea dimensiunii "
        "afective cu cea cognitivă.\n\n"
        "✅ Evaluarea afectivă (pozitivă sau negativă) a experienței la job surprinde "
        "cum simte angajatul munca sa — plăcut sau neplăcut, satisfăcător sau frustrant.\n"
        "✅ Compararea așteptărilor cu ceea ce oferă efectiv munca reflectă componenta "
        "cognitivă: satisfacția crește când realitatea îndeplinește sau depășește "
        "așteptările și scade când există un decalaj negativ.\n\n"
        "❌ Numărul de promovări obținute în ultimii cinci ani este un indicator de "
        "evoluție în carieră, nu o definiție a satisfacției muncii.\n"
        "❌ Scorul la un test de aptitudini profesionale măsoară competența, nu "
        "evaluarea afectivă față de job."
    ),

    # 275 | Fluctuație #21 — Locke: satisfacția crește când munca permite valorile
    (
        "Conform teoriei lui Edwin Locke, satisfacția muncii crește atunci când munca "
        "permite angajatului să-și trăiască și să-și împlinească valorile personale "
        "importante.\n\n"
        "✅ Când munca permite îndeplinirea valorilor personale (autonomie, echitate, "
        "realizare etc.), angajatul percepe jobul ca semnificativ și aliniat cu ceea "
        "ce consideră important.\n"
        "✅ Jobul care se aliniază cu valorile celui care lucrează generează o stare "
        "pozitivă față de acea muncă — nucleul satisfacției în teoria lui Locke.\n\n"
        "❌ Primirea automată a celui mai mare salariu din piață, indiferent de valori, "
        "nu garantează satisfacție conform lui Locke — remunerarea contează, dar numai "
        "în măsura în care se aliniază cu valorile personale ale angajatului.\n"
        "❌ Dimensiunea organizației nu este un predictor al satisfacției."
    ),

    # 276 | Fluctuație #22 — câștigă bine dar valorile sunt contradictorii
    (
        "Conform lui Locke, satisfacția acestui angajat va fi probabil scăzută, "
        "deoarece valorile personale nu sunt împlinite la job. "
        "Teoria lui Locke susține explicit că satisfacția muncii derivă din percepția "
        "că munca permite trăirea valorilor importante pentru individ — și nu este "
        "determinată exclusiv de remunerare. "
        "Chiar dacă salariul este bun, contradicția zilnică cu valorile personale "
        "(etică, echilibru viață-muncă) generează disonanță și insatisfacție. "
        "Salariul este o dimensiune a satisfacției, dar nu anulează celelalte "
        "dimensiuni, în special componenta valorilor personale."
    ),

    # 277 | Fluctuație #23 — satisfacție vs concepte învecinate
    (
        "Satisfacția muncii este un construct distinct față de alte concepte "
        "organizaționale, iar primele trei distincții sunt corecte.\n\n"
        "✅ Satisfacția reprezintă o evaluare afectivă a jobului în ansamblu sau a "
        "dimensiunilor sale, nu o simplă enumerare de beneficii contractuale.\n"
        "✅ Satisfacția nu se reduce nici la performanță obiectivă, nici la prezența "
        "fizică la serviciu — un angajat poate fi prezent și productiv, dar insatisfăcut.\n"
        "✅ Așteptările nerealizate pot alimenta insatisfacția în modelul retragerii: "
        "decalajul așteptări-realitate inițiază lanțul care poate duce la intenție de "
        "plecare și turnover efectiv.\n\n"
        "❌ Satisfacția față de muncă nu înseamnă același lucru cu angajamentul "
        "organizațional — satisfacția vizează jobul/sarcinile, angajamentul vizează "
        "legătura cu organizația ca întreg."
    ),

    # 278 | Fluctuație #24 — afirmație falsă: satisfacție = productivitate
    (
        "Afirmația că satisfacția se reduce la productivitate — că a produce mult "
        "înseamnă automat a fi satisfăcut — este exagerată și incorectă. "
        "Cercetarea arată că relația dintre satisfacție și performanță este pozitivă, "
        "dar modestă, și nu permite inversarea logicii: nu orice angajat productiv "
        "este satisfăcut, și nu orice angajat satisfăcut este maxim productiv. "
        "Satisfacția are componente afective, cognitive și valorice care depășesc "
        "simpla măsurare a output-ului. "
        "Un angajat poate fi productiv din obligație, frică sau standard personal, "
        "fără să resimtă satisfacție autentică față de job."
    ),

    # 279 | Fluctuație #25 — utilitatea distincției așteptări vs realitate
    (
        "Distincția așteptări față de realitate este utilă în înțelegerea satisfacției "
        "muncii din trei motive complementare.\n\n"
        "✅ Aceeași situație obiectivă poate satisface pe unii și nu pe alții — totul "
        "depinde de ce aștepta fiecare angajat înainte de a intra în acel job.\n"
        "✅ Explică de ce doi colegi la același job pot raporta niveluri de satisfacție "
        "radical diferite, chiar cu aceleași condiții obiective de muncă.\n"
        "✅ Leagă satisfacția de percepția subiectivă, nu de faptele brute — construcția "
        "mentală a angajatului contează la fel de mult ca realitatea obiectivă.\n\n"
        "❌ Distincția așteptări-realitate nu anulează rolul valorilor personale în "
        "teoria lui Locke — valorile rămân fundația percepției satisfacției."
    ),

    # 280 | Fluctuație #26 — perechi componente experiență la muncă
    (
        "Primele trei perechi descriu corect componentele experienței la muncă legate "
        "de satisfacție.\n\n"
        "✅ Evaluarea afectivă surprinde starea emoțională față de job — dacă munca "
        "este trăită ca plăcută sau neplăcută, îmbogățitoare sau epuizantă.\n"
        "✅ Așteptările reflectă ce credea angajatul că va obține din job înainte de "
        "angajare — o componentă cognitivă a satisfacției.\n"
        "✅ Realitatea percepută descrie ce oferă efectiv rolul — sarcini, colegi, "
        "mediu sau beneficii, filtrate prin percepție subiectivă.\n\n"
        "❌ Turnover-ul involuntar este un rezultat comportamental potențial legat de "
        "satisfacție, nu o componentă a experienței de muncă în sine."
    ),

    # 281 | Fluctuație #27 — Locke: ce susține satisfacția
    (
        "Conform teoriei lui Locke, satisfacția muncii este susținută atunci când "
        "există o aliniere reală între valorile personale ale angajatului și ceea ce "
        "oferă munca.\n\n"
        "✅ Munca care permite trăirea valorilor personale importante (realizare, "
        "autonomie, echitate, creativitate etc.) generează o evaluare afectivă pozitivă.\n"
        "✅ Un job care se aliniază cu ce contează pentru angajat creează un sentiment "
        "de sens și relevanță personală a muncii.\n\n"
        "❌ Un salariu mediu cu valori încălcate zilnic nu susține satisfacția — "
        "contradicția valorilor produce disonanță, nu satisfacție.\n"
        "❌ Localizarea sediului central al organizației nu este o variabilă în teoria "
        "satisfacției a lui Locke."
    ),

    # 282 | Fluctuație #28 — satisfacție ≠ fericire permanentă la birou
    (
        "Clarificarea pedagogică corectă pentru confundarea satisfacției cu fericirea "
        "permanentă include trei nuanțări.\n\n"
        "✅ Satisfacția muncii este o evaluare afectivă relativ stabilă față de job, "
        "nu o stare de euforie continuă — poate coexista cu momente de frustrare sau "
        "dificultate zilnică.\n"
        "✅ Include și componenta cognitivă a comparației dintre așteptări și ce oferă "
        "efectiv jobul — nu este exclusiv o stare emoțională.\n"
        "✅ Poate coexista cu performanță bună sau slabă — satisfacția și performanța "
        "sunt constructe corelate, dar distincte și independente.\n\n"
        "❌ Salariul decent nu garantează satisfacție — alți factori (promovare, "
        "natura muncii, relații interpersonale) pot genera insatisfacție chiar cu "
        "remunerare acceptabilă."
    ),

    # 283 | Fluctuație #29 — dimensiunile satisfacției muncii
    (
        "Evaluarea satisfacției muncii include mai multe dimensiuni distincte, iar "
        "toate cele patru opțiuni corespund unor categorii recunoscute în literatura "
        "de specialitate. "
        "Salariul (Pay) și perspectivele de promovare (Promotion) vizează remunerarea "
        "și oportunitățile de avansare în carieră. "
        "Beneficiile (Benefits) și recompensele contingente (Contingent Rewards) reflectă "
        "satisfacția față de avantajele non-salariale și față de legătura efort-recompensă. "
        "Colegii (Coworkers), supervizarea (Supervision) și natura muncii în sine (Work "
        "Itself) vizează relațiile interpersonale și conținutul intrinsec al sarcinilor. "
        "Procedurile interne (Policies) și comunicarea organizațională completează tabloul "
        "contextual al satisfacției."
    ),

    # 284 | Fluctuație #30 — promovarea = cel mai puternic predictor al intenției de plecare
    (
        "Cercetarea indică că promovarea (Promotion) — percepția șanselor de avansare "
        "și a blocajelor de carieră — este adesea cel mai puternic predictor individual "
        "al intenției de plecare dintre dimensiunile satisfacției muncii. "
        "Lipsa perspectivei de creștere profesională generează frustrare pe termen lung "
        "și poate iniția procesul descris în modelul retragerii. "
        "Salariul (Pay) este important, dar poate fi compensat parțial de alți factori; "
        "blocajul de carieră perceput este mai dificil de compensat și acționează mai "
        "persistent și profund asupra intenției de plecare."
    ),

    # 285 | Fluctuație #31 — „nu văd șanse să cresc» = promovare afectată
    (
        "Angajatul care declară că „plătesc ok, colegii sunt buni, dar nu văd nicio șansă să cresc» "
        "semnalează clar insatisfacția față de dimensiunea promovare "
        "(Promotion). "
        "Mesajul evidențiază percepția unui blocaj de carieră — lipsa oportunităților "
        "de avansare sau de dezvoltare profesională în cadrul organizației. "
        "Salariul și colegii par satisfăcători, deci dimensiunile Pay și Coworkers nu "
        "sunt afectate. "
        "Blocajul de carieră perceput este unul dintre predictorii cei mai robuști ai "
        "intenției de plecare, conform cercetării."
    ),

    # 286 | Fluctuație #32 — distincții dimensiuni satisfacție
    (
        "Primele trei afirmații descriu corect relațiile dintre dimensiunile satisfacției.\n\n"
        "✅ Pay (salariu) = satisfacția față de remunerare — cât și cât de corect este "
        "plătit angajatul față de contribuția sa și față de piață.\n"
        "✅ Work Itself (natura muncii) = cât de interesante, variate și semnificative "
        "sunt sarcinile zilnice — dimensiunea cu cel mai mare spill-over spre viața "
        "personală.\n"
        "✅ Supervision (supervizare) = calitatea relației cu șeful direct, suportul "
        "perceput și stilul de conducere al acestuia.\n\n"
        "❌ Promotion (promovare) nu înseamnă numărul de zile de concediu legal — "
        "concediul legal ține de beneficiile contractuale, nu de avansarea în carieră."
    ),

    # 287 | Fluctuație #33 — recompense contingente
    (
        "Recompensele contingente (Contingent Rewards) se referă la percepția că "
        "performanța mai bună este recompensată în mod corect și direct.\n\n"
        "✅ Percepția că cei care muncesc mai mult sau mai bine primesc recompense "
        "corespunzătoare (bonusuri, recunoaștere, avansare) este nucleul acestei "
        "dimensiuni a satisfacției.\n"
        "✅ Legătura dintre efort sau rezultate și recompensele primite reflectă "
        "echitatea percepută a sistemului de recompensare — factor motivațional central.\n\n"
        "❌ Beneficiile fixe din contract, identice pentru toți, nu sunt recompense "
        "contingente — ele nu variază în funcție de performanța individuală.\n"
        "❌ Numărul de zile de concediu medical plătit este un beneficiu de sănătate, "
        "nu o recompensă legată de performanță."
    ),

    # 288 | Fluctuație #34 — dimensiuni relații interpersonale
    (
        "Dimensiunile satisfacției legate cel mai direct de relațiile interpersonale "
        "la locul de muncă sunt cele care implică interacțiuni sociale regulate.\n\n"
        "✅ Colegii (Coworkers) reflectă satisfacția față de calitatea relațiilor "
        "cu colegii de echipă, colaborarea și suportul informal din grup.\n"
        "✅ Supervizarea (Supervision) reflectă satisfacția față de relația cu "
        "șeful direct — sprijin, comunicare, corectitudine și competența liderului.\n"
        "✅ Comunicarea organizațională influențează climatul de muncă și percepția "
        "de transparență și respect în relațiile cu organizația.\n\n"
        "❌ Procedurile contabile sunt procese tehnice fără componentă socială directă "
        "și nu aparțin dimensiunilor interpersonale ale satisfacției."
    ),

    # 289 | Fluctuație #35 — de ce promovarea prezice mai bine decât salariul
    (
        "Promovarea poate prezice mai bine intenția de plecare decât salariul din "
        "motive psihologice profunde legate de sens și identitate.\n\n"
        "✅ Lipsa perspectivei de creștere poate genera frustrare cumulativă pe termen "
        "lung, chiar dacă salariul este acceptabil — angajatul poate tolera o plată "
        "medie dacă vede viitor, dar nu va tolera blocajul de carieră la nesfârșit.\n"
        "✅ Promovarea ține de sens, status și dezvoltare personală — nevoi de nivel "
        "mai profund decât tranzacția monetară imediată.\n"
        "✅ Percepția blocajului de carieră alimentează exact etapele din modelul "
        "retragerii: insatisfacție față de promovare, urmate de gânduri de plecare.\n\n"
        "❌ Salariul nu contează niciodată pentru intenția de plecare este o afirmație "
        "falsă — salariul rămâne un factor relevant, chiar dacă nu este mereu cel mai "
        "puternic predictor."
    ),

    # 290 | Fluctuație #36 — asociere dimensiune cu exemplu
    (
        "Primele trei exemple asociază corect o declarație cu dimensiunea "
        "corespunzătoare a satisfacției muncii.\n\n"
        "✅ „Sarcinile mele sunt variate și îmi folosesc competențele» — corespunde "
        "dimensiunii Work Itself (natura muncii), care vizează cât de interesante "
        "și semnificative sunt sarcinile.\n"
        "✅ „Regulile interne sunt clare și corecte» — corespunde dimensiunii Policies "
        "(proceduri), care reflectă percepția corectitudinii și transparenței "
        "organizaționale.\n"
        "✅ „Cei care muncesc mai mult sunt recompensați corect» — corespunde "
        "dimensiunii Contingent Rewards, care vizează legătura efort-recompensă.\n\n"
        "❌ Cunoașterea exactă a salariului colegilor din alt departament nu corespunde "
        "direct niciuneia dintre dimensiunile clasice ale satisfacției — este mai "
        "degrabă un element de percepție a echității comparative."
    ),

    # 291 | Fluctuație #37 — afirmație falsă: salariul e mereu cel mai puternic predictor
    (
        "Afirmația că salariul (Pay) este întotdeauna cel mai puternic predictor al "
        "intenției de plecare, înaintea promovării (Promotion), este falsă. "
        "Cercetarea empirică arată că promovarea — percepția șanselor de avansare "
        "și a blocajelor de carieră — prezice adesea mai puternic intenția de plecare "
        "decât salariul. "
        "Salariul poate fi tolerat dacă există perspective clare de creștere; "
        "sentimentul de stagnare profesională poate eroda motivația chiar și la o "
        "remunerare satisfăcătoare. "
        "Nu există o singură dimensiune universal dominantă — ierarhia predictorilor "
        "variază între industrii, culturi și profiluri de angajați."
    ),

    # 292 | Fluctuație #38 — combinații de dimensiuni care explică insatisfacție generalizată
    (
        "Insatisfacția generalizată este cel mai plauzibil explicată de combinații "
        "de dimensiuni care acoperă mai multe surse de nemulțumire simultane.\n\n"
        "✅ Supervizare toxică, lipsă de promovare și proceduri percepute ca injuste "
        "formează o combinație puternică: relația cu șeful este distrugătoare, cariera "
        "este blocată și sistemul pare nedrept.\n"
        "✅ Beneficii decente combinate cu muncă monotonă și fără sens perceput "
        "ilustrează că recompensele extrinseci nu compensează lipsa satisfacției "
        "intrinseci față de natura muncii.\n\n"
        "❌ Work Itself captivant, colegi cooperanți și comunicare clară descriu un "
        "context de satisfacție, nu de insatisfacție generalizată.\n"
        "❌ Pay excelent, promovare clară și supervizare suportivă reprezintă condiții "
        "favorabile satisfacției, nu surse de insatisfacție."
    ),

    # 293 | Fluctuație #39 — TF: satisfacție–performanță pozitivă dar modestă (ADEVĂRAT)
    (
        "Adevărat. Meta-analizele confirmă că satisfacția muncii și performanța sunt "
        "corelate pozitiv, dar relația este moderată — nu garantată și nu automată. "
        "Există angajați mulțumiți care nu performează la potențial maxim și angajați "
        "care performează bine din alte motive (presiune externă, standard personal, "
        "profesionalism) fără a fi neapărat satisfăcuți. "
        "Performanța depinde și de abilități, resurse, claritatea sarcinii și context "
        "organizațional — nu doar de starea afectivă față de job."
    ),

    # 294 | Fluctuație #40 — legătura satisfacție–performanță: varianta fidelă cercetării
    (
        "Legătura satisfacție-performanță este descrisă cel mai fidel prin existența "
        "unei relații pozitive moderate, cu influența unor factori moderatori.\n\n"
        "✅ Există o relație pozitivă, dar de obicei moderată — satisfacția contribuie "
        "la performanță, dar nu o determină singură.\n"
        "✅ Performanța depinde și de alți factori (abilități, resurse, claritatea "
        "sarcinii, feedback) care nu sunt captați de satisfacție.\n\n"
        "❌ Fericirea la job nu garantează automat productivitate maximă — relația "
        "nu este deterministă.\n"
        "❌ Performanța ridicată nu elimină orice nemulțumire — angajații pot performa "
        "bine și totuși fi nemulțumiți de alte dimensiuni ale jobului."
    ),

    # 295 | Fluctuație #41 — spill-over și cross-over: definiții corecte
    (
        "Spill-over și cross-over descriu mecanisme diferite de transfer al stării "
        "afective sau al satisfacției.\n\n"
        "✅ Spill-over = transferul are loc în interiorul aceleiași persoane — stresul "
        "sau satisfacția de la muncă se transferă în starea de spirit din viața "
        "personală și invers.\n"
        "✅ Cross-over = transferul are loc între două persoane diferite (de obicei "
        "parteneri sau colegi apropiați) — starea afectivă a unuia influențează starea "
        "celuilalt.\n\n"
        "❌ Spill-over nu descrie transferul de la soț la angajat — acela este "
        "cross-over.\n"
        "❌ Cross-over nu se referă la fluctuația între departamente — acela este "
        "transfer organizațional intern, un concept complet diferit."
    ),

    # 296 | Fluctuație #42 — TF: spill-over = transfer între două persoane (FALS)
    (
        "Fals. Definiția din afirmație descrie cross-over-ul, nu spill-over-ul. "
        "Spill-over descrie transferul stării afective sau al satisfacției în cadrul "
        "aceleiași persoane, de la un domeniu al vieții la altul — de exemplu, stresul "
        "de la locul de muncă se transferă în starea de spirit de acasă. "
        "Cross-over-ul este fenomenul interpersonal: starea afectivă a unei persoane "
        "influențează starea altei persoane cu care interacționează (partener, coleg). "
        "Confundarea celor două mecanisme este o greșeală frecventă și un subiect "
        "tipic de capcană la examen."
    ),

    # 297 | Fluctuație #43 — Work Itself = cel mai mare spill-over spre viața personală
    (
        "Natura muncii în sine (Work Itself) este dimensiunea satisfacției cu cel mai "
        "puternic spill-over documentat spre satisfacția vieții personale. "
        "Aceasta reflectă cât de interesante, stimulatoare și semnificative sunt "
        "sarcinile zilnice — o experiență care se extinde natural dincolo de birou "
        "în starea generală de bine a angajatului. "
        "Beneficiile (Benefits) și procedurile (Policies) au un impact mai restrâns "
        "și mai puțin emoțional, generând mai puțin spill-over. "
        "Recompensele contingente izolate de sensul muncii nu produc același transfer "
        "afectiv profund."
    ),

    # 298 | Fluctuație #44 — Work Itself bun + pay slab → spill-over pozitiv
    (
        "Situația descrisă — Work Itself ridicat combinat cu salariu slab — exemplifică "
        "mecanismul de spill-over pozitiv.\n\n"
        "✅ Satisfacția față de natura muncii poate susține parțial starea de bine "
        "personală a angajatului, chiar dacă o altă dimensiune (Pay) este "
        "nesatisfăcătoare.\n"
        "✅ Plăcerea de a face munca se poate transfera în energie și dispoziție "
        "pozitivă dincolo de birou — angajatul se simte bine în general din cauza "
        "sarcinilor semnificative, chiar cu salariu mic.\n\n"
        "❌ Salariul slab nu anulează complet orice spill-over pozitiv — dimensiunile "
        "satisfacției sunt relativ independente.\n"
        "❌ Cross-over nu garantează că partenerul va fi și el mulțumit la job — "
        "cross-over transmite starea afectivă, nu satisfacția față de jobul propriu "
        "al partenerului."
    ),

    # 299 | Fluctuație #45 — soția stresată, el tensionat = cross-over
    (
        "Fenomenul descris — angajatul devine tensionat acasă din cauza stresului "
        "soției, deși la jobul său nimic nu s-a schimbat — este un exemplu clasic de "
        "cross-over. "
        "Cross-over-ul descrie transferul stării afective între persoane diferite "
        "dintr-un sistem social apropiat (familie, echipă). "
        "Stresul soției a traversat granița interpersonală și a influențat starea "
        "emoțională a angajatului fără ca vreo cauză de la locul lui de muncă să fie "
        "implicată. "
        "Nu este spill-over (care ar fi transferul intra-personal, de la jobul "
        "angajatului la viața lui personală), nici turnover disfuncțional, nici "
        "sindrom hobo."
    ),

    # 300 | Fluctuație #46 — exemple spill-over și cross-over
    (
        "Exemplele de spill-over și cross-over pot fi clasificate clar după direcția "
        "și natura transferului afectiv.\n\n"
        "✅ Stresul de la job care afectează dispoziția acasă — spill-over: transferul "
        "are loc în aceeași persoană, de la domeniul muncii la domeniul personal.\n"
        "✅ Nemulțumirea partenerului care influențează și propria stare — cross-over: "
        "transferul are loc între două persoane diferite.\n"
        "✅ Starea de bine de la job care îmbunătățește seara acasă — spill-over "
        "pozitiv: aceeași persoană, transfer pozitiv de la muncă la viața personală.\n\n"
        "❌ Plecarea de la firma A la firma B este turnover, nu spill-over sau "
        "cross-over."
    ),

    # 301 | Fluctuație #47 — de ce satisfacția nu justifică „fericit = performanță explodează»
    (
        "Concluzia că satisfacția maximă produce automat performanță maximă este "
        "contrazisă de mai mulți factori.\n\n"
        "✅ Corelația satisfacție-performanță este modestă — relația există, dar este "
        "departe de o cauzalitate directă și completă.\n"
        "✅ Performanța depinde și de abilități, resurse și claritatea sarcinii — "
        "un angajat fericit, dar fără abilitățile necesare sau fără resurse adecvate, "
        "nu va performa la potențial maxim.\n"
        "✅ Unii angajați pot fi mulțumiți cu munca minimă necesară — satisfacția nu "
        "produce neapărat motivație pentru excelență.\n\n"
        "❌ Satisfacția și performanța nu sunt aceeași măsurătoare cu alt nume — sunt "
        "constructe distincte, cu predictori și consecințe parțial diferite."
    ),

    # 302 | Fluctuație #48 — de ce Work Itself are spill-over puternic
    (
        "Natura muncii în sine (Work Itself) produce un spill-over puternic spre "
        "viața personală din două motive fundamentale.\n\n"
        "✅ Plăcerea de a face munca se transferă în stare generală de bine — sarcinile "
        "interesante și semnificative alimentează o emoție pozitivă care nu se oprește "
        "la ușa biroului.\n"
        "✅ Work Itself este o dimensiune centrală a experienței zilnice a angajatului, "
        "nu un avantaj marginal sau ocazional — impactul ei este constant și profund.\n\n"
        "❌ Work Itself nu transferă satisfacția între două persoane diferite — acela "
        "este cross-over.\n"
        "❌ Beneficiile nu anulează efectul Work Itself — dimensiunile satisfacției "
        "sunt relativ independente ca predictori ai stării de bine."
    ),

    # 303 | Fluctuație #49 — angajament afectiv: definiție
    (
        "Angajamentul afectiv (affective commitment) descrie legătura emoțională dintre "
        "angajat și organizație — o identificare pozitivă care motivează rămânerea.\n\n"
        "✅ Angajatul rămâne pentru că vrea și se identifică cu misiunea, cultura și "
        "valorile organizației — nu din calcul sau obligație.\n"
        "✅ Implică o implicare emoțională autentică față de firmă, nu o simplă "
        "conformare la contract sau prezență din inerție.\n\n"
        "❌ A rămâne doar pentru că nu există oferte alternative descrie angajamentul "
        "de continuare (continuance commitment), nu cel afectiv.\n"
        "❌ A rămâne pentru că șeful are autoritate formală descrie conformare la "
        "autoritate, nu identificare emoțională cu organizația."
    ),

    # 304 | Fluctuație #50 — consecințe ale angajamentului afectiv ridicat
    (
        "Cercetarea identifică trei consecințe asociate în mod consistent cu "
        "angajamentul afectiv ridicat.\n\n"
        "✅ Performanță mai bună — angajații care se identifică cu organizația sunt "
        "mai motivați să contribuie activ și să depună efort discreționnar.\n"
        "✅ Turnover mai scăzut — legătura emoțională cu firma reduce probabilitatea "
        "de a căuta și accepta alternative de angajare.\n"
        "✅ Comportament de cetățenie organizațională (OCB) mai frecvent — angajamentul "
        "afectiv crește disponibilitatea de a ajuta voluntar colegi și organizație.\n\n"
        "❌ Absențele nemotivate nu sunt asociate pozitiv cu angajamentul afectiv — "
        "dimpotrivă, angajamentul ridicat reduce absenteismul."
    ),

    # 305 | Fluctuație #51 — satisfacție vs angajament organizațional
    (
        "Satisfacția muncii și angajamentul organizațional sunt constructe înrudite, "
        "dar distincte.\n\n"
        "✅ Satisfacția ține de evaluarea afectivă a muncii sau a jobului — o judecată "
        "despre cât de plăcute sau corespunzătoare sunt sarcinile, salariul, colegii etc.\n"
        "✅ Angajamentul ține de legătura cu organizația ca întreg — identificarea "
        "cu valorile, misiunea și cultura firmei, dincolo de sarcinile zilnice.\n"
        "✅ Angajamentul afectiv implică „vreau să rămân în această organizație», nu "
        "doar „îmi place sarcina de azi» — este o atitudine față de firmă, nu față "
        "de job.\n\n"
        "❌ Satisfacția și angajamentul nu sunt mereu identice ca măsură — pot coexista "
        "diverse combinații între ele, inclusiv satisfacție ridicată cu angajament "
        "scăzut."
    ),

    # 306 | Fluctuație #52 — îi place munca dar ar pleca = satisfacție bună, angajament scăzut
    (
        "Situația angajatului care iubește munca zilnică dar ar pleca pentru orice "
        "alt angajator similar reflectă o combinație specifică.\n\n"
        "✅ Satisfacție față de muncă relativ ridicată — îi plac sarcinile, activitățile "
        "și conținutul rolului, ceea ce este o evaluare pozitivă a jobului.\n"
        "✅ Angajament afectiv față de organizație probabil scăzut — nu se simte legat "
        "emoțional de firma actuală în mod specific, ci de tipul de muncă.\n"
        "✅ Risc de turnover dacă apare o alternativă atractivă — loialitatea este "
        "față de profesie sau tipul de muncă, nu față de angajatorul actual.\n\n"
        "❌ Nu are angajament afectiv ridicat — satisfacția față de sarcini nu implică "
        "automat identificare emoțională cu organizația."
    ),

    # 307 | Fluctuație #53 — afirmație falsă: continuance = afectiv
    (
        "Afirmația că angajamentul de continuare (continuance) este același lucru cu "
        "angajamentul afectiv este falsă. "
        "Angajamentul de continuare se bazează pe calculul costurilor asociate plecării "
        "— angajatul rămâne pentru că nu are alternative sau pentru că costul plecării "
        "(pierderea beneficiilor, incertitudinea) este prea mare. "
        "Angajamentul afectiv se bazează pe identificare emoțională și dorința autentică "
        "de a rămâne în organizație. "
        "Cele două tipuri de angajament au predictori diferiți, relații diferite cu "
        "performanța și consecințe distincte pentru comportamentul angajatului."
    ),

    # 308 | Fluctuație #54 — lanț cauzal insatisfacție → plecare
    (
        "Lanțurile cauzale coerente cu materia despre insatisfacție și plecare sunt "
        "primele două.\n\n"
        "✅ Insatisfacția față de promovarea blocată generează intenție de plecare, "
        "care la rândul ei prezice turnover-ul efectiv — lanț direct și bine susținut "
        "empiric.\n"
        "✅ Insatisfacția urmată de gânduri de plecare și căutare de joburi alternative "
        "corespunde exact etapelor din modelul retragerii (Withdrawal Model).\n\n"
        "❌ Angajamentul afectiv ridicat nu garantează turnover disfuncțional — "
        "dimpotrivă, este asociat cu mai puțin turnover.\n"
        "❌ Satisfacția ridicată nu produce intenție de plecare maximă — relația "
        "este inversă: satisfacție mare reduce intenția de plecare."
    ),

    # 309 | Fluctuație #55 — satisfacție, angajament, comportament organizațional
    (
        "Relațiile corecte dintre satisfacție, angajament și comportamentul "
        "organizațional sunt primele, a doua și a patra.\n\n"
        "✅ Angajamentul afectiv ridicat este asociat cu mai mult OCB și mai puțin "
        "turnover — un angajat care vrea să rămână contribuie mai mult voluntar.\n"
        "✅ Satisfacția față de muncă nu garantează automat angajament față de firmă "
        "— sunt constructe distincte care pot varia independent.\n"
        "✅ Promovarea percepută influențează satisfacția și poate alimenta intenția "
        "de plecare prin mecanismul modelului retragerii.\n\n"
        "❌ Nu toți angajații mulțumiți au automat angajament afectiv maxim — relația "
        "este pozitivă, dar nu determinată și nu universală."
    ),

    # 310 | Fluctuație #56 — sinteză: perechi corecte
    (
        "Perechile de concepte corect asociate în sinteză sunt primele trei.\n\n"
        "✅ Turnover disfuncțional — pleacă performanții valoroși, ceea ce este cel "
        "mai problematic pentru organizație.\n"
        "✅ Intenția de plecare — cel mai bun predictor individual al turnover-ului "
        "efectiv, conform meta-analizelor.\n"
        "✅ Spill-over — transferul intra-personal al stării afective, de la muncă "
        "la viața personală sau invers.\n\n"
        "❌ Cross-over nu este transfer în aceeași persoană fără influență interpersonală "
        "— exact opusul: cross-over descrie transferul interpersonal, între persoane "
        "diferite."
    ),

    # 311 | Fluctuație #57 — scenarii combinate din capitol
    (
        "Primele trei scenarii combină corect mai multe idei din capitol.\n\n"
        "✅ Nemulțumire față de promovare care declanșează căutare de job, intenție "
        "și demisie urmează fidel secvența modelului retragerii.\n"
        "✅ Work Itself plăcut care generează spill-over pozitiv spre viața personală "
        "ilustrează mecanismul dimensiunii centrale a satisfacției.\n"
        "✅ Angajament afectiv ridicat care produce mai mult OCB și retenție mai bună "
        "reflectă consecințele documentate ale angajamentului afectiv.\n\n"
        "❌ Turnover funcțional înseamnă că pleacă cei cu performanță slabă, nu "
        "performanții valoroși — când pleacă cei mai valoroși, vorbim despre turnover "
        "disfuncțional."
    ),

    # 312 | Fluctuație #58 — intervenții HR pentru reducerea turnover disfuncțional
    (
        "Intervențiile pentru reducerea turnover-ului disfuncțional cel mai bine "
        "ancorate în cercetare sunt primele trei.\n\n"
        "✅ Clarificarea căilor de promovare și dezvoltare răspunde direct celei mai "
        "puternice surse de insatisfacție și intenție de plecare la angajații valoroși.\n"
        "✅ Îmbunătățirea supervizării și a climatului organizațional adresează "
        "dimensiunile Supervision și Coworkers ale satisfacției, puternic legate "
        "de decizia de a rămâne.\n"
        "✅ Monitorizarea intenției de plecare prin sondaje permite HR-ului să "
        "intervină înainte ca intenția să se transforme în plecare efectivă.\n\n"
        "❌ Ignorarea satisfacției pe motiv că performanța e mereu legată perfect de "
        "ea este o eroare — relația este pozitivă, dar modestă, și nu justifică "
        "ignorarea factorilor de satisfacție."
    ),

    # 313 | Fluctuație #59 — afirmații-capcană care trebuie respinse
    (
        "Toate cele patru afirmații sunt capcane — enunțuri plauzibile dar greșite "
        "ce trebuie respinse la examen.\n\n"
        "❌ „Fericit la job = automat performant maxim» — relația este pozitivă, dar "
        "modestă, și nu permite această generalizare deterministă.\n"
        "❌ „Spill-over = influență între două persoane diferite» — acela este "
        "cross-over; spill-over este transferul intra-personal.\n"
        "❌ „Turnover funcțional = pleacă cei mai buni performanți» — tocmai invers: "
        "turnover-ul disfuncțional implică plecarea performanților valoroși.\n"
        "❌ „Satisfacția = angajament organizațional — același construct» — sunt "
        "constructe distincte cu obiect diferit: jobul vs organizația."
    ),

    # 314 | Fluctuație #60 — rezumat corect capitol fluctuație & satisfacție
    (
        "Toate cele patru afirmații rezumă corect capitolul despre fluctuație și "
        "satisfacția muncii.\n\n"
        "✅ Satisfacția muncii = evaluare afectivă (și cognitivă) a jobului sau a "
        "dimensiunilor sale — fundament al teoriei lui Locke și al modelelor de "
        "predicție a turnover-ului.\n"
        "✅ Angajamentul afectiv = dorința autentică de a rămâne în organizație, "
        "derivată din identificare emoțională cu valorile și misiunea firmei.\n"
        "✅ Intenția de plecare = cel mai bun predictor individual al turnover-ului "
        "efectiv, capturând etapa pre-plecare din modelul retragerii.\n"
        "✅ Promovarea percepută = adesea predictorul cel mai puternic al intenției "
        "de plecare dintre dimensiunile satisfacției muncii."
    ),

    # ══════════════════════════════════════════════════════
    # VALUE FIT & STRES — 36 itemi (indici globali 315–350)
    # ══════════════════════════════════════════════════════

    # 315 | Value Fit #1 — TF: Value Fit = aliniere valori individ–organizație (ADEVĂRAT)
    (
        "Adevărat. Potrivirea valorilor (Value Fit) descrie gradul în care valorile "
        "personale ale angajatului sunt aliniate cu valorile promovate și practicate "
        "de organizație. "
        "Cercetările arată că o potrivire bună a valorilor este asociată cu satisfacție "
        "mai ridicată, angajament afectiv mai mare, performanță mai bună și intenție "
        "de plecare mai scăzută. "
        "Dimpotrivă, un mismatch valoric persistent — când angajatul apreciază "
        "autonomia și transparența, dar firma promovează ierarhia și secretul — "
        "generează disonanță cognitivă, stres și dezangajament progresiv."
    ),

    # 316 | Value Fit #2 — afirmații corecte despre Value Fit
    (
        "Primele trei afirmații despre potrivirea valorilor sunt corecte.\n\n"
        "✅ Value Fit descrie alinierea valorilor individuale cu valorile organizației "
        "— nucleul conceptului, distinct de alte forme de potrivire persoană-job.\n"
        "✅ O potrivire bună este asociată cu satisfacție și angajament mai ridicate — "
        "angajatul găsește sens și identitate în munca sa.\n"
        "✅ O potrivire bună este asociată cu turnover mai scăzut și performanță mai "
        "bună — consecințe documentate empiric în meta-analize.\n\n"
        "❌ Value Fit nu înseamnă același lucru cu potrivirea abilităților tehnice la "
        "job — aceea este o altă dimensiune a potrivirii persoană-job (Person-Job Fit "
        "pe competențe), nu potrivire de valori."
    ),

    # 317 | Value Fit #3 — TF: valorile = convingeri, nu aptitudini (ADEVĂRAT)
    (
        "Adevărat. Valorile, în sens organizațional și psihologic, sunt convingeri "
        "despre ce este important, demn de urmărit și dezirabil — nu sunt abilități "
        "cognitive (capacități de procesare) sau trăsături de personalitate "
        "(tendințe comportamentale stabile). "
        "Valorile ghidează prioritățile și judecățile evaluative ale individului, "
        "influențând alegerea carierei, comportamentul organizațional și nivelul de "
        "satisfacție față de muncă. "
        "De exemplu, valorile de autonomie, echitate sau realizare personală sunt "
        "convingeri despre ce merită urmărit, nu tendințe emoționale sau cognitive."
    ),

    # 318 | Value Fit #4 — distincții: valori vs abilități vs trăsături vs emoții
    (
        "Valorile trebuie distinse clar de alte constructe psihologice pentru a evita "
        "confuzia conceptuală.\n\n"
        "✅ Valorile = convingeri despre ce consider important — autonomie, echitate, "
        "realizare, securitate — un sistem de priorități care ghidează deciziile.\n"
        "✅ Abilitățile = capacități de a face ceva cognitiv sau motor — ce pot face "
        "efectiv, nu ce consider important sau dezirabil.\n"
        "✅ Trăsăturile de personalitate = tendințe relativ stabile de comportament "
        "și experiență (ex. extraversiunea, conștiinciozitatea din Big Five).\n"
        "✅ Emoțiile = stări afective trecătoare legate de un eveniment specific — "
        "nu un sistem de convingeri stabil."
    ),

    # 319 | Value Fit #5 — angajat pro-transparență vs firmă competitivă = value fit scăzut
    (
        "Situația descrisă ilustrează două consecințe directe ale potrivirii slabe "
        "a valorilor.\n\n"
        "✅ Potrivire slabă a valorilor (Value Fit scăzut) — angajatul apreciază "
        "transparența și colaborarea, iar firma promovează competiția internă ascunsă "
        "și secretul; acesta este un mismatch valoric evident și semnificativ.\n"
        "✅ Risc de insatisfacție și angajament scăzut pe termen lung — mismatching "
        "valoric este o sursă de stres psihologic și disonanță cognitivă, ce erodează "
        "satisfacția și angajamentul.\n\n"
        "❌ Nu este o problemă de lipsă de abilități tehnice — angajatul are valori "
        "personale incompatibile cu cultura firmei, nu un deficit de competențe.\n"
        "❌ Groupthink nu este aplicabil direct în acest scenariu — descrie gândirea "
        "de grup necritică, nu conflictul de valori individ-organizație."
    ),

    # 320 | Value Fit #6 — afirmație falsă: valorile = trăsături Big Five
    (
        "Afirmația că valorile sunt identice cu trăsăturile de personalitate Big Five "
        "este falsă. "
        "Modelul Big Five (Openness, Conscientiousness, Extraversion, Agreeableness, "
        "Neuroticism) descrie tendințe relativ stabile de comportament și experiență — "
        "nu convingeri despre ce este important sau dezirabil. "
        "Valorile sunt sisteme de credințe evaluative despre ce merită urmărit (ex. "
        "autonomie, echitate, securitate, putere) — conceptual distincte de trăsăturile "
        "de personalitate, deși pot interacționa cu acestea. "
        "Un individ conștiincios poate valoriza fie ordinea rigidă, fie realizarea "
        "creativă — trăsătură și valoare sunt constructe separate."
    ),

    # 321 | Value Fit #7 — de ce value fit contează dincolo de salariu
    (
        "Potrivirea valorilor contează dincolo de salariu sau beneficii din motive "
        "profunde legate de sens și identitate la locul de muncă.\n\n"
        "✅ Valorile definesc sensul și etica percepută a muncii — fără o potrivire "
        "valorică, munca poate părea goală de sens, chiar cu beneficii materiale bune.\n"
        "✅ Mismatching valoric poate genera disonanță cognitivă și, pe termen lung, "
        "burnout din cauza epuizării resurselor emoționale necesare pentru a acționa "
        "contrar propriilor convingeri.\n"
        "✅ Angajamentul afectiv este mai ușor de susținut când valorile personale "
        "coincid cu valorile organizației — identificarea emoțională cu firma este "
        "facilitată de alinierea valorică.\n\n"
        "❌ Salariul nu anulează complet orice conflict de valori — pe termen lung, "
        "disonanța valorică erodează satisfacția și angajamentul chiar cu remunerare "
        "bună."
    ),

    # 322 | Value Fit #8 — afirmație exagerată: value fit măsurat exclusiv prin aptitudini
    (
        "Afirmația că value fit se măsoară exclusiv prin teste de aptitudine "
        "profesională este exagerată și greșită. "
        "Testele de aptitudine profesională evaluează abilitățile cognitive sau "
        "motorii necesare pentru a îndeplini sarcinile unui post — nu convingerile "
        "despre ce este important sau dezirabil. "
        "Potrivirea valorilor se evaluează prin instrumente specifice, cum ar fi "
        "chestionarele de valori (ex. bazate pe modelul Schwartz), compararea "
        "profilurilor de valori ale candidaților cu cele ale organizației sau ale "
        "angajaților existenți. "
        "Aptitudinea profesională și value fit sunt constructe diferite cu metode "
        "de măsurare diferite."
    ),

    # 323 | Value Fit #9 — valorile Schwartz: perechi din cele zece tipuri
    (
        "Modelul lui Shalom Schwartz propune zece tipuri de valori fundamentale "
        "umane, organizate circular pe două axe.\n\n"
        "✅ Autodirecționarea (independența în gândire și acțiune) și universalismul "
        "(protejarea bunăstării tuturor și a mediului) sunt valori din modelul Schwartz.\n"
        "✅ Puterea (dominanța socială și controlul) și realizarea (succesul personal "
        "prin competență) sunt alte două tipuri din model.\n"
        "✅ Bunăvoința (grija față de apropiați) și conformitatea (respectarea regulilor "
        "sociale) completează setul de valori Schwartz.\n\n"
        "❌ Extraversiunea și neuroticismul sunt factori de personalitate din modelul "
        "Big Five, nu valori din sistemul Schwartz — o confuzie frecventă la examen."
    ),

    # 324 | Value Fit #10 — valori hedonism și stimulare Schwartz
    (
        "Valorile de hedonism și stimulare din modelul Schwartz sunt orientate spre "
        "plăcere și căutarea de noutate.\n\n"
        "✅ Hedonismul descrie valori centrate pe plăcere și satisfacere senzorială "
        "imediată — căutarea bunăstării și confortului personal.\n"
        "✅ Stimularea descrie valori centrate pe noutate, provocare și varietate — "
        "dorința de a experimenta lucruri noi și excitante.\n\n"
        "❌ Respectul pentru obiceiuri și credințe consacrate corespunde valorii de "
        "tradiție din modelul Schwartz, nu hedonismului sau stimulării.\n"
        "❌ Siguranța, stabilitatea și ordinea corespund valorii de securitate, care "
        "este opusă pe cercul lui Schwartz față de stimulare."
    ),

    # 325 | Value Fit #11 — valori Schwartz asociate cu siguranță și ordine
    (
        "În modelul circular al lui Schwartz, valorile orientate spre siguranță și "
        "ordine socială formează un cluster specific.\n\n"
        "✅ Securitatea descrie dorința de siguranță personală, familială și socială "
        "— stabilitate și protecție față de amenințări.\n"
        "✅ Conformitatea descrie orientarea spre respectarea regulilor și a normelor "
        "sociale, evitând comportamentele care perturbă ordinea.\n"
        "✅ Tradiția descrie respectul și acceptarea obiceiurilor, ideilor și "
        "credințelor consacrate — continuitate culturală și socială.\n\n"
        "❌ Autodirecționarea descrie independența în gândire și acțiune — este "
        "opusă față de conformitate pe cercul valorilor, nu asociată cu ordinea."
    ),

    # 326 | Value Fit #12 — rolul socializării organizaționale față de valori
    (
        "Socializarea organizațională joacă un rol important în raport cu valorile "
        "angajaților noi.\n\n"
        "✅ Ajută angajații noi să învețe normele, comportamentele așteptate și "
        "cultura firmei — transmițând implicit valorile organizaționale prin interacțiuni "
        "sociale zilnice.\n"
        "✅ Poate crește potrivirea valorilor pe măsură ce angajatul internalizează "
        "valorile organizaționale prin modele de rol și feedback social.\n"
        "✅ Include mecanisme concrete de transmitere a culturii: onboarding structurat, "
        "mentorat, modele de rol și ritualuri organizaționale.\n\n"
        "❌ Socializarea nu înlocuiește complet valorile personale — poate influența "
        "comportamentul și interpretările, dar valorile profunde sunt relativ stabile "
        "și persistente."
    ),

    # 327 | Value Fit #13 — afirmații corecte despre socializarea organizațională
    (
        "Socializarea organizațională are funcții clare legate de transmiterea culturii "
        "și alinierea valorică.\n\n"
        "✅ Ajută angajații să învețe „modul nostru de a face lucrurile» — normele "
        "implicite, așteptările și comportamentele valorizate în organizație.\n"
        "✅ Poate crește alinierea cu valorile firmei — prin expunere repetată la "
        "modele de rol și prin feedback social din partea colegilor mai experimentați.\n"
        "✅ Include mecanisme diverse: mentorat formal și informal, onboarding "
        "structurat, participare la ritualuri organizaționale.\n\n"
        "❌ Socializarea nu înlocuiește complet valorile personale ale angajatului — "
        "valorile adânc înrădăcinate rămân, chiar dacă comportamentul se adaptează "
        "la contextul organizațional."
    ),

    # 328 | Value Fit #14 — aculturația organizațională
    (
        "Aculturația organizațională descrie un proces de adaptare la o cultură "
        "organizațională nouă, diferită de cea cu care angajatul era familiarizat.\n\n"
        "✅ Presupune adaptare la o cultură organizațională diferită — norme, valori "
        "și practici noi față de ce cunoștea angajatul.\n"
        "✅ Implică de obicei păstrarea parțială a valorilor proprii, fără abandon "
        "total — angajatul se adaptează la noul context fără să-și piardă identitatea "
        "valorică fundamentală.\n"
        "✅ Este un proces analog adaptării culturale la nivel societal, dar aplicat "
        "intrării într-o firmă cu cultură distinctivă.\n\n"
        "❌ Aculturația nu presupune renunțarea obligatorie la toate valorile personale "
        "la angajare — o cerință atât de drastică ar fi nerealistă și ar genera "
        "rezistență, nu integrare."
    ),

    # 329 | Value Fit #15 — specialist român în multinațională = aculturație
    (
        "Situația specialistului român care adoptă protocoalele locale, păstrând "
        "valoarea autonomiei, descrie un proces de adaptare cu păstrarea parțială "
        "a identității valorice.\n\n"
        "✅ Adaptare la cultura nouă fără abandon total al valorilor proprii — "
        "angajatul adoptă comportamente noi (protocoale ierarhice), fără a renunța "
        "la ceea ce consideră fundamental (autonomia).\n"
        "✅ Învățarea normelor și culturii firmei face parte din socializarea "
        "organizațională — proces prin care angajatul înțelege așteptările culturale "
        "ale noului angajator.\n\n"
        "❌ Presiunea de conformitate necritică ar implica abandonarea valorilor "
        "proprii fără adaptare activă — scenariul descrie o adaptare inteligentă.\n"
        "❌ Fluctuația repetată de la un job la altul descrie sindromul hobo, nu "
        "aculturația organizațională."
    ),

    # 330 | Value Fit #16 — shared values: beneficii și risc de groupthink
    (
        "Valorile comune într-o echipă au atât beneficii, cât și riscuri specifice.\n\n"
        "✅ Groupthink — gândirea de grup necritică — este principalul risc al "
        "valorilor prea omogene: membrii echipei evită disensul, nu contestă decizii "
        "riscante și supraestimează capacitatea colectivă de a judeca corect.\n"
        "✅ Pierderea diversității de perspective este un risc complementar: o echipă "
        "cu valori identice tinde să genereze mai puțin gândire critică și soluții "
        "mai uniforme.\n\n"
        "❌ Valorile comune nu garantează performanță indiferent de realitate — "
        "facilitează cooperarea, dar nu elimină necesitatea competenței și resurselor.\n"
        "❌ Turnover-ul funcțional nu apare automat ca urmare a valorilor comune."
    ),

    # 331 | Value Fit #17 — scenariu groupthink
    (
        "Groupthink este ilustrat cel mai bine de situațiile în care gândirea critică "
        "este suprimată de presiunea de consens.\n\n"
        "✅ Echipa care evită să conteste o decizie riscantă pentru că „suntem toți de acord» "
        "— aceasta este esența groupthink: coeziunea grupului blochează "
        "evaluarea realistă a alternativelor.\n"
        "✅ Consensul obținut prin presiune socială, nu prin analiză — un alt simptom "
        "al groupthink: membrii cedează presiunii sociale, nu convingerii argumentate.\n\n"
        "❌ Valorile comune care reduc conflicte inutile, dacă se păstrează gândire "
        "critică, sunt benefice — nu orice acord este groupthink.\n"
        "❌ Un nou membru al cărui punct de vedere diferit este ascultat și integrat "
        "descrie exact opusul groupthink-ului — diversitate sănătoasă."
    ),

    # 332 | Value Fit #18 — valori Schwartz orientate spre transcenderea interesului propriu
    (
        "În modelul circular al lui Schwartz, valorile orientate spre transcenderea "
        "interesului propriu grupează valorile care pun binele celorlalți și al "
        "planetei deasupra avantajului personal.\n\n"
        "✅ Universalismul descrie înțelegerea, toleranța și protejarea bunăstării "
        "tuturor oamenilor și a naturii — cea mai largă formă de orientare prosocială.\n"
        "✅ Bunăvoința descrie grija față de bunăstarea persoanelor apropiate — "
        "familie, prieteni, colegi — o orientare prosocială mai focalizată.\n\n"
        "❌ Puterea și realizarea sunt valori orientate spre promovarea interesului "
        "propriu, nu spre transcenderea lui — se află pe latura opusă a cercului "
        "valorilor Schwartz."
    ),

    # 333 | Value Fit #19 — afirmație falsă: socializarea obligă la abandon total de valori
    (
        "Afirmația că socializarea organizațională obligă la abandonul total al "
        "valorilor personale este falsă. "
        "Socializarea organizațională este procesul prin care un angajat nou învață "
        "normele, comportamentele așteptate și cultura firmei — un proces de adaptare "
        "și învățare, nu de înlocuire completă a identității valorice. "
        "Aculturația organizațională presupune adaptare parțială: angajatul adoptă "
        "comportamente și înțelege așteptările noii culturi, păstrând în același "
        "timp valorile personale profunde. "
        "Cererea de abandon total ar fi nerealistă și ar genera mai degrabă tensiune "
        "și rezistență decât integrare autentică."
    ),

    # 334 | Value Fit #20 — asociere concepte cu descrieri (value fit, socializare, aculturație, shared values)
    (
        "Toate cele patru opțiuni asociază corect conceptul cu descrierea "
        "corespunzătoare din capitolul Value Fit.\n\n"
        "✅ Alinierea între valorile personale și cele ale organizației — definiția "
        "directă a Value Fit.\n"
        "✅ Învățarea culturii și normelor firmei — descrierea procesului de "
        "socializare organizațională.\n"
        "✅ Adaptare la o cultură nouă, păstrând parțial valorile proprii — descrierea "
        "aculturației organizaționale.\n"
        "✅ Valori comune ce pot crește coeziunea, dar și groupthink — descrierea "
        "funcțiilor și riscurilor shared values."
    ),

    # 335 | Stres #21 — TF: stresul = reacție la cerințe > resurse (ADEVĂRAT)
    (
        "Adevărat. Stresul la locul de muncă este definit în psihologia organizațională "
        "ca o reacție psihologică și fiziologică care apare atunci când cerințele "
        "percepute depășesc resursele disponibile ale individului pentru a le face față. "
        "Cheia definiției este cuvântul percepute — stresul nu este determinat de "
        "evenimentul obiectiv în sine, ci de modul în care individul îl evaluează "
        "în raport cu propriile resurse. "
        "De aceea, aceeași situație obiectivă poate produce niveluri diferite de stres "
        "la persoane diferite, în funcție de resursele și experiența fiecăruia."
    ),

    # 336 | Stres #22 — definiție stres la muncă
    (
        "Stresul la locul de muncă este înțeles cel mai complet prin combinarea "
        "mai multor elemente definitorii.\n\n"
        "✅ Reacție la dezechilibrul cerințe mai mari decât resursele disponibile — "
        "nucleul definiției moderne a stresului organizațional.\n"
        "✅ Depinde de evaluarea subiectivă a individului, nu doar de evenimentul "
        "obiectiv — același deadline poate stresa un angajat și motiva altul.\n"
        "✅ Include atât componente fiziologice (activare hormonală, tensiune), cât "
        "și psihologice (anxietate, frustrare, epuizare emoțională).\n\n"
        "❌ Nu orice sarcină dificilă produce automat stres identic la toți — "
        "diferențele individuale în resurse, experiență și evaluare cognitivă "
        "modulează răspunsul la stres."
    ),

    # 337 | Stres #23 — GAS Selye: ordinea corectă alarmă → rezistență → epuizare
    (
        "În sindromul general de adaptare (GAS) descris de Hans Selye, ordinea "
        "corectă a celor trei etape este: alarmă, urmată de rezistență, urmată de "
        "epuizare. "
        "Faza de alarmă este răspunsul inițial al organismului la agentul stresor — "
        "activarea fiziologică rapidă (reacția de luptă-sau-fugă). "
        "Faza de rezistență reprezintă adaptarea activă a organismului la stresorul "
        "persistent — aparent lucrurile par sub control, dar resursele sunt consumate "
        "treptat. "
        "Faza de epuizare apare dacă stresorul continuă mai mult decât resursele "
        "adaptative pot susține — duce la deteriorarea sănătății și la burnout."
    ),

    # 338 | Stres #24 — etapele GAS: descrieri corecte
    (
        "Etapele sindromului general de adaptare (GAS) al lui Selye sunt descrise "
        "corect de primele trei opțiuni.\n\n"
        "✅ Reacția inițială la agentul stresor — faza de alarmă: activare fiziologică "
        "acută, eliberarea de hormoni de stres.\n"
        "✅ Adaptarea temporară a organismului — faza de rezistență: mobilizarea "
        "resurselor pentru a face față stresorului persistent.\n"
        "✅ Epuizarea resurselor dacă stresul persistă — faza de epuizare: "
        "vulnerabilitate crescută la boli și burnout.\n\n"
        "❌ Absența totală a oricărei reacții fiziologice nu corespunde niciunei "
        "etape din GAS — Selye a descris tocmai implicarea profundă a sistemului "
        "fiziologic în răspunsul la orice stresor."
    ),

    # 339 | Stres #25 — P–E Fit explică stresul prin nepotrivire
    (
        "Modelul potrivirii persoană-mediu (Person-Environment Fit) explică stresul "
        "prin nepotrivirea dintre caracteristicile individului și mediul de muncă.\n\n"
        "✅ Nepotrivirea între caracteristicile persoanei (valori, abilități, preferințe) "
        "și mediul de muncă (cerințe, cultură, resurse) generează tensiune și stres.\n"
        "✅ Mismatching poate apărea la mai multe niveluri: cerințe față de abilități, "
        "valori față de cultura organizației, preferințe față de caracteristicile "
        "jobului.\n"
        "✅ Stresul crește atunci când mediul nu corespunde cu persoana — o metaforă "
        "care surprinde intuiția de bază a modelului P-E Fit.\n\n"
        "❌ Stresul nu este zero când mediul este oricât de solicitant, dacă există "
        "potrivire — P-E Fit reduce stresul legat de nepotrivire, dar nu poate "
        "elimina orice sursă de stres."
    ),

    # 340 | Stres #26 — introvertit cu rol de vânzări = P–E Fit slab
    (
        "Situația introvertitului cu rol de vânzări agresiv în open-space zgomotos "
        "poate fi explicată prin două cadre teoretice complementare.\n\n"
        "✅ Potrivire persoană-mediu (P-E Fit) slabă — caracteristicile individului "
        "(preferință pentru liniște, structură) nu corespund cerințelor și contextului "
        "jobului (interacțiuni intense, mediu stimulant și zgomotos).\n"
        "✅ Cerințe mai mari decât resursele percepute — rolul impune comportamente "
        "care nu vin natural pentru un introvertit, epuizând resursele de energie "
        "socială mai rapid decât pentru un extravertit.\n\n"
        "❌ Value fit perfect nu este relevant în acest scenariu — nu sunt menționate "
        "valorile organizaționale, ci incompatibilitatea stilului personal cu cerințele "
        "rolului.\n"
        "❌ Tipul B de comportament nu poate fi dedus din simpla preferință pentru "
        "liniște și structură."
    ),

    # 341 | Stres #27 — capcană: stresul e identic cu evenimentul (FALS)
    (
        "Afirmația că stresul este identic cu evenimentul stresor și că toți "
        "reacționează la fel este o capcană clasică de examen — este falsă. "
        "Stresul nu este evenimentul extern în sine, ci reacția subiectivă a "
        "individului la acel eveniment, în funcție de evaluarea cerințelor față "
        "de resursele disponibile. "
        "Aceeași sarcină obiectivă (un deadline strâns, o prezentare publică) poate "
        "fi percepută ca provocare stimulatoare de un angajat cu resurse suficiente "
        "și ca amenințare copleșitoare de altul cu resurse sau experiență mai limitate. "
        "Natura subiectivă și relațională a stresului este esențială pentru "
        "înțelegerea variabilității individuale a răspunsurilor."
    ),

    # 342 | Stres #28 — de ce epuizarea GAS e periculoasă la stres cronic
    (
        "Epuizarea din cadrul sindromului general de adaptare (GAS) este periculoasă "
        "la stres cronic din motive legate de suprasolicitarea sistemului adaptativ.\n\n"
        "✅ Resursele de adaptare se epuizează pe termen lung — organismul nu poate "
        "menține la nesfârșit mobilizarea din faza de rezistență.\n"
        "✅ Poate apărea burnout sau probleme de sănătate fizică și psihică — boli "
        "cardiovasculare, tulburări imunitare și epuizare emoțională, documentate "
        "empiric.\n"
        "✅ Legătura cu absențe, erori și performanță scăzută la locul de muncă — "
        "epuizarea reduce concentrația, motivația și eficiența.\n\n"
        "❌ După epuizare, organismul nu devine automat mai rezistent — dimpotrivă, "
        "vulnerabilitatea crește dacă stresorul continuă."
    ),

    # 343 | Stres #29 — perechi cerințe–resurse în stres
    (
        "Relația cerințe-resurse în stres este descrisă corect de trei perechi.\n\n"
        "✅ Cerințe mari și resurse mici produc stres ridicat — relația de bază "
        "din modelele cerere-resurse.\n"
        "✅ Resursele includ nu doar competențe personale, ci și sprijin social, "
        "controlul asupra modului de lucru și acces la informații — resurse atât "
        "personale, cât și organizaționale.\n"
        "✅ Aceeași cerință obiectivă poate stresa diferit în funcție de resursele "
        "disponibile — confirmând caracterul subiectiv și relațional al stresului.\n\n"
        "❌ Cerințele nu sunt doar evenimente externe, fără interpretare — evaluarea "
        "cognitivă a cerințelor (primară Lazarus) joacă un rol crucial în definirea "
        "lor ca stresori cu impact diferit."
    ),

    # 344 | Stres #30 — TF: rezistența GAS = adaptare temporară, urmată de epuizare (ADEVĂRAT)
    (
        "Adevărat. Faza de rezistență din sindromul general de adaptare (GAS) al "
        "lui Selye reprezintă adaptarea activă a organismului la un stresor persistent. "
        "În această fază, individul pare că face față situației — poate continua să "
        "lucreze, să funcționeze relativ normal și să gestioneze cerințele stresoare. "
        "Totuși, această adaptare are un cost: resursele fiziologice și psihologice "
        "sunt consumate treptat. "
        "Dacă stresorul continuă dincolo de capacitatea de rezistență a individului, "
        "urmează faza de epuizare — cu consecințe grave pentru sănătate și performanță."
    ),

    # 345 | Stres #31 — legătura value fit și stres
    (
        "Relația dintre value fit și stres este susținută de trei conexiuni teoretice "
        "și empirice corecte.\n\n"
        "✅ Value fit scăzut poate fi o sursă de stres psihologic — conflictul zilnic "
        "dintre valorile personale și practicile organizaționale generează disonanță "
        "cognitivă și epuizare emoțională.\n"
        "✅ Modelul P-E Fit include și potrivirea valorilor cu cultura organizației "
        "— mismatching valoric este o formă de nepotrivire persoană-mediu care crește "
        "stresul.\n"
        "✅ Conflictul de valori poate epuiza resursele emoționale pe termen lung — "
        "a acționa zilnic contrar propriilor valori este costisitor psihologic.\n\n"
        "❌ Value fit ridicat nu elimină orice stres legat de volumul de muncă — "
        "potrivirea valorică reduce un tip de stres identitar, dar nu stresul generat "
        "de supraîncărcarea cu sarcini sau presiunea de timp."
    ),

    # 346 | Stres #32 — arc alarmă→rezistență→epuizare = GAS Selye
    (
        "Arcul descris — alarmă la restructurare, adaptare parțială (rezistență), "
        "cedare după luni de incertitudine (epuizare) — corespunde fidel sindromului "
        "general de adaptare (GAS) al lui Hans Selye. "
        "Selye a descris GAS ca un răspuns stereotip al organismului la orice stresor "
        "prelungit, indiferent de natura acestuia: restructurare organizațională, boală "
        "sau conflict personal. "
        "Modelul cerere-control (Karasek) se concentrează pe structura jobului, nu pe "
        "secvența adaptativă biologică. "
        "Evaluarea cognitivă (Lazarus) explică modul de interpretare a stresorului, "
        "nu secvența fiziologică. "
        "Modelul Schwartz descrie valori fundamentale umane, nu răspunsul la stres."
    ),

    # 347 | Stres #33 — Karasek: stres maxim la cerințe mari + control mic
    (
        "Modelul cerere-control (Demand-Control) al lui Robert Karasek identifică "
        "combinația de cerințe mari și control scăzut ca principala sursă de stres "
        "maxim la locul de muncă.\n\n"
        "✅ Cerințele psihologice mari (volum ridicat de muncă, presiune de timp, "
        "complexitate cognitivă) sunt primul factor al stresului în modelul Karasek.\n"
        "✅ Controlul sau autonomia redusă — lipsa posibilității de a decide cum, când "
        "și cu ce mijloace să îndeplești sarcinile — este al doilea factor, care "
        "amplifică efectul cerințelor.\n\n"
        "❌ Cerințele mici și controlul mare descriu un job pasiv — plictisitor, dar "
        "nu maxim stresant.\n"
        "❌ Cerințele mari și controlul mare descriu un job activ — potențial stimulant "
        "și motivant, nu neapărat maxim stresant."
    ),

    # 348 | Stres #34 — Karasek: jobul activ (cerințe mari + control mare)
    (
        "Jobul cu cerințe mari și control mare (activ) în modelul Karasek reprezintă "
        "o combinație specifică cu efecte mai ambigue decât jobul stresant clasic.\n\n"
        "✅ Descrie o muncă solicitantă, dar cu autonomie în modul de lucru — "
        "angajatul poate gestiona cerințele ridicate prin flexibilitate și adaptare.\n"
        "✅ Poate fi stimulatoare și motivantă, nu neapărat maxim stresantă — "
        "autonomia atenuează parțial efectul negativ al cerințelor mari.\n\n"
        "❌ Cerințele mici și controlul mic descriu un job pasiv — alt cadran al "
        "modelului, nu jobul activ.\n"
        "❌ Cerințele mari și controlul mic — jobul cel mai stresant conform Karasek "
        "— este un alt cadran, opus față de jobul activ descris."
    ),

    # 349 | Stres #35 — Lazarus: evaluarea primară = „e amenințătoare sau benefică?»
    (
        "În teoria evaluării cognitive a lui Richard Lazarus, evaluarea primară "
        "răspunde la întrebarea: „Este această situație amenințătoare, dăunătoare sau benefică pentru mine?» "
        "Aceasta este prima etapă de procesare a informației stresante — o judecată "
        "rapidă despre relevanța personală a evenimentului. "
        "Evaluarea secundară răspunde la o altă întrebare: „Am resursele necesare pentru a face față acestei situații?» "
        "— și este distinctă de evaluarea primară. "
        "Emoția apare ca o consecință a acestor evaluări, nu ca evaluare primară în "
        "sine, iar atribuirea vinei este un pas ulterior, separat."
    ),

    # 350 | Stres #36 — ordinea logică în Lazarus: primar→secundar→coping
    (
        "Ordinea logică în modelul evaluării cognitive al lui Lazarus parcurge trei "
        "etape distincte, corect descrise de primele trei opțiuni.\n\n"
        "✅ Prima etapă — evaluarea primară — răspunde la: „Această situație este periculoasă sau benefică?» "
        "Dacă evenimentul este evaluat ca amenințător "
        "sau ca o provocare, procesul continuă.\n"
        "✅ A doua etapă — evaluarea secundară — răspunde la: „Am resursele necesare pentru a face față?» "
        "Dacă resursele par insuficiente, nivelul de stres crește.\n"
        "✅ A treia etapă — alegerea strategiei de coping — angajatul decide cum va "
        "gestiona situația: coping centrat pe problemă sau pe emoție.\n\n"
        "❌ Evaluarea secundară nu precede percepția și evaluarea inițială a "
        "evenimentului — succesiunea corectă este: evaluare primară, evaluare secundară, "
        "coping."
    ),
]

assert len(PART3_EXPLANATIONS) == 117
