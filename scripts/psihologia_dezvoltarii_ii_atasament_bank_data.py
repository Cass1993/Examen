"""Itemi — Psihologia dezvoltării II: emoții și atașament (itemi 211–240, ID 10211–10240)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ATASAMENT_ITEMS: List[Item] = [
    # —— 211–218: emoții timpurii, anxietate separare, Bowlby ——
    {
        "stem": (
            "Emoțiile timpurii (bucurie, furie, frică, tristețe, surpriză, dezgust) "
            "sunt inițial mai apropiate de reflexe, apoi devin treptat socializate "
            "prin interacțiunea cu adultul."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care emoții de bază apar în primii ani și se socializează treptat?"
        ),
        "options": [
            "bucurie, furie, frică, tristețe",
            "surpriză și dezgust",
            "emoții exclusiv abstracte, fără componentă corporală",
            "emoții care apar doar după operațiile formale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Anxietatea de separare se referă la:"
        ),
        "options": [
            "teamă sau neliniște când figura de atașament lipsește",
            "reacție normală în anumite perioade, cu intensitate variabilă",
            "capacitatea de a rezolva probleme ipotetico-deductive",
            "absența oricărei reacții la plecarea îngrijitorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Separarea prelungită de figura de atașament, fără sprijin, poate contribui la:"
        ),
        "options": [
            "dificultăți emoționale și de reglare ulterioare",
            "consolidarea imediată a independenței fără cost emoțional",
            "absența oricărui efect — atașamentul e doar obicei",
            "operații formale abstracte la copil",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care funcție centrală are atașamentul pentru copil?"
        ),
        "options": [
            "oferă securitate emoțională",
            "se formează exclusiv după vârsta școlară",
            "nu influențează comportamentul de explorare",
            "dispare complet după primul an",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre teoria lui Bowlby este corectă?"
        ),
        "options": [
            "atașamentul e o nevoie biologică fundamentală",
            "atașamentul e un moft ce trebuie eliminat prin ignorare",
            "dispare complet după 6 luni",
            "nu motivă căutarea proximității",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care faze ale dezvoltării atașamentului sunt formulate corect?"
        ),
        "options": [
            "preatașament (0–2 luni): contact, dar atașament difuz",
            "atașament în formare (2–7 luni): preferințe crescânde",
            "atașament evident (7–24 luni): protest la separare, căutare la revenire",
            "parteneriat (după 24 luni): cooperare și negociere treptată",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Anxietatea de separare este mereu patologică și semnalează o "
            "tulburare de atașament la orice copil."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— 219–226: Ainsworth, Situația Străină ——
    {
        "stem": (
            "Care afirmație despre Situația Străină (Ainsworth) este corectă?"
        ),
        "options": [
            "evaluează atașamentul prin separări și reuniri copil–îngrijitor",
            "măsoară exclusiv greutatea corporală la naștere",
            "testează operațiile formale abstracte",
            "nu observă reacția copilului la revenirea mamei",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Copilul cu atașament securizant în Situația Străină de obicei:"
        ),
        "options": [
            "explorează mediul când mama e prezentă",
            "protestează moderat la separare",
            "se liniștește și acceptă confortul la revenirea mamei",
            "pare indiferent total și evită contactul la revenire",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Atașamentul anxios-rezistent (ambivalent) se caracterizează prin:"
        ),
        "options": [
            "anxietate mare față de separare",
            "căutare și respingere simultană a contactului la revenire",
            "dificultate de consolare chiar și când mama revine",
            "indiferență aparentă și evitarea contactului ocular",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație despre copilul cu atașament evitant în Situația Străină este corectă?"
        ),
        "options": [
            "pare indiferent la plecarea și revenirea îngrijitorului",
            "protestează intens și se liniștește imediat la revenire",
            "caută contact și respinge simultan pe mama",
            "explorează calm și se liniștește rapid la revenire",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături definesc atașamentul dezorganizat?"
        ),
        "options": [
            "comportamente contradictorii sau dezorientate la separare/reunire",
            "confuzie — apropiere și evitare fără strategie clară",
            "perfect previzibile și exclusiv securizante",
            "liniștire imediată ca la tipul securizant",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei tipuri de atașament identificate de Ainsworth sunt recunoscute în literatura clasică?"
        ),
        "options": [
            "securizant",
            "anxios-rezistent (ambivalent)",
            "evitant",
            "formal-operational",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Prezența mamei în Situația Străină permite copilului securizant "
            "să exploreze mediul — acest comportament ilustrează:"
        ),
        "options": [
            "conceptul de bază sigură din teoria atașamentului",
            "atașamentul evitant cu evitare totală a explorării",
            "stadiul operațiilor formale piagetiene",
            "absența oricărei legături între atașament și explorare",
        ],
        "correct": "a",
    },
    # —— 227–234: Harlow, tulburări, capcane ——
    {
        "stem": (
            "Care patru concluzii din experimentele lui Harlow cu maimuțe sunt corecte?"
        ),
        "options": [
            "contactul și confortul sunt esențiale pentru atașament",
            "hrana singură nu explică legătura afectivă copil–îngrijitor",
            "„mama” din materiale moi poate fi preferată chiar dacă nu oferă lapte",
            "preferința afectivă nu se reduce la alimentație",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care două factori de risc pot contribui la tulburări de atașament?"
        ),
        "options": [
            "abandon, separări bruște sau prelungite",
            "neglijare emoțională, abuz sau instituționalizare timpurie",
            "prezența constantă sensibilă a unui îngrijitor responsiv",
            "răspuns predictibil la nevoile emoționale ale copilului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două distincții separă atașamentul evitant de cel anxios-rezistent?"
        ),
        "options": [
            "evitant: reacții aparent reduse; ambivalent: anxietate mare vizibilă",
            "evitant: evită contactul; ambivalent: caută și respinge simultan",
            "evitant: protest intens ușor de liniștit; ambivalent: indiferență totală",
            "ambele tipuri sunt identice ca manifestare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două descrieri se aplică fazei de preatașament (0–2 luni)?"
        ),
        "options": [
            "reacționează la oameni, dar legătura e difuză, nespecifică unei persoane",
            "nu protestează încă diferențiat la o anumită figură",
            "cooperează verbal în parteneriat cu adultul",
            "preferința clară pentru o singură figură e deja consolidată",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre faza de parteneriat în atașament este corectă?"
        ),
        "options": [
            "presupune negociere și cooperare mai activă cu îngrijitorul",
            "dispariția completă a anxietății de separare la toți copiii",
            "cooperare verbală formală ca la adolescent",
            "absența oricărei comunicări despre plecare și revenire",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Harlow a demonstrat că atașamentul depinde exclusiv de hrana "
            "furnizată de îngrijitor — confortul nu contează."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei descrieri se potrivesc fazei de atașament evident (7–24 luni)?"
        ),
        "options": [
            "protest la separarea de figura preferată",
            "căutare activă și bucurie la revenire",
            "anxietate de separare frecventă în această perioadă",
            "absența oricărei preferințe pentru o anumită persoană",
        ],
        "correct": "abc",
    },
    # —— 235–240: sinteză ——
    {
        "stem": (
            "Care două roluri are adultul în socializarea emoțiilor timpurii?"
        ),
        "options": [
            "etichetează și modelează răspunsuri emoționale (ex. „ești trist”)",
            "răspunde sensibil la semnalele copilului",
            "elimină complet orice expresie emoțională prin ignorare",
            "ignoră semnalele emoționale pentru a crește independența",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care comportament în Situația Străină sugerează cel mai clar "
            "atașament anxios-rezistent, nu evitant?"
        ),
        "options": [
            "protest puternic la plecarea mamei și dificultate de consolare la revenire",
            "indiferență aparentă și evitarea contactului la revenire",
            "căutare a mamei combinat cu împingere sau refuz al îmbrățișării",
            "explorare calmă când mama e prezentă, apoi liniștire rapidă la revenire",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Care două asocieri teoretician–contribuție în atașament sunt corecte?"
        ),
        "options": [
            "Bowlby — teoria atașamentului ca nevoie fundamentală",
            "Ainsworth — Situația Străină și tipurile de atașament",
            "Skinner — condiționarea operantă a limbajului",
            "Piaget — stadiul senzorio-motor exclusiv",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două situații pot contribui la tulburări de atașament?"
        ),
        "options": [
            "instituționalizare timpurie cu îngrijitori schimbători",
            "neglijare cronică sau abuz",
            "răspuns constant și sensibil la nevoile emoționale",
            "prezența stabilă a unei figuri responsive",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații integrează corect emoțiile timpurii și atașamentul?"
        ),
        "options": [
            "emoțiile de bază se socializează în relația cu îngrijitorul",
            "atașamentul securizant oferă baza pentru explorare",
            "anxietatea de separare poate fi normală în anumite etape",
            "atașamentul e irelevant pentru dezvoltarea emoțională",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care trei comportamente pot apărea la copilul dezorganizat la revenirea îngrijitorului?"
        ),
        "options": [
            "comportamente contradictorii — se apropie și se oprește brusc",
            "confuzie, înghețare sau gesturi dezorientate",
            "reacții imprevizibile fără strategie clară de căutare a confortului",
            "liniștire imediată și explorare calmă ca la securizant",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru idei definesc conceptul de „bază sigură”?"
        ),
        "options": [
            "oferă confort și securitate din care copilul poate explora",
            "rămâne punct de referință la care copilul se întoarce",
            "răspunde predictibil la nevoile emoționale (în caz securizant)",
            "susține explorarea mediului când figura e prezentă",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "La naștere și în primele săptămâni, expresiile emoționale ale "
            "copilului sunt în principal:"
        ),
        "options": [
            "reflexe și răspunsuri biologice care se socializează ulterior",
            "emoții abstracte reglate prin operații formale",
            "complet absente până la primul cuvânt",
            "identice ca reglare cu ale adultului",
        ],
        "correct": "a",
    },
]

assert len(ATASAMENT_ITEMS) == 30
