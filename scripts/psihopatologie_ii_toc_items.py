"""Itemi — Psihopatologie II: tulburarea obsesiv-compulsivă."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

TOC_ITEMS: List[Item] = [
    # —— Obsesii și compulsii (1–10) ——
    {
        "stem": "Tulburarea obsesiv-compulsivă este definită prin prezența:",
        "options": [
            "obsesiilor și/sau compulsiilor",
            "episoadelor de elație și grandiozitate",
            "fricii de spații publice, fără ritualuri",
            "halucinațiilor auditive persistente",
        ],
        "correct": "a",
    },
    {
        "stem": "În tulburarea obsesiv-compulsivă, obsesiile sunt:",
        "options": [
            "gânduri, impulsuri sau imagini intruzive și recurente",
            "percepute ca deranjante și incontrolabile",
            "comportamente repetitive vizibile din afară",
            "preferințe estetice pentru ordine și simetrie",
        ],
        "correct": "ab",
    },
    {
        "stem": "Obsesiile frecvente în tulburarea obsesiv-compulsivă includ:",
        "options": [
            "teamă de contaminare",
            "gânduri agresive, accidentale sau sexuale nedorite",
            "îndoială și indecizie patologică",
            "planificarea realistă a activităților zilnice",
        ],
        "correct": "abc",
    },
    {
        "stem": "În tulburarea obsesiv-compulsivă, compulsiile sunt:",
        "options": [
            "comportamente repetitive sau ritualuri mentale",
            "executate pentru a reduce anxietatea sau a preveni un rău",
            "simțite ca necesare, deși excesive sau iraționale",
            "activități plăcute, făcute din proprie inițiativă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Exemple de compulsii în tulburarea obsesiv-compulsivă:",
        "options": [
            "verificare repetată (uși, aragaz, fapte)",
            "spălare sau curățare excesivă",
            "numărare, ordonare sau ritualuri mentale",
            "evitarea gândurilor intruzive, fără ritual",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un pacient cu tulburare obsesiv-compulsivă verifică de 30 de ori încuietoarea, "
            "crezând că altfel va avea loc un accident. Compulsia urmărește:"
        ),
        "options": [
            "prevenirea unui eveniment catastrofal imaginar",
            "reducerea anxietății generate de îndoială",
            "plăcerea de a ordona obiectele",
            "confirmarea unei amintiri reale incomplete",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ritualurile din tulburarea obsesiv-compulsivă pot deveni:",
        "options": [
            "rigide și consumatoare de timp",
            "atât de lungi încât afectează munca sau relațiile",
            "scurte și flexibile, fără suferință",
            "absente la persoanele cu doar obsesii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Persoana cu tulburare obsesiv-compulsivă poate recunoaște că ritualurile sunt excesive, dar:"
        ),
        "options": [
            "simte că trebuie să le execute oricum",
            "crede că previn un dezastru, deși legătura este nerealistă",
            "nu are niciodată conștientizarea excesului",
            "nu resimte anxietate dacă nu le execută",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În tulburarea obsesiv-compulsivă, obsesiile sunt gânduri intruzive percepute "
            "ca incontrolabile, nu simple preferințe."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În tulburarea obsesiv-compulsivă, compulsiile sunt întotdeauna vizibile "
            "și nu pot fi ritualuri mentale."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Diagnostic și prevalență (11–16) ——
    {
        "stem": (
            "Diagnosticul tulburării obsesiv-compulsive presupune că obsesiile sau compulsiile:"
        ),
        "options": [
            "produc suferință marcată sau afectare funcțională",
            "consumă mult timp (de exemplu, peste o oră pe zi)",
            "nu sunt explicate mai bine de altă tulburare sau substanță",
            "apar doar în contextul consumului de alcool",
        ],
        "correct": "abc",
    },
    {
        "stem": "Debutul tulburării obsesiv-compulsive este adesea:",
        "options": [
            "gradual",
            "în adolescență sau la începutul vârstei adulte",
            "obligatoriu după vârsta de 60 de ani",
            "brusc, după orice stres minor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Prevalența pe parcursul vieții pentru tulburarea obsesiv-compulsivă este estimată la:"
        ),
        "options": [
            "aproximativ 2–3%",
            "sub 0,1% în toate populațiile",
            "peste 20% la adulți",
            "identică cu cea a schizofreniei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Simptomele tulburării obsesiv-compulsive nu trebuie atribuite în principal:"
        ),
        "options": [
            "efectelor substanțelor sau medicației",
            "unei alte tulburări mentale (de exemplu, tulburare de spectru autist)",
            "unei afecțiuni medicale generale",
            "obsesiilor și compulsiilor care definesc tulburarea",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În tulburarea obsesiv-compulsivă, persoana poate crede că ritualul previne un dezastru, dar:"
        ),
        "options": [
            "legătura cu evenimentul este nerealistă sau excesivă",
            "convingerea persistă în ciuda lipsei de dovezi",
            "ritualul este întotdeauna logic și proporțional",
            "anxietatea nu scade niciodată după ritual",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea obsesiv-compulsivă afectează aproximativ 2–3% din populație "
            "pe parcursul vieții."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Tulburări asociate (17–20) ——
    {
        "stem": "Tulburarea dismorfică corporală se caracterizează prin:",
        "options": [
            "preocupare excesivă pentru defecte percepute ale aspectului fizic",
            "verificare în oglindă sau căutare de reasigurări",
            "smulgerea compulsivă a părului",
            "dificultatea de a arunca obiecte din locuință",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea de acumulare (tezaurizare) compulsivă implică:",
        "options": [
            "dificultate de a arunca obiecte, indiferent de valoare",
            "aglomerarea severă a locuinței la unii pacienți",
            "ritualuri de spălare pentru contaminare",
            "gânduri sexuale intruzive nedorite",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tricotilomania și dermatilomania sunt frecvent asociate cu tulburarea "
            "obsesiv-compulsivă prin:"
        ),
        "options": [
            "comportamente repetitive legate de păr sau piele",
            "dificultatea de a opri actul, cu daune vizibile",
            "obsesii de contaminare ca singur simptom",
            "apartenența la spectrul tulburărilor legate de controlul impulsurilor",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care perechi tulburare–caracteristică sunt corecte?",
        "options": [
            "tulburarea dismorfică corporală — defect perceput al aspectului",
            "tulburarea de acumulare — dificultate de a arunca obiecte",
            "tricotilomania — smulgerea compulsivă a părului",
            "tulburarea obsesiv-compulsivă — delir persecutoriu persistent",
        ],
        "correct": "abc",
    },
    # —— Etiologie și constructe cognitive (21–26) ——
    {
        "stem": "Etiologia tulburării obsesiv-compulsive include factori:",
        "options": [
            "biologici (de exemplu, circuite fronto-striatale)",
            "cognitivi și comportamentali",
            "genetici, cu contribuție din studii pe gemeni",
            "exclusiv psihodinamici, fără bază biologică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Responsabilitatea exagerată în tulburarea obsesiv-compulsivă presupune:"
        ),
        "options": [
            "convingerea că trebuie să prevină rezultate negative",
            "sentimentul că are putere morală peste evenimente improbabile",
            "absența oricărei vinovății după ritual",
            "acceptarea limitelor reale ale controlului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Fuziunea gând–acțiune în tulburarea obsesiv-compulsivă înseamnă:"
        ),
        "options": [
            "ideea că a gândi ceva echivalează cu a face acțiunea",
            "convingere morală sau magică legată de gânduri intruzive",
            "capacitatea de a distinge clar gândul de fapt",
            "absența oricărei reacții emoționale la gânduri",
        ],
        "correct": "ab",
    },
    {
        "stem": "Contaminarea psihică în tulburarea obsesiv-compulsivă se referă la:",
        "options": [
            "sentiment de murdărie fără contact fizic contaminant",
            "asociere cu rușine, vinovăție sau amintiri aversive",
            "spălarea mâinilor după atingerea unui obiect",
            "frică realistă de bacterii dovedite în laborator",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Supresia activă a gândurilor nedorite în tulburarea obsesiv-compulsivă poate:"
        ),
        "options": [
            "crește frecvența gândurilor (efect de rebound)",
            "întări asocierea cu emoții negative",
            "elimina definitiv obsesiile fără ritual",
            "reduce anxietatea pe termen lung, garantat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Deficitele de memorie în tulburarea obsesiv-compulsivă pot include:",
        "options": [
            "încredere scăzută în validitatea amintirilor",
            "dificultate de a diferenția acțiunea reală de cea imaginată",
            "susținerea verificării repetate („am încuiat ușa?”)",
            "memorie perfectă care exclude orice îndoială",
        ],
        "correct": "abc",
    },
    # —— Tratament și capcane (27–30) ——
    {
        "stem": "Tratamentul de primă linie pentru tulburarea obsesiv-compulsivă include:",
        "options": [
            "terapia cognitiv-comportamentală cu expunere și prevenirea răspunsului",
            "inhibitori selectivi ai recaptării serotoninei",
            "psihanaliză clasică ca singură intervenție obligatorie",
            "restructurare cognitivă a convingerilor despre responsabilitate",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Expunerea cu prevenirea răspunsului, în tratamentul tulburării "
            "obsesiv-compulsive, presupune:"
        ),
        "options": [
            "confruntare treptată cu factorii declanșatori",
            "blocarea ritualurilor până când anxietatea scade",
            "confirmarea ritualurilor pentru a reduce stresul",
            "infirmarea treptată a convingerilor catastrofice",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un pacient cu tulburare obsesiv-compulsivă oprește ritualul „când simt că e complet”, "
            "deși anxietatea rămâne ridicată. Aceasta ilustrează:"
        ),
        "options": [
            "regula de încheiere legată de stare afectivă, nu de criteriu obiectiv",
            "perseverența comportamentală care menține tulburarea",
            "succesul expunerii fără disconfort",
            "absența responsabilității exagerate",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre tulburarea obsesiv-compulsivă sunt greșite?",
        "options": [
            "înseamnă doar ordine și perfecționism, fără suferință",
            "ritualurile reduc anxietatea pe termen scurt, dar o mențin pe termen lung",
            "inhibitorii selectivi ai serotoninei pot fi utili",
            "fuziunea gând–acțiune poate susține compulsia",
        ],
        "correct": "a",
    },
]
