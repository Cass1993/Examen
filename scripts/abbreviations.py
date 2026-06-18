"""Extinde prescurtările la nume complete, păstrând abrevierea în paranteză."""

from __future__ import annotations

import re

# (abreviere, nume complet în română) — ordinea: cele mai lungi primele
_ABBREV_FULL: list[tuple[str, str]] = [
    ("ANOVA pentru măsurători repetate", "Analiza varianței pentru măsurători repetate"),
    ("ANOVA unifactorială", "Analiza varianței unifactorială"),
    ("ANOVA cu măsurători repetate", "Analiza varianței cu măsurători repetate"),
    ("Schema Therapy", "Terapia schemelor"),
    ("Job design", "Proiectarea postului"),
    ("Strange Situation", "Situația stranie"),
    ("Successful aging", "Îmbătrânirea reușită"),
    ("ANOVA", "Analiza varianței"),
    ("WAIS", "Scala Wechsler de inteligență pentru adulți"),
    ("WISC", "Scala Wechsler de inteligență pentru copii"),
    ("MMPI", "Inventarul multiaxial de personalitate Minnesota"),
    ("JVIS", "Inventarul de interese vocaționale Jackson"),
    ("CPI", "Inventarul de personalitate California"),
    ("EPQ", "Chestionarul de personalitate Eysenck"),
    ("CAPS", "Teoria sistemului cognitiv-afectiv al personalității"),
    ("CHC", "Modelul Cattell-Horn-Carroll"),
    ("PTSD", "Tulburarea de stres post-traumatic"),
    ("GWAS", "Studiul de asociere pe întreg genomul"),
    ("SNP", "Polimorfismul nucleotidic unic"),
    ("KSAO", "Cunoștințe, abilități, aptitudini și alte caracteristici"),
    ("OCB", "Comportamentul civic organizațional"),
    ("JD-R", "Modelul cerințelor și resurselor postului"),
    ("HEXACO", "Modelul celor șase factori de personalitate"),
    ("ACT", "Terapia de acceptare și angajament"),
    ("DBT", "Terapia dialectic-comportamentală"),
    ("EFT", "Terapia focalizată pe emoții"),
    ("CBT", "Terapia cognitiv-comportamentală"),
    ("TCC", "Terapia cognitiv-comportamentală"),
    ("ACE", "Modelul eredității: influențe genetice aditive, mediu comun și mediu neîmpărtășit"),
    ("DSM", "Manualul diagnostic și statistic al tulburărilor mentale"),
    ("ICD", "Clasificarea internațională a bolilor"),
    ("TAT", "Testul de appercepție tematică"),
    ("IQ", "Coeficientul de inteligență"),
    ("ADN", "Acid dezoxiribonucleic"),
]

_ORDERED = sorted(_ABBREV_FULL, key=lambda x: len(x[0]), reverse=True)


def _base_full_name(full: str) -> str:
    return full.split("(")[0].strip() if "(" in full else full.strip()


def _expanded_form(abbr: str, full: str) -> str:
    base = _base_full_name(full)
    if abbr.lower() in base.lower():
        return base
    return f"{base} ({abbr})"


def _should_skip_abbrev(text: str, m_start: int, abbr: str, full: str) -> bool:
    """Nu re-extinde abrevierea din «Nume complet (ABBR)» sau din forma deja extinsă."""
    base = _base_full_name(full)
    if m_start > 0 and text[m_start - 1] == "(":
        before = text[: m_start - 1].rstrip()
        if before:
            low = before.lower()
            if low.endswith(base.lower()) or low.endswith(full.lower()):
                return True
    # abrevierea face parte din numele complet deja prezent (ex. HEXACO în text extins greșit)
    if abbr.lower() in base.lower():
        window_start = max(0, m_start - len(base) - 2)
        window = text[window_start : m_start + len(abbr)].lower()
        if base.lower() in window:
            return True
    return False


def collapse_nested_expansions(text: str) -> str:
    """Repară extinderi recursive accidentale din trecut."""
    if not text:
        return text
    result = str(text)
    # buclă HEXACO: «Modelul celor șase factori… (HEXACO)» repetat
    hexaco_nested = re.compile(
        r"Modelul celor șase factori de personalitate\s*"
        r"(?:\(HEXACO\)\s*)+"
        r"(?:Modelul celor șase factori de personalitate\s*(?:\(HEXACO\)\s*)*)+",
        re.IGNORECASE,
    )
    if hexaco_nested.search(result):
        result = hexaco_nested.sub(
            "Modelul celor șase factori de personalitate (HEXACO)",
            result,
        )
    # buclă HEXACO veche: «Modelul personalității» repetat
    if result.lower().count("modelul personalității") >= 3:
        result = re.sub(
            r"(?:Modelul\s+personalității\s*){2,}.*?(?:HEXACO\s*(?:\(HEXACO\))?)?",
            "Modelul celor șase factori de personalitate (HEXACO)",
            result,
            count=1,
            flags=re.IGNORECASE,
        )
    for abbr, full in _ORDERED:
        base = _base_full_name(full)
        if not base:
            continue
        canonical = _expanded_form(abbr, full)
        esc_base = re.escape(base)
        esc_abbr = re.escape(abbr)
        pattern = re.compile(
            rf"{esc_base}\s*(?:\(\s*{esc_base}\s*)+\(\s*{esc_abbr}\s*\)\)+",
            re.IGNORECASE,
        )
        result = pattern.sub(canonical, result)
        # variantă veche: full includea deja paranteza (ex. Strange Situation)
        legacy = f"{base} ({base}"
        if legacy.lower() in result.lower():
            legacy_pat = re.compile(
                rf"{esc_base}\s*(?:\(\s*{esc_base}\s*)+(?:\(\s*{esc_abbr}\s*\))+\)+",
                re.IGNORECASE,
            )
            result = legacy_pat.sub(canonical, result)
    return result


def expand_abbreviations(text: str) -> str:
    if not text or not str(text).strip():
        return text

    result = collapse_nested_expansions(str(text))

    for abbr, full in _ORDERED:
        expanded = _expanded_form(abbr, full)
        if expanded.lower() == result.lower():
            continue

        pattern = re.compile(rf"\b{re.escape(abbr)}\b", re.IGNORECASE)
        parts: list[str] = []
        last = 0
        for m in pattern.finditer(result):
            if _should_skip_abbrev(result, m.start(), abbr, full):
                continue
            parts.append(result[last : m.start()])
            parts.append(expanded)
            last = m.end()
        if last:
            parts.append(result[last:])
            result = "".join(parts) if parts else result

        dup = re.compile(
            rf"({re.escape(_base_full_name(full))}\s*\({re.escape(abbr)}\))\s*\({re.escape(abbr)}\)",
            re.IGNORECASE,
        )
        result = dup.sub(r"\1", result)

    for abbr, full in _ORDERED:
        expanded = _expanded_form(abbr, full)
        result = re.sub(
            rf"\b{re.escape(abbr)}\s*=",
            f"{expanded} =",
            result,
            flags=re.IGNORECASE,
        )

    return collapse_nested_expansions(result)
