"""Utilitare pentru itemi de examen — amestecare opțiuni, construire item."""

from __future__ import annotations

import random
from typing import Dict, List, Sequence, Tuple

LETTERS = ("a", "b", "c", "d")


def normalize_correct(correct: str) -> str:
    return "".join(ch for ch in (correct or "").lower() if ch in LETTERS)


def shuffle_exam_options(
    options: Sequence[str],
    correct: str,
    seed: int,
) -> Tuple[Dict[str, str], List[str]]:
    """Amestecă opțiunile determinist; păstrează textele răspunsurilor corecte."""
    texts = list(options)
    correct_letters = list(normalize_correct(correct))
    correct_texts = {texts[LETTERS.index(ch)] for ch in correct_letters}

    rng = random.Random(seed)
    perm = list(range(4))
    rng.shuffle(perm)

    new_opts = {LETTERS[i]: texts[perm[i]] for i in range(4)}
    new_correct = [letter for letter in LETTERS if new_opts[letter] in correct_texts]
    return new_opts, new_correct


def build_tf_exam_item(
    item_id: int,
    proposition: str,
    is_true: bool,
    lot_name: str,
    explanation: str = "",
) -> Dict:
    """Item adevărat/fals pentru loturi examen."""
    return {
        "id": item_id,
        "text": (proposition or "").strip(),
        "options": {"a": "Adevărat", "b": "Fals"},
        "kind": "single",
        "correct": ["a" if is_true else "b"],
        "explanation": (explanation or "").strip(),
        "domeniu": lot_name,
        "tip": "unic",
        "exam_item": True,
    }


def build_items_from_bank(
    rows: Sequence[Dict],
    start_id: int,
    lot_name: str,
) -> List[Dict]:
    """Construiește itemi din rânduri {stem, options?, correct?} sau {stem, tf, correct_tf}."""
    out: List[Dict] = []
    for i, row in enumerate(rows):
        item_id = start_id + i
        if row.get("tf"):
            out.append(
                build_tf_exam_item(
                    item_id,
                    str(row["stem"]),
                    bool(row.get("correct_tf")),
                    lot_name,
                    str(row.get("explanation") or ""),
                )
            )
        else:
            out.append(
                build_exam_item(
                    item_id,
                    str(row["stem"]),
                    tuple(row["options"]),
                    str(row["correct"]),
                    lot_name,
                    explanation=str(row.get("explanation") or ""),
                )
            )
    return out


def build_exam_item(
    item_id: int,
    stem: str,
    options: Sequence[str],
    correct: str,
    lot_name: str,
    seed: int | None = None,
    explanation: str = "",
) -> Dict:
    shuffle_seed = seed if seed is not None else item_id * 7919 + 104729
    new_opts, new_correct = shuffle_exam_options(options, correct, shuffle_seed)
    kind = "multi" if len(new_correct) > 1 else "single"
    return {
        "id": item_id,
        "text": stem,
        "options": new_opts,
        "kind": kind,
        "correct": new_correct,
        "explanation": (explanation or "").strip(),
        "domeniu": lot_name,
        "tip": "multi" if kind == "multi" else "unic",
        "exam_item": True,
    }
