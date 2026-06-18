"""Rescriere itemi genetică comportamentală / epigenetică — terminologie și separare conceptuală."""

from __future__ import annotations

import copy
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.genetics_epigenetics_specs import (
    GENETICS_PAIRS,
    build_from_spec,
    lookup_single_spec,
    normalize_genetics_text,
    pick_rotation_spec,
)
from scripts.association_pair_fix import (
    _format_pair,
    _wrong_description_for,
    is_association_item,
    parse_pair,
)

_VAGUE_STEM = re.compile(
    r"concepte\s+genetice\s+și\s+epigenetice|"
    r"genetice\s+și\s+epigenetice\s+se\s+referă|"
    r"în\s+psihologia\s+personalității,\s*genetica\s+se\s+referă|"
    r"care\s+tema\s+aparține\s+geneticii\s+comportamentale|"
    r"factorii\s+genetici\s+în\s+psihologie.*asocieri\s+concept",
    re.IGNORECASE,
)

_BROKEN_ACE_STEM = re.compile(
    r"modelul\s+modelul|"
    r"^Modelul\s+modelul\s+genetic\s+aditiv",
    re.IGNORECASE,
)

_BARE_EPIGENETICS = re.compile(
    r"^Epigenetica\s+descriu?:\s*$",
    re.IGNORECASE,
)

_GENETICS_MARKERS = re.compile(
    r"genetic|epigenet|gemen|eritabil|modelul\s+ace|model\s+ace|"
    r"mediu\s+comun|mediu\s+neîmpărtășit|mediu\s+unic|gwas|metilare|"
    r"polimorfism|poligenic|moștenirea\s+epigenetică|programarea\s+epigenetică",
    re.IGNORECASE,
)

_POLYGENIC_STEM = re.compile(r"scorul\s+poligenic|efectul\s+poligenic|scor\s+poligenic", re.I)

_CROSS_FAMILY_IN_OPTIONS = re.compile(
    r"validitate de criteriu|validitatea de criteriu|atașament|psihoterapie|"
    r"hackman|zona proximă|big five|stadii psihosexual|"
    r"(?:Modelul\s+personalității\s+){2,}",
    re.I,
)

_MIXED_GENETICS_ASSOC = re.compile(
    r"asocieri\s+(concept|termen).*(definiție|descriere)|"
    r"referitor\s+la\s+factorii\s+genetici",
    re.IGNORECASE,
)


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _item_blob(item: Dict[str, Any]) -> str:
    parts = [str(item.get("text") or "")]
    opts = item.get("options") or {}
    if isinstance(opts, dict):
        parts.extend(str(v) for v in opts.values())
    return " ".join(parts)


def normalize_item_terminology(item: Dict[str, Any]) -> Dict[str, Any]:
    out = copy.deepcopy(item)
    out["text"] = normalize_genetics_text(str(out.get("text") or ""))
    opts = out.get("options")
    if isinstance(opts, dict):
        out["options"] = {k: normalize_genetics_text(str(v)) for k, v in opts.items()}
    return out


def is_genetics_stem(item: Dict[str, Any]) -> bool:
    return bool(_GENETICS_MARKERS.search(_norm(item.get("text") or "")))


def is_genetics_problem_item(item: Dict[str, Any]) -> bool:
    text = _norm(item.get("text") or "")
    blob = _norm(_item_blob(item))
    if _POLYGENIC_STEM.search(text) and _CROSS_FAMILY_IN_OPTIONS.search(blob):
        return True
    if _POLYGENIC_STEM.search(text):
        return True
    if _VAGUE_STEM.search(text):
        return True
    if _BROKEN_ACE_STEM.search(blob):
        return True
    if _BARE_EPIGENETICS.match(text.strip()):
        return True
    if "modelul modelul" in blob:
        return True
    if "mediu unic" in blob:
        return True
    if "concepte genetice și epigenetice" in blob:
        return True
    if _MIXED_GENETICS_ASSOC.search(text) and _GENETICS_MARKERS.search(blob):
        return True
    # stem «X descrie:» pentru concepte genetice cu opțiuni amestecate
    if re.match(r"^modelul\s+.*ace|^epigenetica\s+descri", text) and _GENETICS_MARKERS.search(blob):
        return True
    return False


def _is_genetics_association(item: Dict[str, Any]) -> bool:
    if not is_association_item(item):
        return False
    blob = _norm(_item_blob(item))
    hits = sum(
        1
        for term, _ in GENETICS_PAIRS
        if _norm(term) in blob or any(w in blob for w in _norm(term).split()[:2])
    )
    return hits >= 2 or (
        _MIXED_GENETICS_ASSOC.search(item.get("text") or "") and _GENETICS_MARKERS.search(blob)
    )


def _build_genetics_association(seed: int) -> Dict[str, Any]:
    """Item multi cu perechi concept–descriere din genetica comportamentală."""
    pairs = list(GENETICS_PAIRS)
    n_correct = 2 + (seed % 2)
    correct_idx = [(seed + i * 3) % len(pairs) for i in range(n_correct)]
    correct_idx = list(dict.fromkeys(correct_idx))[:n_correct]
    while len(correct_idx) < n_correct:
        correct_idx.append((correct_idx[-1] + 1) % len(pairs))

    used_defs: set = set()
    options: Dict[str, str] = {}
    correct_letters: List[str] = []
    letters = ["a", "b", "c", "d"]
    offset = 0

    for i, idx in enumerate(correct_idx):
        concept, defn = pairs[idx]
        options[letters[i]] = _format_pair(concept, defn)
        correct_letters.append(letters[i])
        used_defs.add(_norm(defn))
        offset += 1

    for j in range(n_correct, 4):
        concept, _ = pairs[(seed + j * 5) % len(pairs)]
        wrong = _wrong_description_for(
            "genetica_comportamentala", concept, used_defs, seed + offset
        )
        options[letters[j]] = _format_pair(concept, wrong)
        used_defs.add(_norm(wrong))
        offset += 1

    return {
        "text": "Care dintre următoarele asocieri concept–descriere din genetica comportamentală sunt corecte?",
        "options": options,
        "correct": correct_letters,
        "kind": "multi",
    }


def _stem_targets_ace(text: str) -> bool:
    t = _norm(text)
    return "modelul ace" in t or "model ace" in t or "modelul modelul" in t or (
        "genetic aditiv" in t and "mediu comun" in t
    )


def _stem_targets_twins(text: str) -> bool:
    t = _norm(text)
    return "studiile gemelare" in t or "studiile gemenare" in t or "gemeni monozigo" in t


def _stem_targets_heritability(text: str) -> bool:
    return "eritabilit" in _norm(text)


def _stem_targets_poligenic(text: str) -> bool:
    return bool(_POLYGENIC_STEM.search(_norm(text)))


def _stem_targets_epigenetics(text: str) -> bool:
    t = _norm(text)
    return "epigenet" in t or "metilare" in t or "moștenirea epigenetică" in t


def rewrite_genetics_item(item: Dict[str, Any], seed: int) -> Optional[Dict[str, Any]]:
    item = normalize_item_terminology(item)
    text = str(item.get("text") or "")
    norm_text = _norm(text)

    if _VAGUE_STEM.search(norm_text):
        spec = pick_rotation_spec(seed)
        stem, opts, corr = build_from_spec(spec, seed)
        out = copy.deepcopy(item)
        out["text"] = stem
        out["options"] = opts
        out["correct"] = corr
        out["kind"] = spec.get("kind") or ("multi" if len(corr) > 1 else "single")
        return out

    if _is_genetics_association(item):
        rebuilt = _build_genetics_association(seed)
        out = copy.deepcopy(item)
        out.update(rebuilt)
        return out

    if _stem_targets_ace(text) or "modelul modelul" in _norm(_item_blob(item)):
        from scripts.genetics_epigenetics_specs import SINGLE_SPECS
        spec = SINGLE_SPECS["modelul ace"]
        stem, opts, corr = build_from_spec(spec, seed)
        out = copy.deepcopy(item)
        out["text"] = stem
        out["options"] = opts
        out["correct"] = corr
        out["kind"] = "single"
        return out

    if _stem_targets_twins(text):
        from scripts.genetics_epigenetics_specs import SINGLE_SPECS
        spec = SINGLE_SPECS["studiile gemelare"]
        stem, opts, corr = build_from_spec(spec, seed)
        out = copy.deepcopy(item)
        out["text"] = stem
        out["options"] = opts
        out["correct"] = corr
        out["kind"] = "single"
        return out

    if _stem_targets_poligenic(text):
        from scripts.genetics_epigenetics_specs import SINGLE_SPECS
        key = "efectul poligenic" if "efect" in norm_text else "scorul poligenic"
        spec = SINGLE_SPECS[key]
        stem, opts, corr = build_from_spec(spec, seed)
        out = copy.deepcopy(item)
        out["text"] = stem
        out["options"] = opts
        out["correct"] = corr
        out["kind"] = "single"
        return out

    if _stem_targets_heritability(text) and "asocieri" not in norm_text:
        from scripts.genetics_epigenetics_specs import SINGLE_SPECS
        spec = SINGLE_SPECS["ereditabilitatea"]
        stem, opts, corr = build_from_spec(spec, seed)
        out = copy.deepcopy(item)
        out["text"] = stem
        out["options"] = opts
        out["correct"] = corr
        out["kind"] = "single"
        return out

    if _stem_targets_epigenetics(text) and not is_association_item(item):
        label = text.split("descrie")[0].strip(" :")
        spec = lookup_single_spec(label) or lookup_single_spec(_item_blob(item))
        if spec:
            stem, opts, corr = build_from_spec(spec, seed)
            out = copy.deepcopy(item)
            out["text"] = stem
            out["options"] = opts
            out["correct"] = corr
            out["kind"] = "single"
            return out

    # doar terminologie
    if normalize_genetics_text(str(item.get("text") or "")) != str(item.get("text") or ""):
        return item
    blob_before = _item_blob(item)
    item_norm = normalize_item_terminology(item)
    if _item_blob(item_norm) != blob_before:
        return item_norm

    return None


def apply_genetics_fixes(items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Returnează (items_actualizate, raport_modificări)."""
    out: List[Dict[str, Any]] = []
    changes: List[Dict[str, Any]] = []
    for i, raw in enumerate(items):
        seed = int(raw.get("id") or i)
        current = normalize_item_terminology(raw)
        if is_genetics_problem_item(current):
            fixed = rewrite_genetics_item(current, seed)
            if fixed:
                changes.append(
                    {
                        "id": raw.get("id"),
                        "before": raw.get("text"),
                        "after": fixed.get("text"),
                    }
                )
                current = fixed
        elif _item_blob(current) != _item_blob(raw):
            changes.append(
                {
                    "id": raw.get("id"),
                    "before": raw.get("text"),
                    "after": current.get("text"),
                    "note": "terminologie",
                }
            )
        out.append(current)
    return out, changes
