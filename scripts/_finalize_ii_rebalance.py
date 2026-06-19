"""Patch remaining II bank files and run verify + sync."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._apply_ii_rebalance import patch  # noqa: E402
from scripts._verify_ii_dist import main as verify_main  # noqa: E402

REMAINING = [
    ("scripts/psihologia_dezvoltarii_ii_atasament_bank_data.py", "ATASAMENT_ITEMS", (10, 8, 6, 3, 3), [6, 14, 25]),
    ("scripts/psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py", "SENZORIO_MOTOR_ITEMS", (14, 11, 8, 3, 4), [0, 11, 37]),
    ("scripts/psihologia_dezvoltarii_ii_teorii_bank_data.py", "TEORII_INVATARII_ITEMS", (14, 11, 8, 3, 4), [0, 4, 36]),
    ("scripts/psihologia_dezvoltarii_ii_metode_bank_data.py", "METODE_CERCETARE_ITEMS", (17, 13, 11, 4, 5), [19, 38, 47]),
    ("scripts/psihologia_dezvoltarii_ii_bank_data.py", "PSIHOLOGIA_DEZVOLTARII_II_ITEMS", (17, 13, 11, 4, 5), [1, 7, 44]),
]

OUT = ROOT / "_finalize_log.txt"


def bump_wording() -> str:
    app = ROOT / "app.py"
    text = app.read_text(encoding="utf-8")
    m = re.search(r'WORDING_VERSION = "(\d+)"', text)
    if not m:
        return "no WORDING_VERSION"
    old, new = m.group(1), str(int(m.group(1)) + 1)
    app.write_text(text.replace(f'WORDING_VERSION = "{old}"', f'WORDING_VERSION = "{new}"', 1), encoding="utf-8")
    return f"{old} -> {new}"


def main() -> None:
    lines = ["=== PATCH ==="]
    for rel, var, tgt, quads in REMAINING:
        patch(rel, var, tgt, quads, False)
        lines.append(f"patched {rel}")
    lines.append("\n=== VERIFY ===")
    import io
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    verify_main()
    sys.stdout = old
    lines.append(buf.getvalue())
    lines.append("\n=== SYNC ===")
    from scripts.sync_psihologia_dezvoltarii_ii_lot import main as sync_main
    sync_main()
    lines.append("\n=== BUMP ===")
    lines.append(bump_wording())
    from scripts.psihologia_dezvoltarii_ii_bank_data import PSIHOLOGIA_DEZVOLTARII_II_ITEMS
    lines.append(f"len={len(PSIHOLOGIA_DEZVOLTARII_II_ITEMS)}")
    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
