"""Itemi — Psihologia dezvoltării II: adolescență (321–360, ID 10321–10360)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ADOLESCENTA_ITEMS: List[Item] = [
    # —— 321–328: caracter general, teme centrale ——
    {
        "stem": (
            "Adolescența (aproximativ 14/15–18/20 ani) este o perioadă de tranziție "
            "între copilărie și adultitate, cu schimbări biologice, cognitive, "
            "emoționale, sociale și identitare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care teme sunt centrale în dezvoltarea adolescentului?"
        ),
        "options": [
            "autonomie față de familie și construirea identității",
            "apartenență la grupul de colegi și imaginea corporală",
            "valori, orientare spre viitor profesional și relații afective",
            "dispariția completă a oricărei influențe a mediului social",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tranziția spre adultate în adolescență implică simultan:"
        ),
        "options": [
            "modificări pubertare și maturare sexuală",
            "restructurări cognitive spre gândire abstractă",
            "reorganizare identitară și relațională",
            "revenirea la stadiul senzorio-motor piagetian",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "La Piaget, adolescentul se află de regulă în stadiul:"
        ),
        "options": [
            "operațiilor formale",
            "operațiilor concrete exclusiv",
            "senzorio-motor",
            "preoperațional",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Gândirea adolescentului devine:"
        ),
        "options": [
            "abstractă și ipotetico-deductivă",
            "orientată spre posibil, nu doar spre concretul imediat",
            "posibilistică — poate evalua șanse și alternative",
            "limitată la obiecte fizice prezente în fața sa",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru capacități ale operațiilor formale sunt ilustrate corect "
            "la adolescent?"
        ),
        "options": [
            "raționeze despre ipoteze și variabile abstracte",
            "gândească ce ar fi dacă…, nu doar ce este acum",
            "testeze mental variante posibile înainte de a acționa",
            "formuleze planuri și anticipări pe termen lung",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Adolescentul în stadiul formal poate rezolva doar probleme "
            "concrete — gândirea abstractă lipsește complet."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care caracteristici cognitive sunt tipice adolescenței?"
        ),
        "options": [
            "anticipare și formulare de ipoteze",
            "planificare și raționament abstract",
            "preocupări morale, filosofice sau sociale",
            "centrare exclusivă pe perceptia imediată, fără reflecție",
        ],
        "correct": "abc",
    },
    # —— 329–336: subperioade, criza de originalitate ——
    {
        "stem": (
            "Care descrieri despre subperioadele adolescenței sunt corecte?"
        ),
        "options": [
            "preadolescența: transformări biologice marcante (pubertate)",
            "adolescența propriu-zisă: identitate, conflicte, autonomie",
            "adolescența târzie: orientare spre viitor, stabilizare parțială",
            "toate trei sunt identice ca teme și vârstă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două aspecte definesc preadolescența?"
        ),
        "options": [
            "schimbări corporale și pubertate",
            "începutul maturării sexuale",
            "stabilizarea completă a identității adulte",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două elemente caracterizează criza de originalitate?"
        ),
        "options": [
            "afirmarea propriei identități prin diferențiere de adulți",
            "opoziție, idealism și nevoie de recunoaștere",
            "identificare totală fără conflict cu valorile familiei",
            "revenirea la dependența totală de părinți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care etape ale crizei de originalitate sunt descrise în curs?"
        ),
        "options": [
            "revoltă față de autoritate sau norme impuse",
            "închidere în sine, retragere temporară",
            "exaltare și afirmare a propriei originalități",
            "revenire permanentă la dependența totală de părinți",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două funcții are nevoia de apartenență la grup în adolescență?"
        ),
        "options": [
            "construirea identității prin comparație socială",
            "acceptarea și statutul în rândul colegilor",
            "dispariția oricărei influențe a peer group-ului",
            "absența oricărei influențe a mediului social",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două aspecte ale imaginii corporale sunt tipice adolescenței?"
        ),
        "options": [
            "satisfacție sau nesiguranță legată de schimbările pubertare",
            "comparare cu standarde sociale sau cu colegii",
            "indiferență totală față de aspectul fizic",
            "exclusiv senzorio-motor, fără componentă afectivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Criza de originalitate înseamnă că adolescentul nu are nicio nevoie "
            "de diferențiere sau recunoaștere — acceptă pasiv orice identitate impusă."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care două elemente descriu adolescența târzie (spre 18–20 ani)?"
        ),
        "options": [
            "orientare mai clară spre carieră sau studii",
            "stabilizare parțială a identității și valorilor",
            "absența oricărei planificări a viitorului",
            "stadiul senzorio-motor cu reflexe dominante",
        ],
        "correct": "ab",
    },
    # —— 337–344: agresivitate, gândire formală ——
    {
        "stem": (
            "Agresivitatea în adolescență poate lua forme:"
        ),
        "options": [
            "verbale — insulte, amenințări, ironie",
            "fizice — lovituri, intimidare corporală",
            "relaționale — excludere, răspândire de zvonuri",
            "exclusiv simbolice, fără componentă socială",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care factori pot favoriza agresivitatea adolescentă?"
        ),
        "options": [
            "frustrare, eșec școlar sau resimțit de statut scăzut în grup",
            "modele agresive în familie, mediu sau media",
            "apartenență la un grup care valorizează dominanța",
            "prezența exclusivă a unui mediu calm, fără conflicte",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două trăsături definesc agresivitatea relațională?"
        ),
        "options": [
            "excluderea din grup sau deteriorarea reputației",
            "manipularea relațiilor pentru a răni pe altcineva",
            "lovituri directe și confruntare fizică deschisă",
            "dispariția completă a atașamentului și a intimității",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două capacități definesc gândirea ipotetico-deductivă la adolescent?"
        ),
        "options": [
            "porni de la o ipoteză și deduce consecințe logice",
            "testa mental variante posibile înainte de acțiune",
            "opera doar cu obiecte vizibile, fără „dacă atunci”",
            "absența oricărei influențe a mediului social",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două motive explică preocupările morale la adolescent?"
        ),
        "options": [
            "gândirea formală permite reflecție asupra principiilor",
            "poate compara sisteme de valori diferite",
            "nu are încă capacitate de abstractizare",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două comportamente apar în etapa de „revoltă” a crizei de originalitate?"
        ),
        "options": [
            "respingerea regulilor sau autorității adulte",
            "manifestări de opoziție față de familie sau școală",
            "acceptare necondiționată a tuturor normelor sociale",
            "revenirea la dependența totală de părinți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Toată agresivitatea adolescentă are aceeași cauză unică — "
            "predispoziția genetică, fără rol al mediului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care patru legături explică orientarea spre viitor profesional în adolescență?"
        ),
        "options": [
            "capacitatea de planificare și anticipare",
            "explorarea identității și a competențelor",
            "influența valorilor familiale, școlare și sociale",
            "formularea unor proiecte și alternative de carieră",
        ],
        "correct": "abcd",
    },
    # —— 345–352: capcane, sinteze ——
    {
        "stem": (
            "Care două distincții între operații concrete și formale sunt corecte?"
        ),
        "options": [
            "concret: logică pe situații reale; formal: ipoteze și abstract",
            "formal: gândire despre posibil; concret: legat de obiecte prezente",
            "sunt identice la 16 ani",
            "exclusiv senzorio-motor, fără componentă afectivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două comportamente ilustrează etapa de „închidere în sine”?"
        ),
        "options": [
            "retragere temporară, jurnal intim, distanțare de familie",
            "refuz de comunicare sau izolare în cameră",
            "exaltare publică și afirmare vocală a originalității",
            "absența oricărei influențe a mediului social",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine relațiile afective în adolescență?"
        ),
        "options": [
            "contribuie la formarea identității și a intimității",
            "pot implica idealizare, dependență sau explorare",
            "sunt identice ca intensitate cu ale adultului matur",
            "stadiul senzorio-motor cu reflexe dominante",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre autonomia adolescentului este corectă?"
        ),
        "options": [
            "negocierea regulilor cu părinții, nu ruptura totală obligatorie",
            "luarea treptată a deciziilor proprii",
            "absența oricărui conflict generațional",
            "operații formale abstracte ca la adolescent",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care descriere se confundă cel mai ușor cu agresivitatea fizică?"
        ),
        "options": [
            "împingere și lovire directă în conflict",
            "excludere din grup și răspândire de zvonuri",
            "amenințare verbală și insulte",
            "distrugere simbolică a imaginii (rumoare, ignorare)",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Care afirmație despre gândirea posibilistică la adolescent este corectă?"
        ),
        "options": [
            "evaluarea mai multor variante de acțiune",
            "estimarea consecințelor probabile, nu doar certe",
            "ignorarea completă a incertitudinii",
            "revenirea la dependența totală de părinți",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre idealismul din criza de originalitate este corectă?"
        ),
        "options": [
            "standarde înalte despre lume, justiție sau societate",
            "critica ipocriziei adulte sau a normelor percepute ca injuste",
            "acceptare pasivă a oricărei autorități fără reflecție",
            "exclusiv senzorio-motor, fără componentă afectivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație explică legătura dintre pubertate și identitate?"
        ),
        "options": [
            "schimbările corporale impun redefinirea imaginii de sine",
            "compararea cu colegii influențează stima de sine",
            "identitatea e deja fixă la 10 ani și nu se mai schimbă",
            "absența oricărei influențe a mediului social",
        ],
        "correct": "a",
    },
    # —— 353–360: sinteză finală ——
    {
        "stem": (
            "Care formulare descrie cel mai bine adolescența ca perioadă?"
        ),
        "options": [
            "tranziție biopsihosocială spre adultitate",
            "operații formale și identitate în construcție",
            "teme: autonomie, apartenență, valori, viitor",
            "stadiu senzorio-motor cu reflexe dominante",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine dezbaterea adolescentului despre drepturi egale?"
        ),
        "options": [
            "gândire ipotetico-deductivă",
            "preocupare morală și abstractă",
            "centrare preoperațională pe perceptia imediată",
            "dispariția completă a atașamentului și a intimității",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre etapa de exaltare în criza de originalitate este corectă?"
        ),
        "options": [
            "manifestarea energică a propriei voci sau stil",
            "căutare de recunoaștere pentru originalitate",
            "retragere totală fără contact social",
            "stadiul senzorio-motor cu reflexe dominante",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații explică legătura dintre frustrare și agresivitate în grup?"
        ),
        "options": [
            "adolescentul resimte amenințarea identității sau a prestigiului",
            "agresivitatea poate fi folosită pentru a recâștiga control sau respect",
            "mediul nu are niciun rol — doar trăsătura genetică",
            "absența oricărei influențe a mediului social",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre formarea valorilor la adolescent este corectă?"
        ),
        "options": [
            "confruntare cu valorile familiei și ale societății",
            "explorare și alegeri proprii, nu doar imitație",
            "absența oricărei reflecții — doar condiționare",
            "revenirea la dependența totală de părinți",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care subperioadă accentuează mai mult construirea identității "
            "și conflictele decât transformările biologice pur?"
        ),
        "options": [
            "adolescența propriu-zisă",
            "preadolescența — accent pe pubertate",
            "stadiul senzorio-motor",
            "adolescența târzie — orientare spre viitor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre achizițiile cognitive și identitare la adolescent este corectă?"
        ),
        "options": [
            "gândirea abstractă permite reflecție asupra identității și valorilor",
            "planificarea viitorului necesită operații formale",
            "identitatea nu influențează deloc motivația școlară",
            "exclusiv senzorio-motor, fără componentă afectivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru formulări rezumă corect dezvoltarea adolescentului?"
        ),
        "options": [
            "integrare biologică, cognitivă formală, identitară și socială",
            "criză de originalitate cu etape de revoltă, retragere și afirmare",
            "explorare a autonomiei, valorilor și viitorului în context relațional",
            "teme centrale: apartenență, imagine corporală, orientare profesională",
        ],
        "correct": "abcd",
    },
]

assert len(ADOLESCENTA_ITEMS) == 40
