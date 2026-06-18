"""Catalog autori: nume complete, contribuții, clustere pentru itemi omogeni."""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

AuthorEntry = Tuple[str, str, str]  # short, full, contribution

# short_key -> (full_name, contribution, cluster_id, descriptions[], natural_stem)
AUTHORS: Dict[str, dict] = {
    "I. P. Pavlov": {
        "full": "Ivan P. Pavlov",
        "contrib": "condiționarea răspunsurilor reflexe",
        "cluster": "behaviorist_learning",
        "descriptions": [
            "autor asociat cu condiționarea clasică",
            "autor asociat cu teoriile behavioriste/asociaționiste prin condiționarea clasică",
        ],
        "stem": "În abordarea comportamentală a învățării, condiționarea clasică a reflexelor este legată mai ales de:",
    },
    "J. B. Watson": {
        "full": "John B. Watson",
        "contrib": "condiționarea fricii în experimentul „Micul Albert”",
        "cluster": "behaviorist_learning",
        "descriptions": [
            "autor asociat cu condiționarea clasică a emoțiilor",
        ],
        "stem": "În abordarea comportamentală a personalității, studiul condiționării emoționale este legat mai ales de:",
    },
    "B. F. Skinner": {
        "full": "Burrhus F. Skinner",
        "contrib": "condiționarea operantă prin consecințe",
        "cluster": "behaviorist_learning",
        "descriptions": [
            "autor asociat cu condiționarea operantă",
        ],
        "stem": "În behaviorism, modificarea comportamentului prin consecințe este asociată mai ales cu:",
    },
    "E. L. Thorndike": {
        "full": "Edward L. Thorndike",
        "contrib": "legea efectului",
        "cluster": "behaviorist_learning",
        "descriptions": [
            "autor asociat cu legea efectului",
        ],
        "stem": "În învățarea prin încercare și eroare, legea efectului este formulată de:",
    },
    "J. Piaget": {
        "full": "Jean Piaget",
        "contrib": "stadiile dezvoltării cognitive",
        "cluster": "cognitive_development",
        "descriptions": [
            "autor asociat cu stadiile dezvoltării cognitive",
        ],
        "stem": "În psihologia dezvoltării cognitive, teoria stadiilor este asociată cu:",
    },
    "L. S. Vygotsky": {
        "full": "Lev S. Vygotsky",
        "contrib": "constructivismul sociocultural și zona proximei dezvoltări",
        "cluster": "cognitive_development",
        "descriptions": [
            "autor asociat cu constructivismul sociocultural și zona proximei dezvoltări",
        ],
        "stem": "În abordarea socioculturală a dezvoltării, zona proximei dezvoltării este legată de:",
    },
    "A. Bandura": {
        "full": "Albert Bandura",
        "contrib": "învățarea observațională și teoria social-cognitivă",
        "cluster": "cognitive_development",
        "descriptions": [
            "autor asociat cu teoria social-cognitivă și învățarea observațională",
        ],
        "stem": "În teoria social-cognitivă, învățarea prin observare și modelare este asociată cu:",
    },
    "S. Freud": {
        "full": "Sigmund Freud",
        "contrib": "stadiile psihosexuale și abordarea psihodinamică",
        "cluster": "psychodynamic",
        "descriptions": [
            "autor asociat cu stadiile psihosexuale",
        ],
        "stem": "În abordarea psihodinamică, teoria stadiilor psihosexuale este asociată cu:",
    },
    "E. Erikson": {
        "full": "Erik H. Erikson",
        "contrib": "stadiile psihosociale ale dezvoltării",
        "cluster": "psychodynamic",
        "descriptions": [
            "autor asociat cu stadiile psihosociale",
        ],
        "stem": "În dezvoltarea psihosocială, teoria celor opt stadii este formulată de:",
    },
    "G. W. Allport": {
        "full": "Gordon W. Allport",
        "contrib": "abordarea dispozițională și trăsăturile de personalitate",
        "cluster": "trait_theory",
        "descriptions": [
            "autor asociat cu teoria trăsăturilor și abordarea dispozițională a personalității",
        ],
        "stem": "În psihologia personalității, abordarea dispozițională a trăsăturilor este asociată cu:",
    },
    "R. B. Cattell": {
        "full": "Raymond B. Cattell",
        "contrib": "modelele factoriale ale trăsăturilor de personalitate",
        "cluster": "trait_theory",
        "descriptions": [
            "autor asociat cu modele factoriale ale trăsăturilor de personalitate",
        ],
        "stem": "În psihologia personalității, analiza factorială a trăsăturilor este asociată cu:",
    },
    "H. J. Eysenck": {
        "full": "Hans J. Eysenck",
        "contrib": "dimensiunile extraversie, neuroticism și psihoticism",
        "cluster": "trait_theory",
        "descriptions": [
            "autor asociat cu dimensiuni precum extraversie, neuroticism și psihoticism",
        ],
        "stem": "În modelul tridimensional al personalității, dimensiunile extraversie–neuroticism–psihoticism sunt asociate cu:",
    },
    "J. Bowlby": {
        "full": "John Bowlby",
        "contrib": "teoria atașamentului în relația timpurie copil–îngrijitor",
        "cluster": "attachment",
        "descriptions": [
            "autor asociat cu teoria atașamentului",
        ],
        "stem": "În psihologia dezvoltării timpurii, teoria atașamentului este asociată cu:",
    },
    "M. Ainsworth": {
        "full": "Mary Ainsworth",
        "contrib": "Situația stranie și tipurile de atașament",
        "cluster": "attachment",
        "descriptions": [
            "autoare asociată cu situația stranie și tipurile de atașament",
        ],
        "stem": "În cercetarea atașamentului, procedura Situația stranie este asociată cu:",
    },
    "L. Kohlberg": {
        "full": "Lawrence Kohlberg",
        "contrib": "stadiile dezvoltării morale",
        "cluster": "moral_development",
        "descriptions": [
            "autor asociat cu dezvoltarea morală",
        ],
        "stem": "În psihologia dezvoltării morale, teoria stadiilor este asociată cu:",
    },
    "W. Mischel": {
        "full": "Walter Mischel",
        "contrib": "modelul cognitiv-afectiv al personalității (CAPS)",
        "cluster": "interactionist",
        "descriptions": [
            "autor asociat cu teoria caps",
            "autor asociat cu teoria sistemului cognitiv-afectiv al personalității",
        ],
        "stem": "În abordarea interacționistă a personalității, modelul CAPS este asociat cu:",
    },
    "C. Rogers": {
        "full": "Carl Rogers",
        "contrib": "abordarea umanistă centrată pe persoană",
        "cluster": "humanistic",
        "descriptions": [
            "autor asociat cu teoriile umaniste ale învățării",
        ],
        "stem": "În abordarea umanistă a învățării, orientarea centrată pe persoană este asociată cu:",
    },
}

CLUSTERS: Dict[str, List[AuthorEntry]] = {
    "behaviorist_learning": [
        ("I. P. Pavlov", "Ivan P. Pavlov", "condiționarea răspunsurilor reflexe"),
        ("J. B. Watson", "John B. Watson", "condiționarea fricii în experimentul „Micul Albert”"),
        ("B. F. Skinner", "Burrhus F. Skinner", "condiționarea operantă prin consecințe"),
        ("E. L. Thorndike", "Edward L. Thorndike", "legea efectului"),
    ],
    "cognitive_development": [
        ("J. Piaget", "Jean Piaget", "stadiile dezvoltării cognitive"),
        ("L. S. Vygotsky", "Lev S. Vygotsky", "zona proximei dezvoltării și constructivismul sociocultural"),
        ("A. Bandura", "Albert Bandura", "învățarea observațională"),
        ("J. Bruner", "Jerome S. Bruner", "repere culturale și structurarea învățării"),
    ],
    "psychodynamic": [
        ("S. Freud", "Sigmund Freud", "stadiile psihosexuale"),
        ("E. Erikson", "Erik H. Erikson", "stadiile psihosociale"),
        ("A. Adler", "Alfred Adler", "sentimentul de inferioritate și stilul de viață"),
        ("C. G. Jung", "Carl G. Jung", "inconștientul colectiv și arhetipurile"),
    ],
    "trait_theory": [
        ("G. W. Allport", "Gordon W. Allport", "trăsăturile dispoziționale"),
        ("R. B. Cattell", "Raymond B. Cattell", "analiza factorială a trăsăturilor"),
        ("H. J. Eysenck", "Hans J. Eysenck", "extraversie, neuroticism și psihoticism"),
        ("P. T. Costa", "Paul T. Costa", "modelul celor cinci mari factori"),
    ],
    "attachment": [
        ("J. Bowlby", "John Bowlby", "teoria atașamentului"),
        ("M. Ainsworth", "Mary Ainsworth", "Situația stranie și tipurile de atașament"),
        ("H. Harlow", "Harry Harlow", "nevoia de contact confortabil la primate"),
        ("R. A. Spitz", "René A. Spitz", "deprivarea afectivă timpurie"),
    ],
    "moral_development": [
        ("L. Kohlberg", "Lawrence Kohlberg", "stadiile dezvoltării morale"),
        ("J. Piaget", "Jean Piaget", "judecata morală la copil"),
        ("C. Gilligan", "Carol Gilligan", "perspectiva eticii grijii"),
        ("E. Turiel", "Elliot Turiel", "domeniile sociale ale judecății morale"),
    ],
    "interactionist": [
        ("W. Mischel", "Walter Mischel", "modelul CAPS"),
        ("Y. Shoda", "Yuichi Shoda", "amprenta comportamentală și regularități situaționale"),
        ("J. B. Watson", "John B. Watson", "behaviorismul clasic"),
        ("G. W. Allport", "Gordon W. Allport", "trăsăturile și influența situației"),
    ],
    "humanistic": [
        ("C. Rogers", "Carl Rogers", "terapia centrată pe persoană"),
        ("A. Maslow", "Abraham Maslow", "ierarhia nevoilor"),
        ("V. Frankl", "Viktor E. Frankl", "logoterapia și sensul existențial"),
        ("R. May", "Rollo May", "anxietatea existențială"),
    ],
}

_DESC_INDEX: Dict[str, str] = {}
_SHORT_INDEX: Dict[str, str] = {}


def _norm(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[«»\"'?!.:,;()\[\]]", "", s)
    return s


def _build_indexes() -> None:
    if _DESC_INDEX:
        return
    for short, data in AUTHORS.items():
        _SHORT_INDEX[_norm(short)] = short
        _SHORT_INDEX[_norm(data["full"])] = short
        for desc in data.get("descriptions", []):
            _DESC_INDEX[_norm(desc)] = short
        _DESC_INDEX[_norm(data["contrib"])] = short


def match_author(text: str) -> Optional[str]:
    _build_indexes()
    t = _norm(text)
    if not t:
        return None
    for desc, short in sorted(_DESC_INDEX.items(), key=lambda x: -len(x[0])):
        if desc in t or t in desc:
            return short
    for key, short in _SHORT_INDEX.items():
        if key in t:
            return short
    m = re.search(
        r"contribuția teoretică a lui\s+([A-ZĂÂÎȘȚ]\.\s*(?:[A-ZĂÂÎȘȚ]\.\s*)?[A-ZĂÂÎȘȚ][^\?]+)",
        text,
        re.I,
    )
    if m:
        return match_author(m.group(1))
    m = re.search(r"«([^»]+)»", text)
    if m:
        return match_author(m.group(1))
    return None


def format_author_option(short: str) -> Optional[str]:
    _build_indexes()
    data = AUTHORS.get(short)
    if not data:
        return None
    return f"{data['full']} — {data['contrib']}"


def natural_stem_for_author(short: str) -> Optional[str]:
    data = AUTHORS.get(short)
    return data.get("stem") if data else None


_STEM_TO_AUTHOR: Dict[str, str] = {}


def _build_stem_index() -> None:
    if _STEM_TO_AUTHOR:
        return
    for short, data in AUTHORS.items():
        stem = data.get("stem")
        if stem:
            _STEM_TO_AUTHOR[_norm(stem)] = short


def lookup_author_by_stem(stem: str) -> Optional[str]:
    """Potrivește enunțul catalogat al unui autor (ex. Erikson — opt stadii)."""
    _build_stem_index()
    return _STEM_TO_AUTHOR.get(_norm(stem))


def cluster_for_author(short: str) -> Optional[str]:
    data = AUTHORS.get(short)
    return data.get("cluster") if data else None


def _entry_text(entry: AuthorEntry) -> str:
    return f"{entry[1]} — {entry[2]}"


def build_cluster_options(
    cluster_id: str, correct_short: str, seed: int = 0
) -> Optional[Tuple[Dict[str, str], str]]:
    members = CLUSTERS.get(cluster_id)
    if not members:
        return None
    letters = ["a", "b", "c", "d"]
    pool = list(members)
    if correct_short not in {m[0] for m in pool}:
        data = AUTHORS.get(correct_short)
        if data:
            pool.insert(0, (correct_short, data["full"], data["contrib"]))

    unique: List[AuthorEntry] = []
    seen: set[str] = set()
    for entry in pool:
        key = _norm(_entry_text(entry))
        if key in seen:
            continue
        seen.add(key)
        unique.append(entry)
    if not unique:
        return None

    offset = seed % len(unique)
    ordered: List[AuthorEntry] = []
    for entry in unique[offset:] + unique[:offset]:
        key = _norm(_entry_text(entry))
        if key not in {_norm(_entry_text(e)) for e in ordered}:
            ordered.append(entry)
    for entry in unique:
        if len(ordered) >= 4:
            break
        key = _norm(_entry_text(entry))
        if key not in {_norm(_entry_text(e)) for e in ordered}:
            ordered.append(entry)
    if len(ordered) < 4:
        return None

    ordered = ordered[:4]
    options: Dict[str, str] = {}
    correct_letter = "a"
    for i, entry in enumerate(ordered):
        options[letters[i]] = _entry_text(entry)
        if entry[0] == correct_short:
            correct_letter = letters[i]
    return options, correct_letter
