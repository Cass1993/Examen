"""Verifica compilarea tuturor fisierelor de explicatii."""
from __future__ import annotations

import py_compile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "_compile_verify.log"
PATTERNS = (
    "scripts/psihoterapie_ii_expl_part*.py",
    "scripts/psihoterapie_ii_explanations.py",
    "scripts/pm_ii_explanations_part*.py",
    "scripts/psihopatologie_ii_expl_part*.py",
    "scripts/psihologia_dezvoltarii_ii_explanations.py",
)


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def main() -> int:
    _configure_stdio()
    paths = sorted(p for pat in PATTERNS for p in ROOT.glob(pat))
    failed: list[str] = []
    for path in paths:
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            failed.append(str(exc))

    if failed:
        LOG.write_text("\n\n".join(failed), encoding="utf-8")
        print("\n\n".join(failed))
        return 1

    LOG.write_text(f"OK - {len(paths)} files\n", encoding="utf-8")
    print(f"OK - {len(paths)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
