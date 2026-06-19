"""One-shot: apply II rebalance, verify, sync, bump WORDING_VERSION."""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts._apply_ii_rebalance import SPECS, patch  # noqa: E402
from scripts._verify_ii_dist import FILES, classify, load_items  # noqa: E402

OUT = ROOT / "_rebalance_run_log.txt"


def dist_table() -> str:
    lines = [f"{'file':<16} {'tot':>4} {'1':>4} {'2':>4} {'3':>4} {'4':>4} {'TF':>4}  ok?"]
    lines.append("-" * 60)
    all_ok = True
    for label, path, var, total, target in FILES:
        items = load_items(path, var)
        counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
        for it in items:
            k = classify(it)
            if k in counts:
                counts[k] += 1
        t1, t2, t3, t4, ttf = target
        ok = (
            len(items) == total
            and counts["1"] == t1
            and counts["2"] == t2
            and counts["3"] == t3
            and counts["4"] == t4
            and counts["TF"] == ttf
            and counts["1"] > counts["2"] > counts["3"] > counts["4"]
        )
        if not ok:
            all_ok = False
        lines.append(
            f"{label:<16} {len(items):>4} {counts['1']:>4} {counts['2']:>4} "
            f"{counts['3']:>4} {counts['4']:>4} {counts['TF']:>4}  "
            f"{'OK' if ok else 'NO'} (tgt {t1}/{t2}/{t3}/{t4}/{ttf})"
        )
    lines.append("-" * 60)
    lines.append("ALL OK" if all_ok else "NEEDS REBALANCE")
    return "\n".join(lines)


def bump_wording_version() -> str:
    app = ROOT / "app.py"
    text = app.read_text(encoding="utf-8")
    m = re.search(r'WORDING_VERSION = "(\d+)"', text)
    if not m:
        return "WORDING_VERSION not found"
    old = m.group(1)
    if old == "151":
        return "WORDING_VERSION already 151 (skip)"
    new = "151" if old == "150" else str(int(old) + 1)
    text = text.replace(f'WORDING_VERSION = "{old}"', f'WORDING_VERSION = "{new}"', 1)
    app.write_text(text, encoding="utf-8")
    return f"WORDING_VERSION {old} -> {new}"


def main() -> None:
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    print("=== BEFORE ===")
    print(dist_table())
    print("\n=== APPLY ===")
    for rel, var, tgt, quads, skip in SPECS:
        patch(rel, var, tgt, quads, skip)
    print("\n=== AFTER ===")
    print(dist_table())
    print("\n=== SYNC ===")
    from scripts.sync_psihologia_dezvoltarii_ii_lot import main as sync_main

    sync_main()
    print("\n=== BUMP ===")
    print(bump_wording_version())
    from scripts.psihologia_dezvoltarii_ii_bank_data import PSIHOLOGIA_DEZVOLTARII_II_ITEMS

    print(f"\nassert len == 400: {len(PSIHOLOGIA_DEZVOLTARII_II_ITEMS)}")
    sys.stdout = old
    text = buf.getvalue()
    OUT.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote log to {OUT}")


if __name__ == "__main__":
    main()
