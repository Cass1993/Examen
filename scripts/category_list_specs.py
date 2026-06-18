"""Itemi pentru liste conceptuale — stiluri parentale, atașament, Piaget etc."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

CategoryItem = Dict[str, Any]

# topic normalizat → cluster termeni
TOPIC_CLUSTER_MAP: Dict[str, str] = {
    "stiluri parentale": "stiluri_parentale",
    "stil parental": "stiluri_parentale",
    "tipuri de atașament": "atașament",
    "tipuri de atasament": "atașament",
    "atașament": "atașament",
    "stadii cognitive piaget": "piaget_stadii",
    "stadii piaget": "piaget_stadii",
    "teorii ale învățării": "teorii_invatare",
    "teorii ale invatarii": "teorii_invatare",
    "dimensiuni big five": "big_five",
    "scale de măsurare": "scale_masurare",
}

TERM_POOLS: Dict[str, List[str]] = {
    "stiluri_parentale": [
        "autoritativ",
        "autoritar",
        "permisiv",
        "neglijent/neimplicat",
    ],
    "atașament": [
        "securizant",
        "evitant",
        "ambivalent/rezistent",
        "dezorganizat",
    ],
    "piaget_stadii": [
        "senzorio-motor",
        "preoperațional",
        "operațional concret",
        "formal operațional",
    ],
    "teorii_invatare": [
        "condiționarea clasică",
        "condiționarea operantă",
        "învățarea observațională",
        "constructivismul",
    ],
    "big_five": [
        "neuroticismul",
        "extraversia",
        "deschiderea către experiență",
        "agreabilitatea",
        "conștiinciozitatea",
    ],
    "scale_masurare": [
        "nominală",
        "ordinală",
        "de interval",
        "de raport",
    ],
}

# termeni din alt cluster — înlocuiri când apar ca distractori greșiți
CROSS_CLUSTER_MARKERS: Dict[str, Tuple[str, ...]] = {
    "stiluri_parentale": (
        "evitant", "securizant", "dezorganizat", "ambivalent", "atașament",
        "piaget", "senzorio", "vygotsky", "freud", "id", "superego",
    ),
    "atașament": (
        "autoritativ", "autoritar", "permisiv", "neglijent", "parental",
        "piaget", "senzorio", "big five", "extraversia",
    ),
    "piaget_stadii": (
        "autoritativ", "evitant", "vygotsky", "bandura", "skinner",
        "validitate", "anova",
    ),
    "teorii_invatare": (
        "atașament", "piaget", "zona proxim", "vygotsky", "big five",
        "validitate de criteriu",
    ),
    "big_five": (
        "id", "superego", "ego", "vygotsky", "piaget", "atașament",
        "autoritar", "evitant",
    ),
    "scale_masurare": (
        "anova", "pearson", "terapie", "atașament", "big five",
    ),
}

SINGLE_SPECS: Dict[str, List[CategoryItem]] = {
    "stiluri_parentale": [
        {
            "stem": "Stilul parental caracterizat prin căldură ridicată și limite clare este:",
            "options": {
                "a": "autoritar",
                "b": "autoritativ",
                "c": "permisiv",
                "d": "neglijent/neimplicat",
            },
            "correct": "b",
        },
        {
            "stem": "Stilul parental cu control ridicat și căldură scăzută este:",
            "options": {
                "a": "autoritativ",
                "b": "autoritar",
                "c": "permisiv",
                "d": "neglijent/neimplicat",
            },
            "correct": "b",
        },
        {
            "stem": "Stilul parental cu căldură ridicată și limite reduse este:",
            "options": {
                "a": "autoritar",
                "b": "autoritativ",
                "c": "permisiv",
                "d": "neglijent/neimplicat",
            },
            "correct": "c",
        },
        {
            "stem": "Stilul parental cu căldură scăzută și implicare redusă este:",
            "options": {
                "a": "autoritar",
                "b": "autoritativ",
                "c": "permisiv",
                "d": "neglijent/neimplicat",
            },
            "correct": "d",
        },
    ],
    "atașament": [
        {
            "stem": "Tipul de atașament în care copilul folosește îngrijitorul ca bază de siguranță este:",
            "options": {
                "a": "securizant",
                "b": "evitant",
                "c": "ambivalent/rezistent",
                "d": "dezorganizat",
            },
            "correct": "a",
        },
        {
            "stem": "Tipul de atașament caracterizat prin minimizarea contactului la reunire este:",
            "options": {
                "a": "securizant",
                "b": "evitant",
                "c": "ambivalent/rezistent",
                "d": "dezorganizat",
            },
            "correct": "b",
        },
        {
            "stem": "Tipul de atașament cu căutare de apropiere și rezistență la calmare este:",
            "options": {
                "a": "securizant",
                "b": "evitant",
                "c": "ambivalent/rezistent",
                "d": "dezorganizat",
            },
            "correct": "c",
        },
    ],
    "piaget_stadii": [
        {
            "stem": "Stadiul Piaget în care apare permanența obiectului este:",
            "options": {
                "a": "senzorio-motor",
                "b": "preoperațional",
                "c": "operațional concret",
                "d": "formal operațional",
            },
            "correct": "a",
        },
        {
            "stem": "Stadiul Piaget asociat cu gândirea egocentrică și jocul simbolic este:",
            "options": {
                "a": "senzorio-motor",
                "b": "preoperațional",
                "c": "operațional concret",
                "d": "formal operațional",
            },
            "correct": "b",
        },
        {
            "stem": "Stadiul Piaget în care copilul operează cu raționament concret asupra obiectelor este:",
            "options": {
                "a": "senzorio-motor",
                "b": "preoperațional",
                "c": "operațional concret",
                "d": "formal operațional",
            },
            "correct": "c",
        },
        {
            "stem": "Stadiul Piaget al raționamentului ipotetico-deductiv este:",
            "options": {
                "a": "senzorio-motor",
                "b": "preoperațional",
                "c": "operațional concret",
                "d": "formal operațional",
            },
            "correct": "d",
        },
    ],
    "teorii_invatare": [
        {
            "stem": "Teoria învățării asociată cu Ivan P. Pavlov este:",
            "options": {
                "a": "condiționarea clasică",
                "b": "condiționarea operantă",
                "c": "învățarea observațională",
                "d": "constructivismul",
            },
            "correct": "a",
        },
        {
            "stem": "Teoria învățării asociată cu Burrhus F. Skinner este:",
            "options": {
                "a": "condiționarea clasică",
                "b": "condiționarea operantă",
                "c": "învățarea observațională",
                "d": "constructivismul",
            },
            "correct": "b",
        },
        {
            "stem": "Teoria învățării asociată cu Albert Bandura este:",
            "options": {
                "a": "condiționarea clasică",
                "b": "condiționarea operantă",
                "c": "învățarea observațională",
                "d": "constructivismul",
            },
            "correct": "c",
        },
    ],
    "big_five": [
        {
            "stem": "Dimensiunea Big Five asociată cu sociabilitate și energie pozitivă este:",
            "options": {
                "a": "neuroticismul",
                "b": "extraversia",
                "c": "agreabilitatea",
                "d": "conștiinciozitatea",
            },
            "correct": "b",
        },
        {
            "stem": "Dimensiunea Big Five asociată cu cooperare și încredere interpersonală este:",
            "options": {
                "a": "neuroticismul",
                "b": "extraversia",
                "c": "agreabilitatea",
                "d": "deschiderea către experiență",
            },
            "correct": "c",
        },
    ],
    "scale_masurare": [
        {
            "stem": "Scala de măsurare care clasifică observațiile în categorii fără ordine internă este:",
            "options": {
                "a": "nominală",
                "b": "ordinală",
                "c": "de interval",
                "d": "de raport",
            },
            "correct": "a",
        },
        {
            "stem": "Scala de măsurare cu ordine între categorii, dar fără distanțe egale, este:",
            "options": {
                "a": "nominală",
                "b": "ordinală",
                "c": "de interval",
                "d": "de raport",
            },
            "correct": "b",
        },
    ],
}

MULTI_STEMS: Dict[str, str] = {
    "stiluri_parentale": (
        "Care dintre următoarele sunt stiluri parentale descrise frecvent "
        "în psihologia dezvoltării?"
    ),
    "atașament": (
        "Care dintre următoarele sunt tipuri de atașament descrise în teoria atașamentului?"
    ),
    "piaget_stadii": (
        "Care dintre următoarele sunt stadii ale dezvoltării cognitive, în teoria lui Jean Piaget?"
    ),
    "teorii_invatare": (
        "Care dintre următoarele sunt teorii sau orientări ale învățării discutate în psihologie?"
    ),
    "big_five": (
        "Care dintre următoarele sunt dimensiuni ale modelului Big Five?"
    ),
    "scale_masurare": (
        "Care dintre următoarele sunt tipuri de scale de măsurare în psihometrie?"
    ),
    "cluster_personalitate": (
        "Care dintre următoarele tulburări aparțin Clusterului A al tulburărilor de personalitate?"
    ),
}

CLUSTER_A_DISORDERS = [
    "tulburarea paranoidă de personalitate",
    "tulburarea schizoidă de personalitate",
    "tulburarea schizotipală de personalitate",
    "tulburarea antisocială de personalitate",
]

CLUSTER_PERSONALITY_SINGLE: List[CategoryItem] = [
    {
        "stem": "Clusterul A al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "dramatic, emoțional, impulsiv",
            "b": "anxios, temător, dependent",
            "c": "ciudat, excentric, neobișnuit",
            "d": "perfectionist, rigid, controlant",
        },
        "correct": "c",
    },
    {
        "stem": "Clusterul B al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "dramatic, emoțional, impulsiv",
            "b": "anxios, temător, dependent",
            "c": "ciudat, excentric, neobișnuit",
            "d": "perfectionist, rigid, controlant",
        },
        "correct": "a",
    },
    {
        "stem": "Clusterul C al tulburărilor de personalitate este descris în general prin:",
        "options": {
            "a": "dramatic, emoțional, impulsiv",
            "b": "anxios, temător, dependent",
            "c": "ciudat, excentric, neobișnuit",
            "d": "perfectionist, rigid, controlant",
        },
        "correct": "b",
    },
]


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def topic_to_cluster(topic: str) -> Optional[str]:
    key = _norm(topic.strip("«»"))
    if key in TOPIC_CLUSTER_MAP:
        return TOPIC_CLUSTER_MAP[key]
    for phrase, cluster in TOPIC_CLUSTER_MAP.items():
        if phrase in key or key in phrase:
            return cluster
    return None


def pick_cluster_disorder_spec(stem: str, seed: int) -> Optional[CategoryItem]:
    m = re.search(r"Clusterului\s+([ABC])\b", stem, re.I)
    if not m:
        return None
    cluster = m.group(1).upper()
    if cluster == "A":
        stem_new = (
            "Care dintre următoarele tulburări aparțin Clusterului A "
            "al tulburărilor de personalitate?"
        )
        opts = {
            "a": "tulburarea paranoidă de personalitate",
            "b": "tulburarea schizoidă de personalitate",
            "c": "tulburarea schizotipală de personalitate",
            "d": "tulburarea borderline de personalitate",
        }
        return {
            "stem": stem_new,
            "options": opts,
            "correct": ["a", "b", "c"],
            "kind": "multi",
        }
    if cluster == "C":
        stem_new = (
            "Care dintre următoarele tulburări aparțin Clusterului C "
            "al tulburărilor de personalitate?"
        )
        opts = {
            "a": "tulburarea dependentă de personalitate",
            "b": "tulburarea evitantă de personalitate",
            "c": "tulburarea obsesiv-compulsivă de personalitate",
            "d": "tulburarea borderline de personalitate",
        }
        return {
            "stem": stem_new,
            "options": opts,
            "correct": ["a", "b", "c"],
            "kind": "multi",
        }
    spec = CLUSTER_PERSONALITY_SINGLE[seed % len(CLUSTER_PERSONALITY_SINGLE)]
    return {
        "stem": spec["stem"],
        "options": dict(spec["options"]),
        "correct": [spec["correct"]],
        "kind": "single",
    }


def pick_spec(cluster: str, seed: int, prefer_multi: bool = False) -> Optional[CategoryItem]:
    if prefer_multi and cluster in MULTI_STEMS and cluster in TERM_POOLS:
        terms = TERM_POOLS[cluster][:4]
        opts = {letter: terms[i] for i, letter in enumerate("abcd")}
        return {
            "stem": MULTI_STEMS[cluster],
            "options": opts,
            "correct": list("abcd"),
            "kind": "multi",
        }
    singles = SINGLE_SPECS.get(cluster, [])
    if singles:
        spec = singles[seed % len(singles)]
        return {
            "stem": spec["stem"],
            "options": dict(spec["options"]),
            "correct": [spec["correct"]],
            "kind": "single",
        }
    if cluster in MULTI_STEMS:
        terms = TERM_POOLS.get(cluster, [])[:4]
        if len(terms) == 4:
            return {
                "stem": MULTI_STEMS[cluster],
                "options": {l: terms[i] for i, l in enumerate("abcd")},
                "correct": list("abcd"),
                "kind": "multi",
            }
    return None


def sanitize_options_for_cluster(
    options: Dict[str, str], cluster: str
) -> Dict[str, str]:
    """Înlocuiește termeni din alt cluster în setul de variante."""
    pool = TERM_POOLS.get(cluster, [])
    markers = CROSS_CLUSTER_MARKERS.get(cluster, ())
    if not pool:
        return options

    used = {_norm(v) for v in options.values()}
    out: Dict[str, str] = {}
    pool_idx = 0
    for letter, text in options.items():
        low = _norm(text)
        if any(m in low for m in markers):
            while pool_idx < len(pool) and _norm(pool[pool_idx]) in used:
                pool_idx += 1
            if pool_idx < len(pool):
                text = pool[pool_idx]
                pool_idx += 1
        used.add(_norm(text))
        out[letter] = text
    return out
