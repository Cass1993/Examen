"""Itemi — Evaluarea performanțelor (EPP), lot Psihologia muncii II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

EPP_PERFORMANTA_ITEMS: List[Item] = [
    # —— EPP: definiție, funcții (1–8) ——
    {
        "stem": (
            "Evaluarea performanțelor la locul de muncă (EPP) este aprecierea "
            "sistematică a performanței angajaților — cu implicații pentru "
            "promovare, recompense, instruire și dezvoltare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre evaluarea performanțelor (EPP) este cea "
            "mai precisă?"
        ),
        "options": [
            "e o apreciere sistematică a modului în care lucrează angajatul",
            "informează decizii de salarizare, bonus, promovare",
            "poate orienta coaching, training și planuri de dezvoltare",
            "se limitează la numărarea pieselor produse, fără feedback",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care funcții ale evaluării performanțelor sunt corect asociate?"
        ),
        "options": [
            "salariu, bonus, promovare, uneori concediere",
            "coaching, feedback, identificarea nevoilor de training",
            "exclude orice feedback către angajat",
            "leagă performanța de recompense și decizii HR",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un manager folosește evaluarea anuală doar pentru a decide cine "
            "primește mărirea de salariu, fără discuție despre cum poate "
            "angajatul crește. Ce funcție predomină — și ce lipsește?"
        ),
        "options": [
            "predomină folosirea pentru decizii de salariu și promovare",
            "lipsește discuția despre creștere și competențe de dezvoltat",
            "predomină coaching și feedback pentru dezvoltare",
            "evaluarea nu are nicio funcție administrativă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce este importantă și funcția de dezvoltare a EPP, nu doar cea "
            "administrativă?"
        ),
        "options": [
            "feedback-ul poate îmbunătăți performanța viitoare",
            "angajatul înțelege ce comportamente sunt așteptate",
            "funcția administrativă anulează nevoia de training",
            "legătura cu planurile individuale de dezvoltare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre funcția de dezvoltare a EPP este falsă?"
        ),
        "options": [
            "EPP ar trebui să aibă doar rol administrativ, fără feedback "
            "pentru creștere",
            "feedback-ul poate ghida coaching și training",
            "funcția de dezvoltare ajută angajatul să înțeleagă așteptările",
            "planurile individuale de dezvoltare pot decurge din EPP",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care scenarii ilustrează funcția administrativă, respectiv cea "
            "de dezvoltare?"
        ),
        "options": [
            "nota determină bonusul anual",
            "discuția identifică competențe de îmbunătățit",
            "evaluarea stabilește promovarea",
            "evaluarea exclude autoevaluarea — nu e regulă generală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "EPP bine făcută leagă măsurarea performanței de decizii HR și "
            "de parcursul de dezvoltare al angajatului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Appraisal vs Management, surse (9–18) ——
    {
        "stem": (
            "Care distincție surprinde diferența dintre evaluarea performanței "
            "(Performance Appraisal) și managementul performanței "
            "(Performance Management)?"
        ),
        "options": [
            "appraisal = evaluarea propriu-zisă, adesea periodică",
            "management = sistem continuu: obiective → monitorizare → "
            "feedback → evaluare → dezvoltare",
            "appraisal înseamnă același lucru cu managementul performanței",
            "managementul performanței măsoară și dezvoltă pe tot parcursul "
            "anului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Într-o firmă, șeful stabilește obiective trimestriale, oferă "
            "feedback lunar și la finalul anului face evaluarea formală. "
            "Acest proces seamănă cel mai mult cu:"
        ),
        "options": [
            "managementul performanței (Performance Management)",
            "doar evaluarea punctuală (Performance Appraisal) fără rest",
            "analiza postului (job analysis)",
            "selecția de personal — altă etapă HR",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care surse de informație sunt folosite frecvent în evaluarea "
            "performanței?"
        ),
        "options": [
            "superiorul direct — cea mai uzuală",
            "colegii, subordonații, clienții interni sau externi",
            "autoevaluarea angajatului",
            "exclusiv testele de aptitudine de la angajare — fără observație",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Feedbackul 360° (360-degree feedback) înseamnă:"
        ),
        "options": [
            "colectarea evaluărilor din mai multe surse (șef, colegi, "
            "subordonați, uneori clienți)",
            "o imagine mai completă a comportamentului la muncă",
            "un proces mereu gratuit și simplu de administrat",
            "poate fi costisitor și necesită interpretare atentă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "De ce superiorul direct rămâne sursa cea mai folosită în EPP?"
        ),
        "options": [
            "observă direct sarcinile și rezultatele",
            "are autoritatea decizională pentru recompense",
            "este mereu obiectiv, fără erori cognitive",
            "poate integra obiectivele de echipă",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații despre autoevaluare în EPP sunt corecte?"
        ),
        "options": [
            "poate crește implicarea angajatului în reflecție",
            "trebuie combinată cu șeful, colegii sau 360° pentru echilibru",
            "singură, fără alte surse, garantează obiectivitate perfectă",
            "poate pregăti discuția de dezvoltare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmație despre feedback 360° este exagerată (deci greșită)?"
        ),
        "options": [
            "360° garantează automat obiectivitate perfectă și elimină toate "
            "erorile de evaluare",
            "360° adună perspective multiple",
            "poate fi costisitor în timp și resurse",
            "imaginea combinată poate fi mai bogată decât doar nota șefului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi sursă–avantaj/limitare sunt plauzibile?"
        ),
        "options": [
            "colegi — perspective pe colaborare; risc de favoritism reciproc",
            "subordonați — văd stilul de leadership; poate fi intimidant",
            "clienți — văd calitatea serviciului; acces mai greu",
            "superior — imun la efectul halo (Halo) — capcană",
        ],
        "correct": "abc",
    },
    # —— Metode: scale, BARS, BOS, MBO, forced, mixed (19–32) ——
    {
        "stem": (
            "Care afirmație despre scalele grafice este corectă?"
        ),
        "options": [
            "sunt ușor de administrat",
            "sunt vulnerabile la subiectivitatea evaluatorului",
            "elimină complet efectul halo (Halo) — nerealist",
            "nu folosesc ancore comportamentale — spre deosebire de BARS",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care metodă este ancorată în comportamente observabile concrete, "
            "cu descrieri pentru fiecare nivel de performanță?"
        ),
        "options": [
            "scale cu ancora comportamentală (BARS — Behaviorally Anchored "
            "Rating Scales)",
            "scale grafice simple fără ancore",
            "distribuție forțată (Forced Distribution)",
            "managementul obiectivelor (MBO — Management by Objectives)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "BOS (Behavioral Observation Scales) se concentrează pe:"
        ),
        "options": [
            "frecvența cu care apar anumite comportamente la muncă",
            "observarea și numărarea comportamentelor relevante",
            "calitatea comportamentului descris narativ — mai specific BARS",
            "obiective strategice agregate la nivel de firmă — MBO",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care distincție BARS vs BOS este corectă?"
        ),
        "options": [
            "BARS — ancore comportamentale pentru calitatea performanței",
            "BOS — frecvența observată a comportamentelor",
            "BARS și BOS sunt identice ca metodă",
            "BOS nu folosește observare, doar impresii globale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Managementul obiectivelor (MBO) evaluează performanța în funcție "
            "de:"
        ),
        "options": [
            "atingerea obiectivelor stabilite și măsurabile",
            "alinierea rezultatelor la ținte agreate",
            "impresia globală a evaluatorului fără criterii",
            "distribuția forțată a angajaților pe curba normală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații despre distribuția forțată (Forced Distribution) "
            "sunt corecte?"
        ),
        "options": [
            "evaluatorul plasează angajații în categorii prestabilite",
            "poate reduce indulgența (leniency)",
            "permite orice distribuție liberă fără constrângeri",
            "poate fi nedreaptă dacă toți performează bine",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care avantaje și riscuri sunt asociate distribuției forțate?"
        ),
        "options": [
            "reduce indulgența (leniency) — diferențiere forțată",
            "poate fi percepută ca nedreaptă dacă toți performează bine",
            "garantează automat echitate procedurală",
            "poate demotiva angajații din categoria inferioară artificial",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Metoda standard mixtă (Mixed Standard) folosește:"
        ),
        "options": [
            "exemple de comportamente bune, medii și slabe ca referință",
            "compararea angajatului cu standarde comportamentale variate",
            "doar o singură ancoră „satisfăcător” pentru toți",
            "exclusiv obiective financiare anuale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Asociază corect metoda cu esențialul ei:"
        ),
        "options": [
            "simplu, dar subiectiv",
            "ancorat în comportamente, calitate",
            "observare, frecvență comportamente",
            "evaluare după obiective",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un evaluator notează „3 peste tot” pentru toți angajații ca să "
            "evite conflicte. Problema se numește:"
        ),
        "options": [
            "tendință centrală (Central Tendency)",
            "efect halo (Halo)",
            "lenitate (Leniency)",
            "recență (Recency)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre BARS și BOS este falsă?"
        ),
        "options": [
            "BARS măsoară frecvența; BOS măsoară calitatea — invers corect",
            "BARS folosește ancore comportamentale pentru calitate",
            "BOS se bazează pe observarea frecvenței comportamentelor",
            "ambele sunt mai structurate decât scalele grafice simple",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care metodă este cea mai potrivită când vrei obiective clare "
            "trimestriale legate de vânzări sau proiecte?"
        ),
        "options": [
            "managementul obiectivelor (MBO)",
            "scale grafice simple fără ținte",
            "distribuție forțată fără criterii de performanță",
            "mixed standard — util, dar nu înlocuiește țintele MBO",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce BARS poate îmbunătăți calitatea evaluării față de scalele "
            "grafice simple?"
        ),
        "options": [
            "ancorele comportamentale reduc ambiguitatea notei",
            "evaluatorul compară cu exemple concrete, nu doar impresii",
            "elimină complet orice subiectivitate",
            "facilită discuția de feedback specifică",
        ],
        "correct": "abd",
    },
    # —— Erori de evaluare (33–48) ——
    {
        "stem": (
            "Efectul halo (Halo) apare când o impresie pozitivă globală "
            "ridică toate sub-scorurile; efectul coarne (Horns) face "
            "inversul — o impresie negativă trage totul în jos."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un șef a văzut un angajat excelent la o prezentare și îi dă note "
            "mari și la punctualitate și la raportare, deși acolo e mediocru. "
            "Eroarea probabilă:"
        ),
        "options": [
            "efect halo (Halo) — impresie pozitivă globală ridică toate scorurile",
            "efect coarne (Horns) — impresie negativă globală scade toate scorurile",
            "lenitate generală (Leniency)",
            "tendință centrală (Central Tendency)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "După o greșeală gravă, evaluatorul ignoră lunile bune anterioare "
            "și notează slab peste tot. Eroarea:"
        ),
        "options": [
            "efect coarne (Horns) — impresie negativă globală scade toate scorurile",
            "efect halo (Halo) — impresie pozitivă globală ridică toate scorurile",
            "recență (Recency)",
            "similar cu mine (Similar-to-Me)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care erori descriu indulgență excesivă, respectiv severitate "
            "excesivă?"
        ),
        "options": [
            "note sistematic prea mari",
            "note sistematic prea mici",
            "toți primiți spre mijlocul scalei",
            "contează exagerat doar începutul perioadei",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații despre tendința centrală și lenitate sunt corecte?"
        ),
        "options": [
            "tendința centrală = note spre mijloc; lenitate = note prea mari",
            "sunt erori cognitive distincte",
            "sunt mereu identice — ambele înseamnă note maxime",
            "„3 peste tot” poate indica tendință centrală",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Evaluatorul își amintește doar ultimele două săptămâni înainte de "
            "formular. Eroarea:"
        ),
        "options": [
            "recență (Recency)",
            "primacy — începutul perioadei",
            "efect halo (Halo) — impresie pozitivă globală",
            "distribuție forțată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Evaluatorul își formează opinia după primele impresii din primul "
            "lună și ignoră evoluția ulterioară. Eroarea:"
        ),
        "options": [
            "primacy (Primacy)",
            "recență (Recency)",
            "severitate (Severity)",
            "MBO",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un manager își favorizează angajații cu același stil de lucru și "
            "aceleași hobby-uri. Eroarea:"
        ),
        "options": [
            "similar cu mine (Similar-to-Me)",
            "efect halo (Halo) — impresie pozitivă globală ridică toate scorurile",
            "tendință centrală (Central Tendency)",
            "feedback 360° obligatoriu",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi eroare–efect sunt corecte?"
        ),
        "options": [
            "halo (Halo) — o impresie pozitivă globală ridică toate scorurile",
            "horns (Horns / coarne) — o impresie negativă globală scade toate scorurile",
            "recență — contează prea mult finalul perioadei",
            "primacy — contează prea mult începutul perioadei",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmații despre primacy și recency în evaluare sunt corecte?"
        ),
        "options": [
            "primacy = exagerează începutul perioadei",
            "recency = exagerează sfârșitul perioadei",
            "sunt aceeași eroare — doar ultimele săptămâni contează",
            "ambele distorsionează evaluarea anuală",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care scenarii ilustrează erori diferite de evaluare?"
        ),
        "options": [
            "toți primesc 4 din 5 indiferent de performanță",
            "un singur incident recent domină nota",
            "evaluatorul evită extreme și pune pe toți „mediu”",
            "BARS elimină automat toate erorile",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "De ce eroarea „similar cu mine” (Similar-to-Me) afectează "
            "echitatea?"
        ),
        "options": [
            "favorizează pe cei asemănători, nu neapărat pe cei mai performanți",
            "reduce diversitatea de stiluri valide la muncă",
            "crește automat performanța echipei",
            "poate subevalua angajați diferiți dar eficienți",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații despre distribuția forțată și erorile cognitive "
            "sunt corecte?"
        ),
        "options": [
            "reduce indulgența prin diferențiere forțată",
            "nu elimină halo (Halo) sau horns (Horns), recența sau similar-to-me",
            "elimină automat toate erorile cognitive",
            "halo (Halo) sau horns (Horns) pot persista în sub-criterii",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care eroare este cel mai probabilă în fiecare situație?"
        ),
        "options": [
            "prezentare strălucitoare → impresie pozitivă globală → note mari "
            "la toate criteriile",
            "conflict recent → impresie negativă globală → note mici la toate",
            "evaluatorul evită extreme și pune pe toți spre mijloc",
            "preferință pentru angajați cu același stil ca evaluatorul",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmații despre severitate și lenitate sunt corecte?"
        ),
        "options": [
            "severitate = note sistematic prea mici",
            "lenitate = note sistematic prea mari",
            "severitate = note prea mari pentru toți",
            "ambele sunt erori de tendință a evaluatorului",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un evaluator dă note foarte mici tuturor, deși echipa atinge "
            "țintele. Eroarea principală:"
        ),
        "options": [
            "severitate (Severity)",
            "lenitate (Leniency)",
            "efect halo (Halo) — impresie pozitivă globală",
            "managementul obiectivelor (MBO)",
        ],
        "correct": "a",
    },
    # —— Justiție, feedback, capcane, sinteză (49–60) ——
    {
        "stem": (
            "Care tipuri de justiție în evaluare corespund: rezultat echitabil, "
            "proces corect, respect în feedback?"
        ),
        "options": [
            "rezultat/recompense echitabile",
            "pași clari și consistenți în proces",
            "comunicare respectuoasă în feedback",
            "doar mărimea bonusului, fără respect",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care caracteristici descriu feedbackul eficient în EPP?"
        ),
        "options": [
            "comportamente concrete, nu etichete vagi",
            "aproape de momentul evenimentului",
            "descrie acțiuni, nu atacă persoana",
            "formulări vagi și globale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Angajatul acceptă mai ușor o notă medie dacă procesul a fost "
            "transparent și explicat respectuos. Ce tipuri de justiție "
            "sunt implicate?"
        ),
        "options": [
            "proces transparent și explicat",
            "comunicare respectuoasă a notei",
            "percepția echității rezultatului/recompensei",
            "doar efect halo (Halo) — nu e tip de justiție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care confuzii frecvente de examen sunt perechi corecte?"
        ),
        "options": [
            "evaluarea performanței (Appraisal) vs managementul performanței "
            "— punctual vs sistem continuu",
            "BARS — calitate ancorată în comportamente; BOS — frecvență",
            "halo (Halo) — impresie pozitivă globală ridică scorurile",
            "horns (Horns / coarne) — impresie negativă globală le scade",
            "primacy — început; recency — final",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care afirmații despre screening, deficiență și contaminare sunt "
            "corecte?"
        ),
        "options": [
            "screening/comprehensive țin de selecție, nu de EPP",
            "deficiență = lipsește din măsurare ce e relevant",
            "contaminare = intră în scor factori nerelevanți",
            "screening e o variantă de BARS",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "„Feedbackul trebuie să fie specific, obiectiv, relevant, la timp "
            "și orientat spre comportament” — care afirmație completează cel "
            "mai bine această regulă?"
        ),
        "options": [
            "„Ești prost”",
            "„La raportul din 12 martie, datele erau incomplete”",
            "„Niciodată nu ești punctual”",
            "feedback dat la un an după eveniment",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care intervenții reduc erorile de evaluare?"
        ),
        "options": [
            "training pentru evaluatori despre halo (Halo), horns (Horns), "
            "recență, lenitate",
            "BARS sau BOS pentru criterii mai clare",
            "jurnal de observații pe tot anul, nu doar ultimele săptămâni",
            "eliminarea oricărui feedback scris — agravează subiectivitatea",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un HR proiectează EPP: obiective trimestriale, BARS pe "
            "comportamente cheie, training anti-halo (Halo) și anti-horns "
            "(Horns) pentru șefi, feedback "
            "360° pentru manageri. Combinația urmărește:"
        ),
        "options": [
            "managementul performanței, nu doar formularul anual",
            "calitate și claritate a criteriilor",
            "reducerea erorilor cognitive",
            "eliminarea completă a subiectivității — nerealist",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Managementul obiectivelor (MBO) leagă evaluarea de obiective "
            "stabile și măsurabile agreate între angajat și șef."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Feedbackul 360° colectează evaluări din mai multe surse pentru "
            "o imagine mai completă a comportamentului la muncă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Justiția procedurală în EPP se referie la corectitudinea și "
            "transparența procesului de evaluare — nu la mărimea bonusului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care confuzii frecvente formează perechi corecte legate "
            "de performanță la muncă?"
        ),
        "options": [
            "performanță la sarcină (task) vs performanță contextuală",
            "comportament de cetățenie organizațională (OCB) vs "
            "comportament contraproductiv (CWB)",
            "deficiență criteriu = lipsește; contaminare = apare nerelevant",
            "evaluarea performanței (appraisal) = screening la angajare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un evaluator notează doar comportamentele observate în ultimele "
            "luni și folosește BARS cu ancore clare; șeful explică nota "
            "respectuos. Ce practici bune sunt ilustrate?"
        ),
        "options": [
            "reducerea recenței prin observație pe perioadă mai lungă",
            "BARS pentru claritate comportamentală",
            "justiție interacțională în comunicarea feedbackului",
            "groupthink obligatoriu în echipă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care distincții din capcanele de examen legate de performanță și "
            "măsurare sunt corecte?"
        ),
        "options": [
            "knowledge (cunoștințe) = ce știi; ability (abilitate) = ce poți face",
            "performanță la sarcină vs performanță contextuală (extra-rol)",
            "turnover = plecare efectivă; intenție de plecare = predictor atitudinal",
            "job description = postul; job specification = profilul persoanei (KSAO)",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care rezumat al capitolului Evaluarea performanțelor (EPP) este "
            "corect?"
        ),
        "options": [
            "EPP = apreciere sistematică; funcții administrativă și dezvoltare",
            "metode: scale, BARS, BOS, MBO, forced distribution, mixed standard",
            "erori: halo (Halo), horns (Horns), leniency, severity, central "
            "tendency, recency, primacy, similar-to-me",
            "justiția interacțională = doar mărimea bonusului",
        ],
        "correct": "abc",
    },
]
