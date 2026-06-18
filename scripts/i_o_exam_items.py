"""Itemi examen — Psihologia organizațională/muncii (serie 1–150)."""

from __future__ import annotations

from typing import Dict, List, Tuple
from scripts.exam_item_utils import build_exam_item

LOT_NAME = "Psihologia organizațională/muncii"
START_ID = 5001

# (stem, (a,b,c,d), correct_letters)
_RAW: List[Tuple[str, Tuple[str, str, str, str], str]] = [
    (
        "Analiza muncii orientată spre angajat urmărește:",
        (
            "responsabilitățile postului",
            "KSAO necesare postului",
            "activitățile efectuate zilnic",
            "caracteristicile persoanei",
        ),
        "bd",
    ),
    (
        "În analiza muncii, KSAO desemnează:",
        (
            "volumul de muncă, presiunea de timp, cerințele emoționale și autonomia",
            "cunoștințe, deprinderi, aptitudini și alte caracteristici personale relevante pentru post",
            "salariul, programul, beneficiile și contractul de muncă",
            "cultura organizațională, climatul, satisfacția și angajamentul",
        ),
        "b",
    ),
    (
        "În ierarhia analizei muncii, care unitate este cea mai cuprinzătoare?",
        ("Occupation", "Job Family", "Career", "Position"),
        "c",
    ),
    (
        "Tehnica incidentelor critice presupune colectarea:",
        (
            "comportamentelor foarte eficiente",
            "comportamentelor foarte ineficiente",
            "tuturor activităților zilnice",
            "evenimentelor semnificative",
        ),
        "abd",
    ),
    (
        "Job Specification conține:",
        (
            "responsabilități",
            "experiență necesară",
            "educație necesară",
            "condiții de muncă",
        ),
        "bc",
    ),
    (
        "În modelul Hackman și Oldham, starea psihologică „responsibility” este generată în principal de:",
        ("Feedback", "Task Identity", "Autonomy", "Skill Variety"),
        "c",
    ),
    (
        "Care caracteristici contribuie direct la Meaningfulness?",
        ("Task Identity", "Skill Variety", "Feedback", "Task Significance"),
        "abd",
    ),
    (
        "În JD-R, burnout este asociat în principal cu:",
        (
            "Job Resources reduse",
            "Job Demands ridicate",
            "Feedback crescut",
            "Autonomie ridicată",
        ),
        "b",
    ),
    (
        "Job Resources includ:",
        ("suport social", "autonomie", "conflict de rol", "feedback"),
        "abd",
    ),
    (
        "GMA reprezintă:",
        (
            "capacitatea generală de învățare",
            "inteligența generală",
            "nivelul educației",
            "capacitatea de rezolvare a problemelor",
        ),
        "abd",
    ),
    (
        "Validitatea incrementală apare atunci când:",
        (
            "predictorul nou explică variație suplimentară",
            "predictorul nou este identic cu cel vechi",
            "crește puterea predictivă a modelului",
            "predictorul este mai ieftin",
        ),
        "ac",
    ),
    (
        "Sensibilitatea unui test se referă la:",
        (
            "identificarea persoanelor potrivite",
            "eliminarea persoanelor nepotrivite",
            "reducerea false negative",
            "reducerea false positive",
        ),
        "ac",
    ),
    (
        "Specificitatea ridicată implică:",
        (
            "puține false positive",
            "identificarea candidaților buni",
            "respingerea corectă a candidaților nepotriviți",
            "puține false negative",
        ),
        "ac",
    ),
    (
        "Screening-ul este caracterizat prin:",
        (
            "cost redus",
            "complexitate mare",
            "viteză mare",
            "evaluare aprofundată",
        ),
        "ac",
    ),
    (
        "Taylor-Russell utilizează:",
        ("Base Rate", "Selection Ratio", "Validitate", "Conștiinciozitate"),
        "abc",
    ),
    (
        "Criterion Deficiency apare atunci când:",
        (
            "lipsesc aspecte relevante ale performanței",
            "există influențe nerelevante",
            "criteriul nu surprinde întregul construct",
            "evaluarea este prea severă",
        ),
        "ac",
    ),
    (
        "Criterion Contamination presupune:",
        (
            "influențe nerelevante",
            "favoritism",
            "lipsa unor componente importante",
            "efecte de reputație",
        ),
        "abd",
    ),
    (
        "Task Performance:",
        (
            "diferă între ocupații",
            "este specifică postului",
            "include comportamente voluntare extra-rol",
            "apare în fișa postului",
        ),
        "abd",
    ),
    (
        "Contextual Performance:",
        (
            "susține funcționarea organizației",
            "include OCB",
            "este identică cu Task Performance",
            "depășește cerințele minime",
        ),
        "abd",
    ),
    (
        "OCB include:",
        ("Altruism", "Courtesy", "Civic Virtue", "Sabotaj"),
        "abc",
    ),
    (
        "Sportsmanship se referă la:",
        (
            "tolerarea dificultăților fără plângeri excesive",
            "evitarea conflictelor",
            "participarea la viața organizației",
            "ajutorarea colegilor",
        ),
        "a",
    ),
    (
        "CWB orientat spre organizație poate include:",
        ("absenteism", "furt", "sabotaj", "bullying"),
        "abc",
    ),
    (
        "Predictorii OCB includ:",
        (
            "satisfacția muncii",
            "justiția organizațională",
            "agreabilitatea",
            "neuroticismul ridicat",
        ),
        "abc",
    ),
    (
        "Hobo Syndrome sugerează că:",
        (
            "turnoverul trecut prezice turnoverul viitor",
            "satisfacția ridicată crește plecările",
            "istoricul profesional are valoare predictivă",
            "performanța ridicată determină plecarea",
        ),
        "ac",
    ),
    (
        "Cel mai bun predictor al turnoverului este:",
        ("salariul", "intenția de plecare", "satisfacția muncii", "vechimea"),
        "b",
    ),
    (
        "Relația dintre satisfacția muncii și performanță este descrisă cel mai corect prin:",
        (
            "satisfacția determină întotdeauna performanță ridicată",
            "relația este pozitivă, dar modestă",
            "performanța și satisfacția sunt complet independente",
            "relația este exclusiv negativă",
        ),
        "b",
    ),
    (
        "Care dimensiune a satisfacției muncii este asociată cel mai puternic cu intenția de plecare?",
        ("Comunicare", "Beneficii", "Promotion", "Colegi"),
        "c",
    ),
    (
        "Spill-over apare atunci când:",
        (
            "experiențele de la muncă influențează viața personală",
            "stresul unei persoane este transmis altei persoane",
            "satisfacția profesională influențează satisfacția vieții",
            "două persoane împărtășesc aceeași stare emoțională",
        ),
        "ac",
    ),
    (
        "Cross-over presupune:",
        (
            "transferul emoțiilor între persoane",
            "influențe între rolurile aceleiași persoane",
            "transmiterea stresului de la un partener la altul",
            "transferul satisfacției între membrii familiei",
        ),
        "acd",
    ),
    (
        "Care afirmații despre Value Fit sunt corecte?",
        (
            "reprezintă compatibilitatea valorilor persoană-organizație",
            "este identic cu satisfacția muncii",
            "este asociat cu turnover mai redus",
            "este asociat cu angajament organizațional crescut",
        ),
        "acd",
    ),
    (
        "În modelul lui Schwartz, autodirecționarea este asociată cu:",
        ("autonomie", "independență în gândire", "conformitate", "libertatea alegerii"),
        "abd",
    ),
    (
        "Valorile orientate spre conservare includ:",
        ("Tradiție", "Conformitate", "Securitate", "Stimulare"),
        "abc",
    ),
    (
        "Socializarea organizațională urmărește:",
        (
            "integrarea noului angajat",
            "învățarea normelor organizației",
            "dezvoltarea Value Fit",
            "eliminarea diferențelor individuale",
        ),
        "abc",
    ),
    (
        "Aculturația organizațională presupune:",
        (
            "adaptarea la cultura organizației",
            "abandonarea completă a valorilor personale",
            "integrarea într-un nou context cultural",
            "ajustarea comportamentelor și valorilor",
        ),
        "acd",
    ),
    (
        "Potrivit lui Selye, ultima fază a Sindromului General de Adaptare este:",
        ("alarmă", "rezistență", "epuizare", "recuperare"),
        "c",
    ),
    (
        "Conform lui Selye, stresul este:",
        (
            "răspunsul organismului la solicitări",
            "exclusiv o reacție emoțională",
            "nespecific față de natura stimulului",
            "întotdeauna negativ",
        ),
        "ac",
    ),
    (
        "Modelul Person-Environment Fit susține că stresul apare când:",
        (
            "există nepotrivire între persoană și mediu",
            "există cerințe ridicate și control redus",
            "resursele sunt incompatibile cu cerințele",
            "există potrivire perfectă",
        ),
        "ac",
    ),
    (
        "În modelul Demand-Control, nivelul maxim de stres apare când:",
        (
            "cerințele sunt mari și controlul este redus",
            "cerințele sunt mici și controlul este redus",
            "cerințele sunt mari și controlul este mare",
            "cerințele sunt reduse și controlul este mare",
        ),
        "a",
    ),
    (
        "În modelul lui Lazarus, evaluarea primară răspunde la întrebarea:",
        (
            "Pot controla situația?",
            "Este situația relevantă sau amenințătoare?",
            "Ce strategie de coping folosesc?",
            "Care este cauza evenimentului?",
        ),
        "b",
    ),
    (
        "Evaluarea secundară presupune:",
        (
            "aprecierea resurselor disponibile",
            "estimarea posibilității de a face față situației",
            "evaluarea gradului de amenințare",
            "alegerea strategiilor de coping",
        ),
        "abd",
    ),
    (
        "Copingul centrat pe problemă include:",
        (
            "planificare",
            "căutarea informațiilor",
            "evitarea emoțiilor negative",
            "rezolvarea directă a situației",
        ),
        "abd",
    ),
    (
        "Copingul centrat pe emoție include:",
        (
            "suport emoțional",
            "reinterpretare pozitivă",
            "restructurarea sarcinilor de muncă",
            "relaxare",
        ),
        "abd",
    ),
    (
        "Type A Behavior Pattern este caracterizat prin:",
        ("competitivitate", "nerăbdare", "ostilitate", "relaxare"),
        "abc",
    ),
    (
        "Challenge Stressors sunt:",
        (
            "percepuți ca oportunități de dezvoltare",
            "asociați exclusiv cu stres negativ",
            "frecvent asociați cu motivația",
            "percepuți ca provocări",
        ),
        "acd",
    ),
    (
        "Hindrance Stressors sunt:",
        (
            "obstacole percepute în atingerea obiectivelor",
            "asociați cu frustrare",
            "asociați cu dezvoltare profesională",
            "legați de birocrație excesivă",
        ),
        "abd",
    ),
    (
        "Feedback-ul 360° include informații provenite de la:",
        ("superiori", "colegi", "subordonați", "clienți"),
        "abcd",
    ),
    (
        "Care afirmații despre BARS sunt corecte?",
        (
            "utilizează exemple comportamentale concrete",
            "reduce ambiguitatea evaluării",
            "măsoară frecvența comportamentelor",
            "este o metodă de evaluare a performanței",
        ),
        "abd",
    ),
    (
        "BOS diferă de BARS deoarece:",
        (
            "se concentrează pe frecvența comportamentelor",
            "utilizează observația comportamentelor",
            "măsoară calitatea comportamentelor mai mult decât frecvența",
            "este derivată din comportamente observabile",
        ),
        "abd",
    ),
    (
        "Forced Distribution presupune:",
        (
            "distribuirea forțată a angajaților pe categorii",
            "imposibilitatea acordării acelorași calificative tuturor",
            "eliminarea completă a erorilor evaluatorului",
            "reducerea tendinței de indulgență",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele reprezintă erori de evaluare?",
        (
            "Halo Effect",
            "Recency Effect",
            "Criterion Deficiency",
            "Similar-to-Me Effect",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele situații ilustrează cel mai bine Criterion Contamination?",
        (
            "Un profesor este evaluat doar după publicații, deși predă și coordonează studenți.",
            "Evaluarea unui angajat este influențată de relația apropiată cu managerul.",
            "Sunt măsurate doar o parte dintre responsabilitățile postului.",
            "Un criteriu include exclusiv indicatori obiectivi.",
        ),
        "b",
    ),
    (
        "Criterion Deficiency apare atunci când:",
        (
            "evaluatorul acordă note prea mari tuturor angajaților.",
            "criteriul include informații nerelevante.",
            "anumite aspecte importante ale performanței nu sunt evaluate.",
            "există diferențe între evaluatori.",
        ),
        "c",
    ),
    (
        "Care afirmații despre Contextual Performance sunt corecte?",
        (
            "este identică cu OCB.",
            "facilitează funcționarea organizației.",
            "include comportamente care depășesc cerințele formale.",
            "este specifică fiecărui post.",
        ),
        "bc",
    ),
    (
        "O persoană își transferă stresul profesional asupra satisfacției sale familiale. Acesta este un exemplu de:",
        ("Cross-over", "Value Fit", "Spill-over", "Burnout"),
        "c",
    ),
    (
        "Un soț transmite tensiunea acumulată la serviciu partenerului său. Acesta este un exemplu de:",
        ("Spill-over", "Coping centrat pe emoție", "Demand-Control", "Cross-over"),
        "d",
    ),
    (
        "Care dintre următoarele sunt caracteristici ale angajamentului afectiv?",
        (
            "Angajatul rămâne pentru că nu găsește alternative.",
            "Angajatul se identifică emoțional cu organizația.",
            "Angajatul rămâne deoarece dorește acest lucru.",
            "Angajatul rămâne exclusiv din motive financiare.",
        ),
        "bc",
    ),
    (
        "În modelul Demand-Control, combinația asociată dezvoltării și învățării este:",
        (
            "cerințe reduse + control redus",
            "cerințe ridicate + control ridicat",
            "cerințe reduse + control ridicat",
            "cerințe ridicate + control redus",
        ),
        "b",
    ),
    (
        "Care dintre următoarele sunt Job Resources?",
        ("Ambiguitatea rolului", "Feedback-ul", "Suportul social", "Conflictul de rol"),
        "bc",
    ),
    (
        "În modelul JD-R, burnout-ul este asociat în principal cu:",
        (
            "creșterea engagementului",
            "acumularea de resurse personale",
            "nivel ridicat al cerințelor ocupaționale",
            "satisfacție profesională crescută",
        ),
        "c",
    ),
    (
        "Care dintre următoarele valori aparțin dimensiunii „orientare spre conservare” la Schwartz?",
        ("Putere", "Tradiție", "Securitate", "Conformitate"),
        "bcd",
    ),
    (
        "Care afirmații despre Feedback 360° sunt corecte?",
        (
            "Include evaluarea realizată exclusiv de superior.",
            "Poate reduce influența unei singure perspective.",
            "Utilizează surse multiple de informații.",
            "Elimină complet erorile de evaluare.",
        ),
        "bc",
    ),
    (
        "În comparație cu BARS, BOS:",
        (
            "utilizează exemple comportamentale ancorate.",
            "evaluează frecvența comportamentelor observate.",
            "pune accent pe cât de des apare comportamentul.",
            "este identic metodologic cu BARS.",
        ),
        "bc",
    ),
    (
        "Care dintre următoarele reprezintă exemple de OCB?",
        ("Civic Virtue", "Sportsmanship", "Absenteism voluntar", "Courtesy"),
        "abd",
    ),
    (
        "Un evaluator acordă tuturor angajaților scoruri apropiate de mijlocul scalei. Aceasta este eroarea:",
        ("Recency", "Leniency", "Central Tendency", "Severity"),
        "c",
    ),
    (
        "Un manager acordă scoruri mari tuturor angajaților indiferent de performanță. Este un exemplu de:",
        ("Leniency", "Similar-to-Me", "Severity", "Primacy"),
        "a",
    ),
    (
        "Care dintre următoarele sunt asociate cu Type A Behavior Pattern?",
        ("Competitivitate ridicată", "Ostilitate", "Relaxare accentuată", "Nerăbdare"),
        "abd",
    ),
    (
        "Care dintre următoarele sunt exemple de Challenge Stressors?",
        (
            "Responsabilitate crescută",
            "Ambiguitate de rol",
            "Proiecte dificile",
            "Oportunități de dezvoltare",
        ),
        "acd",
    ),
    (
        "Care afirmații despre Hobo Syndrome sunt corecte?",
        (
            "Istoricul de schimbare a locurilor de muncă poate prezice fluctuația viitoare.",
            "Este o teorie a burnout-ului.",
            "Turnoverul anterior poate avea valoare predictivă.",
            "Este asociat exclusiv cu satisfacția muncii.",
        ),
        "ac",
    ),
    (
        "În selecție, un False Positive reprezintă:",
        (
            "un candidat respins care ar fi performat bine.",
            "un candidat acceptat care performează slab.",
            "o eroare de evaluare a performanței.",
            "un candidat acceptat care performează bine.",
        ),
        "b",
    ),
    (
        "Care dintre următoarele cresc probabilitatea manifestării CWB?",
        (
            "Percepția de injustiție organizațională",
            "Frustrarea",
            "Conștiinciozitatea ridicată",
            "Neuroticismul ridicat",
        ),
        "abd",
    ),
    (
        "În cadrul KSAO, care elemente sunt relativ stabile și mai greu de modificat prin training?",
        ("Knowledge", "Skills", "Abilities", "Unele Other Characteristics"),
        "cd",
    ),
    (
        "Care dintre următoarele caracteristici contribuie direct la Meaningfulness în modelul Hackman & Oldham?",
        ("Task Significance", "Autonomy", "Skill Variety", "Task Identity"),
        "acd",
    ),
    (
        "Care afirmații despre Performance Management sunt corecte?",
        (
            "Include feedback și dezvoltare.",
            "Este mai larg decât Performance Appraisal.",
            "Se reduce la completarea unei fișe de evaluare.",
            "Include stabilirea obiectivelor.",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt exemple de coping centrat pe problemă?",
        (
            "Căutarea informațiilor relevante",
            "Planificarea acțiunilor",
            "Relaxarea musculară",
            "Rezolvarea directă a problemei",
        ),
        "abd",
    ),
    (
        "Care afirmații despre satisfacția muncii sunt susținute de cercetările prezentate?",
        (
            "Este complet independentă de performanță.",
            "Relația cu performanța este pozitivă, dar modestă.",
            "Dimensiunea Work Itself este asociată cu efecte importante de spill-over.",
            "Promotion este asociată cu intenția de plecare.",
        ),
        "bcd",
    ),
    (
        "Care dintre următoarele afirmații despre Job Specification sunt corecte?",
        (
            "descrie cerințele candidatului",
            "include educația necesară",
            "descrie condițiile fizice ale locului de muncă",
            "poate include experiența necesară",
        ),
        "abd",
    ),
    (
        "În analiza muncii, orientarea spre sarcină pune accent pe:",
        (
            "trăsături de personalitate",
            "KSAO",
            "activitățile și responsabilitățile postului",
            "valori organizaționale",
        ),
        "c",
    ),
    (
        "Care dintre următoarele pot fi considerate Job Demands?",
        (
            "conflictul de rol",
            "ambiguitatea rolului",
            "suportul social",
            "suprasolicitarea cantitativă",
        ),
        "abd",
    ),
    (
        "În modelul lui Lazarus, coping-ul apare după:",
        (
            "evaluarea secundară",
            "evaluarea primară",
            "evaluarea cognitivă a situației",
            "identificarea amenințării",
        ),
        "abcd",
    ),
    (
        "Care afirmații despre Selection Ratio sunt corecte?",
        (
            "poate lua valori mai mari de 1",
            "reprezintă raportul dintre candidații selectați și cei disponibili",
            "valori mici indică selecție mai strictă",
            "influențează utilitatea selecției",
        ),
        "bcd",
    ),
    (
        "Un evaluator este impresionat de abilitățile de comunicare ale unui angajat și îi acordă scoruri mari la toate criteriile. Este vorba despre:",
        ("Recency Effect", "Central Tendency", "Halo Effect", "Leniency Error"),
        "c",
    ),
    (
        "Care dintre următoarele sunt caracteristici ale Value Fit ridicat?",
        (
            "angajament organizațional mai mare",
            "fluctuație redusă",
            "satisfacție profesională mai mare",
            "eliminarea conflictelor organizaționale",
        ),
        "abc",
    ),
    (
        "Care dintre următoarele NU sunt dimensiuni clasice OCB?",
        ("Courtesy", "Civic Virtue", "Burnout", "Sportsmanship"),
        "c",
    ),
    (
        "În cadrul GAS al lui Selye, etapa de rezistență presupune:",
        (
            "adaptarea la solicitare",
            "mobilizarea resurselor organismului",
            "dispariția completă a stresului",
            "menținerea efortului de adaptare",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt asociate mai degrabă cu CWB?",
        ("sabotaj", "furt", "altruism", "agresivitate interpersonală"),
        "abd",
    ),
    (
        "În modelul Hackman și Oldham, Feedback contribuie direct la:",
        ("Meaningfulness", "Knowledge of Results", "Responsibility", "Contextual Performance"),
        "b",
    ),
    (
        "O persoană foarte conștiincioasă este mai probabil să:",
        (
            "manifeste OCB",
            "manifeste CWB frecvent",
            "aibă performanță mai bună",
            "prezinte fluctuație redusă",
        ),
        "acd",
    ),
    (
        "Care dintre următoarele sunt exemple de criterii de performanță?",
        (
            "vânzări realizate",
            "evaluarea superiorului",
            "satisfacția clienților",
            "GMA",
        ),
        "abc",
    ),
    (
        "Criterion Relevance reprezintă:",
        (
            "porțiunea comună dintre criteriul teoretic și cel efectiv",
            "partea lipsă din criteriu",
            "influențele nerelevante asupra evaluării",
            "gradul în care măsurăm ceea ce ne interesează",
        ),
        "ad",
    ),
    (
        "În Feedback-ul 360°, care sursă este folosită cel mai frecvent și tradițional?",
        ("clienții", "colegii", "superiorul direct", "autoevaluarea"),
        "c",
    ),
    (
        "Care dintre următoarele pot reprezenta Hindrance Stressors?",
        (
            "birocrația excesivă",
            "ambiguitatea rolului",
            "oportunitățile de promovare",
            "conflictele organizaționale",
        ),
        "abd",
    ),
    (
        "Un candidat respins care ar fi avut performanță ridicată reprezintă:",
        ("False Positive", "True Positive", "False Negative", "Criterion Deficiency"),
        "c",
    ),
    (
        "Care afirmații despre MBO sunt corecte?",
        (
            "se bazează pe obiective stabilite anterior",
            "evaluarea se raportează la atingerea obiectivelor",
            "este identic cu BARS",
            "presupune monitorizarea progresului",
        ),
        "abd",
    ),
    (
        "În analiza muncii, KSAO se referă la caracteristicile persoanei necesare pentru performanță în post. Care dintre următoarele sunt componente KSAO?",
        (
            "cunoștințe relevante pentru post",
            "deprinderi sau abilități formate prin exercițiu",
            "aptitudini generale necesare realizării sarcinilor",
            "alte caracteristici personale relevante, precum motivația sau interesele",
        ),
        "abcd",
    ),
    (
        "În cazul spill-over-ului negativ:",
        (
            "stresul profesional poate afecta viața personală",
            "satisfacția profesională crește satisfacția vieții",
            "efectele rămân în aceeași persoană",
            "emoțiile sunt transmise unei alte persoane",
        ),
        "ac",
    ),
    (
        "Care dintre următoarele sunt asociate cu evaluarea performanței și nu cu selecția?",
        ("BARS", "Feedback 360°", "Taylor-Russell", "Forced Distribution"),
        "abd",
    ),
    (
        "În modelul Person–Environment Fit, stresul apare atunci când:",
        (
            "există compatibilitate ridicată",
            "există nepotrivire între persoană și mediu",
            "resursele și cerințele sunt dezechilibrate",
            "valorile sunt identice",
        ),
        "bc",
    ),
    (
        "Care dintre următoarele sunt beneficii ale socializării organizaționale?",
        (
            "integrarea angajaților noi",
            "creșterea Value Fit",
            "reducerea adaptării la organizație",
            "clarificarea normelor și rolurilor",
        ),
        "abd",
    ),
    (
        "Un evaluator acordă note mici aproape tuturor angajaților. Este un exemplu de:",
        ("Halo Effect", "Severity Error", "Similar-to-Me Effect", "Recency Effect"),
        "b",
    ),
    (
        "Care dintre următoarele concepte sunt asociate direct cu reducerea turnoverului?",
        (
            "satisfacția muncii ridicată",
            "Value Fit ridicat",
            "angajamentul afectiv ridicat",
            "intenția de plecare ridicată",
        ),
        "abc",
    ),
    (
        "Care dintre următoarele sunt rezultate posibile ale unui Value Fit ridicat?",
        (
            "Angajament organizațional crescut",
            "Fluctuație redusă",
            "Burnout inevitabil",
            "Satisfacție profesională crescută",
        ),
        "abd",
    ),
    (
        "În modelul JD-R, engagementul este asociat mai ales cu:",
        ("Job Resources", "Job Demands", "Conflictul de rol", "Autonomia"),
        "ad",
    ),
    (
        "Care dintre următoarele reprezintă exemple de Job Resources?",
        ("Feedback", "Suport social", "Ambiguitate de rol", "Autonomie"),
        "abd",
    ),
    (
        "O persoană evaluată exclusiv după numărul de articole publicate, deși postul include și predare, este un exemplu de:",
        (
            "Criterion Contamination",
            "Criterion Deficiency",
            "Halo Effect",
            "Leniency Error",
        ),
        "b",
    ),
    (
        "Care dintre următoarele afirmații despre OCB sunt corecte?",
        (
            "Este obligatoriu prin fișa postului",
            "Include comportamente voluntare",
            "Contribuie la eficiența organizațională",
            "Reprezintă o formă de Contextual Performance",
        ),
        "bcd",
    ),
    (
        "Care dintre următoarele sunt asociate cu Type B?",
        ("Relaxare", "Competitivitate excesivă", "Calm", "Ostilitate"),
        "ac",
    ),
    (
        "Conform lui Lazarus, stresul depinde de:",
        (
            "Evaluarea cognitivă",
            "Caracteristicile obiective ale situației exclusiv",
            "Percepția resurselor disponibile",
            "Interpretarea evenimentului",
        ),
        "acd",
    ),
    (
        "Care dintre următoarele sunt exemple de coping centrat pe emoție?",
        (
            "Relaxare",
            "Reinterpretare pozitivă",
            "Planificare strategică",
            "Suport emoțional",
        ),
        "abd",
    ),
    (
        "În Feedback 360°, care surse pot participa?",
        ("Clienți", "Colegi", "Subordonați", "Superiori"),
        "abcd",
    ),
    (
        "Care dintre următoarele sunt avantaje ale BARS?",
        (
            "Exemple comportamentale concrete",
            "Reduce ambiguitatea evaluării",
            "Elimină complet subiectivitatea",
            "Crește consistența evaluării",
        ),
        "abd",
    ),
    (
        "Un Selection Ratio foarte mic sugerează:",
        (
            "Puțini candidați disponibili",
            "Selecție mai strictă",
            "Concurență ridicată între candidați",
            "Utilitate potențial mai mare",
        ),
        "bcd",
    ),
    (
        "Care dintre următoarele sunt componente ale Performance Management?",
        ("Feedback", "Dezvoltare", "Stabilirea obiectivelor", "Monitorizare"),
        "abcd",
    ),
    (
        "Care dintre următoarele sunt asociate cu Burnout?",
        (
            "Epuizare",
            "Cinism",
            "Ineficacitate percepută",
            "Engagement ridicat",
        ),
        "abc",
    ),
    (
        "În modelul Demand-Control, combinația cea mai problematică este:",
        (
            "Cerințe mari + control redus",
            "Cerințe mari + control mare",
            "Cerințe reduse + control mare",
            "Cerințe reduse + control redus",
        ),
        "a",
    ),
    (
        "Care dintre următoarele sunt exemple de CWB?",
        ("Sabotaj", "Furt", "Absenteism voluntar", "Civic Virtue"),
        "abc",
    ),
    (
        "În cadrul KSAO, care elemente sunt cel mai ușor de dezvoltat prin training?",
        ("Knowledge", "Skills", "Abilities", "Temperament"),
        "ab",
    ),
    (
        "Care afirmații despre Hobo Syndrome sunt corecte?",
        (
            "Turnoverul trecut poate prezice turnoverul viitor",
            "Este un model de satisfacție a muncii",
            "Istoricul profesional are valoare predictivă",
            "Este legat de mobilitatea ocupațională",
        ),
        "acd",
    ),
    (
        "Care dintre următoarele sunt valori orientate spre ceilalți în modelul Schwartz?",
        ("Universalism", "Bunăvoință", "Putere", "Realizare"),
        "ab",
    ),
    (
        "Criterion Relevance crește atunci când:",
        (
            "Măsurăm exact ceea ce dorim să evaluăm",
            "Reducem Criterion Deficiency",
            "Creștem influențele nerelevante",
            "Reducem Criterion Contamination",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt efecte ale satisfacției ridicate?",
        (
            "Turnover mai redus",
            "OCB mai frecvent",
            "Performanță garantat excelentă",
            "Angajament organizațional mai mare",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt exemple de Hindrance Stressors?",
        (
            "Ambiguitatea rolului",
            "Birocrația excesivă",
            "Oportunitățile de dezvoltare",
            "Conflictele organizaționale",
        ),
        "abd",
    ),
    (
        "Un candidat acceptat care performează slab reprezintă:",
        ("True Positive", "False Positive", "False Negative", "Criterion Contamination"),
        "b",
    ),
    (
        "Care dintre următoarele sunt surse de Criterion Contamination?",
        (
            "Favoritism",
            "Simpatie personală",
            "Reputație anterioară",
            "Lipsa unor dimensiuni relevante",
        ),
        "abc",
    ),
    (
        "În modelul Hackman și Oldham, autonomia contribuie direct la:",
        ("Meaningfulness", "Knowledge of Results", "Responsibility", "Engagement"),
        "c",
    ),
    (
        "Care dintre următoarele sunt predictori ai OCB?",
        (
            "Satisfacția muncii",
            "Agreabilitatea",
            "Justiția organizațională",
            "Neuroticismul ridicat",
        ),
        "abc",
    ),
    (
        "Spill-over pozitiv apare atunci când:",
        (
            "Stresul unei persoane afectează partenerul",
            "Satisfacția muncii crește satisfacția vieții",
            "Emoțiile pozitive se transferă între roluri ale aceleiași persoane",
            "Burnout-ul se transmite între colegi",
        ),
        "bc",
    ),
    (
        "Cross-over presupune:",
        (
            "Transfer între persoane",
            "Transfer între domenii ale vieții aceleiași persoane",
            "Transmiterea stresului sau satisfacției",
            "Influențe emoționale reciproce",
        ),
        "acd",
    ),
    (
        "Care dintre următoarele caracteristici aparțin Job Description?",
        (
            "Responsabilități",
            "Sarcini",
            "Educație necesară",
            "Condiții de muncă",
        ),
        "abd",
    ),
    (
        "Care afirmații despre GMA sunt corecte?",
        (
            "Este unul dintre cei mai buni predictori ai performanței",
            "Reprezintă inteligența generală",
            "Este identic cu experiența profesională",
            "Facilitează învățarea",
        ),
        "abd",
    ),
    (
        "În GAS, etapa de epuizare apare când:",
        (
            "Resursele de adaptare sunt consumate",
            "Organismul se adaptează cu succes",
            "Solicitările persistă prea mult timp",
            "Nu mai poate fi susținut efortul de adaptare",
        ),
        "acd",
    ),
    (
        "Care dintre următoarele sunt metode de analiză a muncii?",
        ("Observația", "Interviul", "Chestionarul", "Incidentele critice"),
        "abcd",
    ),
    (
        "Care dintre următoarele sunt asociate cu Performance Appraisal?",
        (
            "Evaluarea performanței actuale",
            "Feedback",
            "Aprecierea rezultatelor",
            "Stabilirea salariului",
        ),
        "abcd",
    ),
    (
        "Forced Distribution urmărește în principal:",
        (
            "Reducerea indulgenței evaluatorilor",
            "Distribuirea angajaților pe categorii prestabilite",
            "Eliminarea tuturor erorilor de evaluare",
            "Diferențierea performanțelor",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt asociate cu Conștiinciozitatea?",
        ("Organizare", "Responsabilitate", "Autodisciplină", "Impulsivitate"),
        "abc",
    ),
    (
        "Care dintre următoarele sunt beneficii ale socializării organizaționale?",
        (
            "Clarificarea rolurilor",
            "Adaptarea mai rapidă",
            "Reducerea Value Fit",
            "Integrarea în cultură",
        ),
        "abd",
    ),
    (
        "În BOS se măsoară:",
        (
            "Frecvența comportamentelor",
            "Calitatea comportamentelor",
            "Apariția comportamentelor observabile",
            "Intensitatea emoțiilor",
        ),
        "ac",
    ),
    (
        "Care dintre următoarele sunt exemple de Task Performance?",
        (
            "Predarea unui curs",
            "Corectarea examenelor",
            "Ajutor voluntar acordat colegilor",
            "Realizarea sarcinilor principale ale postului",
        ),
        "abd",
    ),
    (
        "OCB și CWB:",
        (
            "sunt constructe opuse conceptual",
            "pot coexista la aceeași persoană",
            "sunt identice cu performanța contextuală",
            "influențează funcționarea organizației",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt asociate cu evaluarea secundară la Lazarus?",
        (
            "Pot face față situației?",
            "Ce resurse am disponibile?",
            "Este situația amenințătoare?",
            "Ce strategie de coping aleg?",
        ),
        "abd",
    ),
    (
        "În Taylor-Russell sunt importante:",
        ("Base Rate", "Selection Ratio", "Validitatea predictorului", "Nivelul de satisfacție"),
        "abc",
    ),
    (
        "Care dintre următoarele sunt exemple de Job Control?",
        (
            "Alegerea modului de lucru",
            "Decizii privind organizarea activității",
            "Control asupra ritmului de lucru",
            "Nivelul salariului",
        ),
        "abc",
    ),
    (
        "Un evaluator influențat excesiv de performanțele recente comite eroarea:",
        ("Halo", "Primacy", "Recency", "Leniency"),
        "c",
    ),
    (
        "Care dintre următoarele sunt componente ale Feedbackului eficient?",
        ("Specificitate", "Relevanță", "Oportunitate temporală", "Ambiguitate"),
        "abc",
    ),
    (
        "Care dintre următoarele sunt exemple de Contextual Performance?",
        (
            "Cooperare cu colegii",
            "Inițiativă voluntară",
            "Respectarea strictă a sarcinilor obligatorii",
            "Implicare suplimentară",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt asociate cu Burnout?",
        (
            "Epuizare emoțională",
            "Cinism",
            "Ineficacitate percepută",
            "Vitalitate ridicată",
        ),
        "abc",
    ),
    (
        "Value Fit ridicat este asociat cu:",
        (
            "Turnover redus",
            "Angajament crescut",
            "Conflict permanent de valori",
            "Satisfacție mai mare",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele sunt exemple de False Negative?",
        (
            "Respingerea unui candidat care ar fi performat bine",
            "Acceptarea unui candidat slab",
            "Eroare de selecție",
            "Pierderea unui candidat valoros",
        ),
        "acd",
    ),
    (
        "În modelul lui Schwartz, Puterea și Realizarea sunt valori orientate:",
        (
            "spre sine",
            "spre schimbare",
            "spre ceilalți",
            "spre afirmare personală",
        ),
        "ad",
    ),
    (
        "Care dintre următoarele sunt avantaje ale Feedbackului 360°?",
        (
            "Perspectivă multiplă",
            "Informații mai complete",
            "Eliminarea completă a biasurilor",
            "Evaluare mai cuprinzătoare",
        ),
        "abd",
    ),
    (
        "Care dintre următoarele concepte sunt printre cele mai importante din întreg cursul?",
        ("JD-R", "GMA", "Criterion Deficiency", "Feedback 360°"),
        "abcd",
    ),
]


def build_items() -> List[Dict]:
    return [
        build_exam_item(START_ID + i, stem, opts, correct, LOT_NAME)
        for i, (stem, opts, correct) in enumerate(_RAW)
    ]


def merge_into_bank(bank_path: str) -> int:
    import json
    from pathlib import Path

    path = Path(bank_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    lots = data.setdefault("lots", {})
    if LOT_NAME in lots:
        return 0
    lots[LOT_NAME] = {"questions": build_items()}
    total = sum(len(b.get("questions") or []) for b in lots.values())
    data["total_questions"] = total
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(build_items())
