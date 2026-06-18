"""Itemi suplimentari — Psihopatologie II: tulburările de personalitate."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PERSONALITATE_EXTRA_ITEMS: List[Item] = [
    # —— Criterii detaliate cluster A (1–10) ——
    {
        "stem": (
            "În tulburarea de personalitate paranoidă, persoana poate fi reticentă "
            "să se confie altora din teamă că informațiile vor fi folosite împotriva ei."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Manifestări frecvente în tulburarea de personalitate paranoidă:",
        "options": [
            "suspiciuni nejustificate privind fidelitatea partenerului",
            "nevoie crescută de control și hipervigilență",
            "interpretarea criticilor ca atacuri personale",
            "căutarea activă a atenției prin comportament teatral",
        ],
        "correct": "abc",
    },
    {
        "stem": "Criterii asociate tulburării de personalitate schizoidă includ:",
        "options": [
            "interes redus pentru activități sexuale",
            "puțini sau niciun prieten apropiat",
            "indiferență față de laude sau critici",
            "dramatizarea evenimentelor cotidiene",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate schizoidă și tulburarea de personalitate "
            "schizotipală au în comun preferința pentru activități solitare, dar "
            "schizotipala se distinge prin:"
        ),
        "options": [
            "comportament excentric și gândire magică",
            "experiențe perceptive neobișnuite",
            "lipsa oricărei anxietăți sociale",
            "afect plat fără suspiciune sau idei de referință",
        ],
        "correct": "ab",
    },
    {
        "stem": "În tulburarea de personalitate schizotipală pot apărea:",
        "options": [
            "afect nepotrivit sau constrâns",
            "discurs vag, metaforic sau greu de urmărit",
            "lipsa prietenilor apropiați",
            "grandiozitate și nevoie de admirație",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un tânăr evită prieteniile, crede că evenimentele din jur îl vizează "
            "personal și are convingeri paranormale, fără psihoză clară. "
            "Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate schizotipală",
            "tulburare de personalitate schizoidă",
            "tulburare de personalitate paranoidă",
            "tulburare de personalitate evitantă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate paranoidă diferă de tulburarea de personalitate "
            "schizotipală prin faptul că paranoidă pune accentul pe:"
        ),
        "options": [
            "suspiciune și interpretarea intențiilor ca răuvoitoare",
            "ranchiună și neîncredere persistentă",
            "gândire magică și excentricitate ca trăsături centrale",
            "lipsa oricărei suspiciuni față de ceilalți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Persoanele cu tulburare de personalitate schizoidă preferă adesea "
            "activități abstracte sau mecanice și au contact social redus."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Clusterul A poate include elemente asemănătoare spectrului schizofrenic, "
            "dar fără halucinații persistente și fără pierderea completă a realității."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea de personalitate schizoidă presupune lipsa dorinței de relații "
            "apropiate, nu doar evitarea din teamă de respingere."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Criterii detaliate cluster B (11–22) ——
    {
        "stem": "Manifestări frecvente în tulburarea de personalitate antisocială:",
        "options": [
            "conduita imprudentă față de propria siguranță sau a altora",
            "manipulare și lipsa responsabilității profesionale",
            "agresivitate repetată și infracționalitate",
            "nevoie excesivă de reasigurare înainte de decizii",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate antisocială nu poate fi diagnosticată la o "
            "persoană sub 18 ani; înainte de această vârstă se poate folosi "
            "tulburarea de conduită."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În tulburarea de personalitate borderline pot apărea, sub stres:",
        "options": [
            "idei paranoide tranzitorii",
            "simptome disociative severe",
            "episoade de grandiozitate stabilă, ca regulă",
            "lipsa oricărei frici de abandon",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii suplimentare în tulburarea de personalitate borderline:",
        "options": [
            "imagine de sine instabilă sau identitate difuză",
            "furie intensă, nepotrivită, greu de controlat",
            "relații interpersonale intense și instabile",
            "indiferență față de respingere sau abandon",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O pacientă idealizează apoi devalorizează partenerul, are impulsivitate "
            "în consum și senzație de gol interior. Aceste elemente susțin:"
        ),
        "options": [
            "tulburarea de personalitate borderline",
            "tulburarea de personalitate narcisistă",
            "tulburarea de personalitate histrionică",
            "tulburarea de personalitate obsesiv-compulsivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate borderline diferă de tulburarea bipolară "
            "prin faptul că instabilitatea afectivă borderline este, de regulă:"
        ),
        "options": [
            "mai legată de relații și teama de abandon",
            "mai reactivă la evenimente interpersonale",
            "însoțită obligatoriu de episoade maniacale clare",
            "absentă în absența conflictelor relationale",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate narcisistă:",
        "options": [
            "sentiment exagerat de importanță personală",
            "preocupare pentru fantezii de succes sau putere",
            "convingerea că este special și unic",
            "teamă dominantă de critică și inferioritate socială",
        ],
        "correct": "abc",
    },
    {
        "stem": "În tulburarea de personalitate narcisistă pot apărea:",
        "options": [
            "așteptări nerezonabile de favorizare",
            "invidie sau convingerea că este invidiat",
            "exploatarea celorlalți pentru propriile scopuri",
            "comportament supus și teamă de separare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un coleg se consideră superior, cere tratament special, răspunde "
            "agresiv la feedback și pare lipsit de empatie. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate narcisistă",
            "tulburare de personalitate evitantă",
            "tulburare de personalitate dependentă",
            "tulburare de personalitate schizoidă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate histrionică și tulburarea de personalitate "
            "narcisistă pot căuta admirație, dar histrionica se distinge prin:"
        ),
        "options": [
            "emoționalitate teatrală și superficială",
            "folosirea aspectului fizic pentru atenție",
            "grandiozitate stabilă ca nucleu central",
            "lipsa oricărei sugestibilități",
        ],
        "correct": "ab",
    },
    {
        "stem": "Manifestări frecvente în tulburarea de personalitate histrionică:",
        "options": [
            "stil de vorbire impresionist, lipsit de detaliu",
            "comportament seductiv sau provocator inadecvat",
            "folosirea aspectului fizic pentru a atrage atenția",
            "retragere preferențială și afect restrâns",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Clusterul B este caracterizat, în general, prin impulsivitate, "
            "instabilitate emoțională sau dificultăți în respectarea drepturilor celorlalți."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Criterii detaliate cluster C (23–34) ——
    {
        "stem": "Criterii suplimentare în tulburarea de personalitate evitantă:",
        "options": [
            "nevoie de siguranță că va fi plăcut înainte de relaționare",
            "reținere în relații intime din teamă de respingere",
            "evitarea activităților noi din teamă de jenă",
            "disconfort când nu este în centrul atenției",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate evitantă diferă de tulburarea de personalitate "
            "schizoidă prin faptul că persoana evitantă:"
        ),
        "options": [
            "dorește relații, dar le evită din teamă de critică",
            "se simte inadecvată și inferioară",
            "nu dorește deloc relații apropiate",
            "este indiferentă la laude și critici",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii suplimentare în tulburarea de personalitate dependentă:",
        "options": [
            "dificultate de a exprima dezacordul din teamă de pierderea sprijinului",
            "dificultate de a iniția proiecte pe cont propriu",
            "eforturi excesive pentru a obține îngrijire",
            "interpretarea neutră a intențiilor altora ca amenințătoare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O femeie rămâne într-o relație dăunătoare de teamă să rămână singură, "
            "nu își asumă decizii fără aprobare și acceptă tratament necorespunzător. "
            "Tabloul sugerează:"
        ),
        "options": [
            "tulburare de personalitate dependentă",
            "tulburare de personalitate antisocială",
            "tulburare de personalitate paranoidă",
            "tulburare de personalitate schizotipală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate dependentă diferă de tulburarea de personalitate "
            "borderline prin faptul că dependenta pune accentul pe:"
        ),
        "options": [
            "nevoia de îngrijire și teama de separare",
            "supunere și dificultăți de autonomie",
            "instabilitate afectivă și autovătămare",
            "grandiozitate și exploatarea celorlalți",
        ],
        "correct": "ab",
    },
    {
        "stem": "Manifestări frecvente în tulburarea de personalitate obsesiv-compulsivă:",
        "options": [
            "perfecționism care împiedică finalizarea sarcinilor",
            "preocupare excesivă pentru reguli, liste sau ordine",
            "rigiditate morală și iresponsabilitate interpersonală",
            "ritualuri de verificare pentru teamă de contaminare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un manager insistă pe reguli stricte, refuză delegarea, este rigid "
            "moral și prioritizează munca în detrimentul relațiilor. Tabloul sugerează:"
        ),
        "options": [
            "tulburare de personalitate obsesiv-compulsivă",
            "tulburarea obsesiv-compulsivă",
            "tulburare de personalitate antisocială",
            "tulburare de personalitate histrionică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate obsesiv-compulsivă se asociază cu perfecționism "
            "rigid și dificultăți de flexibilitate, nu cu obsesii și compulsii clinice obligatorii."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea de personalitate evitantă și tulburarea anxioasă socială pot "
            "coexista; evitantă include, în plus, sentimente cronice de inadecvare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea de personalitate dependentă presupune că persoana acceptă "
            "adesea tratament necorespunzător pentru a evita singurătatea."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Clusterul C al tulburărilor de personalitate este caracterizat, în general, prin:",
        "options": [
            "anxietate și teamă",
            "evitare interpersonală",
            "nevoie de control sau de sprijin",
            "impulsivitate și căutarea atenției",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În tulburarea de personalitate dependentă, teama de abandon poate determina "
            "căutarea rapidă a unei noi relații de sprijin după încheierea unei relații."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Fațete, comorbiditate și evaluare (35–42) ——
    {
        "stem": "Fațeta afectivitate negativă poate include:",
        "options": [
            "labilitate emoțională și anxietate",
            "nesiguranță față de separare și depresivitate",
            "ostilitate, perseverare și suspiciozitate",
            "grandiozitate și căutarea atenției",
        ],
        "correct": "abc",
    },
    {
        "stem": "Fațeta dezinhibiție poate include:",
        "options": [
            "impulsivitate și distractibilitate",
            "iresponsabilitate și asumarea riscurilor",
            "perfecționism rigid și ordine excesivă",
            "retragere socială și anhedonie",
        ],
        "correct": "ab",
    },
    {
        "stem": "Comorbiditatea între tulburările de personalitate este:",
        "options": [
            "frecventă, inclusiv între tulburări din clustere diferite",
            "posibilă cu tulburări de dispoziție sau anxioase",
            "absentă în practica clinică",
            "limitată la un singur cluster, fără excepții",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La evaluarea tulburărilor de personalitate, tiparul trebuie să fie "
            "durabil, inflexibil și să producă suferință sau afectare, nu doar "
            "o reacție tranzitorie la stres."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburările de personalitate nu trebuie diagnosticate dacă tabloul "
            "este explicat mai bine de efectele unei substanțe sau ale unei "
            "afecțiuni medicale."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Trăsăturile de personalitate din spectrul normal pot deveni patologice "
            "când sunt extreme, persistente, inflexibile și produc afectare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "În modelul actual, tulburările de personalitate pot fi evaluate și prin:",
        "options": [
            "nivel de funcționare al personalității",
            "trăsături patologice pe fațete",
            "tipare pe clustere tradiționale",
            "scor unic de inteligență emoțională",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Afectarea funcționării personalității poate include dificultăți în "
            "empatie, intimitate și reglarea emoțională."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Diferențieri avansate și capcane (43–50) ——
    {
        "stem": (
            "Care afirmații descriu corect tulburarea de personalitate paranoidă, "
            "nu tulburarea de personalitate schizotipală?"
        ),
        "options": [
            "ranchiună persistentă și suspiciune față de loialitate",
            "interpretarea amenințătoare a remarcilor neutre",
            "gândire magică și superstiții ca element central",
            "discurs vag, excentric, greu de urmărit",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un adolescent de 16 ani are istoric de încălcări grave ale regulilor, "
            "minciuni și agresivitate. Diagnosticul de tulburare de personalitate "
            "antisocială este:"
        ),
        "options": [
            "prematur; se poate folosi tulburarea de conduită",
            "posibil doar după vârsta de 18 ani",
            "obligatoriu la orice vârstă",
            "exclus dacă există impulsivitate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate borderline și tulburarea de personalitate "
            "histrionică pot căuta atenție, dar borderline se distinge prin:"
        ),
        "options": [
            "frică intensă de abandon și relații instabile",
            "autovătămare sau comportament suicidar",
            "emoții superficiale, teatrale, fără instabilitate profundă",
            "lipsa impulsivității și a furiei intense",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate schizoidă și tulburarea de personalitate "
            "evitantă pot evita socializarea, dar evitantă se distinge prin:"
        ),
        "options": [
            "dorința de relații, inhibată de teamă de critică",
            "sentimente de inadecvare și inferioritate",
            "indiferență la laude și lipsa dorinței de intimitate",
            "comportament seductiv și dramatizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea obsesiv-compulsivă și tulburarea de personalitate "
            "obsesiv-compulsivă pot implica ordine, dar tulburarea obsesiv-compulsivă "
            "presupune:"
        ),
        "options": [
            "obsesii și/sau compulsii clinice recurente",
            "ritualuri menite să reducă anxietatea",
            "doar perfecționism de personalitate, fără obsesii",
            "absența oricărei suferințe funcționale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care tulburări aparțin clusterului B al tulburărilor de personalitate?"
        ),
        "options": [
            "tulburarea de personalitate antisocială",
            "tulburarea de personalitate borderline",
            "tulburarea de personalitate histrionică",
            "tulburarea de personalitate evitantă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O persoană folosește haine stridente, vorbește dramatic, exagerează "
            "legăturile cu colegii și devine rapid centrul atenției la petreceri. "
            "Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate histrionică",
            "tulburare de personalitate evitantă",
            "tulburare de personalitate schizoidă",
            "tulburare de personalitate paranoidă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Toate tulburările de personalitate necesită manifestarea rigidă a "
            "tiparului în cel puțin două domenii: cogniție, afectivitate, "
            "funcționare interpersonală sau controlul impulsurilor."
        ),
        "tf": True,
        "correct_tf": True,
    },
]
