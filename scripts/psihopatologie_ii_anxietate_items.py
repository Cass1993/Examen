"""Itemi — Psihopatologie II: tulburările anxioase."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ANXIETATE_ITEMS: List[Item] = [
    # —— Repere generale tulburări anxioase (1–6) ——
    {
        "stem": "Tulburările anxioase se caracterizează, în principal, prin:",
        "options": [
            "frică, îngrijorare sau incertitudine excesivă",
            "răspuns anxios disproporționat sau persistent",
            "episoade de elație și grandiozitate",
            "halucinații persistente, fără insight",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Consecințele frecvente ale tulburărilor anxioase pot include afectarea:"
        ),
        "options": [
            "sănătății fizice și funcționării profesionale",
            "relațiilor și calității vieții",
            "inteligenței generale, în mod obligatoriu",
            "memoriei pe termen lung, ca simptom central",
        ],
        "correct": "ab",
    },
    {
        "stem": "Procese comune în tulburările anxioase includ:",
        "options": [
            "simptome fiziologice de panică",
            "prejudecăți cognitive și selectarea stimulilor amenințători",
            "evitare și perseverarea gândurilor anxioase",
            "absența oricărei componente fiziologice",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Comorbiditatea în tulburările anxioase este frecventă cu:"
        ),
        "options": [
            "alte tulburări anxioase",
            "episoade depresive",
            "tulburarea obsesiv-compulsivă, în unele cazuri",
            "schizofrenia, ca regulă diagnostică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburările anxioase implică întotdeauna o amenințare reală "
            "și iminentă, clar identificabilă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Experiențele timpurii de vulnerabilizare pot contribui la "
            "dezvoltarea tulburărilor anxioase."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Fobia specifică (7–16) ——
    {
        "stem": "Fobia specifică presupune frică sau anxietate marcată față de:",
        "options": [
            "un obiect sau o situație specifică",
            "orice interacțiune socială, fără excepție",
            "îngrijorare generalizată despre viitor",
            "episoade recurente de panică neașteptată",
        ],
        "correct": "a",
    },
    {
        "stem": "Exemple de stimuli fobici în fobia specifică:",
        "options": [
            "animale, înălțimi sau zbor",
            "injecții, sânge sau proceduri medicale",
            "spații închise sau situații specifice",
            "orice loc public, fără stimul concret",
        ],
        "correct": "abc",
    },
    {
        "stem": "Criteriile pentru fobia specifică includ:",
        "options": [
            "frică imediată și disproporționată față de stimul",
            "evitare sau suportare cu frică intensă",
            "durată de minimum șase luni",
            "prezența obligatorie a atacurilor de panică",
        ],
        "correct": "abc",
    },
    {
        "stem": "Subtipurile fobiei specifice din clasificarea actuală includ:",
        "options": [
            "animale și mediu natural",
            "sânge, injecții și leziuni",
            "situațional și alte fobii",
            "socială și generalizată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O studentă evită lifturile de teamă că va rămâne blocată; "
            "recunoaște că frica este excesivă. Tabloul sugerează:"
        ),
        "options": [
            "fobie specifică de tip situațional",
            "tulburare de panică, ca diagnostic principal",
            "tulburare obsesiv-compulsivă cu ritualuri",
            "tulburare anxioasă generalizată izolată",
        ],
        "correct": "a",
    },
    {
        "stem": "Fobia de sânge sau injecții se deosebește prin:",
        "options": [
            "reacție fiziologică specifică, uneori leșin",
            "evitarea stimulului sau suportarea cu frică intensă",
            "absența oricărei componente corporale",
            "prezența obligatorie a agorafobiei",
        ],
        "correct": "ab",
    },
    {
        "stem": "Explicațiile etiologice ale fobiei specifice includ:",
        "options": [
            "condiționarea clasică și experiențe traumatice",
            "învățare observațională și informații amenințătoare",
            "vulnerabilitate biologică pentru anumite stimuli",
            "exclusiv o cauză psihanalitică unică, demonstrată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Experimentul lui Little Albert ilustrează modul în care un stimul neutru "
            "poate deveni stimul condiționat prin asociere cu un stimul aversiv."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tratamentul fobiei specifice se bazează, în principal, pe:",
        "options": [
            "expunere gradată sau intensivă la stimulul fobic",
            "reducerea evitării și infirmarea convingerilor catastrofice",
            "evitarea permanentă a stimulului pentru siguranță",
            "psihanaliză clasică ca singură intervenție obligatorie",
        ],
        "correct": "ab",
    },
    {
        "stem": "Intervențiile în fobia specifică pot include:",
        "options": [
            "desensibilizare sistematică și flooding",
            "restructurare cognitivă și experimente comportamentale",
            "contracondiționare",
            "confirmarea evitării ca strategie centrală",
        ],
        "correct": "abc",
    },
    # —— Tulburarea anxioasă socială (17–26) ——
    {
        "stem": "Tulburarea anxioasă socială presupune frică severă de:",
        "options": [
            "situații sociale sau de performanță",
            "evaluare negativă de către ceilalți",
            "stimuli fobici concreți, cum ar fi animalele",
            "atacuri de panică neașteptate, fără context social",
        ],
        "correct": "ab",
    },
    {
        "stem": "Persoana cu tulburare anxioasă socială poate evita:",
        "options": [
            "conversații, mâncat sau băut în public",
            "vorbitul în fața altora sau situațiile de observare",
            "orice activitate solitară, fără contact social",
            "interacțiunile în care se simte evaluată",
        ],
        "correct": "abd",
    },
    {
        "stem": "Criteriile pentru tulburarea anxioasă socială includ:",
        "options": [
            "frică marcată de interacțiuni sociale",
            "evitare sau suportare cu anxietate intensă",
            "durată de cel puțin șase luni",
            "prezența obligatorie a agorafobiei",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un adolescent refuză să prezinte în clasă de teamă că va fi "
            "judecat negativ; simptomele persistă de un an. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare anxioasă socială",
            "fobie specifică de tip animalier",
            "tulburare de panică, fără componentă socială",
            "tulburare obsesiv-compulsivă cu verificări",
        ],
        "correct": "a",
    },
    {
        "stem": "Factori de risc pentru tulburarea anxioasă socială includ:",
        "options": [
            "inhibiție comportamentală la copilărie",
            "părinți anxioși sau protecție excesivă",
            "timiditate și retragere în situații noi",
            "absența oricărei componente familiale",
        ],
        "correct": "abc",
    },
    {
        "stem": "Procesele cognitive în tulburarea anxioasă socială includ:",
        "options": [
            "predicții negative despre evenimente sociale",
            "atenție excesivă asupra propriei persoane",
            "procesare negativă după evenimentul social",
            "interpretarea performanței ca excelentă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Terapia cognitivă Clark și Wells în anxietatea socială urmărește:"
        ),
        "options": [
            "reducerea comportamentelor de siguranță",
            "mutarea atenției spre exterior și feedback video",
            "experimente comportamentale și restructurare post-eveniment",
            "evitarea situațiilor sociale ca obiectiv principal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Terapia cognitiv-comportamentală în tulburarea anxioasă socială poate include:"
        ),
        "options": [
            "expunere la situații sociale",
            "training al abilităților sociale",
            "restructurare cognitivă",
            "izolarea completă de stimuli sociali",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Debutul tulburării anxioase sociale este, de regulă, timpuriu, "
            "adesea înainte de 18 ani."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Medicația poate ajuta pe termen scurt în tulburarea anxioasă socială, "
            "dar intervențiile cognitive-comportamentale urmăresc menținerea beneficiilor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Tulburarea de panică și agorafobia (27–38) ——
    {
        "stem": "Tulburarea de panică presupune:",
        "options": [
            "atacuri repetate de panică, bruște și intense",
            "simptome fiziologice: palpitații, transpirație, tremur",
            "frică de moarte, pierdere a controlului sau „a înnebuni”",
            "îngrijorare cronică despre mai multe domenii, fără atacuri",
        ],
        "correct": "abc",
    },
    {
        "stem": "Simptomele unui atac de panică pot include:",
        "options": [
            "dificultăți respiratorii, greață sau amețeală",
            "depersonalizare sau derealizare",
            "hiperventilație și senzație de sufocare",
            "lentoare psihomotorie și anhedonie prelungită",
        ],
        "correct": "abc",
    },
    {
        "stem": "Pentru diagnosticul tulburării de panică este necesar:",
        "options": [
            "atacuri recurente și neașteptate",
            "cel puțin o lună de îngrijorare persistentă față de atacuri",
            "schimbări comportamentale dezadaptative legate de atacuri",
            "prezența obligatorie a agorafobiei",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O pacientă evită metroul de teamă că nu va putea ieși dacă apare panică. "
            "Frica vizează situația de prindere, nu un stimul fobic concret. Aceasta indică:"
        ),
        "options": [
            "agorafobie",
            "fobie specifică de tip animalier",
            "tulburare anxioasă generalizată izolată",
            "tulburare obsesiv-compulsivă cu ritualuri",
        ],
        "correct": "a",
    },
    {
        "stem": "Agorafobia presupune frică sau anxietate față de:",
        "options": [
            "locuri unde persoana se simte prinsă sau nesigură",
            "situații în care ajutorul ar putea lipsi la panică",
            "transport public, spații deschise, cozi sau mulțimi",
            "un singur obiect specific, cum ar fi șerpii",
        ],
        "correct": "abc",
    },
    {
        "stem": "Criteriile pentru agorafobie includ:",
        "options": [
            "frică față de cel puțin două tipuri de situații",
            "evitare sau trăire cu frică intensă",
            "durată de cel puțin șase luni",
            "prezența obligatorie a unui stimul fobic unic",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tulburarea de panică și agorafobia sunt:",
        "options": [
            "probleme înrudite, dar separabile diagnostic",
            "posibil comorbide la unii pacienți",
            "identice și nedistincte în toate cazurile",
            "mutual exclusive, fără suprapunere",
        ],
        "correct": "ab",
    },
    {
        "stem": "Explicațiile etiologice ale panicii includ:",
        "options": [
            "hiperventilație și creșterea dioxidului de carbon",
            "condiționarea clasică cu indici interni sau situaționali",
            "sensibilitate la anxietate și interpretare catastrofală",
            "absența oricărei componente fiziologice",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Sensibilitatea la anxietate se referă la frica de senzațiile anxioase "
            "în sine, interpretate ca semne de pericol."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Comportamentele de siguranță în tulburarea de panică:",
        "options": [
            "mențin problema prin evitarea infirmării convingerilor",
            "împiedică învățarea că senzațiile nu sunt periculoase",
            "elimină automat riscul de atacuri viitoare",
            "sunt recomandate ca strategie principală pe termen lung",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tratamentul tulburării de panică poate include:",
        "options": [
            "educație despre fiziologia panicii",
            "restructurare cognitivă și expunere interoceptivă",
            "prevenirea comportamentelor de siguranță",
            "evitarea oricărei senzații corporale neplăcute",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Expunerea interoceptivă urmărește producerea controlată a senzațiilor "
            "corporale temute, pentru a învăța că nu sunt periculoase."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Tulburarea anxioasă generalizată (39–50) ——
    {
        "stem": "Tulburarea anxioasă generalizată presupune:",
        "options": [
            "îngrijorare excesivă, cronică și greu de controlat",
            "preocupare despre mai multe domenii ale vieții",
            "frică de un singur obiect sau situație specifică",
            "atacuri de panică neașteptate ca simptom central",
        ],
        "correct": "ab",
    },
    {
        "stem": "Simptomele fizice frecvente în tulburarea anxioasă generalizată:",
        "options": [
            "neliniște și tensiune musculară",
            "oboseală, dureri sau greață",
            "grandiozitate și energie crescută",
            "halucinații auditive persistente",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criteriile pentru tulburarea anxioasă generalizată includ:",
        "options": [
            "anxietate și îngrijorare excesivă despre două sau mai multe domenii",
            "prezența simptomelor mai multe zile decât nu, timp de cel puțin trei luni",
            "suferință sau afectare funcțională semnificativă",
            "durată obligatorie de minimum șase luni, ca la fobii",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un bărbat se îngrijorează zilnic despre muncă, sănătate și familie, "
            "nu poate opri gândurile de peste trei luni. Tabloul sugerează:"
        ),
        "options": [
            "tulburare anxioasă generalizată",
            "fobie specifică de tip situațional",
            "tulburare de panică, ca diagnostic principal",
            "tulburare obsesiv-compulsivă cu compulsii",
        ],
        "correct": "a",
    },
    {
        "stem": "Factori etiologici în tulburarea anxioasă generalizată includ:",
        "options": [
            "componentă genetică moderată și reglare emoțională dificilă",
            "bias în procesarea informațiilor amenințătoare",
            "catastrofizarea și credințe metacognitive despre îngrijorare",
            "absența oricărei îngrijorări cognitive",
        ],
        "correct": "abc",
    },
    {
        "stem": "Credințele metacognitive în tulburarea anxioasă generalizată pot include:",
        "options": [
            "ideea că îngrijorarea previne pericolul",
            "convingerea că îngrijorarea este periculoasă și incontrolabilă",
            "certitudinea că îngrijorarea este mereu inutilă",
            "absența oricărei evaluări a utilității îngrijorării",
        ],
        "correct": "ab",
    },
    {
        "stem": "Caracteristici dispoziționale asociate tulburării anxioase generalizate:",
        "options": [
            "intoleranță la incertitudine",
            "perfecționism și responsabilitate exagerată",
            "încredere scăzută în propria capacitate de coping",
            "indiferență totală față de consecințe",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tratamentul psihologic al tulburării anxioase generalizate poate include:",
        "options": [
            "controlul stimulilor de îngrijorare",
            "restructurare cognitivă și relaxare",
            "repetare comportamentală și antrenarea copingului",
            "generalizarea îngrijorării în toată ziua",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Controlul stimulilor de îngrijorare presupune limitarea îngrijorării "
            "la un timp și un context stabilit."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea anxioasă generalizată are comorbiditate ridicată cu depresia "
            "și alte tulburări anxioase."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tratamentul farmacologic al tulburării anxioase generalizate poate include:",
        "options": [
            "inhibitori selectivi ai recaptării serotoninei",
            "inhibitori ai recaptării serotoninei și noradrenalinei",
            "anxiolitice, cu eficiență variabilă pe termen lung",
            "antipsihotice ca tratament de primă linie obligatoriu",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În tulburarea anxioasă generalizată, îngrijorarea este percepută ca "
            "incontrolabilă și poate deveni catastrofizare repetată."
        ),
        "tf": True,
        "correct_tf": True,
    },
]
