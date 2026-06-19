"""Quick distribution counter - writes to _dist_report.txt"""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ("main", "scripts/psihologia_dezvoltarii_ii_bank_data.py", "PSIHOLOGIA_DEZVOLTARII_II_ITEMS", 50, (16, 12, 10, 3, 5)),
    ("metode", "scripts/psihologia_dezvoltarii_ii_metode_bank_data.py", "METODE_CERCETARE_ITEMS", 50, (16, 12, 10, 3, 5)),
    ("teorii", "scripts/psihologia_dezvoltarii_ii_teorii_bank_data.py", "TEORII_INVATARII_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("senzorio_motor", "scripts/psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py", "SENZORIO_MOTOR_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("limbaj", "scripts/psihologia_dezvoltarii_ii_limbaj_bank_data.py", "LIMBAJ_ITEMS", 30, (10, 8, 6, 3, 3)),
    ("atasament", "scripts/psihologia_dezvoltarii_ii_atasament_bank_data.py", "ATASAMENT_ITEMS", 30, (10, 8, 6, 3, 3)),
    ("simbol_joc", "scripts/psihologia_dezvoltarii_ii_simbol_joc_bank_data.py", "SIMBOL_JOC_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("scolaritate", "scripts/psihologia_dezvoltarii_ii_scolaritate_bank_data.py", "SCOLARITATE_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("adolescenta", "scripts/psihologia_dezvoltarii_ii_adolescenta_bank_data.py", "ADOLESCENTA_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("tinereete", "scripts/psihologia_dezvoltarii_ii_tinereete_bank_data.py", "TINERETE_ITEMS", 40, (14, 11, 8, 3, 4)),
]

def load(path, var):
    spec = importlib.util.spec_from_file_location("m", ROOT / path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)

def classify(it):
    if it.get("tf"):
        return "TF"
    c = (it.get("correct") or "").lower()
    n = len("".join(sorted(set(x for x in c if x in "abcd"))))
    return str(n)

lines = []
for label, path, var, total, tgt in FILES:
    items = load(path, var)
    c = {"1":0,"2":0,"3":0,"4":0,"TF":0}
    for it in items:
        k = classify(it)
        c[k] = c.get(k, 0) + 1
    t1,t2,t3,t4,ttf = tgt
    ok = len(items)==total and c["1"]==t1 and c["2"]==t2 and c["3"]==t3 and c["4"]==t4 and c["TF"]==ttf
    lines.append(f"{label}: tot={len(items)} 1={c['1']} 2={c['2']} 3={c['3']} 4={c['4']} TF={c['TF']} tgt={tgt} {'OK' if ok else 'NO'}")

(ROOT / "_dist_report.txt").write_text("\n".join(lines), encoding="utf-8")
