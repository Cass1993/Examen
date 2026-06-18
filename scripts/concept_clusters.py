"""Itemi cu variante omogene — concepte, modele, abordări terapeutice."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

ConceptSpec = Dict[str, Any]

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


# label_key → specificație item
CONCEPT_SPECS: Dict[str, ConceptSpec] = {
    "abordarea transdiagnostică": {
        "stem": "În psihoterapie, abordarea transdiagnostică se concentrează mai ales pe:",
        "options": {
            "a": "mecanisme comune care pot menține tulburări diferite, nu pe eticheta diagnostică izolată",
            "b": "aplicarea unei tehnici separate pentru fiecare simptom izolat, fără mecanism comun",
            "c": "stabilirea unui diagnostic unic și aplicarea rigidă a unui protocol fără adaptare",
            "d": "evaluarea personalității prin mai multe surse înaintea oricărei intervenții terapeutice",
        },
        "correct": "a",
    },
    "studiile gemelare": {
        "stem": "În genetica comportamentală, studiile gemelare sunt folosite mai ales pentru:",
        "options": {
            "a": "estimarea contribuției relative a factorilor genetici și de mediu la diferențele individuale",
            "b": "separarea directă a influențelor genetice aditive, mediului comun și mediului neîmpărtășit fără comparație între gemeni",
            "c": "modificarea expresiei genelor prin intervenții standardizate de învățare",
            "d": "evaluarea atașamentului prin procedura Situația stranie",
        },
        "correct": "a",
        "aliases": [
            "metodă care compară asemănarea gemenilor",
            "eritabilitatea",
            "studiile de gemeni",
            "abordarea idiografică",
            "modelul psihoticism",
        ],
    },
    "clusterul a": {
        "stem": "Clusterul A al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "stiluri dramatice, emoționale sau impulsive",
            "b": "stiluri anxioase, temătoare sau dependente",
            "c": "stiluri ciudate, excentrice sau neobișnuite",
            "d": "stiluri perfecționiste, rigide sau controlante",
        },
        "correct": "c",
        "aliases": ["cluster a", "tulburări din clusterul a"],
    },
    "clusterul b": {
        "stem": "Clusterul B al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "stiluri ciudate, excentrice sau neobișnuite",
            "b": "stiluri dramatice, emoționale sau impulsive",
            "c": "stiluri anxioase, temătoare sau dependente",
            "d": "stiluri perfecționiste, rigide sau controlante",
        },
        "correct": "b",
        "aliases": ["cluster b", "tulburări din clusterul b"],
    },
    "job enlargement": {
        "stem": "În proiectarea postului, job enlargement (lărgirea postului) se referă mai ales la:",
        "options": {
            "a": "adăugarea de sarcini variate la același nivel de responsabilitate",
            "b": "creșterea responsabilității, autonomiei și profunzimii postului",
            "c": "alternarea periodică a angajatului între posturi sau secțiuni diferite",
            "d": "măsura în care postul permite realizarea unei lucrări complete și identificabile",
        },
        "correct": "a",
        "aliases": ["lărgirea postului", "lărgire post"],
    },
    "job enrichment": {
        "stem": "În proiectarea postului, job enrichment (îmbogățirea postului) presupune mai ales:",
        "options": {
            "a": "creșterea responsabilității, autonomiei și profunzimii postului",
            "b": "adăugarea de sarcini variate la același nivel de responsabilitate",
            "c": "alternarea periodică a angajatului între posturi sau secțiuni diferite",
            "d": "măsura în care postul cere activități și abilități diverse",
        },
        "correct": "a",
        "aliases": ["îmbogățirea postului", "îmbogățire post"],
    },
    "clusterul c": {
        "stem": "Clusterul C al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "stiluri ciudate, excentrice sau neobișnuite",
            "b": "stiluri dramatice, emoționale sau impulsive",
            "c": "stiluri anxioase, temătoare sau dependente",
            "d": "stiluri perfecționiste, rigide sau controlante",
        },
        "correct": "c",
        "aliases": ["cluster c", "tulburări din clusterul c"],
    },
    "psihoterapia cognitiv-comportamentală": {
        "stem": "În psihoterapia cognitiv-comportamentală, intervenția vizează mai ales:",
        "options": {
            "a": "relația dintre gânduri, emoții și comportamente și modificarea patternurilor disfuncționale",
            "b": "explorarea exclusivă a conflictelor inconștiente și a transferului în relația terapeutică",
            "c": "acceptarea necondiționată și dezvoltarea congruenței dintre sine și experiență",
            "d": "restructurarea sistemului familial fără lucrul direct cu cognițiile individuale",
        },
        "correct": "a",
    },
    "psihoterapia psihodinamică": {
        "stem": "În psihoterapia psihodinamică, intervenția se centrează mai ales pe:",
        "options": {
            "a": "procese inconștiente, conflicte intrapsihice, mecanisme de apărare și relația terapeutică",
            "b": "restructurarea cognitivă a gândurilor automate fără explorarea conflictelor timpurii",
            "c": "procese comune transdiagnostice precum evitarea experiențială la mai multe tulburări",
            "d": "stabilirea obiectivelor SMART și monitorizarea consecințelor comportamentale",
        },
        "correct": "a",
    },
    "psihoterapia umanist-experiențială": {
        "stem": "În abordarea umanist-experiențială, intervenția pune accent pe:",
        "options": {
            "a": "experiența subiectivă, autenticitate, dezvoltare personală și relația terapeutică centrată pe persoană",
            "b": "protocoluri standardizate pentru fiecare diagnostic, aplicate rigid",
            "c": "identificarea gândurilor distorsionate și testarea lor prin experimente comportamentale",
            "d": "interpretarea simbolurilor din vis și a transferului ca unic mecanism de schimbare",
        },
        "correct": "a",
    },
    "psihoterapia de familie": {
        "stem": "În psihoterapia de familie, intervenția presupune mai ales:",
        "options": {
            "a": "înțelegerea simptomului în contextul sistemului relațional și a patternurilor de interacțiune",
            "b": "lucrul exclusiv individual cu trăsăturile de personalitate, fără context relațional",
            "c": "aplicarea unui protocol transdiagnostic identic indiferent de structura familiei",
            "d": "evaluarea aptitudinilor cognitive prin teste standardizate înaintea oricărei intervenții",
        },
        "correct": "a",
    },
    "integrarea în psihoterapie": {
        "stem": "Integrarea eclectică în psihoterapie presupune:",
        "options": {
            "a": "combinarea coerentă a tehnicilor sau teoriilor din mai multe orientări, adaptată cazului",
            "b": "alternarea aleatorie a tehnicilor fără cadru teoretic comun",
            "c": "aplicarea exclusivă a unui singur protocol manualizat pentru fiecare diagnostic",
            "d": "renunțarea la formularea de caz în favoarea unor tehnici izolate",
        },
        "correct": "a",
    },
    "terapia de acceptare și angajament": {
        "stem": "Terapia de acceptare și angajament (ACT) se bazează mai ales pe:",
        "options": {
            "a": "acceptare, contact cu experiența prezentă, valori personale și flexibilitate psihologică",
            "b": "reinterpretarea viselor și analiza transferului în relația terapeutică",
            "c": "eliminarea completă a simptomelor prin control strict al gândurilor",
            "d": "restructurarea ierarhiei familiale fără lucrul cu evitarea experiențială",
        },
        "correct": "a",
        "aliases": ["act", "acceptare și angajament"],
    },
    "terapia dialectic-comportamentală": {
        "stem": "Terapia dialectic-comportamentală (DBT) combină mai ales:",
        "options": {
            "a": "validare emoțională, strategii de reglare și schimbare comportamentală în context dialectic",
            "b": "explorarea exclusivă a stadiilor psihosexuale din copilărie",
            "c": "aplicarea unui protocol transdiagnostic identic pentru toate tulburările de personalitate",
            "d": "evaluarea intereselor vocaționale prin inventare standardizate",
        },
        "correct": "a",
        "aliases": ["dbt", "dialectic-comportamentală"],
    },
    "terapia focalizată pe emoții": {
        "stem": "Terapia focalizată pe emoții (EFT) pune accent pe:",
        "options": {
            "a": "procesarea emoțiilor, transformarea emoțiilor primare și consolidarea atașamentului",
            "b": "modificarea consecințelor comportamentale fără explorarea emoțiilor",
            "c": "interpretarea conflictelor inconștiente ca singur mecanism de schimbare",
            "d": "stabilirea diagnosticului și aplicarea rigidă a unui protocol CBT",
        },
        "correct": "a",
        "aliases": [
            "eft",
            "emotion-focused",
            "abordare centrată pe procesarea și transformarea emoțiilor",
            "procesarea și transformarea emoțiilor",
        ],
    },
    "terapia schemelor": {
        "stem": "Terapia schemelor (Schema Therapy) vizează mai ales:",
        "options": {
            "a": "scheme cognitive-emotionale dezvoltate timpuriu și strategiile de coping disfuncționale",
            "b": "procese transdiagnostice comune fără lucrul cu schemele timpurii",
            "c": "acceptarea necondiționată ca singură intervenție, fără restructurare cognitivă",
            "d": "analiza factorială a trăsăturilor fără intervenție terapeutică",
        },
        "correct": "a",
        "aliases": ["schema therapy", "scheme"],
    },
    "modelul hackman și oldham": {
        "stem": "Modelul Hackman și Oldham postulează că motivația la muncă este influențată mai ales de:",
        "options": {
            "a": "caracteristicile postului: varietatea aptitudinilor, identitatea sarcinii, semnificația, autonomia și feedbackul",
            "b": "doar nivelul salarial, fără alte caracteristici intrinseci ale muncii",
            "c": "exclusiv trăsăturile de personalitate Big Five, independent de designul postului",
            "d": "procedurile statistice de eșantionare și puterea testului",
        },
        "correct": "a",
    },
    "modelul cerințe-resurse ale postului": {
        "stem": "Modelul cerințelor și resurselor postului (JD-R) postulează că:",
        "options": {
            "a": "echilibrul dintre cerințele jobului și resursele disponibile influențează starea de bine și performanța",
            "b": "doar cerințele cognitive ale postului contează, resursele fiind neglijabile",
            "c": "motivația depinde exclusiv de recompensele extrinseci, nu de contextul muncii",
            "d": "validitatea de criteriu este suficientă pentru a explica stresul ocupațional",
        },
        "correct": "a",
        "aliases": ["modelul cerințe-resurse", "jd-r"],
    },
}

# index alias → key
_ALIAS_INDEX: Dict[str, str] = {}


def _build_alias_index() -> None:
    if _ALIAS_INDEX:
        return
    for key, spec in CONCEPT_SPECS.items():
        _ALIAS_INDEX[_norm(key)] = key
        for alias in spec.get("aliases", []):
            _ALIAS_INDEX[_norm(alias)] = key
        # fără articol
        for prefix in ("modelul ", "abordarea ", "terapia "):
            if key.startswith(prefix):
                _ALIAS_INDEX[_norm(key[len(prefix):])] = key


def _clean_label(label: str) -> str:
    key = _norm(label)
    key = re.sub(r"\([^)]*\)", " ", key)
    key = re.sub(r"\s+", " ", key).strip()
    return key


def lookup_concept(label: str) -> Optional[ConceptSpec]:
    _build_alias_index()
    key = _clean_label(label)
    if key in _ALIAS_INDEX:
        return CONCEPT_SPECS[_ALIAS_INDEX[key]]
    for alias, spec_key in _ALIAS_INDEX.items():
        if len(alias) > 8 and (alias in key or key in alias):
            return CONCEPT_SPECS[spec_key]
    # potriviri tematice
    if "transdiagnostic" in key:
        return CONCEPT_SPECS["abordarea transdiagnostică"]
    if "acceptare" in key and "angajament" in key:
        return CONCEPT_SPECS["terapia de acceptare și angajament"]
    if "dialectic" in key and "comportamental" in key:
        return CONCEPT_SPECS["terapia dialectic-comportamentală"]
    if "focalizat" in key and "emoț" in key:
        return CONCEPT_SPECS["terapia focalizată pe emoții"]
    if "emoț" in key and ("procesar" in key or "transform" in key):
        return CONCEPT_SPECS["terapia focalizată pe emoții"]
    if "schema" in key and "terap" in key:
        return CONCEPT_SPECS["terapia schemelor"]
    if "cognitiv" in key and "comportamental" in key and "psihoterap" in key:
        return CONCEPT_SPECS["psihoterapia cognitiv-comportamentală"]
    if "psihodinamic" in key:
        return CONCEPT_SPECS["psihoterapia psihodinamică"]
    if "hackman" in key and "oldham" in key:
        return CONCEPT_SPECS["modelul hackman și oldham"]
    if "cerințe" in key and "resurse" in key:
        return CONCEPT_SPECS["modelul cerințe-resurse ale postului"]
    if "gemen" in key and ("monozig" in key or "dizig" in key or "eritabil" in key):
        return CONCEPT_SPECS["studiile gemelare"]
    if "poligenic" in key:
        from scripts.genetics_epigenetics_specs import SINGLE_SPECS
        return SINGLE_SPECS.get("efectul poligenic" if "efect" in key else "scorul poligenic")
    if "cluster" in key and " a" in f" {key} ":
        return CONCEPT_SPECS["clusterul a"]
    if "cluster" in key and " b" in f" {key} ":
        return CONCEPT_SPECS["clusterul b"]
    if "cluster" in key and " c" in f" {key} ":
        return CONCEPT_SPECS["clusterul c"]
    if "enlargement" in key or "lărgire" in key:
        return CONCEPT_SPECS["job enlargement"]
    if "enrichment" in key or "îmbogățire" in key:
        return CONCEPT_SPECS["job enrichment"]
    return None


def rotate_options(
    spec: ConceptSpec, seed: int
) -> Tuple[str, Dict[str, str], str]:
    """Rotește opțiunile pentru varietate între duplicate."""
    letters = ["a", "b", "c", "d"]
    opts = spec["options"]
    correct_letter = str(spec["correct"]).lower()
    correct_text = opts[correct_letter]
    ordered = [opts[k] for k in letters]
    offset = seed % 4
    rotated = ordered[offset:] + ordered[:offset]
    new_opts = {letters[i]: rotated[i] for i in range(4)}
    new_correct = letters[rotated.index(correct_text)]
    return spec["stem"], new_opts, new_correct


LABEL_PATTERNS = [
    re.compile(
        r"^Care concept corespunde descrierii:\s*(.+?)\?\s*$", re.I | re.DOTALL
    ),
    re.compile(r"Modelul «(.+?)» postulează că:\s*$", re.I),
    re.compile(r"Abordarea «(.+?)» se bazează pe:\s*$", re.I),
    re.compile(r"^În [^,]+, «(.+?)» (?:descrie|se referă la):\s*$", re.I),
    re.compile(r"^În [^,]+, (.+?) (?:descrie|se referă la):\s*$", re.I),
    re.compile(r"^(.+?) se referă cel mai bine la:\s*$", re.I),
    re.compile(r"^(.+?) descrie:\s*$", re.I),
    re.compile(r"^«(.+?)» descrie mai ales:\s*$", re.I),
]


def extract_concept_label(stem: str) -> Optional[str]:
    t = (stem or "").strip()
    if re.search(r"aparțin (?:domeniului|explicit)", t, re.IGNORECASE):
        return None
    for pat in LABEL_PATTERNS:
        m = pat.match(t)
        if m:
            return m.group(1).strip()
    m = re.search(r"«([^»]+)»", t)
    return m.group(1).strip() if m else None


def build_concept_item(
    label: str, seed: int = 0
) -> Optional[Tuple[str, Dict[str, str], str]]:
    spec = lookup_concept(label)
    if not spec:
        return None
    return rotate_options(spec, seed)
