from __future__ import annotations

import json
import hashlib
import re
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from scripts.polish_text import polish_text


LOT_HEADER_RE = re.compile(r"^\s*#\s*Lotul\s+(\d+)\s*$", re.IGNORECASE)
BAREM_HEADER_RE = re.compile(r"^\s*##\s*Barem\s+—\s+Lotul\s+(\d+)\s*$", re.IGNORECASE)
QUESTION_RE = re.compile(r"^\s*(\d+)\.\s+(.*\S)\s*$")
OPTION_RE = re.compile(r"^\s*([a-d])\)\s+(.*\S)\s*$", re.IGNORECASE)
BAREM_LINE_RE = re.compile(r"^\s*(\d+)\.\s+([a-d](?:\s*,\s*[a-d])*)\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class ParsedQuestion:
    id: int
    text: str
    options: Dict[str, str]  # keys: "a".."d"
    correct: List[str]  # one or more letters, lower-case

    @property
    def kind(self) -> str:
        return "multi" if len(self.correct) > 1 else "single"


def _split_letters(s: str) -> List[str]:
    parts = [p.strip().lower() for p in s.split(",")]
    return [p for p in parts if p]


def parse_barem(lines: Sequence[str], start_idx: int) -> Tuple[Dict[int, List[str]], int]:
    """
    Parse barem section starting at start_idx (first line AFTER the '## Barem — Lotul X' header).
    Returns (answer_key, next_index_after_section).
    """
    key: Dict[int, List[str]] = {}
    i = start_idx
    while i < len(lines):
        line = lines[i].rstrip("\n")
        # Next lot or next barem begins => stop.
        if LOT_HEADER_RE.match(line) or BAREM_HEADER_RE.match(line):
            break
        m = BAREM_LINE_RE.match(line)
        if m:
            qid = int(m.group(1))
            letters = _split_letters(m.group(2))
            key[qid] = letters
        i += 1
    return key, i


def parse_questions(lines: Sequence[str], start_idx: int) -> Tuple[List[Tuple[int, str, Dict[str, str]]], int]:
    """
    Parse questions section until the next '## Barem — Lotul X' or next '# Lotul X'.
    Returns list of (id, text, options) and next index.
    """
    out: List[Tuple[int, str, Dict[str, str]]] = []
    i = start_idx
    current_id: Optional[int] = None
    current_text: Optional[str] = None
    current_options: Dict[str, str] = {}

    def flush():
        nonlocal current_id, current_text, current_options
        if current_id is None or current_text is None:
            return
        if current_options:
            out.append((current_id, current_text.strip(), dict(current_options)))
        current_id = None
        current_text = None
        current_options = {}

    while i < len(lines):
        line = lines[i].rstrip("\n")
        if LOT_HEADER_RE.match(line) or BAREM_HEADER_RE.match(line):
            flush()
            break

        qm = QUESTION_RE.match(line)
        if qm:
            flush()
            current_id = int(qm.group(1))
            current_text = qm.group(2).strip()
            current_options = {}
            i += 1
            continue

        om = OPTION_RE.match(line)
        if om and current_id is not None:
            letter = om.group(1).lower()
            current_options[letter] = om.group(2).strip()
            i += 1
            continue

        # Continuation line for question text (rare but possible): append if we're inside a question and
        # haven't started options yet.
        if current_id is not None and current_text is not None and not current_options:
            if line.strip():
                current_text = f"{current_text} {line.strip()}"

        i += 1

    return out, i


def parse_bank_md(md_path: Path) -> Dict[str, Any]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    lots: Dict[str, Dict[str, Any]] = {}
    i = 0
    current_lot: Optional[str] = None

    # First pass: parse per lot questions + barem.
    while i < len(lines):
        line = lines[i]

        lm = LOT_HEADER_RE.match(line)
        if lm:
            current_lot = f"Lotul {int(lm.group(1))}"
            lots.setdefault(current_lot, {"questions_raw": [], "answer_key": {}})
            i += 1
            # Parse questions until barem/next lot
            qraw, i = parse_questions(lines, i)
            lots[current_lot]["questions_raw"].extend(qraw)
            continue

        bm = BAREM_HEADER_RE.match(line)
        if bm:
            lot = f"Lotul {int(bm.group(1))}"
            lots.setdefault(lot, {"questions_raw": [], "answer_key": {}})
            key, i2 = parse_barem(lines, i + 1)
            lots[lot]["answer_key"].update(key)
            i = i2
            continue

        i += 1

    # Second pass: merge answer keys into questions
    out_lots: Dict[str, Any] = {}
    total_q = 0
    for lot, data in lots.items():
        qraw: List[Tuple[int, str, Dict[str, str]]] = data.get("questions_raw", [])
        key: Dict[int, List[str]] = data.get("answer_key", {})
        questions: List[Dict[str, Any]] = []
        for qid, qtext, opts in qraw:
            correct = key.get(qid)
            if not correct:
                # Keep question but mark missing key; app can warn.
                correct = []
            pq = ParsedQuestion(id=qid, text=qtext, options=opts, correct=correct)
            questions.append(
                {
                    "id": pq.id,
                    "text": pq.text,
                    "options": pq.options,
                    "kind": pq.kind if pq.correct else "unknown",
                    "correct": pq.correct,
                }
            )
        questions.sort(key=lambda q: q["id"])
        out_lots[lot] = {"questions": questions}
        total_q += len(questions)

    return {
        "source_file": str(md_path.name),
        "lots": out_lots,
        "total_questions": total_q,
    }


def write_questions_json(md_path: Path, out_path: Path) -> Dict[str, Any]:
    suffix = md_path.suffix.lower()
    if suffix == ".json":
        data = parse_bank_json(md_path)
    elif suffix == ".txt":
        data = parse_itemi_txt(md_path)
    else:
        data = parse_bank_md(md_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data


def parse_bank_json(json_path: Path) -> Dict[str, Any]:
    """
    Expected format: a JSON array with objects like:
      {
        "id": 1,
        "domeniu": "...",
        "tip": "unic" | "multiplu" | ...,
        "intrebare": "...",
        "variante": {"a": "...", ...},
        "raspuns_corect": ["a", "b"]
      }

    We map `domeniu` to a "lot" name to preserve the UI filter.
    """
    raw = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("Bank JSON must be a list of questions")

    out_lots: Dict[str, Any] = {}
    total_q = 0

    def norm_kind(tip: Any, correct: List[str]) -> str:
        s = str(tip or "").strip().lower()
        if s in {"multiplu", "multi", "multiple"}:
            return "multi"
        if s in {"adevarat_fals", "adevărat_fals", "tf", "true_false"}:
            return "adevărat_fals"
        if s in {"unic", "single", "unica", "unică"}:
            return "single"
        return "multi" if len(correct) > 1 else "single"

    for obj in raw:
        if not isinstance(obj, dict):
            continue
        qid = int(obj.get("id"))
        lot = str(obj.get("domeniu") or "Banca").strip() or "Banca"
        text = polish_text(str(obj.get("intrebare") or "").strip())
        options = {
            str(k).lower(): polish_text(str(v))
            for k, v in (obj.get("variante") or {}).items()
        }
        correct = [str(x).lower() for x in (obj.get("raspuns_corect") or [])]
        kind = norm_kind(obj.get("tip"), correct) if correct else "unknown"

        explanation = polish_text(str(obj.get("explicatie") or "").strip())

        out_lots.setdefault(lot, {"questions": []})
        out_lots[lot]["questions"].append(
            {
                "id": qid,
                "text": text,
                "options": options,
                "kind": kind,
                "correct": correct,
                "explanation": explanation,
            }
        )
        total_q += 1

    # sort questions within each lot
    for lot_name in list(out_lots.keys()):
        out_lots[lot_name]["questions"].sort(key=lambda q: q["id"])

    return {
        "source_file": str(json_path.name),
        "lots": out_lots,
        "total_questions": total_q,
    }


SECTION_HEADER_RE = re.compile(r"^\s*(.+?)\s+—\s*(\d+)\s+itemi\s*$", re.IGNORECASE)


def _stable_seed(*parts: str) -> int:
    h = hashlib.sha1("||".join(parts).encode("utf-8")).hexdigest()
    return int(h[:8], 16)


def _shuffle_options_keep_correct_a(
    question_text: str, options: Dict[str, str]
) -> Tuple[Dict[str, str], List[str]]:
    """
    The `Itemi.txt` file usually encodes the correct answer as option 'a)'.
    We shuffle option order and return:
      - new options dict with keys 'a'.. in shuffled order
      - new correct list with the letter where the ORIGINAL 'a' landed
    """
    if "a" not in options:
        # fallback: don't shuffle
        return options, []

    items = sorted(options.items(), key=lambda kv: kv[0])  # original order
    rng = random.Random(_stable_seed(question_text))
    rng.shuffle(items)

    new_letters = ["a", "b", "c", "d", "e", "f"]
    remapped: Dict[str, str] = {}
    correct_letter: Optional[str] = None
    for idx, (old_letter, text) in enumerate(items):
        new_letter = new_letters[idx]
        remapped[new_letter] = text
        if old_letter.lower() == "a":
            correct_letter = new_letter

    return remapped, [correct_letter] if correct_letter else []


def parse_itemi_txt(txt_path: Path) -> Dict[str, Any]:
    """
    Parse `Itemi.txt`-style banks:
      - Section headers: "Domeniu — N itemi"
      - Questions: a line ending with ":" (may span multiple lines, but usually one line)
      - Options: "a) ..." etc; can be 2 options (T/F) or 4 options

    Assumption (as requested): the correct option in the source is usually `a)`,
    and we randomize option order so the correct letter is no longer mostly 'a'.
    """
    lines = txt_path.read_text(encoding="utf-8").splitlines()

    current_section = "Itemi.txt"
    lots: Dict[str, Any] = {}
    qid = 1
    i = 0

    def add_question(qtext: str, opts: Dict[str, str]) -> None:
        nonlocal qid
        if not qtext or not opts:
            return
        remapped_opts, correct = _shuffle_options_keep_correct_a(qtext, opts)
        kind = "single" if len(correct) <= 1 else "multi"
        lots.setdefault(current_section, {"questions": []})
        lots[current_section]["questions"].append(
            {
                "id": qid,
                "text": qtext.strip(),
                "options": remapped_opts,
                "kind": kind if correct else "unknown",
                "correct": correct,
            }
        )
        qid += 1

    while i < len(lines):
        line = lines[i].strip()

        sm = SECTION_HEADER_RE.match(line)
        if sm:
            current_section = sm.group(1).strip()
            i += 1
            continue

        if not line or line.lower() == "itemi":
            i += 1
            continue

        # detect a question start: ends with ":" and next non-empty lines include "a)" option
        if line.endswith(":"):
            q_lines = [line]
            i += 1
            # consume blank lines
            while i < len(lines) and not lines[i].strip():
                i += 1
            opts: Dict[str, str] = {}
            # read options
            while i < len(lines):
                ol = lines[i].strip()
                if not ol:
                    i += 1
                    break
                om = OPTION_RE.match(ol)
                if om:
                    opts[om.group(1).lower()] = om.group(2).strip()
                    i += 1
                    continue
                # next question/section begins
                if ol.endswith(":") or SECTION_HEADER_RE.match(ol):
                    break
                i += 1
            add_question(" ".join(q_lines), opts)
            continue

        # Some questions are statements without ":" in this file; handle pattern:
        # statement line followed by blank line then a) b)...
        # We'll treat any non-empty line followed by options as question.
        # Peek ahead for an option.
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and OPTION_RE.match(lines[j].strip()):
            qtext = line
            i = j
            opts: Dict[str, str] = {}
            while i < len(lines):
                ol = lines[i].strip()
                if not ol:
                    i += 1
                    break
                om = OPTION_RE.match(ol)
                if om:
                    opts[om.group(1).lower()] = om.group(2).strip()
                    i += 1
                    continue
                if ol.endswith(":") or SECTION_HEADER_RE.match(ol):
                    break
                i += 1
            add_question(qtext, opts)
            continue

        i += 1

    # Sort questions per section (already sequential)
    total_q = sum(len(v["questions"]) for v in lots.values())
    return {"source_file": str(txt_path.name), "lots": lots, "total_questions": total_q}

