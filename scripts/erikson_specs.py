"""Stadiile psihosociale Erikson — enunțuri A/F clare, fără amestec de crize."""

from __future__ import annotations

import re
from typing import Dict, Optional, Tuple

EriksonSpec = Dict[str, str]

# cheie normalizată → specificație
ERIKSON_STAGES: Dict[str, EriksonSpec] = {
    "încredere versus neîncredere": {
        "label": "Încredere versus neîncredere",
        "age": "primului an de viață",
        "theme": "dezvoltarea încrederii de bază față de îngrijitori și de lume",
        "wrong_markers": (
            "tinerețe adultă", "intimitate", "izolare", "generativ", "stagnare",
            "integritate", "disperare", "vârsta înaintată", "acceptarea propriei vieți",
            "școală", "adolescen",
        ),
    },
    "autonomie versus rușine și îndoială": {
        "label": "Autonomie versus rușine și îndoială",
        "age": "perioadei timpurii a copilăriei",
        "theme": "dezvoltarea autonomiei și a controlului asupra propriului corp și acțiunilor",
        "wrong_markers": (
            "intimitate", "generativ", "integritate", "vârsta înaintată", "încredere de bază",
        ),
    },
    "inițiativă versus vinovăție": {
        "label": "Inițiativă versus vinovăție",
        "age": "perioadei preșcolare",
        "theme": "capacitatea de a iniția activități și de a-și asuma planuri proprii",
        "wrong_markers": (
            "intimitate", "generativ", "integritate", "adolescen", "identitate",
        ),
    },
    "muncă versus inferioritate": {
        "label": "Muncă versus inferioritate",
        "age": "vârstei școlare",
        "theme": "dezvoltarea competenței prin învățare și realizări la școală",
        "wrong_markers": (
            "intimitate", "generativ", "integritate", "identitate", "încredere de bază",
        ),
    },
    "identitate versus confuzie de rol": {
        "label": "Identitate versus confuzie de rol",
        "age": "adolescenței",
        "theme": "formarea unui sentiment coerent al identității personale",
        "wrong_markers": (
            "intimitate", "generativ", "integritate", "vârsta înaintată", "încredere de bază",
        ),
    },
    "intimitate versus izolare": {
        "label": "Intimitate versus izolare",
        "age": "tinereții adulte",
        "theme": "capacitatea de a forma relații apropiate, intime și stabile",
        "wrong_markers": (
            "vârsta înaintată", "vârstei a treia", "acceptarea propriei vieți",
            "bilanțul vieții", "integritate", "disperare", "generativ", "stagnare",
            "maturității mijlocii", "contribuția, grija",
        ),
    },
    "generativitate versus stagnare": {
        "label": "Generativitate versus stagnare",
        "age": "maturității mijlocii",
        "theme": "contribuția la generațiile următoare, grija și continuitatea generațiilor",
        "wrong_markers": (
            "intimitate", "izolare", "tinerețe adultă", "integritate", "disperare",
            "vârsta înaintată", "acceptarea propriei vieții", "identitate",
        ),
    },
    "integritate versus disperare": {
        "label": "Integritate versus disperare",
        "age": "vârstei a treia",
        "theme": "acceptarea propriei vieți și a bilanțului existențial",
        "wrong_markers": (
            "intimitate", "izolare", "tinerețe adultă", "generativ", "stagnare",
            "maturității mijlocii", "contribuția, grija", "identitate", "adolescen",
        ),
    },
}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _build_alias_index() -> Dict[str, str]:
    idx: Dict[str, str] = {}
    for key, spec in ERIKSON_STAGES.items():
        idx[_norm(key)] = key
        idx[_norm(spec["label"])] = key
        short = key.split(" versus ")[0].strip()
        if short:
            idx[_norm(short)] = key
    return idx


_ALIAS_INDEX = _build_alias_index()

ERIKSON_STEM_RE = re.compile(
    r"^(?P<crisis>.+?)\s+la\s+Erik\s+H\.?\s+Erikson\s+"
    r"(?:se referă la|exprimă|presupune|indică|descrie|aparține)\s+"
    r"(?P<claim>.+?)\.?\s*$",
    re.IGNORECASE | re.DOTALL,
)


def parse_erikson_stem(stem: str) -> Optional[Tuple[str, str]]:
    m = ERIKSON_STEM_RE.match((stem or "").strip())
    if not m:
        return None
    crisis_raw = m.group("crisis").strip()
    claim = m.group("claim").strip()
    key = _ALIAS_INDEX.get(_norm(crisis_raw))
    if not key:
        for alias, k in _ALIAS_INDEX.items():
            if len(alias) > 8 and alias in _norm(crisis_raw):
                key = k
                break
    if not key:
        return None
    return key, claim


def claim_matches_other_stage(crisis_key: str, claim: str) -> bool:
    low = _norm(claim)
    spec = ERIKSON_STAGES[crisis_key]
    if any(m in low for m in spec["wrong_markers"]):
        return True
    for other_key, other in ERIKSON_STAGES.items():
        if other_key == crisis_key:
            continue
        theme_words = [w for w in _norm(other["theme"]).split() if len(w) > 5][:4]
        if sum(1 for w in theme_words if w in low) >= 2:
            return True
        if _norm(other["age"]) in low:
            return True
    return False


def canonical_tf_stem(crisis_key: str) -> str:
    spec = ERIKSON_STAGES[crisis_key]
    return (
        f"{spec['label']}, în teoria lui Erik H. Erikson, "
        f"este criza {spec['age']} și privește {spec['theme']}."
    )


def is_mixed_erikson_tf_stem(stem: str) -> bool:
    parsed = parse_erikson_stem(stem)
    if not parsed:
        return False
    crisis_key, claim = parsed
    return claim_matches_other_stage(crisis_key, claim)


def fix_erikson_tf_stem(stem: str) -> Optional[str]:
    """Rescrie enunț A/F amestecat → propoziție clară, adevărată."""
    parsed = parse_erikson_stem(stem)
    if not parsed:
        return None
    crisis_key, claim = parsed
    if not claim_matches_other_stage(crisis_key, claim):
        return None
    return canonical_tf_stem(crisis_key)
