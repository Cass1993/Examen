"""Explicații pedagogice — lot Introducere în evaluarea psihologică II (100 itemi)."""

from __future__ import annotations

from typing import List

# Ordinea corespunde: 50 itemi intro evaluare + 50 itemi perspectivă psihometrică.
EXPLANATIONS: List[str] = [
    # —— 1–5: Necesitatea evaluării ——
    (
        "Evaluarea psihologică există pentru a sprijini decizii informate despre "
        "diferențele individuale, pe baza unor date colectate sistematic. Scopul nu "
        "este eliminarea variabilității umane, ci descrierea și compararea ei cât "
        "mai obiectiv posibil (Urbina; standardele profesionale în evaluare)."
    ),
    (
        "Conform lui Urbina, testele psihometrice eșantionează comportamente "
        "relevante pentru funcționarea cognitivă și afectivă, nu orice comportament "
        "la întâmplare. Relevanța față de constructul măsurat este o condiție "
        "de bază a măsurătorii psihologice."
    ),
    (
        "Un test psihometric valorează prin standarde explicite de administrare, "
        "scorare și interpretare — nu prin impresii nesistematice. Standardizarea "
        "face posibilă compararea rezultatelor și reduce arbitrariul deciziei."
    ),
    (
        "Evaluarea psihologică completează, nu înlocuiește judecata clinică sau "
        "organizațională. Datele din teste trebuie integrate cu contextul, "
        "istoricul și observația, mai ales în decizii complexe."
    ),
    (
        "Compararea între persoane sau în timp presupune aceleași reguli de "
        "administrare și barem de notare (standardizare). Replicabilitatea "
        "deciziilor între evaluatori crește când procedura este explicită; "
        "subiectivitatea nu dispare complet, dar este controlată."
    ),
    # —— 6–12: Domenii aplicative ——
    (
        "În practica clinică, evaluarea servește diagnosticului, prognosticului, "
        "monitorizării evoluției și verificării efectelor intervenției (inclusiv "
        "design test–retest). Nu se limitează la o singură metodă sau la selecție "
        "organizațională."
    ),
    (
        "Inventarul Multifazic de Personalitate Minnesota, Inventarul Clinic "
        "Multiaxial Millon și testele proiective (ex. Rorschach) sunt instrumente "
        "frecvent întâlnite în evaluarea clinică. Scala de inteligență nu este "
        "singurul instrument obligatoriu — evaluarea clinică este multimodală."
    ),
    (
        "În domeniul organizațional, evaluarea leagă adesea predictorii (teste, "
        "simulări) de criteriul de performanță la job. Centrele de evaluare a "
        "competențelor combină mai multe metode pentru o estimare mai solidă a "
        "potențialului profesional."
    ),
    (
        "Evaluarea educațională sprijină orientarea vocațională, consilierea "
        "școlară și identificarea dificultăților de învățare sau maladaptării. "
        "Selecția managerială și diagnosticul exclusiv psihotic țin de alte "
        "domenii de aplicare."
    ),
    (
        "Scopul prognostic vizează evoluția viitoare, riscurile și factorii de "
        "protecție — nu doar descrierea simptomelor prezente. Prognosticul "
        "informează planificarea intervenției și monitorizarea în timp."
    ),
    (
        "Centrele de evaluare a competențelor folosesc adesea simulări de lucru, "
        "exerciții structurate, interviu și teste standardizate. O singură probă "
        "scrisă sau doar chestionare de personalitate, fără legătură cu criteriul "
        "de job, nu acoperă complexitatea rolului."
    ),
    (
        "Validarea intervenției prin test–retest presupune aceeași măsurătoare "
        "la momente diferite (înainte și după), pentru a observa schimbarea. "
        "Schimbarea instrumentului la fiecare administrare împiedică compararea "
        "directă a evoluției."
    ),
    # —— 13–24: Predictor–criteriu și erori ——
    (
        "În matricea predictor–criteriu, combinațiile dezirabile sunt: scor înalt "
        "la test cu performanță înaltă la criteriu, și scor scăzut cu performanță "
        "scăzută. Acestea reflectă o predicție corectă în selecție."
    ),
    (
        "Scor înalt la test, dar performanță slabă la job = predicție pozitivă "
        "greșită. În logica selecției, aceasta corespunde erorii de tip I: "
        "„acceptăm” pe cineva (ca fiind potrivit) deși nu era."
    ),
    (
        "Scor scăzut la test, dar performanță bună dacă ar fi fost angajat = "
        "predicție negativă greșită. În selecție, aceasta este echivalentul "
        "erorii de tip II: respingem pe cineva potrivit."
    ),
    (
        "Respingerea unui candidat cu scor scăzut care, oricum, ar fi avut "
        "performanță slabă este o decizie corectă — nu o eroare. Eroarea apare "
        "când respingem pe cineva care ar fi reușit (tip II) sau acceptăm pe "
        "cineva care eșuează (tip I)."
    ),
    (
        "Respingerea unui candidat cu scor scăzut care ar fi avut performanță "
        "bună este eroare de tip II (fals negativ în selecție), nu tip I. Tip I "
        "înseamnă acceptarea greșită: scor înalt, performanță slabă."
    ),
    (
        "Eroarea de tip I în statistica ipotezelor = respingerea ipotezei nule "
        "când ea este adevărată (fals pozitiv). Concluzionăm că există un efect "
        "care, de fapt, nu există."
    ),
    (
        "Eroarea de tip II = acceptarea ipotezei nule când ea este falsă (fals "
        "negativ). Ratăm un efect sau o diferență reală. În selecție, analogia "
        "este respingerea unui candidat potrivit."
    ),
    (
        "Un test foarte strict reduce angajările greșite (tip I în selecție), "
        "dar crește riscul de a respinge candidați buni (tip II). Există un "
        "compromis între cele două tipuri de erori — nu le putem elimina pe "
        "ambele simultan fără a schimba calitatea testului."
    ),
    (
        "Un test foarte permisiv angajează aproape pe toată lumea: scad erorile "
        "de tip II (mai puțini respinși pe nedrept), dar cresc erorile de tip I "
        "(mai mulți angajați nepotriviți). Validitatea predictivă nu este "
        "garantată de permisivitate."
    ),
    (
        "Corelația apropiată de zero între test și criteriu indică validitate "
        "predictivă slabă: scorul la test nu se leagă semnificativ de performanța "
        "reală. Deciziile bazate pe un astfel de test pot semăna cu un proces "
        "aproape aleatoriu."
    ),
    (
        "Tip I și tip II au sens atât în testarea ipotezelor, cât și în selecție "
        "(cu mapare diferită). În selecție: scor înalt + performanță slabă ≈ tip I; "
        "scor scăzut + performanță înaltă ≈ tip II. Nu confunda tip II cu tip I."
    ),
    # —— 25–36: Cantitativ/calitativ; obiectiv/subiectiv ——
    (
        "Metodele cantitative produc date numerice, comparabile, cu reguli explicite "
        "de administrare și notare (teste, chestionare standardizate, observație "
        "codificată). Accentul este pe măsurare și comparabilitate."
    ),
    (
        "Metodele calitative explorează sensuri și contexte prin interviu, observație "
        "sau grup focal. Nu presupun obligatoriu scoruri standardizate; "
        "interpretarea umană este parte din proces, nu o „defectiune”."
    ),
    (
        "Nici cantitativul, nici calitativul nu este superior în mod absolut — "
        "depinde de întrebarea de cercetare sau de scopul evaluării. Abordarea "
        "mixtă (mixed methods) este frecventă și utilă în practică."
    ),
    (
        "Combinarea metodelor (teste + interviu, chestionar + observație) permite "
        "atât comparabilitate numerică, cât și înțelegere aprofundată — triangularea "
        "datelor. O singură metodă sau doar tehnici proiective fără criterii "
        "explicite limitează concluziile."
    ),
    (
        "Un rezultat obiectiv poate fi reprodus de alți evaluatori folosind aceleași "
        "reguli; nu depinde de impresia unui singur clinician. Obiectivitatea este "
        "graduală, nu absolută — chiar și testele standardizate au limite."
    ),
    (
        "Rezultatele subiective depind de interpretarea evaluatorului: subteste "
        "deschise notate cu judecată clinică, analiză proiectivă fără barem fix. "
        "Notarea automată sau cu cheie unică tinde spre obiectivitate."
    ),
    (
        "La scala Wechsler pentru adulți, unele subteste deschise (ex. similitudini, "
        "comprehensiune) necesită judecată în notare, deci au componentă subiectivă "
        "controlată prin barem. Nu tot testul este 100% automatizat."
    ),
    (
        "Chestionarele cu barem fix sunt mai obiective decât interviul nestructurat "
        "pentru că notarea urmează reguli explicite și reduce dependența de un "
        "singur evaluator. Nu elimină nevoia de validare a instrumentului."
    ),
    (
        "Testele de aptitudini și observația cu barem sunt cantitative; grupul focal "
        "și interviul nestructurat sunt calitative. Observația sistematică cu fișă "
        "de codare poate produce date cantitative, deși pornește dintr-o tehnică "
        "descriptivă."
    ),
    (
        "Instrumentele psihometrice și chestionarele standardizate sunt cantitative "
        "pentru că produc scoruri comparabile și folosesc proceduri sistematice. "
        "Nu sunt identice cu tehnicile proiective nestandardizate, care au adesea "
        "componentă calitativă."
    ),
    (
        "Tehnicile proiective (Rorschach etc.) folosesc stimuli ambigui; interpretarea "
        "depinde de formarea evaluatorului și de contextul clinic. De aceea au "
        "componentă calitativă și subiectivă mai pronunțată decât testele cu "
        "răspuns închis."
    ),
    (
        "Observația cu fișă de codare transformă comportamente în categorii "
        "prestabilite (frecvențe, durate), permițând compararea între persoane "
        "sau sesiuni. Este un exemplu de cuantificare a datelor observaționale."
    ),
    # —— 37–44: Etic versus emic ——
    (
        "Abordarea etică (etic = universal, din exterior) presupune construcții "
        "considerate comparabile între culturi, cum ar fi modelul celor cinci mari "
        "factori. Caută generalizare cross-culturală."
    ),
    (
        "Abordarea emică (emic = din interiorul culturii) dezvoltă construcții și "
        "instrumente specifice contextului cultural, nu doar traduceri mecanice. "
        "Sensul comportamentului este înțeles în logica proprie culturii."
    ),
    (
        "Abordarea etică nu înseamnă exclusiv măsuri indigene pentru fiecare cultură "
        "fără comparabilitate — dimpotrivă, caută constructe universale. Măsurile "
        "strict locale țin de perspectiva emică."
    ),
    (
        "Abordarea emică valorizează înțelegerea comportamentului în cadrul cultural "
        "propriu, nu aplicarea mecanică a unui test tradus. Adaptarea și validarea "
        "locală sunt esențiale."
    ),
    (
        "Etic = comparabilitate cross-culturală, constructe considerate universale. "
        "Emic = măsuri locale, sensuri specifice comunității. Nu confunda: traducerea "
        "literală fără validare locală nu este o abordare emică autentică."
    ),
    (
        "Emic = instrumente adaptate culturii, validare locală. Etic = aplicare "
        "identică a testelor occidentale peste tot, fără adaptare — acesta din urmă "
        "poate genera erori de interpretare, nu emicitate."
    ),
    (
        "Aplicarea unui inventar tradus literal, fără validare în România, riscă "
        "să ignore specificul cultural (emic) și să producă interpretări greșite "
        "ale itemilor. Comparabilitatea perfectă nu apare automat prin traducere."
    ),
    (
        "Modelul celor cinci mari factori este asociat abordării etice pentru că "
        "operează cu trăsături considerate relativ universale și permite comparații "
        "între grupuri culturale. Nu exclude nevoia de adaptare în anumite contexte."
    ),
    # —— 45–50: Surse multiple ——
    (
        "Strategia multimodală combină interviu, observație și teste, verificând "
        "convergența între metode. Modelul multitraită-multimetodă (Campbell & Fiske) "
        "este un cadru teoretic pentru evaluarea validității, nu o singură metodă."
    ),
    (
        "Strategia cu mai mulți evaluatori colectează date de la mai mulți informatori "
        "(părinți, profesori) sau perspective (evaluare 360° în organizații). "
        "Auto-raportarea singură nu acoperă comportamentul din medii diferite."
    ),
    (
        "Modelul multitraită-multimetodă separă trăsătura măsurată de metoda folosită: "
        "aceeași trăsătură prin metode diferite ar trebui să convergă; metode diferite "
        "pentru constructe diferite ar trebui să se discrimineze."
    ),
    (
        "Interviul semi-structurat (calitativ) plus chestionar standardizat (cantitativ) "
        "ilustrează combinarea metodelor și triangularea — verificarea informației din "
        "surse diferite. Nu înseamnă renunțarea la standardizare."
    ),
    (
        "Inventarele de personalitate sunt utile în evaluarea clinică, dar nu "
        "înlocuiesc interviul și observația. Evaluarea multimodală oferă o imagine "
        "mai completă decât orice instrument izolat."
    ),
    (
        "Surse multiple (interviu + teste + observație; mai mulți informatori) reduc "
        "părtinirea unei singure metode sau a unui singur evaluator. O singură probă "
        "sau doar auto-raportarea lasă lacune importante."
    ),
    (
        "Niciun inventar standardizat nu poate înlocui complet contextul clinic, "
        "observația și relația terapeutică. Testele oferă date structurate, dar "
        "interpretarea și decizia rămân integrate în procesul clinic."
    ),
    # —— 51–56: Măsurare și scor brut (psihometric) ——
    (
        "Măsurarea psihometrică atribuie valori numerice unor constructe psihologice "
        "prin eșantionarea comportamentelor relevante (ex. răspunsuri la itemi). "
        "Nu elimină variabilitatea individuală — o cuantifică."
    ),
    (
        "Scorul brut (ex. număr de răspunsuri corecte) capătă sens diagnostic "
        "comparativ doar când este raportat la norme sau transformări standardizate. "
        "Fără populație de referință, 34 de puncte nu spun „cât de mult”."
    ),
    (
        "Scorul brut reflectă performanța directă la itemi, dar singur nu are "
        "semnificație diagnostică — trebuie comparat cu norme. Nu este echivalent "
        "cu un percentile fără transformare."
    ),
    (
        "În modelul clasic X = T + E, scorul observat = scorul real + eroarea de "
        "măsurare. Scorul real nu poate fi cunoscut perfect; orice măsurătoare "
        "include o componentă de eroare."
    ),
    (
        "34 de răspunsuri corecte fără norme = scor brut, fără interpretare "
        "comparativă. Nu indică automat un coeficient de inteligență de 100 și "
        "nu înlocuiește populația de referință."
    ),
    (
        "Scorul brut nu poate fi interpretat direct ca diagnostic clinic fără norme "
        "sau transformări. Standardizarea și normele transformă numărul brut în "
        "informație cu sens psihologic comparabil."
    ),
    # —— 57–62: Standardizare ——
    (
        "Standardizarea unui test presupune uniformitate în probă (aceeași stimulare), "
        "administrare și scorare, plus interpretare comună (același scor = același "
        "sens). Ignorarea instrucțiunilor distruge comparabilitatea."
    ),
    (
        "Dacă doi candidați au același scor brut la un test standardizat, "
        "interpretarea ar trebui să fie echivalentă pentru că standardizarea și "
        "normele conferă același sens aceluiași scor. Scoruri diferite nu au "
        "automat același sens."
    ),
    (
        "Standardizarea probei = aceleași condiții de prezentare, aceleași instrucțiuni, "
        "aceiași itemi în aceeași formă. Itemi diferiți pentru fiecare persoană "
        "fără regulă împiedică compararea."
    ),
    (
        "Standardizarea administrării și scorării reduce variabilitatea datorată "
        "procedurii și permite compararea între persoane. Nu elimină complet "
        "eroarea de măsurare și nu înlocuiește normele."
    ),
    (
        "Standardizarea interpretării se bazează pe norme și transformări convenite, "
        "astfel încât specialiștii comunică același sens al scorului. Populația "
        "de referință rămâne necesară."
    ),
    (
        "Un test poate fi standardizat la administrare, dar cu norme învechite — "
        "atunci interpretarea comparativă față de populația actuală rămâne incertă. "
        "Normele trebuie actualizate periodic."
    ),
    # —— 63–70: Normativă versus ipsativă ——
    (
        "Măsurarea normativă compară persoana cu o normă de grup (populație de "
        "referință) — comparație interindividuală. Scorul răspunde la „cât de mult "
        "față de alții”."
    ),
    (
        "Măsurarea ipsativă compară trăsăturile în cadrul propriului profil "
        "(forced-choice, ierarhie de preferințe) — comparație intraindividuală. "
        "Nu oferă direct poziția față de populație."
    ),
    (
        "Instrumente ipsative (Jackson, Myers-Briggs în interpretare tipologică): "
        "subiectul alege între opțiuni; profilul reflectă ordinea preferințelor, "
        "nu un nivel absolut față de normă."
    ),
    (
        "Testele psihometrice clasice folosesc măsurare normativă: scorul se "
        "interpretează față de populația de referință, cu comparație "
        "interindividuală. Formatul forced-choice ipsativ este altceva."
    ),
    (
        "La măsurarea ipsativă, un scor mare pe o scală înseamnă că acea trăsătură "
        "este mai preferată decât altele în profilul personal, nu neapărat că "
        "persoana este „înaltă” față de populație (nu e același lucru cu scor z)."
    ),
    (
        "Normele sunt definite de distribuția scorurilor într-un eșantion "
        "reprezentativ (media, deviația standard) și permit transformarea scorului "
        "brut în scor standardizat. Nu elimină eroarea de măsurare."
    ),
    (
        "Normele pentru aptitudini sunt adesea diferențiate pe vârstă; pentru "
        "personalitate pot fi diferențiate pe gen — pentru că performanța sau "
        "răspunsurile variază sistematic cu aceste variabile."
    ),
    (
        "Măsurarea normativă și ipsativă răspund la întrebări diferite: prima "
        "despre poziția față de populație, a doua despre structura preferințelor "
        "interne. Nu oferă aceleași informații."
    ),
    # —— 71–80: Scale și scoruri ——
    (
        "Scala nominală clasifică în categorii distincte (ex. gen, diagnostic); "
        "permite frecvențe și modul, nu medie aritmetică cu sens psihologic direct "
        "sau ordonare ierarhică garantată."
    ),
    (
        "Scala ordinală permite ordonarea (ex. Likert), mediană și percentile, "
        "dar distanțele între trepte nu sunt neapărat egale. Varianța strictă "
        "interpretată ca distanță egală este problematică."
    ),
    (
        "Scala de interval permite medie, varianță și corelație Pearson (ex. scoruri "
        "standardizate). Nu are origine absolută la zero în sens fizic, dar "
        "suportă multe analize statistice."
    ),
    (
        "Scala de raport are origine absolută (zero real) — ex. scor z, scor T, "
        "coeficient de inteligență. Permite raporturi proporționale („de două ori "
        "mai mult”)."
    ),
    (
        "Transformarea liniară scor T = 50 + 10 × scor z este corectă: media T "
        "este 50, deviația standard 10, păstrând forma distribuției originale."
    ),
    (
        "Coeficientul de inteligență Wechsler (media 100, DS 15) este o transformare "
        "liniară a scorului z, care facilitează interpretarea comparativă. Nu are "
        "media 50 ca scorul T; normele de populație sunt necesare."
    ),
    (
        "Scorurile standardizate liniare (z, T, IQ Wechsler) păstrează forma "
        "distribuției originale. Percentilele sunt neliniare și schimbă forma "
        "distribuției."
    ),
    (
        "Scorurile neliniare includ percentilele și staninele (9 intervale). "
        "Comprimă sau extind diferențele în zonele distribuției față de "
        "transformările liniare."
    ),
    (
        "Percentilele transformă distribuția într-una uniformă (neliniar). "
        "Diferențele din zonele extreme pot fi comprimate — de aceea nu sunt "
        "echivalente cu scorul z ca tip de transformare."
    ),
    (
        "Pe scala nominală nu se calculează corect media aritmetică ca pe scala "
        "de interval — categoriile nu au distanțe numerice egale. Aceasta este "
        "o regulă fundamentală a nivelurilor de măsurare (Stevens)."
    ),
    # —— 81–86: Clasificarea instrumentelor ——
    (
        "Instrumentele se clasifică după construct (aptitudine, personalitate, "
        "interese), dimensionalitate (uni- vs multidimensional), mod de administrare "
        "(hârtie, computer) și format de răspuns."
    ),
    (
        "Alte criterii: administrare individuală vs colectivă, auto- vs hetero-evaluare, "
        "tip sarcină (test vs chestionar). Validitatea și fidelitatea se evaluează "
        "pentru orice instrument, nu doar dificultatea itemilor."
    ),
    (
        "Formate de răspuns: deschis/închis, Likert, forced-choice, ranking. "
        "Nu există un singur format binar obligatoriu — diversitatea reflectă "
        "scopul măsurătorii."
    ),
    (
        "Un inventar cu mai multe scale pentru trăsături diferite (ex. NEO) este "
        "multidimensional — măsoară mai multe constructe distincte, nu o singură "
        "dimensiune."
    ),
    (
        "Testele de inteligență administrate individual pot combina hetero-evaluare "
        "(examinatorul notează) cu răspunsuri deschise la unele subteste, respectând "
        "totuși baremul standardizat."
    ),
    (
        "Scala Likert cuantifică intensitatea acordului (ordinal/cantitativ în "
        "practică) și se încadrează la chestionare, nu la teste de aptitudini cu "
        "răspunsuri corecte/greșite. Poate fi administrată și pe computer."
    ),
    # —— 87–94: Fidelitate și validitate ——
    (
        "Orice instrument psihometric trebuie evaluat pentru validitate (măsoară "
        "ce pretinde?) și fidelitate (măsoară consistent?). Discriminarea și "
        "dificultatea itemilor sunt relevante mai ales la testele de aptitudini."
    ),
    (
        "Discriminarea itemului (cât de bine separă pe cei performanți de cei slabi) "
        "și dificultatea se analizează în principal la testele de aptitudini sau "
        "inteligență, nu la toate tipurile de instrumente la fel."
    ),
    (
        "Fidelitatea include test–retest, forme alternative, split-half, alfa Cronbach, "
        "Kuder-Richardson 20 (itemi binari). Validitatea de fațadă nu este un tip "
        "de fidelitate — este un risc de distorsiune a răspunsului."
    ),
    (
        "Validitatea include conținut, criteriu (predictivă/concurentă) și construct "
        "(convergentă, discriminativă, factorială). Split-half este indice de "
        "fidelitate, nu de validitate."
    ),
    (
        "Validitatea de criteriu predictivă anticipează un rezultat viitor; "
        "concurentă compară testul cu un criteriu actual. Validitatea factorială "
        "ține de structura constructului, nu de criteriu extern."
    ),
    (
        "Validitatea de construct convergentă se verifică prin corelații cu alte "
        "măsuri ale aceluiași construct — susține că instrumentul măsoară ce "
        "pretinde. Nu exclude corelațiile cu teste similare."
    ),
    (
        "Fidelitatea (consistența măsurătorii) și validitatea (adecvarea măsurătorii) "
        "sunt concepte distincte. Un test poate fi fidel dar invalid pentru scopul "
        "ales — măsoară constant ceva greșit."
    ),
    (
        "Eroarea standard a măsurătorii permite construirea unui interval de "
        "încredere în jurul scorului (aprox. ±2 SEM pentru 95%, ±3 pentru 99%). "
        "Nu înlocuiește evaluarea fidelității testului."
    ),
    # —— 95–100: Computerizare și perspective ——
    (
        "Evaluarea computerizată crește eficiența administrării, scorării și "
        "raportării; permite testare adaptivă. Nu elimină eroarea de măsurare "
        "și nu înlocuiește validarea instrumentului."
    ),
    (
        "Testarea adaptivă computerizată selectează itemul următor în funcție de "
        "răspunsul anterior, estimând nivelul cu mai puțini itemi. Nu folosește "
        "aceeași listă fixă pentru toți."
    ),
    (
        "Testarea adaptivă poate fi mai precisă și mai scurtă, dar necesită o "
        "bancă calibrată de itemi și algoritmi de selecție — de aceea costurile "
        "de dezvoltare sunt mai mari."
    ),
    (
        "Perspectiva psihometrică nomotetică caută legi generale, norme de grup și "
        "comparații între persoane. Este specifică evaluării standardizate și "
        "cercetării pe eșantioane."
    ),
    (
        "Perspectiva clinică idiografică urmărește înțelegerea unică a individului; "
        "testele sunt instrumente integrate în contextul cazului, nu scop în sine. "
        "Nu exclude testele standardizate, dar le contextualizează."
    ),
    (
        "În practica clinică, testul standardizat nu înlocuiește înțelegerea "
        "idiografică a cazului — completează-o. Decizia clinică rămâne integrată, "
        "nu redusă la un singur scor."
    ),
]


from scripts.inteligenta_istoric_modele_explanations import INTELIGENTA_EXPLANATIONS

EXPLANATIONS.extend(INTELIGENTA_EXPLANATIONS)

from scripts.inteligenta_emotionala_explanations import INTELIGENTA_EMOTIONALA_EXPLANATIONS

EXPLANATIONS.extend(INTELIGENTA_EMOTIONALA_EXPLANATIONS)

from scripts.motivatie_explanations import MOTIVATIE_EXPLANATIONS

EXPLANATIONS.extend(MOTIVATIE_EXPLANATIONS)

from scripts.interese_explanations import INTERESE_EXPLANATIONS

EXPLANATIONS.extend(INTERESE_EXPLANATIONS)

from scripts.jvis_explanations import JVIS_EXPLANATIONS

EXPLANATIONS.extend(JVIS_EXPLANATIONS)

EVALUARE_EXAM_ID_MAX = 9360


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (9001–9360), independent de questions.json."""
    if 9001 <= int(item_id) <= EVALUARE_EXAM_ID_MAX:
        idx = int(item_id) - 9001
        if 0 <= idx < len(EXPLANATIONS):
            return EXPLANATIONS[idx]
    return ""


def attach_explanations(items: list) -> list:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(EXPLANATIONS):
            item["explanation"] = EXPLANATIONS[i]
        out.append(item)
    return out
