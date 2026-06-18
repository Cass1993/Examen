"""Reformulare enunțuri Psihoterapie II — terapii ca orientări, nu persoane; fără meta-limbaj."""

from __future__ import annotations

import re

# Înlocuiri exacte (prioritare) pentru enunțuri cunoscute ca problematice.
_STEM_EXACT: dict[str, str] = {
    "Gestalt l-ar descrie mai probabil ca pe cineva care:": (
        "Un client își critică dur propriile reacții, respectă standarde rigide de perfecțiune "
        "și își întoarce energia critică spre sine, evitând confruntarea directă. "
        "Din perspectiva terapiei gestaltiste, acest tipar corespunde mai probabil:"
    ),
    "În grile, introiecția se deosebește de proiecție astfel:": (
        "Introiecția gestaltică se deosebește de proiecție astfel:"
    ),
    "În grile, confuzia „proiecție gestaltică = proiecție freudiană” este:": (
        "Confuzia frecventă „proiecție gestaltică = proiecție freudiană” este:"
    ),
    "Confuzia examenului apare pentru că termenul „introiecție” în Gestalt accentuează mai mult:": (
        "Confuzia frecventă apare deoarece termenul „introiecție” în terapia gestaltistă "
        "accentuează mai mult:"
    ),
    'Confuzia examenului „Adler = freudian care neagă sexul” este greșită deoarece Adler:': (
        "Confuzia frecventă „Adler = freudian care neagă sexul” este greșită deoarece Alfred Adler:"
    ),
    "Ellis ar considera mai irațională ideea:": (
        "În terapia rațional-emotivă (Albert Ellis), care dintre următoarele idei "
        "ar fi considerată mai irațională?"
    ),
    "Beck ar descrie mai probabil gândul „Dacă nu ies perfect, e un dezastru total” drept:": (
        "În terapia cognitivă (Aaron T. Beck), gândul „Dacă nu ies perfect, e un dezastru total” "
        "ar fi descris mai probabil drept:"
    ),
    "Glasser ar aborda mai probabil o plângere repetată despre colegi prin întrebări de tipul:": (
        "În terapia centrată pe realitate (William Glasser), o plângere repetată despre colegi "
        "ar fi abordată mai probabil prin întrebări de tipul:"
    ),
    "Freud ar interpreta anxietatea ca semnal al conflictului între:": (
        "În psihanaliza freudiană (Sigmund Freud), anxietatea poate fi interpretată ca semnal "
        "al conflictului între:"
    ),
    "Perls ar prefera formularea „eu mă enervez” în loc de „se enervează lucrurile” pentru a contracara:": (
        "În terapia gestaltistă (Fritz Perls), formularea „eu mă enervez” în loc de "
        "„se enervează lucrurile” este preferată pentru a contracara:"
    ),
    "Adler ar interpreta un adolescent care spune „Trebuie să fiu primul la orice, altfel nu contez” prin:": (
        "În psihologia individuală (Alfred Adler), un adolescent care spune "
        "„Trebuie să fiu primul la orice, altfel nu contez” ar fi interpretat mai probabil prin:"
    ),
    "Un client idealizează terapeutul, apoi îl devalorizează brusc. Gestalt ar putea explora același pattern ca:": (
        "Un client idealizează terapeutul, apoi îl devalorizează brusc. "
        "Din perspectiva terapiei gestaltiste, același tipar ar putea fi explorat ca:"
    ),
    "Un client rogersian respinge o emoție „inacceptabilă”. Gestalt ar interveni mai probabil prin:": (
        "Un client în consilierea centrată pe persoană respinge o emoție „inacceptabilă”. "
        "Terapia gestaltistă ar interveni mai probabil prin:"
    ),
    "Un client amână constant sarcinile importante, dar oferă scuze logice. Adler ar numi asta mai probabil:": (
        "Un client amână constant sarcinile importante, dar oferă scuze logice. "
        "În psihologia individuală (Alfred Adler), acest comportament ar fi numit mai probabil:"
    ),
    "Care afirmații descriu corect diferențe între Rogers și Gestalt?": (
        "Care afirmații descriu corect diferențe între consilierea centrată pe persoană "
        "(Carl R. Rogers) și terapia gestaltistă?"
    ),
}

# Înlocuiri regex — ordinea contează (mai specifice primele).
_STEM_REGEX: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"\bGestalt l-ar\b", re.I),
        "Terapia gestaltistă l-ar",
    ),
    (
        re.compile(r"\bGestalt ar\b", re.I),
        "Terapia gestaltistă ar",
    ),
    (
        re.compile(r"\bÎn Gestalt,\s*", re.I),
        "În terapia gestaltistă, ",
    ),
    (
        re.compile(r"\bîn Gestalt,\s*", re.I),
        "în terapia gestaltistă, ",
    ),
    (
        re.compile(r"\bîn Gestalt\b", re.I),
        "în terapia gestaltistă",
    ),
    (
        re.compile(r"\bGestalt pune\b", re.I),
        "Terapia gestaltistă pune",
    ),
    (
        re.compile(r"\bGestalt este\b", re.I),
        "Terapia gestaltistă este",
    ),
    (
        re.compile(r"\bGestalt respinge\b", re.I),
        "Terapia gestaltistă respinge",
    ),
    (
        re.compile(r"\bGestalt consideră\b", re.I),
        "Terapia gestaltistă consideră",
    ),
    (
        re.compile(r"\bGestalt folosește\b", re.I),
        "Terapia gestaltistă folosește",
    ),
    (
        re.compile(r"\bGestalt lucrează\b", re.I),
        "Terapia gestaltistă lucrează",
    ),
    (
        re.compile(r"\bGestalt recunoaște\b", re.I),
        "Terapia gestaltistă recunoaște",
    ),
    (
        re.compile(r"\bGestalt recunosc\b", re.I),
        "Terapia gestaltistă recunoaște",
    ),
    (
        re.compile(r"\bGestalt ar tinde\b", re.I),
        "Terapia gestaltistă ar tinde",
    ),
    (
        re.compile(r"\bGestalt ar putea\b", re.I),
        "Terapia gestaltistă ar putea",
    ),
    (
        re.compile(r"\bGestalt ar interveni\b", re.I),
        "Terapia gestaltistă ar interveni",
    ),
    (
        re.compile(r"\bGestalt ar explora\b", re.I),
        "Terapia gestaltistă ar explora",
    ),
    (
        re.compile(r"\bGestaltului\b", re.I),
        "terapiei gestaltiste",
    ),
    (
        re.compile(r"\bdecât cu Gestalt\b", re.I),
        "decât cu terapia gestaltistă",
    ),
    (
        re.compile(r"\bdecât Gestalt\b", re.I),
        "decât terapia gestaltistă",
    ),
    (
        re.compile(r"\bși Gestalt\b", re.I),
        "și terapia gestaltistă",
    ),
    (
        re.compile(r"\bRogers și Gestalt\b", re.I),
        "consilierea centrată pe persoană (Carl R. Rogers) și terapia gestaltistă",
    ),
    (
        re.compile(r"\bGestalt și Rogers\b", re.I),
        "terapia gestaltistă și consilierea centrată pe persoană (Carl R. Rogers)",
    ),
    (
        re.compile(r"\bRogers și terapia gestaltistă\b", re.I),
        "consilierea centrată pe persoană (Carl R. Rogers) și terapia gestaltistă",
    ),
    (
        re.compile(r"\bRogers decât Gestalt\b", re.I),
        "consilierea centrată pe persoană decât terapia gestaltistă",
    ),
    (
        re.compile(r"\bGestalt decât Rogers\b", re.I),
        "terapia gestaltistă decât consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bRogers decât terapia gestaltistă\b", re.I),
        "consilierea centrată pe persoană decât terapia gestaltistă",
    ),
    (
        re.compile(r"\bterapia gestaltistă decât Rogers\b", re.I),
        "terapia gestaltistă decât consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bpentru Rogers și Gestalt\b", re.I),
        "pentru consilierea centrată pe persoană (Carl R. Rogers) și terapia gestaltistă",
    ),
    (
        re.compile(r"\bRogers ar\b", re.I),
        "În consilierea centrată pe persoană (Carl R. Rogers), terapeutul ar",
    ),
    (
        re.compile(r"\bclient rogersian\b", re.I),
        "client în consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bUn client rogersian\b", re.I),
        "Un client în consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bcoordonatorul rogersian\b", re.I),
        "coordonatorul în consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bterapeut rogersian\b", re.I),
        "terapeut în consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bTerapeutul rogersian\b", re.I),
        "Terapeutul în consilierea centrată pe persoană",
    ),
    (
        re.compile(r"\bterapeut gestaltic\b", re.I),
        "terapeut în abordarea gestaltistă",
    ),
    (
        re.compile(r"\bTerapeutul gestaltic\b", re.I),
        "Terapeutul în abordarea gestaltistă",
    ),
    (
        re.compile(r"\bUn terapeut gestaltic\b", re.I),
        "Un terapeut în abordarea gestaltistă",
    ),
    (
        re.compile(r"\bclient gestaltic\b", re.I),
        "client în terapia gestaltistă",
    ),
    (
        re.compile(r"\bUn client gestaltic\b", re.I),
        "Un client în terapia gestaltistă",
    ),
    (
        re.compile(r"\bÎn grile,\s*", re.I),
        "",
    ),
    (
        re.compile(r"\bConfuzia examenului\b", re.I),
        "Confuzia frecventă",
    ),
    (
        re.compile(r"\bconfuzia examenului\b", re.I),
        "confuzia frecventă",
    ),
    (
        re.compile(r"\bTerapeutul Gestalt\b", re.I),
        "Terapeutul în abordarea gestaltistă",
    ),
    (
        re.compile(r"\bîn Gestalt\?\b", re.I),
        "în terapia gestaltistă?",
    ),
    (
        re.compile(r"\bîn Gestalt se\b", re.I),
        "în terapia gestaltistă se",
    ),
    (
        re.compile(r"\bîn Gestalt presupune\b", re.I),
        "în terapia gestaltistă presupune",
    ),
    (
        re.compile(r"\bFață de Gestalt,\b", re.I),
        "Față de terapia gestaltistă,",
    ),
    (
        re.compile(r"\bGestalt nu\b", re.I),
        "Terapia gestaltistă nu",
    ),
    (
        re.compile(r"\bGestalt —\b", re.I),
        "Terapia gestaltistă —",
    ),
    (
        re.compile(r"\bGestalt o\b", re.I),
        "Terapia gestaltistă o",
    ),
    (
        re.compile(r"\bla Gestalt\b", re.I),
        "terapia gestaltistă",
    ),
    (
        re.compile(r"\bGestalt — Fritz Perls\b", re.I),
        "Terapia gestaltistă (Fritz Perls)",
    ),
]

# Enunțuri care rămân invalide după reformulare (fără subiect / meta).
_INVALID_PATTERNS = [
    re.compile(r"^Gestalt l-ar\b", re.I),
    re.compile(r"^Gestalt ar\b", re.I),
    re.compile(r"\bÎn grile,\b", re.I),
    re.compile(r"\bConfuzia examenului\b", re.I),
    re.compile(r"^Același enunț\b", re.I),
    re.compile(r"^În examen,\s*itemul\b", re.I),
    re.compile(r"ca pe cineva care:\s*$", re.I),
]


def reformulate_stem(stem: str) -> str:
    """Reformulează enunțul: terapii ca orientări, fără meta-limbaj de grilă."""
    text = (stem or "").strip()
    if not text:
        return text
    if text in _STEM_EXACT:
        return _STEM_EXACT[text]
    for pattern, repl in _STEM_REGEX:
        text = pattern.sub(repl, text)
    return re.sub(r"\s{2,}", " ", text).strip()


def validate_stem(stem: str) -> list[str]:
    """Returnează lista problemelor rămase după reformulare."""
    text = reformulate_stem(stem)
    issues: list[str] = []
    for pattern in _INVALID_PATTERNS:
        if pattern.search(text):
            issues.append(f"pattern invalid: {pattern.pattern}")
    if re.search(r"\bGestalt l-ar\b", text, re.I):
        issues.append("Gestalt tratat ca persoană (l-ar)")
    if re.search(r"^Gestalt\b", text, re.I) and not re.search(
        r"Gestalt\s*\(|gestaltist", text, re.I
    ):
        issues.append("Gestalt fără context de terapie la început")
    return issues


def audit_all_stems(stems: list[str]) -> list[tuple[int, str, list[str]]]:
    """(index, stem, issues) pentru fiecare enunț problematic."""
    out: list[tuple[int, str, list[str]]] = []
    for i, stem in enumerate(stems):
        issues = validate_stem(stem)
        if issues:
            out.append((i, stem, issues))
    return out
