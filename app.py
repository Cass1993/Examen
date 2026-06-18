from __future__ import annotations

import json
import os
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

IS_CLOUD = os.environ.get("STREAMLIT_RUNTIME_ENV") == "cloud"
DATA_DIR = APP_DIR / "data"
BANK_1400 = APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json"
BANK_2000 = APP_DIR / "2000 itemi raw" / "questions_2000_all.json"
MERGED_JSON = APP_DIR / "questions_3400_merged.json"
MERGE_REPORT = APP_DIR / "2000 itemi raw" / "raport_validare_merge_3400.txt"
MERGE_RESEARCH = APP_DIR / "2000 itemi raw" / "raport_cercetare_metodologica_2000.txt"
BANK_MD_DEFAULT = MERGED_JSON
QUESTIONS_JSON = DATA_DIR / "questions.json"
HISTORY_JSON = DATA_DIR / "scores_history.json"


def _has_scripts() -> bool:
    return (APP_DIR / "scripts" / "bank_parser.py").exists()


def _merge_banks(*args: Any, **kwargs: Any) -> Any:
    from scripts.bank_merge import merge_banks

    return merge_banks(*args, **kwargs)


def _write_questions_json(*args: Any, **kwargs: Any) -> Any:
    from scripts.bank_parser import write_questions_json

    return write_questions_json(*args, **kwargs)


def _build_polish_context(rows: List[Dict[str, Any]]) -> Tuple[Any, Dict[str, str], Any]:
    from scripts.distractor_fix import build_index
    from scripts.label_definition_index import build_label_definition_index
    from scripts.upgrade_tf_items import build_label_definition_map

    return (
        build_index(rows),
        build_label_definition_map(rows),
        build_label_definition_index(rows),
    )


@dataclass(frozen=True)
class Q:
    id: int
    text: str
    options: Dict[str, str]
    kind: str  # single|multi|unknown
    correct: List[str]
    lot: str
    explanation: str = ""


def _load_questions() -> Dict[str, Any]:
    if QUESTIONS_JSON.exists():
        return json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    return {"lots": {}}


def _ensure_merged_bank() -> Path:
    """Combină 1400 + 2000 cu validare; regenerează dacă sursele sunt mai noi."""
    if not BANK_1400.exists() or not BANK_2000.exists():
        return BANK_1400 if BANK_1400.exists() else bank_path_fallback()

    needs_merge = not MERGED_JSON.exists()
    if MERGED_JSON.exists():
        merged_mtime = MERGED_JSON.stat().st_mtime
        needs_merge = (
            BANK_1400.stat().st_mtime > merged_mtime
            or BANK_2000.stat().st_mtime > merged_mtime
        )
    if needs_merge:
        _merge_banks(BANK_1400, BANK_2000, MERGED_JSON, MERGE_REPORT, MERGE_RESEARCH)
    return MERGED_JSON


def bank_path_fallback() -> Path:
    if MERGED_JSON.exists():
        return MERGED_JSON
    if BANK_1400.exists():
        return BANK_1400
    return BANK_MD_DEFAULT


WORDING_VERSION = "130"  # fix explicație Self-Transcendence Schwartz + aliniere


def _questions_cache_key() -> str:
    """Cheie cache — se invalidează când se schimbă fișierele băncii."""
    parts: List[str] = [WORDING_VERSION]
    for path in (MERGED_JSON, BANK_1400, BANK_2000, QUESTIONS_JSON):
        if path.exists():
            parts.append(f"{path}:{path.stat().st_mtime_ns}")
    io_items = APP_DIR / "scripts" / "i_o_exam_items.py"
    if io_items.exists():
        parts.append(f"io_exam:{io_items.stat().st_mtime_ns}")
    for supplemental_path in (
        APP_DIR / "scripts" / "epigenetica_exam_items.py",
        APP_DIR / "scripts" / "epigenetica_bank_data.py",
        APP_DIR / "data" / "epigenetica_items.json",
        APP_DIR / "scripts" / "psihoterapie_ii_exam_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_bank_data.py",
        APP_DIR / "scripts" / "psihoterapie_ii_tricky_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_psihodinamic_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_aparare_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_stem_quality.py",
        APP_DIR / "scripts" / "psihoterapie_ii_stem_standalone.py",
        APP_DIR / "scripts" / "psihoterapie_ii_author_labels.py",
        APP_DIR / "scripts" / "psihoterapie_ii_behaviorism_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_behavioral_techniques_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_cbt_ellis_beck_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_lazarus_multimodal_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_glasser_reality_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_family_therapy_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_psychodrama_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_psychodrama_extra_items.py",
        APP_DIR / "scripts" / "psihoterapie_ii_mitrofan_unificare_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_exam_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_bank_data.py",
        APP_DIR / "scripts" / "psihopatologie_ii_bipolar_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_ptsd_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_suicid_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_toc_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_anxietate_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_personalitate_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_personalitate_extra_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_schizofrenie_depresie_items.py",
        APP_DIR / "scripts" / "psihopatologie_ii_schizofrenie_depresie_extra_items.py",
        APP_DIR / "scripts" / "evaluare_psihologica_ii_exam_items.py",
        APP_DIR / "scripts" / "evaluare_psihologica_ii_bank_data.py",
        APP_DIR / "scripts" / "evaluare_psihologica_ii_option_polish.py",
        APP_DIR / "scripts" / "evaluare_psihologica_ii_explanations.py",
        APP_DIR / "scripts" / "inteligenta_istoric_modele_bank_data.py",
        APP_DIR / "scripts" / "inteligenta_istoric_modele_explanations.py",
        APP_DIR / "scripts" / "inteligenta_emotionala_bank_data.py",
        APP_DIR / "scripts" / "inteligenta_emotionala_explanations.py",
        APP_DIR / "scripts" / "motivatie_bank_data.py",
        APP_DIR / "scripts" / "motivatie_explanations.py",
        APP_DIR / "scripts" / "interese_bank_data.py",
        APP_DIR / "scripts" / "interese_explanations.py",
        APP_DIR / "scripts" / "jvis_bank_data.py",
        APP_DIR / "scripts" / "jvis_explanations.py",
        APP_DIR / "scripts" / "psihologia_muncii_ii_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_selectie_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_performanta_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_fluctuatie_satisfactie_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_value_fit_stres_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_epp_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_capcane_grile_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_design_munca_bank_data.py",
        APP_DIR / "scripts" / "psihologia_muncii_ii_explanations.py",
        APP_DIR / "scripts" / "exam_ii_plausible_distractors.py",
        APP_DIR / "scripts" / "psihologia_muncii_ii_exam_items.py",
        APP_DIR / "scripts" / "perspectiva_psihometrica_bank_data.py",
        APP_DIR / "scripts" / "psihopatologie_ii_option_polish.py",
        APP_DIR / "scripts" / "psihoterapie_ii_option_polish.py",
        APP_DIR / "scripts" / "psihoterapie_ii_acronym_expand.py",
        APP_DIR / "scripts" / "psihoterapie_etica_exam_items.py",
        APP_DIR / "scripts" / "psihoterapie_etica_bank_data.py",
        APP_DIR / "scripts" / "psihoterapie_etica_extra_items.py",
        APP_DIR / "scripts" / "psihoterapie_etica_option_polish.py",
    ):
        if supplemental_path.exists():
            parts.append(
                f"supplemental:{supplemental_path}:{supplemental_path.stat().st_mtime_ns}"
            )
    return "|".join(parts) or "empty"


def _ensure_supplemental_lots(data: Dict[str, Any]) -> Dict[str, Any]:
    """Injectează loturi examen suplimentare și le persistă în questions.json."""
    from scripts.supplemental_lots import ensure_all_supplemental_lots

    return ensure_all_supplemental_lots(data, QUESTIONS_JSON)


def _ensure_questions_generated(bank_path: Path) -> Dict[str, Any]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if QUESTIONS_JSON.exists() and (IS_CLOUD or not _has_scripts()):
        data = _load_questions()
        if data.get("lots") and _has_scripts():
            return _ensure_supplemental_lots(data)
        return data

    if BANK_1400.exists() and BANK_2000.exists():
        bank_path = _ensure_merged_bank()

    needs_regen = not QUESTIONS_JSON.exists()
    if QUESTIONS_JSON.exists() and bank_path.exists():
        needs_regen = bank_path.stat().st_mtime > QUESTIONS_JSON.stat().st_mtime

    if needs_regen:
        if not bank_path.exists():
            raise FileNotFoundError(
                f"Nu există {QUESTIONS_JSON.name} și nici banca sursă ({bank_path.name}). "
                "Pentru Streamlit Cloud, include în repo fișierul data/questions.json "
                "(rulează scripts/prepare_streamlit_deploy.py înainte de push)."
            )
        _write_questions_json(bank_path, QUESTIONS_JSON)

    if QUESTIONS_JSON.exists() and _has_scripts():
        from scripts.apply_all_bank_fixes import ensure_bank_fixed

        ensure_bank_fixed(QUESTIONS_JSON, DATA_DIR)
    data = _load_questions()
    if _has_scripts():
        return _ensure_supplemental_lots(data)
    return data


@st.cache_data(show_spinner="Se încarcă banca de întrebări…")
def _load_question_bank(_cache_key: str) -> Dict[str, Any]:
    return _ensure_questions_generated(MERGED_JSON if MERGED_JSON.exists() else BANK_1400)


@st.cache_data(show_spinner=False)
def _get_polish_context(_cache_key: str) -> Tuple[Any, Dict[str, str], Any]:
    db = _load_question_bank(_cache_key)
    rows: List[Dict[str, Any]] = []
    for lot_name, lot_data in (db or {}).get("lots", {}).items():
        for q in lot_data.get("questions", []):
            rows.append(
                {
                    "id": q.get("id"),
                    "text": q.get("text"),
                    "options": q.get("options"),
                    "correct": q.get("correct"),
                    "domeniu": lot_name,
                }
            )
    if not rows or not _has_scripts():
        return ({}, {}, {})
    return _build_polish_context(rows)


@st.cache_data(show_spinner=False)
def _get_all_questions(_cache_key: str) -> List[Q]:
    db = _load_question_bank(_cache_key)
    index, label_map, label_index = _get_polish_context(_cache_key)
    return _flatten_questions(db, index, label_map, label_index)


def _exam_explanation(text: str) -> str:
    """Explicații examen — doar extindere abrevieri, fără reformulare enunț."""
    if not _has_scripts():
        return (text or "").strip()
    from scripts.abbreviations import expand_abbreviations

    return expand_abbreviations((text or "").strip())


def _polish_expl_text(text: str) -> str:
    from scripts.polish_text import polish_text

    return polish_text(text)


def _resolve_explanation(qid: int, lot: str, explanation: str) -> str:
    expl = (explanation or "").strip()
    if expl or not _has_scripts():
        return expl
    if 9001 <= int(qid) <= 9360:
        from scripts.evaluare_psihologica_ii_explanations import explanation_for_exam_id

        return explanation_for_exam_id(int(qid))
    if 9501 <= int(qid) <= 9970:
        from scripts.psihologia_muncii_ii_explanations import explanation_for_exam_id

        return explanation_for_exam_id(int(qid))
    return ""


def _flatten_questions(
    db: Dict[str, Any],
    index: Any,
    label_map: Dict[str, str],
    label_index: Any,
) -> List[Q]:
    out: List[Q] = []
    lots = (db or {}).get("lots", {})
    for lot_name, lot_data in lots.items():
        for q in lot_data.get("questions", []):
            raw: Dict[str, Any] = {
                "id": q.get("id"),
                "text": str(q.get("text") or ""),
                "options": {
                    str(k).lower(): str(v)
                    for k, v in (q.get("options") or {}).items()
                },
                "correct": [str(x).lower() for x in (q.get("correct") or [])],
                "kind": q.get("kind"),
                "explanation": q.get("explanation"),
                "domeniu": lot_name,
                "exam_item": bool(q.get("exam_item")),
            }
            if raw["exam_item"] and "Psihoterapie II" in lot_name and _has_scripts():
                from scripts.psihoterapie_ii_author_labels import polish_exam_display_item

                fixed = polish_exam_display_item(raw)
            elif raw["exam_item"] or not index:
                fixed = raw
            else:
                from scripts.polish_text import polish_question_item

                fixed = polish_question_item(raw, index, label_map, label_index)
            fixed_kind = str(fixed.get("kind") or fixed.get("tip") or q.get("kind") or "unknown")
            qid = int(q["id"])
            fixed_expl = _resolve_explanation(
                qid,
                str(lot_name),
                str(
                    fixed.get("explanation")
                    or fixed.get("explicatie")
                    or q.get("explanation")
                    or ""
                ),
            )
            stem = str(
                fixed.get("text")
                or fixed.get("intrebare")
                or raw.get("text")
                or ""
            ).strip()
            out.append(
                Q(
                    id=qid,
                    text=stem,
                    options={
                        str(k).lower(): str(v)
                        for k, v in (fixed.get("options") or {}).items()
                    },
                    kind=fixed_kind,
                    correct=[
                        str(x).lower()
                        for x in (fixed.get("correct") or raw["correct"])
                    ],
                    lot=str(lot_name),
                    explanation=(
                        _exam_explanation(fixed_expl)
                        if raw["exam_item"]
                        else (
                            _polish_expl_text(fixed_expl)
                            if _has_scripts()
                            else fixed_expl
                        )
                    ),
                )
            )
    out.sort(key=lambda x: (x.lot, x.id))
    return out


def _score_single(selected: Sequence[str], correct: Sequence[str]) -> float:
    if not correct:
        return 0.0
    sel = [s.lower() for s in selected if s]
    # allow selecting multiple, but it's wrong for single-choice items
    if len(sel) != 1:
        return 0.0
    return 1.0 if sel[0] == correct[0].lower() else 0.0


def _score_multi(selected: Sequence[str], correct: Sequence[str]) -> float:
    """
    Partial scoring:
      points = max(0, (|A∩C| - |A\\C|) / |C| ), clamped [0,1]
    """
    C: Set[str] = {c.lower() for c in correct if c}
    if not C:
        return 0.0
    A: Set[str] = {a.lower() for a in selected if a}
    num = len(A & C) - len(A - C)
    pts = num / max(1, len(C))
    if pts < 0:
        pts = 0.0
    if pts > 1:
        pts = 1.0
    return float(pts)


def _ensure_history() -> List[Dict[str, Any]]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not HISTORY_JSON.exists():
        HISTORY_JSON.write_text("[]", encoding="utf-8")
        return []
    try:
        return json.loads(HISTORY_JSON.read_text(encoding="utf-8"))
    except Exception:
        return []


def _append_history(entry: Dict[str, Any]) -> None:
    hist = _ensure_history()
    hist.append(entry)
    HISTORY_JSON.write_text(json.dumps(hist, ensure_ascii=False, indent=2), encoding="utf-8")


def _format_seconds(s: float) -> str:
    s = max(0, int(s))
    mm = s // 60
    ss = s % 60
    return f"{mm:02d}:{ss:02d}"


def _letters_to_text(letters: Sequence[str], options: Dict[str, str]) -> str:
    if not letters:
        return "(niciun răspuns)"
    parts = []
    for letter in sorted({str(x).lower() for x in letters}):
        text = options.get(letter, "")
        parts.append(f"**{letter})** {text}" if text else f"**{letter})**")
    return "; ".join(parts)


def _is_fully_correct(item: Dict[str, Any]) -> bool:
    return float(item.get("points") or 0.0) >= 1.0


def _score_question(q: Q, selected: Sequence[str]) -> float:
    if q.kind == "multi":
        return _score_multi(selected, q.correct)
    return _score_single(selected, q.correct)


def _build_result_item(q: Q, selected: Sequence[str]) -> Dict[str, Any]:
    pts = _score_question(q, selected)
    explanation = _resolve_explanation(q.id, q.lot, q.explanation)
    if explanation:
        explanation = (
            _exam_explanation(explanation)
            if 9001 <= q.id <= 9360 or 9501 <= q.id <= 9970
            else polish_text(explanation)
        )
    return {
        "id": q.id,
        "lot": q.lot,
        "kind": q.kind,
        "selected": list(selected),
        "correct": q.correct,
        "points": pts,
        "max_points": 1.0,
        "text": q.text,
        "options": q.options,
        "explanation": explanation,
    }


def _render_feedback_block(item: Dict[str, Any], *, show_points: bool = True) -> None:
    options: Dict[str, str] = {str(k).lower(): str(v) for k, v in (item.get("options") or {}).items()}
    selected: Set[str] = {str(x).lower() for x in (item.get("selected") or [])}
    correct: Set[str] = {str(x).lower() for x in (item.get("correct") or [])}
    pts = float(item.get("points") or 0.0)
    fully_correct = pts >= 1.0

    if fully_correct:
        st.success("Corect")
    else:
        st.error("Greșit")

    st.markdown(f"**Întrebare:** {item.get('text', '')}")
    st.markdown(f"**Răspunsul tău:** {_letters_to_text(list(selected), options)}")
    st.markdown(f"**Răspuns corect:** {_letters_to_text(list(correct), options)}")

    if show_points:
        st.write(f"Puncte: **{pts:.2f}/1.00**")

    explanation = str(item.get("explanation") or "").strip()
    if not explanation:
        explanation = _resolve_explanation(
            int(item.get("id") or 0),
            str(item.get("lot") or ""),
            "",
        )
        if explanation:
            explanation = _exam_explanation(explanation)
    if explanation:
        st.info(f"**Explicație:** {explanation}")

    st.markdown("**Variante:**")
    for letter, opt_text in sorted(options.items(), key=lambda kv: kv[0]):
        is_correct = letter in correct
        is_selected = letter in selected

        if is_correct and is_selected:
            prefix = "<span style='color:#1f7a1f; font-weight:700'>✓</span>"
        elif is_correct:
            prefix = "<span style='color:#1f7a1f; font-weight:700'>✓</span>"
        elif is_selected:
            prefix = "<span style='color:#b00020; font-weight:700'>✗</span>"
        else:
            prefix = "•"

        st.markdown(f"{prefix} **{letter})** {opt_text}", unsafe_allow_html=True)


def _render_review_item(item: Dict[str, Any]) -> None:
    _render_feedback_block(item, show_points=True)


def _render_correct_item(item: Dict[str, Any]) -> None:
    """Review pentru răspunsuri corecte: evidențiază ce ai ales bine."""
    options: Dict[str, str] = {str(k).lower(): str(v) for k, v in (item.get("options") or {}).items()}
    selected: Set[str] = {str(x).lower() for x in (item.get("selected") or [])}
    correct: Set[str] = {str(x).lower() for x in (item.get("correct") or [])}

    st.success("Corect")
    st.markdown(f"**Întrebare:** {item.get('text', '')}")
    st.markdown(f"**Răspunsul tău:** {_letters_to_text(list(selected), options)}")

    explanation = str(item.get("explanation") or "").strip()
    if not explanation:
        explanation = _resolve_explanation(
            int(item.get("id") or 0),
            str(item.get("lot") or ""),
            "",
        )
        if explanation:
            explanation = _exam_explanation(explanation)
    if explanation:
        st.info(f"**Explicație:** {explanation}")

    for letter, opt_text in sorted(options.items(), key=lambda kv: kv[0]):
        is_correct = letter in correct
        is_selected = letter in selected

        if is_correct and is_selected:
            prefix = "<span style='color:#1f7a1f; font-weight:700'>✓</span>"
        elif is_correct:
            prefix = "<span style='color:#1f7a1f; font-weight:700'>✓</span>"
        else:
            prefix = "•"

        st.markdown(f"{prefix} **{letter})** {opt_text}", unsafe_allow_html=True)


def _question_widget(q: Q, key_prefix: str, *, locked: bool = False) -> Tuple[List[str], bool]:
    """
    Returns (selected_letters, submitted_now).
    UI: always checkboxes (both single and multi). For single-kind, selecting more than 1 => scored wrong.
    """
    stem = (q.text or "").strip()
    with st.container(border=True):
        if stem:
            st.markdown(stem)
        else:
            st.warning(
                "Enunțul întrebării lipsește — sari peste sau repornește aplicația după actualizare."
            )

        opts_items = sorted(q.options.items(), key=lambda kv: kv[0])
        selected: List[str] = []

        for letter, text in opts_items:
            cb_key = f"{key_prefix}_opt_{letter}"
            checked = st.checkbox(f"{letter}) {text}", key=cb_key, disabled=locked)
            if checked:
                selected.append(letter)

        submitted = st.button(
            "Confirmă răspunsul",
            key=f"{key_prefix}_submit",
            disabled=locked,
        )
    return selected, submitted


def main() -> None:
    st.set_page_config(page_title="Test grilă psihologie", layout="wide")
    st.title("Simulare Examen Licență Psihologie")

    with st.sidebar:
        st.header("Setări")
        if os.environ.get("STREAMLIT_RUNTIME_ENV") == "cloud":
            st.caption("Rulează pe Streamlit Cloud — deschide acest link și pe telefon.")

        bank_path_str = st.text_input(
            "Fișier bancă (JSON / MD / TXT)",
            value=str(BANK_MD_DEFAULT),
            help="Pune banca în folderul proiectului sau dă calea completă.",
        )
        bank_path = Path(bank_path_str)

        cache_key = _questions_cache_key()
        db = _load_question_bank(cache_key)
        if not db.get("lots"):
            st.error(f"Nu am putut încărca banca. Verifică: {bank_path}")
            return

        all_questions = _get_all_questions(cache_key)
        _ensure_history()

        available_lots = sorted({q.lot for q in all_questions})
        selected_lots = st.multiselect(
            "Alege loturile",
            options=available_lots,
            default=available_lots,
        )
        mode = st.selectbox(
            "Mod",
            options=[
                "Examen (fără feedback până la final)",
                "Verificare (feedback imediat)",
            ],
        )
        shuffle = st.checkbox("Amestecă întrebările la start", value=True)
        limit_n = st.number_input("Număr întrebări (0 = toate)", min_value=0, value=0, step=10)
        time_limit_min = st.number_input("Limită timp (minute)", min_value=1, value=45, step=5)
        start = st.button("Start / Restart")

        st.divider()
        st.caption("Bancă încărcată")
        st.write(f"Întrebări disponibile: **{len(all_questions)}**")
        st.write(f"Domenii: **{len(available_lots)}**")
        if MERGED_JSON.exists():
            st.caption(f"Sursă combinată: `{MERGED_JSON.name}`")
        if MERGE_REPORT.exists():
            st.caption(f"Raport validare: `{MERGE_REPORT.name}`")
        if MERGE_RESEARCH.exists():
            st.caption(f"Cercetare metodologică: `{MERGE_RESEARCH.name}`")

        st.divider()
        st.caption("Fișiere date")
        st.write(f"- `data/questions.json`: {QUESTIONS_JSON.exists()}")
        st.write(f"- `data/scores_history.json`: {HISTORY_JSON.exists()}")

    if not selected_lots:
        st.warning("Selectează măcar un lot.")
        return

    pool = [q for q in all_questions if q.lot in set(selected_lots)]
    if not pool:
        st.error("Nu am găsit întrebări pentru loturile selectate.")
        return

    with st.sidebar:
        st.write(f"În loturile selectate: **{len(pool)}** întrebări")
        if limit_n and limit_n > len(pool):
            st.warning(
                f"Ai cerut {int(limit_n)}, dar lotul/loturile selectate au doar "
                f"**{len(pool)}** întrebări. Testul va conține **{len(pool)}**."
            )

    if start or "run" not in st.session_state:
        run_questions = pool[:]
        if shuffle:
            random.shuffle(run_questions)
        if limit_n and limit_n > 0:
            run_questions = run_questions[: int(limit_n)]

        st.session_state.run = {
            "questions": run_questions,
            "idx": 0,
            "answers": {},  # qid -> selected letters (list[str])
            "confirmed": set(),  # qid confirmed
            "feedback_qid": None,  # verificare: afișează feedback până la Continuă
            "mode": mode,
            "start_ts": time.time(),
            "time_limit_s": int(time_limit_min) * 60,
            "selected_lots": selected_lots,
            "shuffle": shuffle,
            "limit_n": int(limit_n),
        }

    run = st.session_state.run
    run.setdefault("feedback_qid", None)
    questions: List[Q] = run["questions"]
    idx: int = run["idx"]
    verify_mode = run["mode"].startswith("Verificare")
    showing_feedback = verify_mode and run.get("feedback_qid") is not None

    elapsed = time.time() - run["start_ts"]
    remaining = run["time_limit_s"] - elapsed

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write(f"Progres: **{min(idx + 1, len(questions))}/{len(questions)}**")
    with col2:
        st.write(f"Timp: **{_format_seconds(elapsed)}**")
    with col3:
        st.write(f"Rămas: **{_format_seconds(remaining)}**")

    if remaining <= 0:
        st.warning("Timpul a expirat. Calculez rezultatul.")
        run["idx"] = len(questions)
        st.rerun()

    if run["idx"] >= len(questions):
        # Results
        per_item: List[Dict[str, Any]] = []
        for q in questions:
            sel = run["answers"].get(q.id) or []
            per_item.append(_build_result_item(q, sel))

        total = sum(float(item["points"]) for item in per_item)
        correct_items = [item for item in per_item if _is_fully_correct(item)]
        wrong_items = [item for item in per_item if not _is_fully_correct(item)]

        percent = 100.0 * total / max(1, len(questions))
        st.subheader("Rezultat")
        st.write(f"Scor: **{total:.2f} / {len(questions)}**  (**{percent:.1f}%**)")
        st.write(
            f"Răspunsuri corecte: **{len(correct_items)}** | "
            f"Răspunsuri greșite: **{len(wrong_items)}**"
        )

        # Save history once per run completion
        if not run.get("history_saved"):
            _append_history(
                {
                    "ts": int(time.time()),
                    "mode": run["mode"],
                    "lots": run["selected_lots"],
                    "shuffle": run["shuffle"],
                    "n_questions": len(questions),
                    "time_limit_min": int(run["time_limit_s"] // 60),
                    "elapsed_s": int(elapsed),
                    "score_points": float(total),
                    "score_percent": float(percent),
                    "correct_count": len(correct_items),
                    "wrong_count": len(wrong_items),
                }
            )
            run["history_saved"] = True

        st.subheader("Recapitulare răspunsuri")

        with st.expander(
            f"Răspunsurile tale corecte ({len(correct_items)})",
            expanded=True,
        ):
            if not correct_items:
                st.info("Nu ai răspunsuri complet corecte în această sesiune.")
            else:
                for item in correct_items:
                    _render_correct_item(item)
                    st.divider()

        with st.expander(
            f"Răspunsurile greșite — compară ce ai ales vs. corect ({len(wrong_items)})",
            expanded=bool(wrong_items),
        ):
            if not wrong_items:
                st.success("Toate răspunsurile sunt corecte.")
            else:
                for item in wrong_items:
                    _render_review_item(item)
                    st.divider()

        with st.expander("Istoric scoruri"):
            hist = _ensure_history()
            if not hist:
                st.info("Nu există istoric încă.")
            else:
                st.dataframe(hist[::-1], use_container_width=True)

        return

    # Question page
    q = questions[run["idx"]]
    # user preference: do not show subject/domain title

    answer, submitted = _question_widget(
        q,
        key_prefix=f"q{q.id}",
        locked=showing_feedback and run.get("feedback_qid") == q.id,
    )

    # persist current selection even if not confirmed (nice UX)
    run["answers"][q.id] = answer

    if submitted:
        run["confirmed"].add(q.id)
        if verify_mode:
            run["feedback_qid"] = q.id
            st.rerun()
        else:
            run["idx"] += 1
            st.rerun()

    if showing_feedback and run.get("feedback_qid") == q.id:
        feedback_answer = run["answers"].get(q.id) or []
        result_item = _build_result_item(q, feedback_answer)
        _render_feedback_block(result_item, show_points=True)
        if st.button("Continuă la următoarea întrebare", key=f"next_{q.id}"):
            run["feedback_qid"] = None
            run["idx"] += 1
            st.rerun()

    nav1, nav2, nav3 = st.columns([1, 1, 2])
    with nav1:
        if st.button("Înapoi", disabled=(run["idx"] <= 0 or showing_feedback)):
            run["feedback_qid"] = None
            run["idx"] -= 1
            st.rerun()
    with nav2:
        if st.button("Sari peste", disabled=showing_feedback):
            run["feedback_qid"] = None
            run["idx"] += 1
            st.rerun()
    with nav3:
        if st.button("Finalizează testul acum"):
            run["idx"] = len(questions)
            st.rerun()


if __name__ == "__main__":
    main()
