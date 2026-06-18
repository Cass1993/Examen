"""Itemi — Designul muncii (Hackman–Oldham, JD-R), lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

DESIGN_MUNCII_ITEMS: List[Item] = [
    # —— Scop și cadru (1–5) ——
    {
        "stem": (
            "Designul muncii (job design) urmărește, în principal, organizarea "
            "sarcinilor și responsabilităților astfel încât să crească motivația "
            "la locul de muncă și, în consecință, performanța."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare descrie cel mai bine legătura logică pe care o "
            "presupune designul muncii?"
        ),
        "options": [
            "structurarea sarcinilor influențează experiența psihologică la job, "
            "care la rândul ei influențează atitudinile și rezultatele la muncă",
            "performanța determină automat structura postului, fără intervenție "
            "asupra conținutului sarcinilor",
            "designul muncii se limitează la descrierea cunoștințelor, deprinderilor "
            "și aptitudinilor (KSAO) din job specification",
            "motivația externă înlocuiește orice caracteristică a sarcinii în "
            "modelul clasic al designului muncii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Modelul caracteristicilor muncii al lui Hackman și Oldham pornește "
            "de la ideea că anumite însușiri ale sarcinii pot produce stări "
            "psihologice critice, care apoi influențează rezultatele la locul "
            "de muncă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care enumerare conține toate cele cinci caracteristici centrale ale "
            "muncii din modelul Hackman–Oldham?"
        ),
        "options": [
            "skill variety, task identity, task significance, autonomy și feedback",
            "meaningfulness, responsibility, knowledge of results, burnout și engagement",
            "volum de muncă, presiune de timp, conflict de rol și efort emoțional",
            "recrutare, selecție, training, evaluare performanță și salarizare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un consultant în resurse umane (HR) reformulează un post astfel încât "
            "angajatul să folosească mai multe competențe, să vadă un produs finit "
            "al muncii sale și să înțeleagă impactul rolului asupra altora. Aceste "
            "intervenții vizează, în principal:"
        ),
        "options": [
            "varietatea abilităților, identitatea sarcinii și semnificația sarcinii",
            "autonomia și feedback-ul privind rezultatele",
            "doar cerințele din job specification, nu designul sarcinii",
            "resursele din modelul cerințe–resurse (JD-R), nu caracteristicile Hackman–Oldham",
        ],
        "correct": "a",
    },
    # —— Cele 5 caracteristici — definiții (6–14) ——
    {
        "stem": (
            "În modelul Hackman–Oldham, „varietatea abilităților” (skill variety) "
            "înseamnă că postul:"
        ),
        "options": [
            "postul cere utilizarea mai multor competențe și deprinderi diferite",
            "munca implică variabilitate în tipurile de abilități folosite la job",
            "postul presupune schimbarea permanentă a locului de muncă în firmă",
            "postul evaluează performanța doar prin ore suplimentare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Identitatea sarcinii” (task identity) se referă la faptul că "
            "angajatul poate:"
        ),
        "options": [
            "finaliza o lucrare sau un produs recognoscibil de la început până "
            "la sfârșit",
            "lucrează la fragmente izolate, fără să vadă rezultatul final al lucrării",
            "identifica postul doar prin titlul din organigramă",
            "schimba automat gradul de autonomie fără modificarea sarcinilor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "„Semnificația sarcinii” (task significance) vizează percepția că "
            "munca prestată:"
        ),
        "options": [
            "are un impact semnificativ asupra vieții sau bunăstării altor persoane",
            "este importantă doar pentru salariul primit la sfârșitul lunii",
            "pare importantă în principal pentru indicatorii financiari ai firmei, "
            "nu pentru impactul asupra altora",
            "se măsoară doar prin productivitatea cantitativă, fără sens social",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În modelul Hackman–Oldham, „autonomia” (autonomy) presupune că "
            "angajatul are libertate substanțială în:"
        ),
        "options": [
            "programarea activităților și alegerea metodelor de lucru",
            "stabilirea salariilor tuturor colegilor din departament",
            "modificarea unilaterală a obiectivelor strategice ale organizației",
            "primește feedback doar anual, la evaluarea globală de performanță",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "„Feedback-ul privind rezultatele” (feedback) din modelul "
            "Hackman–Oldham indică faptul că:"
        ),
        "options": [
            "angajatul primește informații clare despre cât de bine își îndeplinește "
            "sarcinile",
            "organizația oferă doar evaluări anuale formale, fără legătură cu "
            "sarcina curentă",
            "feedback-ul ține doar de relațiile informale dintre colegi, nu de "
            "rezultatele muncii",
            "primește informații despre rezultate doar indirect, prin rapoarte "
            "agregate ale departamentului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi asociază corect o caracteristică a muncii cu "
            "descrierea ei în modelul Hackman–Oldham?"
        ),
        "options": [
            "task identity — angajatul vede un produs finit al muncii sale",
            "task significance — munca pare importantă pentru alții",
            "skill variety — postul folosește o singură deprindere repetată",
            "feedback — informații despre rezultate doar la nivel de echipă, "
            "fără legătură cu sarcina individuală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un tehnician repară echipamente diverse, livrează aparatul funcțional "
            "clientului și știe că intervenția sa previne oprirea producției. "
            "Fără autonomie sau feedback suplimentar, care caracteristici "
            "Hackman–Oldham sunt ilustrare?"
        ),
        "options": [
            "skill variety",
            "task identity",
            "task significance",
            "autonomy",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un operator poate decide singur ordinea operațiilor și primește zilnic "
            "date despre rata de erori. În modelul Hackman–Oldham, acestea "
            "corespund:"
        ),
        "options": [
            "autonomiei (autonomy)",
            "feedback-ului privind rezultatele",
            "semnificației sarcinii (task significance)",
            "identității sarcinii (task identity)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei caracteristici ale muncii contribuie la experiența de "
            "meaningfulness (sens perceput al muncii) în modelul Hackman–Oldham?"
        ),
        "options": [
            "skill variety, task identity și task significance",
            "autonomy, feedback și task identity",
            "autonomy și feedback, fără skill variety",
            "toate cele cinci caracteristici, în aceeași pondere",
        ],
        "correct": "a",
    },
    # —— Stări psihologice critice (15–22) ——
    {
        "stem": (
            "În modelul Hackman–Oldham, experiența de „meaningfulness” (sens "
            "perceput al muncii) se calculează ca media aritmetică a:"
        ),
        "options": [
            "skill variety, task identity și task significance",
            "autonomy și feedback",
            "autonomy, feedback și task identity",
            "toate cele cinci caracteristici împreună",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care caracteristică a muncii este asociată în mod direct cu starea "
            "psihologică „experienced responsibility” (responsabilitate "
            "percepută) în modelul Hackman–Oldham?"
        ),
        "options": [
            "autonomia (autonomy)",
            "feedback-ul privind rezultatele",
            "task significance",
            "skill variety",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Starea psihologică „knowledge of results” (cunoașterea rezultatelor) "
            "este legată în mod direct de:"
        ),
        "options": [
            "feedback-ul privind performanța la sarcină",
            "autonomia în programarea muncii",
            "semnificația sarcinii pentru alții",
            "varietatea abilităților cerute de post",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care mapări între caracteristici ale muncii și stări psihologice "
            "critice sunt corecte în modelul Hackman–Oldham?"
        ),
        "options": [
            "(SV + TI + TS) / 3 → meaningfulness",
            "autonomy → experienced responsibility",
            "feedback → knowledge of results",
            "feedback → meaningfulness",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă un post are skill variety, task identity și task significance "
            "ridicate, dar feedback foarte scăzut, care stare psihologică critică "
            "riscă să rămână slabă?"
        ),
        "options": [
            "knowledge of results",
            "meaningfulness",
            "experienced responsibility",
            "toate trei în egală măsură, indiferent de feedback",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un manager crește autonomia angajaților, dar nu modifică conținutul "
            "sarcinilor. În modelul Hackman–Oldham, intervenția vizează în "
            "principal starea psihologică:"
        ),
        "options": [
            "starea psihologică „experienced responsibility” (responsabilitate percepută)",
            "starea psihologică „knowledge of results” (cunoașterea rezultatelor)",
            "experiența de meaningfulness (sens al muncii)",
            "motivația internă la locul de muncă, ca stare intermediară",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Meaningfulness, experienced responsibility și knowledge of results "
            "sunt stări psihologice critice intermediare — nu consecințe finale "
            "precum motivația internă sau performanța."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care lanț cauzal este susținut de modelul Hackman–Oldham?"
        ),
        "options": [
            "caracteristici ale muncii → stări psihologice critice → atitudini și "
            "rezultate la locul de muncă",
            "stări psihologice → caracteristici ale muncii → performanță",
            "salarizare → autonomie → skill variety",
            "feedback → task identity → autonomy → burnout",
        ],
        "correct": "a",
    },
    # —— MPS și consecințe (23–32) ——
    {
        "stem": (
            "Indicele de potențial motivațional (MPS) "
            "din modelul Hackman–Oldham se calculează astfel:"
        ),
        "options": [
            "MPS = [(skill variety + task identity + task significance) / 3] × "
            "autonomy × feedback",
            "MPS = skill variety + task identity + task significance + autonomy + "
            "feedback",
            "MPS = autonomy × feedback / (skill variety + task identity)",
            "MPS = (autonomy + feedback) × task significance, fără skill variety",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un post cu indice de potențial motivațional (MPS) ridicat sugerează, în "
            "modelul Hackman–Oldham:"
        ),
        "options": [
            "un potențial mai mare de a genera stări motivaționale favorabile",
            "garantarea automată a performanței maxime, indiferent de context",
            "variabilitate individuală redusă la zero în răspunsul la orice sarcină",
            "reducerea feedback-ului pentru a limita presiunea evaluativă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care consecințe sunt asociate, în modelul Hackman–Oldham, cu stările "
            "psihologice critice și cu un indice de potențial motivațional (MPS) "
            "favorabil?"
        ),
        "options": [
            "motivație internă la locul de muncă",
            "satisfacție în muncă",
            "performanță ridicată",
            "calitate superioară a muncii prestate",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În modelul Hackman–Oldham, motivația internă la locul de muncă este "
            "de obicei urmată, în lanțul consecințelor, de satisfacție, apoi de "
            "performanță și calitate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "De ce în formula indiceului de potențial motivațional (MPS) varietatea, "
            "identitatea și semnificația sarcinii intră ca medie, iar autonomia și "
            "feedback-ul ca factori multiplicativi?"
        ),
        "options": [
            "cele trei contribuie la meaningfulness, iar autonomia și feedback-ul "
            "activează responsibility și knowledge of results — toate trei stări "
            "sunt necesare pentru potențial motivațional",
            "autonomia și feedback-ul sunt mai puțin importante decât skill variety",
            "media celor trei înlocuiește nevoia de autonomy și feedback",
            "formula urmărește doar satisfacția salarială, nu motivația internă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un post are scoruri mari la skill variety, task identity și task "
            "significance, dar autonomy și feedback aproape de zero. Conform "
            "modelului Hackman–Oldham, indicele de potențial motivațional (MPS) va fi:"
        ),
        "options": [
            "scăzut sau nul, deoarece autonomia și feedback-ul intră multiplicativ",
            "ridicat, deoarece meaningfulness compensează orice alt factor",
            "identic cu media celor trei prime caracteristici, indiferent de rest",
            "irelevant pentru motivația internă la locul de muncă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații despre indicele de potențial motivațional (MPS) sunt "
            "corecte?"
        ),
        "options": [
            "un indice de potențial motivațional (MPS) mare indică un potențial "
            "motivațional mai mare al postului",
            "indicele de potențial motivațional (MPS) nu garantează automat "
            "performanța la toți angajații",
            "indicele de potențial motivațional (MPS) înlocuiește analiza postului "
            "orientată spre sarcină",
            "indicele de potențial motivațional (MPS) sintetizează caracteristicile "
            "muncii relevante pentru motivație",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "„Job control” (controlul asupra muncii) se referă, în literatura de "
            "design al muncii, la gradul în care angajatul poate influența:"
        ),
        "options": [
            "ritmul, metodele și deciziile legate de modul de executare a sarcinilor",
            "politica salarială la nivelul întregii organizații",
            "numirea directorului general al companiei",
            "structura ierarhică a familiei de joburi din rețeaua ocupațională "
            "(O*NET)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Conform cercetărilor din domeniul designului muncii, un control mai "
            "mare asupra muncii (job control) este asociat frecvent cu:"
        ),
        "options": [
            "niveluri mai reduse de stres perceput",
            "satisfacție mai mare la locul de muncă",
            "performanță garantată indiferent de resursele postului",
            "scăderea necesității feedback-ului formal de la supervizor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Empowerment” (împuternicire) la locul de muncă include, în mod tipic:"
        ),
        "options": [
            "autonomie în executarea sarcinilor",
            "participare la decizii relevante pentru rol",
            "asumarea responsabilității pentru rezultate",
            "transferul responsabilității către angajat, fără resurse de suport",
        ],
        "correct": "abc",
    },
    # —— Empowerment, job control, distincții (33–38) ——
    {
        "stem": (
            "Care afirmație despre empowerment (împuternicire) la locul de muncă "
            "este corectă?"
        ),
        "options": [
            "presupune autonomie, participare la decizii relevante și "
            "responsabilitate pentru rezultate",
            "înseamnă doar autonomie operațională, fără implicare în decizii",
            "transferă toată responsabilitatea către angajat, fără resurse sau suport",
            "este sinonim cu job enlargement — adăugarea de sarcini similare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care distincții între concepte din designul muncii sunt corecte?"
        ),
        "options": [
            "job control — influență asupra ritmului și metodelor de lucru",
            "autonomy (Hackman–Oldham) — libertate în programarea și metodele "
            "proprii de muncă",
            "empowerment — autonomie plus participare la decizii și responsabilitate",
            "feedback — informații despre muncă furnizate doar de colegi, nu de "
            "sarcină",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un angajat poate avea feedback frecvent, dar foarte puțină autonomie. "
            "În modelul Hackman–Oldham, această situație poate susține:"
        ),
        "options": [
            "knowledge of results, dar nu neapărat experienced responsibility",
            "meaningfulness ridicat, indiferent de conținutul sarcinii",
            "indice de potențial motivațional (MPS) maxim, deoarece feedback "
            "compensează autonomia",
            "autonomie ridicată prin simpla prezență a feedback-ului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Intervențiile de job enrichment (îmbogățirea muncii) urmăresc, de "
            "regulă, creșterea:"
        ),
        "options": [
            "caracteristicilor centrale din modelul Hackman–Oldham",
            "doar volumului de ore suplimentare, fără schimbarea sarcinilor",
            "creșterea salariului, fără modificarea conținutului muncii",
            "numărului de niveluri ierarhice din organigramă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre job rotation (rotația posturilor) este corectă?"
        ),
        "options": [
            "poate crește skill variety, dar nu garantează task identity ridicată "
            "în fiecare rol",
            "asigură automat identitatea sarcinii în toate posturile prin care "
            "trece angajatul",
            "înlocuiește nevoia de autonomy și feedback în modelul Hackman–Oldham",
            "este identică cu job enrichment — îmbogățirea adâncimii sarcinii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Comparând job enlargement (lărgirea muncii) cu job enrichment "
            "(îmbogățirea muncii), care afirmație este mai precisă?"
        ),
        "options": [
            "enlargement adaugă mai multe sarcini similare; enrichment crește "
            "adâncimea și caracteristicile motivaționale ale sarcinii",
            "ambele înseamnă același lucru în modelul Hackman–Oldham",
            "enrichment reduce autonomy pentru a simplifica munca",
            "enlargement înlocuiește nevoia de feedback și autonomie",
        ],
        "correct": "a",
    },
    # —— JD-R (39–50) ——
    {
        "stem": (
            "Modelul cerințe–resurse la locul de muncă (JD-R) explică bunăstarea și "
            "performanța la muncă prin două tipuri de caracteristici ale "
            "postului:"
        ),
        "options": [
            "cerințe (demands) și resurse (resources)",
            "autonomie și feedback, ca în formula indiceului de potențial motivațional "
            "(MPS)",
            "varietatea abilităților și identitatea sarcinii, ca în formula indiceului "
            "de potențial motivațional (MPS)",
            "salarizare și promovare, ca în ciclul de resurse umane (HR) clasic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care exemple sunt tipice pentru „job demands” (cerințe) în modelul cerințe–resurse (JD-R)?"
        ),
        "options": [
            "volum mare de muncă și presiune de timp",
            "conflict de rol și ambiguitate de rol",
            "efort emoțional ridicat (ex. muncă cu suferința altora)",
            "autonomie și feedback constructiv de la șef",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care exemple sunt tipice pentru „job resources” (resurse) în modelul cerințe–resurse (JD-R)?"
        ),
        "options": [
            "autonomie și control asupra modului de lucru",
            "feedback social și suport din partea colegilor sau a superiorilor",
            "oportunități de dezvoltare și învățare la locul de muncă",
            "presiune constantă și volum excesiv de sarcini",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În modelul cerințe–resurse (JD-R), cerințele ridicate și prelungite ale muncii (job "
            "demands) sunt asociate în principal cu:"
        ),
        "options": [
            "burnout (epuizare profesională)",
            "work engagement (implicare ridicată la muncă)",
            "satisfacție garantată indiferent de resurse",
            "scăderea stresului prin creșterea volumului de muncă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În modelul cerințe–resurse (JD-R), resursele la locul de muncă (job resources) sunt "
            "asociate în principal cu:"
        ),
        "options": [
            "work engagement (implicare și energie pozitivă la muncă)",
            "burnout, atunci când resursele sunt prea multe",
            "scăderea performanței prin autonomie crescută",
            "motivație intrinsecă scăzută, indiferent de resurse",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În modelul cerințe–resurse (JD-R), resursele la locul de muncă duc direct la burnout, "
            "iar cerințele ridicate produc engagement."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care perechi de legături cauzale sunt corecte în modelul cerințe–resurse (JD-R)?"
        ),
        "options": [
            "job demands → burnout",
            "job resources → engagement",
            "job resources → burnout",
            "job demands → engagement garantat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un asistent social are volum mare de cazuri, termene strânse și "
            "contact zilnic cu suferința clienților. În modelul cerințe–resurse (JD-R), acestea "
            "sunt:"
        ),
        "options": [
            "job demands (cerințe)",
            "job resources (resurse)",
            "caracteristici care cresc direct indicele de potențial motivațional "
            "(MPS) în formula Hackman–Oldham",
            "factori care reduc suportul social necesar la job",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Aceeași echipă primește autonomie în programare, feedback regulat de "
            "la șef și acces la formare. În modelul cerințe–resurse (JD-R), acestea sunt:"
        ),
        "options": [
            "job resources (resurse)",
            "job demands (cerințe)",
            "factori care măresc automat skill variety fără schimbarea sarcinii",
            "surse de burnout prin exces de sprijin organizațional",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care diferențe între modelul Hackman–Oldham și modelul cerințe–resurse (JD-R) sunt "
            "corect formulate?"
        ),
        "options": [
            "Hackman–Oldham focalizează caracteristici motivaționale ale sarcinii "
            "și indicele de potențial motivațional (MPS); modelul cerințe–resurse "
            "(JD-R) focalizează cerințe versus resurse și procese de "
            "epuizare/implicare",
            "modelul cerințe–resurse (JD-R) înlocuiește modelul caracteristicilor "
            "muncii în toate aplicațiile",
            "Hackman–Oldham explică doar burnout, nu motivația internă",
            "ambele modele folosesc aceeași formulă a indiceului de potențial "
            "motivațional (MPS) pentru engagement",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre relația dintre cerințe și resurse în modelul "
            "cerințe–resurse (JD-R) este susținută de cercetare?"
        ),
        "options": [
            "resursele pot atenua efectul negativ al cerințelor ridicate asupra "
            "bunăstării",
            "cerințele ridicate produc automat engagement, indiferent de resurse",
            "resursele cresc burnout-ul atunci când autonomia este prea mare",
            "modelul cerințe–resurse (JD-R) exclude feedback-ul și suportul social ca resurse",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un consultant propune: (1) clarificarea impactului muncii asupra "
            "echipei, (2) lăsarea libertății în ordinea sarcinilor, (3) raport "
            "săptămânal de rezultate, (4) reducerea ambiguității rolului și (5) "
            "acces la mentorat. Care intervenții vizează direct caracteristicile "
            "Hackman–Oldham și care resurse din modelul cerințe–resurse (JD-R)?"
        ),
        "options": [
            "task significance și feedback — Hackman–Oldham",
            "autonomy — Hackman–Oldham",
            "suport/mentorat și clarificarea rolului — resurse din modelul "
            "cerințe–resurse (JD-R)",
            "mentoratul este job demand, deoarece consumă timp",
        ],
        "correct": "abc",
    },
]
