"""Itemi — diferențe rapide pentru grilă + cuvinte-cheie (40 itemi, ID 10751–10790)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

DIFERENTE_GRILA_ITEMS: List[Item] = [
    # —— 1–10: întărire, pedeapsă, stima, socială vs operantă ——
    {
        "stem": (
            "Atât întărirea pozitivă, cât și întărirea negativă au efectul de a crește "
            "probabilitatea unui comportament — diferă prin tipul de consecință aplicată."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Întărirea pozitivă, în condiționarea operantă, presupune:"
        ),
        "options": [
            "adăugarea unui stimul plăcut sau recompensă după comportament",
            "eliminarea unui stimul neplăcut după comportament",
            "aplicarea unei consecințe neplăcute care scade comportamentul",
            "întârziere a recompensei după un număr fix de răspunsuri corecte",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între întărirea pozitivă și cea negativă sunt corecte?"
        ),
        "options": [
            "pozitivă: se adaugă un stimul plăcut (ex. laudă, puncte)",
            "negativă: se elimină un stimul neplăcut (ex. încetează un zgomot deranjant)",
            "pozitivă: scade comportamentul; negativă: îl crește prin pedeapsă",
            "negativă: înseamnă critică verbală severă aplicată de profesor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pedeapsa, în abordarea skinneriană, scade frecvența comportamentului prin:"
        ),
        "options": [
            "aplicarea unei consecințe neplăcute după comportament",
            "lipsa întăririi după ce comportamentul a fost anterior recompensat",
            "adăugarea unei recompense pentru a marca un răspuns corect",
            "eliminarea unui stimul aversiv pentru a încuraja repetarea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două diferențe între pedeapsă și extincție sunt formulate corect?"
        ),
        "options": [
            "pedeapsa: consecință neplăcută activă care reduce comportamentul",
            "extincția: dispariția comportamentului când întărirea nu mai urmează",
            "extincția: aplicarea unei pedepse simțite ca injustă de elev",
            "pedeapsa: lipsa recompensei după un comportament corect",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru perechi „concept–diferență esențială” sunt corecte pentru grilă?"
        ),
        "options": [
            "întărire pozitivă vs negativă — ambele cresc comportamentul, dar una adaugă "
            "stimul plăcut, cealaltă elimină stimul neplăcut",
            "pedeapsă vs extincție — pedeapsa adaugă consecință neplăcută; extincția "
            "scade comportamentul prin lipsa întăririi",
            "stima de sine vs autoeficacitate — stima e evaluare globală; autoeficacitatea "
            "e credință legată de o sarcină anume",
            "învățare socială vs operantă — socială prin observare/modelare; operantă "
            "prin consecințele propriului comportament",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Stima de sine se referă la:"
        ),
        "options": [
            "evaluarea globală a valorii personale — „cât de bun sunt ca persoană”",
            "credința specifică că poți reuși la o sarcină anume (ex. matematică)",
            "capacitatea de a observa și imita comportamentul unui model",
            "formarea asocierii între stimul neutru și stimul necondiționat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între stima de sine și autoeficacitate (Bandura) "
            "sunt corecte?"
        ),
        "options": [
            "stima de sine: mai globală, afectiv-evaluativă",
            "autoeficacitatea: legată de o competență sau sarcină concretă",
            "autoeficacitatea: sinonimă perfectă cu stima de sine globală",
            "stima de sine: măsoară capacitatea de a imita un model filmat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea socială (Bandura) se bazează pe observare și modelare, în timp ce "
            "condiționarea operantă skinneriană pe consecințele propriului comportament."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare surprinde diferența esențială între învățarea socială și "
            "condiționarea operantă?"
        ),
        "options": [
            "socială: înveți comportamente noi urmărind modele; operantă: consecințele "
            "propriilor tale răspunsuri modifică frecvența comportamentului",
            "socială: depinde de recompensa directă imediată a observatorului; operantă: "
            "exclude imitația",
            "socială: explică reflexele necondiționate; operantă: explică hărțile cognitive",
            "socială și operantă sunt identice ca mecanism explicativ",
        ],
        "correct": "a",
    },
    # —— 11–20: formală/informală, cognitivism, behaviorism, umanism, Pavlov ——
    {
        "stem": (
            "Care două distincții între învățarea formală și cea informală sunt corecte?"
        ),
        "options": [
            "formală: instituționalizată, cu curriculum și evaluare organizată",
            "informală: spontană, din experiențe cotidiene, fără programă școlară fixă",
            "informală: presupune diplomă și examene naționale obligatorii",
            "formală: apare fără intenție pedagogică în familie sau la joacă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Cognitivismul explică învățarea în principal prin:"
        ),
        "options": [
            "procese interne — atenție, memorie, organizare, scheme mentale",
            "comportamente observabile și legături stimul–răspuns fără reprezentări",
            "reflexe necondiționate și salivarea la clopoțel",
            "ierarhia trebuințelor și autoactualizarea ca tel unic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două caracteristici definesc behaviorismul strict în psihologia "
            "învățării?"
        ),
        "options": [
            "accent pe comportament observabil și măsurabil",
            "explicare prin stimuli externi, asocieri și consecințe",
            "centrare pe procesarea informației și pe modelele mentale",
            "prioritizarea sensului personal și a relației empatic-profesor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei diferențe între cognitivism și behaviorism sunt corecte?"
        ),
        "options": [
            "cognitivism: procese interne; behaviorism strict: accent pe exterior observabil",
            "cognitivism: reprezentări și strategii; behaviorism strict: S–R și întărire",
            "cognitivism: elev activ care organizează informația; behaviorism strict: "
            "accent pe consecințe comportamentale",
            "cognitivism: respinge memoria; behaviorism: introduce scheme gestaltiste",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Umanismul în educație pune accentul pe:"
        ),
        "options": [
            "persoana întreagă, sensul, autonomia și dezvoltarea personală",
            "procesarea pasivă a informației fără dimensiune afectivă",
            "formarea reflexelor prin programe de întărire pe raport variabil",
            "hărțile cognitive și învățarea latentă în labirint",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între umanism și cognitivism sunt formulate corect?"
        ),
        "options": [
            "umanism: sens, relație, valori, dezvoltare personală; cognitivism: procesare "
            "și structuri mentale",
            "umanism: Rogers, Maslow; cognitivism: accent pe memorie, scheme, strategii",
            "umanism: respinge emoția; cognitivism: respinge gândirea",
            "umanism și cognitivism sunt identice ca orientare școlară",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "John B. Watson este asociat cu behaviorismul și cu experimentul de "
            "condiționare emoțională la „micul Albert”."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La Pavlov, după condiționare, stimulul care inițial era neutru devine:"
        ),
        "options": [
            "stimul condiționat (SC) — produce răspuns condiționat (RC)",
            "stimul necondiționat (SN) — produce reflex natural",
            "stimul discriminativ care întărește comportamentul operant",
            "reprezentarea mentală a labirintului tolmanian",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două procese aparțin condiționării clasice pavloviene?"
        ),
        "options": [
            "generalizarea — reacție similară la stimuli asemănători cu SC",
            "discriminarea — răspuns diferențiat la SC, nu la stimuli similari",
            "învățarea latentă fără recompensă vizibilă",
            "autoeficacitatea legată de o sarcină școlară anume",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Edward L. Thorndike este asociat cu:"
        ),
        "options": [
            "încercare-eroare și legea efectului — consecințele întăresc legătura S–R",
            "experimentul Bobo doll și învățarea prin modelare",
            "ierarhia trebuințelor și experiențele culminante",
            "ciclul experiențial concretă–reflecție–conceptualizare–aplicare",
        ],
        "correct": "a",
    },
    # —— 21–30: Hull, Skinner, Tolman, Bandura, Rogers ——
    {
        "stem": (
            "Clark L. Hull pune accentul pe reducerea impulsului (drive) și pe "
            "mecanisme biologice în explicarea învățării."
        ),
        "options": [
            "adevărat — învățarea reduce tensiunea drive-ului, spre obiective biologice",
            "fals — Hull a introdus hărțile cognitive și învățarea latentă",
            "adevărat — Hull a condus experimentul cu micul Albert",
            "fals — Hull este autorul teoriei facilitării rogersiene",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două concepte sunt central asociate cu B. F. Skinner?"
        ),
        "options": [
            "condiționare operantă/instrumentală",
            "întărire, pedeapsă și programe de întărire (raport, interval)",
            "învățare latentă și hărți cognitive în labirint",
            "empatie, acceptare și autenticitate în relația educațională",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei programe de întărire parțială sunt asociate cu Skinner?"
        ),
        "options": [
            "întărire pe raport fix sau variabil",
            "întărire pe interval fix sau variabil",
            "întărire continuă — recompensă la fiecare răspuns",
            "întărire vicariantă prin observarea pedepsei modelului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Edward C. Tolman este cunoscut pentru:"
        ),
        "options": [
            "învățare latentă și reprezentări cognitive (hărți) ale mediului",
            "condiționarea emoțională a fricii la micul Albert",
            "legea efectului și puzzle-box-ul",
            "modelul VARK al preferințelor de învățare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Extincția unui comportament operant presupune aplicarea unei pedepse "
            "neplăcute imediate după fiecare manifestare a comportamentului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care două concepte sunt asociate cu Albert Bandura?"
        ),
        "options": [
            "învățare prin observare, modelare și imitație",
            "determinism reciproc și autoeficacitate",
            "stimul necondiționat și răspuns condiționat pavlovian",
            "blended learning și flipped classroom",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Determinismul reciproc, la Bandura, înseamnă că:"
        ),
        "options": [
            "comportamentul, mediul și factorii personali se influențează reciproc",
            "mediul acționează într-o singură direcție asupra comportamentului",
            "personalitatea este fixă și nu modifică contextul",
            "imitarea înlocuiește gândirea și planificarea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei cuvinte-cheie aparțin cognitivismului în psihologia învățării?"
        ),
        "options": [
            "procesare a informației și memorie",
            "scheme, modele mentale, organizare",
            "modelare cognitivă și învățare multimedia",
            "autoactualizare și experiențe culminante maslowiene",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru perechi proces–autor sunt potrivite pentru condiționarea clasică "
            "pavloviană?"
        ),
        "options": [
            "stimul necondiționat (SN) — declanșează răspuns necondiționat (RN)",
            "stimul condiționat (SC) — după antrenare, produce răspuns condiționat (RC)",
            "generalizare — reacție la stimuli similari cu SC",
            "extincție — slăbirea RC când SC nu mai e urmat de recompensă naturală",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Carl R. Rogers este asociat cu:"
        ),
        "options": [
            "empatie, acceptare, autenticitate și educație centrată pe elev",
            "programe de întărire pe raport variabil",
            "hărți cognitive și scopuri tolmaniene",
            "diagrame VARK și preferințe vizuale",
        ],
        "correct": "a",
    },
    # —— 31–40: Maslow, forme, VARK, sinteză autori ——
    {
        "stem": (
            "Care trei concepte sunt asociate cu Abraham Maslow în educație?"
        ),
        "options": [
            "ierarhia trebuințelor",
            "autoactualizarea",
            "experiențe culminante",
            "legea efectului și încercare-eroare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Flipped classroom (clasă inversată) presupune:"
        ),
        "options": [
            "studiu al conținutului acasă (ex. video), iar la clasă aplicare și sprijin",
            "predare orală la clasă, fără materiale digitale pentru acasă",
            "renunțarea la activități practice în favoarea lecturii pasive",
            "evaluare standardizată fără feedback formativ",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei forme de învățare apar în sinteza cursului?"
        ),
        "options": [
            "activă — discuții, probleme, proiecte",
            "experiențială — ciclul Kolb, experiență și reflecție",
            "socială — norme și roluri prin interacțiune",
            "reflexivă pavloviană — salivare la stimul neutru",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Acronimul VARK desemnează preferințele:"
        ),
        "options": [
            "vizual, auditiv, citit/scriere, kinestezic",
            "verbal, analitic, reflexiv, cognitiv",
            "validare, aplicare, repetiție, cunoaștere",
            "vizual, afectiv, rațional, kinestezic",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În sinteza umanistă, autonomia elevului înseamnă:"
        ),
        "options": [
            "implicare activă, alegeri și asumarea direcției învățării",
            "renunțarea la feedback-ul profesorului și la structura lecției",
            "conformism față de așteptările externe ca scop principal",
            "memorarea obedientă a curriculumului fără sens personal",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două forme de învățare din clasificarea modernă includ tehnologia "
            "și adaptarea parcursului?"
        ),
        "options": [
            "personalizată — ritm, conținut și strategii ajustate elevului",
            "autoreglată — elevul își monitorizează și ajustează parcursul",
            "pavloviană clasică — asociere SN cu SC",
            "reflexivă senzorială — percepție fără procesare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Învățarea latentă și hărțile cognitive sunt asociate în principal cu:"
        ),
        "options": [
            "Edward C. Tolman",
            "Clark L. Hull",
            "Ivan P. Pavlov",
            "Carl R. Rogers",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei perechi autor–contribuție sunt corecte?"
        ),
        "options": [
            "Ivan P. Pavlov — condiționare clasică, reflexe condiționate",
            "John B. Watson — behaviorism, condiționare emoțională (Albert)",
            "B. F. Skinner — condiționare operantă, programe de întărire",
            "Abraham Maslow — legea efectului și puzzle-box",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru perechi autor–idee sunt potrivite pentru grilă?"
        ),
        "options": [
            "Edward C. Tolman — învățare latentă, hărți cognitive",
            "Albert Bandura — modelare, autoeficacitate, determinism reciproc",
            "Carl R. Rogers — facilitare, empatie, învățare semnificativă",
            "Edward L. Thorndike — legea efectului, încercare-eroare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Pentru grilă, diferența rapidă cognitivism–behaviorism se rezumă la:"
        ),
        "options": [
            "procese interne și organizare mentală vs comportament observabil și "
            "consecințe externe",
            "reflexe necondiționate vs ierarhia trebuințelor",
            "VARK vs blended learning",
            "pedeapsă vs extincție ca singure mecanisme ale învățării",
        ],
        "correct": "a",
    },
]

assert len(DIFERENTE_GRILA_ITEMS) == 40
