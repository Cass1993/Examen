"""Context explicit pentru concepte vagi — enunț + variante omogene."""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

from scripts.concept_clusters import ConceptSpec, rotate_options
from scripts.domain_concept_specs import build_domain_concept_item

# lot pattern → prefix contextual
LOT_CONTEXT_RULES: List[Tuple[str, str]] = [
    (r"psihoterapie|etică", "În etica psihoterapiei"),
    (r"psihopatolog", "În psihopatologie"),
    (r"evaluare psihologic|metodolog", "În evaluarea psihologică"),
    (r"statistic", "În statistica aplicată cercetării psihologice"),
    (r"organizațional|muncii", "În psihologia organizațională și a muncii"),
    (r"personalit", "În psihologia personalității"),
    (r"dezvolt", "În psihologia dezvoltării"),
    (r"învățare|educaț", "În psihologia învățării"),
    (r"social", "În psihologia socială"),
    (r"cognitiv", "În psihologia cognitivă"),
]

# Spec-uri complete — enunț contextual + distractori din aceeași zonă
CONTEXT_SPECS: Dict[str, ConceptSpec] = {
    "relațiile duale": {
        "stem": "În etica psihoterapiei, relațiile duale se referă la:",
        "options": {
            "a": "relații suplimentare între terapeut și client, în afara cadrului terapeutic, care pot afecta limitele și obiectivitatea",
            "b": "protejarea informațiilor clientului în limitele legale și etice ale confidențialității",
            "c": "explicarea procesului terapeutic, a riscurilor, beneficiilor și drepturilor clientului",
            "d": "comunicarea empatică a înțelegerii experienței subiective a clientului",
        },
        "correct": "a",
        "aliases": ["relații duale", "relația duală"],
    },
    "transferul": {
        "stem": "În psihoterapia psihodinamică, transferul se referă la:",
        "options": {
            "a": "reacțiile și atitudinile clientului față de terapeut, influențate de relații semnificative din trecut",
            "b": "relații suplimentare terapeut-client în afara cadrului terapeutic",
            "c": "informarea clientului despre limitele, riscurile și drepturile în procesul terapeutic",
            "d": "protejarea confidențialității informațiilor obținute în relația terapeutică",
        },
        "correct": "a",
        "aliases": ["transfer", "transferul terapeutic"],
    },
    "consimțământul informat": {
        "stem": "În etica psihoterapiei, consimțământul informat presupune:",
        "options": {
            "a": "informarea clientului despre proces, limite, riscuri, beneficii și drepturi înainte de intervenție",
            "b": "relații suplimentare terapeut-client care pot afecta obiectivitatea",
            "c": "interpretarea conflictelor inconștiente ca mecanism principal de schimbare",
            "d": "protejarea datelor clientului fără explicarea scopului evaluării",
        },
        "correct": "a",
        "aliases": ["consimțământ informat"],
    },
    "competența profesională": {
        "stem": "În etica psihoterapiei, competența profesională presupune:",
        "options": {
            "a": "lucrul în limitele formării, supervizării și experienței validate ale terapeutului",
            "b": "relații duale acceptate dacă clientul își dă acordul verbal",
            "c": "aplicarea aceluiași protocol pentru toate cazurile, indiferent de formare",
            "d": "divulgarea informațiilor pentru a demonstra eficacitatea intervenției",
        },
        "correct": "a",
    },
    "atașamentul securizant": {
        "stem": "În teoria atașamentului, atașamentul securizant presupune:",
        "options": {
            "a": "folosirea figurii de atașament ca bază de siguranță și confort la explorare",
            "b": "minimizarea contactului și a semnalelor de nevoie la reunire cu îngrijitorul",
            "c": "căutare intensă de apropiere combinată cu rezistență și calmare dificilă",
            "d": "pattern contradictoriu sau dezorientat, fără strategie coerentă de atașament",
        },
        "correct": "a",
        "aliases": ["atașament securizant", "atașamentul"],
    },
    "validitatea de criteriu": {
        "stem": "În evaluarea psihologică, validitatea de criteriu indică:",
        "options": {
            "a": "relația dintre scorurile testului și un criteriu extern relevant de performanță",
            "b": "stabilitatea scorurilor la administrări repetate în condiții similare",
            "c": "gradul în care itemii acoperă domeniul de conținut al constructului",
            "d": "transformarea scorurilor brute prin norme standardizate",
        },
        "correct": "a",
        "aliases": ["validitatea", "validitate de criteriu"],
    },
    "fidelitatea test-retest": {
        "stem": "În evaluarea psihologică, fidelitatea test-retest indică:",
        "options": {
            "a": "stabilitatea scorurilor la administrări repetate în condiții similare",
            "b": "relația dintre scorul testului și un criteriu extern relevant",
            "c": "gradul în care itemii acoperă domeniul de conținut al constructului",
            "d": "proporția variației unei trăsături atribuită diferențelor genetice",
        },
        "correct": "a",
        "aliases": ["fidelitatea", "fidelitate test-retest"],
    },
    "criteriul contaminat": {
        "stem": "În evaluarea performanței, un criteriu contaminat este:",
        "options": {
            "a": "un criteriu influențat de factori irelevanți pentru performanța reală",
            "b": "un criteriu care omite aspecte relevante ale performanței evaluate",
            "c": "un criteriu definit teoretic, înainte de măsurarea efectivă",
            "d": "un criteriu măsurat direct în condiții reale de muncă",
        },
        "correct": "a",
        "aliases": ["criteriul contaminat"],
    },
    "eșantionul": {
        "stem": "În statistica inferențială, eșantionul se referă la:",
        "options": {
            "a": "submulțimea de participanți selectați din populația țintă pentru studiu",
            "b": "totalitatea indivizilor care îndeplinesc criteriile populației de interes",
            "c": "probabilitatea de a respinge ipoteza nulă atunci când este adevărată",
            "d": "mărimea efectului observat într-un studiu experimental",
        },
        "correct": "a",
        "aliases": ["eșantionul", "eșantionarea"],
    },
    "climatul clasei": {
        "stem": "În psihologia educației, climatul clasei se referă la:",
        "options": {
            "a": "calitatea relațiilor, normelor și siguranței psihologice din grupul școlar",
            "b": "distanța dintre nivelul actual de dezvoltare și cel atins cu sprijin adult",
            "c": "procedura de observare a atașamentului prin separări și reuniri scurte",
            "d": "stadiul în care copilul operează cu raționament abstract și ipotetico-deductiv",
        },
        "correct": "a",
        "aliases": ["climatul", "climatul clasei"],
    },
}

_ALIAS_INDEX: Dict[str, str] = {}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _build_alias_index() -> None:
    if _ALIAS_INDEX:
        return
    for key, spec in CONTEXT_SPECS.items():
        _ALIAS_INDEX[_norm(key)] = key
        for alias in spec.get("aliases", []):
            _ALIAS_INDEX[_norm(alias)] = key


def lookup_context_spec(label: str) -> Optional[ConceptSpec]:
    _build_alias_index()
    key = _norm(label.strip("«»"))
    if key in _ALIAS_INDEX:
        return CONTEXT_SPECS[_ALIAS_INDEX[key]]
    for alias, spec_key in _ALIAS_INDEX.items():
        if len(alias) > 5 and (alias in key or key in alias):
            return CONTEXT_SPECS[spec_key]
    return None


def context_prefix_for_lot(lot: str, label: str = "") -> str:
    blob = _norm(f"{lot} {label}")
    for pattern, prefix in LOT_CONTEXT_RULES:
        if re.search(pattern, blob, re.I):
            return prefix
    return "În psihologie"


def build_contextual_item(label: str, lot: str, seed: int = 0):
    spec = lookup_context_spec(label)
    if spec:
        return rotate_options(spec, seed)
    built = build_domain_concept_item(label, seed)
    if built:
        stem, opts, corr = built
        if not stem.lower().startswith("în "):
            prefix = context_prefix_for_lot(lot, label)
            label_clean = label.strip().strip("«»")
            low_label = label_clean[0].lower() + label_clean[1:] if label_clean else label_clean
            stem = f"{prefix}, {low_label} se referă la:"
        return stem, opts, corr
    return None
