"""Explicații Psihoterapie II — partea 6 (index 527–626, exam 7528–7627).

Conținut:
  527–556  CBT Ellis & Beck items 31–60
  557–576  Lazarus multimodal items 1–20
  577–606  Glasser reality items 1–30
  607–626  terapia de familie items 1–20
"""

from __future__ import annotations

from typing import List

PART6_EXPLANATIONS: List[str] = [
    # ── 0–29  CBT Ellis & Beck items 31–60 ───────────────────────────────────
    # —— Aaron T. Beck — continuare (0–15) ——
    # 0  CBT31 — experiment comportamental Beck
    "Experimentele comportamentale (Beck) testează validitatea unei credințe în realitate — clientul verifică empiric dacă predicțiile sale anxioase se realizează. Ex.: „Dacă vorbesc la ședință, oamenii vor râde» — clientul vorbește și observă ce se întâmplă.",
    # 1  CBT32 — activare comportamentală Beck depresie
    "Activarea comportamentală, integrată în protocoalele CBT pentru depresie, reintroduce graduat activități plăcute sau cu sens. Inactivitatea menține și agravează depresia — prin activare, clientul rupe ciclul stagnare–tristețe–stagnare.",
    # 2  CBT33 — fișa de gânduri
    "Fișa de înregistrare a gândurilor (Beck) structurează: situația, emoția și intensitatea, gândul automat, dovezi pro și contra, gândul alternativ mai realist și emoția rezultată. Este un instrument central de auto-monitorizare în CBT.",
    # 3  CBT34 — săgeata descendentă
    "Tehnica săgeții descendente (downward arrow — Beck) identifică credința de bază sub un gând automat prin întrebarea repetată: „Dacă ar fi adevărat, ce ar însemna asta pentru tine?» Coboară de la cogniție situațională la schemă profundă.",
    # 4  CBT35 — distorsiuni (abc)
    "Distorsiunile cognitive asociate terapiei lui Beck: gândire alb-negru (a), generalizare excesivă (b) și personalizare (c). Sublimarea freudiană (d) este un mecanism de apărare psihanalitic, nu o distorsiune cognitivă beckiană.",
    # 5  CBT36 — Beck vs. Ellis accentul
    "Beck pune accent pe gânduri automate situaționale și scheme cognitive, lucrate empiric. Ellis pune accent pe credințele iraționale absolute de tip „trebuie», lucrând filozofic prin disputare. Ambii vizează cognițiile, dar cu focusuri și stiluri diferite.",
    # —— Ellis vs. Beck & integrare (6–13) ——
    # 6  CBT37 — distincție Ellis vs. Beck (ab)
    "Distincție corectă: Ellis — dispută filozofică a cerințelor absolute, model A-B-C (a); Beck — model al gândurilor automate și schemelor cognitive (b). Ambii folosesc teme pentru acasă. Niciuna dintre abordări nu respinge tehnicile comportamentale.",
    # 7  CBT38 — stil terapeutic: Ellis vs. Beck
    "Ellis folosește disputa cognitivă directă și argumentare filozofică. Beck folosește mai frecvent întrebările socratice și testarea empirică a ipotezelor cognitive — empirismul colaborativ — ceea ce face abordarea sa mai puțin confruntativă.",
    # 8  CBT39 — contribuție comună Ellis și Beck
    "Atât Ellis cât și Beck au introdus rolul central al cognițiilor în producerea și menținerea suferinței psihice, fondând orientarea cognitiv-comportamentală. Ellis — credințe iraționale; Beck — distorsiuni și scheme cognitive.",
    # 9  CBT40 — stil: Ellis confruntativ, Beck colaborativ
    "Ellis este adesea mai confruntativ-filozofic, contestând direct credințele. Beck este mai colaborativ și orientat spre formularea ipotezelor testabile — empirismul colaborativ plasează terapeutul și clientul ca parteneri de cercetare.",
    # 10  CBT41 — mecanism diferit Ellis vs. Beck
    "La Beck, suferința rezultă din distorsiunile cognitive (modul de interpretare). La Ellis, suferința apare când preferințele devin cerințe absolute rigide (musturbation). Ambele duc la disfuncție emoțională prin tipuri diferite de erori cognitive.",
    # 11  CBT42 — perechi autor–contribuție (ab)
    "Perechile corecte: Albert Ellis — model A-B-C și REBT (a); Aaron T. Beck — gânduri automate, scheme și triada cognitivă (b). Ellis nu a lucrat cu condiționare operantă (c); Beck nu a formulat inconștientul colectiv (d).",
    # 12  CBT43 — caz trebuie să fiu perfect
    "Beck identifică distorsiunile cognitive (catastrofizare, gândire alb-negru). Ellis identifică cerința absolută irațională (trebuie să fiu perfect) și catastrofizarea (e un dezastru) — ambele vizând evaluarea disfuncțională, cu terminologie diferită.",
    # 13  CBT44 — teme pentru acasă: Ellis + Beck vs. psihanaliză
    "Atât Ellis cât și Beck utilizează teme pentru acasă și exerciții structurate — specifice orientărilor active și directive. Psihanaliza clasică, centrată pe asociație liberă și interpretare în ședință, nu impune teme pentru acasă ca instrument principal.",
    # —— CBT: scop, diferențe, noutăți (14–29) ——
    # 14  CBT45 — CBT definiție
    "Terapia cognitiv-comportamentală (CBT) integrează tehnici de modificare a cognițiilor disfuncționale (restructurare, disputare, testare) cu tehnici comportamentale (expunere, activare, modelare), oferind un cadru unitar pentru intervenție.",
    # 15  CBT46 — CBT vs. behaviorism clasic: noutatea
    "Față de behaviorismul clasic, CBT introduce rolul mediațional al cognițiilor: persoana nu răspunde mecanic la stimuli, ci evaluează și interpretează evenimentele. Această mediție cognitivă determină emoția și comportamentul.",
    # 16  CBT47 — CBT adaugă față de behaviorism
    "CBT adaugă că modul în care persoana evaluează evenimentele influențează emoția și comportamentul. Behaviorismul clasic explică prin asociere stimul–răspuns sau contingențe, fără a implica procese cognitive intermediare.",
    # 17  CBT48 — CBT vs. psihanaliză
    "Față de psihanaliza clasică, CBT: lucrează cu conținuturi conștiente; accentuează prezentul; urmărește obiective clare; utilizează protocoale structurate și evaluate empiric; are durată limitată și măsoară progresul.",
    # 18  CBT49 — scopul CBT
    "Scopul principal al CBT este reducerea suferinței prin modificarea cognițiilor disfuncționale (credințe iraționale, distorsiuni, scheme) și a comportamentelor problematice (evitare, pasivitate), printr-o colaborare activă terapeut–client.",
    # 19  CBT50 — caracteristici CBT
    "Intervențiile CBT sunt structurate, active, orientate spre obiective, cu durată limitată și evaluate empiric. Aceasta le distinge de psihoterapiile nondirective sau de lungă durată, nedeterminate în obiective.",
    # 20  CBT51 — CBT anxietate: restructurare + expunere
    "În anxietate, restructurarea cognitivă (modificarea gândurilor catastrofice) este combinată cu expunerea graduală sau desensibilizarea (reducerea evitării comportamentale). Combinația este mai eficace decât fiecare componentă separat.",
    # 21  CBT52 — psihoeducația în CBT
    "Psihoeducația în CBT transformă clientul în participant activ: înțelegând modelul tulburării, mecanismele de menținere și logica strategiilor de coping, clientul poate aplica tehnicile independent și poate monitoriza progresul.",
    # 22  CBT53 — evidence-based
    "CBT este descrisă ca orientare bazată pe dovezi deoarece protocoalele au fost testate în studii clinice randomizate controlate, cu populații specifice, demonstrând eficacitate pentru depresie, anxietate, OCD, PTSD și alte tulburări.",
    # 23  CBT54 — caz social: restructurare + experiment
    "Combinarea testării cognitive (verificarea empirică a predicției „oamenii mă vor respinge») cu intervenția comportamentală (mersul la întâlnire) este esența CBT pentru anxietate socială — restructurare cognitivă + experiment comportamental.",
    # 24  CBT55 — noutățile CBT (abd)
    "CBT introduce: integrarea cognitivă cu tehnicile comportamentale (a), protocoale structurate cu obiective și evaluare (b) și teme pentru acasă ca instrument de transfer în viața reală (d). Varianta c este greșită — CBT nu respinge rolul gândurilor.",
    # 25  CBT56 — cogniții mediator
    "În CBT, emoțiile și comportamentele sunt influențate de modul în care persoana interpretează situațiile — nu de reflexe innate sau de structura familială, ci de evaluările și credințele individuale.",
    # 26  CBT57 — CBT vs. behaviorism: perechi (ab)
    "Perechile corecte: behaviorism clasic — contingențe stimul–răspuns (a); CBT — cogniții, restructurare, expunere, activare comportamentală (b). Varianta c (behaviorism clasic — disputare REBT) și d (CBT — inconștient) sunt greșite.",
    # 27  CBT58 — perechi greșite (c)
    "Varianta c — „asociația liberă ca tehnică centrală CBT» — este greșită. Asociația liberă este o tehnică psihanalitică, nu CBT. Disputa credințelor (a) aparține Ellis/REBT, restructurarea distorsiunilor (b) aparține Beck, expunerea graduală (d) este componentă comportamentală CBT.",
    # 28  CBT59 — Lazarus în familia CBT
    "Terapia multimodală a lui Arnold A. Lazarus se încadrează în familia CBT deoarece evaluează și intervine sistematic pe comportament, afect, cogniție, senzație, imagistică, relații și biologie — integrând tehnici cognitive și comportamentale validate.",
    # 29  CBT60 — convergența Ellis + Beck + tehnici
    "Convergența în CBT: Ellis (credințe iraționale), Beck (distorsiuni, scheme) și tehnicile comportamentale (expunere, activare) pornesc de la aceeași premisă — schimbarea durabilă necesită intervenție pe gânduri, emoții și comportamente observabile.",

    # ── 30–49  Lazarus multimodal items 1–20 ─────────────────────────────────
    # —— Fundamente & scop (30–35) ——
    # 30  L1 — definiție terapie multimodală
    "Arnold A. Lazarus a fondat terapia multimodală ca extensie a CBT, propunând că evaluarea și intervenția trebuie să acopere toate dimensiunile relevante ale funcționării umane, nu o singură modalitate, pentru a maximiza eficacitatea și a preveni recăderea.",
    # 31  L2 — BASIC ID
    "Acronimul BASIC ID reprezintă cele șapte modalități: Behavior (comportament), Affect (afect), Sensation (senzație), Imagery (imagistică), Cognition (cogniție), Interpersonal (relații interpersonale), Drugs/biology (biologie/medicație). Fiecare poate fi sursă de problemă și țintă de intervenție.",
    # 32  L3 — Interpersonal în BASIC ID
    "Dimensiunea I (Interpersonal) din BASIC ID vizează modul în care clientul comunică, se raportează la ceilalți, gestionează conflictele și construiește relații. Intervenția poate include antrenament de asertivitate, rol playing și negociere.",
    # 33  L4 — eclectism tehnic
    "Eclectismul tehnic (Lazarus) înseamnă selectarea procedurilor pe baza dovezilor și a potrivirii cu profilul clientului, nu pe baza fidelității față de o singură școală teoretică. Este o abordare orientată spre eficacitate.",
    # 34  L5 — eclectism tehnic vs. teoretic
    "Eclectismul tehnic selectează proceduri validate pentru fiecare problemă specifică. Eclectismul teoretic amestecă cadre teoretice incompatibile. Lazarus prefigurează abordarea bazată pe dovezi prin selecție pragmatică a intervențiilor.",
    # 35  L6 — specificitate situațională
    "Specificitatea situațională înseamnă că intervenția este adaptată contextului unic al clientului. Nu există un protocol universal — profilul modal individual ghidează alegerea combinației optime de tehnici pentru fiecare client.",
    # —— Evaluare & profil modal (36–39) ——
    # 36  L7 — profilul modal
    "Profilul modal identifică care dimensiuni BASIC ID sunt cele mai problematice pentru un client specific. Terapeutul prioritizează intervenția pe dimensiunile cele mai disfuncționale, adaptând planul de tratament la nevoile individuale.",
    # 37  L8 — Imagery în BASIC ID
    "Dimensiunea Imagery din BASIC ID include imaginile mentale, fanteziile, scenariile vizualizate și imaginile perturbatoare (ex. flashback-uri). Tehnicile includ vizualizare dirijată, rehearsal mental și modificarea imaginilor negative.",
    # 38  L9 — Drugs/biology în BASIC ID
    "Drugs/biology vizează funcționarea somatică: somn, alimentație, activitate fizică, medicație, stări medicale și substanțe consumate. Lazarus recunoaște că problemele biologice pot influența toate celelalte dimensiuni BASIC ID.",
    # 39  L10 — dimensiuni BASIC ID (abc)
    "Modelul BASIC ID conține: Behavior și Affect (a), Sensation și Cognition (b), Imagery și Interpersonal (c). Variantele abc sunt corecte. Sine, Eul și Supraeu (d) aparțin psihanalizei freudiene, nu modelului lui Lazarus.",
    # —— Intervenții CBT multimodale (40–45) ——
    # 40  L11 — caz anxietate: intervenție combinată
    "Un client cu anxietate prezintă probleme la multiple niveluri: cogniție (gânduri catastrofice), senzație (tensiune musculară) și interpersonal (evitare socială). Terapia multimodală propune intervenții paralele: restructurare cognitivă, relaxare și expunere gradată.",
    # 41  L12 — restructurare cognitivă în TM
    "Restructurarea cognitivă în terapia multimodală vizează dimensiunea C (Cognition) din BASIC ID. Modificând gândurile disfuncționale (catastrofizare, gândire alb-negru), se reduc consecințele emoționale și comportamentale ale acestora.",
    # 42  L13 — relaxare și biofeedback → Sensation
    "Relaxarea și biofeedback-ul vizează dimensiunea Sensation din BASIC ID — controlul răspunsurilor fiziologice (tonus muscular, ritm cardiac, tensiune arterială). Sunt tehnici directe pentru reducerea activării fiziologice excesive.",
    # 43  L14 — rol playing → Interpersonal
    "Rol playing-ul și antrenamentul de asertivitate intervin la nivel interpersonal — dimensiunea I din BASIC ID. Clientul exersează abilități de comunicare, negociere și asertivitate în contexte simulate înainte de aplicarea în viața reală.",
    # 44  L15 — expunere și activare în TM
    "Expunerea graduală și activarea comportamentală ilustrează că Lazarus combină tehnicile comportamentale clasice cu evaluarea cognitivă și emoțională — abordarea eclectică tehnică pune eficacitatea mai presus de fidelitatea față de o singură școală.",
    # 45  L16 — imagistică mentală
    "Vizualizarea controlată (Imagery din BASIC ID) poate fi folosită pentru rehearsal mental — clientul vizualizează executarea competentă a unui comportament înainte de situația reală, crescând self-efficacy și reducând anxietatea de performanță.",
    # —— Clientul este încurajat să… (46–49) ——
    # 46  L17 — clientul activ
    "Terapia multimodală încurajează activ participarea clientului între ședințe prin teme, exerciții și automonitorizare. Principiu CBT comun: schimbarea nu se produce doar în cabinetul terapeutului, ci prin practică consecventă în viața reală.",
    # 47  L18 — automonitorizare
    "Automonitorizarea oferă date concrete despre frecvența și contextul gândurilor, emoțiilor și comportamentelor. Aceste date ghidează alegerea și evaluarea intervențiilor, și constituie în sine un factor de schimbare (reactivity of self-monitoring).",
    # 48  L19 — clientul devine propriul terapeut
    "Lazarus subliniază că schimbarea durabilă cere ca clientul să devină propriul terapeut — să înțeleagă profilul său modal și să aplice independent strategiile adecvate, reducând dependența de terapeut și prevenind recăderea.",
    # 49  L20 — intervenție multimodală complexă
    "Intervenția pe mai multe modalități simultan (restructurare cognitivă + relaxare + rol jucat) reflectă principiul lui Lazarus că problemele complexe necesită intervenție pe mai multe dimensiuni — o singură tehnică este adesea insuficientă pentru schimbare durabilă.",

    # ── 50–79  Glasser reality items 1–30 ────────────────────────────────────
    # —— Fundamente: focus, alegere, responsabilitate (50–57) ——
    # 50  G1 — Glasser: definiție
    "William Glasser a fondat terapia centrată pe realitate în anii 1960, pornind de la lucrul cu adolescenți delincvenți. Principiul central: comportamentul prezent este ales pentru a satisface nevoi interioare; schimbarea vine din asumarea responsabilității alegerilor.",
    # 51  G2 — comportamentul prezent
    "Comportamentul prezent este central la Glasser deoarece poate fi ales și modificat. Trecutul este ireversibil și explicativ, dar nu justifică menținerea alegerilor disfuncționale. Focusul pe prezent oferă clientului control și responsabilitate.",
    # 52  G3 — responsabilitatea personală
    "Responsabilitatea personală, la Glasser, înseamnă că clientul recunoaște că alegerile sale (chiar și comportamentele simptomatice) sunt modalități de a satisface nevoi. Schimbarea cere asumarea acestor alegeri, nu imputarea lor mediului.",
    # 53  G4 — teoria alegerii
    "Teoria alegerii (Choice Theory — Glasser) susține că tot comportamentul este ales pentru a satisface nevoi de bază (supraviețuire, dragoste/apartenența, putere, libertate, distracție). Controlul extern al comportamentului este refuzat ca premisă.",
    # 54  G5 — lumea calității
    "„Lumea calității» (quality world) conține imaginile mentale ale persoanelor, locurilor, lucrurilor și valorilor care au adus satisfacție. Comportamentul este orientat spre apropierea de această lume interioară — terapeutul ajută clientul să o clarifice.",
    # 55  G6 — modelul WDEP
    "Modelul WDEP (Glasser) structurează terapia în patru etape: W — ce vrea clientul (Wants); D — ce face (Doing); E — evaluarea dacă acțiunile funcționează (Evaluation); P — planificarea unor alternative mai eficace (Planning).",
    # 56  G7 — Evaluation în WDEP
    "Etapa Evaluation din WDEP cere clientului să evalueze critic comportamentul actual: „Ceea ce faci acum te ajută să obții ceea ce vrei?» Este un moment de reflecție care pregătește schimbarea fără culpabilizare externă.",
    # 57  G8 — comportamentul total
    "Comportamentul total (total behavior) include patru componente: acțiunea, gândirea, emoția și fiziologia. Glasser subliniază că clientul controlează direct mai ales acțiunea și gândirea — prin acestea poate influența emoția și starea fizică.",
    # —— Relația terapeutică & ce face clientul (58–65) ——
    # 58  G9 — relația terapeutică
    "Relația terapeutică la Glasser este apropiată, caldă și directă. Terapeutul nu interpretează trecutul, ci colaborează cu clientul în planificarea schimbării, întrebând: ce vrea, ce face și ce poate face diferit.",
    # 59  G10 — terapeutul evită scuzele
    "Terapeutul, în abordarea lui Glasser, nu acceptă scuzele bazate pe trecut sau pe circumstanțe externe. Acceptarea scuzelor ar întări ideea că clientul nu poate controla propriile alegeri — contrar principiului responsabilității.",
    # 60  G11 — clientul evaluează
    "Clientul este încurajat să evalueze comportamentul actual în raport cu propriile dorințe: „Funcționează ceea ce fac?» Această evaluare internă (nu judecata terapeutului) este motorul schimbării în terapia centrată pe realitate.",
    # 61  G12 — planul concret
    "Planificarea (P din WDEP) urmărește formularea unui plan concret, realist și asumat: ce anume va face clientul diferit, când și cum. Planul trebuie să fie specific, realizabil și evaluat ulterior pentru a deveni instrument de schimbare.",
    # 62  G13 — WDEP — rol
    "Întrebările WDEP conduc clientul de la dorință la acțiune și evaluare, fără a rămâne blocat în plângere pasivă. Terapia centrată pe realitate este orientată spre soluții și acțiune, nu spre explorarea trecutului.",
    # 63  G14 — plângerea prelungită
    "Glasser consideră că plângerea prelungită fără plan de acțiune menține clientul în pasivitate și îl îndepărtează de responsabilitate. Terapeutul redirecționează: de la „de ce s-a întâmplat» la „ce pot face acum.»",
    # 64  G15 — nevoi + alegeri
    "Glasser identifică cinci nevoi de bază: supraviețuire, dragoste/apartenența, putere/realizare, libertate și distracție. Tot comportamentul este ales pentru a satisface una sau mai multe dintre aceste nevoi — uneori ineficient.",
    # 65  G16 — clientul (abd)
    "Clientul este încurajat: să clarifice ce vrea (W — a), să evalueze dacă acțiunile funcționează (E — b) și să își asume alegerile prin planificare concretă (P și D — d). Varianta c — „evită planificarea» — contrazice modelul WDEP.",
    # —— Diferențe față de alte orientări (66–73) ——
    # 66  G17 — față de psihanaliză
    "Față de psihanaliza clasică, terapia centrată pe realitate nu explorează visele, transferul sau inconștientul. Focusul este pe comportamentul prezent și pe alegerile actuale — terapeutul nu este interpret al trecutului, ci partener în planificarea viitorului.",
    # 67  G18 — față de Rogers
    "Față de Carl R. Rogers, Glasser este mai directiv: confruntă clientul cu consecințele alegerilor, cere evaluarea comportamentului și formularea unui plan de acțiune. Rogers privilegiază acceptarea necondiționată și autonomia fără directivitate.",
    # 68  G19 — față de CBT Beck
    "Față de CBT beckiană, Glasser pune mai mult accent pe ce vrea clientul (Wants) și pe apropierea comportamentului de „lumea calității» — nu pe identificarea distorsiunilor cognitive. Beck lucrează pe scheme; Glasser pe alegeri și nevoi.",
    # 69  G20 — față de gestalt
    "Terapia centrată pe realitate și gestalt se aseamănă prin focusul pe prezent. Diferă: Glasser pune accent pe planificare, evaluare și responsabilitate; gestalt pune accent pe conștientizarea corporală și pe tehnici experimentale (ex. scaunul gol).",
    # 70  G21 — față de Ellis/REBT
    "Față de Ellis, Glasser nu lucrează cu disputa convingerilor iraționale de tip „trebuie». Glasser întreabă: „Ce faci acum și funcționează?» Ellis întreabă: „Ce îți spui despre eveniment și e rațional?» Mecanismele și vocabularul sunt diferite.",
    # 71  G22 — caz copilărie
    "Răspunsul coerent cu Glasser: „Ce faci acum și ce poți alege diferit?» — focusul pe alegere și responsabilitate prezentă, nu pe explorarea trecutului. Glasser refuză să accepte că trecutul determină irevocabil prezentul.",
    # 72  G23 — caz coleg
    "Terapeutul glasserian investighează ce vrea clientul, ce face efectiv și dacă acțiunile îl apropie de scop. Plângerea despre colegi fără plan concret este ineficace; WDEP transformă plângerea în evaluare și acțiune.",
    # 73  G24 — perechi (abd)
    "Perechile corecte: Freud — inconștient, trecut, interpretare (a); Glasser — alegere, responsabilitate, comportament prezent (b); Rogers — acceptare și empatie, cu mai puțin accent pe planificarea acțiunii (d). Varianta c — Glasser cu analiza visului — este greșită.",
    # —— Aplicare & sinteză (74–79) ——
    # 74  G25 — psihologia controlului extern
    "Psihologia controlului extern (criticată de Glasser) este convingerea că alții sau circumstanțele ne controlează comportamentul fără consimțământ. Glasser respinge această premisă: comportamentul este ales intern, chiar dacă este influențat de mediu.",
    # 75  G26 — simptomul în terapia centrată pe realitate
    "Simptomul (plângerea) este abordat prin clarificarea comportamentului actual și a alegerilor care nu satisfac nevoile. Simptomul este înțeles ca o alegere ineficace de a satisface nevoi, nu ca un mesaj inconștient sau o consecință a trecutului.",
    # 76  G27 — Doing în WDEP
    "Etapa Doing (D) clarifică comportamentul actual concret: ce face clientul efectiv, nu ce simte sau ar vrea în abstract. Această concretețe permite evaluarea realistă și formularea unui plan alternativ.",
    # 77  G28 — relații de calitate
    "Relațiile de calitate, la Glasser, se construiesc când oamenii își asumă alegeri care respectă atât nevoile proprii cât și ale celorlalți. Controlul extern al comportamentului celorlalți distruge relațiile — premisă centrală a teoriei alegerii.",
    # 78  G29 — componente WDEP (abc)
    "Modelul WDEP: Wants (a), Doing (b), Evaluation și Planning (c). Varianta d — „Working through» — este un termen psihanalitic (elaborare), nu o componentă a modelului lui Glasser.",
    # 79  G30 — rezumat Glasser
    "Rezumatul „alegere, responsabilitate, comportament prezent, planificare» surprinde nucleul psihoterapiei centrate pe realitate: tot comportamentul este ales; clientul poate alege diferit; terapia ajută la evaluarea alegerilor actuale și la planificarea unor alternative mai eficace.",

    # ── 80–99  Terapia de familie items 1–20 ─────────────────────────────────
    # —— Fundamente (80–84) ——
    # 80  TF1 — familia ca sistem
    "În terapia de familie, familia este un sistem în care membrii se influențează reciproc prin comunicare, reguli și patternuri relaționale. Modificarea unui element al sistemului afectează întreg ansamblul — premisă sistemică fundamentală.",
    # 81  TF2 — cauzalitate circulară
    "Cauzalitatea circulară respinge perspectiva liniară (A cauzează B) și recunoaște că comportamentele familiale se mențin reciproc în cicluri: comportamentul unui membru răspunde la cel al altuia și îl influențează la rândul său.",
    # 82  TF3 — pacientul identificat
    "Pacientul identificat (IP) este membrul familiei care „poartă» simptomul, dar problemele reflectă de obicei disfuncționalități ale sistemului familial mai larg. Focusul exclusiv pe IP omite contextul relațional care menține simptomul.",
    # 83  TF4 — obiectiv terapia de familie
    "Un obiectiv frecvent al terapiei de familie este îmbunătățirea comunicării și clarificarea rolurilor, limitelor și alianțelor — modificarea patternurilor disfuncționale care mențin simptomul sau conflictul în sistem.",
    # 84  TF5 — întrebarea sistemică
    "Orientarea spre patternuri relaționale („cum este menținută problema?») evită culpabilizarea unui singur membru și permite intervenția asupra proceselor care mențin problema. Perspectiva circulară este mai constructivă decât cea punitivă.",
    # —— Abordarea psihodinamică (85–90) ——
    # 85  TF6 — abordare psihodinamică în familie
    "Abordarea psihodinamică în terapia de familie explorează cum relațiile timpurii, conflictele nerezolvate și transferurile din familia de origine influențează viața familială actuală — cum trecutul devine prezent în relațiile intime.",
    # 86  TF7 — Murray Bowen: diferențiere
    "Murray Bowen a introdus conceptul de diferențiere de sine — capacitatea de a rămâne calm, autonom și funcțional în relații intense, fără fuziune emoțională sau distanțare. Diferențierea redusă predispune la reactivitate emoțională și la transmisii transgeneraționale.",
    # 87  TF8 — genograma
    "Genograma (Bowen) este o reprezentare grafică a familiei pe mai multe generații, identificând patternuri emoționale repetitive, alianțe, conflicte, triangulări și transmisii intergeneraționale. Oferă o perspectivă istorică asupra sistemului familial.",
    # 88  TF9 — triangularea Bowen
    "Triangularea (Bowen) apare când tensiunea din relația dintre doi membri devine insuportabilă și un al treilea este atras pentru a o reduce — un copil poate deveni „mesager» sau „arbiter» în conflictul parental, perturbând propria sa dezvoltare.",
    # 89  TF10 — Bowen față de psihodinamic clasic
    "Bowen se distinge de abordarea psihodinamică clasică prin accentul pe procesele relaționale din familia actuală și pe transmisia intergenerațională, nu pe interpretarea conflictelor intrapsihice individuale sau a transferului terapeutic.",
    # —— Abordarea sistemică (90–94) ——
    # 90  TF11 — abordare psihodinamică vs. structurală
    "Abordarea psihodinamică în familie pune accent pe istoria relațională și pe conflictele transmise intergenerațional; abordarea structurală pune accent pe organizarea sistemului actual — granițe, subsisteme, ierarhie (Salvador Minuchin).",
    # 91  TF12 — abordarea sistemică
    "Abordarea sistemică vede familia ca un sistem cu proprietăți emergente: reguli implicite, feedback (negativ — stabilizator; pozitiv — amplificator) și tendință spre homeostazie. Simptomul poate fi înțeles ca mecanism de reglare a sistemului.",
    # 92  TF13 — homeostazia
    "Homeostazia în terapia de familie descrie rezistența sistemului la schimbare, chiar și când patternurile sunt disfuncționale. Familia tinde să revină la starea anterioară, ceea ce explică rezistența la intervenție și importanța schimbării de ordinul II.",
    # 93  TF14 — schimbare ordinul I
    "Schimbarea de ordinul I modifică comportamente sau simptome la suprafață, fără a schimba regulile și structura care le generează. Este ca rezolvarea simptomului fără modificarea patternului — schimbarea nu este durabilă.",
    # 94  TF15 — schimbare ordinul II
    "Schimbarea de ordinul II modifică regulile, credințele sau patternurile fundamentale ale sistemului — structura care generează simptomul. Este mai profundă și mai durabilă, dar mai dificil de realizat.",
    # —— Abordarea structurală (95–99) ——
    # 95  TF16 — caz copil în conflict parental
    "Din perspectivă sistemică, simptomul copilului poate stabiliza familia: când copilul devine centrul atenției părinților în conflict, aceștia se unesc temporar în jurul simptomului. Simptomul are o funcție de reglare sistemică.",
    # 96  TF17 — Salvador Minuchin: structurală
    "Salvador Minuchin a dezvoltat terapia structurală, punând accentul pe organizarea familiei: granițele (clare, difuze sau rigide) dintre subsisteme (conjugal, parental, fraternitate), ierarhia și alianțele definesc sănătatea familială.",
    # 97  TF18 — enmeshment
    "Enmeshment-ul (împletirea excesivă — Minuchin) descrie granițe difuze: membrii supraactivați emoțional reacționează excesiv la orice distanțare, limitând autonomia și individuarea, mai ales a adolescenților.",
    # 98  TF19 — disengagement
    "Disengagement-ul (dezangajarea — Minuchin) descrie granițe rigide: comunicare minimă, sprijin emoțional redus și izolare. Copiii cu părinți dezangajați pot căuta validare și suport emoțional în afara familiei.",
    # 99  TF20 — restructurarea Minuchin
    "Restructurarea, în terapia structurală, urmărește modificarea alianțelor, granițelor și ierarhiei familiei: unbalancing, joining, enactment sunt tehnici utilizate pentru a schimba organizarea sistemului și a permite simptomului să se reducă.",
]

assert len(PART6_EXPLANATIONS) == 100
