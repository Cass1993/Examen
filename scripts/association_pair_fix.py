"""Itemi «asocieri concept–descriere» — variante omogene, același format pereche."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.fix_tf_items import is_tf_item

ASSOCIATION_STEM_RE = re.compile(
    r"asocieri\s+concept|asocieri\s+termen|asocieri\s+.+\s*[-–]\s*defini|"
    r"asocieri\s+.+\s*defini",
    re.IGNORECASE,
)

PAIR_SEP_RE = re.compile(r"\s*[—–\-]\s*", re.UNICODE)

# cluster_id → listă (concept, definiție_corectă)
ASSOCIATION_CLUSTERS: Dict[str, List[Tuple[str, str]]] = {
    "stiluri_parentale": [
        (
            "Stilul parental autoritativ",
            "stil cu căldură ridicată și control ridicat, cu limite clare dar flexibile",
        ),
        (
            "Stilul parental autoritar",
            "stil cu control ridicat și căldură scăzută",
        ),
        (
            "Stilul parental permisiv",
            "stil cu căldură ridicată și limite reduse",
        ),
        (
            "Stilul parental neglijent",
            "stil cu căldură scăzută și control scăzut",
        ),
    ],
    "atașament": [
        (
            "Atașamentul securizant",
            "pattern în care copilul folosește îngrijitorul ca bază de siguranță și confort",
        ),
        (
            "Atașamentul evitant",
            "pattern în care copilul minimizează contactul și semnalele de nevoie la reunire",
        ),
        (
            "Atașamentul ambivalent/rezistent",
            "pattern cu căutare de apropiere combinată cu rezistență și calmare dificilă",
        ),
        (
            "Atașamentul dezorganizat",
            "pattern contradictoriu sau dezorientat, fără strategie coerentă de atașament",
        ),
        (
            "Baza de siguranță",
            "funcția figurii de atașament de a susține explorarea și reglarea emoțională",
        ),
        (
            "Situația stranie (Strange Situation)",
            "procedură de observare a atașamentului prin separări și reuniri scurte",
        ),
    ],
    "psihometrie_scoruri": [
        (
            "Scorul brut",
            "numărul sau suma răspunsurilor obținute înainte de transformări normative",
        ),
        (
            "Scorul real",
            "nivelul ipotetic al trăsăturii fără eroarea de măsurare",
        ),
        (
            "Scorul observat",
            "scorul obținut efectiv, compus din scor real și eroare",
        ),
        (
            "Scorul standardizat",
            "scor transformat pentru interpretare comparabilă prin norme",
        ),
        (
            "Eroarea standard a măsurării",
            "estimare a variației scorului observat în jurul scorului real",
        ),
        (
            "Standardizarea",
            "administrarea, scorarea și interpretarea testului după reguli uniforme",
        ),
        (
            "Operaționalizarea",
            "transformarea unui concept teoretic în indicatori observabili sau măsurabili",
        ),
    ],
    "validitate_fidelitate": [
        (
            "Validitatea de conținut",
            "măsura în care itemii acoperă domeniul relevant al constructului",
        ),
        (
            "Validitatea de construct",
            "măsura în care testul reflectă constructul teoretic vizat",
        ),
        (
            "Validitatea de criteriu",
            "relația scorului la test cu un criteriu extern relevant",
        ),
        (
            "Validitatea criterială",
            "relația scorului la test cu un criteriu extern relevant",
        ),
        (
            "Fidelitatea test-retest",
            "stabilitatea scorurilor la administrări repetate în condiții similare",
        ),
        (
            "Fidelitatea inter-evaluatori",
            "consistența acordului între evaluatori independenți",
        ),
    ],
    "genetica_comportamentala": [
        (
            "Modelul ACE",
            "separă variația trăsăturilor în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
        ),
        (
            "Studiile gemelare",
            "compară asemănarea gemenilor monozigoți și dizigoți pentru estimarea influențelor genetice și de mediu",
        ),
        (
            "Ereditabilitatea",
            "estimează proporția variației unei trăsături într-o populație atribuită diferențelor genetice",
        ),
        (
            "Epigenetica",
            "studiază modificări ale expresiei genelor fără schimbarea secvenței ADN",
        ),
        (
            "Metilarea ADN",
            "mecanism epigenetic care poate reduce sau modifica expresia unei gene",
        ),
        (
            "Studiile de adopție",
            "compară asemănarea dintre copii adoptați și părinții biologici versus cei adoptivi",
        ),
        (
            "Studiul de asociere la nivelul întregului genom (GWAS)",
            "caută asocieri între numeroase variante genetice și o trăsătură la nivel populational",
        ),
        (
            "Polimorfismul nucleotidic unic (SNP)",
            "variație la nivelul unui singur nucleotid în secvența ADN",
        ),
        (
            "Programarea epigenetică prin îngrijire maternă",
            "influența comportamentului matern asupra reglării stresului prin mecanisme epigenetice",
        ),
        (
            "Moștenirea epigenetică a fricii",
            "transmiterea unor efecte epigenetice ale experienței parentale asupra răspunsului la amenințare la urmași",
        ),
    ],
    "validitate_cercetare": [
        (
            "Validitatea internă",
            "măsura în care efectul observat poate fi atribuit variabilei manipulate",
        ),
        (
            "Validitatea externă",
            "măsura în care rezultatele pot fi generalizate la persoane, contexte sau situații",
        ),
        (
            "Cauzalitatea",
            "relație în care modificarea unei variabile produce schimbări în alta, în condiții controlate",
        ),
        (
            "Designul corelațional",
            "design non-experimental care examinează asocierea dintre variabile fără manipulare",
        ),
        (
            "Designul experimental",
            "plan de cercetare cu manipularea variabilei independente și controlul variabilelor alternative",
        ),
    ],
    "hackman_oldham": [
        (
            "Varietatea aptitudinilor",
            "măsura în care postul cere activități și abilități diverse",
        ),
        (
            "Identitatea sarcinii",
            "măsura în care postul permite realizarea unei lucrări complete și identificabile",
        ),
        (
            "Semnificația sarcinii",
            "impactul perceput al muncii asupra altor persoane sau asupra organizației",
        ),
        (
            "Autonomia",
            "libertatea angajatului de a decide cum și când își realizează munca",
        ),
        (
            "Feedbackul din muncă",
            "informația clară primită din activitate despre eficiența performanței",
        ),
        (
            "Job enlargement",
            "adăugarea de sarcini variate la același nivel de responsabilitate",
        ),
        (
            "Job enrichment",
            "creșterea responsabilității, autonomiei și profunzimii postului",
        ),
    ],
    "performanta_munca": [
        (
            "Performanța în sarcină",
            "realizarea activităților tehnice și centrale ale postului",
        ),
        (
            "Performanța contextuală",
            "comportamente care susțin mediul social și organizațional al muncii",
        ),
        (
            "Comportamentul civic organizațional",
            "comportament voluntar care susține colegii sau organizația",
        ),
        (
            "Comportamentul contraproductiv",
            "comportament care dăunează organizației, colegilor sau muncii",
        ),
    ],
    "criterii_performanta": [
        (
            "Criteriul deficient",
            "criteriu care omite aspecte relevante ale performanței",
        ),
        (
            "Criteriul contaminat",
            "criteriu influențat de factori irelevanți pentru performanța reală",
        ),
        (
            "Criteriul efectiv",
            "măsura concretă folosită pentru evaluarea performanței",
        ),
        (
            "Criteriul teoretic",
            "definiția conceptuală a constructului de performanță vizat",
        ),
    ],
    "teste_inteligenta": [
        (
            "Scala Binet-Simon",
            "instrument timpuriu pentru evaluarea aptitudinilor intelectuale la copii",
        ),
        (
            "Stanford-Binet",
            "revizuire a scalei Binet pentru evaluarea inteligenței",
        ),
        (
            "Scala Wechsler de inteligență pentru adulți (WAIS)",
            "scala Wechsler pentru evaluarea inteligenței adulților",
        ),
        (
            "Testul Jackson al intereselor vocaționale",
            "inventar folosit pentru evaluarea intereselor vocaționale",
        ),
        (
            "Inventarul Psihologic California",
            "inventar de personalitate orientat spre funcționarea interpersonală și socială normală",
        ),
    ],
    "stresori_ocupationali": [
        (
            "Ambiguitatea de rol",
            "neclaritatea așteptărilor, responsabilităților sau criteriilor de succes ale rolului",
        ),
        (
            "Conflictul de rol",
            "prezența unor cerințe incompatibile sau contradictorii ale rolului",
        ),
        (
            "Supraîncărcarea muncii",
            "solicitări excesive de muncă raportate la resursele disponibile",
        ),
        (
            "Burnoutul",
            "stare asociată cu epuizare, cinism/distanțare și eficacitate profesională redusă",
        ),
    ],
}

# index rapid concept normalizat → (cluster_id, definiție_corectă)
_CONCEPT_INDEX: Dict[str, Tuple[str, str]] = {}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _build_concept_index() -> None:
    if _CONCEPT_INDEX:
        return
    for cid, pairs in ASSOCIATION_CLUSTERS.items():
        for concept, defn in pairs:
            _CONCEPT_INDEX[_norm(concept)] = (cid, defn)
            short = concept.split("(")[0].strip()
            _CONCEPT_INDEX[_norm(short)] = (cid, defn)


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def is_association_item(item: Dict[str, Any]) -> bool:
    if is_tf_item(item):
        return False
    stem = str(item.get("intrebare") or item.get("text") or "")
    return bool(ASSOCIATION_STEM_RE.search(stem))


def parse_pair(text: str) -> Optional[Tuple[str, str]]:
    t = (text or "").strip()
    if not t or not PAIR_SEP_RE.search(t):
        return None
    parts = PAIR_SEP_RE.split(t, maxsplit=1)
    if len(parts) != 2:
        return None
    concept, defn = parts[0].strip(), parts[1].strip()
    if not concept or not defn:
        return None
    return concept, defn


def is_paired_option(text: str) -> bool:
    return parse_pair(text) is not None


def _cluster_scores_from_texts(texts: Sequence[str]) -> Dict[str, int]:
    _build_concept_index()
    scores: Dict[str, int] = {}
    for text in texts:
        pair = parse_pair(text)
        concept = pair[0] if pair else text
        key = _norm(concept)
        if key in _CONCEPT_INDEX:
            cid = _CONCEPT_INDEX[key][0]
            scores[cid] = scores.get(cid, 0) + 3
            continue
        for nk, (cid, _) in _CONCEPT_INDEX.items():
            if len(nk) > 8 and (nk in key or key in nk):
                scores[cid] = scores.get(cid, 0) + 2
                break
        low = key
        if "parental" in low or "stilul parental" in low:
            scores["stiluri_parentale"] = scores.get("stiluri_parentale", 0) + 2
        if "atașament" in low or "atasament" in low:
            scores["atașament"] = scores.get("atașament", 0) + 2
        if "validitate" in low or "fidelitate" in low or "scorul" in low:
            scores["validitate_fidelitate"] = scores.get("validitate_fidelitate", 0) + 1
            scores["psihometrie_scoruri"] = scores.get("psihometrie_scoruri", 0) + 1
        if "performanț" in low or "criteriul" in low:
            scores["criterii_performanta"] = scores.get("criterii_performanta", 0) + 1
            scores["performanta_munca"] = scores.get("performanta_munca", 0) + 1
        if "job " in low or "varietatea" in low or "autonomia" in low:
            scores["hackman_oldham"] = scores.get("hackman_oldham", 0) + 2
        if "wechsler" in low or "binet" in low or "inventar" in low:
            scores["teste_inteligenta"] = scores.get("teste_inteligenta", 0) + 2
        if (
            "genetic" in low
            or "epigenet" in low
            or "gemen" in low
            or "eritabil" in low
            or "modelul ace" in low
            or "gwas" in low
            or "metilare" in low
            or "polimorfism" in low
        ):
            scores["genetica_comportamentala"] = scores.get("genetica_comportamentala", 0) + 2
    return scores


def infer_association_cluster(
    item: Dict[str, Any],
    prefer_correct: bool = True,
) -> Optional[str]:
    opts = dict(item.get("variante") or item.get("options") or {})
    correct = {str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])}
    stem = str(item.get("intrebare") or item.get("text") or "").lower()

    texts: List[str] = []
    if prefer_correct:
        texts.extend(str(opts[c]) for c in correct if c in opts)
    texts.extend(str(v) for v in opts.values())

    scores = _cluster_scores_from_texts(texts)
    if "parental" in stem:
        scores["stiluri_parentale"] = scores.get("stiluri_parentale", 0) + 4
    if "atașament" in stem or "atasament" in stem:
        scores["atașament"] = scores.get("atașament", 0) + 4
    if "evaluare" in stem or "măsur" in stem or "masur" in stem:
        scores["psihometrie_scoruri"] = scores.get("psihometrie_scoruri", 0) + 2
        scores["validitate_fidelitate"] = scores.get("validitate_fidelitate", 0) + 2
    if "performanț" in stem or "muncă" in stem or "munca" in stem:
        scores["hackman_oldham"] = scores.get("hackman_oldham", 0) + 2
        scores["performanta_munca"] = scores.get("performanta_munca", 0) + 2
    if (
        "genetic" in stem
        or "epigenet" in stem
        or "gemen" in stem
        or "eritabil" in stem
        or "factorii genetici" in stem
    ):
        scores["genetica_comportamentala"] = scores.get("genetica_comportamentala", 0) + 4

    if not scores:
        return None
    return max(scores.items(), key=lambda x: (x[1], x[0]))[0]


def _format_pair(concept: str, definition: str) -> str:
    d = definition.strip()
    if d and d[0].islower():
        pass
    else:
        d = d[0].lower() + d[1:] if d else d
    return f"{concept.strip()} — {d}"


def _wrong_description_for(
    cluster_id: str,
    concept: str,
    used_defs: Set[str],
    seed: int,
) -> str:
    """Alege o definiție din același cluster, dar pentru alt concept (distractor plauzibil)."""
    pairs = ASSOCIATION_CLUSTERS.get(cluster_id, [])
    correct_def = ""
    for c, d in pairs:
        if _norm(c) == _norm(concept):
            correct_def = _norm(d)
            break

    candidates = [
        d for c, d in pairs if _norm(c) != _norm(concept) and _norm(d) not in used_defs
    ]
    if not candidates:
        candidates = [d for c, d in pairs if _norm(d) != correct_def]
    if not candidates:
        return "definiție care nu corespunde conceptului indicat"
    return candidates[seed % len(candidates)]


def needs_association_fix(item: Dict[str, Any]) -> bool:
    if not is_association_item(item):
        return False
    opts = dict(item.get("variante") or item.get("options") or {})
    if len(opts) < 3:
        return False

    paired = sum(1 for v in opts.values() if is_paired_option(str(v)))
    if paired < 2:
        return False

    correct = {str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])}
    cluster = infer_association_cluster(item)

    for letter, text in opts.items():
        t = str(text).strip()
        if not is_paired_option(t):
            return True
        if letter not in correct and cluster:
            concept, _ = parse_pair(t) or ("", "")
            c_scores = _cluster_scores_from_texts([t])
            if cluster not in c_scores and not c_scores:
                return True
    return False


def fix_association_pairs(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """Rescrie variante fără pereche sau din altă familie în format concept — descriere."""
    if not needs_association_fix(item):
        return item, False

    opts = dict(item.get("variante") or item.get("options") or {})
    correct = {str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])}
    cluster_id = infer_association_cluster(item)
    if not cluster_id or cluster_id not in ASSOCIATION_CLUSTERS:
        return item, False

    seed = _item_seed(item)
    pairs_list = ASSOCIATION_CLUSTERS[cluster_id]
    used_concepts: Set[str] = set()
    used_defs: Set[str] = set()

    for v in opts.values():
        p = parse_pair(str(v))
        if p:
            used_concepts.add(_norm(p[0]))
            used_defs.add(_norm(p[1]))

    new_opts = dict(opts)
    changed = False
    offset = 0

    for letter, text in opts.items():
        t = str(text).strip()
        if letter in correct and is_paired_option(t):
            continue

        if is_paired_option(t):
            concept, defn = parse_pair(t) or ("", "")
            c_scores = _cluster_scores_from_texts([t])
            if cluster_id in c_scores or not c_scores:
                continue
            # pereche din alt cluster — rescrie
        else:
            concept = t
            # termen gol sau fără descriere
            key = _norm(concept)
            if key in _CONCEPT_INDEX:
                cid, _ = _CONCEPT_INDEX[key]
                if cid != cluster_id:
                    concept = ""
            if not concept:
                for c, _d in pairs_list:
                    if _norm(c) not in used_concepts:
                        concept = c
                        break

        if not concept:
            unused = [
                c for c, _d in pairs_list if _norm(c) not in used_concepts
            ]
            if not unused:
                unused = [c for c, _d in pairs_list]
            concept = unused[(seed + offset) % len(unused)]
            offset += 1

        wrong_def = _wrong_description_for(
            cluster_id, concept, used_defs, seed + offset
        )
        new_pair = _format_pair(concept, wrong_def)
        if new_pair != t:
            new_opts[letter] = new_pair
            used_concepts.add(_norm(concept))
            used_defs.add(_norm(wrong_def))
            changed = True
            offset += 1

    if not changed:
        return item, False

    out = dict(item)
    if "variante" in item:
        out["variante"] = new_opts
    if "options" in item:
        out["options"] = new_opts
    return out, True


CLUSTER_STEM_PREFIX: Dict[str, str] = {
    "hackman_oldham": "În modelul Hackman și Oldham",
    "stresori_ocupationali": "În psihologia muncii",
    "performanta_munca": "În evaluarea performanței la locul de muncă",
    "validitate_fidelitate": "În evaluarea psihologică",
    "psihometrie_scoruri": "În psihometrie",
    "atașament": "În teoria atașamentului",
    "stiluri_parentale": "În psihologia parentalității",
    "metodologie_design": "În metodologia cercetării",
}


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def _correct(item: Dict[str, Any]) -> List[str]:
    return [str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])]


def is_broken_association_item(item: Dict[str, Any]) -> bool:
    """Enunț de asociere, dar variantele nu mai sunt perechi termen–descriere."""
    if not is_association_item(item):
        return False
    opts = _options(item)
    if len(opts) < 4:
        return False
    paired = sum(1 for v in opts.values() if is_paired_option(str(v)))
    return paired < 2


BARE_TERM_ALIASES: Dict[str, Tuple[str, str]] = {
    "autoritativ": ("stiluri_parentale", "Stilul parental autoritativ"),
    "autoritar": ("stiluri_parentale", "Stilul parental autoritar"),
    "permisiv": ("stiluri_parentale", "Stilul parental permisiv"),
    "neglijent": ("stiluri_parentale", "Stilul parental neglijent"),
    "securizant": ("atașament", "Atașamentul securizant"),
    "evitant": ("atașament", "Atașamentul evitant"),
    "dezorganizat": ("atașament", "Atașamentul dezorganizat"),
    "ambivalent": ("atașament", "Atașamentul ambivalent/rezistent"),
    "rezistent": ("atașament", "Atașamentul ambivalent/rezistent"),
}


def _lookup_concept_for_bare_term(term: str) -> Optional[Tuple[str, str, str]]:
    """Găsește (cluster_id, concept, definiție) pentru etichetă scurtă fără pereche."""
    _build_concept_index()
    text = (term or "").strip()
    if not text or is_paired_option(text):
        return None
    key = _norm(text)
    if key in _CONCEPT_INDEX:
        cid, defn = _CONCEPT_INDEX[key]
        for concept, correct_def in ASSOCIATION_CLUSTERS.get(cid, []):
            if _norm(correct_def) == _norm(defn) or _norm(concept) == key:
                return cid, concept, correct_def
    if key in BARE_TERM_ALIASES:
        cid, concept = BARE_TERM_ALIASES[key]
        for c, d in ASSOCIATION_CLUSTERS.get(cid, []):
            if _norm(c) == _norm(concept):
                return cid, c, d
    for alias, (cid, concept) in BARE_TERM_ALIASES.items():
        if alias in key:
            for c, d in ASSOCIATION_CLUSTERS.get(cid, []):
                if _norm(c) == _norm(concept):
                    return cid, c, d
    return None


def _lookup_concept_for_definition(defn: str) -> Optional[Tuple[str, str]]:
    """Găsește (cluster_id, concept) pentru o definiție din cluster."""
    text = (defn or "").strip()
    if not text:
        return None
    bare = _lookup_concept_for_bare_term(text)
    if bare:
        return bare[0], bare[1]
    n = _norm(text)
    for cid, pairs in ASSOCIATION_CLUSTERS.items():
        for concept, correct_def in pairs:
            cd = _norm(correct_def)
            if n == cd or n in cd or cd in n:
                return cid, concept
    return None


def _inline_concept_label(concept: str) -> str:
    label = concept.strip().strip("«»")
    if "(" in label:
        label = label.split("(")[0].strip()
    if label and label[0].isupper() and len(label.split()) <= 6:
        return label[0].lower() + label[1:]
    return label.lower()


def _build_conceptual_options(
    cluster_id: str,
    target_concept: str,
    target_def: str,
    seed: int,
) -> Tuple[Dict[str, str], str]:
    """Patru definiții comparabile; una corectă pentru conceptul vizat."""
    pool: List[str] = []
    for concept, defn in ASSOCIATION_CLUSTERS.get(cluster_id, []):
        pool.append(defn)
    for cid, pairs in ASSOCIATION_CLUSTERS.items():
        if cid == cluster_id:
            continue
        for _c, defn in pairs:
            if defn not in pool:
                pool.append(defn)
    pool = list(dict.fromkeys(pool))
    if target_def not in pool:
        pool.insert(0, target_def)

    letters = ["a", "b", "c", "d"]
    others = [d for d in pool if _norm(d) != _norm(target_def)]
    offset = seed % max(1, len(others))
    distractors = [others[(offset + i) % len(others)] for i in range(3)]
    ordered = [target_def] + distractors
    rot = seed % 4
    rotated = ordered[rot:] + ordered[:rot]
    options = {letters[i]: rotated[i] for i in range(4)}
    correct_letter = letters[rotated.index(target_def)]
    return options, correct_letter


def fix_broken_association_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """
    Convertește item rupt (enunț «asocieri», variante doar definiții)
    în întrebare conceptuală cu explicații comparabile.
    """
    if not is_broken_association_item(item):
        return item, False

    opts = _options(item)
    correct = _correct(item)
    seed = _item_seed(item)

    cluster_id = ""
    concept = ""
    target_def = ""

    candidates: List[str] = []
    if correct:
        candidates.extend(str(opts[c]).strip() for c in correct if c in opts)
    candidates.extend(str(v).strip() for v in opts.values())

    for text in candidates:
        bare = _lookup_concept_for_bare_term(text)
        if bare:
            cluster_id, concept, target_def = bare
            break
        match = _lookup_concept_for_definition(text)
        if match:
            cluster_id, concept = match
            target_def = text if not is_paired_option(text) else (parse_pair(text) or ("", text))[1]
            for c, d in ASSOCIATION_CLUSTERS.get(cluster_id, []):
                if _norm(c) == _norm(concept):
                    target_def = d
                    break
            break

    if not cluster_id:
        cluster_id = infer_association_cluster(item) or "hackman_oldham"
        pairs = ASSOCIATION_CLUSTERS.get(cluster_id, [])
        if not pairs:
            return item, False
        concept, target_def = pairs[seed % len(pairs)]

    prefix = CLUSTER_STEM_PREFIX.get(cluster_id, "În psihologia organizațională")
    inline = _inline_concept_label(concept)
    new_stem = f"{prefix}, {inline} se referă la:"

    new_options, correct_letter = _build_conceptual_options(
        cluster_id, concept, target_def, seed
    )

    out = dict(item)
    if "intrebare" in item:
        out["intrebare"] = new_stem
    if "text" in item:
        out["text"] = new_stem
    if "variante" in item:
        out["variante"] = new_options
    if "options" in item:
        out["options"] = new_options
    corr = [correct_letter]
    if "correct" in item:
        out["correct"] = corr
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    out["kind"] = "single"
    out["tip"] = "unic"
    out["explicatie"] = ""
    out["explanation"] = ""
    return out, True
