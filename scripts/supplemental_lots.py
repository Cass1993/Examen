"""Loturi examen suplimentare — injectare și persistare în questions.json."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

SupplementalLot = Tuple[str, Callable[[], List[Dict[str, Any]]], Callable[[str], int]]

REGISTERED_LOTS: List[SupplementalLot] = []

# Bump la reformulări distractori — forțează rescrierea loturilor II în questions.json
II_DISTRACTOR_VERSION = "150"
II_LOT_NAMES = frozenset(
    {
        "Introducere în evaluarea psihologică II",
        "Psihologia muncii II",
        "Psihoterapie II: Orientări și metode în psihoterapie",
        "Psihopatologie II",
        "Psihologia dezvoltării II",
        "Psihologia învățării II",
        "Statistică II",
        "Caracteristici psihometrice II",
        "Inventare de personalitate II",
        "Psihologia personalității II",
        "Epigenetica II: BAZE MOLECULARE",
    }
)


def _register() -> None:
    if REGISTERED_LOTS:
        return
    from scripts.epigenetica_exam_items import (
        LOT_NAME as EPIGENETICA_LOT,
        build_items as build_epigenetica,
        merge_into_bank as merge_epigenetica,
    )
    from scripts.i_o_exam_items import (
        LOT_NAME as IO_LOT,
        build_items as build_io,
        merge_into_bank as merge_io,
    )
    from scripts.psihoterapie_etica_exam_items import (
        LOT_NAME as PSIHO_ETICA_LOT,
        build_items as build_psiho_etica,
        merge_into_bank as merge_psiho_etica,
    )
    from scripts.psihoterapie_ii_exam_items import (
        LOT_NAME as PSIHO_II_LOT,
        build_items as build_psiho_ii,
        merge_into_bank as merge_psiho_ii,
    )
    from scripts.psihopatologie_ii_exam_items import (
        LOT_NAME as PSIHOPAT_II_LOT,
        build_items as build_psihopat_ii,
        merge_into_bank as merge_psihopat_ii,
    )
    from scripts.evaluare_psihologica_ii_exam_items import (
        LOT_NAME as EVALUARE_II_LOT,
        build_items as build_evaluare_ii,
        merge_into_bank as merge_evaluare_ii,
    )
    from scripts.psihologia_muncii_ii_exam_items import (
        LOT_NAME as PSIHO_MUNCII_II_LOT,
        build_items as build_psiho_muncii_ii,
        merge_into_bank as merge_psiho_muncii_ii,
    )
    from scripts.psihologia_dezvoltarii_ii_exam_items import (
        LOT_NAME as PSIHO_DEZ_II_LOT,
        build_items as build_psiho_dez_ii,
        merge_into_bank as merge_psiho_dez_ii,
    )
    from scripts.psihologia_invatarii_ii_exam_items import (
        LOT_NAME as PSIHO_INV_II_LOT,
        build_items as build_psiho_inv_ii,
        merge_into_bank as merge_psiho_inv_ii,
    )
    from scripts.statistica_ii_exam_items import (
        LOT_NAME as STATISTICA_II_LOT,
        build_items as build_statistica_ii,
        merge_into_bank as merge_statistica_ii,
    )
    from scripts.caracteristici_psihometrice_ii_exam_items import (
        LOT_NAME as CARACTERISTICI_PSIHOMETRICE_II_LOT,
        build_items as build_caracteristici_psihometrice_ii,
        merge_into_bank as merge_caracteristici_psihometrice_ii,
    )
    from scripts.inventare_personalitate_ii_exam_items import (
        LOT_NAME as INVENTARE_PERSONALITATE_II_LOT,
        build_items as build_inventare_personalitate_ii,
        merge_into_bank as merge_inventare_personalitate_ii,
    )
    from scripts.epigenetica_ii_baze_moleculare_exam_items import (
        LOT_NAME as EPIGENETICA_II_BAZE_LOT,
        build_items as build_epigenetica_ii_baze,
        merge_into_bank as merge_epigenetica_ii_baze,
    )
    from scripts.psihologia_personalitatii_ii_exam_items import (
        LOT_NAME as PSIHOLOGIA_PERSONALITATII_II_LOT,
        build_items as build_psihologia_personalitatii_ii,
        merge_into_bank as merge_psihologia_personalitatii_ii,
    )

    REGISTERED_LOTS.extend(
        [
            (IO_LOT, build_io, merge_io),
            (EPIGENETICA_LOT, build_epigenetica, merge_epigenetica),
            (PSIHO_II_LOT, build_psiho_ii, merge_psiho_ii),
            (PSIHO_ETICA_LOT, build_psiho_etica, merge_psiho_etica),
            (PSIHOPAT_II_LOT, build_psihopat_ii, merge_psihopat_ii),
            (EVALUARE_II_LOT, build_evaluare_ii, merge_evaluare_ii),
            (PSIHO_MUNCII_II_LOT, build_psiho_muncii_ii, merge_psiho_muncii_ii),
            (PSIHO_DEZ_II_LOT, build_psiho_dez_ii, merge_psiho_dez_ii),
            (PSIHO_INV_II_LOT, build_psiho_inv_ii, merge_psiho_inv_ii),
            (STATISTICA_II_LOT, build_statistica_ii, merge_statistica_ii),
            (
                CARACTERISTICI_PSIHOMETRICE_II_LOT,
                build_caracteristici_psihometrice_ii,
                merge_caracteristici_psihometrice_ii,
            ),
            (
                INVENTARE_PERSONALITATE_II_LOT,
                build_inventare_personalitate_ii,
                merge_inventare_personalitate_ii,
            ),
            (
                EPIGENETICA_II_BAZE_LOT,
                build_epigenetica_ii_baze,
                merge_epigenetica_ii_baze,
            ),
            (
                PSIHOLOGIA_PERSONALITATII_II_LOT,
                build_psihologia_personalitatii_ii,
                merge_psihologia_personalitatii_ii,
            ),
        ]
    )


def _lot_content_hash(items: List[Dict[str, Any]]) -> str:
    """Hash pe enunț + opțiuni + barem — detectează reformulări fără schimbare de număr."""
    parts: List[str] = []
    for q in sorted(items, key=lambda x: int(x.get("id") or 0)):
        opts = q.get("options") or {}
        parts.append(
            "|".join(
                [
                    str(q.get("text") or ""),
                    json.dumps(opts, ensure_ascii=False, sort_keys=True),
                    json.dumps(q.get("correct") or [], ensure_ascii=False),
                    str(q.get("explanation") or ""),
                ]
            )
        )
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def _merge_missing_explanations(
    existing: List[Dict[str, Any]], built: List[Dict[str, Any]]
) -> bool:
    """Completează explicații lipsă în lotul existent, fără rescriere completă."""
    by_id = {int(q.get("id") or 0): q for q in built}
    changed = False
    for q in existing:
        qid = int(q.get("id") or 0)
        src = by_id.get(qid)
        if not src:
            continue
        new_expl = str(src.get("explanation") or "").strip()
        old_expl = str(q.get("explanation") or "").strip()
        if new_expl and new_expl != old_expl:
            q["explanation"] = new_expl
            changed = True
    return changed


def ensure_all_supplemental_lots(data: Dict[str, Any], bank_path: Path) -> Dict[str, Any]:
    """Adaugă sau actualizează loturile examen când conținutul din cod diferă."""
    from scripts.lot_archive import (
        archive_path_for,
        ensure_archive_split,
        is_ii_lot,
        load_archive,
        merge_active_and_archive,
        promote_ii_lots_from_archive,
    )

    _register()
    if bank_path.exists():
        data = json.loads(bank_path.read_text(encoding="utf-8"))

    archive_path = archive_path_for(bank_path)
    archive_data = load_archive(archive_path)
    active_lots = data.setdefault("lots", {})
    archive_lots = archive_data.setdefault("lots", {})
    active_lots, archive_lots, promoted = promote_ii_lots_from_archive(
        active_lots, archive_lots
    )
    changed = promoted
    archive_changed = promoted
    version_path = bank_path.parent / ".ii_distractor_version"
    stored_ii_version = (
        version_path.read_text(encoding="utf-8").strip() if version_path.exists() else ""
    )
    force_ii_rebuild = stored_ii_version != II_DISTRACTOR_VERSION

    for obsolete in ("Perspectiva psihometrică",):
        for store in (active_lots, archive_lots):
            if obsolete in store:
                del store[obsolete]
                changed = True
                archive_changed = True

    for lot_name, build_items, _merge_into_bank in REGISTERED_LOTS:
        built = build_items()
        store = active_lots if is_ii_lot(lot_name) else archive_lots
        existing = store.get(lot_name, {}).get("questions") or []
        if (
            not (force_ii_rebuild and lot_name in II_LOT_NAMES)
            and existing
            and len(existing) == len(built)
            and _lot_content_hash(existing) == _lot_content_hash(built)
        ):
            if _merge_missing_explanations(existing, built):
                store[lot_name] = {"questions": existing}
                if is_ii_lot(lot_name):
                    changed = True
                else:
                    archive_changed = True
            continue
        store[lot_name] = {"questions": built}
        if is_ii_lot(lot_name):
            changed = True
        else:
            archive_changed = True

    if changed:
        data["total_questions"] = sum(
            len(b.get("questions") or []) for b in active_lots.values()
        )
        data["active_lots_only"] = True
        bank_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            bank_path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            if force_ii_rebuild:
                version_path.write_text(II_DISTRACTOR_VERSION, encoding="utf-8")
        except OSError:
            pass

    if archive_changed:
        archive_data["total_questions"] = sum(
            len(b.get("questions") or []) for b in archive_lots.values()
        )
        try:
            archive_path.write_text(
                json.dumps(archive_data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except OSError:
            pass

    try:
        ensure_archive_split(bank_path)
        if bank_path.exists():
            data = json.loads(bank_path.read_text(encoding="utf-8"))
        archive_data = load_archive(archive_path)
    except OSError:
        pass

    return merge_active_and_archive(data, archive_data)
