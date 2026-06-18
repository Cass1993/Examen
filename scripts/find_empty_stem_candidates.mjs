import { readFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const APP_DIR = dirname(dirname(fileURLToPath(import.meta.url)));
const DATA = JSON.parse(readFileSync(join(APP_DIR, "data", "questions.json"), "utf8"));

const needles = [
  "Stadiu psihosexual timpuriu centrat pe zona orală și hrănire",
  "Gândire simbolică, egocentrism cognitiv și dificultăți cu reversibilitatea",
  "Raționament moral orientat spre norme, aprobare socială și ordine",
  "Sprijin temporar retras treptat pe măsură ce elevul devine competent",
];

const hits = [];
const shortStems = [];
const mdRisk = [];

for (const [lot, lotData] of Object.entries(DATA.lots || {})) {
  for (const q of lotData.questions || []) {
    const stem = String(q.text || q.intrebare || "").trim();
    const opts = q.options || q.variante || {};
    const vals = Object.values(opts).map(String);

    if (needles.every((n) => vals.includes(n))) {
      hits.push({ id: q.id, lot, stem, opts });
    }
    if (!stem || stem.length < 3) {
      shortStems.push({ id: q.id, lot, stem: JSON.stringify(stem) });
    }
    if (/^[*_#`]/.test(stem) || /[^\\]\*/.test(stem)) {
      mdRisk.push({ id: q.id, lot, stem: stem.slice(0, 80) });
    }
  }
}

console.log("=== All 4 screenshot options ===");
console.log(JSON.stringify(hits, null, 2));
console.log("count", hits.length);

console.log("\n=== Empty/short stems in JSON ===");
console.log(JSON.stringify(shortStems.slice(0, 20), null, 2));
console.log("count", shortStems.length);

console.log("\n=== Markdown-risk stems (sample) ===");
console.log(JSON.stringify(mdRisk.slice(0, 15), null, 2));
console.log("count", mdRisk.length);
