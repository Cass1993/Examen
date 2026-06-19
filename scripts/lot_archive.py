"""Separare loturi examen II (active) vs loturi vechi (arhivă)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Tuple

from scripts.supplemental_lots import II_LOT_NAMES

ARCHIVE_JSON_NAME = "questions_archive.json"


def is_ii_lot(lot_name: str) -> bool:
    """Loturile cu „II” în denumire rămân în selecția principală."""
    return lot_name in II_LOT_NAMES


def archive_path_for(bank_path: Path) -> Path:
    return bank_path.parent / ARCHIVE_JSON_NAME


def split_lots(lots: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    active: Dict[str, Any] = {}
    archived: Dict[str, Any] = {}
    for name, content in lots.items():
        if is_ii_lot(name):
            active[name] = content
        else:
            archived[name] = content
    return active, archived


def _total_questions(lots: Dict[str, Any]) -> int:
    return sum(len(block.get("questions") or []) for block in lots.values())


def load_archive(archive_path: Path) -> Dict[str, Any]:
    if not archive_path.exists():
        return {"lots": {}}
    return json.loads(archive_path.read_text(encoding="utf-8"))


def merge_active_and_archive(
    active_data: Dict[str, Any], archive_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Unește loturile active cu cele arhivate (pentru încărcare completă)."""
    merged = dict(active_data.get("lots") or {})
    for name, content in (archive_data.get("lots") or {}).items():
        merged.setdefault(name, content)
    out = dict(active_data)
    out["lots"] = merged
    out["total_questions"] = _total_questions(merged)
    return out


def ensure_archive_split(bank_path: Path) -> bool:
    """
    Mută loturile non-II din questions.json în questions_archive.json.
    Returnează True dacă a scris ceva.
    """
    if not bank_path.exists():
        return False

    data = json.loads(bank_path.read_text(encoding="utf-8"))
    lots = data.get("lots") or {}
    active, archived = split_lots(lots)
    if not archived:
        return False

    archive_path = archive_path_for(bank_path)
    archive_data = load_archive(archive_path)
    archive_lots = dict(archive_data.get("lots") or {})
    archive_lots.update(archived)

    active_data = dict(data)
    active_data["lots"] = active
    active_data["total_questions"] = _total_questions(active)
    active_data["active_lots_only"] = True

    archive_out = {
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "lots": archive_lots,
        "total_questions": _total_questions(archive_lots),
    }

    bank_path.parent.mkdir(parents=True, exist_ok=True)
    bank_path.write_text(
        json.dumps(active_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    archive_path.write_text(
        json.dumps(archive_out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return True


def write_lot_to_store(
    lot_name: str,
    items: list,
    bank_path: Path,
) -> None:
    """Scrie un lot supplemental în questions.json (II) sau arhivă (non-II)."""
    target_path = bank_path if is_ii_lot(lot_name) else archive_path_for(bank_path)
    if target_path.exists():
        data = json.loads(target_path.read_text(encoding="utf-8"))
    else:
        data = {"lots": {}}
    lots = data.setdefault("lots", {})
    lots[lot_name] = {"questions": items}
    data["total_questions"] = _total_questions(lots)
    if not is_ii_lot(lot_name):
        data["archived_at"] = datetime.now(timezone.utc).isoformat()
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
