"""Itemi — Statistică II (90 itemi, ID 10961–11050)."""

from __future__ import annotations

from typing import Any, Dict, List

from scripts.statistica_ii_scales_sampling_bank_data import SCALES_SAMPLING_ITEMS

Item = Dict[str, Any]

STATISTICA_II_ITEMS: List[Item] = [
    # —— 1–10: rolul statisticii, dificultăți, metoda științifică ——
    {
        "stem": (
            "Statistica este un instrument al metodei științifice, nu o metodă de "
            "cunoaștere în sine."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Ce înseamnă, în psihologie, că statistica este un instrument al metodei "
            "științifice?"
        ),
        "options": [
            "oferă proceduri pentru a organiza datele empirice și a trage concluzii "
            "justificate, în cadrul unei investigații mai largi",
            "înlocuiește observația și formularea ipotezelor, devenind singura cale "
            "de cunoaștere validă",
            "se aplică numai după ce teoria este deja demonstrată, fără rol în "
            "planificarea cercetării",
            "reprezintă o metodă filozofică alternativă la empirism, independentă de "
            "datele colectate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele descriu dificultăți reale în raportarea la "
            "statistică în psihologie?"
        ),
        "options": [
            "statisticofobia: teamă sau evitare a procedurilor cantitative",
            "naivitate statistică: folosirea testelor fără înțelegerea presupunerilor "
            "și a limitelor lor",
            "epatantul statistic: preferința pentru metode sofisticate, chiar când "
            "problema nu le cere",
            "calculul mediei aritmetice ca singură formă acceptată de prezentare a "
            "datelor în orice raport",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele etape aparțin logicii metodei științifice "
            "prezentate în curs?"
        ),
        "options": [
            "observația fenomenului sau a unei regularități",
            "formularea unei ipoteze explicative sau predictivă",
            "colectarea de date empirice relevante pentru ipoteză",
            "tratarea ipotezei ca demonstrată înainte de analiza datelor",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Variabilele observate se caracterizează prin faptul că:"
        ),
        "options": [
            "pot fi înregistrate sau măsurate direct în studiu",
            "sunt inferate indirect din mai mulți indicatori",
            "reprezintă întotdeauna constructe teoretice abstracte",
            "nu pot fi cuantificate în nicio formă numerică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele sunt exemple de variabile observate într-un "
            "experiment psihologic?"
        ),
        "options": [
            "timpul de reacție la un stimul prezentat pe ecran",
            "răspunsul bifat la un item din chestionar",
            "inteligența ca scor la test — indicator al unui construct latent",
            "inteligența ca aptitudine generală, definită teoretic fără test",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Variabilele latente, în sensul din curs, sunt:"
        ),
        "options": [
            "constructe teoretice care nu se observă direct",
            "estimate prin indicatori observabili (itemi, reacții, comportamente)",
            "identice cu orice variabilă numerică din baza de date",
            "măsurabile direct, fără operaționalizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Variabila independentă (VI) este, în general:"
        ),
        "options": [
            "factorul manipulat sau presupus cauză în studiu",
            "efectul pe care cercetătorul îl măsoară",
            "o variabilă care se modifică doar ca urmare a rezultatului obținut",
            "un sinonim pentru variabila dependentă în designul experimental",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele pot funcționa ca variabile independente într-un "
            "studiu?"
        ),
        "options": [
            "vârsta participanților, dacă este comparată între grupuri",
            "gradul de oboseală indus experimental",
            "tipul de exercițiu sau de instrucțiune aplicat",
            "scorul la testul de performanță obținut la final",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele descriu corect variabila dependentă (VD)?"
        ),
        "options": [
            "este efectul sau rezultatul pe care îl măsori",
            "poate fi conformismul într-o situație socială",
            "poate fi măsurată doar dacă este latentă; variabilele observate nu pot fi VD",
            "este factorul pe care îl manipulezi pentru a produce schimbare",
        ],
        "correct": "ab",
    },
    # —— 11–20: VI/VD, continue/discrete, Stevens ——
    {
        "stem": (
            "Naivitatea statistică înseamnă refuzul total de a folosi orice procedură "
            "cantitativă în cercetare."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Într-un experiment, variabila dependentă este:"
        ),
        "options": [
            "ceea ce măsori pentru a vedea dacă s-a produs efectul așteptat",
            "factorul a cărui influență vrei să o testezi",
            "același lucru cu variabila de control din orice design",
            "întotdeauna o variabilă latentă, niciodată observată direct",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele perechi variabilă–rol sunt corecte într-un "
            "experiment clasic?"
        ),
        "options": [
            "tip exercițiu (VI) → performanță la test (VD)",
            "oboseală indusă (VI) → timp de reacție (VD)",
            "conformism măsurat (VD) → vârstă manipulată (VI)",
            "performanță finală (VI) → tip de feedback primit (VD)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele variabile sunt continue?"
        ),
        "options": [
            "timpul de reacție în secunde",
            "greutatea corporală",
            "înălțimea",
            "numărul de răspunsuri corecte la un test (doar valori întregi)",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Conform lui Stevens (1946), măsurarea presupune:"
        ),
        "options": [
            "atribuirea de valori numerice sau simbolice obiectelor sau fenomenelor",
            "respectarea unor reguli de corespondență între obiect și număr/simbol",
            "demonstrarea adevărului unei teorii fără colectare de date",
            "înlocuirea observației cu interpretarea subiectivă a cercetătorului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele diferențe între variabile continue și discrete "
            "sunt corecte?"
        ),
        "options": [
            "continue: teoretic pot lua o infinitate de valori într-un interval",
            "discrete: au un număr finit sau numărabil de valori posibile",
            "discrete: pot lua orice valoare reală, ca greutatea sau timpul",
            "continue: se limitează la răspunsuri da/nu sau la categorii nominale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele exemple ilustrează variabile discrete?"
        ),
        "options": [
            "numărul de persoane din familie",
            "numărul de răspunsuri corecte la un test",
            "timpul de reacție măsurat în milisecunde",
            "scorul pe o scară de interval cu zeci posibile între valori",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Sociabilitatea, în cercetarea psihologică, este de obicei tratată ca:"
        ),
        "options": [
            "variabilă latentă, estimată prin indicatori observabili",
            "construct teoretic care necesită operaționalizare",
            "variabilă observată direct, fără itemi sau scale",
            "sinonim pentru timpul de reacție la stimul social",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între variabile observate și latente "
            "sunt corecte?"
        ),
        "options": [
            "observate: înregistrate direct; latente: inferate din indicatori",
            "inteligența măsurată prin itemi de test este o operaționalizare a unui "
            "construct latent",
            "anxietatea măsurată prin scale validată rămâne latentă, deși are scor "
            "numeric",
            "latentele se văd direct în laborator, observatele doar în chestionare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care dintre următoarele asocieri exemplu–tip de variabilă sunt corecte?"
        ),
        "options": [
            "timp de reacție → observată, continuă",
            "răspuns la item → observată",
            "anxietate (construct) → latentă",
            "tip exercițiu manipulat → independentă (în design experimental)",
        ],
        "correct": "abcd",
    },
    # —— 21–30: dificultăți, măsurare, sinteză ——
    {
        "stem": (
            "Într-un design experimental, variabila independentă este manipulată sau "
            "selectată, iar variabila dependentă este măsurată."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Statisticofobia se referă, în principal, la:"
        ),
        "options": [
            "teamă, respingere sau evitare a gândirii și procedurilor statistice",
            "utilizarea corectă a testelor după înțelegerea presupunerilor lor",
            "preferința pentru analize complexe indiferent de întrebarea de cercetare",
            "capacitatea de a interpreta rezultatele fără anxietate față de numere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele descriu epatantul statistic?"
        ),
        "options": [
            "alegerea unor metode complicate pentru impresie, nu pentru nevoia problemei",
            "raportarea unor analize inadecvate sau inutile în contextul dat",
            "refuzul oricărei proceduri cantitative din teamă de erori",
            "înțelegerea limitelor testului înainte de aplicare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele elemente apar, în ordine logică, în metoda "
            "științifică?"
        ),
        "options": [
            "observație",
            "ipoteză",
            "date empirice",
            "concluzii fondate pe analiza datelor colectate",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Regulile de măsurare la care se referă Stevens (1946) stabilesc cum "
            "se leagă numerele sau simbolurile de:"
        ),
        "options": [
            "obiecte, evenimente sau trăsături ale fenomenelor studiate",
            "preferințele personale ale cercetătorului, fără corespondență fixă",
            "ipotezele formulate înainte de observație",
            "concluziile finale, după ce analiza este terminată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele confuzii frecvente trebuie evitate?"
        ),
        "options": [
            "a confunda variabila manipulată cu cea măsurată",
            "a trata un construct latent ca și cum ar fi observat direct, fără indicatori",
            "a folosi statistica ca substitut al întrebării de cercetare și al "
            "calității datelor",
            "a operaționaliza un construct prin itemi sau reacții observabile",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre dificultățile în folosirea "
            "statisticii sunt corecte?"
        ),
        "options": [
            "statisticofobia împiedică folosirea utilă a instrumentelor cantitative",
            "naivitatea statistică poate produce concluzii greșite chiar cu software "
            "modern",
            "epatantul statistic poate complica inutil raportarea rezultatelor",
            "orice utilizare a mediei arată automat competență metodologică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Numărul de copii dintr-o familie este, de regulă, un exemplu de variabilă:"
        ),
        "options": [
            "discretă",
            "cu valori ce pot fi numărate pe unități indivizibile (ex. număr copii)",
            "continuă, pentru că poate crește gradual în timp",
            "latentă, deoarece nu se vede direct",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele perechi variabilă–tip sunt corecte?"
        ),
        "options": [
            "timp de reacție → continuă",
            "număr răspunsuri corecte → discretă",
            "cod nominal pentru gen → continuă cu origine absolută",
            "greutate → discretă, pentru că se exprimă în unități fixe",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele descrieri despre variabile și măsurare sunt "
            "corecte?"
        ),
        "options": [
            "VI: cauză sau factor manipulat; VD: efect măsurat",
            "observate: măsurabile direct; latente: inferate din indicatori",
            "continue: valori teoretic infinite într-un interval; discrete: niveluri "
            "finite sau întregi",
            "măsurarea (Stevens): atribuire de valori după reguli, nu simplă etichetare "
            "arbitrară",
        ],
        "correct": "abcd",
    },
    # —— 31–40: sinteză, capcane plauzibile ——
    {
        "stem": (
            "Statistica înlocuiește nevoia de ipoteză și de colectare a datelor "
            "empirice în cercetarea psihologică."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Anxietatea măsurată printr-un chestionar validat este, din perspectiva "
            "tipului de variabilă:"
        ),
        "options": [
            "un indicator al unui construct latent, nu măsurarea directă a "
            "„anxietății pure”",
            "o variabilă observată (scorul la itemi), care estimează un construct",
            "o variabilă independentă în orice studiu, indiferent de design",
            "o variabilă nominală fără ordine între valori",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Inteligența, în cercetarea psihometrică, este tratată frecvent ca "
            "construct latent pentru că:"
        ),
        "options": [
            "nu o observi direct, ci prin performanță la itemi sau sarcini",
            "scorul la test este un indicator operațional, nu constructul în sine",
            "orice scor numeric este automat o măsură directă a capacității cognitive",
            "nu necesită reguli de măsurare sau teorie pentru interpretare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații integrează corect rolul statisticii "
            "în metoda științifică?"
        ),
        "options": [
            "pornești de la observație și formulezi ipoteze",
            "colectezi date empirice relevante",
            "folosești statistica ca instrument de analiză, nu ca înlocuitor al "
            "gândirii teoretice",
            "tragi concluzii fără a colecta date, dacă modelul statistic e complex",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Oboseala indusă înainte de sarcină poate fi, în experiment, o variabilă:"
        ),
        "options": [
            "independentă",
            "manipulată pentru a vedea efectul asupra performanței",
            "dependentă, pentru că se măsoară la finalul testului",
            "latentă, deoarece nu poate fi cuantificată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Conformismul într-o situație de grup este un exemplu clasic de variabilă:"
        ),
        "options": [
            "dependentă, dacă o măsori ca efect al presiunii sociale",
            "observată, prin comportamentul manifest sau răspunsuri la sarcină",
            "independentă, dacă o manipulezi pentru a schimba atitudinea",
            "nominală fără posibilitate de ordonare sau frecvență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Înălțimea corporală este un exemplu de variabilă:"
        ),
        "options": [
            "continuă",
            "măsurabilă direct cu instrumente standardizate",
            "discretă cu două niveluri da/nu",
            "latentă inferată doar din autocunoștință verbală, fără indicatori",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele caracterizează corect măsurarea în sensul lui "
            "Stevens?"
        ),
        "options": [
            "implică reguli de atribuire a valorilor",
            "poate folosi numere sau simboluri",
            "leagă proprietăți ale fenomenelor de reprezentări cantitative sau "
            "codificate",
            "elimină necesitatea definirii constructului studiat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Datele empirice, în lanțul metodei științifice, servesc în principal "
            "pentru a:"
        ),
        "options": [
            "verifica sau infirma ipoteze prin informații observate sistematic",
            "susține concluzii după analiză adecvată",
            "înlocui complet etapa de observație inițială",
            "justifica orice concluzie, indiferent de calitatea designului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele perechi descriu corect relația dintre statistici "
            "și înțelegerea cercetării?"
        ),
        "options": [
            "statistica ajută la organizarea datelor, nu le înlocuiește pe cele slabe",
            "înțelegerea presupunerilor testelor reduce naivitatea statistică",
            "alegerea metodei trebuie să urmeze întrebarea de cercetare, nu impresia "
            "tehnică",
            "procedurile cantitative fac inutilă formularea ipotezelor",
        ],
        "correct": "ab",
    },
] + SCALES_SAMPLING_ITEMS

assert len(STATISTICA_II_ITEMS) == 90
