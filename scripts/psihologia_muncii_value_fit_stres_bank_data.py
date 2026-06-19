"""Itemi — Value Fit și stres, lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

VALUE_FIT_STRES_ITEMS: List[Item] = [
    # —— Value Fit: definiție, consecințe (1–8) ——
    {
        "stem": (
            "Potrivirea valorilor (Value Fit) descrie alinierea dintre valorile "
            "personale ale angajatului și valorile promovate de organizație — "
            "cu efecte tipice asupra satisfacției, angajamentului, performanței "
            "și turnover-ului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre potrivirea valorilor (Value Fit) este cea "
            "mai precisă?"
        ),
        "options": [
            "valorile individului se aliniază cu valorile organizației",
            "potrivire bună → satisfacție și angajament mai ridicate",
            "potrivire bună → turnover mai scăzut, performanță mai bună",
            "value fit înseamnă același lucru cu potrivirea abilităților "
            "tehnice la job",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Valorile, în sens organizațional, sunt convingeri despre ce este "
            "important — nu sunt aptitudini cognitive, trăsături de personalitate "
            "sau stări emoționale momentane."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care distincții sunt corecte între valori și alte constructe?"
        ),
        "options": [
            "valorile = ce consider important (ex. autonomie, echitate)",
            "abilitățile = ce pot face cognitiv sau motor",
            "trăsăturile = tendințe relativ stabile de comportament",
            "emoțiile = stări afective trecătoare, nu sisteme de convingeri",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un angajat apreciază transparența și colaborarea, dar firma "
            "promovează competiția internă ascunsă și secretul. Problema "
            "principală este:"
        ),
        "options": [
            "potrivire slabă a valorilor (Value Fit scăzut)",
            "lipsă de abilități tehnice — alt construct",
            "risc de insatisfacție și angajament scăzut pe termen lung",
            "groupthink — nu e cazul direct din exemplu",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Care afirmație despre valori este falsă?"
        ),
        "options": [
            "valorile sunt identice cu trăsăturile de personalitate Big Five",
            "valorile ghidează ce considerăm demn de urmat la muncă",
            "value fit ridicat poate susține performanța",
            "valorile organizației pot fi învățate prin socializare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce contează potrivirea valorilor dincolo de salariu sau "
            "beneficii?"
        ),
        "options": [
            "valorile definesc sensul și etica percepută a muncii",
            "mismatch valoric poate genera disonanță cognitivă și burnout",
            "salariul anulează complet orice conflict de valori",
            "angajamentul afectiv e mai ușor de susținut când valorile coincid",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre potrivirea valorilor (Value Fit) este "
            "exagerată (deci greșită)?"
        ),
        "options": [
            "value fit se măsoară exclusiv prin teste de aptitudine "
            "profesională",
            "alinierea valorilor poate influența satisfacția la muncă",
            "mismatch valoric poate crește intenția de plecare",
            "valorile țin de ce considerăm important, nu de IQ",
        ],
        "correct": "a",
    },
    # —— Schwartz, socializare, aculturație, shared values (9–20) ——
    {
        "stem": (
            "În modelul lui Shalom Schwartz, care perechi sunt valori din "
            "cele zece tipuri fundamentale?"
        ),
        "options": [
            "autodirecționare (Autodirecționare) și universalism (Universalism)",
            "putere (Putere) și realizare (Realizare)",
            "bunăvoință (Bunăvoință) și conformitate (Conformitate)",
            "extraversiune (Extraversiune) și neuroticism (Neuroticism)",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care valori din modelul Schwartz aparțin tipului hedonism "
            "(Hedonism) sau stimulare (Stimulare)?"
        ),
        "options": [
            "plăcere și satisfacere imediată",
            "noutate, provocare, varietate",
            "respect pentru obiceiuri și credințe consacrate",
            "siguranță, stabilitate, ordine",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care valori Schwartz sunt asociate tipic cu orientarea spre "
            "siguranță și ordine socială?"
        ),
        "options": [
            "securitate (Securitate)",
            "conformitate (Conformitate)",
            "tradiție (Tradiție)",
            "autodirecționare (Autodirecționare) — independență creativă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce rol are socializarea organizațională în raport cu valorile?"
        ),
        "options": [
            "ajută angajații noi să învețe normele și cultura firmei",
            "poate crește potrivirea valorilor (Value Fit)",
            "înlocuiește complet valorile personale — nu e corect",
            "include onboarding, mentorat și modele de rol",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații despre socializarea organizațională sunt corecte?"
        ),
        "options": [
            "ajută la învățarea „modului nostru de a face lucrurile”",
            "poate crește alinierea cu valorile firmei",
            "înlocuiește complet valorile personale aduse de angajat",
            "include mentorat, onboarding și modele de rol",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Aculturația organizațională se referie la:"
        ),
        "options": [
            "adaptarea la o cultură organizațională diferită de cea cunoscută",
            "păstrarea parțială a valorilor proprii, fără abandon total",
            "renunțarea obligatorie la toate valorile personale la angajare",
            "proces asemănător adaptării culturale, dar la nivel de firmă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un specialist român intră într-o multinațională cu cultură "
            "puternic orientată spre ierarhie. El își păstrează valoarea "
            "autonomiei, dar învață protocoalele locale. Acest proces seamănă "
            "cel mai mult cu:"
        ),
        "options": [
            "adaptare la cultura nouă fără abandon total al valorilor proprii",
            "învățarea normelor și culturii firmei",
            "presiune de conformitate necritică",
            "fluctuație repetată de la un job la altul",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Valorile comune (Shared Values) în echipă pot susține cooperarea "
            "și coeziunea, dar riscul asociat este:"
        ),
        "options": [
            "groupthink — gândire de grup necritică, evitarea dissensului",
            "pierderea diversității de perspective utile",
            "performanță garantată indiferent de realitate",
            "turnover funcțional automat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care scenariu ilustrează cel mai bine riscul groupthink?"
        ),
        "options": [
            "echipa evită să conteste o decizie riscantă pentru că „suntem "
            "toți de acord”",
            "valorile comune reduc conflictele inutile — benefic dacă rămâne "
            "gândire critică",
            "un membru nou aduce o perspectivă diferită și e ascultat",
            "consensul se obține prin presiune socială, nu prin analiză",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Care valori Schwartz sunt orientate spre transcenderea interesului "
            "propriu (ex. protejarea mediului, egalitate)?"
        ),
        "options": [
            "universalism (Universalism)",
            "bunăvoință (Bunăvoință)",
            "putere (Putere)",
            "realizare (Realizare)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre socializare și aculturație este falsă?"
        ),
        "options": [
            "socializarea obligă la abandon total al valorilor personale",
            "aculturația presupune adaptare parțială, nu renunțare completă",
            "ambele pot influența integrarea în cultura organizațională",
            "socializarea ajută la învățarea normelor firmei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Asociază corect conceptul cu descrierea:"
        ),
        "options": [
            "aliniere între valorile personale și cele ale organizației",
            "învățarea culturii și normelor firmei",
            "adaptare la o cultură nouă, păstrând parțial valorile proprii",
            "valori comune ce pot crește coeziunea, dar și groupthink",
        ],
        "correct": "abcd",
    },
    # —— Stres: definiție, Selye, P–E Fit (21–32) ——
    {
        "stem": (
            "În psihologia muncii, stresul se definește cel mai bine ca o "
            "reacție care apare când cerințele percepute depășesc resursele "
            "disponibile — nu ca evenimentul obiectiv în sine."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care definiție surprinde cel mai bine stresul la locul de muncă?"
        ),
        "options": [
            "reacție la dezechilibrul cerințe > resurse",
            "depinde de evaluarea subiectivă, nu doar de eveniment",
            "orice sarcină dificilă produce automat stres identic la toți",
            "include componentă fiziologică și psihologică",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "În sindromul general de adaptare (GAS) al lui Hans Selye, "
            "ordinea etapelor este:"
        ),
        "options": [
            "alarmă → rezistență → epuizare",
            "rezistență → alarmă → epuizare",
            "epuizare → alarmă → rezistență",
            "alarmă → epuizare imediată, fără rezistență",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care etape ale sindromului general de adaptare (GAS) sunt "
            "descrise corect?"
        ),
        "options": [
            "reacție inițială la agentul stresor",
            "organismul se adaptează temporar",
            "resurse epuizate dacă stresul persistă",
            "absența totală a oricărei reacții fiziologice",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Modelul potrivirii persoană–mediu (Person–Environment Fit) "
            "explică stresul prin:"
        ),
        "options": [
            "nepotrivire între caracteristicile persoanei și mediul de muncă",
            "mismatch la cerințe, valori, abilități sau preferințe",
            "stres zero când mediul e oricât de solicitant",
            "ideea că stresul crește când mediul nu „încape” cu persoana",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un introvertit preferă lucrul structurat și liniștit, dar primește "
            "rol de vânzări agresiv, cu target zilnic și open-space zgomotos. "
            "Ce cadru explică cel mai bine stresul?"
        ),
        "options": [
            "potrivire persoană–mediu (P–E Fit) slabă",
            "cerințe > resurse percepute",
            "value fit perfect — nu e cazul",
            "type B garantat — personalitatea nu e definită aici",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre stres este o capcană de examen (greșită)?"
        ),
        "options": [
            "stresul este identic cu evenimentul stresor — toți reacționează "
            "la fel",
            "stresul depinde de percepția cerințe vs resurse",
            "aceeași sarcină obiectivă poate stresa diferit două persoane",
            "stresul include reacții psihologice și fiziologice",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce etapa de epuizare din GAS (Selye) este periculoasă la "
            "stres cronic la muncă?"
        ),
        "options": [
            "resursele de adaptare se epuizează pe termen lung",
            "poate apărea burnout sau probleme de sănătate",
            "după epuizare, organismul devine automat mai rezistent",
            "legătura cu absențe, erori și performanță scăzută",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care perechi descriu corect relația cerințe–resurse în stres?"
        ),
        "options": [
            "cerințe mari + resurse mici → stres ridicat",
            "resursele includ sprijin social, control, competențe",
            "cerințele sunt doar evenimente externe, fără interpretare",
            "aceeași cerință obiectivă poate stresa diferit după resurse",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "În GAS, faza de rezistență înseamnă că organismul se adaptează "
            "temporar — dar dacă stresorul continuă, urmează epuizarea."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmații leagă corect value fit și stres?"
        ),
        "options": [
            "value fit scăzut poate fi o sursă de stres psihologic",
            "P–E Fit include și potrivirea valorilor cu cultura organizației",
            "value fit ridicat elimină orice stres legat de volumul de muncă",
            "conflict de valori poate epuiza resursele emoționale",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un angajat trece prin alarmă (reorganizare), apoi se adaptează "
            "parțial (rezistență), iar după luni de incertitudine cedează "
            "(epuizare). Care model descrie acest arc?"
        ),
        "options": [
            "sindromul general de adaptare (GAS) — Selye",
            "modelul cerere–control — Karasek",
            "evaluare cognitivă — Lazarus",
            "zece valori — Schwartz",
        ],
        "correct": "a",
    },
    # —— Karasek, Lazarus, coping (33–44) ——
    {
        "stem": (
            "În modelul cerere–control (Demand–Control) al lui Robert Karasek, "
            "stresul maxim apare când:"
        ),
        "options": [
            "cerințele psihologice sunt mari",
            "controlul/autonomia asupra muncii este redus",
            "cerințele sunt mici și controlul mare — job pasiv",
            "cerințele sunt mari și controlul mare — job activ, potențial "
            "optim",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care tip de job descrie modelul Karasek cu cerințe mari + control "
            "mare (activ)?"
        ),
        "options": [
            "muncă solicitantă, dar cu autonomie în modul de lucru",
            "poate fi stimulatoare, nu neapărat maxim stresantă",
            "muncă cu cerințe mici și control mic — pasivă",
            "muncă cu cerințe mari și control mic — cea mai stresantă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În teoria copingului a lui Richard Lazarus, evaluarea primară "
            "răspunde la întrebarea:"
        ),
        "options": [
            "„Este situația amenințătoare sau benefică pentru mine?”",
            "„Am resursele să fac față?” — evaluare secundară",
            "„Ce emoție simt?” — consecință, nu evaluarea primară",
            "„Cine e de vină?” — atribuire, alt pas",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care este ordinea logică în modelul evaluării cognitive Lazarus?"
        ),
        "options": [
            "situația este periculoasă sau benefică?",
            "am resursele necesare pentru a face față?",
            "alegerea strategiei de coping",
            "evaluare secundară înainte de a percepe evenimentul",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Copingul centrat pe problemă înseamnă încercarea de a schimba "
            "situția stresantă; copingul centrat pe emoție înseamnă reglarea "
            "reacției emoționale când situația nu poate fi schimbată ușor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care exemple ilustrează coping centrat pe problemă vs centrat pe "
            "emoție?"
        ),
        "options": [
            "negocierea unui deadline realist",
            "meditație sau respiro pentru calm după conflict",
            "reorganizarea priorităților pentru a reduce volumul de muncă",
            "negarea completă a situației fără nicio strategie",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "După ce evaluează o prezentare ca amenințătoare (evaluare "
            "primară) și crede că exersarea îl poate ajuta (evaluare "
            "secundară), angajatul repetă prezentarea — exemplu de:"
        ),
        "options": [
            "coping centrat pe problemă",
            "evaluare secundară urmată de acțiune",
            "coping centrat pe emoție — doar relaxare fără pregătire",
            "groupthink",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre modelul Karasek este falsă?"
        ),
        "options": [
            "orice job cu cerințe mari este automat maxim stresant, indiferent "
            "de control",
            "joburile pasive au cerințe mici și control mic",
            "autonomia poate atenua efectul cerințelor mari",
            "modelul pune accent pe structura rolului, nu doar pe evenimente",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "După evaluarea secundară Lazarus, dacă resursele par insuficiente, "
            "ce strategii sunt plauzibile?"
        ),
        "options": [
            "coping centrat pe emoție — reducerea anxietății",
            "coping centrat pe problemă — căutare de sprijin sau replanificare",
            "evaluare primară repetată fără acțiune — pasivitate",
            "ignorarea totală — uneori apare, dar nu e strategie adaptivă "
            "ideală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul Karasek, care combinație descrie jobul cel mai "
            "stresant?"
        ),
        "options": [
            "cerințe psihologice mari + control/autonomie redus",
            "cerințe mari + control mare — job activ, nu neapărat maxim "
            "stresant",
            "cerințe mici + control mic — job pasiv",
            "ritm impus strict fără autonomie — exemplu clasic",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Care modele sunt asociate corect cu autorul sau ideea centrală?"
        ),
        "options": [
            "model cerere–control al structurii jobului",
            "evaluare cognitivă și strategii de coping",
            "sindrom general de adaptare la stres",
            "zece valori fundamentale umane",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Evaluarea primară Lazarus întreabă „pot face față?”, iar "
            "evaluarea secundară „e periculos?”."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Type A/B, challenge/hindrance, sinteză (45–60) ——
    {
        "stem": (
            "Care descrieri se potrivesc pattern-ului Tip A (Type A) și Tip B?"
        ),
        "options": [
            "Tip A: competitiv, grăbit, ostil — stres și risc cardiovascular",
            "Tip B: mai relaxat, mai puțin orientat spre competiție intensă",
            "Tip A: lipsă totală de ambiție și ritm foarte lent",
            "Tip B: identic cu Factorul Conștiinciozitate din Big Five",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trăsături descriu mai bine pattern-ul Tip A (Type A)?"
        ),
        "options": [
            "competitivitate și grabă",
            "ostilitate / impaciență",
            "asociere cu stres cronic și risc cardiovascular",
            "lipsă totală de ambiție și ritm lent — Tip B, nu Tip A",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Stresorii provocare (Challenge stressors) vs stresori obstacol "
            "(Hindrance stressors) — care perechi sunt corecte?"
        ),
        "options": [
            "oportunitate, dezvoltare, responsabilitate nouă",
            "birocrație, ambiguitate de rol, obstacole frustrante",
            "proiecte care pot crește competențele",
            "sarcini care blochează obiectivele fără câștig",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un proiect dificil cu deadline clar și șansă de vizibilitate "
            "este probabil un stresor:"
        ),
        "options": [
            "provocare (challenge) — poate motiva dacă resursele sunt ok",
            "obstacol (hindrance) — doar dacă blochează fără sens",
            "identic cu birocrația inutilă",
            "automat dăunător indiferent de context",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Reguli interne obscure, formulare inutile și lipsa clarității rolului "
            "sunt exemple tipice de:"
        ),
        "options": [
            "stresori obstacol (hindrance stressors)",
            "stresori provocare (challenge stressors)",
            "value fit ridicat",
            "coping centrat pe problemă eficient",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre challenge vs hindrance sunt corecte?"
        ),
        "options": [
            "challenge poate susține motivația și creșterea",
            "hindrance consumă resurse fără câștig dezvoltare",
            "toți stresorii sunt dăunători în egală măsură",
            "distincția ajută HR să prioritizeze intervențiile",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre Tip A și Tip B este falsă?"
        ),
        "options": [
            "Tip A și Tip B sunt factori Big Five oficiali",
            "Tip A include grabă și ostilitate",
            "Tip B e mai puțin orientat spre competiție intensă",
            "Tip A e asociat cu risc cardiovascular în cercetare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "O organizație cu valori de inovație angajează pe cineva cu "
            "valori de securitate și tradiție. Stresul poate apărea din:"
        ),
        "options": [
            "value fit scăzut",
            "P–E Fit slab pe dimensiunea valorilor",
            "Karasek — doar dacă controlul e mic, nu automat din valori",
            "necesitate de aculturație sau socializare atentă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care intervenții sunt plauzibile pentru reducerea stresului "
            "în modelul cerere–control?"
        ),
        "options": [
            "creșterea autonomiei unde cerințele sunt mari",
            "reducerea birocrației inutilă (hindrance)",
            "ignorarea completă a cerințelor — nerealist",
            "clarificarea rolului pentru a reduce ambiguitatea",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Într-o sinteză Value Fit & Stres, care asocieri sunt corecte?"
        ),
        "options": [
            "value fit bun → satisfacție, angajament, performanță, turnover↓",
            "stres = cerințe > resurse (reacție)",
            "GAS: alarmă → rezistență → epuizare",
            "groupthink = beneficiu garantat al valorilor comune",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmații „capcană” trebuie respinse?"
        ),
        "options": [
            "valorile = trăsături de personalitate",
            "stresul = evenimentul obiectiv, nu reacția",
            "Karasek: cerințe mari + control mare = mereu maxim stresant",
            "aculturația = abandon total al valorilor personale",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un manager vrea echipă unită prin valori comune, dar încurajează "
            "dissentul constructiv la decizii importante. Echilibrul vizat "
            "evită:"
        ),
        "options": [
            "groupthink",
            "cooperarea și coeziunea — nu le exclude",
            "socializarea organizațională — poate coexista",
            "value fit — dissentul nu înseamnă automat mismatch valoric",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care lanț este cel mai coerent pentru stresul la muncă?"
        ),
        "options": [
            "stresor → evaluare primară Lazarus → evaluare secundară → coping",
            "mismatch P–E Fit → percepție cerințe > resurse → reacție stres",
            "value fit perfect → imposibil orice stres de volum",
            "GAS: alarmă pe termen scurt, epuizare dacă stresul persistă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații rezumă corect capitolul Value Fit & Stres?"
        ),
        "options": [
            "Schwartz: zece valori; socializarea crește value fit",
            "stres Karasek maxim: cerințe mari + control mic",
            "challenge dezvoltă; hindrance frustrează",
            "groupthink e mereu benefic pentru performanță",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care exemple combină value fit și stres?"
        ),
        "options": [
            "firmă agresiv competitivă + angajat cu valori de bunăvoință → "
            "disonanță",
            "onboarding bun → învățare valori → fit mai bun → mai puțin "
            "stres identitar",
            "hindrance birocratic + cerințe mari + control zero → Karasek "
            "stres maxim",
            "shared values → groupthink garantat pozitiv pentru performanță",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmații rezumă corect ideile centrale studiate despre "
            "potrivirea valorilor (value fit), stresul la muncă și modul în "
            "care persoana evaluează situațiile solicitante și răspunde la ele "
            "(modelul Lazarus)?"
        ),
        "options": [
            "valorile sunt convingeri despre ce este important; când valorile "
            "persoanei se potrivesc cu cele ale organizației, cresc de regulă "
            "satisfacția, angajamentul și retenția",
            "stresul la muncă poate fi înțeles ca reacție la percepția că "
            "cerințele depășesc resursele disponibile; sindromul general de "
            "adaptare (GAS, Selye) și potrivirea persoană–mediu (P–E Fit) "
            "explică mecanismele implicate",
            "în modelul lui Richard Lazarus, evaluarea primară (este periculos?) "
            "și evaluarea secundară (pot face față?) precedă alegerea între "
            "coping centrat pe problemă și coping centrat pe emoție",
            "personalitatea de tip A este relaxată și puțin orientată spre "
            "competiție, iar tipul B este agresiv, grăbit și ostil",
        ],
        "correct": "abc",
    },
]
