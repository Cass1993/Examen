"""Itemi — Psihopatologie II: tulburarea bipolară (definiție, manie, hipomanie, I/II, ciclotimie, tratament)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

BIPOLAR_ITEMS: List[Item] = [
    # —— Definiție și episoade (1–10) ——
    {
        "stem": "Tulburarea bipolară este definită, în principal, ca o tulburare a:",
        "options": [
            "dispoziției, cu episoade depresive și maniacale sau hipomaniacale",
            "anxietății generalizate, cu atacuri de panică recurente",
            "personalității, cu instabilitate cronică a relațiilor",
            "atenției, cu hiperactivitate și impulsivitate încă din copilărie",
        ],
        "correct": "a",
    },
    {
        "stem": "În tulburarea bipolară, cursul tipic include:",
        "options": [
            "alternanța între episoade de dispoziție scăzută și episoade de dispoziție crescută",
            "o dispoziție constant scăzută, fără perioade de exaltare",
            "simptome anxioase permanente, fără variații ciclice",
            "episoade psihotice izolate, fără componentă afectivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Episodul maniacal se caracterizează prin:",
        "options": [
            "dispoziție euforică, expansivă sau iritabilă, cu energie crescută",
            "lentoare psihomotorie, anhedonie și pierderea energiei",
            "frică intensă de spații aglomerate, fără modificare a dispoziției",
            "preocupări obsesive recurente, fără elație sau iritabilitate",
        ],
        "correct": "a",
    },
    {
        "stem": "Care simptome apar frecvent în manie?",
        "options": [
            "vorbire accelerată și fugă de idei",
            "distractibilitate crescută",
            "nevoie redusă de somn, fără oboseală resimțită",
            "retragere socială și inhibiție motorie marcată",
        ],
        "correct": "abc",
    },
    {
        "stem": "În episodul maniacal pot apărea:",
        "options": [
            "grandiozitate și comportament impulsiv",
            "investirea excesivă a activităților cu risc ridicat",
            "idei de ruina, vinovăție și demnitate scăzută",
            "agitație psihomotorie sau planuri de acțiune excesive",
        ],
        "correct": "abd",
    },
    {
        "stem": "Durata minimă a unui episod maniacal, în criteriile DSM-5, este de:",
        "options": [
            "aproximativ o săptămână (sau spitalizare)",
            "24 de ore",
            "minimum 6 luni",
            "două săptămâni, în toate cazurile",
        ],
        "correct": "a",
    },
    {
        "stem": "Episodul depresiv major în cadrul tulburării bipolare include, de regulă:",
        "options": [
            "dispoziție depresivă sau pierderea interesului",
            "modificări ale somnului, apetitului sau energiei",
            "sentimente de inutilitate sau dificultăți de concentrare",
            "grandiozitate, elație și nevoie scăzută de somn",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tulburarea bipolară are o componentă etiologică importantă:",
        "options": [
            "genetică și neurobiologică",
            "exclusiv psihodinamică, fără bază biologică",
            "determinată doar de stresul din ultima lună",
            "legată doar de stilul parental autoritar",
        ],
        "correct": "a",
    },
    {
        "stem": "Trecerea rapidă de la dispoziție scăzută la dispoziție crescută, în cursul tulburării bipolare, este descrisă ca:",
        "options": [
            "alternanță între faze „low” și „high”",
            "stabilitate afectivă pe termen lung",
            "episod anxios fără modificare a dispoziției",
            "simptom obsesiv-complusiv izolat",
        ],
        "correct": "a",
    },
    {
        "stem": "Tulburarea bipolară este o tulburare a dispoziției, nu o tulburare de personalitate.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Hipomanie (11–20) ——
    {
        "stem": "Hipomania se definește ca un episod cu simptome:",
        "options": [
            "asemănătoare maniei, dar mai scurte sau mai puțin severe",
            "identice maniei, cu spitalizare obligatorie",
            "depresive, cu anhedonie și lentoare",
            "psihotice, cu halucinații și delir persistent",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de manie, hipomania se deosebește prin faptul că:",
        "options": [
            "nu produce, de regulă, deteriorare funcțională severă",
            "nu necesită spitalizare și nu include psihoză",
            "presupune întotdeauna spitalizare și delir",
            "durează obligatoriu minimum o lună",
        ],
        "correct": "ab",
    },
    {
        "stem": "Durata minimă a unui episod hipomaniacal, în criteriile DSM-5, este de:",
        "options": [
            "aproximativ patru zile consecutive",
            "o singură zi",
            "minimum două săptămâni",
            "șase luni, fără excepție",
        ],
        "correct": "a",
    },
    {
        "stem": "În hipomanie pot apărea:",
        "options": [
            "energie crescută și productivitate sporită",
            "vorbire rapidă sau planuri multe într-un timp scurt",
            "iritabilitate sau dispoziție exaltată",
            "retragere totală și incapacitate de a vorbi",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un pacient descrie o săptămână cu somn redus, idei multe și energie crescută, dar își menține jobul și relațiile. Cel mai probabil:",
        "options": [
            "episod hipomaniacal",
            "episod maniacal cu psihoză",
            "episod depresiv major",
            "tulburare de panică cu agorafobie",
        ],
        "correct": "a",
    },
    {
        "stem": "Hipomania nu este sinonimă cu fericirea normală, deoarece:",
        "options": [
            "implică modificare patologică a dispoziției și a funcționării",
            "apare ca episod distinct, cu simptome clinice clare",
            "nu presupune niciodată modificări de somn sau vorbire",
            "este identică cu entuziasmul tranzitor față de un proiect",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații descriu corect hipomania?",
        "options": [
            "poate include impulsivitate sau comportament riscant",
            "nu atinge, de regulă, severitatea maniei complete",
            "exclude orice modificare a dispoziției sau a energiei",
            "implică, în mod obișnuit, delir sau halucinații",
        ],
        "correct": "ab",
    },
    {
        "stem": "Episodul hipomaniacal diferă de episodul maniacal prin absența, de regulă, a:",
        "options": [
            "psihozei și a spitalizării necesare",
            "deteriorării funcționale severe",
            "oricărei modificări a dispoziției",
            "prezenței energiei crescute",
        ],
        "correct": "ab",
    },
    {
        "stem": "În hipomanie, somnul poate fi:",
        "options": [
            "redus, fără senzația de oboseală",
            "prelungit peste 12 ore zilnic, în mod constant",
            "absent doar dacă apare delir",
            "neschimbat în toate cazurile clinice",
        ],
        "correct": "a",
    },
    {
        "stem": "Hipomania presupune simptome asemănătoare maniei, dar fără deteriorare severă sau psihoză.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Bipolară I și II (21–32) ——
    {
        "stem": "Tulburarea bipolară tip I se diagnostichează atunci când:",
        "options": [
            "a existat cel puțin un episod maniacal",
            "pot coexista episoade depresive majore",
            "episoadele hipomaniacale pot apărea, dar nu sunt obligatorii",
            "nu a existat niciodată un episod maniacal sau hipomaniacal",
        ],
        "correct": "abc",
    },
    {
        "stem": "Elementul diagnostic esențial în tulburarea bipolară tip I este:",
        "options": [
            "prezența a cel puțin unui episod maniacal",
            "absența totală a episoadelor depresive",
            "prezența obligatorie a hipomaniei, fără manie",
            "durata minimă de doi ani cu simptome ciclice ușoare",
        ],
        "correct": "a",
    },
    {
        "stem": "Tulburarea bipolară tip II necesită:",
        "options": [
            "cel puțin un episod depresiv major",
            "cel puțin un episod hipomaniacal",
            "absența episodului maniacal în antecedente",
            "prezența obligatorie a unui episod maniacal",
        ],
        "correct": "abc",
    },
    {
        "stem": "Diferența principală între bipolară I și bipolară II constă în:",
        "options": [
            "prezența episodului maniacal în tip I, absentă în tip II",
            "prezența hipomaniei în tip II, fără manie completă",
            "absența oricărui episod depresiv în tip II",
            "obligativitatea spitalizării în tip II, nu în tip I",
        ],
        "correct": "ab",
    },
    {
        "stem": "Un pacient cu un episod depresiv major și un episod hipomaniacal în antecedente, fără manie, îndeplinește criteriile pentru:",
        "options": [
            "tulburarea bipolară tip II",
            "tulburarea bipolară tip I",
            "tulburarea ciclotimică",
            "tulburarea depresivă majoră recurentă",
        ],
        "correct": "a",
    },
    {
        "stem": "Un pacient cu spitalizare după un episod de elație, grandiozitate și insomnie severă îndeplinește criteriile pentru:",
        "options": [
            "tulburarea bipolară tip I",
            "tulburarea bipolară tip II",
            "tulburarea ciclotimică",
            "tulburarea anxioasă generalizată",
        ],
        "correct": "a",
    },
    {
        "stem": "În tulburarea bipolară tip II:",
        "options": [
            "episoadele depresive pot fi frecvente și severe",
            "episodul hipomaniacal nu echivalează cu mania",
            "episodul maniacal este criteriu diagnostic obligatoriu",
            "funcționarea poate fi afectată mai ales în depresie",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care afirmații despre tulburarea bipolară tip I sunt corecte?",
        "options": [
            "un singur episod maniacal este suficient pentru diagnostic",
            "episoadele depresive majore pot apărea, dar nu sunt obligatorii",
            "diagnosticul exclude prezența oricărei hipomanii ulterioare",
            "episodul maniacal poate impune spitalizare sau tratament intensiv",
        ],
        "correct": "abd",
    },
    {
        "stem": "Tulburarea bipolară tip II presupune cel puțin un episod depresiv major și unul hipomaniacal, fără episod maniacal.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tulburarea bipolară tip I poate fi diagnosticată și fără episoade depresive majore în antecedente.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Episodul hipomaniacal din tulburarea bipolară tip II este identic ca severitate cu episodul maniacal.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "În tulburarea bipolară tip II, absența maniei complete este un criteriu diagnostic central.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Ciclotimie (33–38) ——
    {
        "stem": "Tulburarea ciclotimică se caracterizează prin:",
        "options": [
            "minimum doi ani cu simptome hipomaniacale și depresive alternante",
            "simptome care nu ating criteriile complete de episod maniacal sau depresiv major",
            "un singur episod maniacal urmat de stabilitate pe termen lung",
            "prezența obligatorie a psihozei în cursul bolii",
        ],
        "correct": "ab",
    },
    {
        "stem": "Față de tulburarea bipolară tip II, ciclotimia:",
        "options": [
            "nu atinge severitatea episodului depresiv major",
            "nu atinge severitatea episodului maniacal complet",
            "presupune întotdeauna spitalizare după primul episod",
            "durează minimum doi ani, cu simptome fluctuante",
        ],
        "correct": "abd",
    },
    {
        "stem": "În tulburarea ciclotimică, perioadele asimptomatice:",
        "options": [
            "nu depășesc, de regulă, două luni consecutive",
            "sunt absente minimum cinci ani",
            "durează obligatoriu un an întreg",
            "apar doar după tratament cu litiu",
        ],
        "correct": "a",
    },
    {
        "stem": "Un pacient relatează doi ani cu perioade scurte de energie crescută și perioade de tristețe, fără episoade care să îndeplinească criteriile complete de manie sau depresie majoră. Diagnosticul probabil:",
        "options": [
            "tulburare ciclotimică",
            "tulburare bipolară tip I",
            "tulburare bipolară tip II",
            "tulburare de personalitate histrionică",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu corect tulburarea ciclotimică?",
        "options": [
            "implică fluctuații cronice ale dispoziției",
            "simptomele sunt mai ușoare decât în episoadele majore bipolare",
            "exclude orice simptom hipomaniac sau depresiv",
            "necesită minimum doi ani de evoluție la adult",
        ],
        "correct": "abd",
    },
    {
        "stem": "Tulburarea ciclotimică necesită minimum doi ani cu simptome, fără criterii complete de episod maniacal sau depresiv major.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Tratament și capcane (39–50) ——
    {
        "stem": "Tratamentul de primă linie în tulburarea bipolară include frecvent:",
        "options": [
            "litiu, ca stabilizator al dispoziției",
            "valproat sau carbamazepină, ca stabilizatori",
            "antipsihotice cu efect stabilizator al dispoziției",
            "antidepresive monoterapie, fără stabilizator",
        ],
        "correct": "abc",
    },
    {
        "stem": "Litiu, în tulburarea bipolară, are rolul principal de:",
        "options": [
            "stabilizare a dispoziției și prevenție a recăderilor",
            "eliminare imediată a simptomelor obsesive",
            "tratare exclusivă a anxietății de separare",
            "substituire a psihoterapiei în toate fazele",
        ],
        "correct": "a",
    },
    {
        "stem": "Antidepresivele în monoterapie la pacientul bipolar pot:",
        "options": [
            "precipita trecerea spre manie sau hipomanie",
            "accelera ciclarea dispoziției la unii pacienți",
            "înlocui stabilizatorii dispoziției în toate cazurile",
            "fi riscante fără protecție cu stabilizator",
        ],
        "correct": "abd",
    },
    {
        "stem": "Psihoterapia în tulburarea bipolară este utilă pentru:",
        "options": [
            "monitorizarea dispoziției și aderența la tratament",
            "recunoașterea semnelor timpurii ale recăderii",
            "înlocuirea medicației în episodul maniacal acut",
            "reglarea ritmului de viață și gestionarea stresului",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care medicamente aparțin categoriei stabilizatorilor dispoziției?",
        "options": [
            "litiu",
            "valproat de sodiu",
            "carbamazepină",
            "sertralină în monoterapie la bipolar neprotejat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Episodul maniacal acut poate necesita, pe lângă stabilizatori:",
        "options": [
            "antipsihotice atipice sau tipice",
            "spitalizare, dacă există risc sau agitație severă",
            "doar consiliere vocațională, fără medicație",
            "evaluare medicală și monitorizare atentă",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care perechi diagnostic–caracteristică sunt corecte?",
        "options": [
            "bipolară I — cel puțin un episod maniacal",
            "bipolară II — hipomanie, fără manie",
            "ciclotimie — doi ani, simptome sub pragul episodului major",
            "bipolară II — obligatoriu un episod maniacal",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre manie și hipomanie sunt greșite?",
        "options": [
            "hipomania presupune întotdeauna spitalizare",
            "mania poate include psihoză sau deteriorare severă",
            "ambele pot include energie crescută și vorbire rapidă",
            "hipomania este mai scurtă sau mai puțin intensă decât mania",
        ],
        "correct": "a",
    },
    {
        "stem": "Un student spune: „Bipolară II înseamnă o formă mai ușoară, deci fără risc.” Răspunsul corect:",
        "options": [
            "depresia poate fi severă; riscul de suicid persistă",
            "tip II exclude episoadele depresive majore în diagnostic",
            "tip II presupune manie completă, dar cu durată redusă",
            "tip II nu necesită tratament medicamentos în nicio situație",
        ],
        "correct": "a",
    },
    {
        "stem": "Tulburarea bipolară tip I necesită cel puțin un episod maniacal; tipul II necesită depresie majoră și hipomanie, fără manie.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Litiu este un stabilizator al dispoziției folosit în tratamentul tulburării bipolare.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tulburarea ciclotimică îndeplinește criteriile complete ale unui episod depresiv major de la debut.",
        "tf": True,
        "correct_tf": False,
    },
]
