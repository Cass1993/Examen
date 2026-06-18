"""Audit calitate itemi — duplicate, gramatică, domeniu, omogenitate, similitudine."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Generator, Iterable, List, Set, Tuple

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.author_knowledge import lookup_author_by_stem  # noqa: E402
from scripts.distractor_fix import (  # noqa: E402
    AUTHOR_IN_OPTION_RE,
    FORM_AUTHOR,
    classify_option_form,
    norm,
    options_have_duplicates,
)
from scripts.domain_item_utils import (  # noqa: E402
    is_domain_filter_item,
    is_orphan_domain_item,
    labels_equivalent,
)
from scripts.romanian_grammar import (  # noqa: E402
    STEM_LABEL_RE,
    VERB_PLURAL_AFTER_LABEL,
    is_plural_label,
)

DEFAULT_PATH = APP_DIR / "data" / "questions.json"

AUTHOR_STEM_PATTERNS = (
    re.compile(
        r"^Care variantă descrie cel mai bine contribuția teoretică a lui\s+.+?\?\s*$",
        re.IGNORECASE,
    ),
    re.compile(r"^Contribuția teoretică asociată lui\s+.+?\s+este:\s*$", re.IGNORECASE),
    re.compile(r"^În .+, .+ este (?:asociat|asociată|formulat|formulată) (?:cu|de):\s*$", re.IGNORECASE),
    re.compile(r"^În .+, .+ este legat(?:ă)? (?:de|mai ales de):\s*$", re.IGNORECASE),
    re.compile(r"^În .+, .+ este formulat(?:ă)? (?:de|de:)\s*$", re.IGNORECASE),
)

SINGULAR_VERB_RE = re.compile(
    r"(?:«[^»]+»|[^«]+?)\s+(?:descrie|este|presupune|reflectă|postulează)\s*(?:mai ales)?:",
    re.IGNORECASE,
)

STOPWORDS = frozenset(
    {
        "a", "al", "ale", "ai", "au", "ca", "care", "cel", "cei", "cea", "ce",
        "cu", "de", "din", "doar", "este", "fi", "fie", "iar", "in", "în", "la",
        "le", "li", "lui", "mai", "ne", "nu", "o", "or", "pe", "pentru", "prin",
        "sa", "sau", "se", "si", "și", "sub", "sunt", "un", "una", "unui", "unor",
        "the", "and", "or", "of", "in", "to", "for",
    }
)


def walk_items(data: Any) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    """Parcurge itemii din format lots sau listă plată."""
    if isinstance(data, dict) and "lots" in data:
        for lot_name, lot_data in (data.get("lots") or {}).items():
            for q in lot_data.get("questions", []):
                yield lot_name, q
    elif isinstance(data, list):
        for q in data:
            lot = str(q.get("domeniu") or q.get("lot") or "General")
            yield lot, q
    elif isinstance(data, dict) and "text" in data and "options" in data:
        lot = str(data.get("domeniu") or data.get("lot") or "General")
        yield lot, data


def item_id(item: Dict[str, Any], lot: str = "") -> str:
    iid = item.get("id", item.get("id_local", "?"))
    if lot:
        return f"{lot}#{iid}"
    return str(iid)


def stem_text(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def option_dict(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def duplicate_option_texts(item: Dict[str, Any]) -> List[str]:
    """Returnează textele duplicate (normalizate) din același item."""
    opts = option_dict(item)
    seen: Dict[str, str] = {}
    dups: List[str] = []
    for v in opts.values():
        n = norm(v)
        if not n:
            continue
        if n in seen:
            dups.append(v.strip())
        else:
            seen[n] = v
    return dups


def has_plural_singular_mismatch(stem: str) -> bool:
    """Etichetă la plural + verb la singular (ex. «Normele» descrie:)."""
    if not stem:
        return False

    m = STEM_LABEL_RE.search(stem)
    if m:
        label = m.group(1)
        if is_plural_label(label):
            for singular, _plural in VERB_PLURAL_AFTER_LABEL:
                if singular in stem:
                    return True
        return False

    # Enunțuri fără ghilimele: «tipuri de atașament»-style sau plural explicit
    plural_markers = (
        r"\b(?:normele|scalele|tulburările|itemii|testele|stadii|teorii|tipuri|"
        r"stiluri|variabile|metodele|procedurile)\b"
    )
    if re.search(plural_markers, stem, re.IGNORECASE):
        for singular, _plural in VERB_PLURAL_AFTER_LABEL:
            if singular in stem.lower():
                # evită fals pozitive când verbul e deja la plural
                idx = stem.lower().find(singular)
                if idx >= 0:
                    return True
    return False


def is_orphan_domain(item: Dict[str, Any], lot: str) -> bool:
    if is_orphan_domain_item(item):
        return True
    stem = stem_text(item)
    domain = str(item.get("domeniu") or item.get("lot") or lot or "").strip()
    if not stem or not domain:
        return False
    m = re.search(r"«([^»]+)»", stem)
    if m and labels_equivalent(m.group(1), domain):
        kind = str(item.get("kind") or item.get("tip") or "").lower()
        correct = item.get("raspuns_corect") or item.get("correct") or []
        if kind in ("multi", "multiple") or len(correct) > 1:
            return True
    return False


def is_heterogeneous_options(item: Dict[str, Any]) -> bool:
    opts = option_dict(item)
    if len(opts) < 2:
        return False
    forms = {classify_option_form(str(v)) for v in opts.values() if (v or "").strip()}
    return len(forms) > 1


def is_author_stem(stem: str, item: Dict[str, Any]) -> bool:
    if lookup_author_by_stem(stem):
        return True
    for pat in AUTHOR_STEM_PATTERNS:
        if pat.match(stem):
            return True
    opts = option_dict(item)
    correct = [str(c).lower() for c in (item.get("correct") or item.get("raspuns_corect") or [])]
    author_opts = sum(
        1 for c in correct if c in opts and classify_option_form(str(opts[c])) == FORM_AUTHOR
    )
    if author_opts and author_opts == len(correct):
        # stem asks about association / author
        low = stem.lower()
        if any(
            k in low
            for k in (
                "asociat",
                "asociată",
                "legat de",
                "legată de",
                "formulat de",
                "formulată de",
                "contribuția",
                "autor",
            )
        ):
            return True
    return False


def author_stem_non_author_options(item: Dict[str, Any]) -> bool:
    stem = stem_text(item)
    if not is_author_stem(stem, item):
        return False
    opts = option_dict(item)
    return any(classify_option_form(str(v)) != FORM_AUTHOR for v in opts.values())


def tokenize(text: str) -> Set[str]:
    words = re.findall(r"[a-zăâîșț0-9]+", norm(text))
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def word_overlap_ratio(a: str, b: str) -> float:
    ta, tb = tokenize(a), tokenize(b)
    if not ta or not tb:
        return 0.0
    inter = ta & tb
    smaller = min(len(ta), len(tb))
    if smaller == 0:
        return 0.0
    return len(inter) / smaller


def similar_option_pairs(item: Dict[str, Any], threshold: float = 0.8) -> List[Tuple[str, str, float]]:
    opts = option_dict(item)
    texts = [(k, str(v).strip()) for k, v in opts.items() if (v or "").strip()]
    pairs: List[Tuple[str, str, float]] = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            k1, t1 = texts[i]
            k2, t2 = texts[j]
            if norm(t1) == norm(t2):
                continue
            ratio = word_overlap_ratio(t1, t2)
            if ratio >= threshold:
                pairs.append((f"{k1}:{t1[:50]}", f"{k2}:{t2[:50]}", ratio))
    return pairs


def examples(ids: Iterable[str], n: int = 3) -> List[str]:
    return list(ids)[:n]


def audit_bank(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    items = list(walk_items(data))

    cat1: List[str] = []
    cat2: List[str] = []
    cat3: List[str] = []
    cat4: List[str] = []
    cat5: List[str] = []
    cat6: List[str] = []
    cat7: List[str] = []

    for lot, item in items:
        iid = item_id(item, lot)
        stem = stem_text(item)

        if duplicate_option_texts(item) or options_have_duplicates(option_dict(item)):
            cat1.append(iid)

        if has_plural_singular_mismatch(stem):
            cat2.append(iid)

        if is_orphan_domain(item, lot):
            cat3.append(iid)

        if is_domain_filter_item(item):
            cat4.append(iid)

        if is_heterogeneous_options(item):
            cat5.append(iid)

        if author_stem_non_author_options(item):
            cat6.append(iid)

        if similar_option_pairs(item):
            cat7.append(iid)

    return {
        "path": str(path),
        "total_items": len(items),
        "categories": {
            "1_duplicate_options": {"count": len(cat1), "examples": examples(cat1)},
            "2_plural_singular_grammar": {"count": len(cat2), "examples": examples(cat2)},
            "3_orphan_domain": {"count": len(cat3), "examples": examples(cat3)},
            "4_domain_filter_stems": {"count": len(cat4), "examples": examples(cat4)},
            "5_heterogeneous_options": {"count": len(cat5), "examples": examples(cat5)},
            "6_author_stem_non_author_opts": {"count": len(cat6), "examples": examples(cat6)},
            "7_similar_options_80pct": {"count": len(cat7), "examples": examples(cat7)},
        },
        "ids": {
            "1_duplicate_options": cat1,
            "2_plural_singular_grammar": cat2,
            "3_orphan_domain": cat3,
            "4_domain_filter_stems": cat4,
            "5_heterogeneous_options": cat5,
            "6_author_stem_non_author_opts": cat6,
            "7_similar_options_80pct": cat7,
        },
    }


def print_report(result: Dict[str, Any]) -> None:
    print("=" * 72)
    print(f"AUDIT CALITATE ITEMI — {result['path']}")
    print("=" * 72)
    print(f"Total itemi scanati: {result['total_items']}")
    print()

    labels = {
        "1_duplicate_options": "1. Duplicate option texts (normalized, same item)",
        "2_plural_singular_grammar": "2. Plural label + singular verb (e.g. «Normele» descrie:)",
        "3_orphan_domain": "3. Orphan domain items (explanation / tautological «Domain» stems)",
        "4_domain_filter_stems": "4. Domain filter stems still present",
        "5_heterogeneous_options": "5. Heterogeneous options (author/term/definition mix)",
        "6_author_stem_non_author_opts": "6. Author stem items with non-author options",
        "7_similar_options_80pct": "7. Very similar option pairs (>80% word overlap)",
    }

    for key, label in labels.items():
        cat = result["categories"][key]
        print(f"{label}")
        print(f"  Count: {cat['count']}")
        print(f"  Examples: {', '.join(cat['examples']) if cat['examples'] else '(none)'}")
        print()

    overlap = Counter()
    for ids in result["ids"].values():
        for iid in ids:
            overlap[iid] += 1
    multi = sum(1 for c in overlap.values() if c > 1)
    print(f"Itemi cu >=2 categorii de probleme: {multi}")
    print()


def print_pipeline_summary() -> None:
    print("=" * 72)
    print("POLISH_QUESTION_ITEM PIPELINE (scripts/polish_text.py)")
    print("=" * 72)
    steps = [
        "1. polish_text — expand_abbreviations + fix_intrebare on stem/options/explanation",
        "2. upgrade_tf_item — convert trivial A/F items to 4-option MCQ (needs index+label_map)",
        "3. reformulate_domain_item — replace domain-filter stems with contextual items",
        "4. fix_orphan_domain_item — fix partially transformed domain items",
        "5. reformulate_item — natural exam-style stems + homogeneous options (natural_items.py)",
        "6. fix_item_distractors — author/reverse-desc/refer/heterogeneous/definition fixes",
        "7. fix_stem_grammar — plural/singular verb agreement after «label» (romanian_grammar.py)",
    ]
    for s in steps:
        print(f"  {s}")
    print()
    print("GAPS / LIMITATIONS:")
    gaps = [
        "- data/questions.json may not be batch-polished; app.py polishes at runtime only",
        "- fix_domain_item in distractor_fix.py is a no-op (delegated to reformulate_domain.py)",
        "- fix_stem_grammar only fixes verbs after «guillemet» labels; misses compound labels",
        "- is_plural_label misses some plural nouns inside long «label» phrases (tipuri/teorii in guillemets)",
        "- No pipeline step removes duplicate options (except fix_author_item side-effect)",
        "- No pipeline step detects >80% similar distractors",
        "- fix_orphan_domain_item / reformulate_domain_item need label_map+label_index",
        "- fix_natural_items.py patch_lots does not persist explanation/kind changes",
        "- Heterogeneous options only fixed when correct answers share one form",
        "- Category 4 items remain if _pick_concept_item fails (no fallback)",
    ]
    for g in gaps:
        print(f"  {g}")
    print()


def main() -> None:
    path = DEFAULT_PATH
    json_out: Path | None = APP_DIR / "data" / "audit_item_quality_report.json"
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--json-out" and i + 1 < len(args):
            json_out = Path(args[i + 1])
            i += 2
        elif not args[i].startswith("-"):
            path = Path(args[i])
            i += 1
        else:
            i += 1

    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)

    result = audit_bank(path)
    print_report(result)
    print_pipeline_summary()

    if json_out:
        json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON report: {json_out}")

    print("=" * 72)
    print("FILES LIKELY NEEDING CHANGES")
    print("=" * 72)
    files = [
        ("data/questions.json", "Primary bank — fix flagged items in-place or re-run batch scripts"),
        ("scripts/polish_text.py", "Orchestrator — add missing audit/fix steps if desired"),
        ("scripts/romanian_grammar.py", "Extend plural/singular fixes beyond «label» stems"),
        ("scripts/reformulate_domain.py", "Orphan + domain-filter reformulation (37+ items remain)"),
        ("scripts/distractor_fix.py", "Heterogeneous/author/duplicate distractor fixes"),
        ("scripts/natural_items.py", "Natural reformulation for concept/author items"),
        ("scripts/domain_item_utils.py", "Orphan/domain-filter detection patterns"),
        ("scripts/fix_broken_domain_items.py", "Batch fix orphan domain items on questions.json"),
        ("scripts/fix_natural_items.py", "Batch polish_question_item on questions.json lots"),
        ("scripts/fix_all_distractors.py", "Batch distractor homogenization"),
    ]
    for fp, reason in files:
        print(f"  {fp}")
        print(f"    → {reason}")
    print()


if __name__ == "__main__":
    main()
