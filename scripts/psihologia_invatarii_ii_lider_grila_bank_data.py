"""Itemi — profesorul ca lider, sinteză grilă (30 itemi, ID 10931–10960)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

LIDER_GRILA_ITEMS: List[Item] = [
    # —— 1–10: lider al clasei, stiluri ——
    {
        "stem": (
            "Stilul democratic de conducere a clasei este asociat cu participare mai "
            "bună, responsabilitate și inițiativă din partea elevilor."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Profesorul ca lider al clasei deține:"
        ),
        "options": [
            "statut formal, dar și rol informal — coordonează, organizează, "
            "controlează, motivează și influențează climatul",
            "statut formal fără influență asupra climatului sau a motivației",
            "rol centrat pe evaluare, fără coordonare sau organizare",
            "autoritate limitată la transmiterea manualului, fără leadership",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele funcții aparțin rolului informal de lider al profesorului?"
        ),
        "options": [
            "motivarea elevilor și influențarea climatului clasei",
            "coordonarea activității și organizarea procesului de învățare",
            "reducerea feedbackului și a structurii activității de la începutul lecției",
            "evaluarea sumativă la final de semestru, fără rol în timpul lecției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele dimensiuni ale leadershipului didactic sunt menționate în curs?"
        ),
        "options": [
            "coordonarea și organizarea activității",
            "controlul și motivarea grupului",
            "influențarea climatului clasei",
            "transmiterea mecanică fără relație sau structură",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Stilul autoritar de conducere a clasei se caracterizează prin:"
        ),
        "options": [
            "control sever, decizii centralizate și constrângere",
            "implicarea elevilor în decizii și stimularea inițiativei",
            "control redus și libertate mare, cu risc de dezorganizare",
            "dialog deschis și responsabilitate împărțită cu elevii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele consecințe pot apărea la stilul autoritar excesiv?"
        ),
        "options": [
            "reducerea libertății și a implicării active a elevilor",
            "climat tensionat, cu participare scăzută la decizii",
            "responsabilitate crescută și inițiativă ridicată din partea elevilor",
            "comunicare deschisă și cooperare spontană în grup",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Stilul democratic de leadership didactic presupune:"
        ),
        "options": [
            "implicarea elevilor, stimularea responsabilității, inițiativei și "
            "comunicării",
            "decizii centralizate fără consultarea clasei",
            "lipsa regulilor și a obiectivelor comune",
            "control sever și constrângere pentru menținerea ordinii",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele trăsături definesc stilul democratic?"
        ),
        "options": [
            "participarea elevilor la decizii și la organizarea activității",
            "comunicare deschisă și stimularea responsabilității",
            "constrângere și decizii impuse unilateral de profesor",
            "libertate maximă fără ghidare sau obiective",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Stilul permisiv / laissez-faire este întotdeauna superior stilului "
            "democratic pentru învățarea profundă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Stilul permisiv / laissez-faire se caracterizează prin:"
        ),
        "options": [
            "control redus, libertate mare, dar risc de dezorganizare și lipsă "
            "de direcție",
            "control sever și decizii centralizate fără consultare",
            "implicare activă a elevilor în toate deciziile de curriculum",
            "structură rigidă și constrângere pentru menținerea disciplinei",
        ],
        "correct": "a",
    },
    # —— 11–20: eficiență, competențe, sinteză ——
    {
        "stem": (
            "Care dintre următoarele riscuri sunt asociate stilului permisiv / laissez-faire?"
        ),
        "options": [
            "dezorganizarea activității și lipsa unei direcții clare",
            "scăderea structurii și a obiectivelor vizibile pentru elevi",
            "supra-controlul deciziilor de către profesor",
            "participare forțată și responsabilitate impusă din exterior",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Influențarea climatului clasei este parte din rolul de lider al "
            "profesorului."
        ),
        "options": [
            "adevărat — profesorul modelează atmosfera, relațiile și motivația",
            "fals — climatul depinde în totalitate de elev, fără rolul profesorului",
            "adevărat — climatul se formează și prin reguli explicite, nu prin relație",
            "fals — leadershipul didactic se limitează la conținutul predat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele componente apar în formula eficienței profesorului din "
            "sinteza pentru grilă?"
        ),
        "options": [
            "conținut",
            "relație",
            "organizare",
            "memorare pasivă ca strategie centrală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Competența pedagogică nu se reduce la știința de carte; include și:"
        ),
        "options": [
            "relaționare, comunicare, climat, adaptare și evaluare",
            "transmiterea manualului fără adaptare la clasă",
            "cunoașterea materiei, fără proceduri didactice sau feedback",
            "evaluarea sumativă la final de an, fără formativă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele elemente aparțin competenței pedagogice, pe lângă "
            "cunoașterea conținutului?"
        ),
        "options": [
            "adaptarea didactică la nevoile și nivelul elevilor",
            "organizarea și evaluarea procesului de învățare",
            "memorarea pasivă ca metodă principală",
            "evitarea comunicării pentru a menține autoritatea",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele componente definesc eficiența profesorului în sinteza "
            "pentru grilă?"
        ),
        "options": [
            "conținut",
            "relație",
            "organizare",
            "adaptare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Predarea indirectă și nivelul conceptual înalt al profesorului sunt "
            "asociate cu învățare mai activă și mai profundă."
        ),
        "options": [
            "adevărat — elevul gândește, participă, descoperă cu sprijin",
            "fals — nivelul înalt presupune transmitere pasivă",
            "adevărat — predarea indirectă exclude structura și obiectivele",
            "fals — asocierea apare la stil autoritar, nu la indirectă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele roluri ale profesorului eficient sunt formulate corect?"
        ),
        "options": [
            "specialist în domeniu și organizator al activității",
            "model și facilitator al dezvoltării elevului",
            "receptor pasiv al feedbackului, fără adaptare",
            "evaluator sumativ, fără rol de motivare sau facilitare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Profesorul eficient este specialist, organizator, model și facilitator "
            "al dezvoltării elevului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dintre următoarele afirmații din sinteza pentru grilă sunt corecte?"
        ),
        "options": [
            "predarea indirectă și nivelul conceptual înalt sunt asociate cu "
            "învățare mai activă și profundă",
            "competența pedagogică include relaționare, comunicare, climat, "
            "adaptare și evaluare",
            "profesorul eficient este specialist, organizator, model și facilitator",
            "eficiența profesorului include conținut, relație, organizare, adaptare, "
            "comunicare și motivație",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele tipuri de competență trebuie diferențiate la grilă?"
        ),
        "options": [
            "competență profesională / științifică — conținut",
            "competență psihopedagogică — adaptare didactică",
            "competență psihosocială — relații și climat",
            "competență administrativă — birocrație școlară ca sinonim psihosocial",
        ],
        "correct": "abc",
    },
    # —— 21–30: grilă, capcane, sinteză ——
    {
        "stem": (
            "Competența profesională / științifică se referă în principal la:"
        ),
        "options": [
            "cunoașterea solidă a conținutului predat",
            "adaptarea metodelor la nevoile emoționale ale clasei",
            "construirea relațiilor și a climatului pozitiv",
            "organizarea regulilor de conduită fără predare de conținut",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele diferențe între competența psihopedagogică și cea "
            "psihosocială sunt corecte?"
        ),
        "options": [
            "psihopedagogică: adaptare didactică; psihosocială: relații și climat",
            "psihopedagogică: metode și organizare a învățării; psihosocială: "
            "comunicare și atmosferă în clasă",
            "psihopedagogică: identică cu știința de carte; psihosocială: notare",
            "psihopedagogică: birocrație; psihosocială: conținut academic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Competența psihosocială a profesorului vizează în special:"
        ),
        "options": [
            "relațiile cu elevii, comunicarea și climatul clasei",
            "structurarea logaritmică a conținutului de matematică",
            "memorarea definițiilor din manual fără adaptare",
            "evaluarea concentrată pe teste standardizate, cu relație redusă în clasă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele roluri definesc profesorul eficient în sinteza pentru grilă?"
        ),
        "options": [
            "specialist în domeniu",
            "organizator al activității",
            "model pentru elevi",
            "facilitator al dezvoltării elevului",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Deciziile centralizate și constrângerea sunt trăsături ale stilului:"
        ),
        "options": [
            "autoritar",
            "democratic",
            "permisiv / laissez-faire",
            "facilitativ indirect, cu participare largă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele beneficii sunt asociate stilului democratic de leadership?"
        ),
        "options": [
            "participare mai bună a elevilor la activitate",
            "responsabilitate și inițiativă crescute",
            "control sever și decizii impuse unilateral",
            "dezorganizare și lipsă de direcție pedagogică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Lipsa direcției pedagogice este un risc asociat stilului permisiv / "
            "laissez-faire."
        ),
        "options": [
            "adevărat — fără ghidare, activitatea poate deveni haotică",
            "fals — permisivul garantează structură și obiective clare",
            "adevărat — stilul autoritar produce lipsă de direcție",
            "fals — direcția apare automat, fără intervenția profesorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele funcții ale profesorului ca lider al clasei sunt enumerate "
            "în curs?"
        ),
        "options": [
            "coordonează și organizează activitatea",
            "controlează și motivează grupul",
            "influențează climatul clasei",
            "renunță la statutul formal de cadru didactic",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Pentru grilă, diferența rapidă între competența profesională și cea "
            "psihopedagogică este:"
        ),
        "options": [
            "profesională = conținut; psihopedagogică = adaptare didactică",
            "profesională = climat; psihopedagogică = conținut",
            "profesională = relații; psihopedagogică = birocrație",
            "profesională = motivație; psihopedagogică = memorare pasivă",
        ],
        "correct": "a",
    },
]

assert len(LIDER_GRILA_ITEMS) == 30
