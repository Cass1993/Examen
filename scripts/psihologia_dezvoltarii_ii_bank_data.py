"""Itemi — lot examen Psihologia dezvoltării II (490 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

from scripts.psihologia_dezvoltarii_ii_metode_bank_data import METODE_CERCETARE_ITEMS

Item = Dict[str, Any]

PSIHOLOGIA_DEZVOLTARII_II_ITEMS: List[Item] = [
    # —— 1–8: Natura dezvoltării psihice ——
    {
        "stem": (
            "Dezvoltarea psihică este un proces unitar, stadial și individual: "
            "copiii trec prin etape recognoscibile, dar fiecare are ritm, viteză "
            "și durată proprii."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care patru trăsături descriu corect procesul de dezvoltare psihică?"
        ),
        "options": [
            "procesul are continuitate — schimbările se leagă de cele anterioare",
            "fiecare copil are ritm și viteză proprii de parcurgere a etapelor",
            "dezvoltarea are sens direcțional — nu este o simplă acumulare aleatoare",
            "caracter stadial, cu etape recognoscibile în dezvoltare",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un profesor observă că doi elevi de aceeași vârstă cronologice "
            "diferă mult la maturitatea emoțională și la strategiile de rezolvare "
            "a problemelor. Care explicație este cea mai potrivită din perspectiva "
            "dezvoltării psihice?"
        ),
        "options": [
            "diferențele dovedesc că dezvoltarea nu este stadială",
            "diferențele reflectă caracterul individual al ritmului de dezvoltare",
            "diferențele arată că doar ereditatea contează, nu experiența",
            "diferențele înseamnă că unul dintre elevi nu se dezvoltă deloc",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Dezvoltarea psihică înseamnă că toți copiii ajung identici la "
            "sfârșitul adolescenței, pentru că etapele sunt aceleași pentru toți."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care patru elemente aparțin ideii că dezvoltarea are „propria durată” "
            "și „propriul sens”?"
        ),
        "options": [
            "schimbările actuale pregătesc etapele următoare",
            "există o direcție generală a creșterii competențelor",
            "ritmul poate fi mai lent sau mai rapid de la un copil la altul",
            "durata etapelor este fixată biologic la aceleași luni pentru fiecare copil",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În raport cu învățarea punctuală dintr-o singură lecție, dezvoltarea "
            "psihică se deosebește prin:"
        ),
        "options": [
            "caracter global — restructurează modul de a gândi și de a relaționa",
            "caracter de durată — se construiește în timp, nu într-o clipă",
            "lipsa oricărei continuități cu experiențele anterioare",
            "imposibilitatea de a fi influențată de mediu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care pereche distinge corect „etapă” de „ritm individual”?"
        ),
        "options": [
            "etapa = tipar general recognoscibil; ritmul = viteza personală de parcurgere",
            "etapa = vârsta cronologică exactă; ritmul = același pentru toți copiii",
            "etapa și ritmul sunt sinonime în psihologia dezvoltării",
            "ritmul individual anulează existența etapelor comune",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un copil învață să coopereze la joacă, apoi să negocieze reguli, "
            "apoi să își asume perspectivele altora. Această succesiune ilustrează "
            "mai ales:"
        ),
        "options": [
            "lipsa continuității în dezvoltare",
            "caracterul stadial și direcționat al dezvoltării psihosociale",
            "faptul că mediul nu are niciun rol în schimbare",
            "identitatea perfectă între toți copiii la aceeași vârstă",
        ],
        "correct": "b",
    },
    # —— 9–16: Ereditate și mediu ——
    {
        "stem": (
            "Care două afirmații despre ereditate în dezvoltarea psihică sunt corecte?"
        ),
        "options": [
            "ereditatea transmite potențial biologic și psihologic, nu un destin fix",
            "ereditatea oferă „materia primă” — maturarea și experiența o modelează",
            "ereditatea înseamnă că mediul devine irelevant",
            "ereditatea exclude complet orice influență a experienței",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ereditatea determină rigid și complet traseul dezvoltării, indiferent "
            "de experiență, educație sau cultură."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Mediul, în sens larg, include influențe care pot stimula sau bloca "
            "dezvoltarea. Care intră în această totalitate?"
        ),
        "options": [
            "condițiile naturale și fizice ale creșterii",
            "relațiile sociale și normele culturale",
            "experiențele educaționale formale și informale",
            "doar genele transmise de părinți, excluzând societatea",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Două gemene monozigote cresc în familii diferite și diferă la "
            "încrederea în sine, deși au aptitudini cognitive similare. Interpretarea "
            "cea mai echilibrată este:"
        ),
        "options": [
            "mediul nu contează deloc — doar genele explică totul",
            "potențialul ereditar poate fi valorificat sau frânat de experiență",
            "diferențele dovedesc că ereditatea nu există",
            "genele și mediul acționează uneori împreună, nu separat",
        ],
        "correct": "bd",
    },
    {
        "stem": (
            "Care situație ilustrează mai clar că mediul poate bloca dezvoltarea?"
        ),
        "options": [
            "copil cu potențial lingvistic ridicat, dar expus foarte puțin la "
            "conversație și lectură",
            "copil stimulat cognitiv într-o grădiniță cu activități variate",
            "adolescent care beneficiază de mentorat și feedback",
            "copil care primește atenție emoțională constantă acasă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între ereditate și mediu sunt formulate corect?"
        ),
        "options": [
            "ereditatea transmite tendințe și potențial; mediul oferă ocazii de "
            "exprimare sau limitare",
            "mediul poate amplifica sau reduce manifestarea unor capacități ereditare",
            "ereditatea și mediul sunt mereu în opoziție totală, fără interacțiune",
            "doar mediul contează; ereditatea e neglijabilă în orice explicație",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un copil are ușurință ereditară pentru coordonarea motrică fină, "
            "dar nu a avut niciodată materiale sau încurajare să deseneze. "
            "Cel mai probabil:"
        ),
        "options": [
            "potențialul există, dar nu s-a transformat încă în competență vizibilă",
            "ereditatea garantează automat performanța, chiar fără practică",
            "mediul este singurul factor care contează la desen",
            "dezvoltarea motorie nu depinde de experiență",
        ],
        "correct": "a",
    },
    # —— 17–24: Educația ——
    {
        "stem": (
            "Care afirmație despre educație și dezvoltare este cea mai precisă?"
        ),
        "options": [
            "educația este influență organizată, conștientă și sistematică",
            "educația valorifică potențialul ereditar prin experiență structurată",
            "educația este la fel cu orice întâmplare din mediul natural",
            "educația înlocuiește complet maturarea biologică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două afirmații despre rolul educației în dezvoltare sunt corecte?"
        ),
        "options": [
            "educația structurează experiența într-un mod planificat",
            "educația poate valorifica aptitudinile ereditare prin exercițiu ghidat",
            "educația înlocuiește complet maturarea biologică",
            "educația este identică cu orice întâmplare din mediul natural",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un părinte lasă copilul să învețe singur din întâmplare, fără "
            "obiective, fără feedback și fără progresie planificată. Aceasta "
            "reprezintă mai degrabă:"
        ),
        "options": [
            "educație în sens pedagogic strict",
            "influență mediatică generală, nu educație organizată",
            "exemplu de valorificare sistematică a potențialului ereditar",
            "intervenție conștientă asupra dezvoltării cognitive",
        ],
        "correct": "b",
    },
    {
        "stem": (
            "Profesorul proiectează activități de la simplu la complex, oferă "
            "modele, corectează erorile și urmărește obiective clare la fiecare "
            "lecție. Aceste practici aparțin rolului:"
        ),
        "options": [
            "educației ca influență organizată asupra dezvoltării",
            "eredității ca factor unic determinant",
            "mediului natural necontrolat",
            "maturării biologice care nu necesită intervenție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care combinații ilustrează corect relația educație — ereditate — "
            "dezvoltare?"
        ),
        "options": [
            "educația poate crea contexte în care potențialul ereditar se exprimă",
            "educația ignoră complet individualitatea copilului",
            "fără potențial minim, educația nu poate face orice, dar poate "
            "susține mult progresul",
            "educația și experiența mediului sunt echivalente cu orice întâmplare "
            "din jur",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Educația este doar o influență întâmplătoare a mediului, fără "
            "planificare, fără obiective și fără intenție pedagogică."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care caracteristică definește educația, spre deosebire de simpla "
            "expunere la mediu?"
        ),
        "options": [
            "organizare și intenționalitate",
            "lipsa oricărui obiectiv asumat de adult",
            "absența oricărei planificări pedagogice",
            "identitate cu orice influență mediatică întâmplătoare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În grădiniță, copiii învață să își exprime emoțiile prin joc "
            "structurat, povești și reguli de grup stabilite de educator. "
            "Componenta centrală este:"
        ),
        "options": [
            "educația ca experiență organizată care susține dezvoltarea emoțională",
            "refuzul oricărei intervenții adulte",
            "determinismul genetic exclusiv",
            "absența oricărei influențe sociale",
        ],
        "correct": "a",
    },
    # —— 25–32: Perspectiva biologică ——
    {
        "stem": (
            "Care formulare reflectă cel mai bine perspectiva biologică asupra "
            "dezvoltării?"
        ),
        "options": [
            "maturarea internă explică în principal ritmul etapelor",
            "mediul are rol secundar față de programul de maturare",
            "mediul este singurul factor relevant",
            "dezvoltarea nu are etape recognoscibile",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații reflectă perspectiva biologică asupra dezvoltării?"
        ),
        "options": [
            "există un program intern de maturare care pregătește anumite competențe",
            "debutul mersului sau al vorbirii are legătură cu pregătirea organismului",
            "mediul este singurul factor care explică toate etapele",
            "dezvoltarea cognitivă ar fi aceeași indiferent de vârsta biologică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un specialist insistă că un copil nu poate învăța operații logice "
            "formale înainte ca sistemul nervos să fi atins un anumit nivel de "
            "maturare — indiferent cât de mult l-am expune la exerciții. "
            "Această poziție este:"
        ),
        "options": [
            "strict interacționistă — mediul și ereditatea sunt egale",
            "strict culturală — limbajul decide totul",
            "aproape de accentul biologic pe maturare internă",
            "exclusiv behavioristă — doar recompensele contează",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Care capcane trebuie evitate când înțelegem perspectiva biologică?"
        ),
        "options": [
            "confundarea ei cu determinism rigid — potențialul nu e un destin fix",
            "credința că mediul nu contează deloc în viața reală a copilului",
            "ideea că maturarea internă poate fi ignorată complet",
            "recunoașterea că organismul pune limite de timp pentru anumite competențe",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Copilul începe să vadă perspectivă spațială în desen abia după ce "
            "anumite structuri corticale sunt suficient de mature. Exemplul "
            "susține mai mult:"
        ),
        "options": [
            "perspectiva biologică — maturarea pregătește apariția competenței",
            "perspectiva ambientală pură — orice se învață doar prin pedeapsă",
            "ideea că educația nu are rol",
            "faptul că etapele nu există în dezvoltare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmație despre perspectiva biologică este falsă?"
        ),
        "options": [
            "mediul este întotdeauna factorul principal, iar maturarea internă "
            "este neglijabilă",
            "există un program intern de maturare",
            "debutul unor competențe are legătură cu pregătirea organismului",
            "potențialul ereditar nu înseamnă destin fix",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două perechi opun corect perspectiva biologică de cea ambientală "
            "simplificată?"
        ),
        "options": [
            "biologică: accent pe maturare internă; ambientală: accent pe experiență "
            "și învățare",
            "biologică: mediu secundar în explicarea ritmului etapelor; ambientală: "
            "mediu ca factor central",
            "biologică: totul se învață prin recompensă; ambientală: totul e genetic",
            "ambele perspective resping complet ideea de etape în dezvoltare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce nu este suficientă singură perspectiva biologică pentru "
            "psihologia educației?"
        ),
        "options": [
            "ignoră modul în care experiența și școala pot accelera sau încetini "
            "manifestarea competențelor",
            "explică perfect fără a ține cont de cultură și limbaj",
            "nu ține cont că potențialul ereditar are nevoie de context",
            "răspunde complet la toate întrebările despre diferențe individuale",
        ],
        "correct": "ac",
    },
    # —— 33–40: Perspectiva ambientală ——
    {
        "stem": (
            "Care afirmații descriu perspectiva ambientală asupra dezvoltării?"
        ),
        "options": [
            "experiența și învățarea modelează comportamentul",
            "recompensele și pedepsele influențează comportamentul",
            "stimularea din mediu este centrală în explicație",
            "maturarea internă este singurul mecanism acceptat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care elemente aparțin perspectivelor ambientale / behavioriste asupra "
            "dezvoltării?"
        ),
        "options": [
            "învățarea prin asociere și repetare",
            "modificarea comportamentului prin recompense și pedepse",
            "stimularea din mediu ca sursă principală de schimbare",
            "ignorarea completă a oricărei experiențe după naștere",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un copil primește laude când împarte jucăriile și pierde privilegii "
            "când refuză — în timp cooperarea devine mai frecventă. Explicația "
            "din perspectiva ambientală este:"
        ),
        "options": [
            "comportamentul s-a modificat prin consecințele mediului social",
            "schimbarea dovedește că genele singure decid totul",
            "exemplul arată că maturarea internă nu există",
            "laudele și consecințele sunt forme de influență a mediului asupra "
            "comportamentului",
        ],
        "correct": "ad",
    },
    {
        "stem": (
            "Care afirmație despre perspectiva ambientală este falsă?"
        ),
        "options": [
            "dezvoltarea ar exista identic fără nicio experiență postnatală",
            "mediul poate modela comportamente noi",
            "învățarea observațională este o formă de influență ambientală",
            "stimularea precoce poate susține competențe cognitive",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Profesorul folosește recompense simbolice, feedback imediat și "
            "repetiție ghidată pentru a forma obiceiul de lectură zilnică. "
            "Strategia se aliniază cu:"
        ),
        "options": [
            "perspectiva ambientală — învățare prin consecințe și practică",
            "perspectiva biologică pură — doar maturarea contează",
            "ideea că educația nu poate structura experiența",
            "refuzul oricărei stimulări din exterior",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care limită a perspectivei ambientale strict simplificate este corect "
            "formulată?"
        ),
        "options": [
            "poate subestima rolul maturării și al potențialului ereditar",
            "explică perfect creativitatea fără context social",
            "mediul devine singurul factor relevant la orice vârstă",
            "genele decid totul, iar experiența e decor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În perspectiva ambientală, un copil devine anxios în situații sociale "
            "pentru că a fost criticat repetat — nu pentru că s-a născut „așa”. "
            "Accentul cade pe:"
        ),
        "options": [
            "experiența acumulată și învățarea din mediu",
            "programul genetic care exclude mediul",
            "etapele interne care nu necesită interacțiune",
            "lipsa oricărei influențe a consecințelor sociale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care combinație descrie corect mecanisme ambientale?"
        ),
        "options": [
            "stimulare — mediul oferă ocazii de exercițiu",
            "recompensă — consecințe care cresc probabilitatea repetării",
            "pedeapsă — consecințe care reduc un comportament",
            "maturare internă — singurul mecanism ambiental valid",
        ],
        "correct": "abc",
    },
    # —— 41–46: Perspectiva interacționistă ——
    {
        "stem": (
            "Perspectiva interacționistă susține că ereditatea și mediul acționează "
            "permanent împreună — niciun factor nu explică singur dezvoltarea."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație exprimă cel mai bine perspectiva interacționistă?"
        ),
        "options": [
            "potențialul ereditar se manifestă diferit în medii diferite",
            "ereditatea și mediul sunt separați complet și nu se influențează",
            "doar genele explică dezvoltarea, mediul e irelevant",
            "mediul scrie totul de la zero, fără potențial ereditar",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un copil cu temperament mai reactiv devine anxios într-o clasă cu "
            "pedepse publice, dar se adaptează bine într-o clasă cu feedback "
            "calm. Exemplul ilustrează:"
        ),
        "options": [
            "interacțiune temperament (tendință ereditară) — mediu educațional",
            "faptul că doar genele contează",
            "faptul că mediul contează doar la adulți",
            "imposibilitatea educației de a influența emoțiile",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care poziții sunt incompatibile cu perspectiva interacționistă?"
        ),
        "options": [
            "determinism genetic total — mediul e decor",
            "tabula rasa absolută — doar mediul scrie totul",
            "potențial ereditar modelat de experiență",
            "educația valorifică aptitudini diferite la copii diferiți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două motive fac perspectiva interacționistă utilă în practica școlară?"
        ),
        "options": [
            "evită fatalismul genetic și neglijarea mediului",
            "permite adaptarea educației la potențialul și nevoile copilului",
            "confirmă că toți copiii sunt identici biologic",
            "susține un singur tipar de predare pentru toți copiii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un cercetător spune: „genele deschid uși, mediul decide prin care "
            "treci”. Această metaforă se apropie de:"
        ),
        "options": [
            "perspectiva interacționistă",
            "determinism biologic rigid",
            "negarea completă a eredității",
            "ideea că educația nu structurează experiența",
        ],
        "correct": "a",
    },
    # —— 47–50: Perspectiva culturală (Vygotsky, Bruner) ——
    {
        "stem": (
            "Care afirmație despre perspectiva culturală (Vygotsky, Bruner) este "
            "cea mai precisă?"
        ),
        "options": [
            "limbajul, valorile și interacțiunea socială modelează dezvoltarea",
            "dezvoltarea cognitivă are loc în vid social",
            "cultura este decor, fără influență reală",
            "doar genele explică apariția gândirii simbolice",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei idei aparțin perspectivei culturale asupra dezvoltării?"
        ),
        "options": [
            "cogniția se construiește prin participare la practici sociale",
            "limbajul mediatizează învățarea și gândirea",
            "dezvoltarea are loc în afara oricărei culturi sau simboluri",
            "adultul sau partenerul mai competent poate ghida zona proximală de "
            "dezvoltare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "În activitatea de grup, copilul rezolvă o problemă cu ajutorul "
            "colegului mai avansat, apoi reușește singur. Conceptul vygotskian "
            "relevant este:"
        ),
        "options": [
            "zona proximală de dezvoltare: ce reușește cu sprijin vs. singur",
            "extincție comportamentală prin pedeapsă",
            "maturare reflexă fără influență socială",
            "potențial ereditar care exclude orice partener",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru afirmații despre Bruner și învățare culturală sunt corecte?"
        ),
        "options": [
            "învățarea poate urma reprezentări enactive, iconice și simbolice",
            "cultura oferă unelte cognitive transmise prin limbaj și instituții",
            "educația poate organiza experiența în forme accesibile vârstei",
            "copilul învață exclusiv izolat, fără modele culturale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru distincții între perspectivele biologică, ambientală, "
            "interacționistă și culturală sunt corecte?"
        ),
        "options": [
            "biologică: maturare internă; ambientală: experiență și consecințe",
            "interacționistă: ereditate + mediu împreună; culturală: limbaj și practici sociale",
            "culturală: dezvoltare în vid social; biologică: doar recompense",
            "toate patru pot fi recunoscute după factorul pe care îl pun central",
        ],
        "correct": "abd",
    },
]

from scripts.psihologia_dezvoltarii_ii_teorii_bank_data import TEORII_INVATARII_ITEMS
from scripts.psihologia_dezvoltarii_ii_senzorio_motor_bank_data import (
    SENZORIO_MOTOR_ITEMS,
)
from scripts.psihologia_dezvoltarii_ii_limbaj_bank_data import LIMBAJ_ITEMS
from scripts.psihologia_dezvoltarii_ii_atasament_bank_data import ATASAMENT_ITEMS
from scripts.psihologia_dezvoltarii_ii_simbol_joc_bank_data import SIMBOL_JOC_ITEMS
from scripts.psihologia_dezvoltarii_ii_scolaritate_bank_data import SCOLARITATE_ITEMS
from scripts.psihologia_dezvoltarii_ii_adolescenta_bank_data import ADOLESCENTA_ITEMS
from scripts.psihologia_dezvoltarii_ii_tinereete_bank_data import TINERETE_ITEMS
from scripts.psihologia_dezvoltarii_ii_batranete_bank_data import BATRANETE_ITEMS
from scripts.psihologia_dezvoltarii_ii_durere_bank_data import DURERE_ITEMS
from scripts.psihologia_dezvoltarii_ii_autori_bank_data import AUTORI_CLASICI_ITEMS

PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(METODE_CERCETARE_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(TEORII_INVATARII_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(SENZORIO_MOTOR_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(LIMBAJ_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(ATASAMENT_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(SIMBOL_JOC_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(SCOLARITATE_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(ADOLESCENTA_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(TINERETE_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(BATRANETE_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(DURERE_ITEMS)
PSIHOLOGIA_DEZVOLTARII_II_ITEMS.extend(AUTORI_CLASICI_ITEMS)

assert len(PSIHOLOGIA_DEZVOLTARII_II_ITEMS) == 490
