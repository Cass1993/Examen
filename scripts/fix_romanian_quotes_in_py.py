"""Înlocuiește ghilimelele românești închise greșit cu ASCII " în stringuri Python."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "_quote_fix_log.txt"


def fix_text(text: str) -> str:
    import importlib.util

    path = Path(__file__).resolve().parent / "_apply_quote_fix.py"
    spec = importlib.util.spec_from_file_location("_apply_quote_fix", path)
    if spec is None or spec.loader is None:
        raise ImportError("_apply_quote_fix.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.fix_text(text)


def main() -> int:
    import importlib.util

    path = Path(__file__).resolve().parent / "_apply_quote_fix.py"
    spec = importlib.util.spec_from_file_location("_apply_quote_fix", path)
    if spec is None or spec.loader is None:
        raise ImportError("_apply_quote_fix.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.main()


if __name__ == "__main__":
    raise SystemExit(main())
