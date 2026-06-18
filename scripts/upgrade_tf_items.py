"""Convertește itemii A/F triviali în itemi cu 4 variante plauzibile."""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.distractor_fix import BankIndex, build_index, classify_option_form, norm
from scripts.stem_templates import natural_concept_stem as _natural_concept_stem

TF_TRUE = {"adevărat", "adevarat", "true", "a"}
TF_FALSE = {"fals", "false", "b"}

TF_REFER_RE = re.compile(
    r"^(.+?)\s+se referă la\s+(.+?)\.?\s*$",
    re.IGNORECASE | re.DOTALL,
)
TF_AFFIRM_RE = re.compile(
    r"^Afirmația următoare este corectă:\s*(.+?)\s*=\s*(.+?)\.?\s*$",
    re.IGNORECASE | re.DOTALL,
)
EXPL_CORRECT_RE = re.compile(
    r"Corect:\s*(.+?)\s+se referă la\s+(.+?)\.?\s*$",
    re.IGNORECASE | re.DOTALL,
)
LABEL_FROM_NATURAL_RE = re.compile(r"«([^»]+)»")

# Grupuri omogene pentru itemi psihometrice / statistice frecvente
HOMOGENEOUS_CLUSTERS: Dict[str, List[Tuple[str, str]]] = {
    "intelligence_tests": [
        ("Scala Binet-Simon", "Instrument timpuriu pentru evaluarea aptitudinilor intelectuale la copii"),
        ("Testul Stanford-Binet", "Revizuire a scalei Binet pentru evaluarea inteligenței"),
        ("Scala Wechsler pentru Adulți", "Instrument standardizat pentru evaluarea inteligenței la adulți"),
        ("Raven's Progressive Matrices", "Test de raționament fluid, cu matrice progresive"),
    ],
    "research_variables": [
        ("Variabila independentă", "Variabila manipulată de cercetător într-un studiu experimental"),
        ("Variabila dependentă", "Variabila măsurată ca rezultat al manipulării experimentale"),
        ("Variabila de control", "Variabila menținută constantă pentru a reduce explicațiile alternative"),
        ("Variabila confundată", "Factor care influențează simultan variabila independentă și dependentă"),
    ],
    "descriptive_stats": [
        ("Media aritmetică", "Media valorilor dintr-un set de date"),
        ("Mediana", "Valoarea care împarte distribuția ordonată în două părți egale"),
        ("Abaterea standard", "Indicator al dispersiei scorurilor în jurul mediei"),
        ("Varianța", "Măsura dispersiei obținută ca medie a pătratelor abaterilor"),
    ],
    "validity_types": [
        ("Validitatea internă", "Gradul în care efectul poate fi atribuit cauzei studiate"),
        ("Validitatea externă", "Gradul în care rezultatele pot fi generalizate la alte contexte"),
        ("Validitatea de construct", "Măsura în care instrumentul evaluează constructul teoretic vizat"),
        ("Validitatea de conținut", "Gradul în care itemii acoperă domeniul de conținut al constructului"),
    ],
}

CLUSTER_STEMS: Dict[str, str] = {
    "intelligence_tests": "În evaluarea aptitudinilor cognitive, care descriere se potrivește cu {label}?",
    "research_variables": "În designul cercetării experimentale, care descriere se potrivește cu {label}?",
    "descriptive_stats": "În analiza statistică a datelor, care descriere se potrivește cu {label}?",
    "validity_types": "În evaluarea calității cercetării, care descriere se potrivește cu {label}?",
}

LABEL_CLUSTER: Dict[str, str] = {}
for cluster_id, members in HOMOGENEOUS_CLUSTERS.items():
    for label, _ in members:
        LABEL_CLUSTER[norm(label)] = cluster_id
        # alias fără articol
        short = label.replace("Testul ", "").replace("Scala ", "")
        LABEL_CLUSTER[norm(short)] = cluster_id

FALLBACK_DEFINITIONS: Dict[str, str] = {
    "stanford-binet": "Revizuire a scalei Binet pentru evaluarea inteligenței",
    "testul stanford-binet": "Test de inteligență derivat din tradiția Binet-Simon",
    "scala binet-simon": "Instrument timpuriu pentru evaluarea aptitudinilor intelectuale la copii",
    "scala wechsler pentru adulți": "Instrument standardizat pentru evaluarea inteligenței la adulți",
    "scala wechsler": "Serie de teste Wechsler pentru evaluarea funcțiilor cognitive",
}


def _cap(text: str) -> str:
    t = (text or "").strip()
    if t and t[0].islower():
        return t[0].upper() + t[1:]
    return t


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', item.get('id_local', ''))}|{item.get('intrebare', item.get('text', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def is_tf_item(item: Dict[str, Any]) -> bool:
    from scripts.fix_tf_items import is_tf_item as _is_tf_item

    return _is_tf_item(item)


def _tf_answer_is_true(item: Dict[str, Any]) -> bool:
    options = item.get("variante") or item.get("options") or {}
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not correct:
        return False
    ans = norm(str(options.get(correct[0], "")))
    return ans in TF_TRUE


def parse_tf_stem(stem: str) -> Optional[Tuple[str, str]]:
    t = (stem or "").strip()
    m = TF_REFER_RE.match(t)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    m = TF_AFFIRM_RE.match(t)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return None


def _normalize_label(label: str) -> str:
    key = norm(label)
    if key in FALLBACK_DEFINITIONS:
        for full, _ in HOMOGENEOUS_CLUSTERS.get("intelligence_tests", []):
            if norm(full) == key or norm(full.replace("Testul ", "")) == key:
                return full
    # păstrează forma cu articol dacă e test/scală
    if key.startswith("testul ") or key.startswith("scala "):
        return label.strip()
    if "stanford" in key and "binet" in key:
        return "Testul Stanford-Binet"
    if key == "stanford-binet":
        return "Testul Stanford-Binet"
    return label.strip()


def extract_correct_definition(
    item: Dict[str, Any], label: str, stated: str, label_map: Dict[str, str]
) -> Optional[str]:
    expl = str(item.get("explicatie") or item.get("explanation") or "")
    m = EXPL_CORRECT_RE.search(expl)
    if m:
        return _cap(m.group(2))

    if _tf_answer_is_true(item):
        return _cap(stated)

    key = norm(label)
    if key in label_map:
        return label_map[key]
    if key in FALLBACK_DEFINITIONS:
        return _cap(FALLBACK_DEFINITIONS[key])

    # cluster definition
    cluster_id = LABEL_CLUSTER.get(key)
    if cluster_id:
        for lbl, defn in HOMOGENEOUS_CLUSTERS[cluster_id]:
            if norm(lbl) == key or norm(lbl.replace("Testul ", "")) == key:
                return _cap(defn)

    return None


def build_label_definition_map(items: Sequence[Dict[str, Any]]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for item in items:
        stem = str(item.get("intrebare") or item.get("text") or "")
        if is_tf_item(item):
            parsed = parse_tf_stem(stem)
            if not parsed:
                continue
            label, stated = parsed
            correct = extract_correct_definition(item, label, stated, mapping)
            if correct:
                mapping[norm(label)] = correct
                mapping[norm(_normalize_label(label))] = correct
            continue

        options = item.get("variante") or item.get("options") or {}
        correct = item.get("raspuns_corect") or item.get("correct") or []
        if len(options) < 4 or not correct:
            continue

        label = None
        m = LABEL_FROM_NATURAL_RE.search(stem)
        if m:
            label = m.group(1)
        else:
            parsed = parse_tf_stem(stem.replace(" cel mai bine", ""))
            if parsed:
                label = parsed[0]
        if not label:
            continue

        letter = str(correct[0]).lower()
        defn = str(options.get(letter) or "")
        if classify_option_form(defn) == "definition" or len(defn) > 25:
            mapping[norm(label)] = _cap(defn)
            mapping[norm(_normalize_label(label))] = _cap(defn)

    for key, val in FALLBACK_DEFINITIONS.items():
        mapping.setdefault(key, _cap(val))
    return mapping


def _pick_distractors(
    pool: List[str], used: Set[str], seed: int, count: int = 3
) -> List[str]:
    available = [x for x in pool if norm(x) not in used]
    if len(available) < count:
        available = list(pool)
    out: List[str] = []
    for i in range(count):
        if not available:
            break
        idx = (seed + i * 17) % len(available)
        choice = available.pop(idx)
        if norm(choice) not in used:
            out.append(choice)
            used.add(norm(choice))
    return out


def _cluster_options(
    cluster_id: str, label: str, seed: int
) -> Optional[Tuple[str, Dict[str, str], str]]:
    members = HOMOGENEOUS_CLUSTERS.get(cluster_id)
    if not members:
        return None
    key = norm(label)
    correct_def = None
    correct_label = label
    for lbl, defn in members:
        if norm(lbl) == key or norm(lbl.replace("Testul ", "")) == key:
            correct_def = defn
            correct_label = lbl
            break
    if not correct_def:
        return None

    letters = ["a", "b", "c", "d"]
    offset = seed % len(members)
    ordered = members[offset:] + members[:offset]
    options: Dict[str, str] = {}
    correct_letter = "a"
    for i, (lbl, defn) in enumerate(ordered[:4]):
        options[letters[i]] = _cap(defn)
        if norm(lbl) == norm(correct_label):
            correct_letter = letters[i]
    from scripts.stem_templates import cap_definition

    tpl = CLUSTER_STEMS.get(cluster_id, "Care descriere se potrivește cu {label}?")
    stem = tpl.format(label=cap_definition(_normalize_label(correct_label)))
    return stem, options, correct_letter


def upgrade_tf_item(
    item: Dict[str, Any],
    label_map: Dict[str, str],
    index: BankIndex,
) -> Tuple[Dict[str, Any], bool]:
    """Deprecat: standardizare A/F (nu conversie la 4 variante)."""
    from scripts.fix_tf_items import fix_tf_item

    return fix_tf_item(item)


def upgrade_items_batch(items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    label_map = build_label_definition_map(items)
    index = build_index(items)
    count = 0
    out: List[Dict[str, Any]] = []
    for item in items:
        upgraded, changed = upgrade_tf_item(item, label_map, index)
        if changed:
            count += 1
        out.append(upgraded)
    return out, count
