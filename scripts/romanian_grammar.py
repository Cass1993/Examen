"""Acord gramatical simplu pentru enunțuri de itemi (singular/plural)."""

from __future__ import annotations

import re

STEM_LABEL_RE = re.compile(r"«([^»]+)»")

PLURAL_SUFFIX_RE = re.compile(
    r"(?:ele|ile|ii|uri|ăți|ori|atele|urile)$",
    re.IGNORECASE,
)

# singular → plural (doar după eticheta «…»)
VERB_PLURAL_AFTER_LABEL = (
    (" descrie:", " descriu:"),
    (" descrie mai ales:", " descriu mai ales:"),
    (" este:", " sunt:"),
    (" este caracterizată prin:", " sunt caracterizate prin:"),
    (" este utilizat pentru:", " sunt utilizate pentru:"),
    (" presupune:", " presupun:"),
)


def is_plural_label(label: str) -> bool:
    """Heuristică pentru etichete la plural (Normele, Scalele, Tulburările…)."""
    t = (label or "").strip().strip("«»")
    t = t.split("—")[0].split("–")[0].split("(")[0].strip()
    if not t:
        return False
    low = t.lower()
    words = [w for w in re.split(r"\s+", low) if w]
    if words and PLURAL_SUFFIX_RE.search(words[0]):
        return True
    if words and words[0].endswith("i") and not words[0].endswith(("ări", "iri")):
        # dimensiuni, surse, stresori — plural în -i (nu -ări singular abstract)
        if words[0] in {
            "dimensiuni", "surse", "stresori", "criterii", "teorii", "tipuri",
            "stadii", "stiluri", "metode", "proceduri", "variabile", "norme",
            "scale", "intervenții", "interventii",
        }:
            return True
    if PLURAL_SUFFIX_RE.search(words[-1]) if words else False:
        return True
    if re.search(
        r"\b(?:normele|scalele|tulburările|itemii|testele|tipuri|teorii|stadii|"
        r"stiluri|metodele|procedurile|variabile|psihoterapiile|cerințele|"
        r"dimensiuni|surse|intervenții)\b",
        low,
    ):
        return True
    return False


def agree_stem_verbs(stem: str, label: str) -> str:
    if not is_plural_label(label):
        return stem
    out = stem
    for singular, plural in VERB_PLURAL_AFTER_LABEL:
        if singular in out:
            out = out.replace(singular, plural, 1)
            break
    return out


SUBJECT_BEFORE_VERB_RE = re.compile(
    r"^(?:În [^,]+,\s*)?(?P<subject>.+?)\s+"
    r"(?P<verb>descrie mai ales:|descrie:|este:|presupune:|"
    r"este caracterizată prin:|este caracterizate prin:|"
    r"este utilizat pentru:|sunt:)\s*",
    re.IGNORECASE,
)


BROKEN_ABORDAREA_PREFIX_RE = re.compile(
    r"^Abordarea (Terapia|Psihoterapia|Modelul|Teoria) (.+?) se bazează pe:\s*$",
    re.IGNORECASE,
)


def fix_broken_abordarea_stem(stem: str) -> str:
    """Abordarea Terapia X → Terapia X; Abordarea Modelul X → Modelul X postulează."""
    text = (stem or "").strip()
    m = BROKEN_ABORDAREA_PREFIX_RE.match(text)
    if not m:
        return text
    head, rest = m.group(1), m.group(2)
    if head.lower().startswith("modelul"):
        return f"Modelul {rest} postulează că:"
    if head.lower().startswith("teoria"):
        return f"Teoria {rest} postulează că:"
    return f"{head} {rest} se bazează pe:"


def fix_stem_grammar(stem: str) -> str:
    """Corectează acordul verbal după subiectul la plural (cu sau fără ghilimele)."""
    text = fix_broken_abordarea_stem((stem or "").strip())
    if not text:
        return text

    m = STEM_LABEL_RE.search(text)
    if m:
        return agree_stem_verbs(text, m.group(1))

    m2 = SUBJECT_BEFORE_VERB_RE.match(text)
    if m2:
        subject = m2.group("subject").strip()
        if is_plural_label(subject):
            return agree_stem_verbs(text, subject)

    low = text.lower()
    plural_markers = (
        r"\b(?:normele|scalele|tulburările|itemii|testele|stiluri|teorii|"
        r"tipuri|variabile|metodele|procedurile|stadii|psihoterapiile|"
        r"dimensiuni|surse|cerințele|intervenții)\b"
    )
    if re.search(plural_markers, low, re.IGNORECASE):
        for singular, plural in VERB_PLURAL_AFTER_LABEL:
            if singular in low and plural not in low:
                return text.replace(singular, plural, 1)
    return text
