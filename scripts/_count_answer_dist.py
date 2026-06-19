"""Analizează distribuția tipurilor de răspuns în segmentele lotului II."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = [
    "psihologia_dezvoltarii_ii_teorii_bank_data.py",
    "psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py",
    "psihologia_dezvoltarii_ii_limbaj_bank_data.py",
    "psihologia_dezvoltarii_ii_atasament_bank_data.py",
    "psihologia_dezvoltarii_ii_simbol_joc_bank_data.py",
    "psihologia_dezvoltarii_ii_scolaritate_bank_data.py",
    "psihologia_dezvoltarii_ii_adolescenta_bank_data.py",
    "psihologia_dezvoltarii_ii_tinereete_bank_data.py",
]

for name in FILES:
    path = ROOT / name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    c = Counter()
    tf = text.count('"tf": True')
    for m in re.finditer(r'"correct": "([a-d]+)"', text):
        c[len(m.group(1))] += 1
    total_mc = sum(c.values())
    print(f"\n{name} (TF={tf}, MC={total_mc})")
    for k in sorted(c):
        print(f"  {k} răspuns: {c[k]}")
