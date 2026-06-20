"""Itemi — Epigenetica II: GENETICĂ COMPORTAMENTALĂ (50 itemi, ID 11806–11855)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

GENETICA_COMPORTAMENTALA_ITEMS: List[Item] = [
    {
        "stem": (
            "Genetica comportamentală studiază influența factorilor genetici "
            "asupra comportamentului și a diferențelor individuale."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Eritabilitatea (H²) se calculează ca raportul varianței genetice "
            "(Vg) la varianța fenotipică totală (Vp): H² = Vg / Vp."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Gemenii monozigoți (MZ) împart, în medie, aproximativ 50% din "
            "variantele de ADN, la fel ca gemenii dizigoți (DZ)."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "În modelul ACE, componenta C se referă la mediul unic/individual "
            "(experiențe neîmpărtășite)."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "GWAS (Genome-Wide Association Study) investighează asocierile "
            "dintre SNP-uri și trăsături comportamentale sau psihologice."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Scopul principal al geneticii comportamentale este:",
        "options": [
            "înțelegerea influenței genelor asupra comportamentului și a diferențelor individuale",
            "descrierea mutațiilor cromozomiale fără legătură cu comportamentul",
            "negarea contribuției mediului în explicarea diferențelor individuale",
            "măsurarea numărului de cromozomi din celulele somatice",
        ],
        "correct": "a",
    },
    {
        "stem": "În formula H² = Vg / Vp, numeratorul (Vg) reprezintă:",
        "options": [
            "varianța atribuită diferențelor genetice",
            "varianța mediului comun familial",
            "varianța fenotipică totală",
            "varianța mediului unic individual",
        ],
        "correct": "a",
    },
    {
        "stem": "În formula H² = Vg / Vp, numitorul (Vp) reprezintă:",
        "options": [
            "varianța fenotipică totală (totalitatea diferențelor observate)",
            "varianța genetică aditivă strictă",
            "varianța mediului neîmpărtășit exclusiv",
            "proporția varianței explicate de un singur SNP",
        ],
        "correct": "a",
    },
    {
        "stem": "Când H² se apropie de 1, interpretarea uzuală este:",
        "options": [
            "influență genetică relativ mare asupra variației trăsăturii",
            "influență a mediului relativ mare asupra variației trăsăturii",
            "lipsa varianței fenotipice în populația studiată",
            "determinism genetic absolut al fiecărui individ",
        ],
        "correct": "a",
    },
    {
        "stem": "Când H² se apropie de 0, interpretarea uzuală este:",
        "options": [
            "influență a mediului relativ mare asupra variației trăsăturii",
            "influență genetică relativ mare asupra variației trăsăturii",
            "demonstrarea că genele nu există în populația studiată",
            "certitudinea că trăsătura este determinată genetic în totalitate",
        ],
        "correct": "a",
    },
    {
        "stem": "Gemenii monozigoți (MZ) au, în medie, aproximativ:",
        "options": [
            "~100% ADN comun (sunt genetic identici)",
            "~50% ADN comun (ca frații obișnuiți)",
            "~25% ADN comun",
            "0% ADN comun (la fel de diferiți ca străinii)",
        ],
        "correct": "a",
    },
    {
        "stem": "Gemenii dizigoți (DZ) au, în medie, aproximativ:",
        "options": [
            "~50% ADN comun (ca frații obișnuiți)",
            "~100% ADN comun (identici genetic)",
            "~12,5% ADN comun (ca verii primari)",
            "100% mediu comun, dar 0% asemănare genetică",
        ],
        "correct": "a",
    },
    {
        "stem": "Gemenii monozigoți (MZ) sunt descriși ca:",
        "options": [
            "gemeni identici (din același ovul fertilizat)",
            "gemeni fraterni (din ovule diferite)",
            "frați obișnuiți născuți în zile diferite",
            "indivizi cu același fenotip, dar 50% ADN comun",
        ],
        "correct": "a",
    },
    {
        "stem": "Gemenii dizigoți (DZ) sunt descriși ca:",
        "options": [
            "gemeni fraterni (din ovule diferite, fertilizate separat)",
            "gemeni identici (din același zigot)",
            "clonă perfectă a aceluiași individ",
            "indivizi cu 100% identitate de ADN",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă gemenii monozigoți (MZ) seamănă semnificativ mai mult decât "
            "gemenii dizigoți (DZ) la o trăsătură, concluzia uzuală este:"
        ),
        "options": [
            "există influență genetică asupra trăsăturii",
            "trăsătura este determinată de mediu",
            "genele nu contribuie la variația trăsăturii",
            "MZ și DZ au același grad de asemănare genetică",
        ],
        "correct": "a",
    },
    {
        "stem": "În modelul ACE, componenta A reprezintă:",
        "options": [
            "influența genetică aditivă",
            "mediul comun/familial",
            "mediul unic/individual",
            "varianța de măsurare (eroare de test)",
        ],
        "correct": "a",
    },
    {
        "stem": "În modelul ACE, componenta C reprezintă:",
        "options": [
            "mediul comun/familial (factori de mediu împărtășiți)",
            "influența genetică aditivă",
            "mediul unic/individual (experiențe neîmpărtășite)",
            "varianța fenotipică totală",
        ],
        "correct": "a",
    },
    {
        "stem": "În modelul ACE, componenta E reprezintă:",
        "options": [
            "mediul unic/individual (experiențe neîmpărtășite + eroare)",
            "mediul comun/familial",
            "influența genetică aditivă",
            "coeficientul de eritabilitate H²",
        ],
        "correct": "a",
    },
    {
        "stem": "SNP (Single Nucleotide Polymorphism) este:",
        "options": [
            "o variație a unei singure baze azotate în secvența ADN",
            "un scor care combină efectele a mii de variante genetice",
            "studiu asociativ la nivel de genom întreg",
            "proporția varianței fenotipice explicate genetic",
        ],
        "correct": "a",
    },
    {
        "stem": "GWAS (Genome-Wide Association Study) investighează:",
        "options": [
            "relația dintre SNP-uri și trăsături (comportamentale/psihologice)",
            "eritabilitatea gemenilor monozigoți fără date moleculare",
            "varianța mediului comun familial din modelul ACE",
            "numărul total de cromozomi din celulele somatice",
        ],
        "correct": "a",
    },
    {
        "stem": "GPS (Genetic/Polygenic Score) reprezintă:",
        "options": [
            "un scor poligenic care combină efectele mai multor SNP-uri",
            "varianța fenotipică totală din formula H²",
            "procentul de ADN comun la gemenii dizigoți",
            "componenta C din modelul ACE",
        ],
        "correct": "a",
    },
    {
        "stem": "Eritabilitatea (H²) exprimă:",
        "options": [
            "proporția variației fenotipice explicate de diferențele genetice",
            "proporția variației explicate de un singur gen",
            "identitatea genetică perfectă între gemeni DZ",
            "măsura directă a influenței mediului unic",
        ],
        "correct": "a",
    },
    {
        "stem": "Modelul ACE separă varianța fenotipică în:",
        "options": [
            "A (genetic), C (mediu comun), E (mediu unic)",
            "A (mediu comun), C (genetic), E (măsurare)",
            "A (genetic), C (mediu unic), E (mediu comun)",
            "A, C și E — toate trei reprezintă varianța genetică",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi tip gemeni–ADN comun sunt corecte?",
        "options": [
            "Monozigoți (MZ) — ~100% ADN comun",
            "Dizigoți (DZ) — ~50% ADN comun",
            "Monozigoți (MZ) — ~50% ADN comun",
            "Dizigoți (DZ) — ~100% ADN comun",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care interpretări ale valorilor extreme ale H² sunt corecte?",
        "options": [
            "H² → 1: influență genetică relativ mare",
            "H² → 0: influență a mediului relativ mare",
            "H² → 1: varianță genetică zero în populație",
            "H² = Vg / Vp",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi componentă ACE–semnificație sunt corecte?",
        "options": [
            "A — genetic (aditiv)",
            "C — mediu comun/familial",
            "A — mediu unic individual",
            "E — varianța fenotipică totală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi componentă ACE–semnificație sunt corecte?",
        "options": [
            "C — mediu comun/familial",
            "E — mediu unic/individual",
            "C — genetic aditiv",
            "E — varianța fenotipică totală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre studiile gemelare sunt corecte?",
        "options": [
            "MZ au ~100% ADN comun; DZ au ~50%",
            "dacă MZ seamănă mai mult decât DZ → suport pentru influență genetică",
            "DZ sunt gemeni identici din același ovul",
            "MZ sunt gemeni fraterni din ovule diferite",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre SNP și GWAS sunt corecte?",
        "options": [
            "SNP = variație a unei singure baze",
            "GWAS analizează asocieri SNP–trăsături la scară genomică",
            "SNP = scor poligenic combinat",
            "GWAS măsoară direct H² prin interviu clinic",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre GWAS și GPS sunt corecte?",
        "options": [
            "GWAS identifică SNP-uri asociate cu trăsături",
            "GPS combină efectele mai multor SNP-uri într-un scor",
            "GPS înlocuiește studiile gemelare în toate contextele",
            "GWAS studiază relația SNP–trăsături",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre eritabilitate și varianță sunt corecte?",
        "options": [
            "H² = Vg / Vp",
            "Vg = varianța genetică",
            "Vp = varianța fenotipică totală",
            "Vp = varianța mediului unic (E) exclusiv",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre gemenii MZ vs DZ sunt corecte?",
        "options": [
            "MZ: ~100% ADN comun (identici)",
            "DZ: ~50% ADN comun (fraterni)",
            "MZ: din același ovul fertilizat",
            "DZ: din același ovul fertilizat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre interpretarea H² sunt corecte?",
        "options": [
            "H² = Vg / Vp",
            "H² mare → contribuție genetică relativ mai mare la variație",
            "H² mic → contribuție a mediului relativ mai mare la variație",
            "H² = 1 → determinism genetic absolut al fiecărui individ",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care tehnici din genetica comportamentală sunt corect descrise?",
        "options": [
            "SNP — variație a unei singure baze",
            "GWAS — relația SNP–trăsături",
            "GPS — scor poligenic (mai multe SNP-uri combinate)",
            "GPS — variație a unei singure baze azotate",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care componente ale modelului ACE sunt corect definite?",
        "options": [
            "A — genetic",
            "C — mediu comun/familial",
            "E — mediu unic/individual",
            "E — mediu comun familial",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care inferențe din studiile gemelare sunt valide?",
        "options": [
            "MZ mai similari decât DZ → există influență genetică",
            "MZ și DZ crescuți împreună împart adesea mediu familial similar",
            "similaritate MZ > DZ exclude orice rol al mediului",
            "DZ au același grad de asemănare genetică ca MZ",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre scorul poligenic (GPS) sunt corecte?",
        "options": [
            "combină efectele mai multor SNP-uri",
            "poate estima o tendință genetică pentru o trăsătură",
            "este identic cu un singur SNP",
            "se construiește adesea pe baza rezultatelor GWAS",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre genetica comportamentală sunt corecte?",
        "options": [
            "studiază influența genelor asupra comportamentului",
            "analizează diferențe individuale cu componentă genetică",
            "postulează că mediul nu contează deloc",
            "folosește eritabilitatea ca indicator al contribuției genetice la variație",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre A și E în modelul ACE sunt corecte?",
        "options": [
            "A = influență genetică aditivă",
            "E = mediu unic/individual (+ eroare)",
            "A = mediu comun familial",
            "E = influență genetică aditivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre Vg și Vp sunt corecte?",
        "options": [
            "Vg = varianța datorată diferențelor genetice",
            "Vp = varianța fenotipică totală",
            "Vg = varianța fenotipică totală",
            "Vp = varianța genetică aditivă strictă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații leagă corect H² de componentele de varianță?",
        "options": [
            "H² = Vg / Vp",
            "Vg se referă la varianța genetică",
            "Vp se referă la varianța mediului unic (E) exclusiv",
            "H² = Vp / Vg",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce set descrie corect modelul ACE?",
        "options": [
            "A = genetic (aditiv)",
            "C = mediu comun/familial",
            "E = mediu unic/individual",
            "A + C + E descompun varianța fenotipică",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set descrie corect studiile gemelare?",
        "options": [
            "MZ: ~100% ADN comun, gemeni identici",
            "DZ: ~50% ADN comun, gemeni fraterni",
            "MZ > DZ la similaritate → influență genetică",
            "MZ și DZ pot fi crescuți în același mediu familial",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set descrie corect eritabilitatea (H²)?",
        "options": [
            "H² = Vg / Vp",
            "H² → 1: influență genetică relativ mare",
            "H² → 0: influență a mediului relativ mare",
            "H² se interpretează la nivel de populație, nu al individului",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set descrie corect tehnici moderne (SNP, GWAS, GPS)?",
        "options": [
            "SNP = variație a unei singure baze",
            "GWAS = relația SNP–trăsături",
            "GPS = scor poligenic (combină SNP-uri)",
            "GPS se bazează adesea pe rezultatele GWAS",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set integrează scopul, H², gemenii și modelul ACE?",
        "options": [
            "Scop: influența genelor asupra comportamentului și diferențelor individuale",
            "H² = Vg / Vp; H² mare → influență genetică relativ mai mare",
            "Studii gemelare: MZ ~100% ADN, DZ ~50%; MZ > DZ → influență genetică",
            "ACE: A = genetic, C = mediu comun, E = mediu unic",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care perechi tehnologie–rol sunt corecte?",
        "options": [
            "SNP — variație a unei singure baze azotate",
            "GWAS — asocieri între SNP-uri și trăsături",
            "GPS — variație a unei singure baze azotate",
            "SNP — scor poligenic combinat din mii de variante",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre componenta C (ACE) sunt corecte?",
        "options": [
            "C = mediu comun/familial",
            "include factori de mediu împărtășiți (ex. familie, școală)",
            "C = mediu unic/individual",
            "C = influență genetică aditivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce set descrie corect studiile gemelare și inferența genetică?",
        "options": [
            "MZ: ~100% ADN comun; DZ: ~50% ADN comun",
            "MZ = gemeni identici; DZ = gemeni fraterni",
            "Similaritate MZ > DZ → suport pentru influență genetică",
            "Similaritate MZ = DZ → demonstrează eritabilitate maximă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce set recapitulează genetica comportamentală (scop → metode)?",
        "options": [
            "Scop: gene → comportament și diferențe individuale",
            "H² = Vg/Vp; model ACE (A, C, E); studii gemelare MZ/DZ",
            "SNP, GWAS, GPS — abordări moleculare moderne",
            "H² = 1 înseamnă că mediul nu influențează deloc fiecare individ",
        ],
        "correct": "abc",
    },
]


def _count_dist(rows):
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


SEG_DIST_50 = {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}

assert len(GENETICA_COMPORTAMENTALA_ITEMS) == 50
assert _count_dist(GENETICA_COMPORTAMENTALA_ITEMS) == SEG_DIST_50
