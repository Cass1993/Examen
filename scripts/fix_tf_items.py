"""Standardizează itemii Adevărat/Fals — enunț natural + variante strict Adevărat/Fals."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

TF_TRUE = frozenset({"adevărat", "adevarat", "true"})
TF_FALSE = frozenset({"fals", "false"})

TF_OPTIONS: Dict[str, str] = {"a": "Adevărat", "b": "Fals"}

TF_PREFIX_RES: Tuple[re.Pattern[str], ...] = (
    re.compile(r"^Afirmația următoare este corectă:\s*", re.I),
    re.compile(r"^Este adevărat că:\s*", re.I),
    re.compile(r"^Este fals că:\s*", re.I),
    re.compile(r"^Alege adevărat sau fals:\s*", re.I),
    re.compile(r"^Adevărat sau fals:\s*", re.I),
    re.compile(r"^Se poate afirma că:\s*", re.I),
    re.compile(r"^Care afirmație este adevărată:\s*", re.I),
    re.compile(r"^Conceptul .+ este descris de formularea:\s*", re.I),
)

EQUALS_PROP_RE = re.compile(r"^(.+?)\s*=\s*(.+?)\.?\s*$", re.DOTALL)
REFER_PROP_RE = re.compile(
    r"^(.+?)\s+(se referă la|exprimă|presupune|indică|descrie|aparține)\s+(.+?)\.?\s*$",
    re.I | re.DOTALL,
)
EXPL_FALSE_RE = re.compile(r"^\s*Fals\b", re.I)
EXPL_TRUE_RE = re.compile(r"^\s*(?:Adevărat|Corect)\b", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _cap_first(text: str) -> str:
    t = (text or "").strip()
    if t and t[0].islower():
        return t[0].upper() + t[1:]
    return t


def _cap_sentence(text: str) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip())
    if not t:
        return t
    if t[-1] not in ".!?":
        t += "."
    return _cap_first(t)


def is_tf_item(item: Dict[str, Any]) -> bool:
    """Item A/F: exact 2 variante, dintre care cel puțin una e Adevărat/Fals."""
    tip = str(item.get("tip") or item.get("kind") or "").lower()
    if tip in {"adevarat_fals", "adevărat_fals", "tf", "true_false"}:
        return True

    options = item.get("variante") or item.get("options") or {}
    if len(options) != 2:
        return False

    vals = {norm(str(v)) for v in options.values()}
    return bool(vals & TF_TRUE) or bool(vals & TF_FALSE)


def _strip_tf_prefix(stem: str) -> str:
    text = (stem or "").strip()
    for pat in TF_PREFIX_RES:
        text = pat.sub("", text).strip()
    return text


def _pick_verb(label: str, definition: str) -> str:
    blob = norm(f"{label} {definition}")
    if "aparține" in blob or "cluster" in blob:
        return "aparține"
    if any(w in blob for w in ("proporț", "variaț", "eritabil", "genetic")):
        return "exprimă"
    if "validitate" in blob:
        return "indică"
    if any(w in blob for w in ("atașament", "întărire", "presupune", "implică")):
        return "presupune"
    if definition and definition[0].islower():
        return "se referă la"
    return "se referă la"


def _naturalize_proposition(text: str) -> str:
    t = _strip_tf_prefix(text).strip().strip("«»")

    m = EQUALS_PROP_RE.match(t)
    if m:
        label, definition = m.group(1).strip(), m.group(2).strip()
        verb = _pick_verb(label, definition)
        if verb == "aparține":
            return _cap_sentence(f"{label} {verb} {definition}")
        if definition and definition[0].islower():
            return _cap_sentence(f"{label} {verb} {definition}")
        return _cap_sentence(f"{label} {verb} {definition}")

    m2 = REFER_PROP_RE.match(t)
    if m2:
        label, verb, definition = m2.group(1).strip(), m2.group(2).lower(), m2.group(3).strip()
        return _cap_sentence(f"{label} {verb} {definition}")

    return _cap_sentence(t)


def _truth_from_correct_option(
    options: Dict[str, str], correct: Sequence[str]
) -> Optional[bool]:
    if not correct:
        return None
    letter = str(correct[0]).lower()
    if letter not in options:
        return None
    val = norm(str(options[letter]))
    if val in TF_TRUE:
        return True
    if val in TF_FALSE:
        return False
    return None


def _truth_from_explanation(item: Dict[str, Any]) -> Optional[bool]:
    expl = str(item.get("explicatie") or item.get("explanation") or "").strip()
    if not expl:
        return None
    if EXPL_FALSE_RE.match(expl):
        return False
    if EXPL_TRUE_RE.match(expl):
        return True
    return None


def _infer_truth_value(item: Dict[str, Any], options: Dict[str, str]) -> bool:
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    truth = _truth_from_correct_option(options, correct)
    if truth is not None:
        return truth

    expl_truth = _truth_from_explanation(item)
    if expl_truth is not None:
        return expl_truth

    # Varianta greșită e concept — cealaltă literă e Fals/Adevărat
    tf_letters: Dict[str, bool] = {}
    for letter, val in options.items():
        n = norm(str(val))
        if n in TF_TRUE:
            tf_letters[letter] = True
        elif n in TF_FALSE:
            tf_letters[letter] = False

    if len(tf_letters) == 1:
        return next(iter(tf_letters.values()))

    return False


def fix_tf_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """Rescrie item A/F: enunț natural + a) Adevărat, b) Fals."""
    if not is_tf_item(item):
        return item, False

    from scripts.fix_incomplete_tf import fix_incomplete_tf_item, is_incomplete_tf_item

    if is_incomplete_tf_item(item):
        fixed, changed = fix_incomplete_tf_item(item)
        if changed:
            return fixed, True

    from scripts.fix_erikson_tf import fix_erikson_tf_item

    fixed_erikson, erikson_changed = fix_erikson_tf_item(item)
    if erikson_changed:
        item = fixed_erikson

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]

    is_true = _infer_truth_value(item, options)
    new_stem = _naturalize_proposition(stem)
    from scripts.fix_incomplete_tf import is_incomplete_tf_stem

    if is_incomplete_tf_stem(new_stem):
        from scripts.fix_incomplete_tf import fix_incomplete_tf_item

        fixed, changed = fix_incomplete_tf_item(item)
        if changed:
            return fixed, True
        new_stem = new_stem.rstrip(":.").strip() + "."

    new_correct = ["a"] if is_true else ["b"]

    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    if "variante" in item:
        out["variante"] = dict(TF_OPTIONS)
    if "options" in item:
        out["options"] = dict(TF_OPTIONS)
    if "raspuns_corect" in item:
        out["raspuns_corect"] = new_correct
    if "correct" in item:
        out["correct"] = new_correct
    out["tip"] = "adevărat_fals"
    out["kind"] = "adevărat_fals"

    changed = (
        new_stem != stem
        or options != TF_OPTIONS
        or correct != new_correct
        or str(item.get("kind") or item.get("tip") or "") != "adevărat_fals"
    )
    return out, changed


def fix_tf_items_batch(items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    count = 0
    out: List[Dict[str, Any]] = []
    for item in items:
        fixed, changed = fix_tf_item(item)
        if changed:
            count += 1
        out.append(fixed)
    return out, count
