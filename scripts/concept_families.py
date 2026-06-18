"""Familii conceptuale — detectare coerență stem/variante și pool-uri de distractori."""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Set, Tuple

FAMILY_KEYWORDS: Dict[str, Tuple[str, ...]] = {
    "behavioral_genetics": (
        "genetic", "genom", "eritabil", "gemen", "monozig", "dizig",
        "adopți", "adoptie", "epigenet", "moștenire", "heritab", "gwas",
        "mediu comun", "mediu neîmpărtășit", "mediu unic", "modelul ace",
        "variației unei trăsături", "factorilor genetici",
    ),
    "personality": (
        "personalitat", "trăsătur", "big five", "eysenck", "hexaco",
        "neuroticism", "extraversie", "conștiincioz", "agreabilit",
        "idiograf", "nomotet", "temperament", "caracterologic",
        "modelul pen", "psihoticism",
    ),
    "psychotherapy": (
        "psihoterap", "terapie", "psihanaliz", "psihodinamic", "umanist",
        "cognitiv-comportamental", "act ", "dbt", "eft", "schema therapy",
        "alianță terapeutic", "transfer", "interpretare", "restructurare cognitiv",
        "transdiagnostic", "congruență", "empatie terapeutic",
    ),
    "psychometrics": (
        "validitate", "fidelitate", "norme", "standardiz", "psihometr",
        "test-retest", "inter-evaluator", "incrementală", "de conținut",
        "de construct", "de criteriu", "coeficient", "scor brut",
        "interpretarea scor", "fiabilitate",
    ),
    "statistics": (
        "statistic", "anova", "corelaț", "pearson", "spearman", "regresi",
        "test t", "testul t", "eșantion", "populaț", "semnificaț",
        "ipotez", "putere statistic", "interval", "medie", "median",
        "abatere standard", "varianț", "chi-pătrat",
    ),
    "development": (
        "dezvoltar", "piaget", "vygotsky", "bruner", "stadiu",
        "cognitivă la copil", "zona proxim", "scaffolding", "joc simbolic",
        "permanența obiect", "atașament", "ainsworth", "bowlby", "harlow",
        "parental", "adolescen",
    ),
    "work_org": (
        "muncă", "munca", "organizaț", "postului", "job", "hackman",
        "oldham", "jd-r", "burnout", "rol organiza", "leadership",
        "performanță organiza", "satisfacție profes", "implicare în muncă",
        "evaluare 360", "analiza muncii", "ksao", "selecție personal",
        "enlargement", "enrichment", "îmbogățire", "lărgire", "rotire",
        "varietatea aptitudinilor", "identitatea sarcinii", "autonomia",
        "feedbackul din muncă", "semnificația sarcinii", "fișa postului",
        "criteriul contaminat", "criteriul deficient", "evaluarea performanței",
    ),
    "psychopathology": (
        "tulburare", "simptom", "dsm", "diagnostic", "episod",
        "delir", "halucina", "mania", "depresie", "anxietate",
        "schizofren", "borderline", "cluster", "psihopatolog",
        "comorbid", "prognostic",
    ),
    "learning": (
        "învățare", "conditionare", "condiționare", "întărire", "pedeapsă",
        "skinner", "bandura", "observațional", "operant", "clasica",
        "recompens", "stimul condiționat", "generalizare stimul",
    ),
    "social": (
        "social", "grup", "conformism", "obediență", "atitudine",
        "persuasiune", "prejudec", "stereotip", "agresiv", "prosocial",
        "justiție", "normă de grup",
    ),
    "cognitive": (
        "cognitiv", "memorie", "atenție", "percepț", "reprezentare mental",
        "procesare informa", "heuristic", "bias cognitiv", "schema cognitiv",
    ),
}

# Marcatori care indică distractor din alt capitol față de familia enunțului
CROSS_FAMILY_MARKERS: Dict[str, Tuple[str, ...]] = {
    "behavioral_genetics": (
        "vygotsky", "piaget", "psihoterap", "validitate de criteriu", "big five",
        "idiograf", "eysenck", "zona proxim", "hackman", "job design",
        "atașament", "satisfacția muncii", "anova", "test t pentru",
        "umanist-experiențial", "criteriul contaminat",
    ),
    "psychotherapy": (
        "eritabilit", "gemen", "anova", "eșantion", "populaț", "hackman",
        "vygotsky", "big five", "epigenet", "validitate externă", "job design",
        "stadiul senzorio", "corelație pearson", "hipoman", "anorex",
        "restricție alimentar", "îngrășare", "episod de dispoziție",
        "lărgirea postului", "rotirea posturilor", "analiza muncii",
    ),
    "psychometrics": (
        "gemen", "epigenet", "psihoterap", "vygotsky", "atașament",
        "hackman", "borderline", "cluster a", "întărire negativă",
    ),
    "statistics": (
        "psihoterap", "atașament", "big five", "gemen", "hackman",
        "terapia dialectic", "cluster b", "vygotsky",
    ),
    "development": (
        "eritabilit", "anova", "validitate de criteriu", "hackman",
        "psihoterap", "cluster", "job design", "burnout",
    ),
    "work_org": (
        "gemen", "epigenet", "vygotsky", "atașament", "psihanaliz",
        "big five", "delir", "anova unifactorială",
    ),
    "psychopathology": (
        "hackman", "vygotsky", "validitate de conținut", "gemen",
        "job design", "anova", "întărire pozitivă",
    ),
    "personality": (
        "vygotsky", "psihoterap", "anova", "hackman", "validitate de criteriu",
        "atașament", "job design", "test t pentru",
    ),
}

DOMAIN_DEFAULT_FAMILIES: Dict[str, Tuple[str, ...]] = {
    "psihologia personalității": ("personality", "behavioral_genetics"),
    "psihologia dezvoltării": ("development",),
    "metodologie": ("psychometrics", "statistics"),
    "evaluare psihologică": ("psychometrics",),
    "statistică": ("statistics",),
    "psihologia organizațională": ("work_org",),
    "psihopatologie": ("psychopathology",),
    "psihoterapie": ("psychotherapy",),
}

# Pool-uri de definiții omogene pentru rescriere
FAMILY_DEFINITION_POOLS: Dict[str, List[str]] = {
    "behavioral_genetics": [
        "contribuția relativă a factorilor genetici și de mediu la diferențele individuale",
        "diferența dintre influențele genetice aditive, mediul comun și mediul neîmpărtășit",
        "gradul în care gemenii monozigoți sunt mai asemănători decât gemenii dizigoți pentru o trăsătură",
        "estimarea ereditabilității unei trăsături prin compararea concordanței gemenilor",
        "separarea aproximativă a mediului comun de mediul neîmpărtășit în variația trăsăturilor",
        "compararea similarității la adopție pentru a separa influențele genetice de cele familiale",
        "identificarea directă a fiecărei gene responsabile de o trăsătură psihologică complexă",
        "modificarea directă a expresiei genelor prin intervenții educaționale standardizate",
        "eliminarea completă a influenței mediului din explicația diferențelor individuale",
        "calcularea tuturor variantelor genetice responsabile pentru o trăsătură într-un singur studiu",
    ],
    "psychometrics": [
        "relația dintre scorul la test și un criteriu extern relevant",
        "gradul în care itemii acoperă domeniul de conținut al constructului măsurat",
        "măsura în care instrumentul evaluează constructul teoretic vizat",
        "stabilitatea scorurilor la administrări repetate în condiții similare",
        "consistența acordului între evaluatori independenți",
        "contribuția suplimentară a unui predictor peste metodele deja folosite",
        "compararea scorului individual cu performanța unui grup de referință",
        "demonstrarea automată a cauzalității doar pe baza unui coeficient de corelație",
    ],
    "statistics": [
        "probabilitatea de a respinge incorect ipoteza nulă când ea este adevărată",
        "măsura asocierii liniare dintre două variabile cantitative",
        "compararea mediilor a două grupuri independente",
        "compararea mediilor aceluiași grup la două momente de măsurare",
        "gradul în care rezultatele pot fi generalizate la alte populații",
        "diferența dintre semnificația statistică și importanța practică a efectului",
        "definirea populației țintă și a unității de analiză în cercetare",
        "identificarea automată a cauzei pe baza unei corelații observate",
    ],
    "psychotherapy": [
        "mecanisme comune care pot menține tulburări diferite, nu doar eticheta diagnostică",
        "relația dintre gânduri, emoții și comportamente și modificarea patternurilor disfuncționale",
        "procese inconștiente, conflicte intrapsihice și relația terapeutică",
        "acceptare, valori personale și flexibilitate psihologică în schimbare",
        "validare emoțională și strategii de reglare în context dialectic",
        "aplicarea rigidă a aceluiași protocol pentru orice diagnostic, fără formulare de caz",
        "evaluarea aptitudinilor cognitive prin teste standardizate ca unică intervenție",
        "explorarea exclusivă a viselor fără lucrul cu comportamentele actuale",
    ],
    "development": [
        "distanța dintre nivelul actual de dezvoltare și cel atins cu sprijin adult",
        "folosirea figurii de atașament ca bază de siguranță la explorare",
        "stadiul în care copilul operează cu raționament abstract și ipotetico-deductiv",
        "învățarea prin observarea modelelor și a consecințelor comportamentelor lor",
        "internalizarea regulilor morale și a normelor sociale în relația cu adultul",
        "perioada în care apare permanența obiectului în stadiul senzorio-motor",
        "dependența de sprijinul adultului în rezolvarea sarcinilor din zona proximă",
        "tipurile de atașament diferențiate prin reacția copilului la separare și reuniune",
    ],
    "work_org": [
        "adăugarea de sarcini variate la același nivel de responsabilitate",
        "creșterea responsabilității, autonomiei și profunzimii postului",
        "alternarea periodică a angajatului între posturi sau secțiuni diferite",
        "măsura în care postul cere activități și abilități diverse",
        "măsura în care postul permite realizarea unei lucrări complete și identificabile",
        "impactul perceput al muncii asupra altor persoane sau asupra organizației",
        "libertatea angajatului de a decide cum și când își realizează munca",
        "informația clară primită din activitate despre eficiența performanței",
        "echilibrul dintre cerințele jobului și resursele disponibile ale angajatului",
        "epuizarea emoțională, detașarea cinică și scăderea competenței profesionale",
        "neclaritatea așteptărilor, responsabilităților sau criteriilor de succes ale rolului",
        "comportamentul voluntar care susține colegii sau organizația",
    ],
    "personality": [
        "tendința la instabilitate emoțională și experiențe negative frecvente",
        "orientarea spre sociabilitate, energie și căutarea stimulării",
        "regularitatea comportamentului prin patternuri dacă-atunci activate de situație",
        "proporția variației unei trăsături atribuită diferențelor genetice",
        "abordarea care pune accent pe unicitatea și irreductibilitatea fiecărei persoane",
        "modelul care reduce personalitatea la trei dimensiuni biologice fundamentale",
        "validitatea externă a unui instrument de evaluare a personalității",
        "tehnica de restructurare cognitivă a gândurilor automate disfuncționale",
    ],
    "psychopathology": [
        "pattern persistent de experiență interioară și comportament care deviază de la așteptări",
        "prezența convingerilor false fixe care nu se modifică la prezentarea dovezilor",
        "percepție fără stimul extern adecvat în circumstanțe clare",
        "episod cu dispoziție depresivă și/sau anhedonie cu afectare semnificativă",
        "frică sau evitare socială asociată cu evaluare negativă de către alții",
        "stiluri dramatice, emoționale sau impulsive în relațiile interpersonale",
        "validitatea de criteriu a unui test de aptitudini cognitive",
        "compararea gemenilor pentru estimarea ereditabilității anxietății",
    ],
    "learning": [
        "creșterea probabilității unui comportament prin eliminarea unui stimul neplăcut",
        "creșterea probabilității unui comportament prin prezentarea unui stimul plăcut",
        "scăderea probabilității unui comportament prin eliminarea unui stimul plăcut",
        "învățarea prin observarea consecințelor comportamentului unui model",
        "asocierea unui stimul neutru cu un stimul incondiționat",
        "extinderea unui răspuns condiționat la stimuli asemănători cu cel inițial",
        "reducerea treptată a recompenselor pentru menținerea unui comportament învățat",
        "înregistrarea consecințelor comportamentului pentru modificarea frecvenței sale",
    ],
}

# Termeni scurți omogene (itemi care cer etichete, nu definiții lungi)
FAMILY_TERM_POOLS: Dict[str, List[str]] = {
    "work_org": [
        "Job enlargement",
        "Job enrichment",
        "Rotirea posturilor",
        "Varietatea aptitudinilor",
        "Identitatea sarcinii",
        "Semnificația sarcinii",
        "Autonomia",
        "Feedbackul din muncă",
        "Burnoutul",
        "Ambiguitatea de rol",
        "Conflictul de rol",
        "Implicarea în muncă",
    ],
    "behavioral_genetics": [
        "Ereditabilitatea",
        "Studiile gemelare",
        "Modelul ACE",
        "Mediul comun",
        "Mediul neîmpărtășit",
        "Studiile de adopție",
        "Moștenirea epigenetică",
    ],
}

STEM_FAMILY_RULES: List[Tuple[str, str]] = [
    (r"job enlargement|lărgirea postului|lărgire.*post", "work_org"),
    (r"job enrichment|îmbogățirea postului|îmbogățire.*post", "work_org"),
    (r"rotirea posturilor|job rotation", "work_org"),
    (r"hackman|oldham|caracteristicile postului|proiectarea postului", "work_org"),
    (r"evaluare 360|evaluarea performanței|criteriul contaminat|criteriul deficient", "work_org"),
    (r"genetic|gemen|eritabil|epigenet|moștenire.*genetic", "behavioral_genetics"),
    (r"studiile gemenare|studiile de gemeni|genetica comportamental", "behavioral_genetics"),
    (r"validitate|fidelitate|norme|standardiz|psihometr|test-retest", "psychometrics"),
    (r"statistic|anova|corelaț|pearson|eșantion|populaț|ipotez", "statistics"),
    (r"psihoterap|terapie|psihanaliz|psihodinamic|transdiagnostic", "psychotherapy"),
    (r"dezvoltar|vygotsky|piaget|atașament|zona proxim|situația stranie", "development"),
    (r"muncă|organizaț|postului|hackman|burnout|jd-r|job", "work_org"),
    (r"tulburare|cluster [abc]|psihopatolog|simptom|dsm", "psychopathology"),
    (r"învățare|întărire|pedeapsă|conditionare|bandura|skinner", "learning"),
    (r"personalitat|trăsătur|big five|eysenck|temperament", "personality"),
    (r"social|grup|conformism|atitudine|agresiv", "social"),
]


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def score_families(text: str) -> Dict[str, int]:
    low = _norm(text)
    scores: Dict[str, int] = {}
    for family, keywords in FAMILY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in low)
        if score:
            scores[family] = score
    return scores


def primary_families(text: str, domain: str = "") -> List[str]:
    scores = score_families(text)
    if not scores and domain:
        dlow = _norm(domain)
        for key, fams in DOMAIN_DEFAULT_FAMILIES.items():
            if key in dlow:
                return list(fams)
    if not scores:
        for pattern, family in STEM_FAMILY_RULES:
            if re.search(pattern, _norm(text), re.I):
                return [family]
        return []
    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    top = ranked[0][1]
    return [f for f, s in ranked if s >= max(1, top - 1)]


def family_from_stem(stem: str, domain: str = "") -> Optional[str]:
    fams = primary_families(stem, domain)
    return fams[0] if fams else None


def is_cross_family_distractor(
    distractor: str, stem_family: str, stem: str = ""
) -> bool:
    """Distractor evident din alt capitol."""
    if not stem_family:
        return False
    low = _norm(distractor)
    markers = CROSS_FAMILY_MARKERS.get(stem_family, ())
    if any(m in low for m in markers):
        return True

    d_fams = primary_families(distractor)
    if not d_fams:
        return False
    stem_fams = set(primary_families(stem, "")) if stem else {stem_family}
    stem_fams.add(stem_family)
    if not stem_fams & set(d_fams):
        # termen scurt din altă familie (ex. „Abordarea idiografică”)
        if len(low) < 80 and d_fams[0] not in stem_fams:
            return True
    return False


def families_overlap(a: str, b: str) -> bool:
    return bool(set(primary_families(a)) & set(primary_families(b)))


def anchor_families(
    stem: str, domain: str, correct_texts: Sequence[str]
) -> Set[str]:
    """Familii de referință: enunț + răspuns(uri) corect(e) + domeniu lot."""
    fams: Set[str] = set()
    for f in primary_families(stem, domain):
        fams.add(f)
    for text in correct_texts:
        for f in primary_families(str(text)):
            fams.add(f)
    if not fams and domain:
        dlow = _norm(domain)
        for key, defaults in DOMAIN_DEFAULT_FAMILIES.items():
            if key in dlow:
                fams.update(defaults)
    return fams


def distractor_out_of_anchor(
    option_text: str,
    anchor: Set[str],
    stem: str = "",
) -> bool:
    """True dacă varianta nu aparține familiei conceptuale a itemului."""
    if not anchor:
        return False
    text = str(option_text)
    for af in anchor:
        if is_cross_family_distractor(text, af, stem):
            return True
    opt_fams = set(primary_families(text))
    if opt_fams and not opt_fams & anchor:
        return True
    return False


def resolve_target_family(
    stem: str,
    domain: str,
    correct_texts: Sequence[str],
) -> Optional[str]:
    """Alege familia pentru reconstrucție — prioritate răspuns corect + enunț."""
    anchor = anchor_families(stem, domain, correct_texts)
    if not anchor:
        return family_from_stem(stem, domain)

    stem_f = family_from_stem(stem, domain)
    if stem_f and stem_f in anchor:
        return stem_f

    if correct_texts:
        scored: Dict[str, int] = {}
        for ct in correct_texts:
            for f in primary_families(str(ct)):
                scored[f] = scored.get(f, 0) + 2
        for f in primary_families(stem, domain):
            scored[f] = scored.get(f, 0) + 1
        if scored:
            return max(scored.items(), key=lambda x: (x[1], x[0]))[0]

    return next(iter(anchor)) if anchor else stem_f


def balance_length(text: str, target: int = 72) -> str:
    t = (text or "").strip()
    if len(t) <= target + 15:
        return t[0].upper() + t[1:] if t and t[0].islower() else t
    return t
