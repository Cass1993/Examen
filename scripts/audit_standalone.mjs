import { readFileSync, writeFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const APP_DIR = dirname(dirname(fileURLToPath(import.meta.url)));
const DATA = JSON.parse(readFileSync(join(APP_DIR, "data", "questions.json"), "utf8"));

const DOMAIN_SHORT_NAMES = {
  "Psihologia personalității": "psihologiei personalității",
  "Psihologia dezvoltării, educației și învățării": "psihologiei dezvoltării, educației și învățării",
  "Psihologia dezvoltării, învățării și educației": "psihologiei dezvoltării, învățării și educației",
  "Metodologie și evaluare psihologică": "metodologiei și evaluării psihologice",
  "Metodologia cercetării psihologice și evaluare psihologică": "metodologiei cercetării și evaluării psihologice",
  "Statistică": "statisticii aplicate în psihologie",
  "Psihologia organizațională și a muncii": "psihologiei organizaționale și a muncii",
  "Psihopatologie": "psihopatologiei",
};
const ORPHAN_DOMAIN_EXPLANATION = "Răspunsurile corecte aparțin domeniului indicat";
const DOMAIN_FILTER_RE = /^Care dintre următoarele(?: concepte sau teme| teme)? aparțin (?:domeniului|explicit) «(.+?)»(?: în tematica de examen)?\?\s*$/i;
const STEM_LABEL_RE = /«([^»]+)»/;
const PLURAL_SUFFIX_RE = /(?:ele|ile|ii|uri|ăți|ori|atele|urile)$/i;
const VERB_PLURAL_AFTER_LABEL = [" descrie:", " descrie mai ales:", " este:", " este caracterizată prin:", " este utilizat pentru:", " presupune:"];
const AUTHOR_OPTION_RE = /^[A-ZĂÂÎȘȚ][A-Za-zĂÂÎȘȚăâîșț.\s\-]+ — .+$/;
const AUTHOR_IN_OPTION_RE = /^[A-ZĂÂÎȘȚ][^.]+ — .+$|^(Autor|Autoare)\s/i;
const AUTHOR_DESC_RE = /^(Autor|Autoare)\s+(asociat|asociată)/i;
const AUTHOR_NAME_RE = /^[A-ZĂÂÎȘȚ]\.\s*(?:[A-ZĂÂÎȘȚ]\.\s*)?[A-ZĂÂÎȘȚÀ-Ž][a-zăâîșțà-ž\-]+(?:\s+în\s+.+)?$/;
const DEFINITION_START_RE = /^(variabila|setul|procedura|proces|tip |categorie|tulburare|măsura|indicator|ipoteza|analiza|scala|statistica|comportament|relația|gradul|posibilitatea|influența|adăugarea|proporția|subgrupul|grupul|valoarea|eroarea|nivelul|autor asociat|autoare asociată|perspectivă|abordare|stare|episod|pattern)/i;
const AUTHOR_STEM_PATTERNS = [
  /^Care variantă descrie cel mai bine contribuția teoretică a lui\s+.+?\?\s*$/i,
  /^Contribuția teoretică asociată lui\s+.+?\s+este:\s*$/i,
  /^În .+, .+ este (?:asociat|asociată|formulat|formulată) (?:cu|de):\s*$/i,
  /^În .+, .+ este legat(?:ă)? (?:de|mai ales de):\s*$/i,
  /^În .+, .+ este formulat(?:ă)? (?:de|de:)\s*$/i,
];
const STOPWORDS = new Set("a al ale ai au ca care cel cei cea ce cu de din doar este fi fie iar in în la le li lui mai ne nu o or pe pentru prin sa sau se si și sub sunt un una unui unor the and or of in to for".split(" "));
const FORM_AUTHOR = "author", FORM_TERM = "term", FORM_DEFINITION = "definition";

function norm(s) { return (s || "").trim().toLowerCase().replace(/\s+/g, " "); }
function trimLabel(label) {
  let t = (label || "").trim();
  for (const sep of [" — ", " – "]) if (t.includes(sep)) t = t.split(sep)[0].trim();
  return t;
}
function labelsEquivalent(label, domain) {
  if (!label || !domain) return false;
  const a = norm(trimLabel(label)), b = norm(domain);
  if (a === b) return true;
  const short = DOMAIN_SHORT_NAMES[domain] || "";
  if (short && a === norm(short)) return true;
  return a === norm(trimLabel(domain));
}
function classifyOptionForm(text) {
  const t = (text || "").trim();
  if (!t) return FORM_TERM;
  if (AUTHOR_DESC_RE.test(t)) return FORM_DEFINITION;
  if (AUTHOR_OPTION_RE.test(t) || AUTHOR_IN_OPTION_RE.test(t)) return FORM_AUTHOR;
  if (AUTHOR_NAME_RE.test(t)) return FORM_AUTHOR;
  if (t[0] === t[0].toLowerCase() || t.length > 58 || DEFINITION_START_RE.test(t)) return FORM_DEFINITION;
  const words = t.split(/\s+/);
  if (words.length <= 7 && !t.endsWith(".")) return FORM_TERM;
  return FORM_DEFINITION;
}
function isPluralLabel(label) {
  let t = (label || "").trim().replace(/«|»/g, "");
  t = t.split("—")[0].split("–")[0].split("(")[0].trim();
  if (!t) return false;
  const low = t.toLowerCase();
  if (PLURAL_SUFFIX_RE.test(low)) return true;
  if (/\b(?:normele|scalele|tulburările|itemii|testele|tipuri|teorii|stadii|stiluri|metodele|procedurile|variabile)\b/i.test(low)) return true;
  return false;
}
function hasPluralSingularMismatch(stem) {
  if (!stem) return false;
  const m = STEM_LABEL_RE.exec(stem);
  if (m) {
    if (isPluralLabel(m[1])) {
      const low = stem.toLowerCase();
      for (const singular of VERB_PLURAL_AFTER_LABEL) if (low.includes(singular.trim())) return true;
    }
    return false;
  }
  if (/\b(?:normele|scalele|tulburările|itemii|testele|stadii|teorii|tipuri|stiluri|variabile|metodele|procedurile)\b/i.test(stem)) {
    const low = stem.toLowerCase();
    for (const singular of VERB_PLURAL_AFTER_LABEL) if (low.includes(singular.trim())) return true;
  }
  return false;
}
function isDomainFilterItem(item) {
  const stem = (item.intrebare || item.text || "").trim();
  return DOMAIN_FILTER_RE.test(stem);
}
function isOrphanDomainItem(item, lot) {
  const expl = item.explicatie || item.explanation || "";
  if (expl.includes(ORPHAN_DOMAIN_EXPLANATION)) return true;
  const stem = (item.intrebare || item.text || "").trim();
  const domain = (item.domeniu || item.lot || lot || "").trim();
  if (!stem || !domain) return false;
  const m = /«([^»]+)»/.exec(stem);
  if (!m || !labelsEquivalent(m[1], domain)) return false;
  const kind = (item.kind || item.tip || "").toLowerCase();
  const correct = item.raspuns_corect || item.correct || [];
  return kind === "multi" || kind === "multiple" || correct.length > 1;
}
function isAuthorStem(stem, item) {
  for (const pat of AUTHOR_STEM_PATTERNS) if (pat.test(stem)) return true;
  const opts = item.variante || item.options || {};
  const correct = (item.correct || item.raspuns_corect || []).map((c) => String(c).toLowerCase());
  const authorOpts = correct.filter((c) => opts[c] && classifyOptionForm(String(opts[c])) === FORM_AUTHOR).length;
  if (authorOpts && authorOpts === correct.length) {
    const low = stem.toLowerCase();
    if (["asociat", "asociată", "legat de", "legată de", "formulat de", "formulată de", "contribuția", "autor"].some((k) => low.includes(k))) return true;
  }
  return false;
}
function tokenize(text) {
  return new Set((norm(text).match(/[a-zăâîșț0-9]+/g) || []).filter((w) => w.length > 2 && !STOPWORDS.has(w)));
}
function wordOverlapRatio(a, b) {
  const ta = tokenize(a), tb = tokenize(b);
  if (!ta.size || !tb.size) return 0;
  let inter = 0;
  for (const w of ta) if (tb.has(w)) inter++;
  const smaller = Math.min(ta.size, tb.size);
  return smaller ? inter / smaller : 0;
}
function walkItems(data) {
  const out = [];
  if (data.lots) {
    for (const [lot, lotData] of Object.entries(data.lots)) {
      for (const q of lotData.questions || []) out.push([lot, q]);
    }
  } else if (Array.isArray(data)) {
    for (const q of data) out.push([q.domeniu || q.lot || "General", q]);
  }
  return out;
}
function itemId(item, lot) {
  const iid = item.id ?? item.id_local ?? "?";
  return lot ? `${lot}#${iid}` : String(iid);
}

const items = walkItems(DATA);
const cats = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [] };
for (const [lot, item] of items) {
  const iid = itemId(item, lot);
  const stem = (item.intrebare || item.text || "").trim();
  const opts = item.variante || item.options || {};
  const texts = Object.values(opts).map((v) => norm(v)).filter(Boolean);
  if (texts.length !== new Set(texts).size) cats[1].push(iid);
  if (hasPluralSingularMismatch(stem)) cats[2].push(iid);
  if (isOrphanDomainItem(item, lot)) cats[3].push(iid);
  if (isDomainFilterItem(item)) cats[4].push(iid);
  const forms = new Set(Object.values(opts).map((v) => classifyOptionForm(String(v))));
  if (forms.size > 1) cats[5].push(iid);
  if (isAuthorStem(stem, item) && Object.values(opts).some((v) => classifyOptionForm(String(v)) !== FORM_AUTHOR)) cats[6].push(iid);
  const entries = Object.entries(opts).filter(([, v]) => (v || "").trim());
  let similar = false;
  for (let i = 0; i < entries.length && !similar; i++)
    for (let j = i + 1; j < entries.length; j++) {
      const t1 = String(entries[i][1]).trim(), t2 = String(entries[j][1]).trim();
      if (norm(t1) === norm(t2)) continue;
      if (wordOverlapRatio(t1, t2) >= 0.8) { similar = true; break; }
    }
  if (similar) cats[7].push(iid);
}

const result = {
  path: join(APP_DIR, "data", "questions.json"),
  total_items: items.length,
  categories: {
    "1_duplicate_options": { count: cats[1].length, examples: cats[1].slice(0, 3) },
    "2_plural_singular_grammar": { count: cats[2].length, examples: cats[2].slice(0, 3) },
    "3_orphan_domain": { count: cats[3].length, examples: cats[3].slice(0, 3) },
    "4_domain_filter_stems": { count: cats[4].length, examples: cats[4].slice(0, 3) },
    "5_heterogeneous_options": { count: cats[5].length, examples: cats[5].slice(0, 3) },
    "6_author_stem_non_author_opts": { count: cats[6].length, examples: cats[6].slice(0, 3) },
    "7_similar_options_80pct": { count: cats[7].length, examples: cats[7].slice(0, 3) },
  },
  ids: {
    "1_duplicate_options": cats[1],
    "2_plural_singular_grammar": cats[2],
    "3_orphan_domain": cats[3],
    "4_domain_filter_stems": cats[4],
    "5_heterogeneous_options": cats[5],
    "6_author_stem_non_author_opts": cats[6],
    "7_similar_options_80pct": cats[7],
  },
};

const outJson = join(APP_DIR, "data", "audit_item_quality_report.json");
writeFileSync(outJson, JSON.stringify(result, null, 2), "utf8");

let stdout = "=".repeat(72) + "\nAUDIT CALITATE ITEMI\n" + "=".repeat(72) + `\nTotal: ${items.length}\n\n`;
const labels = {
  1: "1. Duplicate option texts (normalized, same item)",
  2: "2. Plural label + singular verb",
  3: "3. Orphan domain items",
  4: "4. Domain filter stems still present",
  5: "5. Heterogeneous options",
  6: "6. Author stem with non-author options",
  7: "7. Very similar option pairs (>80% word overlap)",
};
for (const k of [1, 2, 3, 4, 5, 6, 7]) {
  stdout += `${labels[k]}\n  Count: ${cats[k].length}\n  Examples: ${cats[k].slice(0, 3).join(", ") || "(none)"}\n\n`;
}
writeFileSync(join(APP_DIR, "data", "audit_stdout.txt"), stdout, "utf8");
console.log(stdout);
console.log(`JSON report: ${outJson}`);
