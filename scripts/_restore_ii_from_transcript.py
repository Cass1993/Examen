"""Restore II bank_data files from agent transcript (pre-rebalance state)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPT = Path(
    r"C:\Users\casia\.cursor\projects\1779881827047\agent-transcripts"
    r"\9c792901-f166-4bb7-8631-05405dc07911"
    r"\9c792901-f166-4bb7-8631-05405dc07911.jsonl"
)
OUT = ROOT / "scripts"
TARGETS = {
    "psihologia_dezvoltarii_ii_metode_bank_data.py": "metode",
    "psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py": "senzorio",
    "psihologia_dezvoltarii_ii_teorii_bank_data.py": "teorii",
}
REBALANCE_LINE = 2918  # first mention of _apply_ii_rebalance


def apply_str_replace(content: str, old: str, new: str) -> str:
    if old not in content:
        return content
    return content.replace(old, new, 1)


def main() -> int:
    if not TRANSCRIPT.exists():
        print("Transcript missing:", TRANSCRIPT)
        return 1

    files: dict[str, str] = {}
    line_no = 0
    for line in TRANSCRIPT.read_text(encoding="utf-8").splitlines():
        line_no += 1
        if line_no >= REBALANCE_LINE:
            break
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = obj.get("message", {})
        for part in msg.get("content", []):
            if part.get("type") != "tool_use":
                continue
            name = part.get("name")
            inp = part.get("input", {})
            path = str(inp.get("path", "")).replace("\\", "/")
            for fname in TARGETS:
                if not path.endswith(fname):
                    continue
                if name == "Write" and inp.get("contents"):
                    files[fname] = inp["contents"]
                elif name == "StrReplace" and fname in files:
                    old = inp.get("old_string")
                    new = inp.get("new_string")
                    if old is not None and new is not None:
                        files[fname] = apply_str_replace(files[fname], old, new)

    for fname, content in files.items():
        dest = OUT / fname
        dest.write_text(content, encoding="utf-8")
        abcd = len(re.findall(r'"correct": "abcd"', content))
        a_only = len(re.findall(r'"correct": "a"', content))
        print(f"Restored {fname}: {len(content)} chars, abcd={abcd}, a={a_only}")

    missing = set(TARGETS) - set(files)
    if missing:
        print("Missing restores:", missing)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
