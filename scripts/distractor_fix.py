"""Îmbunătățire distractori: opțiuni omogene, plauzibile, din același registru."""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, DefaultDict, Dict, List, Optional, Sequence, Set, Tuple

from scripts.question_wording import CONCEPT_AUTHOR_LABEL_RE, EXAM_META_RE
from scripts.term_clusters import (
    build_definition_cluster_options,
    build_term_cluster_options,
    cluster_id_for_term,
    contextual_stem_for_cluster,
    definitions_for_cluster,
    replace_heterogeneous_options,
    terms_for_cluster,
)

DOMAIN_STEM_RE = re.compile(
    r"^Care dintre următoarele aparțin domeniului «(.+?)»\?\s*$",
    re.IGNORECASE,
)

AUTHOR_NAME_RE = re.compile(
    r"^[A-ZĂÂÎȘȚ]\.\s*(?:[A-ZĂÂÎȘȚ]\.\s*)?"
    r"[A-ZĂÂÎȘȚÀ-Ž][a-zăâîșțà-ž\-]+"
    r"(?:\s+în\s+.+)?$"
)

AUTHOR_DESC_RE = re.compile(r"^(Autor|Autoare)\s+(asociat|asociată)", re.IGNORECASE)

REVERSE_DESC_RE = re.compile(r"^«(.+?)» descrie(?: mai ales)?:\s*$", re.IGNORECASE)
CONCEPT_MATCH_DESC_RE = re.compile(
    r"^Care concept corespunde descrierii:\s*(.+?)\?\s*$", re.IGNORECASE | re.DOTALL
)
REFER_CEL_MAI_BINE_RE = re.compile(
    r"^(.+?)\s+se referă cel mai bine la:\s*$", re.IGNORECASE
)
AUTHOR_IN_OPTION_RE = re.compile(
    r"^[A-ZĂÂÎȘȚ][^.]+ — .+$|^(Autor|Autoare)\s", re.IGNORECASE
)
AUTHOR_OPTION_RE = re.compile(
    r"^[A-ZĂÂÎȘȚ][A-Za-zĂÂÎȘȚăâîșț.\s\-]+ — .+$"
)

DEFINITION_START_RE = re.compile(
    r"^(variabila|setul|procedura|proces|tip |categorie|tulburare|măsura|indicator|"
    r"ipoteza|analiza|scala|statistica|comportament|relația|gradul|posibilitatea|"
    r"influența|adăugarea|proporția|subgrupul|grupul|valoarea|eroarea|nivelul|"
    r"autor asociat|autoare asociată|perspectivă|abordare|stare|episod|pattern)",
    re.IGNORECASE,
)

FORM_DEFINITION = "definition"
FORM_AUTHOR = "author"
FORM_TERM = "term"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def classify_option_form(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return FORM_TERM
    if AUTHOR_DESC_RE.match(t):
        return FORM_DEFINITION
    if AUTHOR_OPTION_RE.match(t) or AUTHOR_IN_OPTION_RE.match(t):
        return FORM_AUTHOR
    if AUTHOR_NAME_RE.match(t):
        return FORM_AUTHOR
    if t[0].islower() or len(t) > 58 or DEFINITION_START_RE.match(t):
        return FORM_DEFINITION
    words = t.split()
    if len(words) <= 7 and not t.endswith("."):
        return FORM_TERM
    return FORM_DEFINITION


def item_stem_kind(text: str) -> str:
    t = (text or "").strip()
    if DOMAIN_STEM_RE.match(t):
        return "domain"
    if CONCEPT_AUTHOR_LABEL_RE.match(t) or EXAM_META_RE.match(t):
        return "definition_match"
    if "care variantă descrie cel mai bine" in t.lower():
        return "definition_match"
    if "care concept este descris" in t.lower() or "ce concept corespunde" in t.lower():
        return "definition_match"
    if "formulare este cea mai potrivită" in t.lower():
        return "definition_match"
    if REVERSE_DESC_RE.match(t) or CONCEPT_MATCH_DESC_RE.match(t):
        return "reverse_desc"
    if REFER_CEL_MAI_BINE_RE.match(t):
        return "refer_cel_mai_bine"
    return "other"


def _domain_from_stem(text: str) -> Optional[str]:
    m = DOMAIN_STEM_RE.match((text or "").strip())
    return m.group(1).strip() if m else None


def _item_seed(item: Dict[str, Any]) -> int:
    raw = f"{item.get('id', item.get('id_local', ''))}|{item.get('intrebare', item.get('text', ''))}"
    return int(hashlib.md5(raw.encode()).hexdigest()[:8], 16)


def _pick(pool: List[str], used: Set[str], seed: int, offset: int = 0) -> Optional[str]:
    if not pool:
        return None
    available = [x for x in pool if norm(x) not in used]
    if not available:
        available = list(pool)
    idx = (seed + offset) % len(available)
    return available[idx]


@dataclass
class BankIndex:
    definitions_by_domain: DefaultDict[str, List[str]] = field(
        default_factory=lambda: defaultdict(list)
    )
    terms_by_domain: DefaultDict[str, List[str]] = field(
        default_factory=lambda: defaultdict(list)
    )
    authors_by_domain: DefaultDict[str, List[str]] = field(
        default_factory=lambda: defaultdict(list)
    )
    term_domains: DefaultDict[str, Set[str]] = field(default_factory=lambda: defaultdict(set))
    def_domains: DefaultDict[str, Set[str]] = field(default_factory=lambda: defaultdict(set))
    definitions_other: List[str] = field(default_factory=list)
    terms_other: List[str] = field(default_factory=list)
    authors_other: List[str] = field(default_factory=list)
    _seen_def: Set[str] = field(default_factory=set)
    _seen_term: Set[str] = field(default_factory=set)
    _seen_author: Set[str] = field(default_factory=set)

    def add_option(self, domain: str, text: str) -> None:
        t = (text or "").strip()
        if not t:
            return
        form = classify_option_form(t)
        key = norm(t)
        d = domain or "General"

        if form == FORM_AUTHOR:
            self.term_domains[key].add(d)
            if key not in self._seen_author:
                self._seen_author.add(key)
                self.authors_by_domain[d].append(t)
                self.authors_other.append(t)
        elif form == FORM_DEFINITION:
            self.def_domains[key].add(d)
            if key not in self._seen_def:
                self._seen_def.add(key)
                self.definitions_by_domain[d].append(t)
                self.definitions_other.append(t)
        else:
            self.term_domains[key].add(d)
            if key not in self._seen_term:
                self._seen_term.add(key)
                self.terms_by_domain[d].append(t)
                self.terms_other.append(t)

    def distractor_pool(
        self, form: str, domain: str, exclude_domain: bool = True
    ) -> List[str]:
        if form == FORM_AUTHOR:
            if exclude_domain:
                own = {norm(x) for x in self.authors_by_domain.get(domain, [])}
                return [x for x in self.authors_other if norm(x) not in own]
            return list(self.authors_other)
        if form == FORM_DEFINITION:
            if exclude_domain:
                own = {norm(x) for x in self.definitions_by_domain.get(domain, [])}
                return [x for x in self.definitions_other if norm(x) not in own]
            return list(self.definitions_other)
        if exclude_domain:
            own = {norm(x) for x in self.terms_by_domain.get(domain, [])}
            return [x for x in self.terms_other if norm(x) not in own]
        return list(self.terms_other)


def build_index(items: Sequence[Dict[str, Any]]) -> BankIndex:
    idx = BankIndex()
    for item in items:
        domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
        options = item.get("variante") or item.get("options") or {}
        for v in options.values():
            idx.add_option(domain, str(v))
    return idx


def _target_form_for_domain_item(
    options: Dict[str, str], correct: Sequence[str]
) -> str:
    correct_forms = [classify_option_form(options[c]) for c in correct if c in options]
    if not correct_forms:
        return FORM_TERM
    if all(f == FORM_AUTHOR for f in correct_forms):
        return FORM_AUTHOR
    if all(f == FORM_DEFINITION for f in correct_forms):
        return FORM_DEFINITION
    # Autor + concept/teorie în același item → etichete scurte omogene
    return FORM_TERM


def _term_belongs_to_domain(term: str, domain: str, index: BankIndex) -> bool:
    domains = index.term_domains.get(norm(term), set())
    return domain in domains if domains else False


def _needs_domain_distractor_replacement(
    opt: str, domain: str, index: BankIndex, target_form: str
) -> bool:
    form = classify_option_form(opt)
    if form != target_form:
        return True
    if target_form == FORM_AUTHOR:
        return not _term_belongs_to_domain(opt, domain, index)
    if target_form == FORM_TERM:
        return not _term_belongs_to_domain(opt, domain, index)
    return form != FORM_DEFINITION


def _reformulate_domain_stem(domain: str, target_form: str, correct_forms: Set[str]) -> str:
    if target_form == FORM_AUTHOR or (
        correct_forms == {FORM_AUTHOR}
    ):
        return (
            f"Care dintre următorii autori sunt asociați domeniului «{domain}»?"
        )
    if target_form == FORM_DEFINITION:
        return (
            f"Care dintre următoarele formulări descriu concepte din domeniul «{domain}»?"
        )
    return f"Care dintre următoarele concepte sau teme aparțin domeniului «{domain}»?"


def fix_domain_item(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    """Itemii de domeniu sunt reformulați în reformulate_domain.py — nu dublăm aici."""
    return item, False


def options_have_duplicates(options: Dict[str, str]) -> bool:
    texts = [norm(v) for v in options.values() if (v or "").strip()]
    return len(texts) != len(set(texts))


def _author_item_needs_fix(
    options: Dict[str, str], correct: Sequence[str], correct_author: str
) -> bool:
    if options_have_duplicates(options):
        return True
    forms = {classify_option_form(options.get(c, "")) for c in correct if c in options}
    if forms != {FORM_AUTHOR}:
        return True
    if any(classify_option_form(v) != FORM_AUTHOR for v in options.values()):
        return True
    cluster = None
    from scripts.author_knowledge import cluster_for_author, format_author_option

    cluster = cluster_for_author(correct_author)
    if not cluster:
        return True
    expected = format_author_option(correct_author)
    if expected and not any(norm(v) == norm(expected) for v in options.values()):
        return True
    return False


def fix_author_item(item: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """Reconstruiește itemii cu enunț de autor — 4 contribuții omogene, fără duplicate."""
    from scripts.author_knowledge import (
        build_cluster_options,
        cluster_for_author,
        lookup_author_by_stem,
        match_author,
        natural_stem_for_author,
    )

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not stem or not options or not correct:
        return item, False

    correct_author: Optional[str] = None
    for letter in correct:
        if letter in options:
            correct_author = match_author(str(options[letter]))
            if correct_author:
                break
    stem_author = lookup_author_by_stem(stem)
    author = correct_author or stem_author
    if not author:
        return item, False
    if stem_author and correct_author and stem_author != correct_author:
        author = correct_author

    if not _author_item_needs_fix(options, correct, author):
        return item, False

    cluster = cluster_for_author(author)
    if not cluster:
        return item, False

    seed = _item_seed(item)
    built = build_cluster_options(cluster, author, seed)
    if not built:
        return item, False

    new_options, correct_letter = built
    new_stem = natural_stem_for_author(author) or stem
    out = _apply_option_fix(item, new_options, [correct_letter], new_stem)
    out["tip"] = "unic"
    out["kind"] = "single"
    return out, True


def _is_bad_distractor(opt: str, target_form: str, pool_norms: Set[str]) -> bool:
    if AUTHOR_IN_OPTION_RE.match((opt or "").strip()):
        return True
    form = classify_option_form(opt)
    if target_form == FORM_TERM and form != FORM_TERM:
        return True
    if target_form == FORM_DEFINITION and form == FORM_AUTHOR:
        return True
    if pool_norms and norm(opt) not in pool_norms:
        return True
    return False


def _domain_pool(index: BankIndex, domain: str, form: str) -> List[str]:
    if form == FORM_DEFINITION:
        return list(index.definitions_by_domain.get(domain, [])) or list(
            index.definitions_other
        )
    return list(index.terms_by_domain.get(domain, [])) or list(index.terms_other)


def _apply_option_fix(
    item: Dict[str, Any],
    new_options: Dict[str, str],
    new_correct: List[str],
    new_stem: Optional[str] = None,
) -> Dict[str, Any]:
    out = dict(item)
    if new_stem and str(new_stem).strip():
        if "intrebare" in item:
            out["intrebare"] = str(new_stem).strip()
        if "text" in item:
            out["text"] = str(new_stem).strip()
    if "variante" in item:
        out["variante"] = new_options
    if "options" in item:
        out["options"] = new_options
    if "raspuns_corect" in item:
        out["raspuns_corect"] = new_correct
    if "correct" in item:
        out["correct"] = new_correct
    return out


def fix_reverse_desc_item(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    """Descriere → concept: enunț direct, fără ghilimele « »."""
    from scripts.stem_naturalize import flip_reverse_desc_to_forward

    flipped, changed = flip_reverse_desc_to_forward(item, index)
    if changed:
        return flipped, True

    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    m = REVERSE_DESC_RE.match(stem)
    desc: Optional[str] = None
    if m:
        desc = m.group(1).strip()
    else:
        m2 = CONCEPT_MATCH_DESC_RE.match(stem)
        if m2:
            desc = m2.group(1).strip()
    if not desc:
        return item, False

    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not options or not correct:
        return item, False
    explanation = str(item.get("explicatie") or item.get("explanation") or "")
    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    seed = _item_seed(item)

    correct_labels = [str(options[c]).strip() for c in correct if c in options]
    if not correct_labels:
        return item, False

    primary = correct_labels[0]
    target_form = classify_option_form(primary)
    cluster_id = cluster_id_for_term(primary, explanation, desc)

    # Mod definiții: «Varietatea aptitudinilor» descrie → răspunsuri tip definiție
    if target_form == FORM_DEFINITION or (
        cluster_id and definitions_for_cluster(cluster_id)
        and all(classify_option_form(o) != FORM_TERM for o in correct_labels)
    ):
        pool = definitions_for_cluster(cluster_id) if cluster_id else []
        if len(pool) < 4:
            pool = _domain_pool(index, domain, FORM_DEFINITION)
        pool_norms = {norm(p) for p in pool}
        if any(
            _is_bad_distractor(options[l], target_form, pool_norms)
            for l in options
            if l not in correct
        ):
            if len(correct) == 1 and len(pool) >= 4:
                built = build_definition_cluster_options(pool, primary, seed)
                if built:
                    new_options, new_corr = built
                    new_stem = contextual_stem_for_cluster(cluster_id or "", desc) or stem
                    return (
                        _apply_option_fix(item, new_options, [new_corr], new_stem),
                        True,
                    )
            new_options, new_correct, changed = replace_heterogeneous_options(
                options, correct, pool, seed
            )
            if changed:
                return _apply_option_fix(item, new_options, new_correct), True
        return item, False

    # Mod termeni: descriere → etichetă scurtă
    pool = terms_for_cluster(cluster_id) if cluster_id else []
    if len(pool) < 4:
        pool = _domain_pool(index, domain, FORM_TERM)
    pool_norms = {norm(p) for p in pool} if pool else set()

    needs_fix = any(
        _is_bad_distractor(options[l], FORM_TERM, pool_norms)
        for l in options
        if l not in correct
    )
    if not needs_fix:
        return item, False

    if len(correct) == 1 and len(pool) >= 4 and cluster_id:
        built = build_term_cluster_options(pool, primary, seed)
        if built:
            new_options, new_corr = built
            new_stem = contextual_stem_for_cluster(cluster_id, desc) or stem
            return _apply_option_fix(item, new_options, [new_corr], new_stem), True

    new_options, new_correct, changed = replace_heterogeneous_options(
        options, correct, pool, seed
    )
    if not changed:
        return item, False
    new_stem = contextual_stem_for_cluster(cluster_id or "", desc) if cluster_id else None
    return _apply_option_fix(item, new_options, new_correct, new_stem), True


def fix_refer_cel_mai_bine_item(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    """«Concept» se referă cel mai bine la: — definiții din același domeniu."""
    stem = str(item.get("intrebare") or item.get("text") or "").strip()
    m = REFER_CEL_MAI_BINE_RE.match(stem)
    if not m:
        return item, False

    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not options or not correct:
        return item, False

    label = m.group(1).strip().strip("«»")
    explanation = str(item.get("explicatie") or item.get("explanation") or "")
    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    seed = _item_seed(item)

    correct_labels = [str(options[c]).strip() for c in correct if c in options]
    if not correct_labels:
        return item, False

    cluster_id = cluster_id_for_term(label, explanation, label)
    pool = definitions_for_cluster(cluster_id) if cluster_id else []
    if len(pool) < 4:
        pool = _domain_pool(index, domain, FORM_DEFINITION)

    pool_norms = {norm(p) for p in pool}
    needs_fix = any(
        _is_bad_distractor(options[l], FORM_DEFINITION, pool_norms)
        for l in options
        if l not in correct
    )
    if not needs_fix:
        return item, False

    if len(correct) == 1 and len(pool) >= 4:
        built = build_definition_cluster_options(pool, correct_labels[0], seed)
        if built:
            new_options, new_corr = built
            return _apply_option_fix(item, new_options, [new_corr]), True

    new_options, new_correct, changed = replace_heterogeneous_options(
        options, correct, pool, seed
    )
    if changed:
        return _apply_option_fix(item, new_options, new_correct), True
    return item, False


def fix_heterogeneous_item(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    """Ultimă plasă: înlocuiește distractori de alt registru (autor/definiție/termen)."""
    stem_low = str(item.get("intrebare") or item.get("text") or "").lower()
    if re.search(
        r"poligenic|eritabilit|epigenet|gemen|modelul ace|model eredit|gwas|metilare adn",
        stem_low,
    ):
        return item, False

    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    if not options or not correct:
        return item, False

    correct_forms = [
        classify_option_form(str(options[c])) for c in correct if c in options
    ]
    if not correct_forms or len(set(correct_forms)) != 1:
        return item, False
    target = correct_forms[0]
    if target == FORM_AUTHOR:
        return item, False

    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    seed = _item_seed(item)
    pool = _domain_pool(index, domain, target)
    pool_norms = {norm(p) for p in pool}

    needs_fix = any(
        _is_bad_distractor(options[l], target, pool_norms)
        for l in options
        if l not in correct
    )
    if not needs_fix:
        return item, False

    new_options, new_correct, changed = replace_heterogeneous_options(
        options, correct, pool, seed
    )
    if changed:
        return _apply_option_fix(item, new_options, new_correct), True
    return item, False


def fix_definition_item(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    options: Dict[str, str] = dict(item.get("variante") or item.get("options") or {})
    correct = [str(c).lower() for c in (item.get("raspuns_corect") or item.get("correct") or [])]
    domain = str(item.get("domeniu") or item.get("lot") or "General").strip()
    if not options or not correct:
        return item, False

    seed = _item_seed(item)
    used = {norm(options[c]) for c in correct if c in options}
    changed = False
    new_options = dict(options)

    # Prefer distractors from same domain, then other domains
    same_domain = index.definitions_by_domain.get(domain, [])
    other_domain = index.distractor_pool(FORM_DEFINITION, domain)

    item_domain = domain

    for letter, opt in options.items():
        if letter in correct:
            continue
        form = classify_option_form(opt)
        in_domain = item_domain in index.def_domains.get(norm(opt), set())
        if form == FORM_DEFINITION and in_domain:
            continue
        pool = [x for x in same_domain if norm(x) not in used] or same_domain
        if not pool:
            pool = [x for x in other_domain if norm(x) not in used] or other_domain
        replacement = _pick(pool, used, seed, ord(letter))
        if not replacement:
            replacement = _pick(other_domain, used, seed, ord(letter) + 7)
        if replacement and norm(replacement) != norm(opt):
            new_options[letter] = replacement
            used.add(norm(replacement))
            changed = True

    if not changed:
        return item, False

    out = dict(item)
    if "variante" in item:
        out["variante"] = new_options
    if "options" in item:
        out["options"] = new_options
    return out, True


def fix_item_distractors(
    item: Dict[str, Any], index: BankIndex
) -> Tuple[Dict[str, Any], bool]:
    from scripts.fix_tf_items import is_tf_item
    from scripts.fix_malformed_flashcard import (
        fix_malformed_flashcard_item,
        is_malformed_flashcard_item,
    )

    if is_tf_item(item):
        return item, False

    if is_malformed_flashcard_item(item):
        fixed, changed = fix_malformed_flashcard_item(item)
        if changed:
            return fixed, True

    from scripts.stem_naturalize import flip_reverse_desc_to_forward

    flipped, flipped_changed = flip_reverse_desc_to_forward(item, index)
    if flipped_changed:
        item = flipped

    fixed, changed = fix_author_item(item)
    if changed:
        item = fixed

    options = dict(item.get("variante") or item.get("options") or {})
    if options_have_duplicates(options):
        fixed, changed = fix_author_item(item)
        if changed:
            return fixed, True

    text = str(item.get("intrebare") or item.get("text") or "")
    kind = item_stem_kind(text)
    if kind == "domain":
        return fix_domain_item(item, index)
    if kind == "definition_match":
        return fix_definition_item(item, index)
    if kind == "reverse_desc":
        return fix_reverse_desc_item(item, index)
    if kind == "refer_cel_mai_bine":
        return fix_refer_cel_mai_bine_item(item, index)
    fixed, changed = fix_heterogeneous_item(item, index)
    if changed:
        item = fixed

    from scripts.item_quality import fix_item_quality

    fixed, changed = fix_item_quality(item, index)
    if changed:
        return fixed, True
    return item, False


def fix_items_batch(items: List[Dict[str, Any]], passes: int = 3) -> Tuple[List[Dict[str, Any]], int]:
    """Două treceri — a doua prinde itemi îmbunătățiți parțial de prima."""
    out = list(items)
    fixed_count = 0
    for _ in range(max(1, passes)):
        index = build_index(out)
        next_out: List[Dict[str, Any]] = []
        pass_count = 0
        for item in out:
            fixed, changed = fix_item_distractors(item, index)
            if changed:
                pass_count += 1
            next_out.append(fixed)
        out = next_out
        fixed_count += pass_count
    return out, fixed_count


def polish_item_options(item: Dict[str, Any], index: Optional[BankIndex] = None) -> Dict[str, Any]:
    """Pentru apel din app — necesită index pre-construit sau returnează itemul nemodificat."""
    if index is None:
        return item
    fixed, _ = fix_item_distractors(item, index)
    return fixed
