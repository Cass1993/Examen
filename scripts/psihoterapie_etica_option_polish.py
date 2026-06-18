"""Opțiuni echilibrate — lot etică, psihodramă, terapia unificării."""

from __future__ import annotations

from typing import Dict

from scripts.psihoterapie_ii_option_polish import polish_option_set


def polish_bank_row(row: Dict) -> Dict:
    if row.get("tf") or not row.get("options"):
        return row
    new_opts, new_correct = polish_option_set(
        str(row.get("stem", "")),
        row["options"],
        str(row.get("correct", "")),
    )
    out = dict(row)
    out["options"] = new_opts
    out["correct"] = new_correct
    return out
