"""Opțiuni echilibrate pentru Psihoterapie II — fără indicii «doar/exclusiv» sau lungime."""

from __future__ import annotations

import re
from typing import Dict, List, Sequence, Tuple

from scripts.exam_item_utils import LETTERS, normalize_correct
from scripts.exam_ii_plausible_distractors import fix_exam_wrong_options

RESTRICTIVE_RE = re.compile(
    r"\b("
    r"doar|exclusiv|numai|niciodată|niciodata|mereu|întotdeauna|intotdeauna|"
    r"fără orice|fara orice|unicul|unică|singura|singurul|singura|"
    r"obligatoriu|obligatorie|absența oricărei|absenta oricarei"
    r")\b",
    re.IGNORECASE,
)

NU_DOAR_TAIL_RE = re.compile(r",?\s*nu doar\b.+$", re.IGNORECASE)
LEADING_RESTRICT_RE = re.compile(r"^(doar|exclusiv|numai)\s+", re.IGNORECASE)
AMBELE_EXCLUSIV_RE = re.compile(
    r"ambele urmăresc exclusiv|ambele resping în totalitate|"
    r"evită orice|respinge orice|lucrul exclusiv|centrat exclusiv|"
    r"focus exclusiv|accent exclusiv",
    re.IGNORECASE,
)

# Reformulări manuale — enunț exact → [opțiunea a, b, c, d], literă corectă
STEM_OPTION_OVERRIDES: Dict[str, Tuple[List[str], str]] = {
    "Terapia multimodală (Lazarus) evaluează:": (
        [
            "profilul multidimensional al clientului (comportament, afect, cogniție, senzație, relații)",
            "conflictele inconștiente și istoricul relațiilor obiectuale din copilărie",
            "transferul, contratransferul și repetarea relațiilor timpurii în cabinet",
            "patternurile de comunicare și granițele din sistemul familial extins",
        ],
        "a",
    ),
    "Terapia multimodală a lui Lazarus urmărește:": (
        [
            "potrivirea tehnicilor la profilul multidimensional al clientului",
            "explorarea liberă a asociațiilor și interpretarea viselor freudiene",
            "acceptarea necondiționată ca tehnică centrală în relație",
            "restructurarea ierarhiei generaționale în familie",
        ],
        "a",
    ),
    "Psihanaliza freudiană urmărește în principal:": (
        [
            "restructurarea personalității prin explorarea inconștientului",
            "eliminarea rapidă a simptomului fără explorarea sensului",
            "antrenarea abilităților sociale prin modelare și întărire",
            "clarificarea alegerilor și responsabilității în prezent",
        ],
        "a",
    ),
    "Dacă Eul nu reușește să medieze tensiunile dintre Sine, Supraeu și realitate, pot apărea:": (
        [
            "anxietate, conflicte interne și simptome nevrotice",
            "consolidarea automată a funcțiilor cognitive superioare",
            "reorganizarea structurală a granițelor familiale",
            "disocierea completă între trecut și prezent",
        ],
        "a",
    ),
    "Jung nu reduce psihicul la sexualitate, ci introduce:": (
        [
            "inconștientul colectiv, arhetipurile și procesul de individuare",
            "analiza transferului în relația terapeutică clasică",
            "tehnici comportamentale de expunere și relaxare",
            "restructurarea cognitivă a gândurilor automate",
        ],
        "a",
    ),
    "În abordarea existențială, anxietatea existențială poate fi înțeleasă ca:": (
        [
            "răspuns la libertate, responsabilitate și limitele condiției umane",
            "semn că trebuie aplicată desensibilizarea sistematică",
            "dovadă a unei fixări în stadiul anal freudian",
            "rezultat al unei distorsiuni cognitive beckiene",
        ],
        "a",
    ),
    "Psihoterapia Gestalt (Fritz Perls) este:": (
        [
            "experiențială, centrată pe aici și acum și pe conștientizare",
            "orientată spre interpretarea trecutului infantil în cabinet",
            "strict comportamentală, cu accent pe întăriri și pedepse",
            "nondirectivă, fără experimente sau intervenții active",
        ],
        "a",
    ),
    "Ciclul experienței Gestalt descrie:": (
        [
            "trecerea de la nevoie la contact și satisfacere sau blocaj",
            "etapele dezvoltării psihosexuale freudiene",
            "modelul Activator, Beliefs, Consequences (A-B-C) al terapiei rațional-emotive",
            "ierarhia granițelor în terapia de familie structurală",
        ],
        "a",
    ),
    "Intervențiile cognitiv-comportamentale sunt, de regulă:": (
        [
            "structurate, cu obiective clare și exerciții între ședințe",
            "orientate spre interpretarea simbolică a viselor",
            "bazate pe asociația liberă fără planificare",
            "limitate la ascultarea reflectivă nondirectivă",
        ],
        "a",
    ),
    "Abordarea strategică în terapia de familie se caracterizează prin:": (
        [
            "intervenții planificate pentru a modifica interacțiunile problematice",
            "explorarea liberă a inconștientului fără țintă relațională",
            "lucrul individual, fără implicarea membrilor familiei",
            "evitarea obiectivelor terapeutice explicite",
        ],
        "a",
    ),
    "Față de abordările strict deterministe, orientările umanist-experiențiale insistă că:": (
        [
            "persoana are potențial de creștere, alegeri și responsabilitate",
            "comportamentul este determinat exclusiv de reflexe condiționate",
            "simptomul se explică prin structura genetică, fără context",
            "schimbarea necesită interpretarea autoritară a visului",
        ],
        "a",
    ),
}


def _length(text: str) -> int:
    return len((text or "").strip())


def _median(values: Sequence[int]) -> int:
    if not values:
        return 60
    s = sorted(values)
    mid = len(s) // 2
    if len(s) % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) // 2


def _strip_restrictive_phrasing(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return t
    t = NU_DOAR_TAIL_RE.sub("", t).strip(" ,;—-")
    t = LEADING_RESTRICT_RE.sub("", t)
    t = re.sub(r"\b(exclusiv|numai)\s+", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\b(doar)\s+", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\bfără orice\b", "fără", t, flags=re.IGNORECASE)
    t = re.sub(r"\s+", " ", t).strip()
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t


def _expand_short(text: str, stem: str, target: int) -> str:
    """Completează opțiuni prea scurte cu formulări plauzibile, paralele."""
    t = text.strip()
    if _length(t) >= target - 8:
        return t
    stem_l = stem.lower()
    suffixes: List[str] = []
    if "freud" in stem_l or "psihodinamic" in stem_l or "psihanaliz" in stem_l:
        suffixes = [
            "în relația terapeutică",
            "în dinamica aparatului psihic",
            "în contextul conflictelor interne",
        ]
    elif "rogers" in stem_l or "centrat pe persoană" in stem_l:
        suffixes = [
            "în relația de ajutorare",
            "în procesul de autoactualizare",
            "în relația terapeut autentică",
        ]
    elif "gestalt" in stem_l:
        suffixes = [
            "în contactul din prezent",
            "în experiența de aici și acum",
            "în procesul de conștientizare",
        ]
    elif "familie" in stem_l or "sistemic" in stem_l or "structural" in stem_l:
        suffixes = [
            "în dinamica sistemului familial",
            "în patternurile relaționale dintre membri",
            "în organizarea subsistemelor familiale",
        ]
    elif "beck" in stem_l or "ellis" in stem_l or "cognitiv" in stem_l:
        suffixes = [
            "în modificarea patternurilor cognitive",
            "în relația dintre gânduri, emoții și comportament",
            "în intervenția pe termen scurt structurată",
        ]
    elif any(
        k in stem_l
        for k in (
            "job",
            "post",
            "ksao",
            "hr",
            "muncii",
            "muncă",
            "sarcin",
            "ierarh",
            "ocupați",
            "performanță",
            "training",
            "recrutare",
            "selecție",
            "salariz",
            "fjas",
            "o*net",
            "analiz",
            "description",
            "specification",
        )
    ):
        suffixes = [
            "în documentarea cerințelor postului",
            "în deciziile de selecție și evaluare",
            "în calibrarea description și specification",
        ]
    elif any(
        k in stem_l
        for k in (
            "evaluare",
            "test",
            "psihometric",
            "validitate",
            "fidelitate",
            "barem",
            "jvis",
            "motivați",
            "interese",
        )
    ):
        suffixes = [
            "în interpretarea rezultatelor standardizate",
            "în raport cu criteriul de validitate",
            "în procedura de administrare a testului",
        ]
    elif any(
        k in stem_l
        for k in (
            "tulburare",
            "dsm",
            "simptom",
            "episod",
            "diagnostic",
            "mania",
            "depresie",
            "ptsd",
            "psihopatolog",
        )
    ):
        suffixes = [
            "în evaluarea clinică a cazului",
            "în planul de intervenție",
            "în monitorizarea evoluției simptomatice",
        ]
    else:
        from scripts.exam_ii_plausible_distractors import detect_domain

        domain = detect_domain(stem)
        if domain == "hr":
            suffixes = [
                "în documentarea cerințelor postului",
                "în deciziile de selecție și evaluare",
                "în calibrarea description și specification",
            ]
        elif domain == "evaluare":
            suffixes = [
                "în interpretarea rezultatelor standardizate",
                "în raport cu criteriul de validitate",
                "în procedura de administrare a testului",
            ]
        elif domain == "psihopatologie":
            suffixes = [
                "în evaluarea clinică a cazului",
                "în planul de intervenție",
                "în monitorizarea evoluției simptomatice",
            ]
        else:
            suffixes = [
                "în procesul terapeutic",
                "în abordarea respectivă",
                "în contextul intervenției psihologice",
            ]
    for suffix in suffixes:
        candidate = f"{t.rstrip('.')}, {suffix}"
        if _length(candidate) <= target + 25:
            t = candidate
            break
    return t


def _trim_long(text: str, target: int) -> str:
    t = text.strip()
    if _length(t) <= target + 20:
        return t
    # Taie explicații meta după virgulă dacă opțiunea e prea lungă
    parts = re.split(r",\s+(?=[a-zăâîșț])", t, maxsplit=1)
    if len(parts) > 1 and _length(parts[0]) >= target - 15:
        return parts[0].strip()
    if len(t) > target + 35 and " — " in t:
        return t.split(" — ", 1)[0].strip()
    return t


def _has_bias(options: Sequence[str], correct_idxs: set[int]) -> bool:
    lengths = [_length(o) for o in options]
    if not lengths:
        return False
    med = _median(lengths)
    correct_lens = [lengths[i] for i in correct_idxs]
    wrong_lens = [lengths[i] for i in range(len(options)) if i not in correct_idxs]
    if correct_lens and wrong_lens:
        if max(correct_lens) > min(wrong_lens) + 18 and max(correct_lens) == max(lengths):
            return True
    for i, opt in enumerate(options):
        if RESTRICTIVE_RE.search(opt) or AMBELE_EXCLUSIV_RE.search(opt):
            return True
        if i not in correct_idxs and LEADING_RESTRICT_RE.match(opt.strip()):
            return True
    if max(lengths) - min(lengths) > 35:
        return True
    return False


def polish_option_set(
    stem: str,
    options: Sequence[str],
    correct: str,
) -> Tuple[List[str], str]:
    """Returnează opțiuni echilibrate; litera/literele corecte rămân pe aceleași poziții."""
    stem_key = (stem or "").strip()
    if stem_key in STEM_OPTION_OVERRIDES:
        return list(STEM_OPTION_OVERRIDES[stem_key][0]), STEM_OPTION_OVERRIDES[stem_key][1]

    opts = [str(o).strip() for o in options]
    if len(opts) != 4:
        return list(options), correct

    opts = fix_exam_wrong_options(stem, opts, correct)

    correct_letters = normalize_correct(correct)
    correct_idxs = {LETTERS.index(ch) for ch in correct_letters if ch in LETTERS}

    polished: List[str] = [_strip_restrictive_phrasing(o) for o in opts]
    needs_work = _has_bias(opts, correct_idxs) or polished != opts
    if not needs_work:
        return opts, correct

    target = _median([_length(o) for o in polished])
    target = max(target, 52)

    balanced: List[str] = []
    for i, opt in enumerate(polished):
        if i in correct_idxs:
            balanced.append(_trim_long(opt, target))
        else:
            expanded = _expand_short(opt, stem, target)
            balanced.append(_trim_long(expanded, target + 12))

    # A doua trecere pentru echilibrare fină
    lens = [_length(o) for o in balanced]
    med = _median(lens)
    final: List[str] = []
    for i, opt in enumerate(balanced):
        if lens[i] < med - 22:
            final.append(_expand_short(opt, stem, med))
        elif lens[i] > med + 28 and i in correct_idxs:
            final.append(_trim_long(opt, med + 10))
        else:
            final.append(opt)

    # După echilibrare: elimină sufixe off-topic (ex. „procesul terapeutic” la HR/evaluare)
    final = fix_exam_wrong_options(stem, final, correct)
    return final, correct


def polish_bank_row(row: Dict) -> Dict:
    from scripts.psihoterapie_ii_acronym_expand import expand_stem_acronyms
    from scripts.psihoterapie_ii_author_labels import expand_author_labels
    from scripts.psihoterapie_ii_stem_quality import reformulate_stem
    from scripts.psihoterapie_ii_stem_quality import reformulate_stem
    from scripts.psihoterapie_ii_stem_standalone import ensure_standalone_stem

    stem = ensure_standalone_stem(
        reformulate_stem(
            expand_author_labels(expand_stem_acronyms(str(row.get("stem", ""))))
        )
    )
    out = dict(row)
    out["stem"] = stem

    if row.get("tf") or not row.get("options"):
        return out

    raw_opts = [
        reformulate_stem(expand_author_labels(str(o).strip())) for o in row["options"]
    ]
    new_opts, new_correct = polish_option_set(
        stem,
        raw_opts,
        str(row.get("correct", "")),
    )
    out["options"] = new_opts
    out["correct"] = new_correct
    return out
