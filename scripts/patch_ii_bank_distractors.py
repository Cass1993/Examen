"""Aplică fix distractori pe sursele loturilor examen II + resync questions.json."""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.exam_ii_plausible_distractors import fix_exam_wrong_options  # noqa: E402

II_BANK_SOURCES: List[Tuple[str, str]] = [
    ("scripts.psihologia_muncii_ii_bank_data", "PSIHOLOGIA_MUNCII_ITEMS"),
    ("scripts.psihologia_muncii_performanta_bank_data", "PERFORMANTA_MUNCII_ITEMS"),
    ("scripts.psihologia_muncii_selectie_bank_data", "SELECTIE_PERSONAL_ITEMS"),
    ("scripts.psihologia_muncii_design_munca_bank_data", "DESIGN_MUNCII_ITEMS"),
    ("scripts.evaluare_psihologica_ii_bank_data", "EVALUARE_ITEMS"),
    ("scripts.perspectiva_psihometrica_bank_data", "PSIHOMETRIC_ITEMS"),
    ("scripts.inteligenta_istoric_modele_bank_data", "INTELIGENTA_ITEMS"),
    ("scripts.inteligenta_emotionala_bank_data", "INTELIGENTA_EMOTIONALA_ITEMS"),
    ("scripts.motivatie_bank_data", "MOTIVATIE_ITEMS"),
    ("scripts.interese_bank_data", "INTERESE_ITEMS"),
    ("scripts.jvis_bank_data", "JVIS_ITEMS"),
    ("scripts.psihoterapie_ii_bank_data", "ITEMS"),
    ("scripts.psihoterapie_ii_tricky_items", "TRICKY_ITEMS"),
    ("scripts.psihoterapie_ii_psihodinamic_items", "PSIHODINAMIC_ITEMS"),
    ("scripts.psihoterapie_ii_aparare_items", "APARARE_ITEMS"),
    ("scripts.psihoterapie_ii_behaviorism_items", "BEHAVIORISM_ITEMS"),
    ("scripts.psihoterapie_ii_behavioral_techniques_items", "BEHAVIORAL_TECHNIQUES_ITEMS"),
    ("scripts.psihoterapie_ii_cbt_ellis_beck_items", "CBT_ELLIS_BECK_ITEMS"),
    ("scripts.psihoterapie_ii_lazarus_multimodal_items", "LAZARUS_MULTIMODAL_ITEMS"),
    ("scripts.psihoterapie_ii_glasser_reality_items", "GLASSER_REALITY_ITEMS"),
    ("scripts.psihoterapie_ii_family_therapy_items", "FAMILY_THERAPY_ITEMS"),
    ("scripts.psihoterapie_ii_psychodrama_items", "PSYCHODRAMA_ITEMS"),
    ("scripts.psihoterapie_ii_psychodrama_extra_items", "PSYCHODRAMA_EXTRA_ITEMS"),
    ("scripts.psihoterapie_ii_mitrofan_unificare_items", "MITROFAN_UNIFICARE_ITEMS"),
    ("scripts.psihopatologie_ii_bank_data", "ITEMS"),
    ("scripts.psihopatologie_ii_bipolar_items", "BIPOLAR_ITEMS"),
    ("scripts.psihopatologie_ii_ptsd_items", "PTSD_ITEMS"),
    ("scripts.psihopatologie_ii_suicid_items", "SUICID_ITEMS"),
    ("scripts.psihopatologie_ii_toc_items", "TOC_ITEMS"),
    ("scripts.psihopatologie_ii_anxietate_items", "ANXIETATE_ITEMS"),
    ("scripts.psihopatologie_ii_personalitate_items", "PERSONALITATE_ITEMS"),
    ("scripts.psihopatologie_ii_personalitate_extra_items", "PERSONALITATE_EXTRA_ITEMS"),
    ("scripts.psihopatologie_ii_schizofrenie_depresie_items", "SCHIZOFRENIE_DEPRESIE_ITEMS"),
    (
        "scripts.psihopatologie_ii_schizofrenie_depresie_extra_items",
        "SCHIZOFRENIE_DEPRESIE_EXTRA_ITEMS",
    ),
]


def _replace_in_file(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    for quote in ('"', "'"):
        old_q = f"{quote}{old}{quote}"
        new_q = f'{quote}{new}{quote}'
        if old_q in text:
            path.write_text(text.replace(old_q, new_q, 1), encoding="utf-8")
            return True
    return False


def patch_module(mod_name: str, list_name: str) -> int:
    path = ROOT / (mod_name.replace(".", "/") + ".py")
    if not path.exists():
        return 0
    mod = importlib.import_module(mod_name)
    items: List[Dict[str, Any]] = getattr(mod, list_name, [])
    n = 0
    for row in items:
        if row.get("tf") or not row.get("options"):
            continue
        stem = str(row.get("stem", ""))
        old_opts = [str(o) for o in row["options"]]
        new_opts = fix_exam_wrong_options(stem, old_opts, str(row.get("correct", "")))
        for old, new in zip(old_opts, new_opts):
            if old != new and _replace_in_file(path, old, new):
                n += 1
    return n


def patch_all_banks() -> int:
    total = 0
    for mod_name, list_name in II_BANK_SOURCES:
        try:
            n = patch_module(mod_name, list_name)
        except Exception as exc:
            print(f"ERR {mod_name}: {exc}")
            continue
        if n:
            print(f"{mod_name}.{list_name}: {n} opțiuni")
            total += n
    return total


def sync_all_ii_lots() -> None:
    from scripts.evaluare_psihologica_ii_exam_items import build_items as build_eval
    from scripts.psihologia_muncii_ii_exam_items import build_items as build_pm
    from scripts.psihopatologie_ii_exam_items import build_items as build_psihopat
    from scripts.psihoterapie_ii_exam_items import build_items as build_psiho

    qpath = ROOT / "data" / "questions.json"
    data = json.loads(qpath.read_text(encoding="utf-8"))
    lots = data.setdefault("lots", {})

    for name, builder in (
        ("Introducere în evaluarea psihologică II", build_eval),
        ("Psihologia muncii II", build_pm),
        ("Psihoterapie II: Orientări și metode în psihoterapie", build_psiho),
        ("Psihopatologie II", build_psihopat),
    ):
        built = builder()
        lots[name] = {"questions": built}
        print(f"Sync {name}: {len(built)} itemi")

    data["total_questions"] = sum(len(b.get("questions") or []) for b in lots.values())
    qpath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    print("=== Patch distractori sursă (loturi II) ===")
    n = patch_all_banks()
    print(f"Total opțiuni rescrise în sursă: {n}")
    print()
    print("=== Resync questions.json (cu polish la build) ===")
    sync_all_ii_lots()
    print()
    print("=== Audit distractori rămași în sursă ===")
    from scripts.audit_ii_absolutes import audit

    report = audit()
    print("\n".join(report[:25]))
    if len(report) > 25:
        print(f"... și încă {len(report) - 25} linii (vezi data/audit_ii_absolutes.txt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
