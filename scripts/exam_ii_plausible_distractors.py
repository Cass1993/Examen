"""Înlocuiește distractori prea ușor de eliminat în loturile examen II."""

from __future__ import annotations

import hashlib
import re
from typing import Dict, List, Optional, Sequence, Set, Tuple

from scripts.exam_item_utils import LETTERS, normalize_correct

# Absolutisme, negări evidente, formulări imposibil de ales
EASY_WRONG_RE = re.compile(
    r"\b("
    r"exclusiv\w*|complet\w*|oricărui|oricarei|orice\s+document|niciodată|niciodata|"
    r"întotdeauna|intotdeauna|automat(?!iz)|nu mai este nevoie|evitarea oricărui|"
    r"măsurarea exclusivă|irelevant pentru procesul terapeutic|"
    r"înlocuiește complet|elimină complet|eliminarea completă|depinde exclusiv|"
    r"ignor\w+|absența oricărei|absenta oricarei|evitarea completă|respingerea completă|"
    r"excluderea completă|exclude complet|renunțarea la orice|fără nicio|fără niciun|"
    r"dispariția completă|nu are niciodată|nu presupune niciodată|nu poate fi niciodată|"
    r"vinovăției exclusive|explorării exclusive|centrat exclusiv|lucrul exclusiv|"
    r"focus exclusiv|accent exclusiv|medierea exclusivă|tratare exclusivă"
    r")\b",
    re.IGNORECASE,
)

OFFTOPIC_ABSURD_RE = re.compile(
    r"("
    r"procesul terapeutic|coeficient(?:ul)? de inteligență|tulburări de personalitate|"
    r"diagnostic(?:ul)?(?:ul)?\s+psihiatric|interviu clinic|spitalizare psihiatrică|"
    r"campaignii publicitare|marketing|evaluare clinică a personalității|"
    r"test proiectiv de personalitate|coeficientului de inteligență"
    r")",
    re.IGNORECASE,
)

# Înlocuiri directe (pattern → text nou plauzibil dar greșit în context)
DIRECT_REPLACEMENTS: List[Tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"ignor\w+.*(?:ksao|cerinț|sarcin)", re.I),
        "calculul salarial bazat doar pe gradul ierarhic, fără date despre sarcini",
    ),
    (
        re.compile(r"ignor\w+.*context(?:ual)?", re.I),
        "interpretarea scorurilor cu bareme internaționale nemodificate local",
    ),
    (
        re.compile(r"ignor\w+.*instruc", re.I),
        "administrarea testului cu formulări diferite de itemi între subiecți",
    ),
    (
        re.compile(r"ignor\w+.*scor", re.I),
        "raportarea scorurilor brute fără verificarea valorilor extreme",
    ),
    (
        re.compile(r"ignor\w+.*tentativ", re.I),
        "plan de siguranță fără întrebare despre comportament autolesiv anterior",
    ),
    (
        re.compile(r"ignor\w+.*educațional", re.I),
        "consiliere vocațională bazată doar pe profilul RIASEC, fără context școlar",
    ),
    (
        re.compile(r"ignor\w+.*(?:social|etic)", re.I),
        "evaluarea competențelor emoționale doar prin auto-raportare izolată",
    ),
    (
        re.compile(r"ignor\w+.*comportament observabil", re.I),
        "explicații strict intrapsihice, fără date comportamentale sistematice",
    ),
    (
        re.compile(r"ignor\w+.*proces", re.I),
        "notarea simptomelor fără monitorizarea evoluției în timp",
    ),
    (
        re.compile(r"ignor\w+.*emic", re.I),
        "compararea directă a scorurilor între culturi fără validare locală",
    ),
    (
        re.compile(r"absența oricărei componente fiziolog", re.I),
        "simptome prezente doar în situații interpersonale, fără activare autonomă",
    ),
    (
        re.compile(r"absența oricărei componente (?:afectiv|emoțion)", re.I),
        "tablou limitat la simptome cognitive, fără modificare afectivă marcată",
    ),
    (
        re.compile(r"absența oricărei", re.I),
        "tablou clinic redus la un singur simptom, fără alte semne asociate",
    ),
    (
        re.compile(r"eliminarea completă", re.I),
        "reducerea semnificativă, dar nu eliminarea totală",
    ),
    (
        re.compile(r"elimină complet", re.I),
        "reduce parțial, fără a elimina integral",
    ),
    (
        re.compile(r"măsurare.*personalitate", re.I),
        "accentul pe scoruri cantitative din chestionar, fără verificare calitativă",
    ),
    (
        re.compile(r"evitare.*document", re.I),
        "redactarea description doar din observație, fără interviu cu ocupantul",
    ),
    (
        re.compile(r"coeficient.*inteligen", re.I),
        "compararea scorurilor brute între candidați, fără raportare la cerințele postului",
    ),
    (
        re.compile(r"înlocuie.*interviu.*angajare", re.I),
        "standardizarea selecției prin chestionar unic, fără probă practică",
    ),
    (
        re.compile(r"irelevant pentru procesul terapeutic", re.I),
        "util pentru definirea competențelor tehnice și a contextului de lucru",
    ),
    (
        re.compile(r"interpretarea scorurilor exclusiv", re.I),
        "compararea distanțelor între valori, presupunând un zero arbitrar",
    ),
    (
        re.compile(r"utilizarea exclusivă a scorurilor pe scări nominale", re.I),
        "aplicarea testelor parametrice fără verificarea presupunerilor",
    ),
    (
        re.compile(r"motivația depinde exclusiv", re.I),
        "motivația depinde doar de recompensele imediate, nu de sensul muncii",
    ),
    (
        re.compile(r"personalitatea se explică exclusiv", re.I),
        "personalitatea se explică prin trăsături stabile, independent de situație",
    ),
    (
        re.compile(r", în procesul terapeutic", re.I),
        "",
    ),
    (
        re.compile(r"explorarea exclusivă a stadiilor psihosexuale", re.I),
        "explorarea liberă a asociațiilor și a viselor în relația terapeutică",
    ),
    (
        re.compile(r"lucrul exclusiv cu conflicte inconștiente", re.I),
        "lucrul cu obiective comportamentale concrete, fără contract terapeutic",
    ),
]

DOMAIN_POOLS: Dict[str, List[str]] = {
    "hr": [
        "documentarea postului doar din date cantitative de chestionar",
        "prioritizarea comparării salariilor cu media pieței externe",
        "redactarea job specification înainte de analiza sarcinilor",
        "clasificarea postului la nivel de ocupație, fără sarcini detaliate",
        "ancorarea postului în date O*NET, fără analiză internă a sarcinilor",
        "calculul salarial bazat pe vechime, nu pe complexitatea rolului",
        "selecția bazată pe titlul formal, fără profil KSAO",
    ],
    "evaluare": [
        "interpretarea scorurilor fără raportare la baremul de administrare",
        "generalizarea rezultatelor la toate populațiile fără restandardizare",
        "prioritizarea validității de fațadă în detrimentul validității de conținut",
        "utilizarea testelor doar pentru screening, fără interpretare contextuală",
        "administrarea testului cu timpi diferiți între subiecți",
        "raportarea scorurilor brute fără norme de referință",
    ],
    "psihopatologie": [
        "explicarea simptomelor doar prin stres cotidian recent",
        "diagnostic pe baza unui singur simptom dominant la interviu",
        "tratarea episodului acut fără plan de continuare a îngrijirii",
        "atribuirea simptomelor doar factorilor psihodinamici",
        "evaluarea evoluției doar prin chestionar, fără interviu clinic",
        "interpretarea remisiunii parțiale ca recuperare totală",
    ],
    "psihoterapie": [
        "reducerea ședințelor la suport nonspecific, fără obiective explicite",
        "lucrul doar cu simptomul prezent, fără relație terapeutică",
        "aplicarea aceleiași tehnici indiferent de orientarea teoretică",
        "interpretarea transferului fără contractul de lucru inițial",
        "limitarea intervenției la sfaturi generale, fără tehnică specifică",
    ],
}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def detect_domain(stem: str) -> str:
    s = (stem or "").lower()
    if re.search(
        r"job|post\b|ksao|hr|recrutare|selecți|salariz|fjas|o\*net|description|"
        r"specification|analiz[aă]|ierarhia muncii|psihologia muncii|duty|ocupați|"
        r"performanț|training|incidente critice|fjass?|design(?:ul)? muncii|"
        r"hackman|oldham|mps|empowerment|jd-r|engagement|burnout|selecți|"
        r"predictor|criteriu|gma|validitate incremental|selection ratio|base rate",
        s,
    ):
        return "hr"
    if re.search(
        r"evaluare|test|psihometric|validitate|fidelitate|barem|etic|standardiz|"
        r"reliabilit|corelați|jvis|interese vocaționale|motivați|inteligenț",
        s,
    ):
        return "evaluare"
    if re.search(
        r"tulburare|dsm|simptom|episod|diagnostic|mania|depresie|ptsd|toc|"
        r"schizofren|suicid|bipolar|anxietate|psihopatolog",
        s,
    ):
        return "psihopatologie"
    return "psihoterapie"


def _is_easy_wrong(text: str, stem: str) -> bool:
    t = (text or "").strip()
    if not t:
        return False
    domain = detect_domain(stem)
    if OFFTOPIC_ABSURD_RE.search(t):
        if domain == "psihoterapie" and re.search(
            r"procesul terapeutic", t, re.I
        ) and not re.search(r"irelevant", t, re.I):
            return False
        return True
    if EASY_WRONG_RE.search(t):
        return True
    return False


def _direct_replace(text: str) -> Optional[str]:
    for pat, repl in DIRECT_REPLACEMENTS:
        if pat.search(text):
            if repl == "":
                t = pat.sub("", text).strip(" ,;—-")
                if t and t[0].islower():
                    t = t[0].upper() + t[1:]
                return t or text
            return repl
    return None


def _pick_pool_replacement(
    stem: str, used: Set[str], seed: int, offset: int
) -> str:
    pool = DOMAIN_POOLS.get(detect_domain(stem), DOMAIN_POOLS["psihoterapie"])
    clean = [p for p in pool if not EASY_WRONG_RE.search(p)]
    if not clean:
        clean = list(pool)
    available = [p for p in clean if _norm(p) not in used] or clean
    idx = (seed + offset) % len(available)
    return available[idx]


def _soften_remaining(text: str) -> str:
    """Ultimă plasă: reformulează absolutismele rămase."""
    t = (text or "").strip()
    t = re.sub(r"\b(exclusiv\w*|complet\w*)\b", "", t, flags=re.I)
    t = re.sub(r"\bignor\w+\b", "prioritizează", t, flags=re.I)
    t = re.sub(r"\babsența oricărei\b", "lipsa", t, flags=re.I)
    t = re.sub(r"\boricărui\b", "unor", t, flags=re.I)
    t = re.sub(r"\belimină\b", "reduce", t, flags=re.I)
    t = re.sub(r"\bînlocuiește\b", "suplimentează", t, flags=re.I)
    t = re.sub(r"\s+", " ", t).strip(" ,;—-")
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    return t or text


def fix_easy_wrong_option(
    text: str,
    stem: str,
    used: Set[str],
    seed: int,
    offset: int,
) -> str:
    if not _is_easy_wrong(text, stem):
        return text
    direct = _direct_replace(text)
    if direct and _norm(direct) not in used:
        return direct
    candidate = _pick_pool_replacement(stem, used, seed, offset)
    if _norm(candidate) in used:
        candidate = _soften_remaining(text)
    return candidate


def fix_exam_wrong_options(
    stem: str,
    options: Sequence[str],
    correct: str,
) -> List[str]:
    """Înlocuiește distractorii prea ușori; păstrează opțiunile corecte."""
    opts = [str(o).strip() for o in options]
    if len(opts) != 4:
        return list(options)

    correct_letters = set(normalize_correct(correct))
    used = {_norm(o) for o in opts}
    seed = int(hashlib.md5(f"{stem}|{correct}".encode()).hexdigest()[:8], 16)
    out: List[str] = []

    for i, opt in enumerate(opts):
        letter = LETTERS[i]
        if letter in correct_letters:
            out.append(opt)
            continue
        fixed = fix_easy_wrong_option(opt, stem, used, seed, i * 17 + 3)
        if _norm(fixed) in used and _norm(fixed) != _norm(opt):
            fixed = _pick_pool_replacement(stem, used, seed, i * 31 + 7)
        used.add(_norm(fixed))
        out.append(fixed)

    return out
