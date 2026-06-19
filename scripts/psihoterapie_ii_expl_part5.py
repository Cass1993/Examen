"""Explicații Psihoterapie II — partea 5 (index 427–526, exam 7428–7527).

Conținut:
  427–436  behaviorism items 51–60 (comparativ & controverse)
  437–496  tehnici comportamentale (toate 60)
  497–526  CBT Ellis & Beck items 1–30
"""

from __future__ import annotations

from typing import List

PART5_EXPLANATIONS: List[str] = [
    # ── 0–9  Behaviorism items 51–60 (comparativ & controverse) ───────────────
    # 0  item 51 — Pavlov: paradigma condiționării clasice la animale
    "Ivan P. Pavlov a studiat reflexele condiționate la câini în laborator de fiziologie, fără scopul inițial de a trata pacienți. Behaviorismul clinic aplicat a venit mai târziu, prin Watson, Eysenck și alții.",
    # 1  item 52 — Watson: controversa etică Little Albert
    "Experimentul Little Albert (1920) a fost condus de John B. Watson și Rosalie Rayner; controversele etice vizează absența decondiționării finale, ceea ce face ca Watson să fie autorul asociat direct cu această controversă.",
    # 2  item 53 — Skinner: Walden Two
    "B.F. Skinner a scris romanul „Walden Two» (1948) și ulterior „Beyond Freedom and Dignity» (1971), în care propunea o utopie fondată pe control comportamental planificat al societății.",
    # 3  item 54 — condiționare operantă vs. clasică
    "Condiționarea operantă (Skinner) vizează consecințele unui comportament emis voluntar; condiționarea clasică (Pavlov) asociază doi stimuli — un stimul neutru cu un reflex necondiționat. Dacă scopul este creșterea frecvenței unui comportament prin consecințe, paradigma skinneriana este cea potrivită.",
    # 4  item 55 — biofeedback: Neal E. Miller
    "Neal E. Miller a demonstrat că răspunsurile autonome (frecvența cardiacă, tensiunea arterială) pot fi controlate voluntar prin biofeedback — feedback vizual sau sonor care permite condiționarea operantă a unor răspunsuri fiziologice.",
    # 5  item 56 — perechi greșite: Pavlov ≠ cutia Skinner
    "Cutia Skinner (Skinner chamber) aparține lui B.F. Skinner, nu lui Ivan P. Pavlov. Pavlov a studiat reflexul salivar, nu contingențele de întărire. Perechea „Pavlov — cutia Skinner» este, prin urmare, greșită.",
    # 6  item 57 — tranziția Watson → Eysenck
    "Watson a formulat manifestul behaviorismului (1913), propunând o psihologie fără introspectie. Hans J. Eysenck a dus mai departe ideea: a evaluat empiric protocoale de intervenție comportamentală și a demonstrat eficacitatea lor clinică, marcând trecerea de la polemică la practică clinică.",
    # 7  item 58 — Pavlov vs. Skinner: distincție fundamentală
    "La Pavlov, stimulul condiționat elicitează un reflex — răspunsul este pasiv. La Skinner, organismul emite comportamentul, iar consecințele îl modelează. Distincția: reflex elicitat (condiționare clasică) vs. comportament operant emis și urmat de consecință.",
    # 8  item 59 — behaviorism comun tuturor autorilor
    "Toți autorii menționați (Dollard–Miller, Watson, Skinner) resping introspectia ca metodă și pun comportamentul observabil în centrul studiului. Diferențele apar în accent: contingențe, drive-uri, aplicații clinice — dar premisa empirică este comună.",
    # 9  item 60 — pluralitatea contribuțiilor behavioriste
    "Afirmația este corectă: fiecare autor a aplicat ideile behavioriste pe un domeniu specific. Pavlov și Watson — condiționare clasică; Skinner — operantă; Dollard și Miller — drive-uri și frustrare; Eysenck — terapie și personalitate; Krumboltz — carieră.",

    # ── 10–69  Tehnici comportamentale (items 1–60) ───────────────────────────
    # —— Desensibilizare sistematică & expunere (10–21) ——
    # 10  DS1 — definiție
    "Desensibilizarea sistematică, elaborată de Joseph Wolpe, combină relaxarea cu expunerea graduală la stimuli anxiogeni. Principiul: răspunsul de relaxare este incompatibil cu anxietatea (contracondiționare), astfel încât parcurgerea ierarhiei reduce treptat reacția de frică.",
    # 11  DS2 — mecanism teoretic
    "Mecanismul invocat este contracondiționarea: relaxarea profundă și anxietatea nu pot coexista simultan (inhibiție reciprocă). Prin asocierea relaxării cu stimulii anxiogeni în ordine gradată, răspunsul de frică este treptat inhibat.",
    # 12  DS3 — ierarhia de anxietate
    "Ierarhia de anxietate este o listă construită colaborativ, ordonând situațiile de la cel mai puțin la cel mai anxiogen. Ea ghidează expunerea graduală astfel încât clientul să nu depășească capacitatea de relaxare la fiecare treaptă.",
    # 13  DS4 — flooding vs. DS
    "Flooding-ul (inundarea) diferă de desensibilizarea sistematică prin expunere intensă și imediată la stimulul maxim fobic, fără ierarhie și fără relaxare prealabilă. Mecanismul propus este extincția prin absența consecințelor temute.",
    # 14  DS5 — expunere in vivo
    "Expunerea în vivo presupune confruntarea reală cu situația evitată — nu imaginată sau simbolică. Este o componentă centrală a terapiei comportamentale pentru fobii și are eficacitate empirică superioară expunerii exclusiv imaginare.",
    # 15  DS6 — caz fobie lift
    "Parcurgerea treptelor din imagini ușoare spre situații mai dificile, asociată cu relaxare, definește desensibilizarea sistematică cu ierarhie gradată — tehnica fondată de Joseph Wolpe pentru tratamentul fobiilor.",
    # 16  DS7 — imaginar vs. in vivo
    "Desensibilizarea prin imaginație utilizează descrieri verbale sau vizualizări controlate ale stimulilor fobici, fără prezență fizică. Este utilă ca prim pas sau atunci când expunerea reală nu este imediat posibilă.",
    # 17  DS8 — pași clasici (abc)
    "Desensibilizarea sistematică clasică include obligatoriu trei pași: antrenarea relaxării (ex. relaxare progresivă Jacobson), construirea ierarhiei de anxietate și expunerea graduată cu relaxare asociată.",
    # 18  DS9 — de ce este comportamentală
    "Tehnica este comportamentală deoarece modifică asocierile stimul–răspuns prin proceduri structurate și replicabile, reduce evitarea și urmărește schimbarea comportamentului observabil, nu insight-ul inconștient.",
    # 19  DS10 — DS ≠ orice expunere
    "Nu orice expunere este desensibilizare sistematică. DS presupune ierarhie gradată și relaxare asociată (contracondiționare). Flooding-ul presupune expunere intensă imediată, fără ierarhie sau relaxare prealabilă — mecanismul său este extincția.",
    # 20  DS11 — Eysenck și desensibilizarea
    "Hans J. Eysenck a susținut și promovat terapia comportamentală pentru anxietate în Europa, popularizând desensibilizarea sistematică ca alternativă eficientă la psihoterapia psihanalitică de lungă durată, cu evaluare empirică a rezultatelor.",
    # 21  DS12 — progres condiționat de scăderea anxietății
    "Logica desensibilizării sistematice cere ca trecerea la treapta următoare să se facă doar după ce clientul atinge relaxare la nivelul actual — principiul inhibiției reciproce: anxietatea trebuie să scadă la fiecare treaptă înainte de avansare.",

    # —— Relaxare (22–31) ——
    # 22  R1 — relaxare musculară Jacobson
    "Relaxarea musculară progresivă (Edmund Jacobson) constă în tensionarea deliberată și relaxarea secvențială a grupurilor musculare. Scopul este conștientizarea și reducerea tonusului muscular excesiv asociat anxietății.",
    # 23  R2 — rolul relaxării în DS
    "În desensibilizarea sistematică, relaxarea funcționează ca răspuns incompatibil cu anxietatea, după principiul inhibiției reciproce. Relaxarea adâncă face imposibilă menținerea anxietății în prezența stimulului anxiogen imaginar.",
    # 24  R3 — antrenament sistematic vs. simpla calmare
    "Relaxarea comportamentală este o procedură antrenată, replicabilă și măsurabilă (tonus muscular, ritm cardiac). Nu este simpla „calmare» spontană, ci un răspuns condiționat care poate fi invocat sistematic în situații anxiogene.",
    # 25  R4 — autogenic training
    "Antrenamentul autogen (Johannes Schultz) și relaxarea progresivă (Jacobson) reduc ambele activarea fiziologică prin proceduri repetate și auto-instrucțiuni, diferind în metodologie: autogenicul folosește sugestii despre greutate și căldură; Jacobson — tensionare–relaxare musculară.",
    # 26  R5 — respirație → DS
    "Antrenarea respirației diafragmatice înainte de parcurgerea ierarhiei reflectă logica desensibilizării sistematice: mai întâi se consolidează răspunsul incompatibil cu anxietatea (relaxarea), apoi se începe expunerea graduată.",
    # 27  R6 — relaxare singură, fără expunere
    "Relaxarea singură, fără expunere graduată, poate reduce tensiunea generală și este benefică pentru stresul cotidian, dar nu adresează evitarea specifică și nu dezactivează răspunsul condiționat de frică față de stimulul fobic.",
    # 28  R7 — biofeedback
    "Biofeedback-ul, asociat cu Neal E. Miller, extinde relaxarea prin furnizarea unui feedback vizual sau sonor al răspunsului fiziologic (puls, tensiune musculară), permițând clientului să învețe controlul voluntar al răspunsurilor autonome.",
    # 29  R8 — afirmații corecte (abd)
    "Relaxarea comportamentală: poate fi componentă a desensibilizării sistematice (a), antrenează un răspuns fiziologic alternativ anxietății (b) și poate fi măsurată obiectiv prin tonus muscular sau ritm cardiac (d). Varianta c — „înlocuiește obligatoriu expunerea» — este greșită.",
    # 30  R9 — protocoale combinate
    "Protocoalele care combină relaxare, ierarhie de anxietate și expunere gradată respectă logica desensibilizării sistematice clasice — tehnica fondată de Joseph Wolpe, în care fiecare element are un rol precis.",
    # 31  R10 — relaxare ≠ hipnoză
    "Relaxarea musculară progresivă este o procedură structurată de auto-control muscular, bazată pe tensionare–relaxare conștientă. Hipnoza clinică implică sugestie și stare alterată de conștiință. Cele două sunt diferite ca mecanism și indicații.",

    # —— Tehnica aversivă (32–41) ——
    # 32  A1 — definiție
    "Tehnica aversivă asociază un comportament nedorit cu un stimul neplăcut (fizic, chimic sau imaginar), reducând frecvența comportamentului prin condiționare de aversiune — bazată pe condiționarea clasică sau pe penalizare operantă.",
    # 33  A2 — aversivă ≠ DS
    "Tehnica aversivă urmărește reducerea unui comportament nedorit prin consecințe neplăcute, nu reducerea fricii față de un stimul extern. Desensibilizarea sistematică urmărește reducerea fricii față de un stimul prin contracondiționare cu relaxare.",
    # 34  A3 — controverse etice
    "Controversele etice ale tehnicii aversive vizează: consimțământul informat al clientului, proporționalitatea stimulului aversiv față de problema tratată și riscul de efecte secundare (traumatizare, generalizare nedorită).",
    # 35  A4 — întărire negativă ≠ aversivă
    "Întărirea negativă (Skinner) crește frecvența unui comportament prin eliminarea unui stimul neplăcut — este un mecanism de creștere a comportamentului adaptiv. Tehnica aversivă penalizează un comportament nedorit — este un mecanism de reducere.",
    # 36  A5 — exemplu clasic
    "Asocierea consumului de alcool cu un medicament care produce greață (ex. disulfiram) este un exemplu de condiționare aversivă chimică — alcoolul devine stimul condiționat pentru disconfort, reducând motivația de a bea.",
    # 37  A6 — de ce este comportamentală
    "Tehnica aversivă este comportamentală deoarece modifică probabilitatea comportamentului prin consecințe contingente — relația directă comportament–stimul neplăcut, fără explorarea inconștientului.",
    # 38  A7 — față de întăriri pozitive
    "Față de întărirea pozitivă, tehnica aversivă pune accent pe reducerea unui comportament nedorit prin consecințe neplăcute, nu pe creșterea unui comportament adaptiv prin recompensă. Abordările contemporane preferă, de regulă, întărirea pozitivă.",
    # 39  A8 — exemple (abd)
    "Time-out (eliminarea întăririi sociale — b), aversiunea chimică (a) și costul răspuns (pierderea privilegiilor — d) reduc comportamentul prin consecințe neplăcute sau absența recompensei. Desensibilizarea sistematică (c) vizează fobia, nu reducerea unui comportament nedorit.",
    # 40  A9 — aversivă ≠ pedeapsă arbitrară
    "Tehnica aversivă în context terapeutic urmează un protocol planificat cu obiective clare, consimțământ informat și monitorizare etică profesională. Nu este o pedeapsă arbitrară; distincția este esențială din perspectivă deontologică.",
    # 41  A10 — nu prima alegere în fobii
    "În fobii, prima alegere terapeutică este expunerea graduală sau flooding-ul, care adresează direct anxietatea și evitarea. Tehnica aversivă ar penaliza comportamentul de frică, ceea ce nu este o abordare etică sau eficace pentru fobii.",

    # —— Modelare (42–53) ——
    # 42  M1 — definiție
    "Modelarea este o tehnică de achiziție a comportamentului prin observarea unui model care execută comportamentul țintă. Clientul nu trebuie să fie direct întărit; observarea și imitarea sunt suficiente pentru achiziție (Albert Bandura).",
    # 43  M2 — Bandura: învățare observațională
    "Albert Bandura a extins modelarea cu teoria învățării observaționale: eficacitatea depinde de patru procese — atenția la model, reținerea comportamentului, reproducerea motorie și motivația sau auto-eficacitatea (self-efficacy).",
    # 44  M3 — modelare participativă
    "Modelarea participativă presupune că clientul nu observă pasiv, ci practică treptat comportamentul alături de model, beneficiind de sprijin și feedback imediat — metodă eficace mai ales în fobii și antrenamentul abilităților.",
    # 45  M4 — in vivo vs. simbolică
    "Modelarea în vivo implică prezența fizică a unui model real; modelarea simbolică utilizează filme, descrieri verbale sau joc de rol. Ambele pot fi eficace, dar modelarea în vivo permite feedback imediat și contact social real.",
    # 46  M5 — caz copil
    "Urmărind părintele care se spală pe mâini și imitând comportamentul, copilul dobândește o competență prin observare și imitare — mecanism central al modelării, descris de Albert Bandura ca învățare observațională.",
    # 47  M6 — modelare ≠ întărire directă
    "Modelarea permite achiziția unui comportament fără trial-and-error individual — comportamentul este observat la altul. Întărirea directă modelează comportamentul existent prin consecințe. Modelarea este mai eficace când comportamentul nu există în repertoriul clientului.",
    # 48  M7 — abilități sociale
    "În antrenamentul de abilități sociale, modelarea oferă un exemplu concret al comportamentului țintă (ex. asertivitate, abilități de interviu), permițând clientului să observe înainte de a practica, reducând anxietatea de performanță.",
    # 49  M8 — self-efficacy
    "Self-efficacy (Bandura) — convingerea că poți executa comportamentul — mediază eficacitatea modelării. Un model cu competențe similare clientului poate crește self-efficacy mai mult decât un model expert, facilitând reproducerea comportamentului.",
    # 50  M9 — modelare + DS
    "Combinarea modelării cu desensibilizarea este eficace: terapeutul modelează calm în situația fobică, demonstrând că nu există pericol, iar clientul imită treptat — modelare participativă cu expunere progresivă.",
    # 51  M10 — afirmații corecte (abd)
    "Modelarea este vizibilă în învățarea observațională (a), utilă în antrenamentul abilităților sociale (b) și poate include model viu, film sau rol jucat (d). Varianta c — „identică cu relaxarea progresivă» — este greșită.",
    # 52  M11 — modelare ≠ sugestie hipnotică
    "Modelarea se bazează pe observare conștientă și reproducere deliberată a comportamentului, nu pe stare alterată de conștiință sau sugestii hipnotice. Cele două mecanisme sunt radical diferite.",
    # 53  M12 — token economy + modelare
    "În token economy, modelarea poate fi folosită pentru a demonstra comportamentul țintă înainte ca clientul să execute — văzând consecințele pozitive obținute de model, clientul este motivat să imite comportamentul.",

    # —— Modificarea comportamentului (54–63) ——
    # 54  MC1 — definiție
    "Modificarea comportamentului desemnează aplicarea sistematică a principiilor derivate din psihologia experimentală (condiționare, întărire, extincție, modelare) pentru a schimba comportamente observabile și măsurabile.",
    # 55  MC2 — token economy
    "Token economy este un program de modificare comportamentală în care jetoanele simbolice funcționează ca întăritori secundari, schimbabili cu privilegii sau recompense. Comportamentele țintă sunt întărite imediat și sistematic.",
    # 56  MC3 — shaping
    "Shaping-ul constă în întărirea progresivă a oricărui comportament care se apropie de cel țintă. Este util pentru achiziția de comportamente noi, complexe, care nu există în repertoriul inițial al clientului.",
    # 57  MC4 — analiza funcțională ABC
    "Analiza funcțională (A-B-C) mapează Antecedentul → Comportamentul → Consecința, permițând identificarea condițiilor care declanșează și mențin comportamentul. Este baza planificării oricărei intervenții comportamentale.",
    # 58  MC5 — extincția
    "Extincția presupune retragerea consecventă a întăririi: comportamentul nu mai este urmat de recompensă și scade treptat în frecvență. Inițial poate apărea un „burst de extincție» — creștere temporară a comportamentului.",
    # 59  MC6 — modificare ≠ disciplină
    "Modificarea comportamentului este o intervenție bazată pe principii empirice: obiective observabile, proceduri replicabile și evaluare a progresului. Nu este disciplină arbitrară sau pedeapsă aplicată fără criterii clare.",
    # 60  MC7 — chaining
    "Chaining-ul (lanțuirea) divide un comportament complex în pași mici, fiecare întărit separat, formând un lanț de răspunsuri. Este util pentru sarcini cu multe etape secvențiale (ex. autoîngrijire la persoanele cu dizabilități).",
    # 61  MC8 — automonitorizarea
    "Automonitorizarea constă în înregistrarea sistematică a propriilor comportamente, gânduri sau stări. Datele colectate oferă baseline, permit evaluarea progresului și cresc conștientizarea — factor de schimbare în sine.",
    # 62  MC9 — tehnici (abc)
    "Token economy și programele de întărire (a), shaping și chaining (b), desensibilizarea și modelarea (c) sunt toate tehnici comportamentale. Interpretarea visului freudian (d) aparține psihanalizei, nu modificării comportamentale.",
    # 63  MC10 — Skinner și contingențe
    "B.F. Skinner a pus accentul pe contingențe — relația precisă și consecventă dintre comportament și consecință. Controlul contingențelor este esența modificării comportamentale derivate din psihologia skinneriana.",

    # —— Comparativ & aplicare (64–69) ——
    # 64  CA1 — caz fobie vorbit + DS
    "Ierarhia de situații + relaxare + parcurgere treptată (imaginară sau reală) descrie desensibilizarea sistematică — cel mai bine documentată tehnică pentru fobii de performanță, inclusiv frica de a vorbi în public.",
    # 65  CA2 — caz modelare vorbit
    "Urmărirea unui model care ține un discurs calm, urmată de practica propriei versiuni scurte, descrie modelarea participativă — clientul observă mai întâi, apoi imită treptat cu sprijin, reducând anxietatea de performanță.",
    # 66  CA3 — perechi tehnic–mecanism corecte (abc)
    "Perechile corecte: desensibilizare — contracondiționare (a), aversivă — consecință neplăcută (b), modelare — observare și imitare (c). Relaxarea nu este reprimare freudiană (d) — este un răspuns fiziologic antrenat.",
    # 67  CA4 — perechi greșite
    "„Desensibilizare — pedeapsă pentru frică» (a) este greșită: desensibilizarea nu pedepsește, ci contracondiționează. Celelalte variante (modelare — imitare, modificare — întăriri, relaxare — reducere tonus) sunt corecte.",
    # 68  CA5 — primul pas
    "Definirea comportamentului țintă observabil și măsurabil este primul pas necesar în orice program comportamental: fără o definiție clară nu se poate monitoriza progresul, nu se poate selecta tehnica adecvată și nu se poate evalua eficacitatea.",
    # 69  CA6 — toate tehnicile sunt comportamentale
    "Toate tehnicile menționate sunt comportamentale deoarece: (1) operează pe comportamente observabile, (2) aplică principii de învățare (condiționare, întărire, extincție, modelare), (3) utilizează proceduri structurate și replicabile.",

    # ── 70–99  CBT Ellis & Beck items 1–30 ───────────────────────────────────
    # —— Albert Ellis & REBT (70–83) ——
    # 70  CBT1 — Ellis: REBT definiție
    "Albert Ellis a fondat terapia rațional-emotivă (RET, ulterior REBT) în 1955, bazând-o pe ideea că suferința psihică nu provine direct din evenimentele exterioare, ci din evaluările iraționale (credințele absolute) aplicate acestor evenimente.",
    # 71  CBT2 — modelul A-B-C
    "Modelul A-B-C al lui Albert Ellis: A (evenimentul activator) → B (credința/evaluarea) → C (consecința emoțională sau comportamentală). Esența: C nu rezultă direct din A, ci este mediată de B — evaluarea pe care persoana o face evenimentului.",
    # 72  CBT3 — A din A-B-C
    "Litera A din modelul Ellis se referă la evenimentul activator — situația externă sau internă care declanșează procesul cognitiv-emoțional. Poate fi real sau imaginar, prezent sau anticipat.",
    # 73  CBT4 — B din A-B-C
    "Litera B (Beliefs) desemnează credințele, evaluările și interpretările despre evenimentul activator. Credințele pot fi raționale (preferențe flexibile) sau iraționale (cerințe absolute de tip „trebuie»).",
    # 74  CBT5 — C din A-B-C
    "Litera C (Consequences) desemnează consecințele emoționale (ex. anxietate, furie, depresie) și comportamentale (ex. evitare, agresivitate) care rezultă din credințele B aplicate evenimentului A.",
    # 75  CBT6 — B ca mediator
    "Ideea centrală a modelului Ellis: emoțiile intense nu sunt cauzate direct de eveniment (A), ci de modul în care persoana evaluează evenimentul (B). Același eveniment poate produce emoții diferite la persoane cu credințe diferite.",
    # 76  CBT7 — caz respingere la interviu
    "Afirmând că respingerea la interviu produce direct devastarea, studentul omite credința intermediară B. Ellis ar întreba: „Ce îți spui despre această respingere?» Credința tip „trebuie să fiu acceptat» mediază consecința emoțională intensă.",
    # 77  CBT8 — credință irațională tipică
    "O credință irațională tipică în REBT este o cerință absolută: „Trebuie să fiu perfect.» Ellis distinge credințele iraționale (cerințe absolute, catastrofizare, intoleranță la frustrare) de cele raționale (preferențe flexibile, toleranță).",
    # 78  CBT9 — musturbation
    "„Musturbarea» (musturbation — Ellis) descrie transformarea unei preferințe în cerință absolută de tip „trebuie», „musai», „obligatoriu». Aceste cerințe rigide sunt, după Ellis, sursa principală a suferinței emoționale inutile.",
    # 79  CBT10 — disputa cognitivă
    "Disputa cognitivă (D) este pasul activ al REBT: terapeutul contestă logic (e adevărat că trebuie?), empiric (există dovezi?) și pragmatic (te ajută să crezi asta?) credința irațională, urmărind înlocuirea ei cu o credință rațională.",
    # 80  CBT11 — A-B-C-D-E
    "Ellis a extins modelul la A-B-C-D-E: D (Disputing) = disputarea cognitivă a credințelor iraționale; E (Effective new philosophy) = o nouă filozofie de viață rațională, cu consecințe emoționale mai adaptate.",
    # 81  CBT12 — Ellis vs. Beck stilistic
    "Ellis este direct, filosofic și confruntativ — disputând credințele „trebuie» cu argumente logice și filozofice. Beck este mai colaborativ și empiric: terapeut și client testează împreună cognițiile ca ipoteze, prin întrebări socratice.",
    # 82  CBT13 — Ellis și filosofia stoică
    "Ellis s-a inspirat din filosofia stoică, în special din Epictet: „Nu evenimentele ne perturbă, ci judecățile despre ele» — premisa fundamentală a REBT, conform căreia responsabilitatea emoțională apartine evaluărilor persoanei.",
    # 83  CBT14 — REBT (abd)
    "REBT utilizează modelul A-B-C (a), vizează credințele absolute și catastrofizarea (b) și pune accent pe responsabilitatea emoțională — persoana contribuie la propria suferință prin evaluări rigide (d). Varianta c este greșită: Ellis include teme pentru acasă și exerciții comportamentale.",

    # —— Model A-B-C: aplicare & confuzii (84–89) ——
    # 84  CBT15 — A nu produce C direct
    "Conform REBT, ideea că A produce direct C contrazice modelul, deoarece credința B (evaluarea evenimentului) mediază legătura. Fără B, același A poate produce consecințe emoționale complet diferite.",
    # 85  CBT16 — caz șef critic
    "Identificarea lanțului A (critica șefului) → B (cred că sunt incompetent) → C (mă retrag) este coerentă cu modelul Ellis, deoarece surprinde corect rolul mediator al credinței B. Varianta d descrie triada cognitivă a lui Beck, nu modelul Ellis.",
    # 86  CBT17 — schimbarea B
    "Schimbarea credinței B de la o cerință absolută („trebuie să fiu iubit de toți») la o preferință flexibilă („prefer, dar pot tolera respingerea») este obiectivul central al REBT — înlocuirea credințelor iraționale cu credințe raționale.",
    # 87  CBT18 — componente A-B-C (abc)
    "Modelul A-B-C al Ellis conține: evenimentul activator (a), credințele despre eveniment (b) și consecințele emoționale sau comportamentale (c). Interpretarea arhetipului umbrei jungiene (d) nu face parte din modelul Ellis.",
    # 88  CBT19 — toleranță scăzută la frustrare
    "Toleranța scăzută la frustrare (LFT) este o credință irațională tipică: „Nu pot suporta deloc disconfortul.» Ellis distinge LFT de toleranța înaltă la frustrare (HFT): „Disconfortul e neplăcut, dar îl pot gestiona.»",
    # 89  CBT20 — awfulizing
    "„Awfulizing» (catastrofizarea) în REBT este credința că situația este „groaznică, de nesuportat, mai rea decât poate fi imaginat.» Ellis o diferențiază de evaluarea realistă: „E neplăcut, dar pot funcționa.» Catastrofizarea amplifică suferința emoțională.",

    # —— Aaron T. Beck & terapia cognitivă (90–99) ——
    # 90  CBT21 — Beck: originea terapiei cognitive
    "Aaron T. Beck a dezvoltat terapia cognitivă în anii 1960 pornind de la cercetarea depresiei. Observând că pacienții depresivi aveau gânduri automate negative sistematice, a formulat un model cognitiv al depresiei bazat pe triada cognitivă.",
    # 91  CBT22 — gânduri automate
    "Gândurile automate (Beck) sunt cogniții rapide, involuntare, care apar în situații specifice și influențează emoția. Sunt accesibile conștiinței, dar adesea neexaminate critic. Pot fi identificate prin întrebări socratice sau fișa de gânduri.",
    # 92  CBT23 — triada cognitivă a depresiei
    "Triada cognitivă a depresiei (Beck) include viziuni negative despre: sine (sunt incompetent), lume (lumea e ostilă) și viitor (lucrurile nu se vor îmbunătăți). Aceste trei distorsiuni se susțin reciproc și mențin depresia.",
    # 93  CBT24 — credință de bază vs. gând automat
    "Credința de bază (schema) este o convingere globală, stabilă, despre sine (ex. „Sunt incompetent»). Se distinge de gândul automat situațional (ex. „Am greșit la această sarcină») și de credința intermediară (reguli, asumpții condiționante).",
    # 94  CBT25 — distorsiuni cognitive
    "Distorsiunile cognitive (Beck) sunt erori sistematice de interpretare care susțin și mențin stările emoționale disfuncționale. Exemple: gândire alb-negru, generalizare excesivă, personalizare, catastrofizare, citirea gândurilor.",
    # 95  CBT26 — catastrofizare/alb-negru
    "Gândul „Dacă nu ies perfect, e un dezastru total» conține catastrofizarea (dezastru total) și gândire alb-negru (ori perfect ori dezastru). Aaron T. Beck le-ar identifica ca distorsiuni cognitive care amplifică suferința.",
    # 96  CBT27 — citirea gândurilor
    "„Citirea gândurilor» (Beck) este distorsiunea prin care persoana pretinde că știe ce gândesc alții fără dovezi. Exemplu: „Știu sigur că mă consideră incompetent» — concluzie fără suport empiric, susținând anxietatea socială sau depresia.",
    # 97  CBT28 — empirism colaborativ
    "Empirismul colaborativ (Beck) presupune că terapeutul și clientul funcționează ca o echipă de investigare: cognițiile sunt tratate ca ipoteze de testat, nu ca adevăruri fixe. Relația este colaborativă, nu autoritară.",
    # 98  CBT29 — întrebări socratice
    "Întrebările socratice ghidează clientul prin examinarea dovezilor pro și contra unei cogniții, fără a impune o concluzie. Exemple: „Ce dovezi ai că ești incompetent?», „Există dovezi contrare?», „Ce ar spune un prieten?» — tehnică centrală a terapiei beckiene.",
    # 99  CBT30 — restructurare cognitivă Beck
    "Restructurarea cognitivă (Beck) urmărește înlocuirea interpretărilor distorsionate cu alternative mai realiste și mai funcționale. Nu neagă realitatea evenimentelor, ci modifică modul de interpretare al acestora.",
]

assert len(PART5_EXPLANATIONS) == 100
