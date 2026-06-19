"""Rescrie sursele explicațiilor Psihologia dezvoltării II — fără litere a/b/c/d."""

from __future__ import annotations

import ast
import importlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.explanation_prose import to_prose_explanation  # noqa: E402

SEGMENTS: list[tuple[str, str]] = [
    ("scripts.psihologia_dezvoltarii_ii_metode_explanations", "METODE_CERCETARE_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_teorii_explanations", "TEORII_INVATARII_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_senzorio_motor_explanations", "SENZORIO_MOTOR_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_limbaj_explanations", "LIMBAJ_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_atasament_explanations", "ATASAMENT_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_simbol_joc_explanations", "SIMBOL_JOC_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_scolaritate_explanations", "SCOLARITATE_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_adolescenta_explanations", "ADOLESCENTA_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_tinereete_explanations", "TINERETE_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_batranete_explanations", "BATRANETE_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_durere_explanations", "DURERE_EXPLANATIONS"),
    ("scripts.psihologia_dezvoltarii_ii_autori_explanations", "AUTORI_CLASICI_EXPLANATIONS"),
]


def _path(mod: str) -> Path:
    return ROOT / (mod.replace(".", "/") + ".py")


def _fmt(s: str) -> str:
    esc = s.replace("\\", "\\\\").replace('"', '\\"')
    if len(s) > 72:
        return f'    (\n        "{esc}"\n    )'
    return f'    "{esc}"'


def _replace_list(source: str, name: str, values: list[str]) -> str:
    pat = re.compile(rf"({re.escape(name)}\s*:\s*List\[str\]\s*=\s*\[|{re.escape(name)}\s*=\s*\[)")
    m = pat.search(source)
    if not m:
        raise ValueError(f"List {name} not found")
    start = m.end()
    depth = 1
    i = start
    while i < len(source) and depth:
        if source[i] == "[":
            depth += 1
        elif source[i] == "]":
            depth -= 1
        i += 1
    body = ",\n".join(_fmt(v) for v in values)
    return source[: m.start()] + m.group(1) + "\n" + body + "\n]" + source[i:]


def _rewrite_fundamente() -> int:
    path = _path("scripts.psihologia_dezvoltarii_ii_explanations")
    src = path.read_text(encoding="utf-8")
    m = re.search(
        r"PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS:\s*List\[str\]\s*=\s*\[",
        src,
    )
    if not m:
        raise ValueError("fundamente list missing")
    start = m.end()
    depth = 1
    i = start
    while i < len(src) and depth:
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
        i += 1
    block = src[m.start() : i]
    old = ast.literal_eval(block.split("=", 1)[1].strip())
    new = [to_prose_explanation(x) for x in old]
    changed = sum(a != b for a, b in zip(old, new))
    out = _replace_list(src, "PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS: List[str]", new)
    path.write_text(out, encoding="utf-8")
    print(f"fundamente: {changed}/{len(old)}")
    return changed


def _rewrite_segment(mod: str, name: str) -> int:
    path = _path(mod)
    mod_obj = importlib.import_module(mod)
    old = list(getattr(mod_obj, name))
    new = [to_prose_explanation(x) for x in old]
    changed = sum(a != b for a, b in zip(old, new))
    src = path.read_text(encoding="utf-8")
    out = _replace_list(src, name, new)
    path.write_text(out, encoding="utf-8")
    print(f"{path.name}: {changed}/{len(old)}")
    return changed


def main() -> int:
    total = _rewrite_fundamente()
    for mod, name in SEGMENTS:
        importlib.invalidate_caches()
        total += _rewrite_segment(mod, name)
    print(f"TOTAL {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
