"""Date brute — Psihoterapie II: orientări și metode în psihoterapie."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ITEMS: List[Item] = [
    # —— Psihodinamic / freudian ——
    {
        "stem": "Abordarea psihodinamică pune accent pe:",
        "options": [
            "comportamente observabile și întăriri imediate",
            "inconștient, conflicte interne și experiențe timpurii",
            "restructurarea cognitivă a gândurilor automate",
            "rolurile și regulile sistemului familial",
        ],
        "correct": "b",
    },
    {
        "stem": "Psihanaliza freudiană urmărește în principal:",
        "options": [
            "restructurarea personalității prin explorarea inconștientului",
            "eliminarea simptomului vizibil pe termen scurt",
            "antrenarea abilităților sociale prin modelare",
            "clarificarea alegerilor și responsabilității în prezent",
        ],
        "correct": "a",
    },
    {
        "stem": "La Freud, Sinele (Es) funcționează după:",
        "options": [
            "principiul realității",
            "principiul plăcerii",
            "normele morale interiorizate",
            "logica socială a grupului",
        ],
        "correct": "b",
    },
    {
        "stem": "Care afirmații descriu corect aparatul psihic freudian?",
        "options": [
            "Eul mediază între Sine, Supraeu și realitate",
            "Supraeul este legat de conștiința morală și vinovăție",
            "Sinele caută satisfacerea imediată a impulsurilor",
            "Sinele funcționează după principiul realității",
        ],
        "correct": "abc",
    },
    {
        "stem": "Dacă Eul nu reușește să medieze tensiunile dintre Sine, Supraeu și realitate, pot apărea:",
        "options": [
            "anxietate, conflicte interne și simptome nevrotice",
            "consolidarea funcțiilor cognitive superioare",
            "reorganizarea structurii și granițelor familiale",
            "disocierea completă între trecut și prezent",
        ],
        "correct": "a",
    },
    {
        "stem": "Stadiul oral freudian este asociat cu:",
        "options": [
            "apariția complexului Oedip",
            "zona erogenă a gurii și primul an de viață",
            "controlul sfincterian și autonomia",
            "matuizarea sexualității în adolescență",
        ],
        "correct": "b",
    },
    {
        "stem": "Stadiul anal se caracterizează prin:",
        "options": [
            "accent pe control, ordine și raportarea la autoritate",
            "diminuarea relativă a energiei sexuale și orientare spre școală",
            "identificarea cu părintele de același sex",
            "integrarea identității adulte",
        ],
        "correct": "a",
    },
    {
        "stem": "Care asocieri sunt corecte pentru stadiile psihosexuale?",
        "options": [
            "stadiul falic — complexul Oedip/Electra",
            "stadiul de latență — relativă liniștire, nu dispariția dezvoltării",
            "stadiul genital — maturizare sexuală și relații intime",
            "stadiul falic — absența oricărei sexualități psihice",
        ],
        "correct": "abc",
    },
    {
        "stem": "Stadiul de latență (aprox. 6–12 ani) presupune:",
        "options": [
            "dispariția completă a dezvoltării psihosexuale",
            "energie sexuală relativ diminuată și orientare spre școală și joc",
            "apariția exclusivă a mecanismelor de apărare patologice",
            "fixarea obligatorie pe zona anală",
        ],
        "correct": "b",
    },
    {
        "stem": "Reprimarea, ca mecanism de apărare, presupune:",
        "options": [
            "atribuirea propriilor impulsuri altor persoane",
            "excluderea din conștiință a conținuturilor dureroase",
            "canalizarea impulsurilor spre activități social acceptate",
            "întoarcerea la reacții infantile",
        ],
        "correct": "b",
    },
    {
        "stem": "Care mecanisme de apărare sunt descrise corect?",
        "options": [
            "proiecția — atribuirea propriilor impulsuri altora",
            "raționalizarea — explicații aparent logice pentru motive inacceptabile",
            "sublimarea — canalizarea impulsurilor spre activități acceptate social",
            "negarea — acceptarea lucidă a realității amenințătoare",
        ],
        "correct": "abc",
    },
    {
        "stem": "Introiecția, în perspectivă psihodinamică, înseamnă:",
        "options": [
            "preluarea în sine a unor caracteristici sau norme ale altora",
            "refuzul total de a percepe o realitate amenințătoare",
            "evitarea contactului prin glume și schimbarea subiectului",
            "întoarcerea energiei spre exterior împotriva altcuiva",
        ],
        "correct": "a",
    },
    {
        "stem": "Mecanismele de apărare devin problematice atunci când:",
        "options": [
            "sunt rigide, excesive sau rup persoana de realitate",
            "apar ocazional într-un context stresant",
            "reduc temporar anxietatea într-o situație limită",
            "sunt folosite conștient în terapie ca tehnici de relaxare",
        ],
        "correct": "a",
    },
    {
        "stem": "Asociația liberă în psihoterapia psihodinamică urmărește:",
        "options": [
            "accesul la material inconștient prin exprimare fără cenzură",
            "antrenarea răspunsurilor condiționate la stimuli neutri",
            "reformularea empatică a mesajului clientului",
            "stabilirea unui plan comportamental pentru acasă",
        ],
        "correct": "a",
    },
    {
        "stem": "Care tehnici aparțin procesului psihanalitic/psihodinamic?",
        "options": [
            "analiza viselor",
            "analiza transferului",
            "analiza rezistențelor",
            "desensibilizarea sistematică",
        ],
        "correct": "abc",
    },
    {
        "stem": "În psihoterapia psihodinamică, contratransferul desemnează:",
        "options": [
            "reacțiile și atitudinile emoționale ale terapeutului față de client",
            "sentimentele și așteptările clientului proiectate asupra terapeutului",
            "refuzul clientului de a vorbi despre relațiile din copilărie",
            "reformularea empatică a mesajului în consilierea centrată pe persoană",
        ],
        "correct": "a",
    },
    {
        "stem": "Carl Gustav Jung este asociat cu:",
        "options": [
            "inconștientul colectiv, arhetipuri și procesul de individuare",
            "sentimentul de inferioritate și stilul de viață",
            "terapia rațional-emotivă și credințele iraționale",
            "terapia centrată pe realitate și alegeri prezente",
        ],
        "correct": "a",
    },
    {
        "stem": "Alfred Adler pune accent pe:",
        "options": [
            "arhetipuri și inconștient colectiv",
            "inferioritate, compensare, stil de viață și interes social",
            "gânduri automate și scheme cognitive",
            "granițe și ierarhii în sistemul familial",
        ],
        "correct": "b",
    },
    {
        "stem": "Karen Horney este cunoscută pentru accentul pus pe:",
        "options": [
            "condiționarea operantă",
            "anxietatea bazală și relațiile interpersonale",
            "ciclul experienței și figură-fond",
            "sociometrie și scenă psihodramatică",
        ],
        "correct": "b",
    },
    {
        "stem": "Jung nu reduce psihicul la sexualitate, ci introduce:",
        "options": [
            "inconștientul colectiv și arhetipurile",
            "analiza transferului în relația terapeutică clasică",
            "tehnici comportamentale de expunere și relaxare",
            "interpretarea rigidă a viselor ca profeții literale",
        ],
        "correct": "a",
    },
    # —— Existențial ——
    {
        "stem": "Abordarea existențială pune accent pe:",
        "options": [
            "libertate, responsabilitate, sens și condiția umană",
            "restructurarea schemei cognitive disfuncționale",
            "întărirea răspunsurilor adaptative prin consecințe",
            "analiza inconștientului și a conflictelor infantile",
        ],
        "correct": "a",
    },
    {
        "stem": "Care teme sunt centrale în consilierea existențială?",
        "options": [
            "anxietatea existențială",
            "căutarea sensului vieții",
            "confruntarea cu moartea și finitudinea",
            "eliminarea exclusivă a simptomelor fără reflecție asupra modului de a trăi",
        ],
        "correct": "abc",
    },
    {
        "stem": "În abordarea existențială, anxietatea existențială poate fi înțeleasă ca:",
        "options": [
            "un semn al confruntării cu libertatea, responsabilitatea sau finitudinea",
            "un simptom care trebuie eliminat fără reflecție asupra modului de a trăi",
            "o reacție fără legătură cu alegerile și valorile personale",
            "un indiciu că trebuie folosită doar desensibilizarea sistematică",
        ],
        "correct": "a",
    },
    {
        "stem": "Consilierea existențială poate folosi tehnici precum:",
        "options": [
            "fantezia dirijată și dramatizarea",
            "experimentarea imaginară a propriei morți pentru clarificarea valorilor",
            "desensibilizarea sistematică clasică",
            "analiza transferului în sens strict freudian",
        ],
        "correct": "ab",
    },
    # —— Rogers ——
    {
        "stem": "Consilierea centrată pe persoană (Carl R. Rogers) se bazează pe:",
        "options": [
            "tendința de actualizare a persoanei",
            "directive clare ale terapeutului pentru repararea clientului",
            "interpretarea simbolică obligatorie a viselor",
            "modificarea ierarhiilor din sistemul familial",
        ],
        "correct": "a",
    },
    {
        "stem": "Care sunt condițiile facilitatoare la Rogers?",
        "options": [
            "congruența terapeutului",
            "acceptarea pozitivă necondiționată",
            "înțelegerea empatică",
            "interpretarea sugestivă a inconștientului",
        ],
        "correct": "abc",
    },
    {
        "stem": "Condițiile de valoare la Rogers apar atunci când:",
        "options": [
            "acceptarea este condiționată de aprobarea celorlalți",
            "clientul este acceptat necondiționat ca persoană",
            "terapeutul oferă soluții concrete pentru fiecare problemă",
            "clientul este evaluat permanent prin teste standardizate",
        ],
        "correct": "a",
    },
    {
        "stem": "Ascultarea reflectivă la Rogers înseamnă:",
        "options": [
            "înțelegerea mesajului clientului și redarea lui într-o formă clarificatoare",
            "sfaturi, moralizare și persuasiune directă",
            "interpretarea ascunsă a motivațiilor inconștiente",
            "confruntarea imediată cu distorsiunile cognitive",
        ],
        "correct": "a",
    },
    {
        "stem": "Care tehnici aparțin ascultării reflective?",
        "options": [
            "reflectarea tip ecou",
            "parafrazarea",
            "reflectarea sentimentelor",
            "tehnica aversivă",
        ],
        "correct": "abc",
    },
    {
        "stem": "În grupurile rogersiene, coordonatorul:",
        "options": [
            "facilitează procesul, fără a conduce autoritar grupul",
            "impune interpretări standard pentru fiecare participant",
            "folosește scena și rolurile ca în psihodramă clasică",
            "evaluează membrii prin note și ierarhii fixe",
        ],
        "correct": "a",
    },
    {
        "stem": "Rogers nu urmărește „repararea” clientului prin directive, ci:",
        "options": [
            "facilitarea dezvoltării într-un climat de acceptare, empatie și congruență",
            "eliminarea inconștientului prin sugestie hipnotică",
            "modificarea structurii cromozomiale a trăsăturilor",
            "prescrierea unui plan familial rigid",
        ],
        "correct": "a",
    },
    # —— Gestalt ——
    {
        "stem": "Psihoterapia Gestalt (Fritz Perls) este:",
        "options": [
            "holistă, experiențială, orientată spre aici și acum",
            "strict psihanalitică și orientată spre trecutul infantil",
            "strict comportamentală, cu redus accent pe experiența subiectivă",
            "centrată pe regulile homeostaziei familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "Care concepte sunt centrale în terapia gestaltistă?",
        "options": [
            "contactul autentic cu sine și cu mediul",
            "conștientizarea experienței prezente",
            "integrarea polarităților",
            "reprimarea permanentă a emoțiilor ca scop terapeutic",
        ],
        "correct": "abc",
    },
    {
        "stem": "În terapia gestaltistă, retroflexia presupune:",
        "options": [
            "energia orientată spre exterior este întoarsă împotriva propriei persoane",
            "preluarea normelor din exterior fără asimilare personală",
            "lipsa graniței între sine și ceilalți",
            "evitarea contactului prin deviere sau superficialitate",
        ],
        "correct": "a",
    },
    {
        "stem": "Care rezistențe la contact sunt descrise corect în terapia gestaltistă?",
        "options": [
            "introiecția — preluare de valori fără asimilare personală",
            "proiecția — atribuirea altora a propriilor trăiri",
            "confluența — confuzia granițelor dintre sine și ceilalți",
            "sublimarea — canalizarea impulsurilor spre artă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Introiecția gestaltică se deosebește de proiecție astfel:",
        "options": [
            "introiecția = preluare în sine; proiecția = atribuire către celălalt",
            "introiecția = atribuire către celălalt; proiecția = preluare în sine",
            "ambele înseamnă refuzul realității externe",
            "ambele sunt tehnici rogersiene de ascultare reflectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Ciclul experienței Gestalt descrie:",
        "options": [
            "modul în care o nevoie devine figură, mobilizează energie și poate fi satisfăcută prin contact",
            "etapele dezvoltării psihosexuale freudiene",
            "succesiunea întăririlor și pedepselor în condiționarea operantă",
            "ierarhia subsistemelor într-o familie structuralistă",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul în abordarea gestaltistă încurajează formulări la persoana întâi, de exemplu:",
        "options": [
            "„mie îmi este greu”, nu doar „este greu”",
            "„ei sunt vinovați”, pentru externalizare maximă",
            "„se știe că așa e”, pentru neutralitate",
            "„terapeutul consideră că…”, pentru autoritate",
        ],
        "correct": "a",
    },
    {
        "stem": "Tehnici gestaltice includ:",
        "options": [
            "scaunul gol",
            "dialogul polarităților",
            "focalizarea corporală",
            "desensibilizarea sistematică în sens strict behaviorist",
        ],
        "correct": "abc",
    },
    # —— Comportamental / CBT ——
    {
        "stem": "Abordarea comportamentală clasică se concentrează pe:",
        "options": [
            "comportamente observabile, stimul–răspuns și învățare",
            "explorarea simbolică a viselor",
            "acceptarea necondiționată și empatia",
            "granițele și alianțele din familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Care asocieri autor–idee sunt corecte?",
        "options": [
            "Pavlov — condiționare clasică",
            "Skinner — condiționare operantă",
            "Ellis — terapia rațional-emotivă",
            "Beck — terapia cognitivă",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Desensibilizarea sistematică este folosită mai ales pentru:",
        "options": [
            "anxietăți și fobii, prin relaxare și expunere gradată",
            "interpretarea transferului în relația terapeutică",
            "clarificarea sensului existențial al vieții",
            "restructurarea ierarhiei familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "Modelarea în terapia comportamentală presupune:",
        "options": [
            "învățarea unui comportament prin observare și imitare",
            "asocierea unui comportament cu un stimul neplăcut",
            "analiza viselor ca expresie simbolică",
            "acceptarea necondiționată a clientului",
        ],
        "correct": "a",
    },
    {
        "stem": "Modelul Activator, Beliefs, Consequences (A-B-C) la Ellis descrie:",
        "options": [
            "evenimentul activator, credințele despre eveniment și consecințele emoționale/comportamentale",
            "atașamentul, comportamentul și consecința socială",
            "anxietatea, blocajul și conștientizarea",
            "automatizarea, biologia și cogniția",
        ],
        "correct": "a",
    },
    {
        "stem": "Aaron T. Beck este asociat cu:",
        "options": [
            "gânduri automate negative, scheme și distorsiuni cognitive",
            "inconștientul colectiv și arhetipurile",
            "spontaneitatea scenică și eurile auxiliare",
            "homeostazia și feedbackul în sistemul familial",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia multimodală (Lazarus) evaluează:",
        "options": [
            "profilul multidimensional al clientului (comportament, afect, cogniție, senzație, relații)",
            "conflictele inconștiente și istoricul relațiilor obiectuale din copilărie",
            "transferul, contratransferul și repetarea relațiilor timpurii în cabinet",
            "patternurile de comunicare și granițele din sistemul familial extins",
        ],
        "correct": "a",
    },
    # —— Terapia realității ——
    {
        "stem": "Psihoterapia centrată pe realitate (William Glasser) pune accent pe:",
        "options": [
            "alegeri, responsabilitate personală și comportamentul prezent",
            "analiza inconștientului și a copilăriei",
            "acceptarea necondiționată ca unic mecanism de schimbare",
            "restructurarea colectivă a normelor familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia realității, întrebările utile vizează:",
        "options": [
            "ce face clientul acum și dacă acțiunile îl apropie de scopuri",
            "interpretarea viselor și conflictelor din copilărie",
            "mecanismele de apărare inconștiente ca explicație principală",
            "cine este „identificat” ca purtător al simptomului în familie",
        ],
        "correct": "a",
    },
    # —— Terapia de familie ——
    {
        "stem": "În terapia de familie, familia este conceptualizată, de regulă, ca:",
        "options": [
            "un sistem relațional în care membrii se influențează reciproc",
            "o colecție de indivizi separați, fără interacțiuni relevante",
            "repetarea mecanică a stadiilor psihosexuale freudiene",
            "un grup de susținere fără reguli sau patternuri relaționale",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia de familie, din perspectivă sistemică, simptomul unui membru este adesea înțeles ca un semn al:",
        "options": [
            "unor dificultăți în modul în care familia comunică, se organizează și se influențează reciproc",
            "unei probleme strict biologice, independente de relațiile familiale",
            "necesității de a elimina comunicarea dintre membri",
            "vinovăției exclusive a acelei persoane, indiferent de contextul familial",
        ],
        "correct": "a",
    },
    {
        "stem": "Care abordări apar în terapia de familie?",
        "options": [
            "structurală — granițe, subsisteme, ierarhie",
            "sistemică — reguli, feedback, homeostazie",
            "strategică — intervenții concrete pentru schimbarea interacțiunilor",
            "rațional-emotivă — doar înlocuirea credințelor individuale, fără context relațional",
        ],
        "correct": "abc",
    },
    {
        "stem": "În terapia de familie, una dintre întrebările centrale pentru terapeut este:",
        "options": [
            "cum este menținută problema în modul în care membrii interacționează",
            "cine este singurul vinovat care trebuie corectat",
            "cum putem elimina toate emoțiile din relație",
            "cum evităm stabilirea oricăror reguli sau limite",
        ],
        "correct": "a",
    },
    # —— Set suplimentar (recapitulare și diferențieri) ——
    {
        "stem": "La Freud, Supraeul este asociat cu:",
        "options": [
            "principiul plăcerii și impulsurile biologice imediate",
            "interiorizarea normelor, idealurilor și conștiinței morale",
            "medierea exclusivă între stimul și răspuns observabil",
            "acceptarea necondiționată a clientului în relație",
        ],
        "correct": "b",
    },
    {
        "stem": "Eul (Ego) freudian funcționează după:",
        "options": [
            "principiul plăcerii",
            "principiul realității",
            "principiul homeostaziei familiale",
            "principiul restructurării cognitive",
        ],
        "correct": "b",
    },
    {
        "stem": "O fixare în stadiul oral poate fi asociată cu:",
        "options": [
            "dependență, neîncredere sau dificultăți relaționale",
            "obsesie exclusivă pentru controlul sfincterian",
            "identificarea obligatorie cu părintele de sex opus",
            "absența oricărei investiri afective în relații",
        ],
        "correct": "a",
    },
    {
        "stem": "Care distincții sunt corecte între mecanismele de apărare?",
        "options": [
            "negarea — refuzul de a accepta o realitate amenințătoare",
            "reprimarea — excluderea din conștiință a conținuturilor dureroase",
            "sublimarea — canalizarea impulsurilor spre activități acceptate social",
            "proiecția — preluarea în sine a normelor altora",
        ],
        "correct": "abc",
    },
    {
        "stem": "Compensarea, ca mecanism de apărare, presupune:",
        "options": [
            "mascarea unei vulnerabilități prin accentuarea unei alte calități",
            "refuzul total de a percepe o amenințare externă",
            "atribuirea altora a propriilor dorințe reprimate",
            "întoarcerea la comportamente caracteristice stadiului anal",
        ],
        "correct": "a",
    },
    {
        "stem": "Analiza rezistențelor în psihoterapia psihodinamică urmărește:",
        "options": [
            "blocajele, evitările sau tăcerile care împiedică accesul la material dificil",
            "modificarea ierarhiei dintre părinți și copii în familie",
            "antrenarea relaxării musculare progresive",
            "înlocuirea credințelor iraționale cu altele raționale",
        ],
        "correct": "a",
    },
    {
        "stem": "În psihanaliză, interpretarea trebuie să:",
        "options": [
            "oferă sens materialului inconștient fără a fi impusă sugestiv",
            "convingă imediat clientul că terapeutul are dreptate",
            "evite orice referire la trecut sau la relația terapeutică",
            "înlocuiască consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "Melanie Klein este asociată cu dezvoltarea:",
        "options": [
            "analizei relațiilor obiectuale",
            "terapiei multimodale",
            "sociometriei",
            "terapiei centrate pe realitate",
        ],
        "correct": "a",
    },
    {
        "stem": "În consilierea existențială, libertatea este legată de:",
        "options": [
            "responsabilitatea alegerilor personale",
            "determinismul biologic exclusiv",
            "eliminarea oricărei anxietăți prin medicatie",
            "interpretarea obligatorie a viselor",
        ],
        "correct": "a",
    },
    {
        "stem": "La Rogers, imaginea de sine incongruentă poate:",
        "options": [
            "bloca dezvoltarea personalității",
            "garanta autoactualizarea rapidă",
            "elimina nevoia de empatie",
            "înlocui contactul psihologic autentic",
        ],
        "correct": "a",
    },
    {
        "stem": "Care trăsături descriu persoana autoactualizată în viziunea lui Rogers?",
        "options": [
            "deschidere față de experiență",
            "autenticitate și orientare spre creștere",
            "relații profunde cu ceilalți",
            "dependență rigidă de aprobarea terapeutului",
        ],
        "correct": "abc",
    },
    {
        "stem": "Deflecția, ca rezistență la contact în terapia gestaltistă, presupune:",
        "options": [
            "evitarea contactului direct prin deviere, glume sau schimbarea subiectului",
            "întoarcerea energiei împotriva propriei persoane",
            "confundarea granițelor dintre sine și grup",
            "preluarea mecanică a valorilor familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "În ciclul experienței Gestalt, când o nevoie nu este satisfăcută, pot apărea:",
        "options": [
            "retragere, evitare sau tensiune cronică",
            "îmbunătățirea automată a contactului fără conștientizare",
            "dispariția definitivă a figurii pe fond",
            "fixare freudiană în stadiul oral",
        ],
        "correct": "a",
    },
    {
        "stem": "Tehnica aversivă în abordarea comportamentală presupune:",
        "options": [
            "asocierea comportamentului dezadaptativ cu un stimul neplăcut",
            "relaxarea progresivă în fața unui stimul neutru",
            "interpretarea simbolică a viselor",
            "acceptarea necondiționată a clientului",
        ],
        "correct": "a",
    },
    {
        "stem": "Care tehnici aparțin modificării comportamentului?",
        "options": [
            "întărirea pozitivă",
            "întărirea negativă",
            "controlul consecințelor",
            "analiza transferului",
        ],
        "correct": "abc",
    },
    {
        "stem": "În terapia cognitivă beckiană, accentul cade pe:",
        "options": [
            "gânduri automate, scheme și distorsiuni cognitive",
            "arhetipuri și inconștient colectiv",
            "regulile homeostaziei familiale",
            "spontaneitatea scenică și rolurile auxiliare",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia rațional-emotivă (REBT) a lui Ellis vizează în special:",
        "options": [
            "identificarea și modificarea convingerilor iraționale",
            "explorarea exclusivă a relațiilor obiectuale timpurii",
            "restructurarea ierarhiei generaționale în familie",
            "eliminarea contactului cu emoțiile prezente",
        ],
        "correct": "a",
    },
    {
        "stem": "Intervențiile cognitiv-comportamentale sunt, de regulă:",
        "options": [
            "structurate, active și orientate spre schimbare concretă",
            "pasive, nedirective și fără obiective clare",
            "centrate exclusiv pe interpretarea simbolică a viselor",
            "limitate la relația terapeutică fără exerciții",
        ],
        "correct": "a",
    },
    {
        "stem": "Abordarea psihodinamică în terapia de familie urmărește:",
        "options": [
            "influența relațiilor timpurii, a conflictelor și a transferurilor în viața familială",
            "întărirea comportamentelor prin recompense imediate",
            "tehnici de relaxare și expunere ca intervenție centrală",
            "eliminarea referințelor la trecutul parental",
        ],
        "correct": "a",
    },
    {
        "stem": "Abordarea structurală în terapia de familie pune accent pe:",
        "options": [
            "granițe, subsisteme, ierarhie și organizarea relațiilor",
            "credințele iraționale ale unui singur membru al familiei",
            "interpretarea colectivă a arhetipurilor jungiene",
            "experimentarea morții ca tehnică centrală",
        ],
        "correct": "a",
    },
    {
        "stem": "Abordarea strategică în terapia de familie se caracterizează prin:",
        "options": [
            "intervenții concrete pentru schimbarea interacțiunilor problematice",
            "explorarea liberă a inconștientului fără țintă",
            "refuzul oricărei intervenții planificate",
            "lucrul exclusiv individual, fără membrii familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi orientare–accent sunt corecte?",
        "options": [
            "Freud — inconștient, conflicte, mecanisme de apărare",
            "Rogers — actualizare, empatie, acceptare necondiționată",
            "Terapia gestaltistă — aici și acum, contact, conștientizare",
            "Glasser — analiza viselor și transferul",
        ],
        "correct": "abc",
    },
    {
        "stem": "Watson este asociat cu:",
        "options": [
            "aplicarea condiționării la comportamentul uman",
            "inconștientul colectiv",
            "terapia rațional-emotivă",
            "scaunul gol gestaltic",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia de familie, abordarea experiențială pune accent pe:",
        "options": [
            "exprimarea emoțiilor, autenticitate și contact afectiv între membri",
            "restructurarea cognitivă individuală, fără lucrul cu relațiile",
            "pedeapsa consecventă a membrului cu simptom",
            "evitarea emoțiilor pentru a menține „calmul” în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Stadiul falic (aprox. 3–6 ani) este asociat cu:",
        "options": [
            "complexul Oedip/Electra și identificarea cu părintele de același sex",
            "controlul sfincterian și raportarea la autoritate",
            "orientarea predominantă spre școală și jocuri de echipă",
            "matuizarea relațiilor intime adulte",
        ],
        "correct": "a",
    },
    # —— Set suplimentar II (după textul cursului) ——
    {
        "stem": "Față de abordările strict deterministe, orientările umanist-experiențiale insistă că:",
        "options": [
            "persoana are potențial de creștere, libertate și responsabilitate",
            "omul poate fi redus exclusiv la reflexe condiționate",
            "experiența subiectivă și relația terapeutică au importanță centrală",
            "tehnica rigidă este mai importantă decât contactul autentic",
        ],
        "correct": "ac",
    },
    {
        "stem": "Analiza viselor, în psihoterapia psihodinamică, presupune că visul poate fi:",
        "options": [
            "o expresie simbolică a dorințelor și conflictelor inconștiente",
            "un material de evaluare standardizată fără interpretare",
            "dovada directă a unei afecțiuni organice",
            "irelevant pentru procesul terapeutic",
        ],
        "correct": "a",
    },
    {
        "stem": "În psihoterapia psihodinamică, analiza transferului urmărește înțelegerea modului în care clientul:",
        "options": [
            "proiectează asupra terapeutului sentimente și modele relaționale din relații importante anterioare",
            "transferă obligatoriu responsabilitatea terapiei către un alt specialist",
            "evită discuția despre relațiile actuale din viața de zi cu zi",
            "învață tehnici de relaxare musculară progresivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Care concepte jungiene sunt corect asociate?",
        "options": [
            "Persona — masca socială",
            "Umbra — aspecte respinse sau neasumate",
            "inconștientul colectiv și arhetipurile",
            "stilul de viață și interesul social",
        ],
        "correct": "abc",
    },
    {
        "stem": "Karen Horney pune accent pe anxietatea bazală și pe:",
        "options": [
            "relațiile interpersonale",
            "condiționarea operantă strictă",
            "ierarhia subsistemelor familiale",
            "desensibilizarea sistematică",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea existențială, teme precum singurătatea, moartea și sensul vieții:",
        "options": [
            "sunt centrale pentru modul de a trăi și de a alege",
            "trebuie evitate complet în terapie",
            "sunt relevante doar în terapia de familie",
            "înlocuiesc orice discuție despre emoții",
        ],
        "correct": "a",
    },
    {
        "stem": "Confruntarea cu moartea, în perspectivă existențială, poate:",
        "options": [
            "da intensitate și direcție vieții prin conștientizarea finitudinii",
            "elimina necesitatea oricărei responsabilități personale",
            "dovedi că libertatea umană este iluzorie",
            "înlocui consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "Tendința de actualizare la Rogers desemnează:",
        "options": [
            "forța internă de creștere, maturizare și organizare pozitivă",
            "obligația terapeutului de a corecta defectele clientului",
            "adaptarea prin reprimarea permanentă a emoțiilor",
            "determinismul biologic al comportamentului",
        ],
        "correct": "a",
    },
    {
        "stem": "Care condiții facilitatoare rogersiene sunt corect descrise?",
        "options": [
            "congruența terapeutului — autenticitate și coerență în relație",
            "acceptarea pozitivă necondiționată — acceptare fără judecată",
            "înțelegerea empatică — perspectiva clientului",
            "contactul psihologic — relație reală și suficient de stabilă",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Reflectarea tip ecou în ascultarea reflectivă presupune:",
        "options": [
            "repetarea unui cuvânt sau expresii relevante ale clientului",
            "o interpretare freudiană a visului",
            "prescrierea unui plan comportamental",
            "schimbarea subiectului către problemele terapeutului",
        ],
        "correct": "a",
    },
    {
        "stem": "Parafrazarea în consilierea centrată pe persoană este:",
        "options": [
            "o reformulare mai amplă a mesajului clientului, păstrând sensul",
            "o tehnică de expunere gradată la fobii",
            "interpretarea simbolică a transferului",
            "o metodă de restructurare a ierarhiei familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "Reflectarea sentimentelor urmărește:",
        "options": [
            "evidențierea emoției exprimate direct sau indirect",
            "negarea emoțiilor pentru a reduce anxietatea",
            "diagnosticarea medicală a tulburării de anxietate",
            "înlocuirea contactului cu interpretări morale",
        ],
        "correct": "a",
    },
    {
        "stem": "În grupurile centrate pe persoană (Rogers), participarea autentică poate contribui la:",
        "options": [
            "modificări în structura personalității și la contact interpersonal",
            "conformism și ascultarea obligatorie a directivei liderului",
            "evitarea exprimării emoțiilor în relație cu ceilalți",
            "înlocuirea responsabilității personale cu dependență de grup",
        ],
        "correct": "a",
    },
    {
        "stem": "Psihoterapia Gestalt este asociată cu Frederick S. Perls și pune accent pe:",
        "options": [
            "holism, conștientizare și contact aici și acum",
            "analiza exclusivă a inconștientului freudian",
            "întărirea și pedeapsa comportamentelor",
            "interpretarea rigidă a normelor familiale",
        ],
        "correct": "a",
    },
    {
        "stem": "Integrarea polarităților în terapia gestaltistă presupune:",
        "options": [
            "recunoașterea și integrarea părților opuse ale personalității",
            "reprimarea permanentă a uneia dintre polarități",
            "alegerea unei singure părți ca fiind „corectă” moral",
            "evitarea oricărui conflict intern",
        ],
        "correct": "a",
    },
    {
        "stem": "În ciclul experienței Gestalt, nevoia activată devine:",
        "options": [
            "figură pe fondul experienței",
            "mecanism de apărare freudian fix",
            "regulă de homeostazie familială",
            "credință irațională în sens ellisian",
        ],
        "correct": "a",
    },
    {
        "stem": "Skinner este asociat în principal cu:",
        "options": [
            "condiționarea operantă și rolul întăririlor",
            "condiționarea clasică a lui Pavlov",
            "terapia cognitivă a depresiei",
            "inconștientul colectiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Pavlov este cunoscut pentru:",
        "options": [
            "condiționarea clasică — asocierea stimul–răspuns",
            "condiționarea operantă",
            "analiza transferului",
            "ascultarea reflectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Desensibilizarea sistematică combină, de regulă:",
        "options": [
            "relaxarea cu expunerea gradată la stimuli anxiogeni",
            "interpretarea viselor cu analiza transferului",
            "restructurarea familiei cu pedeapsa consecventă",
            "acceptarea necondiționată cu interpretarea sugestivă",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea cognitiv-comportamentală, emoțiile și comportamentele sunt influențate de:",
        "options": [
            "modul în care persoana interpretează situațiile",
            "reflexele innate, cu redus accent pe procesele cognitive",
            "structura ierarhică și granițele din sistemul familial",
            "transferul și contratransferul în relația terapeutică",
        ],
        "correct": "a",
    },
    {
        "stem": "În modelul Activator, Beliefs, Consequences (A-B-C) al lui Ellis, litera B se referă la:",
        "options": [
            "credințele despre evenimentul activator",
            "biologia temperamentului",
            "beneficiile contractului terapeutic",
            "blocajul din ciclul gestaltic",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia multimodală a lui Lazarus urmărește:",
        "options": [
            "evaluarea mai multor dimensiuni ale funcționării persoanei",
            "eliminarea unui simptom izolat, fără alte dimensiuni",
            "explorarea copilăriei freudiene ca prioritate",
            "lucrul cu visul în sens jungian ca intervenție centrală",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia centrată pe realitate (Glasser), accentul cade pe comportamentul prezent și pe:",
        "options": [
            "responsabilitatea clientului pentru propriile alegeri",
            "analiza inconștientului ca explicație principală",
            "acceptarea necondiționată ca singură intervenție",
            "interpretarea simbolică obligatorie a copilăriei",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia de familie, expresia „pacientul identificat” (IP) descrie de obicei membrul care:",
        "options": [
            "aduce în vizibil simptomul unei dificultăți mai largi a sistemului familial",
            "este singurul responsabil pentru toate conflictele din familie",
            "nu necesită implicarea celorlalți membri în terapie",
            "demonstrează că familia nu are nicio influență asupra individului",
        ],
        "correct": "a",
    },
    {
        "stem": "Abordarea sistemică în terapia de familie vede familia ca sistem cu:",
        "options": [
            "reguli, feedback și tendință spre homeostazie",
            "membri complet independenți unii de alții",
            "obligația eliminării oricărei reguli",
            "focus exclusiv pe o singură genă comportamentală",
        ],
        "correct": "a",
    },
    {
        "stem": "Un obiectiv important al terapiei de familie este:",
        "options": [
            "îmbunătățirea comunicării și clarificarea limitelor, rolurilor și alianțelor",
            "identificarea unui singur vinovat care poartă toată responsabilitatea",
            "păstrarea neschimbate a patternurilor disfuncționale",
            "evitarea oricărei discuții despre regulile implicite din familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Regresia, ca mecanism de apărare, presupune:",
        "options": [
            "întoarcerea la moduri de reacție mai infantile sau mai vechi",
            "canalizarea impulsurilor spre activități social acceptate",
            "atribuirea propriilor sentimente altor persoane",
            "oferirea de explicații logic-sunătoare pentru motive inacceptabile",
        ],
        "correct": "a",
    },
    {
        "stem": "Sublimarea, ca mecanism de apărare al Eului, presupune:",
        "options": [
            "canalizarea impulsurilor inacceptabile spre activități social acceptate",
            "refuzul de a percepe o realitate amenințătoare",
            "preluarea normelor altora fără asimilare personală",
            "evitarea contactului prin schimbarea subiectului",
        ],
        "correct": "a",
    },
    {
        "stem": "Stadiul anal (aprox. 1–3 ani) este centrat pe:",
        "options": [
            "controlul sfincterian, autonomie și raportarea la autoritate",
            "complexul Oedip",
            "școală, jocuri și activități sociale",
            "relații intime adulte",
        ],
        "correct": "a",
    },
    {
        "stem": "Stadiul genital freudian presupune:",
        "options": [
            "matuizarea sexualității și integrarea identității adulte",
            "fixare exclusiv orală",
            "absența totală a dezvoltării psihosexuale",
            "identificarea cu părintele de sex opus în mod obligatoriu patologic",
        ],
        "correct": "a",
    },
    {
        "stem": "Contratransferul trebuie:",
        "options": [
            "conștientizat și gestionat profesional de terapeut",
            "exprimat liber ca relație de prietenie cu clientul",
            "notarea simptomelor fără monitorizarea evoluției în timp",
            "folosit pentru a impune valorile terapeutului",
        ],
        "correct": "a",
    },
    {
        "stem": "Relaxarea este folosită în desensibilizarea sistematică pentru a:",
        "options": [
            "reduce tensiunea fiziologică înaintea expunerii gradate",
            "interpreta simbolic visul clientului",
            "restructura ierarhia generațională",
            "înlocui consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia cognitiv-comportamentală, clientul este încurajat să:",
        "options": [
            "observe propriile gânduri și comportamente și să exerseze alternative mai adaptative",
            "evite monitorizarea interpretărilor pentru a nu crește anxietatea",
            "accepte că schimbarea este imposibilă fără interpretarea viselor",
            "lucreze doar pe trecut, fără exerciții practice între ședințe",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia de familie se concentrează în special pe:",
        "options": [
            "relații, comunicare, reguli, roluri, limite și alianțe dintre membri",
            "modificarea scorului la un test de aptitudine profesională",
            "interpretarea arhetipurilor jungiene ale fiecărui membru",
            "corectarea exclusivă a copilului considerat „problema” familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Ascultarea reflectivă nu înseamnă a da sfaturi sau soluții prestabilite.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În terapia gestaltistă, contactul presupune întâlnirea autentică cu sine, cu ceilalți și cu mediul.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Terapia centrată pe realitate insistă pe trecut ca explicație principală a comportamentului.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Stadiul de latență este o perioadă de relativă liniștire, nu de dispariție a dezvoltării.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Interpretarea în psihanaliză nu trebuie impusă sugestiv clientului.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Stadiul falic și stadiul genital freudian sunt același lucru.",
        "tf": True,
        "correct_tf": False,
    },
    # —— Adevărat / Fals ——
    {
        "stem": "Psihanaliza urmărește doar reducerea simptomului, fără explorarea cauzelor profunde.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Stadiul genital freudian începe în adolescență și presupune maturizarea sexualității.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Proiecția presupune atribuirea propriilor impulsuri sau sentimente altor persoane.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În abordarea existențială, relația terapeutică autentică este mai importantă decât tehnica rigidă.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Ascultarea reflectivă la Rogers include oferirea de sfaturi directe și soluții prestabilite.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Terapia gestaltistă pune accent pe experiența de aici și acum, nu doar pe explicații abstracte despre trecut.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În behaviorism, termeni precum stimul, răspuns, întărire și modelare sunt centrali.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Terapia realității insistă pe analiza inconștientului ca explicație principală.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Ellis este asociat cu terapia rațional-emotivă, iar Beck cu terapia cognitivă.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În terapia de familie, scopul este culpabilizarea unui membru pentru a elimina simptomul.",
        "tf": True,
        "correct_tf": False,
    },
    # —— Set examen avansat (comparații, aplicare, capcane) ——
    {
        "stem": "Un client spune: „Spune-mi direct ce să fac, tu ești expertul.” Abordarea care se potrivește cel mai puțin cu această așteptare este:",
        "options": [
            "consilierea centrată pe persoană, nondirectivă",
            "terapia rațional-emotivă, cu sarcini și dispută logică",
            "terapia cognitiv-comportamentală, structurată",
            "terapia strategică de familie, cu intervenții planificate",
        ],
        "correct": "a",
    },
    {
        "stem": "O studentă descrie că, după ce a fost criticată de șef, a început să evite colegii și să declare că „toată lumea e ostilă”, deși colegii nu i-au adresat comportamente agresive. Mecanismul de apărare cel mai probabil implicat este:",
        "options": [
            "sublimarea",
            "proiecția",
            "formarea reactivă",
            "intelectualizarea",
        ],
        "correct": "b",
    },
    {
        "stem": "Un pacient relatează motive elaborate și „logice” pentru a nu participa la o reuniune, deși terapeutul observă teamă de respingere. Explicația aparent rațională pentru un motiv mai puțin acceptabil sugerează:",
        "options": [
            "raționalizarea",
            "negarea",
            "regresia",
            "introiecția",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi tehnică–orientare sunt corecte?",
        "options": [
            "asociația liberă — psihodinamic",
            "scaunul gol — terapia gestaltistă",
            "disputa irațională — terapia rațional-emotivă",
            "restructurarea ierarhiei familiale — terapia rațional-emotivă clasică",
        ],
        "correct": "abc",
    },
    {
        "stem": "În psihoterapia psihodinamică, clientul care întârzie sistematic, schimbă subiectul când se apropie de amintiri dureroase sau contestă utilitatea procesului manifestă, cel mai probabil:",
        "options": [
            "rezistență",
            "transfer pozitiv exclusiv",
            "autoactualizare",
            "confluență gestaltică",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapeutul observă că devine neobișnuit de protector cu un client vulnerabil și își amintește de relația cu un frate mai mic. Fenomenul descris este relevant pentru:",
        "options": [
            "contratransfer",
            "introiecție gestaltică",
            "condiționare operantă",
            "homeostazia familială",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații diferențiază corect transferul de contratransfer?",
        "options": [
            "transferul implică reacțiile clientului față de terapeut, influențate de relații anterioare",
            "contratransferul implică reacțiile terapeutului față de client",
            "transferul descrie reacțiile terapeutului față de client",
            "ambele necesită conștientizare profesională în psihodinamic",
        ],
        "correct": "abd",
    },
    {
        "stem": "La Jung, Umbra se referă, în principal, la:",
        "options": [
            "masca socială prezentată public",
            "aspectele respinse, neasumate sau incomplet integrate ale personalității",
            "normele morale interiorizate din copilărie",
            "principiul realității în aparatul psihic freudian",
        ],
        "correct": "b",
    },
    {
        "stem": "Care concepte jungiene sunt asociate corect?",
        "options": [
            "Persona — aspectul social, adaptiv, „masca”",
            "Anima/Animus — reprezentări ale contrasexualității psihice",
            "procesul de individuare — integrare spre Sinele",
            "stilul de viață — compensarea inferiorității în sens adlerian",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care intervenții NU aparțin ascultării reflective rogersiene?",
        "options": [
            "sfaturi directe și moralizare",
            "parafrazarea mesajului clientului",
            "reflectarea tip ecou",
            "interpretarea simbolică impusă a visului",
        ],
        "correct": "ad",
    },
    {
        "stem": "Un client își critică dur propriile reacții, spunând că partea „trebuie” să fie perfectă, iar partea „slabă” trebuie reprimată. În terapia gestaltistă, lucrul cu aceste părți opuse relevă conceptul de:",
        "options": [
            "polarități de personalitate",
            "fixare orală",
            "homeostazie sistemică",
            "scor poligenic",
        ],
        "correct": "a",
    },
    {
        "stem": "Care rezistență la contact gestaltică este descrisă corect în următoarele situații?",
        "options": [
            "preia reguli familiale fără a le asimila — introiecție",
            "atribuie altuia propria furie — proiecție",
            "își critică constant propriul corp — retroflexie",
            "se pierde în opinia grupului fără granițe — confluență",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care distincție este corectă în abordarea comportamentală?",
        "options": [
            "întărirea negativă — creșterea unui comportament prin îndepărtarea unui stimul neplăcut",
            "pedeapsa — consecință care tinde să reducă un comportament",
            "modelarea — învățare prin observare și imitare",
            "asociația liberă — tehnica centrală a lui Skinner",
        ],
        "correct": "abc",
    },
    {
        "stem": "În terapia cognitivă (Aaron T. Beck), gândul „Dacă nu ies perfect, e un dezastru total” ar fi descris mai probabil drept:",
        "options": [
            "distorsiune cognitivă de tip catastrofizare / gândire alb-negru",
            "mecanism de apărare prin sublimare",
            "rezistență la contact gestaltică",
            "manifestare a inconștientului colectiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu corect terapia cognitivă beckiană?",
        "options": [
            "accent pe gânduri automate și scheme cognitive",
            "restructurarea cognitivă urmărește interpretări mai realiste și funcționale",
            "emoțiile sunt influențate de modul de interpretare a evenimentelor",
            "scopul principal este explorarea liberă a asociațiilor fără structură",
        ],
        "correct": "abc",
    },
    {
        "stem": "În terapia rațional-emotivă (Albert Ellis), care dintre următoarele idei ar fi considerată mai irațională?",
        "options": [
            "„Trebuie să fiu aprobat de toți ca să merit ceva”",
            "„Prefer să fiu acceptat, dar pot tolera respingerea”",
            "„E dificil când greșesc, dar nu e catastrofă totală”",
            "„Aș vrea să reușesc, dar pot învăța din eșec”",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia centrată pe realitate (William Glasser), o plângere repetată despre colegi ar fi abordată mai probabil prin întrebări de tipul:",
        "options": [
            "„Ce faci acum și cum te apropie sau te îndepărtează de ceea ce vrei?”",
            "„Ce vise ai avut despre mama ta?”",
            "„Ce arhetip jungian activezi în relație?”",
            "„Ce mecanism de apărare folosești în stadiul anal?”",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații contrastează corect terapia centrată pe realitate cu abordarea psihodinamică clasică?",
        "options": [
            "Glasser pune accent pe comportamentul și alegerile din prezent",
            "psihodinamicul explorează mai ales conflicte inconștiente și trecutul",
            "ambele urmăresc interpretarea viselor ca tehnică principală",
            "terapia realității evită folosirea trecutului ca explicație principală",
        ],
        "correct": "abd",
    },
    {
        "stem": "Un copil dezvoltă simptome când părinții sunt în conflict cronic, iar copilul devine centrul atenției familiale. În terapia de familie, acest scenariu ilustrează mai ales ideea că:",
        "options": [
            "simptomul poate stabiliza sau reorganiza sistemul familial",
            "simptomul dovedește o boală strict individuală, fără context",
            "terapia trebuie să evite orice implicare a părinților",
            "restructurarea cognitivă a copilului, fără restul familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu corect diferențe între psihodinamic și cognitiv-comportamental?",
        "options": [
            "psihodinamic — accent pe inconștient, conflicte, istorie personală",
            "cognitiv-comportamental — accent pe gânduri, comportamente și exerciții structurate",
            "ambele resping în totalitate relația terapeutică",
            "cognitiv-comportamental urmărește frecvent restructurarea cognitivă și schimbare concretă",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care afirmații descriu corect diferențe între consilierea centrată pe persoană (Carl R. Rogers) și terapia gestaltistă?",
        "options": [
            "Rogers pune accent pe acceptare, empatie și facilitare nondirectivă",
            "terapia gestaltistă pune accent pe experiment, conștientizare și contact în prezent",
            "terapia gestaltistă folosește frecvent experimente și intervenții mai active",
            "Rogers folosește în mod obișnuit scaunul gol ca tehnică centrală",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmație surprinde corect diferența dintre stadiul falic și stadiul genital freudian?",
        "options": [
            "stadiul falic este asociat cu complexul Oedip/Electra",
            "stadiul genital presupune maturitate relațională și integrare adultă",
            "stadiul falic coincide cu maturitatea sexuală completă din adolescență",
            "stadiul genital nu înseamnă doar biologie, ci integrare psihosexuală",
        ],
        "correct": "abd",
    },
    {
        "stem": "Introiecția în terapia gestaltistă se deosebește de proiecție deoarece:",
        "options": [
            "introiecția presupune preluare în sine a valorilor sau normelor fără asimilare",
            "proiecția presupune atribuirea altuia a propriilor impulsuri sau trăiri",
            "introiecția presupune atribuirea altuia a propriilor dorințe",
            "ambele sunt tehnici rogersiene de ascultare reflectivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "În terapia psihodinamică, interpretarea precoce și autoritară a visului de către terapeut riscă să:",
        "options": [
            "stimuleze rezistență și să reducă explorarea personală a clientului",
            "garanteze vindecarea rapidă prin sugestie",
            "înlocuiască necesitatea consimțământului informat",
            "elimine transferul din relația terapeutică",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client în terapia cognitiv-comportamentală (CBT) raportează: „Am ratat prezentarea, deci sunt un eșec complet.” Tehnica potrivită în primul rând ar fi:",
        "options": [
            "identificarea și restructurarea distorsiunii cognitive",
            "analiza liberă a asociațiilor din copilărie",
            "interpretarea simbolică obligatorie a visului",
            "lucrul exclusiv cu ierarhia generațională familială",
        ],
        "correct": "a",
    },
    {
        "stem": "Care obiective sunt mai specifice abordării psihanalitice decât unei intervenții simptomatice exclusive?",
        "options": [
            "înțelegerea conflictelor inconștiente",
            "explorarea semnificației simptomului în context personal",
            "restructurarea personalității pe termen lung",
            "eliminarea imediată a simptomului fără explorarea sensului",
        ],
        "correct": "abc",
    },
    {
        "stem": "Negarea, spre deosebire de reprimare, implică mai ales:",
        "options": [
            "refuzul de a accepta o realitate amenințătoare",
            "excluderea din conștiință a unui conținut deja perceput",
            "canalizarea impulsurilor spre activități acceptate social",
            "atribuirea altora a propriilor sentimente",
        ],
        "correct": "a",
    },
    {
        "stem": "Formarea reactivă presupune, de regulă:",
        "options": [
            "manifestarea unui comportament opus celui dorit sau temut",
            "întoarcerea la reacții infantile",
            "copierea normelor altora fără asimilare",
            "evitarea contactului prin glume",
        ],
        "correct": "a",
    },
    {
        "stem": "Un student confundă terapia cognitivă cu cea rațional-emotivă. Care distincție este corectă?",
        "options": [
            "Ellis pune accent pe disputarea convingerilor iraționale și modelul Activator, Beliefs, Consequences (A-B-C)",
            "Beck pune accent pe gânduri automate, scheme și distorsiuni cognitive",
            "ambele resping orice intervenție comportamentală",
            "ambele sunt identice cu analiza transferului freudiană",
        ],
        "correct": "ab",
    },
    {
        "stem": "În terapia de familie, întrebarea „cum este menținută problema în sistem?” este preferabilă întrebării „cine este vinovat?” deoarece:",
        "options": [
            "orientarea spre patternuri relaționale evită culpabilizarea unilaterală",
            "familia funcționează fără reguli sau feedback între membri",
            "simptomul aparține biologiei individului, independent de sistem",
            "comunicarea trebuie redusă pentru a diminua conflictul",
        ],
        "correct": "a",
    },
    {
        "stem": "Sublimarea diferă de refularea simplă deoarece:",
        "options": [
            "canalizează energia spre activități social valoroase",
            "refularea lasă impulsul neatins, fără expresie adaptată",
            "sublimarea presupune atribuirea altora a propriilor impulsuri",
            "ambele presupun refuzul total al realității externe",
        ],
        "correct": "ab",
    },
    {
        "stem": "Reprimarea diferă de negare prin faptul că reprimarea:",
        "options": [
            "exclude din conștiință conținuturi conflictuale deja formate",
            "constă în refuzul de a recunoaște o realitate externă evidentă",
            "presupune întotdeauna comportament opus celui dorit",
            "este o tehnică gestaltică de contact",
        ],
        "correct": "a",
    },
    {
        "stem": "Analiza tranzacțională (AT) aparține orientării umanist-experiențiale, dar se deosebește de Rogers prin faptul că:",
        "options": [
            "folosește concepte precum tranzacții, jocuri psihologice și scene de viață",
            "respinge orice analiză a comunicării dintre părți",
            "este identică cu psihanaliza freudiană clasică",
            "nu are legătură cu relațiile interpersonale",
        ],
        "correct": "a",
    },
    {
        "stem": "Confuzia între terapia de familie psihodinamică și cea structurală se clarifică astfel:",
        "options": [
            "psihodinamică — istorie relațională, conflicte, transfer în familie",
            "structurală — granițe, ierarhie, organizarea subsistemelor",
            "structurală — dispută irațională individuală ca intervenție centrală",
            "psihodinamică — întărire și pedeapsă comportamentală",
        ],
        "correct": "ab",
    },
    {
        "stem": "În psihanaliza freudiană (Sigmund Freud), anxietatea poate fi interpretată ca semnal al conflictului între:",
        "options": [
            "Sine, Eul și Supraeu, când Eul nu mediează suficient",
            "Rogers și Perls în terapia de grup",
            "stadiul genital și inconștientul colectiv",
            "cognițiile automate și schemele beckiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Un terapeut gestaltic observă că un client își strânge pumnii în timp ce spune „nu sunt supărat.” Intervenția orientată spre corp urmărește mai ales:",
        "options": [
            "integrarea experienței emoționale negate în prezent",
            "diagnosticarea unei tulburări psihotice fără evaluare",
            "modificarea ierarhiei familiale",
            "disputarea convingerilor iraționale ellisiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Stadiul de latență freudian nu înseamnă absența dezvoltării, ci mai ales:",
        "options": [
            "diminuarea relativă a investirii libidinale și orientare spre activități sociale și școlare",
            "apariția complexului Oedip",
            "matuizarea relațiilor intime adulte",
            "fixarea obligatorie pe controlul sfincterian",
        ],
        "correct": "a",
    },
    {
        "stem": "Care mecanism de apărare este ilustrat de o persoană care devine excesiv de grijulie cu alții după ce resimte vinovăție pentru propriile impulsuri egoiste?",
        "options": [
            "formarea reactivă",
            "proiecția",
            "sublimarea",
            "regresia",
        ],
        "correct": "a",
    },
    {
        "stem": "Abordarea comportamentală ar explica menținerea unui comportament de evitare prin:",
        "options": [
            "reducerea imediată a anxietății, ceea ce întărește evitarea",
            "complexul Oedip nerezolvat",
            "inconștientul colectiv",
            "clarificarea sensului existențial",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia de familie, alianțele și coaliziile pot menține problema deoarece:",
        "options": [
            "reorganizează puterea și comunicarea într-un mod care stabilizează simptomul",
            "dovedesc că familia nu are reguli",
            "elimină nevoia de limite între generații",
            "sunt irelevante pentru abordarea sistemică",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia gestaltistă (Fritz Perls), formularea „eu mă enervez” în loc de „se enervează lucrurile” este preferată pentru a contracara:",
        "options": [
            "deflecția și pierderea responsabilității pentru experiență",
            "sublimarea artistică",
            "transferul pozitiv",
            "condiționarea clasică",
        ],
        "correct": "a",
    },
    {
        "stem": "Psihanaliza clasică se deosebește de terapia cognitiv-comportamentală (CBT) prin durata și accentul pus pe:",
        "options": [
            "explorarea profundă a inconștientului și a istoriei personale",
            "exerciții structurate pe gânduri și comportamente prezente",
            "acceptarea necondiționată ca singură tehnică",
            "restructurarea granițelor familiale ca unic obiectiv",
        ],
        "correct": "ab",
    },
    {
        "stem": "În abordarea umanist-experiențială, autenticitatea clientului este încurajată, nu perfecțiunea socială.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În terapia cognitiv-comportamentală (CBT), schimbarea cognitivă poate preceda schimbarea emoțională și comportamentală.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Transferul și contratransferul sunt concepte folosite în principal în abordarea psihodinamică.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În terapia gestaltistă, retroflexia presupune îndreptarea energiei împotriva propriei persoane.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Terapia de familie sistemică presupune că modificarea unui element poate influența întregul sistem.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Ellis și Beck folosesc exact aceeași metodă, fără diferențe teoretice semnificative.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Glasser consideră că explicațiile din trecut sunt suficiente pentru schimbarea comportamentului prezent.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "În terapia rațional-emotivă (REBT), disputa cognitivă poate viza convingerile absolute de tip „trebuie”.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Set diversificat II (teme puțin acoperite) ——
    {
        "stem": "Karen Horney descrie trei tendințe nevrotice fundamentale de adaptare la anxietatea bazală. Care sunt corecte?",
        "options": [
            "tendința de a merge spre oameni — nevoie de apropiere și aprobare",
            "tendința de a merge împotriva oamenilor — nevoie de putere și control",
            "tendința de a merge departe de oameni — nevoie de independență și distanță",
            "tendința de a elimina complet orice conflict intern prin sublimare obligatorie",
        ],
        "correct": "abc",
    },
    {
        "stem": "La Horney, diferența dintre sinele real și sinele idealizat devine problematică atunci când:",
        "options": [
            "imaginea idealizată este rigidă și îndepărtată de experiența reală",
            "clientul acceptă imperfecțiunea umană ca normală",
            "terapeutul oferă empatie autentică",
            "anxietatea bazală dispare complet în relații sigure",
        ],
        "correct": "a",
    },
    {
        "stem": "În psihologia individuală (Alfred Adler), un adolescent care spune „Trebuie să fiu primul la orice, altfel nu contez” ar fi interpretat mai probabil prin:",
        "options": [
            "compensarea sentimentului de inferioritate și stil de viață orientat spre superioritate",
            "fixarea orală freudiană",
            "jocul psihologic „Da, dar” din analiza tranzacțională (AT)",
            "triada cognitivă beckiană",
        ],
        "correct": "a",
    },
    {
        "stem": "La Jung, un complex este:",
        "options": [
            "un grup de imagini și afecte organizate în jurul unui nucleu emoțional",
            "identic cu arhetipul Marelui Mamă în toate cazurile",
            "un mecanism de apărare freudian standard",
            "o tehnică gestaltică de polaritate",
        ],
        "correct": "a",
    },
    {
        "stem": "Imaginația activă, în abordarea jungiană, presupune:",
        "options": [
            "dialog conștient cu imagini sau figuri din inconștient",
            "asociație liberă fără nicio structură",
            "expunere graduală la stimuli fobici",
            "disputa convingerilor iraționale ellisiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client relatează visul la suprafață (conținut manifest), iar terapeutul psihodinamic explorează semnificațiile ascunse. Aceasta vizează distincția dintre:",
        "options": [
            "conținut manifest și conținut latent",
            "transfer și contratransfer",
            "figură și fond gestaltic",
            "tranzacție complementară și încrucișată",
        ],
        "correct": "a",
    },
    {
        "stem": "„Lucrul de trecere” (working through) în psihanaliză presupune:",
        "options": [
            "repetarea explorării conflictelor în relația terapeutică, nu o singură interpretare",
            "eliminarea imediată a simptomului prin sugestie",
            "evitarea oricărei reinterpretări a materialului",
            "înlocuirea relației terapeutice cu exerciții de relaxare",
        ],
        "correct": "a",
    },
    {
        "stem": "În perspectivă existențială, vinovăția autentică se deosebește de cea nevrotică prin faptul că prima:",
        "options": [
            "reflectă conștientizarea alegerilor proprii și a responsabilității",
            "este mereu patologică și trebuie eliminată prin raționalizare",
            "apare doar în stadiul anal freudian",
            "se rezolvă exclusiv prin întărire negativă",
        ],
        "correct": "a",
    },
    {
        "stem": "Acceptarea necondiționată pozitivă la Rogers înseamnă:",
        "options": [
            "respect pentru persoană ca întreg, nu aprobarea tuturor comportamentelor",
            "acordul cu orice comportament dăunător",
            "lipsa oricărei reacții autentice din partea terapeutului",
            "impunerea valorilor terapeutului",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia gestaltistă, dialogul între „câinele de sus” (top dog) și „câinele de jos” (underdog) urmărește:",
        "options": [
            "integrarea părților interne critice și reprimate",
            "interpretarea simbolică obligatorie a visului",
            "modificarea ierarhiei generaționale",
            "disputa convingerilor iraționale ellisiene",
        ],
        "correct": "a",
    },
    {
        "stem": "„Afaceri neterminate” (unfinished business) în terapia gestaltistă se referă la:",
        "options": [
            "emoții sau nevoi rămase neexprimate sau neintegrate din relații anterioare",
            "teme de licență neterminate",
            "exerciții de relaxare incomplete",
            "planuri de tratament fără obiective",
        ],
        "correct": "a",
    },
    {
        "stem": "În analiza tranzacțională (AT), stările ego Parent (Părinte), Adult și Copil (Copil) descriu:",
        "options": [
            "moduri de funcționare psihică cu conținut, gândire și comportament specifice",
            "vârsta cronologică reală a clientului",
            "rolurile obligatorii în terapia de familie structurală",
            "stadiile psihosexuale freudiene",
        ],
        "correct": "a",
    },
    {
        "stem": "O tranzacție încrucișată (crossed transaction) apare când:",
        "options": [
            "răspunsul nu corespunde stimulului la nivelul stării ego adresate",
            "ambele părți comunică din Adult",
            "comunicarea este complementară și fluidă",
            "terapeutul folosește exclusiv ascultarea reflectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "În analiza tranzacțională (AT), jocul psihologic „Da, dar...” se caracterizează prin:",
        "options": [
            "clientul respinge soluțiile oferite, menținând poziția de neajutorat",
            "clientul acceptă imediat orice sugestie",
            "terapeutul oferă directive autoritare",
            "familia restructurează granițele rigid",
        ],
        "correct": "a",
    },
    {
        "stem": "„Scenariul de viață” (life script) în analiza tranzacțională (AT) se referă la:",
        "options": [
            "planul narativ timpuriu despre cum va fi viața, adesea în afara conștientizării",
            "protocolul scris al ședințelor de terapie",
            "ierarhia de expunere în fobii",
            "genograma structurală a familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "Flooding-ul (inundarea) se deosebește de desensibilizarea sistematică prin faptul că:",
        "options": [
            "expune clientul rapid și intens la stimulul fobic, fără ierarhie graduală",
            "folosește relaxarea progresivă ca element central obligatoriu",
            "interpretă visul în sens jungian",
            "lucrează exclusiv cu granițe familiale difuze",
        ],
        "correct": "a",
    },
    {
        "stem": "Triada cognitivă a depresiei, la Beck, include visionarea negativă despre:",
        "options": [
            "sine, lume și viitor",
            "Sine, Eul și Supraeu",
            "Parent, Adult și Copil",
            "figură, fond și contact",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client spune: „Sunt incompetent” (credință de sine) versus „Am eșuat la acest proiect” (gând automat). Distincția ilustrează diferența dintre:",
        "options": [
            "credință de bază / schemă și gând automat situațional",
            "transfer și contratransfer",
            "introiecție și proiecție gestaltică",
            "homeostazie și cauzalitate circulară",
        ],
        "correct": "a",
    },
    {
        "stem": "Activarea comportamentală, în terapia cognitiv-comportamentală (CBT) pentru depresie, urmărește mai ales:",
        "options": [
            "reintroducerea graduală a activităților plăcute sau cu sens, pentru a întrerupe cicul inactivității",
            "interpretarea simbolică a viselor din copilărie",
            "restructurarea granițelor familiale difuze",
            "disputa irațională a convingerilor ellisiene exclusiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Empirismul colaborativ, în terapia beckiană, presupune că:",
        "options": [
            "terapeutul și clientul testează împreună validitatea cognițiilor ca ipoteze",
            "terapeutul deține adevărul și îl transmite autoritar",
            "clientul nu participă la stabilirea obiectivelor",
            "emotiile sunt ignorate în favoarea logicii pure",
        ],
        "correct": "a",
    },
    {
        "stem": "Întrebările socratice în terapia cognitiv-comportamentală (CBT) au rolul de a:",
        "options": [
            "ghida clientul să examineze dovezi pro și contra unei cogniții",
            "impune interpretarea transferului",
            "evita orice exercițiu comportamental",
            "înlocui consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "Ellis distinge între preferințe („aș prefera să fiu acceptat”) și cerințe absolute („trebuie să fiu acceptat”). Problema apare când:",
        "options": [
            "preferințele devin cerințe rigide și globale",
            "clientul are preferințe flexibile",
            "terapeutul folosește empatie rogersiană",
            "clientul acceptă eșecul ca posibil",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia multimodală, modelul Behavior, Affect, Sensation, Imagery, Cognition, Interpersonal, Drugs/biology (BASIC ID) include dimensiuni precum:",
        "options": [
            "Behavior (comportament), Affect (afect), Sensation (senzație)",
            "Imagery (imagistică), Cognition (cogniție), Interpersonal (interpersonal)",
            "Drugs/biology (biologic) — în sens larg, funcționarea somatică",
            "Dreams freudiene ca singura dimensiune evaluată",
        ],
        "correct": "abc",
    },
    {
        "stem": "Modelul Wants, Doing, Evaluation, Planning (WDEP) la Glasser include:",
        "options": [
            "Wants (ce vrea), Direction and Doing (direcție și acțiune)",
            "Evaluation (evaluare), Planning (planificare)",
            "Working through (lucrul de trecere freudian)",
            "Withdrawal (retragere) ca scop terapeutic principal",
        ],
        "correct": "ab",
    },
    {
        "stem": "„Lumea calității” (quality world) la Glasser descrie:",
        "options": [
            "imaginile interioare ale a ceea ce clientul își dorește și ce îi aduce satisfacție",
            "normele morale freudiene ale Supraeului",
            "arhetipurile jungiene obligatorii",
            "regulile implicite ale sistemului familial",
        ],
        "correct": "a",
    },
    {
        "stem": "Într-o familie, mama și tatăl sunt în conflict, iar copilul devine mesager între ei. Acest pattern este numit, în terapia de familie:",
        "options": [
            "triangulare",
            "sublimare",
            "condiționare clasică",
            "individuare jungiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Enmeshment (împletirea excesivă) în abordarea structurală se caracterizează prin:",
        "options": [
            "granițe difuze și suprareacție la distanțare",
            "granițe rigide și comunicare minimă",
            "ierarhie clară și autonomie optimă",
            "absența oricărei emoții în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Disengagement (dezangajare) familială, în sens structural, presupune:",
        "options": [
            "granițe rigide, puțin sprijin emoțional și comunicare redusă",
            "granițe difuze și dependență emoțională excesivă",
            "triangulare obligatorie cu copilul",
            "interpretarea visului ca unică tehnică",
        ],
        "correct": "a",
    },
    {
        "stem": "Diferențierea de sine (Bowen) în terapia de familie vizează:",
        "options": [
            "capacitatea de a rămâne calm și autonom în relații emoțional intense",
            "identificarea unui membru vinovat pentru simptom",
            "eliminarea tuturor conflictelor familiale",
            "prescrierea simptomului ca tehnică beckiană",
        ],
        "correct": "a",
    },
    {
        "stem": "Schimbarea de ordinul I (first-order) în terapia de familie presupune:",
        "options": [
            "modificarea comportamentelor sau simptomelor fără schimbarea regulilor sistemului",
            "schimbarea regulilor și patternurilor care mențin problema",
            "interpretarea inconștientului colectiv",
            "disputa convingerilor iraționale",
        ],
        "correct": "a",
    },
    {
        "stem": "Schimbarea de ordinul II (second-order) în abordarea sistemică presupune:",
        "options": [
            "modificarea regulilor, credințelor sau patternurilor care organizează sistemul",
            "reducerea simptomului fără alterarea interacțiunilor familiale",
            "evitarea intervenției asupra comunicării dintre membri",
            "lucrul individual, fără implicarea familiei",
        ],
        "correct": "a",
    },
    {
        "stem": "„Pacientul identificat” (IP) în terapia de familie nu înseamnă neapărat că:",
        "options": [
            "el este singura cauză sau singurul responsabil al problemei familiale",
            "el poartă simptomul vizibil al unei dificultăți sistemice",
            "familia se concentrează adesea pe el ca purtător al problemei",
            "intervenția poate necesita implicarea întregului sistem",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea strategică (ex. Haley), prescrierea simptomului urmărește, în anumite cazuri:",
        "options": [
            "să schimbe regulile jocului relațional care mențin simptomul",
            "să amplifice permanent suferința clientului",
            "să evite orice implicare a familiei",
            "să înlocuiască consimțământul informat",
        ],
        "correct": "a",
    },
    {
        "stem": "Intelectualizarea, ca mecanism de apărare, este ilustrată mai probabil de:",
        "options": [
            "un client care vorbește detaliat și abstract despre durere, fără a o trăi emoțional",
            "un client care refuză să recunoască un diagnostic medical evident",
            "un client care lovește obiecte când este frustrat",
            "un client care devine excesiv de amabil după gânduri agresive",
        ],
        "correct": "a",
    },
    {
        "stem": "Deplasarea (displacement), ca mecanism de apărare, presupune:",
        "options": [
            "redirecționarea impulsului de la o țintă amenințătoare spre una mai sigură",
            "atribuirea altora a propriilor dorințe",
            "canalizarea impulsului spre activități social valoroase",
            "refuzul de a percepe realitatea externă",
        ],
        "correct": "a",
    },
    {
        "stem": "Care abordări sunt orientate mai mult spre insight decât spre acțiune imediată?",
        "options": [
            "psihodinamică / psihanalitică",
            "existențială (în sensul înțelegerii modului de a trăi)",
            "terapia rațional-emotivă cu sarcini comportamentale",
            "desensibilizarea sistematică",
        ],
        "correct": "ab",
    },
    {
        "stem": "Un terapeut beckian propune clientului să noteze gândurile automate și să testeze o predicție în viața reală. Combinația ilustrează:",
        "options": [
            "monitorizarea cognitivă și experiment comportamental",
            "asociația liberă și interpretarea visului",
            "scaunul gol și polarități gestaltice",
            "triangulare și homeostazie",
        ],
        "correct": "a",
    },
    {
        "stem": "În consilierea existențială, tema singurătății poate fi abordată ca:",
        "options": [
            "experiență fundamentală a condiției umane, nu doar deficit social",
            "semn că clientul are fixare orală",
            "dovadă că terapia de familie e inutilă",
            "rezultat al unei distorsiuni beckiene obligatorii",
        ],
        "correct": "a",
    },
    {
        "stem": "În terapia gestaltistă, „rămânerea cu figura” (staying with the figure) presupune:",
        "options": [
            "susținerea conștientizării unei experiențe emergente, fără a o evita",
            "schimbarea rapidă a subiectului când apare emoția",
            "interpretarea autoritară a visului",
            "prescrierea simptomului în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia rațional-emotivă folosește frecvent disputa cognitivă, în timp ce terapia beckiană folosește mai des:",
        "options": [
            "întrebări socratice și restructurare a distorsiunilor",
            "asociația liberă și analiza visului",
            "scaunul gol gestaltic",
            "restructurarea ierarhiei generaționale",
        ],
        "correct": "a",
    },
    {
        "stem": "În analiza tranzacțională (AT), un „hook” (cârlig) în jocurile psihologice este:",
        "options": [
            "punctul vulnerabil al unei persoane, folosit pentru a o atrage în joc",
            "tehnica gestaltică a scaunului gol",
            "ierarhia de expunere în fobii",
            "interpretarea visului latent",
        ],
        "correct": "a",
    },
    {
        "stem": "La Beck, distorsiunea „citirea gândurilor” este ilustrată de:",
        "options": [
            "„Știu sigur că colegii mă consideră incompetent, deși nu am verificat”",
            "„Prefer să reușesc, dar pot învăța din eșec”",
            "„Mă simt trist și vreau să înțeleg de ce”",
            "„Vreau să schimb comportamentul meu de evitare”",
        ],
        "correct": "a",
    },
    {
        "stem": "În abordarea umanist-experiențială, valoarea experienței trăite depășește uneori explicația intelectuală abstractă.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În analiza tranzacțională (AT), o tranzacție complementară menține comunicarea fluidă, pe când una încrucișată o perturbă.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Enmeshment (împletirea excesivă) și Disengagement (dezangajarea) descriu tipuri diferite de probleme ale granițelor familiale.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Schimbarea de ordinul II (second-order) modifică regulile sistemului, nu doar simptomul izolat.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Triada cognitivă beckiană include visionarea pozitivă despre sine, lume și viitor.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Modelul Wants, Doing, Evaluation, Planning (WDEP) aparține terapiei centrate pe realitate (Glasser).",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Extincția în condiționarea operantă crește un comportament prin întărire continuă.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "La Rogers, locusul de evaluare intern indică orientarea spre propriile valori și experiență, nu spre aprobarea exclusivă a altora.",
        "tf": True,
        "correct_tf": True,
    },
]

from scripts.psihoterapie_ii_tricky_items import TRICKY_ITEMS
from scripts.psihoterapie_ii_psihodinamic_items import PSIHODINAMIC_ITEMS
from scripts.psihoterapie_ii_aparare_items import APARARE_ITEMS
from scripts.psihoterapie_ii_behaviorism_items import BEHAVIORISM_ITEMS
from scripts.psihoterapie_ii_behavioral_techniques_items import BEHAVIORAL_TECHNIQUES_ITEMS
from scripts.psihoterapie_ii_cbt_ellis_beck_items import CBT_ELLIS_BECK_ITEMS
from scripts.psihoterapie_ii_lazarus_multimodal_items import LAZARUS_MULTIMODAL_ITEMS
from scripts.psihoterapie_ii_glasser_reality_items import GLASSER_REALITY_ITEMS
from scripts.psihoterapie_ii_family_therapy_items import FAMILY_THERAPY_ITEMS
from scripts.psihoterapie_ii_psychodrama_items import PSYCHODRAMA_ITEMS
from scripts.psihoterapie_ii_psychodrama_extra_items import PSYCHODRAMA_EXTRA_ITEMS
from scripts.psihoterapie_ii_mitrofan_unificare_items import MITROFAN_UNIFICARE_ITEMS

ITEMS.extend(TRICKY_ITEMS)
ITEMS.extend(PSIHODINAMIC_ITEMS)
ITEMS.extend(APARARE_ITEMS)
ITEMS.extend(BEHAVIORISM_ITEMS)
ITEMS.extend(BEHAVIORAL_TECHNIQUES_ITEMS)
ITEMS.extend(CBT_ELLIS_BECK_ITEMS)
ITEMS.extend(LAZARUS_MULTIMODAL_ITEMS)
ITEMS.extend(GLASSER_REALITY_ITEMS)
ITEMS.extend(FAMILY_THERAPY_ITEMS)
ITEMS.extend(PSYCHODRAMA_ITEMS)
ITEMS.extend(PSYCHODRAMA_EXTRA_ITEMS)
ITEMS.extend(MITROFAN_UNIFICARE_ITEMS)
