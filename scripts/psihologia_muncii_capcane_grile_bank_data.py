"""Itemi — Capcane grilă (Psihologia muncii II), lot suplimentar."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

CAPCANE_GRILE_ITEMS: List[Item] = [
    # —— Analiză post & KSAO (1–6) ——
    {
        "stem": (
            "Un document listează sarcinile, responsabilitățile și raportările "
            "rolului de contabil. Alt document descrie studiile, experiența și "
            "competențele cerute ocupantului. Care asociere este corectă?"
        ),
        "options": [
            "primul = job description (descrierea postului)",
            "al doilea = job specification (specificația postului / profil KSAO)",
            "primul = profilul persoanei; al doilea = lista sarcinilor",
            "ambele sunt sinonime pentru același document HR",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un candidat știe teoria contabilității (a citit manuale), dar nu "
            "reușește să închidă raportările la termen. Distincția relevantă:"
        ),
        "options": [
            "knowledge (cunoștințe) = ce știe teoretic",
            "ability (abilitate) = ce poate executa efectiv",
            "knowledge și ability sunt mereu identice la examen",
            "problema e de ability, nu doar de knowledge",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Job description descrie postul; job specification descrie profilul "
            "persoanei potrivite pentru acel post (KSAO)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre analiza orientată spre sarcină vs cea "
            "orientată spre angajat este corectă?"
        ),
        "options": [
            "spre sarcină = ce face ocupantul în rol",
            "spre angajat = ce KSAO trebuie să aibă ocupantul",
            "sunt sinonime — aceeași listă de întrebări",
            "spre angajat = fluxul zilnic de proceduri",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care pereche din capcanele de examen este inversată greșit?"
        ),
        "options": [
            "job description = postul; job specification = persoana (KSAO)",
            "knowledge = ce știi; ability = ce poți face",
            "job description = KSAO; job specification = sarcini zilnice",
            "analiză spre sarcină = ce face; analiză spre angajat = ce trebuie să aibă",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Un HR amestecă în același fișier „operează soft X” cu „are diplomă "
            "în Y”. Ce confuzie de grilă ilustrează?"
        ),
        "options": [
            "amestecă job description cu job specification",
            "amestecă knowledge cu ability fără a le distinge",
            "descrie turnover în loc de intenție de plecare",
            "folosește BOS în loc de BARS",
        ],
        "correct": "ab",
    },
    # —— Selecție: screening, sensibilitate, deficiență (7–12) ——
    {
        "stem": (
            "Screening-ul la angajare elimină candidații nepotriviți; evaluarea "
            "comprehensivă (comprehensive) selectează printre cei rămași pe cel "
            "mai potrivit."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un test de selecție are sensibilitate ridicată: prinde aproape toți "
            "candidații buni, dar lasă să treacă și unii slabi. Ce măsoară "
            "sensibilitatea?"
        ),
        "options": [
            "capacitatea de a identifica corect pe cei buni (adevărați pozitivi)",
            "capacitatea de a respinge pe cei răi — mai degrabă specificitate",
            "același lucru cu specificitatea — capcana de examen",
            "utilă când vrei să nu pierzi talente, cu risc de fals pozitivi",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Care afirmație despre sensibilitate și specificitate la teste "
            "este corectă?"
        ),
        "options": [
            "sensibilitate ridicată = prinde mai bine candidații buni",
            "specificitate ridicată = respinge mai bine candidații slabi",
            "ambele sunt mereu maxime simultan în practică",
            "le confundă frecvent grilele: sensibilitate ≠ specificitate",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "În evaluarea performanței, criteriul nu include „lucru în echipă” "
            "deși e esențial pentru rol — dar se notează „aspect vestimentar”. "
            "Ce pereche de capcane descrie situația?"
        ),
        "options": [
            "deficiență de criteriu = lipsește ce e relevant",
            "contaminare de criteriu = intră ce e nerelevant",
            "screening = comprehensive — aceeași etapă",
            "spill-over = cross-over — aceeași persoană",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care distincții din grila de selecție și măsurare sunt corecte?"
        ),
        "options": [
            "screening elimină; comprehensive selectează dintre supraviețuitori",
            "sensibilitate = prinde buni; specificitate = elimină răi",
            "deficiență = lipsește relevant; contaminare = apare nerelevant",
            "sensibilitate și specificitate sunt mereu maxime simultan — realist",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un test cu specificitate scăzută lasă să treacă candidați slabi. "
            "Care afirmații sunt corecte?"
        ),
        "options": [
            "specificitate scăzută = mai mulți nepotriviți acceptați",
            "specificitatea scăzută respinge pe toți, inclusiv pe cei buni",
            "sensibilitatea și specificitatea sunt capcane frecvent confundate",
            "specificitate ridicată ajută să elimini candidații slabi",
        ],
        "correct": "acd",
    },
    # —— Performanță: task, OCB, CWB (13–17) ——
    {
        "stem": (
            "Angajatul își îndeplinește toate sarcinile din fișa postului, dar "
            "refuză să ajute colegii sau să respecte normele de bunăvoință. "
            "Ce distincție e relevantă?"
        ),
        "options": [
            "performanță la sarcină (task) poate fi bună",
            "performanță contextuală / OCB poate fi slabă",
            "CWB înseamnă comportament care ajută organizația — invers",
            "task și contextual nu sunt același lucru la examen",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "OCB (organizational citizenship behavior) ajută organizația; "
            "CWB (counterproductive work behavior) îi dăunează."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care pereche din capcanele despre performanță la muncă este "
            "gresit formulată (de respins)?"
        ),
        "options": [
            "task performance = obligațiile de rol",
            "contextual performance = comportamente extra-rol care susțin organizația",
            "OCB = contraproductiv; CWB = cetățenie organizațională",
            "performanța totală poate include task și contextual",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Un angajat fură timp de lucru și sabotează proiecte, dar livrează "
            "rapoartele la termen. Cum clasifici?"
        ),
        "options": [
            "task performance — posibil acceptabilă pe livrabile",
            "CWB — comportament contraproductiv prezent",
            "OCB — pentru că livrează la timp",
            "nu poți avea task bun și CWB simultan — capcană",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care asocieri task / contextual / OCB / CWB sunt corecte?"
        ),
        "options": [
            "task = sarcini din job description",
            "contextual = comportamente care susțin mediul de lucru",
            "OCB = voluntar, ajută organizația",
            "CWB = dăunează organizației sau colegilor",
        ],
        "correct": "abcd",
    },
    # —— Fluctuație: turnover, spill-over, satisfacție (18–23) ——
    {
        "stem": (
            "Care distincție turnover vs intenție de plecare este corectă?"
        ),
        "options": [
            "turnover = comportament de plecare efectivă",
            "intenție de plecare = atitudine; predictor al turnover-ului",
            "sunt mereu același construct măsurat",
            "intenția poate fi măsurată înainte de plecare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "După o zi grea la birou, angajatul e irascibil acasă cu familia. "
            "Ce fenomen descrie?"
        ),
        "options": [
            "spill-over — transfer între domenii la aceeași persoană",
            "cross-over — între persoane diferite",
            "turnover funcțional",
            "intenție de plecare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Partenerul unui angajat stresat devine și el anxios fără să lucreze "
            "în aceeași firmă. Termenul potrivit:"
        ),
        "options": [
            "cross-over (crossover) — între persoane diferite",
            "spill-over — aceeași persoană, domenii diferite",
            "satisfacție muncii",
            "angajament continuu (continuance commitment)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care capcană de examen confundă spill-over cu cross-over?"
        ),
        "options": [
            "spill-over = aceeași persoană, muncă ↔ viață personală",
            "cross-over = starea unuia influențează pe altul",
            "spill-over = soțul îl influențează pe angajat — invers",
            "ambele implică transfer de stare, dar între entități diferite",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Care distincție satisfacție muncii vs angajament organizațional "
            "este corectă?"
        ),
        "options": [
            "satisfacția = evaluare afectivă a jobului",
            "angajamentul = legătură psihologică cu organizația",
            "sunt constructe identice — capcană de examen",
            "pot fi corelate, dar nu sunt același lucru",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații „capcană” despre fluctuație și satisfacție sunt "
            "greșite?"
        ),
        "options": [
            "turnover și intenție de plecare sunt mereu același lucru",
            "spill-over înseamnă influență între două persoane",
            "satisfacția muncii și angajamentul organizațional sunt identice",
            "turnover funcțional = pleacă cei mai valoroși — disfuncțional",
        ],
        "correct": "abcd",
    },
    # —— EPP: appraisal, BARS, erori (24–28) ——
    {
        "stem": (
            "Care distincție appraisal vs management al performanței este "
            "corectă?"
        ),
        "options": [
            "appraisal = evaluarea propriu-zisă, adesea periodică",
            "management = ciclu continuu obiective–feedback–dezvoltare",
            "sunt termeni interschimbabili pentru același formular",
            "managementul include monitorizare pe parcursul anului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care distincție BARS vs BOS este corectă?"
        ),
        "options": [
            "BARS = ancore comportamentale pentru calitate",
            "BOS = frecvența observată a comportamentelor",
            "BARS = frecvență; BOS = calitate — invers la examen",
            "ambele sunt mai structurate decât scalele grafice simple",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un evaluator dă note mici peste tot după un conflict recent, deși "
            "anul a fost bun. Eroarea probabilă și capcana de pereche:"
        ),
        "options": [
            "recență (Recency) — domină finalul perioadei",
            "primacy — domină începutul",
            "halo — impresie pozitivă globală",
            "confundarea recenței cu primacy la examen",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Care perechi eroare / efect din grila EPP sunt inversate greșit?"
        ),
        "options": [
            "halo = impresie + ridică scorurile; horns = impresie − le coboară",
            "primacy = începutul; recency = sfârșitul",
            "leniency = note prea mari; severity = note prea mici",
            "halo = note mici peste tot; horns = note mari peste tot",
        ],
        "correct": "d",
    },
    {
        "stem": (
            "Care capcane despre metode și erori în EPP trebuie respinse?"
        ),
        "options": [
            "BARS = frecvență; BOS = calitate — invers corect",
            "appraisal = managementul performanței — nu sunt identice",
            "forced distribution elimină automat halo și recența",
            "scalele grafice simple sunt mereu obiective",
        ],
        "correct": "abcd",
    },
    # —— Stres, Karasek, JD-R, challenge (29–35) ——
    {
        "stem": (
            "În modelul cerințe–control (Karasek), stresul maxim apare când "
            "cerințele (demands) sunt ridicate și controlul este scăzut."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre modelul JD-R (Job Demands–Resources) este "
            "corectă?"
        ),
        "options": [
            "cerințe ridicate fără resurse → risc de burnout",
            "resurse adecvate pot susține engagement-ul",
            "demands și resources sunt același lucru în JD-R",
            "resursele includ sprijin social, autonomie, feedback",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un proiect dificil dar cu sens și învățare este stresor de tip "
            "challenge; birocrația care blochează munca este stresor de tip "
            "hindrance."
        ),
        "options": [
            "challenge = oportunitate de creștere, poate motiva",
            "hindrance = obstacol frustrant, consumă fără câștig",
            "challenge și hindrance sunt mereu la fel la examen",
            "hindrance = ambiguitate rol, birocrație excesivă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care pereche din capcanele despre stres este formulată greșit?"
        ),
        "options": [
            "Karasek: demands mari + control mic = stres ridicat",
            "JD-R: demands = risc burnout; resources = engagement",
            "challenge = obstacol birocratic; hindrance = proiect cu sens",
            "stresorul ≠ răspunsul de stres — Lazarus",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Value fit = potrivirea valorilor persoanei cu organizația; "
            "P–E fit (person–environment fit) e mai larg — include și "
            "cerințe–abilități, nevoi–oferte."
        ),
        "options": [
            "value fit este un tip de potrivire persoană–mediu",
            "P–E fit poate include potrivirea valorică, nu doar abilități",
            "value fit și P–E fit sunt mereu sinonime — capcană",
            "potrivire slabă valorică poate crește stresul și intenția de plecare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care distincții din grila de capcane (toate capitolele PM II) sunt "
            "corecte?"
        ),
        "options": [
            "description/specification; knowledge/ability; screening/comprehensive",
            "sensibilitate/specificitate; deficiență/contaminare; task/contextual",
            "OCB/CWB; spill-over/cross-over; turnover/intenție plecare",
            "appraisal/management; BARS/BOS; halo/horns; primacy/recency; "
            "demands/resources; challenge/hindrance",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmații „capcană” trebuie respinse la un examen integrat "
            "pe Psihologia muncii II?"
        ),
        "options": [
            "job specification = lista sarcinilor zilnice",
            "sensibilitate = elimină răii; specificitate = prinde buni — invers",
            "spill-over soț–angajat = spill-over muncă–acasă la aceeași persoană",
            "Karasek: demands mari + control mare = stres maxim",
        ],
        "correct": "abcd",
    },
]
