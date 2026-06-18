"""Clustere omogene — termeni scurți, definiții și mapare din enunț."""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Sequence, Tuple

# --- Termeni scurți (descriere → etichetă) ---
TERM_CLUSTERS: Dict[str, List[str]] = {
    "hackman_oldham": [
        "Varietatea aptitudinilor",
        "Identitatea sarcinii",
        "Semnificația sarcinii",
        "Autonomia",
        "Feedbackul din muncă",
    ],
    "performanta_munca": [
        "Performanța în sarcină",
        "Performanța contextuală",
        "Comportamentul civic organizațional",
        "Comportamentul contraproductiv",
    ],
    "motivatie_implicare": [
        "Implicarea în muncă",
        "Satisfacția profesională",
        "Motivația intrinsecă",
        "Motivația extrinsecă",
    ],
    "job_design": [
        "Îmbogățirea postului",
        "Lărgirea postului",
        "Rotirea posturilor",
        "Analiza muncii",
    ],
    "evaluare_performanta": [
        "Efectul halo",
        "Efectul de seriozitate",
        "Efectul de lenitate",
        "Tendința centrală",
        "Criteriul deficient",
        "Criteriul contaminat",
        "Criteriul efectiv",
        "Criteriul teoretic",
    ],
    "surse_360": [
        "Superiorul",
        "Colegii",
        "Subordonații",
        "Autoevaluarea",
        "Clienții externi",
    ],
    "stresori_ocupationali": [
        "Supraîncărcarea muncii",
        "Ambiguitatea de rol",
        "Conflictul de rol",
        "Lipsa controlului",
        "Condițiile de muncă",
    ],
    "stres_rol": [
        "Burnoutul",
        "Stresul ocupațional",
        "Conflictul de rol",
        "Ambiguitatea rolului",
    ],
    "teoria_asteptarii": [
        "Teoria așteptării a lui Victor H. Vroom",
        "Motivația intrinsecă",
        "Motivația extrinsecă",
        "Instrumentalitatea",
    ],
    "cultura_climat_org": [
        "Cultura organizațională",
        "Climatul organizațional",
        "Compatibilitatea persoană-organizație",
        "Satisfacția profesională",
    ],
    "documente_post": [
        "Fișa postului",
        "Specificația postului",
        "Descrierea postului",
        "Analiza muncii",
    ],
    "atașament": [
        "Securizant",
        "Evitant",
        "Ambivalent/rezistent",
        "Dezorganizat",
    ],
    "stiluri_parentale": [
        "Autoritativ",
        "Autoritar",
        "Permisiv",
        "Neglijent",
    ],
    "big_five": [
        "Neuroticismul",
        "Extraversia",
        "Deschiderea către experiență",
        "Agreabilitatea",
        "Conștiinciozitatea",
    ],
    "statistica_descriptiva": [
        "Media aritmetică",
        "Mediana",
        "Modul",
        "Abaterea standard",
        "Tendința centrală",
    ],
    "validitate_fidelitate": [
        "Validitatea de conținut",
        "Validitatea de construct",
        "Validitatea de criteriu",
        "Validitatea incrementală",
        "Fidelitatea test-retest",
    ],
    "criterii_performanta": [
        "Criteriul deficient",
        "Criteriul contaminat",
        "Criteriul efectiv",
        "Criteriul teoretic",
    ],
    "ksao": [
        "KSAO",
        "Cunoștințe, aptitudini, abilități și alte caracteristici",
        "Analiza muncii",
        "Profilul postului",
    ],
}

# --- Definiții omogene (etichetă → descriere) ---
DEFINITION_CLUSTERS: Dict[str, List[str]] = {
    "hackman_oldham": [
        "Măsura în care postul cere folosirea mai multor abilități",
        "Măsura în care postul permite realizarea unei lucrări complete și identificabile",
        "Măsura în care lucrarea are un impact semnificativ asupra vieții altor persoane",
        "Gradul de libertate și discreționalitate în programarea muncii",
        "Informația clară primită din activitate despre eficiența performanței",
    ],
    "motivatie_implicare": [
        "Atitudine evaluativ-afectivă față de muncă",
        "Stare pozitivă caracterizată prin vigoare, dedicare și absorbție",
        "Realizarea unei activități pentru interesul sau satisfacția ei proprie",
        "Realizarea unei activități pentru recompense sau consecințe externe",
    ],
    "performanta_munca": [
        "Realizarea activităților tehnice și centrale ale postului",
        "Comportamente care susțin mediul social și organizațional al muncii",
        "Comportament voluntar care susține colegii sau organizația",
        "Comportament care dăunează organizației, colegilor sau muncii",
    ],
    "evaluare_performanta": [
        "Tendința evaluatorului de a evita extremele și de a oferi scoruri medii",
        "Generalizarea unei impresii pozitive sau negative de pe o dimensiune pe altele",
        "Tendința de a acorda scoruri mai favorabile decât merită performanța reală",
        "Criteriu care omite aspecte relevante ale performanței",
    ],
    "stresori_ocupationali": [
        "Prezența unor cerințe incompatibile sau contradictorii ale rolului",
        "Neclaritatea așteptărilor, responsabilităților sau criteriilor de succes ale rolului",
        "Solicitări excesive de muncă raportate la resursele disponibile",
        "Lipsa informațiilor clare despre așteptările și responsabilitățile rolului",
    ],
    "documente_post": [
        "Descrierea sarcinilor, responsabilităților și condițiilor principale ale postului",
        "Descrierea activităților, operațiilor și responsabilităților postului",
        "Document care sintetizează cerințele, responsabilitățile și condițiile unui post",
        "Colectarea sistematică a informațiilor despre sarcini și cerințele postului",
    ],
    "validitate_fidelitate": [
        "Gradul în care itemii acoperă domeniul de conținut al constructului",
        "Măsura în care instrumentul evaluează constructul teoretic vizat",
        "Relația dintre scorul testului și un criteriu extern relevant",
        "Contribuția suplimentară a unui predictor peste metodele deja folosite",
    ],
    "norme_psihometrice": [
        "Reperele statistice obținute pe eșantioane relevante pentru interpretarea scorurilor",
        "Compararea scorului individual cu performanța unui grup de referință",
        "Transformarea scorurilor brute în scoruri standardizate pe baza normelor",
        "Stabilitatea scorurilor la administrări repetate în condiții similare",
        "Relația dintre scorul testului și un criteriu extern de performanță",
        "Gradul în care itemii acoperă domeniul de conținut al constructului",
    ],
}

# Mapare enunț (subșir) → cluster
STEM_CLUSTER_RULES: List[Tuple[str, str]] = [
    (r"surse.*360|evaluare\s*360", "surse_360"),
    (r"dimensiuni ale performanței", "performanta_munca"),
    (r"stresori ocupaționali", "stresori_ocupationali"),
    (r"supraîncărcare|ambiguitate.*rol|conflict.*rol|neclaritate.*rol", "stresori_ocupationali"),
    (r"tendința evaluatorului|efectului halo|eroarea halo|lenitate|seriozitate", "evaluare_performanta"),
    (r"criteriu deficient|criteriu contaminat|criteriu efectiv", "evaluare_performanta"),
    (r"varietatea aptitudinilor|identitatea sarcinii|semnificația sarcinii|autonomia|feedback.*munc", "hackman_oldham"),
    (r"postul cere folosirea|postul permite realizarea|libertatea angajatului|impact.*muncii", "hackman_oldham"),
    (r"performanța în sarcină|performanța contextuală|comportament civic|comportament contraproductiv", "performanta_munca"),
    (r"vigoare.*dedicare|implicare în muncă|implicarea în muncă", "motivatie_implicare"),
    (r"satisfacția profesională|atitudine evaluativ-afectivă", "motivatie_implicare"),
    (r"expectanță.*instrumentalitate|valență|vroom", "teoria_asteptarii"),
    (r"motivație intrinsecă|motivație extrinsecă|interes.*satisfacție.*proprie|recompense.*externe", "motivatie_implicare"),
    (r"îmbogățire|lărgire.*post|rotire.*post|job enrichment|job enlargement", "job_design"),
    (r"fișa postului|specificația postului|descrierea postului|descrierea sarcinilor", "documente_post"),
    (r"validitate|fidelitate|incrementală", "validitate_fidelitate"),
    (r"normele|normă|norme standardizate|standardizare", "norme_psihometrice"),
    (r"cunoștințe.*aptitudini|ksao", "ksao"),
    (r"compatibilitate.*organiza|valorile persoanei|cultura organiza|climat organiza", "cultura_climat_org"),
    (r"epuizare.*cinism|burnout", "stres_rol"),
    (r"training|formare|dezvoltare.*cunoștințe", "job_design"),
]

EXPLANATION_CLUSTER_HINTS: Dict[str, str] = {
    "hackman": "hackman_oldham",
    "oldham": "hackman_oldham",
    "360": "surse_360",
    "performanță": "performanta_munca",
    "implicare": "motivatie_implicare",
    "atașament": "atașament",
    "parental": "stiluri_parentale",
    "vroom": "teoria_asteptarii",
}

_LABEL_INDEX: Dict[str, str] = {}
_DEF_INDEX: Dict[str, str] = {}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _build_indexes() -> None:
    if _LABEL_INDEX:
        return
    aliases: Dict[str, List[str]] = {
        "hackman_oldham": ["Feedbackul", "Semnificația sarcinii", "Identitatea sarcinii", "Autonomia"],
        "performanta_munca": ["Performanța contextuală", "Performanța în sarcină"],
        "surse_360": ["Superiorul", "Subordonații", "Colegii", "Autoevaluarea"],
        "stresori_ocupationali": ["Ambiguitatea de rol", "Conflictul de rol", "Supraîncărcarea muncii"],
    }
    for cluster_id, members in TERM_CLUSTERS.items():
        for label in members + aliases.get(cluster_id, []):
            _LABEL_INDEX[_norm(label)] = cluster_id
    for cluster_id, members in DEFINITION_CLUSTERS.items():
        for defn in members:
            _DEF_INDEX[_norm(defn)] = cluster_id


def cluster_id_from_stem(description: str) -> Optional[str]:
    low = _norm(description)
    for pattern, cluster_id in STEM_CLUSTER_RULES:
        if re.search(pattern, low, re.IGNORECASE):
            return cluster_id
    return None


def cluster_id_from_explanation(explanation: str) -> Optional[str]:
    low = _norm(explanation)
    for hint, cluster_id in EXPLANATION_CLUSTER_HINTS.items():
        if hint in low:
            return cluster_id
    return None


def cluster_id_for_term(label: str, explanation: str = "", stem_desc: str = "") -> Optional[str]:
    _build_indexes()
    cid = cluster_id_from_stem(stem_desc)
    if cid:
        return cid
    key = _norm(label)
    if key in _LABEL_INDEX:
        return _LABEL_INDEX[key]
    if key in _DEF_INDEX:
        return _DEF_INDEX[key]
    cid = cluster_id_from_explanation(explanation)
    if cid:
        return cid
    for member_key, cluster_id in _LABEL_INDEX.items():
        if len(member_key) > 6 and (member_key in key or key in member_key):
            return cluster_id
    for member_key, cluster_id in _DEF_INDEX.items():
        if len(member_key) > 12 and (member_key in key or key in member_key):
            return cluster_id
    return None


def cluster_for_term(label: str) -> Optional[List[str]]:
    cid = cluster_id_for_term(label)
    return list(TERM_CLUSTERS[cid]) if cid and cid in TERM_CLUSTERS else None


def cluster_from_explanation(explanation: str) -> Optional[List[str]]:
    cid = cluster_id_from_explanation(explanation)
    return list(TERM_CLUSTERS[cid]) if cid and cid in TERM_CLUSTERS else None


def definitions_for_cluster(cluster_id: str) -> List[str]:
    return list(DEFINITION_CLUSTERS.get(cluster_id, []))


def terms_for_cluster(cluster_id: str) -> List[str]:
    return list(TERM_CLUSTERS.get(cluster_id, []))


def build_term_cluster_options(
    cluster: List[str], correct_label: str, seed: int
) -> Optional[Tuple[Dict[str, str], str]]:
    if len(cluster) < 4:
        return None
    letters = ["a", "b", "c", "d"]
    key = _norm(correct_label)
    correct_term = correct_label
    for term in cluster:
        nk = _norm(term)
        if nk == key or key in nk or nk in key:
            correct_term = term
            break

    offset = seed % len(cluster)
    ordered = cluster[offset:] + cluster[:offset]
    picked: List[str] = []
    for term in ordered:
        if term not in picked:
            picked.append(term)
        if len(picked) >= 4:
            break
    if correct_term not in picked:
        picked[-1] = correct_term

    options = {letters[i]: picked[i] for i in range(4)}
    correct_letter = letters[[_norm(v) for v in picked].index(_norm(correct_term))]
    return options, correct_letter


def build_definition_cluster_options(
    cluster: List[str], correct_def: str, seed: int
) -> Optional[Tuple[Dict[str, str], str]]:
    if len(cluster) < 4:
        return None
    letters = ["a", "b", "c", "d"]
    key = _norm(correct_def)
    correct_text = correct_def
    for defn in cluster:
        nk = _norm(defn)
        if nk == key or key in nk or nk in key:
            correct_text = defn
            break

    offset = seed % len(cluster)
    ordered = cluster[offset:] + cluster[:offset]
    picked: List[str] = []
    for defn in ordered:
        if defn not in picked:
            picked.append(defn)
        if len(picked) >= 4:
            break
    if correct_text not in picked:
        picked[-1] = correct_text

    options = {letters[i]: picked[i] for i in range(4)}
    correct_letter = letters[[_norm(v) for v in picked].index(_norm(correct_text))]
    return options, correct_letter


def replace_heterogeneous_options(
    options: Dict[str, str],
    correct: Sequence[str],
    pool: List[str],
    seed: int,
) -> Tuple[Dict[str, str], List[str], bool]:
    """Înlocuiește distractorii care nu sunt în pool; păstrează literele corecte."""
    used = {_norm(options[c]) for c in correct if c in options}
    new_options = dict(options)
    changed = False
    pool_norms = {_norm(p) for p in pool}

    for letter, opt in options.items():
        if letter in correct:
            continue
        if _norm(opt) in pool_norms:
            continue
        available = [p for p in pool if _norm(p) not in used]
        if not available:
            available = [p for p in pool if _norm(p) != _norm(opt)]
        if not available:
            continue
        idx = (seed + ord(letter)) % len(available)
        repl = available[idx]
        if _norm(repl) != _norm(opt):
            new_options[letter] = repl
            used.add(_norm(repl))
            changed = True
    new_correct = list(correct)
    return new_options, new_correct, changed


def contextual_stem_for_cluster(cluster_id: str, description: str) -> Optional[str]:
    from scripts.stem_templates import cap_definition

    desc = cap_definition(description.strip())
    templates = {
        "hackman_oldham": (
            "În modelul Hackman și Oldham, care componentă a postului este descrisă "
            f"astfel: {desc}?"
        ),
        "performanta_munca": (
            f"În evaluarea performanței la locul de muncă, care concept corespunde "
            f"descrierii: {desc}?"
        ),
        "motivatie_implicare": (
            f"În psihologia organizațională, care concept corespunde descrierii: {desc}?"
        ),
        "evaluare_performanta": (
            f"În evaluarea performanței, care concept corespunde descrierii: {desc}?"
        ),
        "surse_360": f"În evaluarea 360°, care sursă corespunde descrierii: {desc}?",
        "stresori_ocupationali": (
            f"În psihologia muncii, care stresor ocupațional corespunde descrierii: {desc}?"
        ),
        "atașament": (
            f"În teoria atașamentului, care concept corespunde descrierii: {desc}?"
        ),
        "stiluri_parentale": (
            f"În psihologia parentalității, care stil parental corespunde descrierii: {desc}?"
        ),
        "validitate_fidelitate": (
            f"În evaluarea psihologică, care tip de validitate sau fidelitate "
            f"corespunde descrierii: {desc}?"
        ),
        "documente_post": (
            f"În analiza posturilor, care document corespunde descrierii: {desc}?"
        ),
        "teoria_asteptarii": (
            f"În motivația la locul de muncă, care concept corespunde descrierii: {desc}?"
        ),
        "cultura_climat_org": (
            f"În psihologia organizațională, care concept corespunde descrierii: {desc}?"
        ),
    }
    return templates.get(cluster_id)
