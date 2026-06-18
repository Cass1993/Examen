"""Bancă itemi — Psihopatologie II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

ITEMS: List[Item] = []

from scripts.psihopatologie_ii_bipolar_items import BIPOLAR_ITEMS
from scripts.psihopatologie_ii_ptsd_items import PTSD_ITEMS
from scripts.psihopatologie_ii_suicid_items import SUICID_ITEMS
from scripts.psihopatologie_ii_toc_items import TOC_ITEMS
from scripts.psihopatologie_ii_anxietate_items import ANXIETATE_ITEMS
from scripts.psihopatologie_ii_personalitate_items import PERSONALITATE_ITEMS
from scripts.psihopatologie_ii_personalitate_extra_items import PERSONALITATE_EXTRA_ITEMS
from scripts.psihopatologie_ii_schizofrenie_depresie_items import SCHIZOFRENIE_DEPRESIE_ITEMS
from scripts.psihopatologie_ii_schizofrenie_depresie_extra_items import SCHIZOFRENIE_DEPRESIE_EXTRA_ITEMS

ITEMS.extend(BIPOLAR_ITEMS)
ITEMS.extend(PTSD_ITEMS)
ITEMS.extend(SUICID_ITEMS)
ITEMS.extend(TOC_ITEMS)
ITEMS.extend(ANXIETATE_ITEMS)
ITEMS.extend(PERSONALITATE_ITEMS)
ITEMS.extend(PERSONALITATE_EXTRA_ITEMS)
ITEMS.extend(SCHIZOFRENIE_DEPRESIE_ITEMS)
ITEMS.extend(SCHIZOFRENIE_DEPRESIE_EXTRA_ITEMS)
