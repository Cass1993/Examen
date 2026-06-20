"""Itemi — teoriile cognitive ale învățării (40 itemi, ID 10591–10630)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

COGNITIVE_ITEMS: List[Item] = [
    # —— 1–10: fundament cognitiv, modelare, gestalt ——
    {
        "stem": (
            "Teoriile cognitive ale învățării consideră că învățarea implică prelucrarea, "
            "organizarea, stocarea și utilizarea informației, nu doar legături stimul–răspuns "
            "observabile din exterior."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare surprinde cel mai bine ideea că, în perspectiva cognitivă, "
            "cunoașterea este adaptativă?"
        ),
        "options": [
            "oamenii construiesc modele, semnificații, scheme și strategii de rezolvare",
            "informația se fixează doar prin repetare mecanică, fără reorganizare mentală",
            "învățarea depinde de recompense externe imediate, ca la Skinner",
            "creierul înregistrează pasiv stimuli, fără selectare sau interpretare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei despre învățare sunt centrale în abordarea cognitivă?"
        ),
        "options": [
            "procese mentale interne: atenție, codificare, organizare, recuperare",
            "construirea activă a sensului, nu doar fixarea automată a răspunsurilor",
            "respingerea completă a oricărei influențe a experienței anterioare",
            "echivalarea învățării cu salivarea condiționată la un stimul neutru",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Față de behaviorismul strict, teoriile cognitive pun accentul pe:"
        ),
        "options": [
            "ce se întâmplă „în mintea” cursantului: reprezentări, strategii, planificare",
            "doar frecvența comportamentelor observabile, măsurate din exterior",
            "mecanisme reflexe și asocieri S–R ca explicație unică a învățării",
            "cursantul rămâne pasiv în fața conținutului predat, fără rol activ",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele caracteristici descriu învățarea din perspectiva cognitivă?"
        ),
        "options": [
            "prelucrare activă a informației, nu doar primire pasivă",
            "organizarea cunoștințelor în structuri (scheme, modele mentale)",
            "utilizarea adaptivă a informației stocate în situații noi",
            "reducerea completă a învățării la imitație fără gândire",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Modelarea cognitivă, în didactică, presupune că:"
        ),
        "options": [
            "modelele mentale ajută la înțelegerea fenomenelor complexe",
            "modelele evoluează de la reprezentări simple la altele mai complexe",
            "modelele înlocuiesc complet nevoia de explicație și feedback",
            "un singur model simplu rămâne mereu suficient, indiferent de dificultate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Principiul gestaltist „întregul este mai mult decât suma părților” "
            "înseamnă că:"
        ),
        "options": [
            "percepția și înțelegerea depind de organizarea totală a configurației, "
            "nu doar de adunarea elementelor izolate",
            "fiecare element izolat explică singur tot comportamentul perceptiv",
            "contextul nu influențează deloc modul în care organizăm informația",
            "învățarea se reduce la asocieri elementare între stimuli separați",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei aparțin perspectivei gestaltiste asupra percepției "
            "și învățării?"
        ),
        "options": [
            "percepția este organizată, nu o sumă de senzații disparate",
            "selectivitate — atenția structurează ce devine figura vs. fundal",
            "contextul influențează modul în care interpretăm informația",
            "percepția este mereu o copiere fidelă, fără filtrare cognitivă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Teoria cognitivă tradițională (Bruner, Gagné) pune accentul pe "
            "procesele interne ale învățării, nu doar pe comportamentul observabil."
        ),
        "options": [
            "adevărat — învățarea este un proces mental activ",
            "fals — doar consecințele externe contează, ca la Skinner",
            "adevărat — procesele interne apar la condiționarea clasică a lui Pavlov, nu la cognitivism",
            "fals — Bruner respinge orice rol al reprezentărilor mentale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei sunt asociate cu teoria cognitivă tradițională?"
        ),
        "options": [
            "cursantul este agent activ al propriei învățări, nu doar receptor pasiv",
            "responsabilitatea morală pentru efort și realizări revine în parte cursantului",
            "învățarea se produce fără procese interne, doar prin imitație automată",
            "profesorul controlează singur rezultatul, indiferent de implicarea elevului",
        ],
        "correct": "ab",
    },
    # —— 11–20: procesarea informației, memorie ——
    {
        "stem": (
            "Modelul procesării informației compară creierul cu un sistem care "
            "primește, codifică, stochează și recuperează informații."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În modelul procesării informației, fluxul de bază al informației este:"
        ),
        "options": [
            "intrare → codificare → stocare → recuperare → utilizare",
            "doar stimul → răspuns, fără etape intermediare",
            "recuperare → uitare → extincție, fără codificare",
            "recompensă → pedeapsă → reflex, fără reprezentare mentală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele tipuri de memorie sunt distinse în modelul procesării "
            "informației?"
        ),
        "options": [
            "memoria senzorială — reținere foarte scurtă pentru procesare inițială",
            "memoria de scurtă durată / de lucru — capacitate limitată, manipulare activă",
            "memoria de lungă durată — stocare relativ durabilă, organizată",
            "memoria reflexă din paradigma clasică — singurul tip relevant la oameni",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre memoria senzorială sunt corecte?"
        ),
        "options": [
            "reține informația foarte scurt, suficient pentru procesarea inițială",
            "filtrează și păstrează temporar inputul din mediu înainte de codificare",
            "are capacitate nelimitată și stochează permanent toate stimuli",
            "este identică cu memoria de lungă durată ca durată și funcție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Memoria de scurtă durată (memoria de lucru) se distinge prin faptul că:"
        ),
        "options": [
            "are capacitate limitată și manipulează activ informația pentru înțelegere",
            "păstrează tot ce auzim sau vedem timp îndelungat, fără selecție",
            "funcționează doar la animale, nu la copii sau adulți",
            "nu are legătură cu rezolvarea problemelor sau înțelegerea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele funcții ale memoriei de lucru sunt esențiale în învățare?"
        ),
        "options": [
            "menținerea temporară a informației active în conștient",
            "manipularea informației pentru comparare, calcul, planificare",
            "integrarea informației noi cu reprezentări existente",
            "stocarea permanentă a tuturor experiențelor fără selecție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre memoria de lungă durată sunt corecte?"
        ),
        "options": [
            "recuperarea depinde de calitatea codificării și organizării informației",
            "legăturile cu cunoștințele anterioare facilitează stocarea și regăsirea",
            "informația dispare automat după câteva secunde, ca la memoria senzorială",
            "nu poate fi influențată de strategii de învățare sau de sens",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce poate eșua recuperarea din memoria de lungă durată, deși "
            "informația a fost „învățată”?"
        ),
        "options": [
            "codificarea a fost superficială, fără organizare sau legături de sens",
            "informația nu a fost legată de scheme sau cunoștințe anterioare",
            "memoria de lucru este prea mare și blochează automat stocarea",
            "recuperarea reușește mereu dacă informația a fost repetată mecanic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele etape descriu modelul clasic al procesării informației "
            "aplicat învățării?"
        ),
        "options": [
            "recepționarea informației din mediu (input)",
            "codificarea — transformarea în reprezentări mentale",
            "stocarea în memoria de lungă durată",
            "recuperarea și utilizarea informației la nevoie",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între procesarea informației și behaviorismul "
            "strict sunt corecte?"
        ),
        "options": [
            "PI: etape interne (atenție, codificare); behaviorism strict: accent pe S–R observabil",
            "PI: memoria ca stocare organizată; behaviorism strict: subestimează reprezentările",
            "PI: ignoră comportamentul observabil în analiza învățării",
            "behaviorismul strict explică creativitatea doar prin scheme gestaltiste",
        ],
        "correct": "ab",
    },
    # —— 21–30: cognitiv-social, evaluare, multimedia ——
    {
        "stem": (
            "Teoria cognitiv-socială a învățării include, pe lângă procesarea "
            "informației, elemente precum:"
        ),
        "options": [
            "autoreglarea, controlul emoțional și monitorizarea propriului progres",
            "doar reflexele necondiționate, fără reprezentări mentale",
            "întărirea externă, ca la Skinner, ca mecanism principal",
            "respingerea învățării observaționale ca mecanism cognitiv-social",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele componente sunt recunoscute în abordarea cognitiv-socială "
            "a învățării?"
        ),
        "options": [
            "învățare observațională și modelare (inclusiv auto-modelare)",
            "autoeficacitate — credința în propria capacitate de acțiune",
            "autoreglarea — planificare, monitorizare, ajustare a strategiilor",
            "doar condiționarea clasică a emoțiilor, fără cogniție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Teoria evaluării cognitive susține că emoțiile și evaluarea subiectivă "
            "a situației influențează direct procesarea informației în învățare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dintre următoarele consecințe ale evaluării cognitive asupra învățării sunt "
            "formulate corect?"
        ),
        "options": [
            "emoțiile pot facilita procesarea când situația e percepută ca provocare",
            "emoțiile pot bloca învățarea când situația e percepută ca amenințare",
            "evaluarea cognitivă ignoră dimensiunea afectivă a învățării",
            "doar recompensele externe contează, indiferent de interpretarea situației",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Evaluarea cognitivă a unei situații de învățare se referie la:"
        ),
        "options": [
            "modul în care persoana interpretează semnificația evenimentului pentru sine",
            "judecata despre dacă situația e relevantă, controlabilă sau amenințătoare",
            "doar măsurarea obiectivă a timpului de reacție, fără sens subiectiv",
            "reflexul necondiționat produs de stimulul necondiționat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele legături între emoție și învățare sunt centrale în teoria "
            "evaluării cognitive?"
        ),
        "options": [
            "interpretarea situației precede sau însoțește răspunsul emoțional",
            "emoția poate canaliza atenția spre informații relevante sau o poate reduce",
            "starea emoțională influențează motivația și persistența la sarcină",
            "emoția funcționează doar la condiționarea operantă, nu la învățarea școlară",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Conform teoriei învățării multimedia (Mayer), de ce contează distincția "
            "între canale verbal și vizual?"
        ),
        "options": [
            "informația verbală și cea vizuală pot fi procesate pe canale parțial distincte",
            "eficiența depinde de gestionarea memoriei de lucru și a încărcării cognitive",
            "prezentarea simultană a oricărei cantități de text și imagini e mereu optimă",
            "canalul vizual procesează limbajul scris, fără imagini sau diagrame",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Încărcarea cognitivă excesivă în lecțiile multimedia apare cel mai "
            "probabil când:"
        ),
        "options": [
            "memoria de lucru este depășită de informații irelevante sau prezentate haotic",
            "elevul primește prea multe elemente de procesat simultan, fără organizare",
            "elevul înțelege profund materialul și îl leagă de cunoștințe anterioare",
            "profesorul se bazează pe expunere orală, fără suport vizual sau grafic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele tipuri de prelucrare descriu modelul triarhic al învățării "
            "multimedia (Mayer)?"
        ),
        "options": [
            "prelucrare intrinsecă — efort orientat spre înțelegerea esenței materialului",
            "prelucrare extrinsecă — efort irosit pe elemente care nu ajută învățarea",
            "prelucrare generativă — organizarea și integrarea informației cu ce știi deja",
            "prelucrare reflexă — salivarea condiționată la stimulul condiționat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între prelucrarea extrinsecă și cea generativă "
            "sunt corecte?"
        ),
        "options": [
            "extrinsecă: încărcare inutilă (fonturi, animații distragătoare); "
            "generativă: construirea de legături și sens",
            "generativă: integrarea informației noi; extrinsecă: consum de resurse "
            "fără contribuție la înțelegere",
            "extrinsecă și generativă sunt mereu identice ca efect asupra învățării",
            "generativă presupune memorare mecanică fără organizare",
        ],
        "correct": "ab",
    },
    # —— 31–40: prelucrare generativă, rolul profesorului, sinteză ——
    {
        "stem": (
            "Prelucrarea generativă în învățarea multimedia presupune că elevul:"
        ),
        "options": [
            "organizează activ informația și o integrează în cunoștințe existente",
            "construiește reprezentări coerente, nu doar repetă mecanic enunțuri",
            "evită orice efort cognitiv, delegând totul profesorului",
            "memorează cuvânt cu cuvânt textul de pe slide, fără înțelegere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele recomandări pentru profesor derivă din perspectiva cognitivă "
            "a învățării (procesare + multimedia)?"
        ),
        "options": [
            "ajută elevul să înțeleagă structura și sensul materialului",
            "facilitează organizarea informației (scheme, exemple, conexiuni)",
            "reduce încărcarea extrinsecă (claritate, relevanță, fără distrageri)",
            "stimulează prelucrarea generativă (întrebări, integrare, aplicare)",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Concluzia cognitivă pentru practica didactică este că profesorul ar trebui "
            "să ajute elevul să înțeleagă și să organizeze informația, nu să memorizeze "
            "mecanic fără sens."
        ),
        "options": [
            "adevărat — sensul și organizarea susțin stocarea durabilă",
            "fals — memorarea mecanică e singura cale validă de învățare",
            "adevărat — aplicarea organizării mentale e limitată la ciclul primar",
            "fals — procesele interne nu contează în evaluarea școlară",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele roluri ale profesorului sunt susținute de teoriile cognitive "
            "ale învățării?"
        ),
        "options": [
            "organizator al experienței de învățare — structură, claritate, progresie",
            "facilitator al înțelegerii — exemple, feedback, strategii",
            "sprijin pentru autoreglare — încurajarea monitorizării și ajustării",
            "sursă unică de adevăr — elevul receptează pasiv conținutul fără procesare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care distincție între gestaltism și asociaționism este formulată corect?"
        ),
        "options": [
            "gestalt: percepția ca întreg organizat; asociaționism: legături între "
            "elemente separate",
            "gestalt: contextul structurează sensul; asociaționism: accent pe contiguitate",
            "gestalt: respinge orice organizare perceptivă",
            "asociaționism: întregul e mereu mai mult decât părțile, ca la gestalt",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între memoria de lucru și memoria de lungă durată "
            "sunt corecte?"
        ),
        "options": [
            "lucru: capacitate limitată, durată scurtă; lungă durată: stocare extinsă",
            "lucru: manipulare activă; lungă durată: depozit organizat pentru recuperare",
            "lucru: stochează permanent toate cursurile; lungă durată: dispare în secunde",
            "nu există diferențe funcționale între cele două tipuri de memorie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru a reduce prelucrarea extrinsecă într-o lecție multimedia, profesorul "
            "poate:"
        ),
        "options": [
            "elimina elementele decorative care nu susțin obiectivul lecției",
            "alinia textul și imaginea astfel încât elevul să nu caute inutil conexiuni",
            "adăuga simultan mai multe animații și fonturi diferite pe același slide",
            "citi integral un text lung identic cu cel de pe ecran, fără selecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei explică de ce schemele și cunoștințele anterioare "
            "facilitează învățarea?"
        ),
        "options": [
            "oferă structuri în care informația nouă poate fi integrată",
            "activarea lor la începutul lecției pregătește codificarea în memoria de lungă durată",
            "blochează permanent orice informație care nu e identică cu ce știm deja",
            "funcționează doar la condiționarea clasică, nu la învățarea școlară",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele idei despre legătura dintre cunoștințe anterioare și "
            "codificare sunt corecte?"
        ),
        "options": [
            "informația legată de scheme existente se stochează mai ușor în memoria de lungă durată",
            "activarea cunoștințelor anterioare la începutul lecției pregătește codificarea",
            "cunoștințele anterioare blochează mereu orice informație nouă",
            "codificarea reușește independent de experiența anterioară a elevului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Sinteza teoriilor cognitive: învățarea este un proces complex, adaptiv, "
            "mediat de procese interne, memorie și semnificație — nu doar formare "
            "de obiceiuri observabile."
        ),
        "tf": True,
        "correct_tf": True,
    },
]

assert len(COGNITIVE_ITEMS) == 40
