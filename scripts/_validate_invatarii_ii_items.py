"""Verifică consistența itemilor Psihologia învățării II (10501–10960)."""



from __future__ import annotations



import json

import re

import sys

from pathlib import Path



ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:

    sys.path.insert(0, str(ROOT))



from scripts.psihologia_invatarii_ii_exam_items import LOT_NAME, START_ID, build_items  # noqa: E402

from scripts.psihologia_invatarii_ii_explanations import explanation_for_exam_id  # noqa: E402

from scripts.invatarii_ii_stem_audit import audit_option_text, audit_options_spoonfeed, audit_stem  # noqa: E402



LETTER_MARKERS = re.compile(

    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",

    re.IGNORECASE,

)





def main() -> int:

    built = build_items()

    data = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))

    json_lot = data.get("lots", {}).get(LOT_NAME, {}).get("questions") or []

    json_by_id = {int(q["id"]): q for q in json_lot}

    issues: list[str] = []



    expected_n = 460

    if len(built) != expected_n:

        issues.append(f"build_items: așteptat {expected_n}, primit {len(built)}")

    if len(json_lot) != expected_n:

        issues.append(f"questions.json: așteptat {expected_n}, primit {len(json_lot)}")



    for q in built:

        qid = int(q["id"])

        if not (10501 <= qid <= 10960):

            issues.append(f"{qid}: ID în afara intervalului 10501–10960")

        stem = str(q.get("text") or "").strip()

        if not stem:

            issues.append(f"{qid}: enunț gol")

        opts = q.get("options") or {}

        opt_texts = [str(v) for v in opts.values()] if isinstance(opts, dict) else []

        if not q.get("options") and not q.get("tf"):

            issues.append(f"{qid}: fără opțiuni")

        if not q.get("correct") and not q.get("tf"):

            issues.append(f"{qid}: fără barem")

        expl = str(q.get("explanation") or "").strip()

        if not expl:

            issues.append(f"{qid}: fără explicație în build_items")

        if LETTER_MARKERS.search(expl):

            issues.append(f"{qid}: explicație cu marcaje a/b/c/d")

        if not explanation_for_exam_id(qid).strip():

            issues.append(f"{qid}: explanation_for_exam_id gol")



        for issue in audit_stem(stem, opt_texts):

                issues.append(f"{qid}: [{issue.rule}] {issue.message} — «{stem[:90]}»")

        correct_key = str(q.get("correct") or "")
        if opt_texts and correct_key and not q.get("tf"):
            for issue in audit_options_spoonfeed(opt_texts, correct_key):
                issues.append(f"{qid}: [{issue.rule}] {issue.message}")



        for opt in opt_texts:

            for issue in audit_option_text(opt):

                issues.append(

                    f"{qid}: [{issue.rule}] {issue.message} în variantă — «{opt[:70]}…»"

                )



        jq = json_by_id.get(qid)

        if jq:

            json_stem = str(jq.get("text") or "").strip()

            if json_stem and json_stem != stem:

                issues.append(

                    f"{qid}: questions.json NEsincronizat — rulează sync_psihologia_invatarii_ii_lot.py"

                )

                issues.append(f"      cod: «{stem[:85]}…»")

                issues.append(f"      json: «{json_stem[:85]}…»")



    json_ids = sorted(int(q["id"]) for q in json_lot)

    expected_ids = list(range(START_ID, START_ID + expected_n))

    if json_ids != expected_ids:

        missing = set(expected_ids) - set(json_ids)

        extra = set(json_ids) - set(expected_ids)

        if missing:

            issues.append(f"JSON lipsesc ID-uri: {sorted(missing)[:10]}")

        if extra:

            issues.append(f"JSON ID-uri în plus: {sorted(extra)[:10]}")



    if not issues:

        with_expl = sum(1 for q in built if str(q.get("explanation") or "").strip())

        print(f"OK: {len(built)} itemi ({START_ID}–{START_ID + len(built) - 1})")

        print(f"JSON sincronizat: {len(json_lot)} itemi, explicații: {with_expl}/{expected_n}")

        print("Audit enunțuri: 0 probleme")

        return 0



    print(f"Probleme ({len(issues)}):")

    for line in issues[:100]:

        print(f"  - {line}")

    if len(issues) > 100:

        print(f"  ... și încă {len(issues) - 100}")

    return 1





if __name__ == "__main__":

    raise SystemExit(main())


