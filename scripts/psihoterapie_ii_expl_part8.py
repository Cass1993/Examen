"""Explicații Psihoterapie II — partea 8 (index 727–857, exam 7728–7858).
Psihodramă extra (ultimii 31) + Terapia Unificării Mitrofan (toți 100).
"""

from __future__ import annotations

from typing import List

# ── Psihodramă extra — ultimii 31 de itemi (itemi 30–60) ─────────────────────
# idx 0–30 / exam 7728–7758

_PSYCHODRAMA_EXTRA_LAST31: List[str] = [
    # 0 / item 30 — scenariu: fotografia psihodramatică / sculptura
    (
        "Directorul care cere grupului să redea pozițiile corporale din conflict "
        "ilustrează fotografia psihodramatică sau sculptura de grup — înghețarea "
        "scenei într-o poziție expresivă; nu solilocviul (verbalizare interioară), "
        "asociația liberă (psihanaliza) sau disputa REBT."
    ),
    # 1 / item 31 — reluarea scenei + surplus reality
    (
        "Protagonistul care repetă scena cu părintele spunând acum ce nu a spus "
        "atunci combină reluarea scenei și posibil surplus reality — explorarea "
        "situației dorite sau nerealizate anterior; token economy, triangularea "
        "boweniană și stadiul genital nu sunt tehnici psihodramatice similare."
    ),
    # 2 / item 32 — multiselect perechi tehnică-funcție corecte
    (
        "Perechi corecte în psihodramă: dublul — exprimă trăiri greu accesibile "
        "protagonistului; oglinda — reflectă comportamentul protagonistului; "
        "inversiunea — schimbă perspectiva prin rol. "
        "Solilocviul înlocuiește complet scena este o afirmație greșită."
    ),
    # 3 / item 33 — perechi greșite (răspuns c)
    (
        "Afirmația greșită este că 'catharsisul = pedeapsă pentru emoții negative' "
        "— catharsisul este eliberare emoțională prin trăire, urmată de integrare. "
        "Fotografia psihodramatică înghețând scena, concretizarea făcând vizibil "
        "conflictul abstract și amplificarea mărind gestul sau cuvântul "
        "sunt toate corecte."
    ),
    # 4 / item 34 — scenariu: concretizarea
    (
        "Un protagonist blocat verbal căruia directorul îi pune în mână un obiect "
        "de pe scenă ca punct de sprijin ilustrează concretizarea — ancorarea "
        "experienței în obiect sau acțiune; nu proiecția ca mecanism de apărare "
        "freudian, sociometria sau interpretarea visului."
    ),
    # 5 / item 35 — corpul pe scenă
    (
        "Corpul pe scenă este important deoarece gesturile, distanța și poziția "
        "exprimă relații pe care cuvintele le omit — corpul nu trebuie ignorat "
        "în favoarea discursului intelectual și doar cuvintele au valoare terapeutică "
        "este o perspectivă incompletă pentru psihodramă."
    ),
    # 6 / item 36 — sociograma
    (
        "Sociograma este o hartă grafică a alegerilor și legăturilor dintre membrii "
        "grupului — creată de Moreno în cadrul sociometriei; nu interpretarea visului "
        "în sens freudian, nu ierarhia de expunere în fobii și nu genograma boweniană."
    ),
    # 7 / item 37 — exercițiul sociometric
    (
        "Exercițiul sociometric cu întrebarea 'Cu cine ai vrea să lucrezi la un "
        "proiect?' urmărește vizualizarea atracțiilor și structurii relaționale "
        "din grup — nu stabilirea diagnosticului medical, nu pedepsirea membrilor "
        "respinși și nu evitarea discuției despre relații."
    ),
    # 8 / item 38 — sociometria în încălzire
    (
        "Sociometria poate fi folosită în încălzirea grupei pentru a crește coeziunea "
        "și conștientizarea dinamicii interpersonale — nu înlocuiește complet faza "
        "de acțiune, nu respinge protagonistul și nu interpretează inconștientul "
        "colectiv jungian."
    ),
    # 9 / item 39 — membrul ales ca eur auxiliar
    (
        "Un membru constant ales ca eur auxiliar indică, în sociometrie, o poziție "
        "de încredere sau resursă percepută în grup — nu dovedește o tulburare psihotică "
        "certă, nu obligă persoana să devină director și nu indică absența oricărei relații."
    ),
    # 10 / item 40 — sociodrama în școală
    (
        "Sociodrama aplicată într-o școală poate pune în scenă conflicte de bullying "
        "sau excludere pentru conștientizare și schimbare — nu diagnosticul individual "
        "fără consimțământ, nu pedepsirea publică a elevilor și nu interpretarea "
        "visului directorului de școală."
    ),
    # 11 / item 41 — relații studiate scientific (Moreno)
    (
        "Moreno considera că relațiile din grup pot fi studiate științific prin "
        "sociometrie — alegeri, preferințe și repulsii vizibile; nu prin asociația "
        "liberă individuală, restructurarea cognitivă beckiană sau condiționarea "
        "operantă fără observație socială."
    ),
    # 12 / item 42 — multiselect sociometria
    (
        "Sociometria lui Moreno studiază structura relațiilor prin alegeri, poate fi "
        "folosită în încălzire sau evaluarea grupei și completează psihodrama. "
        "Ea nu respinge reprezentarea grafică — sociograma este tocmai o hartă grafică, "
        "element central al metodei."
    ),
    # 13 / item 43 — analiza după scenă vs împărtășire
    (
        "Analiza după scenă poate include clarificarea sensului scenei și legătura "
        "cu viața reală, nu doar reacțiile personale (care caracterizează mai mult "
        "împărtășirea) — nu obligă grupul să judece protagonistul, nu îl exclude "
        "și nu respinge orice reflecție."
    ),
    # 14 / item 44 — formularea corectă în împărtășire
    (
        "Formularea corectă în împărtășire este subiectivă, de tipul 'Când am văzut "
        "scena ta, am simțit/gândit…' — fără judecată morală. Sfaturile de tipul "
        "'ar fi trebuit să faci', evaluarea clinică sau acuzarea sunt formule "
        "de evitat în această fază."
    ),
    # 15 / item 45 — tema în faza de integrare
    (
        "Protagonistul care primește o temă de experimentat în viața reală se află "
        "în faza de integrare — transferul învățămintelor din scenă în cotidian; "
        "nu faza de încălzire, nu interpretarea freudiană a visului și nu token economy."
    ),
    # 16 / item 46 — confidențialitatea
    (
        "Confidențialitatea în grupul psihodramatic presupune protejarea conținutului "
        "împărtășit față de exteriorul grupului — publicarea scenelor pe rețele sociale, "
        "discutarea protagonistului fără acord sau invitarea publicului neautorizat "
        "sunt încălcări etice grave."
    ),
    # 17 / item 47 — contactul fizic
    (
        "Contactul fizic în psihodramă (ex. îmbrățișare în scenă) necesită consimțământ "
        "clar și respectarea limitelor protagonistului — nu este obligatoriu în orice "
        "scenă, nu înlocuiește consimțământul informat și nici nu este interzis "
        "în orice formă."
    ),
    # 18 / item 48 — catharsisul fără integrare
    (
        "Catharsisul fără integrare poate lăsa protagonistul epuizat emoțional, fără "
        "sens sau direcție clară — nu îl vindecă complet de la sine fără alte etape, "
        "nu îl obligă să repete aceeași scenă la infinit și nu îl scutește "
        "de faza de împărtășire."
    ),
    # 19 / item 49 — încălzirea prin joc de nume și mișcare
    (
        "Încălzirea prin joc de nume și mișcare simplă urmărește reducerea anxietății "
        "și creșterea spontaneității în grup — nu stabilirea ierarhiei familiale, "
        "nu interpretarea visului și nu disputa convingerilor iraționale (REBT)."
    ),
    # 20 / item 50 — montarea scenei din momentul ales
    (
        "Montarea scenei poate începe dintr-un moment ales de protagonist — respectând "
        "centrarea pe materialul relevant al protagonistului; nu este obligatorie "
        "reconstituirea întregii biografii, nu se impune interpretarea autoritară "
        "a directorului și nu se evită orice emoție."
    ),
    # 21 / item 51 — psihodrama organizațională
    (
        "Psihodrama în domeniul organizațional poate explora roluri profesionale, "
        "conflicte de echipă și comunicare prin scenă — nu exclusiv traume din "
        "copilărie fără context de muncă, nu restructurarea DSM la angajați "
        "și nu token economy în fabrică."
    ),
    # 22 / item 52 — psihodrama în doliu
    (
        "Psihodrama în doliu poate ajuta prin scene de despărțire sau mesaj nespus "
        "către persoana pierdută — nu prin interpretarea visului ca singură intervenție, "
        "nu prin evitarea oricărei emoții legate de pierdere și nu prin pedepsire."
    ),
    # 23 / item 53 — la vârstnici
    (
        "La vârstnici, psihodrama se adaptează prin scene mai scurte, ritm mai lent "
        "și respectarea limitelor fizice — nu aceleași exerciții ca la copii mici "
        "fără modificare, nu evitarea oricărui subiect al trecutului și nu grup "
        "mare fără contract de siguranță."
    ),
    # 24 / item 54 — psihodrama în penitenciar
    (
        "Psihodrama în context penitenciar, etic aplicată, poate viza responsabilizarea, "
        "roluri sociale și reintegrare prin acțiune — nu pedeapsa publică a "
        "deținuților prin scenă, nu divulgarea crimelor fără protecție și nu "
        "diagnosticul colectiv fără consimțământ."
    ),
    # 25 / item 55 — formarea terapeuților
    (
        "Formarea terapeuților prin psihodramă presupune adesea experiențierea "
        "rolurilor de protagonist, eur auxiliar și director — nu memorarea definițiilor "
        "fără practică scenică, nu evitarea participării proprii la grup și nu "
        "interpretarea autoritară a colegilor."
    ),
    # 26 / item 56 — grupul de adolescenți (sociodramă)
    (
        "Un grup de adolescenți care explorează presiunea colegilor printr-o scenă "
        "colectivă practică sociodramă sau psihodramă de grup pe temă socială — "
        "nu psihanaliză individuală, nu desensibilizare sistematică și nu terapia "
        "centrată pe realitate a lui Glasser."
    ),
    # 27 / item 57 — psihodrama nu înlocuiește medicația
    (
        "Psihodrama nu înlocuiește automat medicația sau tratamentul psihiatric "
        "deoarece este o metodă psihoterapeutică relațională, nu tratament medical "
        "— nu respinge colaborarea cu psihiatria și nu pretinde că vindecă orice "
        "tulburare prin scenă."
    ),
    # 28 / item 58 — ordinea etapelor
    (
        "Ordinea etapelor într-o ședință psihodramatică este: încălzire → acțiune "
        "→ împărtășire → analiză/integrare — ordinea inversă sau intercalarea "
        "pedepsei, a diagnosticului sau a token economy nu respectă structura metodei."
    ),
    # 29 / item 59 — multiselect psihodramă vs CBT
    (
        "Psihodrama: scenă, rol, grup, catharsis; CBT: restructurare cognitivă, "
        "exerciții, măsurare; ambele pot include teme pentru acasă, dar prin "
        "mijloace diferite. Disputa convingerilor 'trebuie' este specifică REBT "
        "(Albert Ellis), nu psihodramei moreniene."
    ),
    # 30 / item 60 — insight prin acțiune (scenariu)
    (
        "Clientul care înțelege pe scenă ce nu reușea să spună în cuvinte ilustrează "
        "insight-ul prin acțiune — principiul central al metodei lui Moreno. "
        "Nu dovedește eșecul psihodramei față de vorbire și nu înseamnă că "
        "scena trebuie eliminată sau că interpretarea freudiană a visului "
        "este superioară."
    ),
]

# ── Terapia Unificării Mitrofan — toți 100 de itemi ──────────────────────────
# idx 31–130 / exam 7759–7858

_MITROFAN_100: List[str] = [
    # 31 / item 1 — PEU — denumire
    (
        "Terapia Unificării, dezvoltată de Iolanda Mitrofan, este cunoscută și sub "
        "denumirea de Psihoterapia Experiențială a Unificării (PEU) — nu REBT "
        "(Ellis), nu analiza tranzacțională (Berne) și nu terapia centrată pe "
        "realitate (Glasser)."
    ),
    # 32 / item 2 — Iolanda Mitrofan
    (
        "Iolanda Mitrofan este asociată cu terapia unificării și orientarea "
        "experiențială holistică — nu cu psihodrama clasică (Moreno), nu cu CBT "
        "beckiană și nu cu analiza bioenergetică reichiană ca singura metodă "
        "inventată de ea."
    ),
    # 33 / item 3 — orientarea PEU
    (
        "Terapia Unificării se încadrează în orientarea experiențială, holistică "
        "și integrativă — nu în psihanaliza clasică centrată pe interpretarea "
        "visului latent, nu în behaviorismul pur și nu în orientarea vocatională "
        "standardizată."
    ),
    # 34 / item 4 — multiselect afirmații corecte despre PEU
    (
        "Terapia unificării pune accent pe experiența trăită, integrează dimensiuni "
        "corp–psihic–relațional–spiritual și valorizează autoschimbarea și "
        "responsabilitatea personală. Nu reduce clientul la un simptom de eliminat "
        "rapid fără explorare — acesta este opusul filosofiei mitrofaniene."
    ),
    # 35 / item 5 — PEU față de CBT
    (
        "Față de CBT, terapia unificării accesează experiența prin metaforă, simbol "
        "și trăire — nu exclusiv prin restructurare cognitivă; corpul și imaginația "
        "creatoare nu sunt excluse, iar disputa convingerilor iraționale nu este "
        "prioritatea centrală."
    ),
    # 36 / item 6 — filosofia de fond (răspuns ab)
    (
        "Filosofia de fond a PEU include influențe existențiale și fenomenologice "
        "și este centrată pe libertate, responsabilitate și sens — nu interpretare "
        "freudiană rigidă cu obligativitatea simbolului și nu behaviorism strict "
        "fără dimensiune subiectivă."
    ),
    # 37 / item 7 — axele integrate (răspuns ab)
    (
        "Axele integrate în modelul mitrofanian sunt conștient–inconștient–"
        "transconștient și corp–psihic împreună cu dimensiuni socio-spirituale "
        "— nu exclusiv cognițiile automate, nu numai transferul analitic pe canapea."
    ),
    # 38 / item 8 — contextele practicii (răspuns abc)
    (
        "Terapia unificării poate fi practicată individual, în grup, cu cuplul sau "
        "familia; cu adulți, adolescenți sau copii; în contexte clinice și de "
        "dezvoltare personală — nu este redusă la un test psihometric standardizat "
        "fără experiențiere."
    ),
    # 39 / item 9 — PEU urmărește reconectarea
    (
        "PEU urmărește reconectarea Egoului cu Sinele și activarea resurselor "
        "autotransformative — nu o interpretare unică impusă de terapeut, nu "
        "eliminarea imediată a simptomului fără trăire și nu evaluarea "
        "coeficientului de inteligență al grupului."
    ),
    # 40 / item 10 — TF: Mitrofan vs Moreno
    (
        "Adevărat: terapia unificării a fost dezvoltată de Iolanda Mitrofan, nu de "
        "Jacob Levy Moreno. Moreno este fondatorul psihodramei clasice — cele două "
        "metode, autori și instrumente centrale sunt distincte."
    ),
    # 41 / item 11 — starea de martor — instrument fundamental
    (
        "Instrumentul fundamental în terapia unificării este starea de martor — nu "
        "interpretarea freudiană a visului, nu condiționarea operantă și nu "
        "genograma, care aparțin altor orientări."
    ),
    # 42 / item 12 — starea de martor presupune (răspuns ab)
    (
        "Starea de martor presupune observarea experienței interioare în aici și "
        "acum, fără a evalua sau condamna prematur, ca martor imparțial al "
        "gândurilor, emoțiilor și imaginilor — nu reprimarea emoțiilor negative "
        "și nu identificarea totală cu fiecare gând automat."
    ),
    # 43 / item 13 — starea de martor vs pasivitate (răspuns ab)
    (
        "Starea de martor se deosebește de pasivitate prin faptul că implică prezență "
        "lucidă și contact cu trăirea și permite clarificarea experienței și asumarea "
        "responsabilității — nu înseamnă indiferență față de propria suferință și "
        "nu anulează nevoia de acțiune sau alegere personală."
    ),
    # 44 / item 14 — clientul blocat (răspuns ab)
    (
        "Când clientul se blochează sau fuge de experiența internă, terapeutul în "
        "PEU îl susține să revină treptat la observarea conștientă și îl ajută să "
        "practice starea de martor — nu îi impune o interpretare standard și nu îl "
        "obligă să elimine imediat orice emoție inconfortabilă."
    ),
    # 45 / item 15 — practicarea stării de martor favorizează (răspuns abc)
    (
        "Practicarea stării de martor favorizează distanțarea sănătoasă față de "
        "identificarea totală cu trăirea, accesul la părți reprimate sau negate "
        "anterior și clarificarea scenariilor interioare repetitive — nu anulează "
        "responsabilitatea personală pentru alegeri."
    ),
    # 46 / item 16 — starea de martor — răspuns b
    (
        "Starea de martor este echivalentă cu observarea fără judecată prematură "
        "a experienței în desfășurare (varianta b) — nu cu reținerea respirației "
        "până la amețeală, nu cu interpretarea autoritară a visului de către terapeut "
        "și nu cu identificarea completă cu rolul de victimă."
    ),
    # 47 / item 17 — starea de martor permite clientului (răspuns ab)
    (
        "Starea de martor permite clientului să nu mai fuzioneze total cu fiecare "
        "emoție sau gând și să devină mai permisiv cu procesele interioare — nu "
        "înseamnă evitarea permanentă a confruntării cu durerea și nu implică "
        "externalizarea responsabilității asupra terapeutului."
    ),
    # 48 / item 18 — starea de martor în sens mitrofanian (răspuns ab)
    (
        "Starea de martor mitrofaniană este strâns legată de conștientizarea acum-"
        "și-aici și de autoschimbarea prin observare lucidă, nu control rigid — nu "
        "implică dublul morenian ca instrument central obligatoriu și nu se reduce "
        "la disputa ellisiană a convingerilor iraționale."
    ),
    # 49 / item 19 — scenariu: clientul observă furia
    (
        "Un client care observă o emoție de furie fără a o reprima și fără a acționa "
        "impulsiv ilustrează starea de martor în terapia unificării — nu interpretarea "
        "transferului în psihanaliză, nu tehnica aversivă comportamentală "
        "și nu triangularea în terapia structurală de familie."
    ),
    # 50 / item 20 — TF: starea de martor presupune observarea fără confundare
    (
        "Adevărat: starea de martor în terapia unificării presupune observarea "
        "trăirilor fără confundare totală cu ele — aceasta este definiția esențială: "
        "prezență lucidă, nu fuzionare sau reprimare."
    ),
    # 51 / item 21 — multiselect: viziunea persoanei (răspuns abc)
    (
        "În PEU, persoana este văzută ca întreg (corp, emoții, cogniții, relații, sens), "
        "expert în propria experiență și sumă de fragmente adesea în conflict sau blocaj "
        "— nu ca obiect pasiv care așteaptă diagnosticul și interpretarea terapeutului."
    ),
    # 52 / item 22 — perspectiva holistică (răspuns ab)
    (
        "Perspectiva holistică mitrofaniană leagă suferința de fragmentare și blocaje "
        "între părți ale ființei și de separarea de propriile resurse și de sensul "
        "trăirii — nu de determinism genetic exclusiv, fără componentă psihologică."
    ),
    # 53 / item 23 — clientul nu este privit ca (răspuns ab)
    (
        "Clientul în PEU nu este privit ca simptom izolat decupat din context și nici "
        "ca obiect al interpretării unice impuse de terapeut — ci ca ființă cu "
        "demnitate, libertate și responsabilitate, capabilă de insight și "
        "autotransformare."
    ),
    # 54 / item 24 — corpul în PEU (răspuns ab)
    (
        "Corpul în terapia unificării este parte integrantă a sistemului psihic și "
        "mediu de exprimare și conștientizare a trăirii — nu este exclus din procesul "
        "terapeutic în favoarea discuției abstracte și nu este redus la simptom "
        "somatic fără legătură cu emoția."
    ),
    # 55 / item 25 — dimensiunea transpersonală (răspuns ab)
    (
        "Dimensiunea transpersonală sau transconștientă poate fi abordată prin "
        "metaforă, simbol și experiențe de sens existențial și meditație creativă "
        "cu explorarea valorilor profunde — nu prin testarea aptitudinilor "
        "logico-matematice și nu prin interpretarea jungiană obligatorie."
    ),
    # 56 / item 26 — simptomul în PEU (răspuns ab)
    (
        "Simptomul în PEU poate funcționa ca semnal al unei tensiuni sau fragmentări "
        "mai largi și ca punct de intrare în explorare experiențială și simbolică "
        "— nu ca obiectiv unic de eliminat fără înțelegerea contextului și nici ca "
        "dovadă că persoana nu are resurse interioare."
    ),
    # 57 / item 27 — potențialul creativ (răspuns ac)
    (
        "Potențialul creativ al clientului în PEU este resursă terapeutică activată "
        "prin artterapie și improvizație (a) și este legat de capacitatea de "
        "resemnificare a experienței (c) — nu este ignorat în favoarea explicațiilor "
        "intelectuale și nici rezervat doar artiștilor profesioniști."
    ),
    # 58 / item 28 — față de viziunea mecanicistă (răspuns ab)
    (
        "Față de viziunea mecanicistă, PEU consideră că omul trăiește și simbolizează "
        "experiența și poate alege și se poate autotransforma în relație cu sensul "
        "— nu este redus la reflex condiționat fără interioritate și are nevoie "
        "de relație terapeutică pentru schimbare."
    ),
    # 59 / item 29 — integrarea părților respinse (răspuns ab)
    (
        "Integrarea părților respinse sau neasumate ale personalității presupune "
        "contact cu emoții și aspecte anterior negate și recuperarea resurselor "
        "fragmentate — nu splitarea obligatorie în subpersonalități fixe diagnostice "
        "și nu evitarea oricărei vulnerabilități în cabinet."
    ),
    # 60 / item 30 — TF: persoana nu este redusă la simptom
    (
        "Adevărat: în terapia unificării, persoana nu este redusă la un simptom "
        "izolat, fără dimensiune holistică — perspectiva integrativă mitrofaniană "
        "include toate dimensiunile ființei: corp, emoții, cogniții, relații și sens."
    ),
    # 61 / item 31 — multiselect: scopul terapiei (răspuns abc)
    (
        "Scopul terapiei unificării este orientat spre unificarea dimensiunilor aflate "
        "în conflict, autotransformare/maturizare emoțională și relațională și "
        "congruență corp–emoții–valori–acțiune — nu eliminarea imediată a simptomului "
        "fără explorare experiențială."
    ),
    # 62 / item 32 — unificarea presupune (răspuns ab)
    (
        "Unificarea presupune armonizarea părților interioare într-o coerență "
        "experiențială și trecerea de la reacții automate la alegeri asumate "
        "— nu renunțarea la orice relație interpersonală și nu preferința pentru "
        "explicația abstractă în locul trăirii."
    ),
    # 63 / item 33 — procesul de unificare (răspuns abc)
    (
        "Procesul de unificare poate include integrare internă și transgresarea "
        "limitelor vechi, restructurare experiențială și insight ('aha') și "
        "resemnificarea experienței trăite prin metaforă — nu rescrierea biografiei "
        "clientului fără consimțământ."
    ),
    # 64 / item 34 — autoschimbarea (răspuns ab)
    (
        "Autoschimbarea în PEU înseamnă învățarea strategiei de a lucra asupra "
        "propriei experiențe și activarea resurselor personale, nu dependența "
        "de un salvator extern — nu aplicarea unui protocol fix identic pentru toți "
        "și nu anularea libertății de alegere."
    ),
    # 65 / item 35 — transformarea personală (răspuns abc)
    (
        "Transformarea personală în PEU poate viza eliberarea de blocaje, creșterea "
        "libertății de alegere asumată și consolidarea identității prin contact cu "
        "sensul existențial — nu conformarea la valorile impuse autoritar de terapeut."
    ),
    # 66 / item 36 — acceptarea ca premisă (răspuns ab)
    (
        "Acceptarea în PEU permite recunoașterea lucidă a ceea ce este prezent și "
        "deschide contactul cu părți reprimate fără aprobare pasivă a oricărui "
        "comportament — nu înseamnă respingerea tuturor emoțiilor negative "
        "și nu exclude confruntarea cu durerea."
    ),
    # 67 / item 37 — echilibrul și sănătatea psihică (răspuns ab)
    (
        "Echilibrul și sănătatea psihică în PEU sunt asociate cu reunificarea "
        "părților interioare și trăirea conștientă, întreagă și cu armonizarea "
        "gândurilor, emoțiilor, corpului și spiritului — nu cu evitarea permanentă "
        "a inconfortului sau externalizarea responsabilității."
    ),
    # 68 / item 38 — scopul nu este (răspuns a)
    (
        "Scopul terapiei unificării nu este adaptarea clientului la o singură "
        "interpretare impusă de terapeut (a) — este, dimpotrivă, integrarea "
        "experienței, coerența interioară, capacitatea de martor și activarea "
        "resurselor autotransformative."
    ),
    # 69 / item 39 — resemnificarea (răspuns ab)
    (
        "Resemnificarea experienței trăite urmărește transformarea sensului personal "
        "al unei trăiri dificile și accesul la perspective noi prin simbol și "
        "metaforă — nu impunerea unei chei universale freudiene de decodare "
        "și nu eliminarea memoriei biografice prin sugestie."
    ),
    # 70 / item 40 — TF: reunificarea vs suprimarea
    (
        "Adevărat: terapia unificării urmărește reunificarea părților interioare, "
        "nu doar suprimarea simptomului — aceasta este esența abordării mitrofaniene "
        "față de metodele simptom-focale."
    ),
    # 71 / item 41 — multiselect: etape ale procesului (răspuns abcd)
    (
        "Procesul terapeutic în PEU include toate patru etape: provocare sau "
        "activare, explorare experiențială, analiză și integrare, restructurare "
        "și autotransformare (răspuns abcd) — niciuna nu este excludentă."
    ),
    # 72 / item 42 — faza de provocare/activare (răspuns ab)
    (
        "Faza de provocare/activare presupune contact cu o temă, emoție sau imagine "
        "relevantă și trezirea disponibilității de a explora, nu interpretare "
        "autoritară — nu stabilirea diagnosticului DSM înainte de relație "
        "și nu pedepsire pentru rezistență."
    ),
    # 73 / item 43 — explorarea experiențială (răspuns ab)
    (
        "Explorarea experiențială în PEU poate folosi exprimare verbală, corporală, "
        "plastică sau dramatică și joc de rol și scenariu simbolic — nu exclusiv "
        "discuție intelectuală fără implicare trăită și nu numai teste projective "
        "standardizate."
    ),
    # 74 / item 44 — analiza și integrarea (răspuns ab)
    (
        "Analiza și integrarea vizează clarificarea sensului personal al trăirii "
        "explorate și legătura între experiență, valori și alegeri de viață — nu "
        "interpretarea obligatorie a visului în cheie jungiană și nu evitarea "
        "oricărei reflecții după exercițiu."
    ),
    # 75 / item 45 — restructurarea experiențială vs beckiană (răspuns ab)
    (
        "Restructurarea experiențială în PEU pornește din trăire și simbol și include "
        "corpul, metafora și insight-ul — față de restructurarea beckiană, care "
        "identifică distorsiunile cognitive prin argumentație rațională; PEU nu "
        "exclude emoția și corpul și nu impune o listă fixă de gânduri înlocuitoare."
    ),
    # 76 / item 46 — abordarea diferențială (răspuns ab)
    (
        "Abordarea diferențială înseamnă că intervenția se adaptează persoanei, "
        "problemei și momentului terapeutic și tehnicile se aleg în funcție de "
        "nevoile clientului — nu un protocol fix indiferent de context și nu "
        "tratarea mecanică a cauzei fără trăire sau simbolizare."
    ),
    # 77 / item 47 — punctul de plecare (răspuns ab)
    (
        "Punctul de plecare în PEU este experiența trăită de client și prezența "
        "în aici și acum — nu schema ierarhică a familiei extinse ca prim pas "
        "obligatoriu și nu lista de pedepse și recompense comportamentale."
    ),
    # 78 / item 48 — momente de tip insight (răspuns ab)
    (
        "Procesul terapeutic mitrofanian poate facilita insight-ul sau 'aha' cu "
        "reorganizare a experienței și contact profund cu o emoție sau imagine "
        "semnificativă — nu conformare automată la așteptările terapeutului "
        "și nu evitare permanentă a vulnerabilității."
    ),
    # 79 / item 49 — etapa de integrare după exercițiu (răspuns ab)
    (
        "După un exercițiu metaforic intens, etapa de integrare urmărește legarea "
        "simbolului de viața concretă a clientului și consolidarea stării de martor "
        "asupra a ce s-a trăit — nu impunerea interpretării standard de grup "
        "și nu trecerea imediată la alt client fără ancorație."
    ),
    # 80 / item 50 — TF: cauza prin trăire și simbolizare
    (
        "Adevărat: în terapia unificării, cauza problemei este adesea abordată "
        "prin trăire și simbolizare, nu doar prin explicație intelectuală — aceasta "
        "diferențiază PEU de abordările exclusiv cognitive care prioritizează "
        "argumentația rațională."
    ),
    # 81 / item 51 — metafora în PEU (răspuns ab)
    (
        "Metafora permite accesul indirect la conținuturi greu de formulat rațional "
        "și explorarea blocajelor, resurselor și dorințelor în mod simbolic — nu "
        "interpretare rigidă impusă independent de client și nu înlocuiește "
        "consimțământul informat."
    ),
    # 82 / item 52 — multiselect: strategii și tehnici (răspuns abcd)
    (
        "Strategii și tehnici în PEU includ: joc de rol și scenariu simbolic; "
        "lucrul cu visul în sens personal al clientului; exerciții corporale, "
        "expresive și artterapeutice; meditație creativă și imaginație ghidată "
        "(abcd) — toate sunt vehicule ale autocunoașterii mitrofaniene."
    ),
    # 83 / item 53 — vehiculele autocunoașterii (răspuns abc)
    (
        "PEU utilizează ca vehicule: improvizația dramaterapeutică și expresia "
        "corporală; artterapia (desen, modelaj, colaj, lut); improvizația metaforică "
        "și narativă — nu exclusiv interpretarea liberă pe canapea fără acțiune "
        "sau simbol."
    ),
    # 84 / item 54 — lucrul cu măști sau marionete (răspuns ab)
    (
        "Lucrul cu măști sau marionete poate facilita explorarea rolurilor și a "
        "părților interne prin simbol și distanțare creatoare față de conținuturi "
        "greu de abordat direct — nu este spectacol artistic pentru public extern "
        "și nu este diagnosticarea obligatorie a tulburării de personalitate."
    ),
    # 85 / item 55 — reconversia polarităților (răspuns ab)
    (
        "Improvizația centrată pe reconversia polarităților urmărește integrarea "
        "opozițiilor interne (ex. putere–vulnerabilitate) și depășirea blocajelor "
        "prin acțiune simbolică în prezent — nu menținerea permanentă a unui singur "
        "pol activ și nu evitarea tensiunii emoționale în grup."
    ),
    # 86 / item 56 — exerciții metaforice cu teme naturale (răspuns ab)
    (
        "Exercițiile metaforice cu teme precum apa, muntele sau drumul au scop "
        "terapeutic și de restructurare experiențială și de explorare simbolică "
        "a resurselor și fricilor personale — nu sunt decorative și nu sunt "
        "destinate evaluării psihometrice a inteligenței fluid."
    ),
    # 87 / item 57 — lucrul cu visul în PEU (răspuns ab)
    (
        "Lucrul cu visul în PEU urmărește semnificațiile personale ale imaginilor "
        "onirice și accesul la material simbolic relevant pentru client — nu o "
        "cheie universală de decodare freudiană obligatorie și nu eliminarea "
        "viselor prin sugestie hipnotică."
    ),
    # 88 / item 58 — meditația creativă (răspuns ab)
    (
        "Meditația creativă în PEU poate include imaginație ghidată cu suport vizual, "
        "sonor sau corporal și clarificarea și reorganizarea experienței interioare "
        "— nu evitarea oricărei implicări emoționale și nu implică obligativitatea "
        "relaxării musculare progresive."
    ),
    # 89 / item 59 — elemente naturale (răspuns ab)
    (
        "Elementele naturale (pietre, scoici, frunze, lut) în PEU sunt folosite "
        "pentru valoarea proiectivă și simbolică în improvizația creatoare și pentru "
        "ancorarea concretă a explorării metaforice — nu sunt decor de cabinet fără "
        "funcție terapeutică și nu înlocuiesc relația terapeutică."
    ),
    # 90 / item 60 — TF: exerciții metaforice au scop de restructurare
    (
        "Adevărat: exercițiile metaforice în terapia unificării au scop de "
        "restructurare experiențială, nu sunt joc gratuit — ele urmăresc explorarea "
        "și integrarea experienței personale cu sens terapeutic explicit."
    ),
    # 91 / item 61 — rolul terapeutului (răspuns ab)
    (
        "Terapeutul în PEU are rol de martor, facilitator și însoțitor al procesului "
        "și creator al unui cadru sigur pentru experiențiere și simbolizare — nu "
        "expert care impune un singur sens corect al experienței și nu judecător "
        "moral al alegerilor clientului."
    ),
    # 92 / item 62 — terapeutul nu (răspuns ab)
    (
        "Terapeutul în PEU nu impune interpretarea unică și obligatorie a metaforei "
        "clientului și nu înlocuiește responsabilitatea și expertiza clientului "
        "asupra propriei vieți — facilitează revenirea la starea de martor și creează "
        "condiții pentru explorare experiențială responsabilă."
    ),
    # 93 / item 63 — relația terapeutică (răspuns ab)
    (
        "Relația terapeutică în PEU se bazează pe încredere, respect și colaborare "
        "și pe empatie și prezență autentică a terapeutului — nu pe dependența "
        "indusă a clientului de salvator extern și nu pe secretizarea limitelor "
        "și riscurilor intervenției."
    ),
    # 94 / item 64 — competența terapeutului (răspuns ab)
    (
        "Competența terapeutului în PEU include formare în orientarea experiențială "
        "a unificării și capacitatea de a lucra cu metaforă, simbol și grup — nu "
        "libertatea de a folosi orice tehnică fără pregătire sau supervizare "
        "și nu impunerea valorilor personale ca normă pentru client."
    ),
    # 95 / item 65 — terapeutul ca martor al procesului (răspuns ab)
    (
        "Terapeutul care funcționează ca martor al procesului observă și susține "
        "fără a se confunda cu experiența clientului și intervine pentru reancorare "
        "când clientul evită sau se blochează — nu oferă soluții prefabricate "
        "și nu evită orice intervenție activă."
    ),
    # 96 / item 66 — terapeutul în grupul PEU (răspuns ab)
    (
        "În grupul PEU, terapeutul menține cadrul de siguranță și regulile procesului "
        "și facilitează metafora colectivă și rezonanța între participanți — nu "
        "impune interpretări morale protagonistului și nu înlocuiește consimțământul "
        "informat pentru exerciții."
    ),
    # 97 / item 67 — autenticitatea terapeutului (răspuns ab)
    (
        "Autenticitatea terapeutului trebuie distinsă de confesiunea nelimitată care "
        "folosește clientul pentru nevoile personale și de depășirea limitelor "
        "profesionale ale relației — autenticitatea constă în prezența congruentă "
        "cu autocunoaștere și clarificarea rolului de la început."
    ),
    # 98 / item 68 — supervizarea (răspuns ab)
    (
        "Supervizarea terapeutului în PEU este relevantă când cazul depășește "
        "competența sau implică risc și când apar dileme etice sau blind spots "
        "personale — nu este opțională la latitudinea exclusivă a terapeutului "
        "care se consideră perfect sigur."
    ),
    # 99 / item 69 — TF: terapeutul respectă clientul ca expert
    (
        "Adevărat: terapeutul în terapia unificării respectă clientul ca expert "
        "al propriei experiențe — expertiza terapeutului vizează facilitarea "
        "procesului, nu deținerea adevărului despre experiența subiectivă a clientului."
    ),
    # 100 / item 70 — TF: terapeutul oferă interpretarea corectă unică
    (
        "Fals: terapeutul în PEU nu trebuie să ofere interpretarea corectă unică "
        "a fiecărei metafore — clientul este cel care construiește semnificația "
        "personală; terapeutul facilitează și însoțește procesul, nu îl impune."
    ),
    # 101 / item 71 — psihodrama vs PEU (răspuns ab)
    (
        "Psihodrama (Moreno) și PEU (Mitrofan) sunt amândouă experiențiale, dar "
        "psihodrama centrează scena, rolul, protagonistul și directorul, iar PEU "
        "centrează metafora, martorul interior și integrarea holistică — nu au "
        "același autor și PEU nu exclude corpul și simbolul."
    ),
    # 102 / item 72 — PEU față de psihodramă (răspuns ab)
    (
        "Față de psihodrama clasică, PEU pune accent mai mare pe starea de martor "
        "și observarea procesului interior și pe metaforă, resemnificare și integrare "
        "holistică — sociometria și tele-ul sunt instrumente moreniene, nu centrale "
        "în PEU; faza de împărtășire nu este momentul definitoriu unic al PEU."
    ),
    # 103 / item 73 — PEU față de Gestalt (răspuns ab)
    (
        "Față de Gestalt (Perls), PEU împărtășește orientarea experiențială și "
        "contactul cu aici și acum, dar PEU își definește explicit instrumentul "
        "central ca stare de martor și unificare — nu se identifică cu tehnica "
        "scaunului gol ca singur procedeu și nu respinge metafora sau simbolul."
    ),
    # 104 / item 74 — PEU față de Rogers (răspuns ab)
    (
        "Față de terapia centrată pe persoană (Rogers), PEU adaugă o paletă bogată "
        "de tehnici simbolice și expresiv-creative și păstrează respectul față de "
        "client și potențialul de creștere — nu renunță la empatie în favoarea "
        "interpretării autoritare și nu exclude acceptarea și relația autentică."
    ),
    # 105 / item 75 — multiselect perechi corecte autor–orientare (răspuns ab)
    (
        "Perechi corecte: Iolanda Mitrofan — terapia unificării; Jacob Levy Moreno "
        "— psihodramă clasică. Greșite: Mitrofan nu a inventat psihodrama clasică; "
        "starea de martor ca instrument central PEU aparține mitrofanismului, "
        "nu lui Moreno."
    ),
    # 106 / item 76 — PEU și analiza bioenergetică (răspuns ab)
    (
        "PEU și analiza bioenergetică (Lowen) pot împărtăși accentul pe corp și "
        "eliberarea tensiunilor prin experiență și orientarea holistică asupra "
        "persoanei — dar au identitate metodologică proprie și autori fondatori "
        "diferiți; nu sunt identice."
    ),
    # 107 / item 77 — PEU nu este echivalentă cu (răspuns ab)
    (
        "PEU nu este echivalentă cu psihodrama clasică moreniană, deși poate folosi "
        "joc de rol, și nici cu terapia rațional-emotivă a lui Ellis — PEU este o "
        "abordare integrativă cu metaforă și martor interior, care lucrează "
        "experiențial cu simbol și corp."
    ),
    # 108 / item 78 — jocul de rol în PEU vs psihodramă (răspuns ab)
    (
        "Jocul de rol în PEU diferă de psihodramă deoarece poate fi mai scurt, "
        "simbolic și centrat pe metaforă și nu presupune obligatoriu director, "
        "protagonist și fazele clasice moreniene — nu exclude componenta dramatică "
        "și nu înlocuiește consimțământul informat."
    ),
    # 109 / item 79 — starea de martor vs mindfulness (răspuns ab)
    (
        "Starea de martor se aseamănă parțial cu atenția mindfulness, dar în PEU "
        "este integrată într-un cadru terapeutic holistic mitrofanian și este legată "
        "de unificare, metaforă și autotransformare — nu este identică cu expunerea "
        "progresivă comportamentală și nu se reduce la relaxare musculară."
    ),
    # 110 / item 80 — TF: Moreno vs Mitrofan — autori
    (
        "Adevărat: Jacob Levy Moreno este fondatorul psihodramei clasice; Iolanda "
        "Mitrofan este fondatoarea terapiei unificării — cele două metode au autori, "
        "instrumente centrale și specificitate metodologică distincte."
    ),
    # 111 / item 81 — indicații pentru PEU (răspuns ab)
    (
        "Terapia unificării poate fi indicată pentru blocaje emoționale, impasuri "
        "existențiale și dificultăți relaționale când clientul poate lucra "
        "experiențial — nu este indicată când clientul refuză categoric orice simbol "
        "sau metaforă; tulburările cu componentă biologică gravă necesită evaluare medicală."
    ),
    # 112 / item 82 — scenariu: podul fragil (răspuns ab)
    (
        "Un client care descrie un pod fragil peste apă tulbure beneficiază în PEU "
        "de explorarea semnificațiilor personale ale imaginii și a blocajului resimțit "
        "și de accesarea resurselor și fricilor prin simbol — nu diagnosticarea "
        "psihozei fără evaluare clinică și nu eliminarea emoției prin respirație forțată."
    ),
    # 113 / item 83 — grupul în PEU (răspuns ab)
    (
        "În grupul PEU, metafora colectivă facilitează oglindirea experiențelor "
        "între participanți și rezonanța, sprijinul reciproc și experimentarea "
        "simbolică — nu înlocuiește consimțământul informat pentru fiecare exercițiu "
        "și nu autorizează judecarea morală a protagonistului."
    ),
    # 114 / item 84 — la copii și adolescenți (răspuns ab)
    (
        "La copii și adolescenți, PEU poate folosi joc simbolic, desen și exprimare "
        "corporală adaptate vârstei și metaforă și artterapie pentru accesul la trăiri "
        "greu de verbalizat — nu interpretarea autoritară a visului fără adaptare "
        "la vârstă și nu excluderea completă a părinților."
    ),
    # 115 / item 85 — autoacceptarea în PEU (răspuns ab)
    (
        "Autoacceptarea permite contact cu emoții, vulnerabilități și resurse "
        "interioare și este premisa integrării, fără a aproba pasiv comportamentele "
        "dăunătoare — nu înseamnă evitarea confruntării cu durerea și nu anulează "
        "responsabilitatea personală."
    ),
    # 116 / item 86 — scenariu: clientul furios (răspuns ab)
    (
        "Terapeutul în PEU va susține practica stării de martor și explorarea sensului "
        "furiei și va facilita integrarea emoției în contextul mai larg al experienței "
        "— nu îi va spune clientului să ignore furia până dispare și nu îi va "
        "oferi interpretarea corectă standard."
    ),
    # 117 / item 87 — grupul ca spațiu (răspuns ab)
    (
        "Grupul în PEU poate funcționa ca spațiu de oglindire, susținere și "
        "experimentare și cadru pentru metaforă colectivă și învățare reciprocă "
        "— nu ca arenă de evaluare psihometrică fără reguli de siguranță și nu "
        "înlocuiește terapia individuală pentru toate cazurile clinice grave."
    ),
    # 118 / item 88 — PEU în cuplu/familie (răspuns ab)
    (
        "Terapia unificării în cuplu sau familie poate explora patternuri relaționale "
        "și tensiuni prin simbol și joc de rol și resurse comune și blocaje de "
        "comunicare experiențial — nu exclusiv prin contractul WDEP al terapiei "
        "centrate pe realitate și nu prin restructurare cognitivă exclusivă."
    ),
    # 119 / item 89 — evitarea experienței interne (răspuns ab)
    (
        "Evitarea experienței interne de către client în PEU este semnal că procesul "
        "poate fi abordat treptat prin martor și metaforă și este o temă relevantă, "
        "nu simplu 'rezistență' de pedepsit — nu dovedește că metoda nu se aplică "
        "niciodată și nu autorizează moralizarea."
    ),
    # 120 / item 90 — TF: simptomul ca obiectiv de eliminat
    (
        "Fals: în terapia unificării, simptomul nu este văzut doar ca obiectiv de "
        "eliminat rapid fără legătură cu tensiuni mai largi — simptomul este semnal "
        "al fragmentărilor existențiale și punct de intrare în explorarea holistică."
    ),
    # 121 / item 91 — multiselect: cadrul metodologic PEU (răspuns abc)
    (
        "Cadrul metodologic al PEU include experiențiere, simbolizare și metaforă; "
        "stare de martor și integrare restructurativă; joc de rol, lucru corporal "
        "și meditație creativă. Dublul, oglinda și sociometria ca instrumente "
        "definitorii obligatorii aparțin psihodramei clasice moreniene."
    ),
    # 122 / item 92 — multiselect: greșeli despre starea de martor (răspuns ab)
    (
        "Afirmații greșite despre starea de martor: a presupune reprimarea emoțiilor "
        "pentru calm superficial și b că înseamnă indiferență față de propria "
        "suferință. Starea de martor implică de fapt observare lucidă și contact "
        "(c) și susținerea clarificării și asumării responsabilității (d)."
    ),
    # 123 / item 93 — multiselect: scopul PEU (răspuns abc)
    (
        "Scopul PEU corect: unificarea părților interioare aflate în conflict (a), "
        "creșterea coerenței între trăire, valori și acțiune (b), autoschimbare "
        "și activarea resurselor personale (c) — conformarea la interpretarea "
        "terapeutului ca singur adevăr (d) este opusul scopului mitrofanian."
    ),
    # 124 / item 94 — multiselect: tehnici NU centrale în PEU (răspuns ab)
    (
        "Tehnici NU centrale, definitorii pentru PEU: disputa convingerilor iraționale "
        "din REBT (a) și sociometria și atomul social morenian (b) — metafora, "
        "artterapia și starea de martor (c) și improvizația simbolică și integrarea "
        "holistică (d) sunt tocmai instrumente centrale în PEU."
    ),
    # 125 / item 95 — unificarea — congruența (răspuns ab)
    (
        "Unificarea vizează congruența între corp, emoții, gânduri, valori și "
        "acțiune și între experiența interioară și alegerile asumate în viață — "
        "nu eliminarea rapidă a simptomului fără explorare și nu dependența "
        "de terapeut ca salvator."
    ),
    # 126 / item 96 — acceptarea vs aprobarea pasivă (răspuns ab)
    (
        "Acceptarea se deosebește de aprobarea pasivă deoarece recunoaște ce este "
        "prezent fără a legitima orice comportament dăunător și deschide calea "
        "spre integrare și alegere responsabilă — nu renunță la discernământ "
        "moral și nu exclude confruntarea cu consecințele acțiunilor."
    ),
    # 127 / item 97 — PEU utilizează puterea (răspuns ab)
    (
        "PEU utilizează puterea metaforei și resemnificării experienței trăite și "
        "a exercițiului provocator, improvizației și meditației creatoare — nu "
        "interpretarea unică impusă de manualul freudian și nu condiționarea "
        "aversivă ca metodă centrală."
    ),
    # 128 / item 98 — TF: metoda românească
    (
        "Adevărat: terapia unificării este o metodă românească de orientare "
        "experiențială holistică — dezvoltată de Iolanda Mitrofan în România, "
        "integrând influențe existențiale, fenomenologice și expresiv-creative "
        "într-un model holistic propriu."
    ),
    # 129 / item 99 — TF: starea de martor presupune evaluare și condamnare
    (
        "Fals: starea de martor nu presupune evaluarea și condamnarea rapidă a "
        "fiecărei emoții — dimpotrivă, presupune observarea fără judecată prematură "
        "a experienței în desfășurare, ca premisă a contactului și integrării."
    ),
    # 130 / item 100 — TF: integrarea tehnicilor din orientări diverse
    (
        "Adevărat: terapia unificării integrează tehnici din orientarea existențială, "
        "gestaltterapie și dramaterapie în cadrul unui model holistic propriu — "
        "caracterul integrativ și original este definitotoriu pentru PEU mitrofaniană."
    ),
]

# ── Asamblare ─────────────────────────────────────────────────────────────────

PART8_EXPLANATIONS: List[str] = (
    _PSYCHODRAMA_EXTRA_LAST31
    + _MITROFAN_100
)

assert len(PART8_EXPLANATIONS) == 131
