"""Itemi — Fluctuația și satisfacția muncii, lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

FLUCTUATIE_SATISFACTIE_MUNCII_ITEMS: List[Item] = [
    # —— Turnover: definiție, tipuri (1–8) ——
    {
        "stem": (
            "În psihologia organizațională, turnover-ul (fluctuația personalului) "
            "înseamnă părăsirea organizației de către angajați — fie voluntar "
            "(aleg să plece), fie involuntar (sunt concediați)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care distincție descrie corect turnover-ul voluntar față de cel "
            "involuntar?"
        ),
        "options": [
            "voluntar = angajatul inițiază plecarea; involuntar = organizația "
            "încetează contractul",
            "voluntar = concediere disciplinară; involuntar = demisie la cerere",
            "voluntar = transfer intern între departamente; involuntar = plecare "
            "către alt angajator",
            "voluntar = absențe nemotivate; involuntar = concediu medical lung",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Turnover-ul funcțional presupune că pleacă în principal angajații "
            "cu performanță slabă, eliberând loc pentru oameni mai potriviți. "
            "Turnover-ul disfuncțional înseamnă că pleacă performanții sau "
            "angajații valoroși — situația considerată cea mai problematică "
            "pentru organizație."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "O firmă de IT pierde trei programatori de top care pleacă la "
            "concurență, în timp ce doi angajați cu performanță sub așteptări "
            "sunt concediați în aceeași lună. Care tip de turnover este cel "
            "mai îngrijorător pentru organizație?"
        ),
        "options": [
            "disfuncțional — pleacă performanții valoroși",
            "funcțional — pleacă cei slabi, ceea ce e mereu benefic",
            "involuntar — pentru că organizația a inițiat concedierile",
            "voluntar — pentru că demisiile sunt mereu mai costisitoare decât "
            "concedierile",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre turnover-ul funcțional și disfuncțional sunt "
            "corecte?"
        ),
        "options": [
            "funcțional: pleacă cei cu performanță slabă — poate îmbunătăți "
            "calitatea echipei",
            "disfuncțional: pleacă performanții — pierdere de know-how și "
            "costuri de înlocuire",
            "disfuncțional este considerat cel mai problematic pentru firmă",
            "funcțional este întotdeauna de dorit, indiferent de context sau "
            "volum",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre turnover-ul disfuncțional este falsă "
            "(deci greșită)?"
        ),
        "options": [
            "disfuncțional este preferabil pentru că eliberează posturi de "
            "neperformanți",
            "disfuncțional înseamnă că pleacă angajați valoroși",
            "disfuncțional este considerat cel mai problematic",
            "funcțional poate îmbunătăți uneori calitatea echipei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care scenarii ilustrează turnover voluntar, respectiv involuntar?"
        ),
        "options": [
            "angajatul demisionează pentru un salariu mai bun",
            "firma îl concediază pentru abateri repetate",
            "angajatul pleacă după ce a găsit alt job",
            "contractul expiră și nu este prelungit la inițiativa angajatorului",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "De ce nu este suficient să raportezi doar „rata de fluctuație” fără "
            "a distinge tipul de turnover?"
        ),
        "options": [
            "aceeași rată poate ascunde plecări de performanți (disfuncțional) "
            "sau de neperformanți (funcțional)",
            "costurile și implicațiile pentru organizație diferă după cine "
            "pleacă și de ce",
            "voluntar vs involuntar ajută la înțelegerea cauzelor și a "
            "intervențiilor HR",
            "toate tipurile de turnover au același impact asupra satisfacției "
            "clienților, deci distincția e decorativă",
        ],
        "correct": "abc",
    },
    # —— Withdrawal model, intenție, Hobo (9–18) ——
    {
        "stem": (
            "Modelul retragerii (Withdrawal Model) descrie, în ordine logică, "
            "lanțul: insatisfacție la muncă → gânduri despre plecare → "
            "căutare de alternative → intenție de plecare → plecare efectivă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În modelul retragerii (Withdrawal Model), care este ordinea "
            "corectă a etapelor?"
        ),
        "options": [
            "insatisfacție → gânduri de plecare → căutare alternative → "
            "intenție de plecare → plecare",
            "plecare → intenție → insatisfacție → căutare alternative",
            "căutare alternative → insatisfacție → plecare imediată",
            "intenție de plecare → insatisfacție → gânduri de plecare → plecare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre predicția turnover-ului este susținută cel "
            "mai consistent de cercetare?"
        ),
        "options": [
            "intenția de plecare este cel mai bun predictor al turnover-ului "
            "efectiv",
            "absențele din ultima lună sunt mereu mai predictive decât "
            "intenția de plecare",
            "vârsta cronologică singură explică majoritatea plecărilor",
            "satisfacția raportată acum 5 ani prezice mai bine plecarea decât "
            "intenția actuală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un angajat spune că e nemulțumit, caută activ joburi pe site-uri "
            "de recrutare și declară că „probabil pleacă în 3 luni”, dar încă "
            "vine la serviciu. În modelul retragerii, el se află cel mai probabil:"
        ),
        "options": [
            "la etapa de intenție de plecare (înainte de plecarea efectivă)",
            "deja în turnover efectiv, deoarece intenția = plecare",
            "doar la insatisfacție, fără legătură cu căutarea de alternative",
            "în turnover involuntar, pentru că organizația nu l-a concediat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Sindromul hobo (Hobo Syndrome) în literatura despre fluctuație "
            "se referie la:"
        ),
        "options": [
            "tendința ca turnover-ul din trecut să prezică turnover viitor la "
            "aceeași persoană",
            "obligația legală de a preda laptopul la demisie",
            "transferul satisfacției de la muncă către viața personală",
            "angajamentul afectiv față de organizație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care factori sunt asociați în mod tipic cu turnover-ul sau "
            "intenția de plecare?"
        ),
        "options": [
            "salariu și perspective de promovare",
            "suportul șefului și climatul organizațional",
            "stilul de leadership perceput",
            "descrierea postului din analiza orientată spre sarcină — fără "
            "legătură cu decizia de a pleca",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În cercetarea personalității și a fluctuației, care tendințe sunt "
            "raportate frecvent?"
        ),
        "options": [
            "neuroticismul (N) mai ridicat este asociat cu mai mult turnover "
            "sau intenție de plecare",
            "conștiinciozitatea (C) mai ridicată este asociată cu mai puțin "
            "turnover",
            "deschiderea (Openness) poate fi asociată cu mai multă schimbare "
            "de job, din căutarea de varietate",
            "extraversiunea (E) elimină complet orice intenție de plecare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care etape din modelul retragerii (Withdrawal Model) intervin "
            "înainte de plecarea efectivă?"
        ),
        "options": [
            "insatisfacție la muncă",
            "gânduri despre plecare",
            "căutare de alternative de angajare",
            "intenție de plecare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Intenția de plecare este un predictor slab al turnover-ului "
            "pentru că majoritatea oamenilor care spun că vor pleca rămân "
            "definitiv în firmă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un recrutor observă că un candidat a avut șase joburi în opt ani, "
            "fiecare sub un an. Conceptul relevant pentru a anticipa "
            "comportament viitor este:"
        ),
        "options": [
            "sindromul hobo (Hobo Syndrome) — pattern de fluctuație repetată",
            "spill-over — transfer al stresului de la muncă acasă",
            "turnover funcțional — pleacă performanții",
            "cross-over — influența satisfacției soțului asupra angajatului",
        ],
        "correct": "a",
    },
    # —— Satisfacția muncii: definiție, Locke (19–28) ——
    {
        "stem": (
            "Care enunț descrie cel mai precis satisfacția muncii?"
        ),
        "options": [
            "evaluare afectivă a experienței profesionale",
            "compararea așteptărilor cu realitatea de la job",
            "numărul de ore suplimentare lucrate lunar",
            "scorul la un test de inteligență generală (GMA)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care definiție surprinde cel mai bine satisfacția muncii?"
        ),
        "options": [
            "evaluare afectivă (pozitivă/negativă) a experienței la job",
            "compararea așteptărilor cu ceea ce oferă efectiv munca",
            "numărul de promovări obținute în ultimii cinci ani",
            "scorul pur cognitiv la un test de aptitudini profesionale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Conform lui Edwin Locke, satisfacția muncii crește atunci când:"
        ),
        "options": [
            "munca permite îndeplinirea valorilor personale importante",
            "jobul se aliniază cu ce consideră angajatul că contează pentru el",
            "angajatul primește automat cel mai mare salariu din piață, "
            "indiferent de valori",
            "organizația are cel mai mare număr de angajați din industrie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un angajat câștigă bine, dar simte că munca îi contrazice "
            "valorile (ex. etică, echilibru viață–muncă). Conform lui Locke, "
            "satisfacția lui va fi probabil:"
        ),
        "options": [
            "scăzută, deoarece valorile personale nu sunt împlinite la job",
            "ridicată, pentru că salariul anulează orice evaluare afectivă",
            "neutră, pentru că Locke vorbește doar de promovare",
            "determinată exclusiv de personalitate, nu de valori",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care distincții sunt corecte între satisfacția muncii și "
            "concepte învecinate?"
        ),
        "options": [
            "satisfacția = evaluare afectivă a jobului, nu doar lista de "
            "beneficii",
            "satisfacția nu se reduce la performanță obiectivă sau la "
            "prezența la serviciu",
            "satisfacția înseamnă același lucru cu angajamentul organizațional",
            "așteptările nerealizate pot alimenta insatisfacția în modelul "
            "retragerii",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre satisfacția muncii este exagerată (deci "
            "greșită)?"
        ),
        "options": [
            "satisfacția se reduce la productivitate — dacă produci mult, ești "
            "automat satisfăcut",
            "satisfacția include o componentă afectivă față de job",
            "așteptările nerealizate pot genera insatisfacție",
            "Locke leagă satisfacția de valorile personale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce este utilă distincția așteptări vs realitate în "
            "înțelegerea satisfacției muncii?"
        ),
        "options": [
            "aceeași situație obiectivă poate satisface pe unii și nu pe "
            "alții, după ce așteaptă fiecare",
            "explică de ce doi colegi la același job pot raporta satisfacții "
            "diferite",
            "anulează rolul valorilor personale în teoria lui Locke",
            "leagă satisfacția de percepția subiectivă, nu doar de fapte brute",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care perechi descriu corect componente ale experienței la muncă "
            "legate de satisfacție?"
        ),
        "options": [
            "evaluare afectivă — plăcut vs neplăcut la job",
            "așteptări — ce credeam că voi obține",
            "realitate percepută — ce oferă efectiv rolul",
            "turnover involuntar — concediere fără demisie",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Conform lui Locke, ce situație susține cel mai probabil "
            "satisfacția muncii?"
        ),
        "options": [
            "munca permite trăirea valorilor personale importante",
            "jobul se aliniază cu ce contează pentru angajat",
            "salariul este mediu, dar valorile sunt încălcate zilnic",
            "organizația are sediu central într-un oraș mare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un student crede că „satisfacția = fericire permanentă la birou”. "
            "Care clarificare pedagogică este cea mai potrivită?"
        ),
        "options": [
            "e o evaluare afectivă relativ stabilă față de job, nu stare de "
            "euforie continuă",
            "include și comparația între ce așteptam și ce am găsit",
            "poate coexista cu performanță bună sau slabă — nu le identifică",
            "înseamnă că nu poți fi nemulțumit dacă ai salariu decent",
        ],
        "correct": "abc",
    },
    # —— Cele 9 dimensiuni, promovare (29–38) ——
    {
        "stem": (
            "Care fac parte din dimensiunile frecvent evaluate ale "
            "satisfacției muncii?"
        ),
        "options": [
            "salariul (Pay) și perspectivele de promovare (Promotion)",
            "beneficiile (Benefits) și recompensele contingente",
            "colegii, supervizarea și natura muncii în sine (Work Itself)",
            "procedurile interne și comunicarea organizațională",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În multe studii, care dimensiune a satisfacției muncii este "
            "cel mai puternic predictor al intenției de plecare?"
        ),
        "options": [
            "promovarea (Promotion) — percepția șanselor de avansare",
            "salariul (Pay) — uneori important, dar nu mereu cel mai puternic",
            "beneficiile (Benefits) — asigurări, tichete etc.",
            "procedurile (Policies) — reguli interne",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un angajat spune: „Plătesc ok, colegii sunt buni, dar nu văd "
            "nicio șansă să cresc.” Care dimensiune a satisfacției este "
            "probabil cea mai afectată?"
        ),
        "options": [
            "promovarea (Promotion)",
            "natura muncii în sine (Work Itself)",
            "beneficiile (Benefits)",
            "comunicarea — deși e relevantă, mesajul indică blocaj de carieră",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre dimensiunile satisfacției muncii sunt "
            "corecte?"
        ),
        "options": [
            "Pay = satisfacția față de remunerare",
            "Work Itself = cât de interesantă și semnificativă e sarcina",
            "Supervision = relația cu șeful direct",
            "Promotion = doar numărul de zile de concediu legal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce înseamnă recompensele contingente în evaluarea satisfacției "
            "muncii?"
        ),
        "options": [
            "percepția că performanța mai bună este recompensată corect",
            "legătura dintre efort/rezultate și bonusuri sau recunoaștere",
            "beneficiile fixe din contract, identice pentru toți",
            "numărul de zile de concediu medical plătit",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dimensiuni țin mai direct de relațiile interpersonale la "
            "locul de muncă?"
        ),
        "options": [
            "colegii (Coworkers)",
            "supervizarea (Supervision)",
            "comunicarea organizațională",
            "procedurile contabile — fără componentă socială directă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce promovarea (Promotion) poate prezice mai bine intenția de "
            "plecare decât salariul (Pay)?"
        ),
        "options": [
            "lipsa perspectivei de creștere poate genera frustrare pe termen "
            "lung, chiar cu plată acceptabilă",
            "promovarea ține de sens, status și dezvoltare, nu doar de "
            "tranzacția monetară imediată",
            "salariul nu contează niciodată pentru intenția de plecare",
            "percepția blocajului de carieră alimentează etapele din modelul "
            "retragerii",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Asociază corect dimensiunea cu exemplul:"
        ),
        "options": [
            "„Sarcinile mele sunt variate și îmi folosesc competențele”",
            "„Regulile interne sunt clare și corecte”",
            "„Cei care muncesc mai mult sunt recompensați corect”",
            "„Știu exact cât plătesc colegii din alt departament”",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre predictori ai intenției de plecare este "
            "falsă?"
        ),
        "options": [
            "salariul (Pay) este întotdeauna cel mai puternic predictor, "
            "înaintea promovării (Promotion)",
            "promovarea percepută poate prezice puternic intenția de plecare",
            "lipsa perspectivei de carieră poate frustra chiar cu plată ok",
            "insatisfacția la promovare poate alimenta modelul retragerii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care combinații de dimensiuni ar explica cel mai plauzibil o "
            "insatisfacție generalizată?"
        ),
        "options": [
            "supervizare toxică + lipsă promovare + proceduri percepute ca "
            "injuste",
            "work itself captivant + colegi cooperanți + comunicare clară",
            "beneficii decente, dar work itself monoton și fără sens perceput",
            "pay excelent + promotion clară + supervision suportivă",
        ],
        "correct": "ac",
    },
    # —— Satisfacție–performanță, spill-over, cross-over (39–48) ——
    {
        "stem": (
            "Relația dintre satisfacția muncii și performanță este, în "
            "general, pozitivă, dar modestă: a fi mulțumit nu garantează "
            "automat performanță ridicată, și invers."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre legătura satisfacție–performanță este "
            "cea mai fidelă cercetării?"
        ),
        "options": [
            "există o relație pozitivă, dar de obicei moderată (nu perfectă)",
            "fericirea la job garantează automat productivitate maximă",
            "performanța ridicată elimină orice nemulțumire",
            "relația poate fi influențată de alți factori (abilități, resurse, "
            "claritatea rolului)",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Spill-over și cross-over descriu transferul satisfacției sau "
            "stării afective. Care definiții sunt corecte?"
        ),
        "options": [
            "spill-over = transfer în aceeași persoană (ex. muncă → viață "
            "personală)",
            "cross-over = transfer între persoane (ex. starea partenerului "
            "influențează pe angajat)",
            "spill-over = transfer de la soț la angajat în aceeași familie",
            "cross-over = doar fluctuația între departamente în aceeași firmă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Spill-over înseamnă transferul stării între două persoane "
            "diferite (ex. de la coleg la coleg)."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care dimensiune a satisfacției muncii are, în studii, cel mai "
            "mare spill-over către satisfacția vieții personale?"
        ),
        "options": [
            "natura muncii în sine (Work Itself)",
            "beneficiile (Benefits)",
            "procedurile (Policies)",
            "recompensele contingente izolate de sensul muncii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un angajat iubește sarcinile zilnice (Work Itself ridicat), dar "
            "e nemulțumit de salariu. Ce efect este plauzibil conform ideii "
            "de spill-over?"
        ),
        "options": [
            "satisfacția vieții personale poate fi susținută parțial de "
            "plăcerea muncii, chiar dacă pay e slab",
            "work itself poate „curge” spre stare generală de bine dincolo de "
            "birou",
            "salariul slab anulează complet orice spill-over pozitiv, mereu",
            "cross-over garantează că partenerul va fi și el mulțumit la job",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Soția unui angajat e foarte stresată la job; el raportează că "
            "și el se simte mai tensionat acasă, deși la serviciul lui nimic "
            "nu s-a schimbat. Acest fenomen se numește cel mai probabil:"
        ),
        "options": [
            "cross-over — transfer între persoane",
            "spill-over — transfer în aceeași persoană de la muncă la viață",
            "turnover disfuncțional",
            "sindrom hobo (Hobo Syndrome)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care exemple ilustrează spill-over, respectiv cross-over?"
        ),
        "options": [
            "stresul de la job îmi afectează dispoziția acasă",
            "nemulțumirea partenerului mă influențează și pe mine",
            "plec de la firmă A la firmă B",
            "mă simt bine la job și asta îmi îmbunătățește seara acasă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "De ce relația satisfacție–performanță nu justifică singură "
            "concluzia „dacă îi fac pe toți fericiți, performanța explodează”?"
        ),
        "options": [
            "corelația e modestă — mulți factori influențează performanța",
            "performanța depinde și de abilități, resurse, claritatea sarcinii",
            "unii pot fi mulțumiți cu munca minimă necesară",
            "satisfacția și performanța sunt aceeași măsurătoare cu alt nume",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce natura muncii în sine (Work Itself) are spill-over puternic "
            "către viața personală?"
        ),
        "options": [
            "plăcerea de a face munca se transferă în stare generală de bine",
            "e o dimensiune centrală a experienței zilnice — nu doar un "
            "beneficiu marginal",
            "work itself transferă automat satisfacția între două persoane "
            "(cross-over)",
            "beneficiile anulează complet orice efect al work itself",
        ],
        "correct": "ab",
    },
    # —— Angajament afectiv, sinteză satisfacție vs angajament (49–60) ——
    {
        "stem": (
            "Care descriere se potrivește angajamentului afectiv (affective "
            "commitment)?"
        ),
        "options": [
            "rămâi pentru că vrei și te identifici cu organizația",
            "implicare emoțională față de firmă, nu doar obligație",
            "rămâi doar pentru că nu ai oferte alternative",
            "rămâi pentru că șeful are autoritate formală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care consecințe sunt asociate tipic cu angajamentul afectiv "
            "ridicat?"
        ),
        "options": [
            "performanță mai bună",
            "turnover mai scăzut",
            "comportament de cetățenie organizațională (OCB) mai frecvent",
            "absențe nemotivate obligatorii la toți angajații",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care distincție surprinde cel mai bine diferența dintre "
            "satisfacția muncii și angajamentul organizațional?"
        ),
        "options": [
            "satisfacția ține de evaluarea afectivă a muncii / jobului",
            "angajamentul ține de legătura cu organizația ca întreg",
            "satisfacția și angajamentul sunt mereu identice ca măsură",
            "angajamentul afectiv implică „vreau să rămân”, nu doar „îmi place "
            "sarcina de azi”",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un angajat își place munca zilnică (satisfacție ridicată), dar "
            "nu se simte legat de firmă și ar pleca pentru un alt angajator "
            "similar. Ce combinație descrie cel mai bine situația?"
        ),
        "options": [
            "satisfacție față de muncă relativ ridicată",
            "angajament afectiv față de organizație probabil scăzut",
            "angajament afectiv ridicat — pentru că îi place sarcina",
            "risc de turnover dacă apare o alternativă atractivă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre tipurile de angajament organizațional "
            "este falsă?"
        ),
        "options": [
            "angajamentul continuance (lipsă alternative) = angajamentul "
            "afectiv",
            "angajamentul afectiv implică dorința de a rămâne",
            "continuance înseamnă că rămâi pentru că trebuie sau n-ai opțiuni",
            "afectivul se leagă de identificare emoțională cu organizația",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care lanț cauzal este cel mai coerent cu materia despre "
            "insatisfacție și plecare?"
        ),
        "options": [
            "insatisfacție (ex. promovare blocată) → intenție de plecare → "
            "turnover",
            "insatisfacție → gânduri de plecare → căutare joburi — model "
            "retragerii",
            "angajament afectiv ridicat → turnover disfuncțional garantat",
            "satisfacție ridicată → intenție de plecare maximă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații leagă corect satisfacția, angajamentul și "
            "comportamentul la organizație?"
        ),
        "options": [
            "angajament afectiv ridicat → mai mult OCB, mai puțin turnover",
            "satisfacția față de muncă nu garantează angajament față de firmă",
            "toți angajații mulțumiți au automat angajament afectiv maxim",
            "promovarea percepută influențează satisfacția și poate alimenta "
            "intenția de plecare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Într-o sinteză pentru examen, care perechi de concepte sunt "
            "corect asociate?"
        ),
        "options": [
            "turnover disfuncțional — pleacă performanții",
            "intenție de plecare — cel mai bun predictor al turnover-ului",
            "spill-over — aceeași persoană, muncă → viață",
            "cross-over — transfer în aceeași persoană, fără influență "
            "interpersonală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care scenarii combină corect mai multe idei din capitol?"
        ),
        "options": [
            "nemulțumire de promovare → căutare job → intenție → demisie",
            "work itself plăcut → spill-over pozitiv spre viața personală",
            "angajament afectiv ridicat → OCB și retenție mai bună",
            "turnover funcțional când pleacă cei mai valoroși — disfuncțional",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un HR vrea să reducă turnover-ul disfuncțional. Care intervenții "
            "sunt cele mai bine ancorate în cercetare?"
        ),
        "options": [
            "clarificarea căilor de promovare și dezvoltare",
            "îmbunătățirea supervizării și climatului",
            "monitorizarea intenției de plecare în sondaje",
            "ignorarea satisfacției pentru că performanța e mereu legată "
            "perfect de ea",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmații „capcană” (greșite dar plausible) trebuie respinse?"
        ),
        "options": [
            "fericit la job = automat performant maxim",
            "spill-over = influență între două persoane diferite",
            "turnover funcțional = pleacă cei mai buni performanți",
            "satisfacția = angajament organizațional — același construct",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmații rezumă corect capitolul despre fluctuație și "
            "satisfacția muncii?"
        ),
        "options": [
            "satisfacția muncii = evaluare afectivă a jobului",
            "angajamentul afectiv = dorința de a rămâne în organizație",
            "intenția de plecare = cel mai bun predictor al turnover-ului",
            "promovarea percepută = adesea predictor puternic al intenției "
            "de plecare",
        ],
        "correct": "abcd",
    },
]
