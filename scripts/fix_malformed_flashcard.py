"""Repară itemi flashcard cu «descrieri» false — etichete de capitol, nu definiții."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.admin_list_specs import STILURI_PARENTALE_POOL, pick_conceptual_spec, resolve_pool_key
from scripts.concept_clusters import rotate_options
from scripts.domain_concept_specs import build_domain_concept_item, lookup_domain_concept
from scripts.fix_admin_list_items import options_are_short_labels
from scripts.fix_tf_items import is_tf_item
from scripts.stem_naturalize import is_definition_phrase

FLASHCARD_DESC_STEM_RE = re.compile(
    r"^Care concept corespunde descrierii:\s*(.+?)\?\s*$",
    re.IGNORECASE | re.DOTALL,
)
FAKE_DESC_RE = re.compile(
    r"^Concepte\s+(?:teoria|legate|asociate|din)\b",
    re.IGNORECASE,
)
LIST_TOPIC_IN_CONTEXT_RE = re.compile(
    r"Concepte legate de\s+(.+?)\s+este:\s*$",
    re.IGNORECASE,
)

ConceptItem = Dict[str, Any]

CAPS_CONCEPTUAL: List[ConceptItem] = [
    {
        "stem": "În modelul CAPS al lui Walter Mischel, unitățile cognitiv-afective reprezintă:",
        "options": {
            "a": "construcții psihologice (cogniții, afecte, obiective) care organizează comportamentul",
            "b": "dimensiuni stabile ale personalității măsurate prin chestionare tip Big Five",
            "c": "erori de măsurare apărute la transformarea scorurilor brute în norme",
            "d": "proceduri standardizate de administrare și interpretare a testelor",
        },
        "correct": "a",
    },
    {
        "stem": "În modelul CAPS, patternurile dacă–atunci descriu:",
        "options": {
            "a": "regularități comportamentale activate de anumite situații sau stimuli",
            "b": "relații cauzale demonstrate prin manipularea experimentală a variabilelor",
            "c": "asocieri statistice observate fără controlul variabilelor confuze",
            "d": "trăsături trans-situaționale independente de contextul social",
        },
        "correct": "a",
    },
    {
        "stem": "Modelul CAPS (cognitiv-afectiv al personalității) al lui Walter Mischel descrie personalitatea ca:",
        "options": {
            "a": "sistem dinamic de construcții cognitive-afective activate în interacțiune cu situația",
            "b": "set fix de trăsături care determină comportamentul indiferent de context",
            "c": "rezultat exclusiv al condiționării operante a răspunsurilor",
            "d": "produs al normelor standardizate aplicate scorurilor brute",
        },
        "correct": "a",
    },
]

ERORI_INFERENTIALE: List[ConceptItem] = [
    {
        "stem": "Eroarea de tip I în testarea statistică presupune:",
        "options": {
            "a": "respingerea ipotezei nule când aceasta este de fapt adevărată",
            "b": "nerespingerea ipotezei nule când aceasta este falsă",
            "c": "generalizarea rezultatelor la o populație fără eșantion reprezentativ",
            "d": "interpretarea unui coeficient de corelație ca relație cauzală",
        },
        "correct": "a",
    },
    {
        "stem": "Eroarea de tip II în testarea statistică presupune:",
        "options": {
            "a": "nerespingerea ipotezei nule când aceasta este de fapt falsă",
            "b": "respingerea ipotezei nule când aceasta este adevărată",
            "c": "folosirea unui eșantion prea mic pentru a detecta un efect real",
            "d": "confundarea varianței între grupuri cu varianța în interiorul grupurilor",
        },
        "correct": "a",
    },
    {
        "stem": "Valoarea p indică:",
        "options": {
            "a": "probabilitatea de a obține date cel puțin la fel de extreme dacă ipoteza nulă este adevărată",
            "b": "mărimea efectului observat în populația studiată",
            "c": "procentul din varianță explicat de variabila independentă",
            "d": "gradul în care rezultatele pot fi generalizate la alte populații",
        },
        "correct": "a",
    },
]

TOPIC_POOLS: Dict[str, List[ConceptItem]] = {
    "caps": CAPS_CONCEPTUAL,
    "erori_inferentiale": ERORI_INFERENTIALE,
    "stiluri_parentale": STILURI_PARENTALE_POOL,
}


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def is_fake_flashcard_description(desc: str) -> bool:
    """Textul după «descrierii:» nu e o definiție, ci etichetă de capitol."""
    d = (desc or "").strip().strip("«»")
    if not d:
        return True
    if FAKE_DESC_RE.match(d):
        return True
    if re.match(r"^Concepte\s+", d, re.I):
        return True
    if re.search(r"\bteoria\s+", d, re.I) and d[0].isupper() and len(d) < 100:
        return True
    if is_definition_phrase(d):
        return False
    words = d.split()
    if d[0].isupper() and len(words) <= 14 and not d.endswith("."):
        return True
    return False


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def is_malformed_flashcard_item(item: Dict[str, Any]) -> bool:
    if is_tf_item(item):
        return False
    stem = _stem(item)
    opts = _options(item)
    m = FLASHCARD_DESC_STEM_RE.match(stem)
    if m:
        desc = m.group(1).strip()
        if is_fake_flashcard_description(desc):
            return True
        if opts and options_are_short_labels(opts):
            return True
    m2 = LIST_TOPIC_IN_CONTEXT_RE.search(stem)
    if m2:
        return True
    return False


def _resolve_topic_key(desc_or_stem: str) -> Optional[str]:
    low = re.sub(r"\s+", " ", (desc_or_stem or "").lower())
    if "cognitiv-afectiv" in low or "caps" in low or "mischel" in low:
        return "caps"
    if "stilul parental" in low or "stil parental" in low or "parental autorit" in low:
        return "stiluri_parentale"
    if "erori inferen" in low or "inferențial" in low or "inferential" in low:
        return "erori_inferentiale"
    if "eroare" in low and ("tip i" in low or "tip ii" in low or "nulă" in low):
        return "erori_inferentiale"
    return None


def _pick_from_pool(pool_key: str, seed: int) -> Optional[Tuple[str, Dict[str, str], str]]:
    pool = TOPIC_POOLS.get(pool_key, [])
    if not pool:
        return None
    spec = pool[seed % len(pool)]
    return rotate_options(spec, seed)


def _apply_result(
    item: Dict[str, Any],
    stem: str,
    options: Dict[str, str],
    correct: str,
) -> Dict[str, Any]:
    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = stem
    if "text" in item:
        out["text"] = stem
    if "variante" in item:
        out["variante"] = options
    if "options" in item:
        out["options"] = options
    corr = [correct.lower()]
    if "correct" in item:
        out["correct"] = corr
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    out["kind"] = "single"
    out["tip"] = "unic"
    out["explicatie"] = ""
    out["explanation"] = ""
    return out


def fix_malformed_flashcard_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    if not is_malformed_flashcard_item(item):
        return item, False

    stem = _stem(item)
    seed = _item_seed(item)

    m = FLASHCARD_DESC_STEM_RE.match(stem)
    topic_text = m.group(1).strip() if m else stem
    m2 = LIST_TOPIC_IN_CONTEXT_RE.search(stem)
    if m2:
        topic_text = m2.group(1).strip()

    topic_key = _resolve_topic_key(topic_text) or resolve_pool_key(topic_text)
    if topic_key:
        built = _pick_from_pool(topic_key, seed)
        if built:
            new_stem, opts, corr = built
            return _apply_result(item, new_stem, opts, corr), True

    if opts := _options(item):
        if options_are_short_labels(opts):
            built = pick_conceptual_spec(topic_text, seed, opts)
            if built:
                new_stem, new_opts, corr = built
                return _apply_result(item, new_stem, new_opts, corr), True

    clean_label = re.sub(r"^Concepte\s+(?:teoria|legate de|asociate cu|din)\s*", "", topic_text, flags=re.I).strip()
    built = build_domain_concept_item(clean_label, seed)
    if not built:
        built = build_domain_concept_item(topic_text, seed)
    if built:
        new_stem, opts, corr = built
        return _apply_result(item, new_stem, opts, corr), True

    spec = lookup_domain_concept(clean_label) or lookup_domain_concept(topic_text)
    if spec:
        new_stem, opts, corr = rotate_options(spec, seed)
        return _apply_result(item, new_stem, opts, corr), True

    return item, False
