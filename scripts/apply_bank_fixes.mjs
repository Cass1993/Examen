import { readFileSync, writeFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { spawnSync } from "child_process";

const APP = dirname(dirname(fileURLToPath(import.meta.url)));
const BANK = join(APP, "data", "questions.json");
const MARKER = join(APP, "data", ".bank_fix_37");

if (existsSync(MARKER)) {
  console.log("Bank fix v37 already applied.");
  process.exit(0);
}

const py = spawnSync("python", [join(APP, "scripts", "apply_all_bank_fixes.py")], {
  encoding: "utf-8",
  cwd: APP,
});

console.log(py.stdout || "");
console.error(py.stderr || "");
if (py.status === 0) {
  process.exit(0);
}

// Fallback: fix known CAPS flashcard items directly in JSON
const data = JSON.parse(readFileSync(BANK, "utf-8"));
const CAPS_SPECS = [
  {
    text: "În modelul CAPS al lui Walter Mischel, unitățile cognitiv-afective reprezintă:",
    options: {
      a: "construcții psihologice (cogniții, afecte, obiective) care organizează comportamentul",
      b: "dimensiuni stabile ale personalității măsurate prin chestionare tip Big Five",
      c: "erori de măsurare apărute la transformarea scorurilor brute în norme",
      d: "proceduri standardizate de administrare și interpretare a testelor",
    },
    correct: ["a"],
  },
  {
    text: "În modelul CAPS, patternurile dacă–atunci descriu:",
    options: {
      a: "regularități comportamentale activate de anumite situații sau stimuli",
      b: "relații cauzale demonstrate prin manipularea experimentală a variabilelor",
      c: "asocieri statistice observate fără controlul variabilelor confuze",
      d: "trăsături trans-situaționale independente de contextul social",
    },
    correct: ["a"],
  },
  {
    text: "Modelul CAPS (cognitiv-afectiv al personalității) al lui Walter Mischel descrie personalitatea ca:",
    options: {
      a: "sistem dinamic de construcții cognitive-afective activate în interacțiune cu situația",
      b: "set fix de trăsături care determină comportamentul indiferent de context",
      c: "rezultat exclusiv al condiționării operante a răspunsurilor",
      d: "produs al normelor standardizate aplicate scorurilor brute",
    },
    correct: ["a"],
  },
];

const BAD_STEM =
  "Care concept corespunde descrierii: Concepte teoria sistemului cognitiv-afectiv al personalității?";
let n = 0;
for (const lot of Object.values(data.lots || {})) {
  for (const q of lot.questions || []) {
    if (q.text === BAD_STEM) {
      const spec = CAPS_SPECS[n % CAPS_SPECS.length];
      q.text = spec.text;
      q.options = { ...spec.options };
      q.correct = [...spec.correct];
      q.kind = "single";
      n++;
    }
  }
}

writeFileSync(BANK, JSON.stringify(data, null, 2), "utf-8");
writeFileSync(MARKER, String(n), "utf-8");
console.log(`Fallback fix: ${n} CAPS items rescrise.`);
