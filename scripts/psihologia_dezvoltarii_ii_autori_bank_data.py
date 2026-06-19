"""Itemi — Psihologia dezvoltării II: autori clasici (461–490, ID 10461–10490)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

AUTORI_CLASICI_ITEMS: List[Item] = [
    # —— 461–470: Piaget, Vygotsky, behaviorism ——
    {
        "stem": (
            "La Piaget, dezvoltarea cognitivă trece prin stadii cu reorganizări "
            "calitative ale gândirii — nu doar prin acumulare de informații."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un adolescent rezolvă o problemă ipotetică („dacă gravitația ar fi "
            "mai mică…”). Stadiul piagetian ilustrat este cel mai probabil:"
        ),
        "options": [
            "operațiilor formale",
            "senzorio-motor",
            "operațiilor concrete",
            "preoperațional",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între operațiile concrete și operațiile formale "
            "sunt corecte?"
        ),
        "options": [
            "concrete: raționament legat de obiecte manipulabile; formale: abstract",
            "formale: ipoteze și variabile; concrete: conservare pe obiecte reale",
            "concrete: gândire exclusiv simbolică fără logică",
            "formale: apar la naștere, înaintea senzorio-motorului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Vygotsky explică dezvoltarea funcțiilor psihice superioare prin "
            "accentul pus pe:"
        ),
        "options": [
            "medierea socială, limbajului și culturii",
            "doar maturarea biologică internă, fără interacțiune",
            "exclusiv întărirea și pedeapsa comportamentală",
            "tipare fixe de atașament măsurate în Situația Străină",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei idei aparțin perspectivei lui L. S. Vygotsky?"
        ),
        "options": [
            "funcțiile superioare au origine socială, apoi devin interne",
            "limbajul mediatizează gândirea și învățarea",
            "zona proximală de dezvoltare și sprijinul adultului (scaffolding)",
            "stadii cognitive universale: senzorio-motor, preoperațional, formal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "La B. F. Skinner, frecvența unui comportament operant se modifică "
            "în principal prin:"
        ),
        "options": [
            "consecințele care urmează răspunsului (întăriri, pedepse, extinction)",
            "reorganizarea structurală a stadiilor piagetiene",
            "conflicte inconștiente și mecanisme de apărare",
            "predispoziția innată pentru gramatică universală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două afirmații despre condiționarea operantă skinneriană "
            "sunt corecte?"
        ),
        "options": [
            "întărirea pozitivă poate crește probabilitatea repetării comportamentului",
            "lipsa întăririi (extinction) poate reduce un comportament întărit anterior",
            "comportamentul se modifică doar prin conflicte edipiene",
            "mediul nu are rol — doar maturarea reflexelor involutive",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "J. B. Watson este asociat în principal cu ideea că:"
        ),
        "options": [
            "mediul și experiența modelează comportamentul observabil",
            "atașamentul este o nevoie biologică de securitate față de îngrijitor",
            "limbajul este produs exclusiv al unei gramatici innată",
            "criza identității versus confuzie de rol apare la adolescență",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Noam Chomsky susține că limbajul se învață exclusiv prin imitare "
            "și întărire, fără nicio componentă biologică."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care două distincții între Watson și Skinner sunt formulate corect?"
        ),
        "options": [
            "Watson: behaviorism clasic, accent pe stimuli și mediu timpuriu",
            "Skinner: condiționare operantă, control prin consecințe ale răspunsului",
            "Watson: operații formale; Skinner: zona proximală de dezvoltare",
            "ambii resping complet rolul mediului în învățare",
        ],
        "correct": "ab",
    },
    # —— 471–480: Chomsky, atașament, Harlow, Erikson ——
    {
        "stem": (
            "N. Chomsky critică abordarea skinneriană a limbajului prin ideea:"
        ),
        "options": [
            "există o predispoziție biologică / capacitate innată pentru limbaj",
            "copilul învață gramatica doar prin pedepse pentru propoziții greșite",
            "limbajul nu are structură și apare aleator",
            "atașamentul se formează doar prin hrana oferită de mamă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei contraste între Chomsky și Skinner privind limbajul "
            "sunt corecte?"
        ),
        "options": [
            "Chomsky: componentă innată; Skinner: accent pe întărire și mediu",
            "Chomsky: gramatică universală; Skinner: asociere stimul–răspuns",
            "Chomsky: limbajul nu poate fi redus la simplă condiționare",
            "Chomsky: respinge orice rol al biologiei; Skinner: innatism total",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "John Bowlby descrie atașamentul ca:"
        ),
        "options": [
            "nevoie biologică de securitate și proximitate față de îngrijitor",
            "stadiu piagetian al operațiilor formale",
            "etapă Kübler-Ross de negociere",
            "rezultat exclusiv al hranei, fără contact afectiv",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două concepte aparțin teoriei atașamentului lui Bowlby?"
        ),
        "options": [
            "figura de atașament ca bază sigură de explorare",
            "model intern de lucru despre sine și ceilalți",
            "Situația Străină ca unic instrument de măsurare a inteligenței",
            "operații concrete ca explicație a tuturor emoțiilor timpurii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Mary Ainsworth a dezvoltat procedura Situația Străină pentru a "
            "evalua în principal:"
        ),
        "options": [
            "tipul de atașament copil–îngrijitor (ex. sigur, evitant, anxios)",
            "nivelul operațiilor formale la adolescent",
            "stadiile Kübler-Ross la adulți în durere",
            "gramatica universală la vârsta prelingvistică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei descrieri corespund tipurilor de atașament identificate "
            "de Ainsworth?"
        ),
        "options": [
            "sigur: explorează, revine la îngrijitor pentru confort",
            "evitant: evită contactul la revenirea îngrijitorului",
            "anxios-rezistent: oscilație între căutare și furie la revenire",
            "dezorganizat: exclusiv stadiul senzorio-motor piagetian",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Experimentele lui H. Harlow cu maimuțe sugerează că, pentru "
            "atașament, contează mai mult:"
        ),
        "options": [
            "contactul confortabil și „mama” din pânză decât doar hrana",
            "doar cantitatea de lapte primită, indiferent de contact",
            "operațiile formale abstracte",
            "etapele Kübler-Ross în ordine fixă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două concluzii din experimentele lui Harlow sunt corecte?"
        ),
        "options": [
            "„mama” din pânză oferea confort când maimuța era speriată",
            "hrana singură nu explica complet legătura afectivă față de „mamă”",
            "contactul nu are rol — doar reflexele senzorio-motorii",
            "atașamentul se formează exclusiv după adolescență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Erik Erikson descrie dezvoltarea psihosocială doar în primii doi "
            "ani de viață, fără crize la adolescență sau bătrânețe."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Criza „identitate versus confuzie de rol” în teoria lui Erikson "
            "este asociată în principal cu:"
        ),
        "options": [
            "adolescența",
            "perioada senzorio-motoră timpurie",
            "marea bătrânețe exclusiv",
            "stadiul operațiilor concrete de la 2 ani",
        ],
        "correct": "a",
    },
    # —— 481–490: Erikson, Kübler-Ross, sinteză autori ——
    {
        "stem": (
            "Care două perechi eriksoniene „criză–temă” sunt corecte?"
        ),
        "options": [
            "încredere versus neîncredere — primul an de viață",
            "identitate versus confuzie de rol — adolescență",
            "operații formale versus senzorio-motor — vârsta școlară mică",
            "negare versus furie — stadiul atașamentului evitant",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei elemente aparțin perspectivei eriksoniene asupra "
            "dezvoltării?"
        ),
        "options": [
            "crize psihosociale pe parcursul întregii vieți",
            "identitate, roluri sociale și integrare în comunitate",
            "fiecare etapă poate influența etapele următoare",
            "dezvoltarea se termină la sfârșitul stadiului senzorio-motor",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Elisabeth Kübler-Ross este asociată în principal cu:"
        ),
        "options": [
            "descrierea reacțiilor la moarte și durere (negare, furie etc.)",
            "tipurile de atașament din Situația Străină",
            "gramatica universală și dispoziția innată pentru limbaj",
            "experimentul maimuțelor cu „mama” din sârmă versus pânză",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două afirmații despre modelul Kübler-Ross sunt corecte?"
        ),
        "options": [
            "include etape precum negare, furie, negociere, depresie, acceptare",
            "etapele nu sunt obligatorii sau fixe în ordine la toți oamenii",
            "înlocuiește complet teoria atașamentului lui Bowlby",
            "explică exclusiv dezvoltarea cognitivă formală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru perechi autor–idee sunt potrivite?"
        ),
        "options": [
            "J. Piaget — stadii cognitive (senzorio-motor, concrete, formale)",
            "L. S. Vygotsky — mediere socială, limbaj, cultură",
            "John Bowlby — atașament ca nevoie de securitate",
            "B. F. Skinner — condiționare operantă, întărire",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un copil de 8 ani conservă volumul apei la operații concrete, dar "
            "nu formulează ipoteze abstracte. Autorul cel mai relevant este:"
        ),
        "options": [
            "J. Piaget",
            "E. Kübler-Ross",
            "H. Harlow",
            "N. Chomsky",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două situații ilustrează cel mai bine ideile lui Vygotsky?"
        ),
        "options": [
            "copilul rezolvă o sarcină cu ajutorul adultului, apoi singur",
            "adultul oferă indicii verbale care devin treptat gândire internă",
            "copilul primește pedeapsă pentru fiecare greșeală de vorbire",
            "maimuța preferă „mama” din sârmă pentru că oferă lapte",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei asocieri autor–contribuție sunt corecte?"
        ),
        "options": [
            "Mary Ainsworth — Situația Străină, tipuri de atașament",
            "H. Harlow — importanța contactului și confortului în atașament",
            "J. B. Watson — behaviorism, rolul mediului în comportament",
            "Erik Erikson — doar condiționare operantă a limbajului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru autori sunt corect legați de ideea din dreapta?"
        ),
        "options": [
            "N. Chomsky — predispoziție biologică pentru limbaj",
            "Mary Ainsworth — clasificarea atașamentului în Situația Străină",
            "E. Kübler-Ross — reacții la moarte și durere",
            "Erik Erikson — crize psihosociale și identitate",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un student confundă teoriile și spune: „Skinner a descris stadiile "
            "senzorio-motor și formale, iar Piaget a inventat întărirea.” "
            "Corecția pedagogică corectă este:"
        ),
        "options": [
            "Piaget — stadii cognitive; Skinner — condiționare operantă",
            "Piaget — întărire; Skinner — zona proximală de dezvoltare",
            "ambii au descris Situația Străină",
            "Kübler-Ross a formulat gramatica universală",
        ],
        "correct": "a",
    },
]

assert len(AUTORI_CLASICI_ITEMS) == 30
