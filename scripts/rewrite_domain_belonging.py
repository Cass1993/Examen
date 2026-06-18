"""Elimină itemii «aparțin domeniului» — rescriere în întrebări conceptuale reale."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from scripts.audit_item_quality import item_id, stem_text, walk_items
from scripts.concept_clusters import build_concept_item
from scripts.domain_concept_specs import build_domain_concept_item
from scripts.domain_item_utils import (
    ORPHAN_DOMAIN_EXPLANATION,
    ORPHAN_DOMAIN_EXPLANATION_ALT,
    domain_from_filter_stem,
    is_domain_belonging_item,
    is_domain_belonging_stem,
    is_domain_filter_item,
)
from scripts.author_knowledge import (
    build_cluster_options,
    cluster_for_author,
    match_author,
    natural_stem_for_author,
)
from scripts.label_definition_index import build_contextual_definition_item

ConceptResult = Tuple[str, Dict[str, str], str]

OBVIOUS_CROSS_DOMAIN_RE = re.compile(
    r"\b("
    r"id|superego|ego\b|analiza muncii|zona proxim|vygotsky|piaget|"
    r"anhedonia|burnoutul|anova|eșantionul|populația|validitatea de criteriu|"
    r"hackman|job enlargement|scala binet"
    r")\b",
    re.I,
)

CLUSTER_STEM_RE = re.compile(r"tulburări aparțin Clusterului\s+([ABC])\b", re.I)

CLUSTER_LABELS = {
    "A": "Clusterul A — tulburări cu suspiciune, detașare socială sau comportament ciudat",
    "B": "Clusterul B — tulburări cu instabilitate emoțională, dramatism sau impulsivitate",
    "C": "Clusterul C — tulburări cu anxietate socială, dependență sau evitare",
}

PERSONALITY_DISORDER_CLUSTER = {
    "tulburarea paranoidă": "A",
    "tulburarea schizoidă": "A",
    "tulburarea schizotipală": "A",
    "tulburarea antisocială": "B",
    "tulburarea borderline": "B",
    "tulburarea histrionică": "B",
    "tulburarea narcisică": "B",
    "tulburarea evitantă": "C",
    "tulburarea dependentă": "C",
    "tulburarea obsesiv-compulsivă": "C",
}


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', '')}|{item.get('text', item.get('intrebare', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _stem(item: Dict[str, Any]) -> str:
    return str(item.get("intrebare") or item.get("text") or "").strip()


def _options(item: Dict[str, Any]) -> Dict[str, str]:
    return dict(item.get("variante") or item.get("options") or {})


def _correct(item: Dict[str, Any]) -> List[str]:
    return [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]


def _norm_label(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def _usable_anchor(label: str, stem: str) -> bool:
    if not label or len(label.strip()) < 3:
        return False
    if OBVIOUS_CROSS_DOMAIN_RE.search(label):
        return False
    if labels_equivalent_safe(label, stem):
        return False
    return True


def labels_equivalent_safe(label: str, stem: str) -> bool:
    from scripts.domain_item_utils import labels_equivalent

    domain = domain_from_filter_stem(stem) if is_domain_filter_item({"text": stem}) else ""
    if domain and labels_equivalent(label, domain):
        return True
    m = re.search(r"domeniului\s+(.+?)\?", stem, re.I)
    if m and labels_equivalent(label, m.group(1).strip("«»")):
        return True
    return False


def _anchor_candidates(item: Dict[str, Any]) -> List[str]:
    opts = _options(item)
    correct = _correct(item)
    stem = _stem(item)
    seed = _item_seed(item)

    correct_labels = [str(opts[c]) for c in correct if c in opts]
    all_labels = [str(v) for v in opts.values()]

    pool = [l for l in correct_labels if _usable_anchor(l, stem)]
    if not pool:
        pool = [l for l in all_labels if _usable_anchor(l, stem)]
    if not pool:
        pool = [l for l in all_labels if l.strip()]

    if not pool:
        return []

    offset = seed % len(pool)
    return pool[offset:] + pool[:offset]


def _disorder_cluster(label: str) -> Optional[str]:
    key = _norm_label(label)
    for disorder, cluster in PERSONALITY_DISORDER_CLUSTER.items():
        if disorder in key or key in disorder:
            return cluster
    return None


def _rewrite_cluster_membership(item: Dict[str, Any]) -> Optional[ConceptResult]:
    stem = _stem(item)
    m = CLUSTER_STEM_RE.search(stem)
    if not m:
        return None

    anchors = _anchor_candidates(item)
    if not anchors:
        return None

    disorder = anchors[0].strip()
    cluster = _disorder_cluster(disorder) or m.group(1).upper()
    new_stem = f"{disorder} se încadrează în clusterul:"
    new_opts = {
        "a": CLUSTER_LABELS["A"],
        "b": CLUSTER_LABELS["B"],
        "c": CLUSTER_LABELS["C"],
        "d": "Clusterul D — tulburări cu simptome pozitive și negative ale psihozei",
    }
    letter = {"A": "a", "B": "b", "C": "c"}.get(cluster, "c")
    return new_stem, new_opts, letter


def _try_author_item(label: str, seed: int) -> Optional[ConceptResult]:
    author = match_author(label)
    if not author:
        return None
    cluster = cluster_for_author(author)
    if not cluster:
        return None
    built = build_cluster_options(cluster, author, seed)
    if not built:
        return None
    options, correct_letter = built
    stem = natural_stem_for_author(author) or f"Contribuția teoretică asociată lui {author} este:"
    return stem, options, correct_letter


def _pick_concept_item(
    correct_labels: List[str],
    domain: str,
    seed: int,
    label_index: Any,
    bank_index: Any,
    label_map: Dict[str, str],
) -> Optional[ConceptResult]:
    if not correct_labels:
        return None
    from scripts.domain_item_utils import labels_equivalent

    ordered = correct_labels[seed % len(correct_labels) :] + correct_labels[
        : seed % len(correct_labels)
    ]
    for anchor in ordered:
        if labels_equivalent(anchor, domain):
            continue
        built = build_domain_concept_item(anchor, seed)
        if built:
            return built
        built = _try_author_item(anchor, seed)
        if built:
            return built
        if label_index is not None and bank_index is not None:
            built = build_contextual_definition_item(
                anchor,
                domain,
                seed,
                sibling_labels=correct_labels,
                label_index=label_index,
                bank_index=bank_index,
                label_map=label_map,
            )
            if built:
                return built
    return None


def _try_build_from_anchor(anchor: str, seed: int) -> Optional[ConceptResult]:
    for fn in (build_domain_concept_item, build_concept_item):
        built = fn(anchor, seed)
        if built:
            return built
    return None


def _apply_single(
    item: Dict[str, Any],
    stem: str,
    options: Dict[str, str],
    correct_letter: str,
    explanation: str = "",
) -> Dict[str, Any]:
    out = dict(item)
    out["tip"] = "unic"
    out["kind"] = "single"
    if "intrebare" in item:
        out["intrebare"] = stem
    if "text" in item:
        out["text"] = stem
    if "variante" in item:
        out["variante"] = options
    if "options" in item:
        out["options"] = options
    corr = [correct_letter.lower()]
    if "raspuns_corect" in item:
        out["raspuns_corect"] = corr
    if "correct" in item:
        out["correct"] = corr
    if explanation:
        out["explicatie"] = explanation
        out["explanation"] = explanation
    else:
        out["explicatie"] = ""
        out["explanation"] = ""
    return out


def rewrite_domain_belonging_item(
    item: Dict[str, Any],
    bank_index: Any = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Any = None,
) -> Tuple[Dict[str, Any], bool]:
    """Rescrie un item de tip «aparține domeniului» în întrebare conceptuală."""
    if not is_domain_belonging_item(item):
        return item, False

    seed = _item_seed(item)
    stem = _stem(item)
    domain = (
        domain_from_filter_stem(stem)
        or str(item.get("domeniu") or item.get("lot") or "").strip()
    )

    cluster_built = _rewrite_cluster_membership(item)
    if cluster_built:
        new_stem, new_opts, corr = cluster_built
        return _apply_single(item, new_stem, new_opts, corr), True

    anchors = _anchor_candidates(item)
    for anchor in anchors:
        built = _try_build_from_anchor(anchor, seed)
        if built:
            new_stem, new_opts, corr = built
            return _apply_single(item, new_stem, new_opts, corr), True

    if anchors:
        built = _pick_concept_item(
            anchors,
            domain,
            seed,
            label_index,
            bank_index,
            label_map or {},
        )
        if built:
            new_stem, new_opts, corr = built
            return _apply_single(item, new_stem, new_opts, corr), True

    return item, False


def rewrite_domain_belonging_bank(
    data: Dict[str, Any],
    bank_index: Any = None,
    label_map: Optional[Dict[str, str]] = None,
    label_index: Any = None,
) -> Tuple[Dict[str, Any], int, List[Dict[str, Any]]]:
    """Rescrie toți itemii problematici din bancă."""
    changes = 0
    log: List[Dict[str, Any]] = []
    for lot, item in walk_items(data):
        old_stem = _stem(item)
        if not is_domain_belonging_item(item):
            continue
        new_item, changed = rewrite_domain_belonging_item(
            item, bank_index, label_map, label_index
        )
        if changed:
            changes += 1
            log.append(
                {
                    "id": item_id(item),
                    "lot": lot,
                    "old_stem": old_stem,
                    "new_stem": _stem(new_item),
                    "new_correct": _correct(new_item),
                }
            )
            item.clear()
            item.update(new_item)
    return data, changes, log


def audit_domain_belonging(data: Dict[str, Any]) -> Dict[str, Any]:
    """Detectează itemi rămași cu formulări de apartenență la domeniu."""
    report: Dict[str, Any] = {
        "total_items": 0,
        "domain_belonging_count": 0,
        "by_pattern": Counter(),
        "items": [],
        "orphan_explanation_count": 0,
    }
    patterns = [
        ("apartin_domeniului", re.compile(r"aparțin domeniului", re.I)),
        ("apartin_explicit", re.compile(r"aparțin explicit", re.I)),
        ("tematica_examen", re.compile(r"tematica de examen", re.I)),
        ("in_aceasta_tematica", re.compile(r"în această tematică", re.I)),
        ("sunt_dimensiuni_big_five", re.compile(r"sunt dimensiuni Big Five", re.I)),
        ("sunt_scale_masurare", re.compile(r"sunt scale de măsurare", re.I)),
        ("genetica_comportamentala", re.compile(r"aparțin geneticii comportamentale", re.I)),
        ("epigenetica_programa", re.compile(r"epigenetică din programă", re.I)),
        ("relatie_terapeutica", re.compile(r"relației terapeutice", re.I)),
        ("cluster_personalitate", re.compile(r"tulburări aparțin Clusterului", re.I)),
        ("menționate_tematica", re.compile(r"menționate în tematică", re.I)),
    ]

    for lot, item in walk_items(data):
        report["total_items"] += 1
        stem = stem_text(item)
        expl = str(item.get("explanation") or item.get("explicatie") or "")

        if not is_domain_belonging_item(item) and not is_domain_belonging_stem(stem):
            if ORPHAN_DOMAIN_EXPLANATION in expl or ORPHAN_DOMAIN_EXPLANATION_ALT in expl:
                report["orphan_explanation_count"] += 1
            continue

        report["domain_belonging_count"] += 1
        matched = [name for name, pat in patterns if pat.search(stem)]
        for name in matched:
            report["by_pattern"][name] += 1
        if not matched:
            report["by_pattern"]["other_domain_belonging"] += 1

        report["items"].append(
            {
                "id": item_id(item),
                "lot": lot,
                "stem": stem,
                "correct": _correct(item),
                "patterns": matched or ["other"],
            }
        )
    return report


def format_domain_audit_report(
    report: Dict[str, Any],
    rewrite_log: Optional[List[Dict[str, Any]]] = None,
) -> str:
    lines = [
        "=" * 72,
        "AUDIT ITEMI «APARȚIN DOMENIULUI» / TEMATICĂ DE EXAMEN",
        "=" * 72,
        f"Total itemi în bancă: {report['total_items']}",
        f"Itemi problematici rămași: {report['domain_belonging_count']}",
        f"Explicații orphan rămase: {report.get('orphan_explanation_count', 0)}",
        "",
    ]
    if rewrite_log:
        lines.append(f"Itemi rescriși în această rulare: {len(rewrite_log)}")
        lines.append("")

    if report["by_pattern"]:
        lines.append("--- Distribuție pattern-uri (itemi rămași) ---")
        for name, count in report["by_pattern"].most_common():
            lines.append(f"  {name}: {count}")
        lines.append("")

    if report["items"]:
        lines.append("--- Itemi problematici (max 60) ---")
        for entry in report["items"][:60]:
            lines.append(f"  [{entry['id']}] ({entry['lot']})")
            lines.append(f"    {entry['stem'][:120]}")
            lines.append(f"    barem: {', '.join(entry['correct'])} | {entry['patterns']}")
        if len(report["items"]) > 60:
            lines.append(f"  ... și încă {len(report['items']) - 60}")
        lines.append("")

    if rewrite_log:
        lines.append("--- Exemple rescrieri (max 30) ---")
        for entry in rewrite_log[:30]:
            lines.append(f"  [{entry['id']}] {entry['lot']}")
            lines.append(f"    ÎNAINTE: {entry['old_stem'][:100]}")
            lines.append(f"    DUPĂ:    {entry['new_stem'][:100]}")
            lines.append(f"    barem: {', '.join(entry['new_correct'])}")
        if len(rewrite_log) > 30:
            lines.append(f"  ... și încă {len(rewrite_log) - 30}")
        lines.append("")

    if report["domain_belonging_count"] == 0:
        lines.append("OK — nu mai există itemi «aparțin domeniului» sau formulări echivalente.")
    else:
        lines.append("ATENȚIE — mai există itemi de rescris sau șters manual.")
    lines.append("=" * 72)
    return "\n".join(lines)


def main() -> None:
    app_dir = Path(__file__).resolve().parent.parent
    in_path = app_dir / "data" / "questions.json"
    out_json = app_dir / "questions_clean.json"
    out_txt = app_dir / "questions_clean.txt"
    out_audit = app_dir / "audit_report_domain_items.txt"

    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    apply_app = "--apply" in sys.argv
    if args:
        in_path = Path(args[0])

    if not in_path.exists():
        print(f"ERROR: {in_path} not found")
        sys.exit(1)

    from scripts.distractor_fix import build_index
    from scripts.label_definition_index import build_label_definition_index
    from scripts.rewrite_bank_natural import export_txt, process_bank
    from scripts.upgrade_tf_items import build_label_definition_map

    print(f"Încărcare: {in_path}")
    data = json.loads(in_path.read_text(encoding="utf-8"))

    pre = audit_domain_belonging(data)
    print(f"Itemi «aparțin domeniului» înainte: {pre['domain_belonging_count']}")

    rows = []
    for lot, lot_data in (data.get("lots") or {}).items():
        for q in lot_data.get("questions", []):
            row = dict(q)
            row["lot"] = lot
            row["domeniu"] = lot
            rows.append(row)
    index = build_index(rows)
    label_map = build_label_definition_map(rows)
    label_index = build_label_definition_index(rows)

    data, changes, log = rewrite_domain_belonging_bank(data, index, label_map, label_index)
    print(f"Rescriși direct: {changes}")

    print("Polish + rescriere conceptuală completă...")
    clean_data, polish_changes = process_bank(data)
    print(f"Modificări polish total: {polish_changes}")

    post = audit_domain_belonging(clean_data)
    audit_text = format_domain_audit_report(post, log)
    out_audit.write_text(audit_text, encoding="utf-8")
    print(f"Salvat: {out_audit}")

    clean_data["source_file"] = "questions_clean (fără itemi domeniu)"
    out_json.write_text(
        json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    out_txt.write_text(export_txt(clean_data), encoding="utf-8")
    print(f"Salvat: {out_json}")
    print(f"Salvat: {out_txt}")
    print()
    print(audit_text)

    if apply_app:
        app_path = app_dir / "data" / "questions.json"
        app_path.write_text(
            json.dumps(clean_data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Aplicat în aplicație: {app_path}")


if __name__ == "__main__":
    main()
