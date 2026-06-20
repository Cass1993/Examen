"""Itemi — Psihologia învățării II (460 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

from scripts.psihologia_invatarii_ii_bandura_bank_data import BANDURA_ITEMS
from scripts.psihologia_invatarii_ii_cognitive_bank_data import COGNITIVE_ITEMS
from scripts.psihologia_invatarii_ii_atitudini_profesor_bank_data import ATITUDINI_PROFESOR_ITEMS
from scripts.psihologia_invatarii_ii_predare_stiluri_bank_data import PREDARE_STILURI_ITEMS
from scripts.psihologia_invatarii_ii_roluri_empatie_bank_data import ROLURI_EMPATIE_ITEMS
from scripts.psihologia_invatarii_ii_lider_grila_bank_data import LIDER_GRILA_ITEMS
from scripts.psihologia_invatarii_ii_diferente_grila_bank_data import DIFERENTE_GRILA_ITEMS
from scripts.psihologia_invatarii_ii_educatie_invatare_bank_data import (
    EDUCATIE_INVATARE_ITEMS,
)
from scripts.psihologia_invatarii_ii_profesor_eficient_bank_data import PROFESOR_EFICIENT_ITEMS
from scripts.psihologia_invatarii_ii_tipuri_forme_bank_data import TIPURI_FORME_ITEMS
from scripts.psihologia_invatarii_ii_umanist_bank_data import UMANIST_ITEMS
from scripts.psihologia_invatarii_ii_vark_bank_data import VARK_ITEMS

Item = Dict[str, Any]

PSIHOLOGIA_INVATARII_II_ITEMS: List[Item] = [
    # —— 1–10: idee centrală, Pavlov, Watson ——
    {
        "stem": (
            "Teoriile asociaționiste și behavioriste explică comportamentul în principal "
            "prin factori externi, legături stimul–răspuns și consecințele comportamentului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La Pavlov, asocierea repetată a unui stimul neutru cu un stimul necondiționat "
            "duce în cele din urmă la un răspuns condiționat la stimulul neutru. "
            "Secvența inițială este:"
        ),
        "options": [
            "stimul neutru + stimul necondiționat → răspuns necondiționat",
            "stimul condiționat → răspuns condiționat, fără etapă necondiționată",
            "doar răspuns operant urmat de întărire, fără asociere de stimuli",
            "reorganizare a schemei în teoria lui Piaget ca mecanism principal",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele procese descriu corect dinamica condiționării clasice a lui Pavlov?"
        ),
        "options": [
            "achiziția — formarea asocierii între SC și RC",
            "extincția — dispariția RC când SC nu mai e urmat de recompensă naturală",
            "generalizarea — reacție similară la stimuli asemănători cu SC",
            "discriminarea — diferențierea între SC și stimuli similari",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Care dintre următoarele perechi stimul–răspuns apar în condiționarea clasică după "
            "formarea asocierii?"
        ),
        "options": [
            "stimul necondiționat (SI) → răspuns necondiționat (RI)",
            "stimul condiționat (SC) → răspuns condiționat (RC)",
            "stimul neutru (SN), înainte de antrenare, nu produce RC stabil",
            "răspunsul operant modelează singur toate fazele fără stimuli",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care afirmație descrie cel mai bine poziția lui John B. Watson în psihologie?"
        ),
        "options": [
            "psihologia trebuie să studieze comportamentul observabil și rolul mediului, nu introspecția",
            "obiectul științei e introspecția și analiza experienței subiective",
            "învățarea se explică doar prin hărți cognitive și scopuri interne (Tolman)",
            "toate comportamentele se reduc la reducerea impulsurilor biologice (Hull)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Experimentul lui Watson cu „micul Albert” a ilustrat în principal "
            "condiționarea emoțională a fricii prin asociere stimul–răspuns."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dintre următoarele idei sunt asociate cu behaviorismul lui John B. Watson?"
        ),
        "options": [
            "comportamentul poate fi modelat prin condiționare și mediu",
            "emoțiile pot fi condiționate, nu doar răspunsurile motorii simple",
            "învățarea latentă și hărțile cognitive sunt concepte centrale",
            "reducerea impulsului biologic explică toate comportamentele umane",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Edward L. Thorndike formulează legea efectului astfel: răspunsurile urmate "
            "de satisfacție tind să se întărească, cele urmate de disconfort să se slăbească. "
            "Aceasta aparține:"
        ),
        "options": [
            "conexionismului lui Thorndike și învățării prin încercare și eroare",
            "condiționării clasice pure fără consecințe ale răspunsului",
            "teoriei hărților cognitive tolmaniene",
            "stadiilor operațiilor formale descrise de Piaget",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele elemente descriu învățarea descrisă de Thorndike?"
        ),
        "options": [
            "încercare și eroare în situații problemă",
            "întărirea conexiunilor utile între stimuli și răspunsuri",
            "slăbirea conexiunilor urmate de disconfort sau eșec",
            "interiorizarea complet automată a gramaticii universale innată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Thorndike și Skinner explică amândoi învățarea exclusiv prin salivarea "
            "condiționată la un stimul neutru, fără rol al consecințelor răspunsului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— 11–20: Hull, Skinner, proceduri operante ——
    {
        "stem": (
            "Clark L. Hull explică comportamentul prin reducerea impulsurilor (drive) "
            "și formarea obișnuințelor (habit) care restabilesc echilibrul biologic."
        ),
        "options": [
            "organismul acționează pentru a reduce tensiuni și nevoi biologice",
            "întărirea poate funcționa prin reducerea unui impuls activ",
            "comportamentul nu are nicio legătură cu stările fiziologice interne",
            "hărțile cognitive și scopurile explică totul fără întărire",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele concepte sunt centrale în teoria reducției impulsului (Hull)?"
        ),
        "options": [
            "drive/impuls — tensiune care motivează acțiunea",
            "habit/obișnuință — tendința consolidată a unui răspuns",
            "latent learning fără întărire vizibilă",
            "condiționare clasică a salivării la clopoțel",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "B. F. Skinner pune accentul pe relația răspuns–consecință (R–S), nu doar "
            "pe asocierea stimul–răspuns (S–R) din condiționarea clasică."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La Skinner, întărirea pozitivă și cea negativă au în comun faptul că:"
        ),
        "options": [
            "cresc probabilitatea ca un comportament operant să fie repetat",
            "adaugă mereu un stimul plăcut, indiferent de tip",
            "elimină complet nevoia de repetare a răspunsului",
            "funcționează doar la condiționarea clasică a lui Pavlov",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele consecințe pot modela un comportament operant în paradigma lui B. F. Skinner?"
        ),
        "options": [
            "întărire pozitivă — adăugarea unui stimul plăcut după răspuns",
            "întărire negativă — eliminarea unui stimul neplăcut după răspuns",
            "pedeapsa — consecință care scade probabilitatea răspunsului",
            "asimilarea în teoria lui Piaget ca singur mecanism de schimbare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între condiționarea clasică și cea operantă sunt corecte?"
        ),
        "options": [
            "clasică: asociere stimul–stimul/răspuns reflex; operantă: consecințe ale răspunsului",
            "clasică: Pavlov; operantă: Skinner",
            "operanta se aplică la animale de laborator, nu la comportamentul uman",
            "clasică: explică învățarea matematică prin asocieri de stimuli",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Condiționarea instrumentală (operantă) include proceduri precum antrenamentul "
            "prin recompensă, omisiunea, pedeapsa și evitarea. Acestea se referă la:"
        ),
        "options": [
            "modul în care consecințele modifică frecvența comportamentului",
            "doar salivarea la sunetul unui clopoțel fără hrană",
            "formarea atașamentului ca nevoie biologică bowlbyană",
            "stadiul senzorio-motor din teoria lui Piaget ca explicație a întăririi",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele tipuri de consecințe operante sunt recunoscute în literatura "
            "behavioristă (recompensă, omisiune, pedeapsă, evitare)?"
        ),
        "options": [
            "întărire pozitivă — adăugare stimul plăcut după comportament",
            "întărire negativă — eliminare stimul aversiv după comportament",
            "pedeapsă pozitivă — prezentare stimul aversiv după comportament",
            "omisiune/pedeapsă negativă — retragerea unui stimul plăcut",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre întărirea continuă versus parțială sunt corecte?"
        ),
        "options": [
            "întărirea continuă facilitează achiziția inițială a unui comportament nou",
            "programele parțiale (variabile) mențin comportamentul mai rezistent la extincție",
            "întărirea continuă produce mereu cel mai rezistent comportament pe termen lung",
            "programele variabile nu au legătură cu jocurile de noroc sau verificarea rețelelor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Programele de întărire pe raport variabil mențin comportamentul mai "
            "rezistent la extincție decât întărirea continuă."
        ),
        "options": [
            "adevărat — recompensele imprevizibile mențin răspunsul mai persistent",
            "fals — întărirea continuă produce mereu cel mai rezistent comportament",
            "adevărat — fenomenul apare la condiționarea clasică a lui Pavlov, nu la operantă",
            "fals — programele variabile nu au legătură cu jocurile de noroc",
        ],
        "correct": "a",
    },
    # —— 21–30: Tolman, programe, extincție ——
    {
        "stem": (
            "Edward C. Tolman propune că învățarea poate avea loc fără întărire imediată "
            "vizibilă și că organismul formează reprezentări cognitive ale mediului."
        ),
        "options": [
            "învățare latentă și hărți cognitive (cognitive maps)",
            "doar condiționare clasică a reflexelor fiziologice",
            "refularea freudiană ca mecanism principal",
            "centrarea preoperațională permanentă la adult",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei aparțin comportamentalismului intențional al lui Tolman?"
        ),
        "options": [
            "organismul acționează orientat spre scopuri, nu doar reactiv",
            "există variabile intermediare: anticipări, cerințe, modele operatorii",
            "învățarea latentă poate apărea fără recompensă imediată la fiecare încercare",
            "toate comportamentele se reduc la reflexe innate fără cogniție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele contraste între Tolman și behaviorismul strict al lui B. F. Skinner sunt corecte?"
        ),
        "options": [
            "Tolman: reprezentări și scopuri; Skinner strict: accent pe consecințe observabile",
            "Tolman: învățare latentă; behaviorism strict: respinge uneori procese interne",
            "Tolman: doar condiționare clasică; Skinner: doar psihanaliză",
            "ambii negă complet rolul mediului în învățare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În labirintul cu șobolanii, Tolman a arătat că animalele pot învăța ruta "
            "fără recompensă la fiecare rulare, iar performanța apare când recompensa "
            "este introdusă — fenomen numit:"
        ),
        "options": [
            "învățare latentă",
            "extincție clasică a salivării",
            "criză de identitate eriksoniană",
            "operații formale abstracte",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între extincția clasică și cea operantă sunt corecte?"
        ),
        "options": [
            "clasică: RC dispare când SC nu mai e urmat de SI",
            "operantă: comportamentul scade când întărirea încetează",
            "ambele presupun adăugarea unei pedepse corporale obligatorii",
            "extincția operantă crește probabilitatea comportamentului întărit",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între generalizare și discriminare în condiționarea "
            "clasică sunt corecte?"
        ),
        "options": [
            "generalizare: reacție similară la stimuli asemănători cu SC",
            "discriminare: răspuns diferențiat doar la SC, nu la stimuli similari",
            "generalizare: dispariția completă a oricărui răspuns",
            "discriminare: creșterea probabilității răspunsului prin recompensă operantă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un program de întărire pe interval fix (ex. salariu la două săptămâni) "
            "este asociat cu:"
        ),
        "options": [
            "recompense previzibile după trecerea unui timp stabilit",
            "recompense după un număr fix de răspunsuri, indiferent de timp",
            "recompense la intervale complet imprevizibile",
            "recompense furnizate independent de comportamentul observat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele programe de întărire parțială sunt descrise corect?"
        ),
        "options": [
            "raport fix — recompensă după un număr constant de răspunsuri",
            "raport variabil — recompensă după un număr mediu, imprevizibil de răspunsuri",
            "interval variabil — recompensă după timp mediu imprevizibil",
            "interval fix — recompensă doar la naștere, fără legătură cu comportamentul",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele exemple ilustrează întărirea pe raport variabil?"
        ),
        "options": [
            "jocuri de noroc — câștig imprevizibil după un număr variabil de încercări",
            "verificarea frecventă a rețelelor sociale — recompensă variabilă (like, mesaj)",
            "salariul fix la aceeași dată calendaristică lunar",
            "salivarea la clopoțel fără hrană — extincție clasică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi autor–contribuție sunt potrivite pentru teoriile "
            "asociaționiste/behavioriste?"
        ),
        "options": [
            "Ivan Pavlov — condiționare clasică, asociere SN–SI",
            "John B. Watson — behaviorism, mediu, condiționare emoțională",
            "B. F. Skinner — condiționare operantă, programe de întărire",
            "Edward C. Tolman — învățare latentă, hărți cognitive, scopuri",
        ],
        "correct": "abcd",
    },
    # —— 31–40: limite, sinteză, capcane ——
    {
        "stem": (
            "O limită importantă a behaviorismului strict este că explică bine "
            "comportamentele observabile, dar tinde să subestimeze:"
        ),
        "options": [
            "procesele cognitive, motivația internă și sensul subiectiv al învățării",
            "rolul consecințelor mediului în modificarea comportamentului",
            "posibilitatea condiționării prin recompense și pedepse",
            "existența unor asocieri stimul–răspuns la animale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele critici frecvente la adresa explicației behavioriste stricte "
            "sunt formulate corect?"
        ),
        "options": [
            "reducerea învățării la comportament observabil, ignorând gândirea",
            "dificultatea de a explica creativitatea lingvistică doar prin întărire",
            "subestimarea motivației intrinseci și a scopurilor personale",
            "negarea completă a oricărui rol al mediului în dezvoltare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre ce explică bine behaviorismul sunt corecte?"
        ),
        "options": [
            "modificarea frecvenței comportamentelor prin consecințe",
            "formarea unor asocieri stimul–răspuns și obiceiuri observabile",
            "toate aspectele conștiinței și sensului existențial uman",
            "dezvoltarea cognitivă formală ca reorganizare de stadii fixe",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între Hull și Skinner sunt formulate corect?"
        ),
        "options": [
            "Hull: drive și reducerea impulsului biologic",
            "Skinner: consecințe observabile și programe de întărire",
            "Hull: habit ca tendință consolidată a răspunsului",
            "ambii resping complet ideea că mediul influențează comportamentul",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un student confundă Pavlov cu Skinner și spune că „salivarea la clopoțel "
            "arată condiționare operantă”. Corecția corectă este:"
        ),
        "options": [
            "salivarea la clopoțel este exemplu clasic din experimentele lui Pavlov (S–R reflex), nu operantă",
            "Pavlov a inventat programele de întărire pe raport variabil",
            "Skinner a descris condiționarea emoțională a lui Albert",
            "Thorndike a formulat legea efectului prin experimentul cu câinele lui Pavlov",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între Thorndike și Hull sunt formulate corect?"
        ),
        "options": [
            "Thorndike: legea efectului, încercare și eroare; Hull: drive și habit",
            "Hull: reducerea impulsului biologic; Thorndike: consecințe satisfăcătoare",
            "Thorndike: învățare latentă în labirint; Hull: behaviorism strict al lui Watson",
            "ambii resping ideea că întărirea influențează comportamentul",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele mecanisme diferă clar între condiționarea clasică și cea operantă?"
        ),
        "options": [
            "clasică: reflex biologic legat de stimuli; operantă: probabilitatea răspunsului",
            "clasică: asociere între stimuli; operantă: consecințe după comportament",
            "operantă: programe de întărire; clasică: generalizare și discriminare stimul",
            "clasică: moralitate adultă; operantă: comportament la sugari",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Watson a demonstrat că frica poate fi condiționată; Skinner a arătat că "
            "frecvența unui comportament se modifică prin consecințele sale. "
            "Aceste afirmații sunt:"
        ),
        "options": [
            "corecte — ilustrează contribuții distincte ale celor doi autori",
            "false — Watson a inventat condiționarea operantă",
            "false — Skinner a condus experimentul Little Albert",
            "false — ambii au respins rolul mediului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele procese apar în condiționarea clasică a lui Pavlov?"
        ),
        "options": [
            "achiziția asocierii SC–RC",
            "extincția RC când SC nu mai e însoțit de SI",
            "generalizarea la stimuli similari",
            "discriminarea între SC și alți stimuli",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Tolman depășește behaviorismul strict prin scopuri, anticipări și "
            "reprezentări cognitive — idee centrală a comportamentalismului intențional."
        ),
        "options": [
            "organismul acționează orientat spre scopuri, nu doar reactiv la stimuli",
            "învățarea latentă arată că performanța poate apărea fără recompensă la fiecare pas",
            "toate comportamentele se reduc la reflexe salivare în experimentele lui Pavlov",
            "Skinner a formulat conceptul de hartă cognitivă în labirint",
        ],
        "correct": "a",
    },
    # —— 41–50: aplicații, sinteză finală ——
    {
        "stem": (
            "Care dintre următoarele situații ilustrează legea efectului lui Thorndike?"
        ),
        "options": [
            "copilul repetă o strategie care a dus la reușită la teme",
            "abandonarea unei tactici care a produs eșec repetat",
            "formarea hărții cognitive fără nicio recompensă în labirint",
            "salivarea reflexă la prezentarea hranei fără antrenare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pedeapsa pozitivă în paradigma operantă presupune:"
        ),
        "options": [
            "prezentarea unui stimul aversiv după comportament, pentru a-l reduce",
            "adăugarea unei recompense după comportament",
            "eliminarea unui stimul neplăcut ca recompensă",
            "dispariția comportamentului fără nicio consecință prezentată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele elemente din experimentul Little Albert sunt esențiale de reținut?"
        ),
        "options": [
            "asocierea unui stimul neutru (ex. animal) cu un stimul care produce frică",
            "generalizarea fricii la stimuli similari",
            "ideea că emoțiile pot fi condiționate, nu doar răspunsurile motorii",
            "demonstrarea operațiilor formale la vârsta școlară mică",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre omisiune și evitare în condiționarea operantă "
            "sunt corecte?"
        ),
        "options": [
            "omisiunea: retragerea unei recompense după comportament nedorit",
            "evitarea: comportament care previne apariția unui stimul aversiv",
            "omisiunea: adăugarea unei pedepse corporale obligatorii",
            "evitarea: identică cu extincția în paradigma clasică a lui Pavlov",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi autor–contribuție sunt corecte?"
        ),
        "options": [
            "Edward L. Thorndike — legea efectului, conexionism",
            "Clark L. Hull — reducerea impulsului, habit",
            "Ivan Pavlov — condiționare clasică",
            "Edward C. Tolman — comportamentalism intențional",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care dintre următoarele limite ale explicației behavioriste stricte sunt recunoscute "
            "în psihologia învățării?"
        ),
        "options": [
            "subestimează procesele cognitive și gândirea internă",
            "greu de explicat creativitatea lingvistică doar prin întărire",
            "neglijează motivația intrinsecă și sensul personal",
            "dificultate în explicarea sensului subiectiv și al scopurilor personale",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un profesor folosește recompense imprevizibile (sticker uneori, nu mereu) "
            "pentru participare — programul de întărire cel mai probabil este:"
        ),
        "options": [
            "raport variabil — menține participarea rezistentă la extincție",
            "interval fix — recompensă la fiecare oră exactă",
            "întărire continuă — sticker la fiecare răspuns",
            "condiționare clasică — asociere clopoțel–salivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei rezumă contribuția lui Skinner la psihologia învățării?"
        ),
        "options": [
            "comportamentul operant este controlat de consecințele care îl urmează",
            "programele de întărire explică menținerea și extincția comportamentelor",
            "învățarea latentă în labirint fără recompensă imediată",
            "legea efectului și puzzle-box-ul lui Thorndike",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele distincții diferențiază corect contribuțiile "
            "lui Pavlov, Watson și Skinner?"
        ),
        "options": [
            "Pavlov — condiționare clasică, reflexe fiziologice",
            "Watson — behaviorism, mediu, condiționare emoțională (Albert)",
            "Skinner — operantă, întărire, programe de recompensă",
            "toți trei — hărți cognitive și învățare latentă descrise de Tolman",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Sinteza corectă: teoriile asociaționiste și behavioriste explică învățarea "
            "prin legături stimul–răspuns și consecințe, dar au limite în explicarea "
            "cogniției complexe și a motivației intrinseci."
        ),
        "tf": True,
        "correct_tf": True,
    },
] + BANDURA_ITEMS + COGNITIVE_ITEMS + UMANIST_ITEMS + EDUCATIE_INVATARE_ITEMS + TIPURI_FORME_ITEMS + VARK_ITEMS + DIFERENTE_GRILA_ITEMS + PROFESOR_EFICIENT_ITEMS + ATITUDINI_PROFESOR_ITEMS + PREDARE_STILURI_ITEMS + ROLURI_EMPATIE_ITEMS + LIDER_GRILA_ITEMS

assert len(PSIHOLOGIA_INVATARII_II_ITEMS) == 460
