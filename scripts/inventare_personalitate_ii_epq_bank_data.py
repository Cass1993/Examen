"""Itemi — Inventare de personalitate II, seg. 2: Eysenck EPQ-R & IVE (60 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

EPQ_IVE_ITEMS: List[Item] = [
    {
        "stem": (
            "Modelul lui Eysenck descrie trei dimensiuni funcționale majore ale "
            "personalității: Nevrotism, Extraversiune și Psihoticism."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Scala P (Psihoticism) din EPQ măsoară direct simptomele unei "
            "psihoze diagnosticate clinic."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Scala L (Lie) poate reflecta conformism social sau tendința de a "
            "prezenta o imagine favorabilă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În studiile de fidelitate test-retest ale EPQ-R, Nevrotismul (N) "
            "este, de regulă, cel mai stabil."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Adaptarea românească a EPQ-R a fost realizată de Pitariu, Iliescu "
            "și Băban (2008)."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "IVE explică, în eșantionul românesc, peste 70% din varianța totală "
            "a răspunsurilor."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Autorii versiunii EPQ-R (1991) sunt:",
        "options": [
            "Hans Eysenck și Sybil Eysenck",
            "Costa și McCrae",
            "Cattell",
            "Gough",
        ],
        "correct": "a",
    },
    {
        "stem": "Forma standard EPQ-R conține:",
        "options": [
            "100 de itemi",
            "63 de itemi",
            "24 de itemi (EPQR-A)",
            "480 de itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Numărul de itemi al scalei Psihoticism (P) în EPQ-R este:",
        "options": [
            "32",
            "23",
            "24",
            "21",
        ],
        "correct": "a",
    },
    {
        "stem": "Numărul de itemi al scalei Extraversiune (E) în EPQ-R este:",
        "options": [
            "23",
            "32",
            "24",
            "21",
        ],
        "correct": "a",
    },
    {
        "stem": "Numărul de itemi al scalei Nevrotism (N) în EPQ-R este:",
        "options": [
            "24",
            "32",
            "23",
            "21",
        ],
        "correct": "a",
    },
    {
        "stem": "Numărul de itemi al scalei Lie (L) în EPQ-R este:",
        "options": [
            "21",
            "32",
            "24",
            "23",
        ],
        "correct": "a",
    },
    {
        "stem": "Versiunea EPQR-A conține, de regulă:",
        "options": [
            "24 itemi (câte 6 pe scară)",
            "100 itemi completi",
            "160 itemi",
            "54 itemi IVE",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe Psihoticism (P) sugerează, orientativ:",
        "options": [
            "agresivitate, nonconformism, tendințe antisociale",
            "calm emoțional și stabilitate",
            "sociabilitate crescută și optimism",
            "conformism social și fake good",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe Extraversiune (E) este asociat, tipic, cu:",
        "options": [
            "sociabilitate, impulsivitate, căutarea senzațiilor",
            "retragere, planificare, seriozitate",
            "anxietate și instabilitate emoțională",
            "minciună socială și conformism",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor scăzut pe Extraversiune (introversie) indică, de regulă:",
        "options": [
            "retragere socială, planificare, control emoțional",
            "căutarea senzațiilor și impulsivitate",
            "instabilitate emoțională marcată",
            "agresivitate și nonconformism",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor ridicat pe Nevrotism (N) este legat, tipic, de:",
        "options": [
            "anxietate, instabilitate emoțională, vulnerabilitate psihosomatică",
            "calm și reziliență emoțională",
            "sociabilitate și optimism",
            "empatie și altruism",
        ],
        "correct": "a",
    },
    {
        "stem": "Un scor scăzut pe Nevrotism indică, orientativ:",
        "options": [
            "stabilitate emoțională și calm",
            "anxietate și depresivitate",
            "agresivitate și risc antisocial",
            "căutarea senzațiilor periculoase",
        ],
        "correct": "a",
    },
    {
        "stem": "Scala L (Lie) din EPQ evaluează, în principal:",
        "options": [
            "conformism social / tendința de impresionare favorabilă",
            "agresivitate și nonconformism",
            "anxietate și instabilitate",
            "empatie față de ceilalți",
        ],
        "correct": "a",
    },
    {
        "stem": "Inventarul IVE conține, în forma completă:",
        "options": [
            "63 de itemi",
            "100 de itemi",
            "24 de itemi",
            "160 de itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Versiunea scurtă a IVE are:",
        "options": [
            "54 de itemi",
            "63 de itemi",
            "106 itemi",
            "32 itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Pe IVE, un scor ridicat la Impulsivitate indică:",
        "options": [
            "lipsă de autocontrol și tendință spre risc",
            "planificare riguroasă și prudență",
            "empatie accentuată",
            "conformism social",
        ],
        "correct": "a",
    },
    {
        "stem": "Pe IVE, un scor ridicat la Aventură (Venturesomeness) reflectă:",
        "options": [
            "căutarea senzațiilor și toleranța la risc",
            "evitarea situațiilor noi sau riscante",
            "instabilitate emoțională anxioasă",
            "retragere socială",
        ],
        "correct": "a",
    },
    {
        "stem": "Pe IVE, un scor ridicat la Empatie este asociat cu:",
        "options": [
            "sensibilitate față de ceilalți și altruism",
            "rece față de ceilalți și insensibilitate interpersonală",
            "agresivitate și nonconformism",
            "fake good pe scala L",
        ],
        "correct": "a",
    },
    {
        "stem": "EPQ poate fi administrat:",
        "options": [
            "individual sau în grup, inclusiv citit cu voce tare",
            "numai în cabinet, fără citire vocală",
            "numai online, fără prezența examinatorului",
            "numai ca test proiectiv nestandardizat",
        ],
        "correct": "a",
    },
    {
        "stem": "Eșantionul normativ britanic clasic pentru EPQ include, orientativ:",
        "options": [
            "408 bărbați și 494 femei, 16–70 ani",
            "2400 persoane din România",
            "100 studenți la psihologie",
            "doar adolescenți sub 16 ani",
        ],
        "correct": "a",
    },
    {
        "stem": "Eșantionul normativ românesc pentru EPQ include, orientativ:",
        "options": [
            "2400–3741 persoane, 12–69 ani, reprezentativ",
            "408 bărbați din UK",
            "sub 200 participanți conveniență",
            "exclusiv medici psihiatri",
        ],
        "correct": "a",
    },
    {
        "stem": "Studiile cross-culturale ale structurii EPQ au inclus, orientativ:",
        "options": [
            "34–51 de țări",
            "doar eșantionul britanic",
            "maximum 3 culturi",
            "exclusiv populația românească",
        ],
        "correct": "a",
    },
    {
        "stem": "Contribuția teoretică a lui Eysenck include:",
        "options": [
            "modelul tridimensional al personalității (N, E, P)",
            "scala L pentru evaluarea validității profilului",
            "tranziția conceptuală spre modele ca Big Five",
            "inventarul CPI al lui Gough",
        ],
        "correct": "ab",
    },
    {
        "stem": "Despre scala Psihoticism (P), care afirmații sunt corecte?",
        "options": [
            "reflectă agresivitate și nonconformism",
            "nu echivalează direct cu diagnostic psihiatric",
            "poate indica factor de risc pentru comportament antisocial",
            "măsoară în primul rând coeficientul de inteligență",
        ],
        "correct": "abc",
    },
    {
        "stem": "Versiunile EPQ includ, printre altele:",
        "options": [
            "forma lungă (~160 itemi)",
            "forma scurtă (~106 itemi)",
            "EPQR-A (24 itemi)",
            "EPQR-BV ca versiune proiectivă nestandardizată",
        ],
        "correct": "abc",
    },
    {
        "stem": "Interpretarea scalei L depinde, parțial, de context:",
        "options": [
            "în situații neutre poate reflecta trăsătură stabilă",
            "în selecție poate indica disimulare",
            "este identică cu scorul pe Psihoticism",
            "scor ridicat poate sugera fake good",
        ],
        "correct": "ab",
    },
    {
        "stem": "Comparativ cu normele UK, studiile românești raportează adesea:",
        "options": [
            "P mai ridicat la bărbați români",
            "E mai ridicat la români, în general",
            "N mai ridicat la femei române",
            "L mai scăzut la toate categoriile, fără excepție",
        ],
        "correct": "abc",
    },
    {
        "stem": "Scalele IVE Impulsivitate și Aventură se corelează, de regulă, semnificativ cu:",
        "options": [
            "Psihoticism (P)",
            "Extraversiune (E)",
            "Nevrotism (N) ca singur predictor",
            "Scala L ca măsură a empatiei",
        ],
        "correct": "ab",
    },
    {
        "stem": "IVE măsoară, în mod direct, trei dimensiuni:",
        "options": [
            "Impulsivitate",
            "Aventură (Venturesomeness)",
            "Empatie",
            "Psihoticism clinic",
        ],
        "correct": "abc",
    },
    {
        "stem": "Scorarea EPQ se poate realiza prin:",
        "options": [
            "corectare manuală cu chei",
            "software dedicat",
            "interpretare exclusiv intuitivă, fără barem",
            "transpunere directă în diagnostic DSM",
        ],
        "correct": "ab",
    },
    {
        "stem": "Studiile cross-culturale ale EPQ (34–51 țări) arată:",
        "options": [
            "congruență factorială foarte ridicată pentru N și E (~0,98)",
            "replicabilitate a structurii în contexte diverse",
            "absența totală a diferențelor culturale",
            "invalidarea scalei L în toate culturile",
        ],
        "correct": "ab",
    },
    {
        "stem": "Un profil cu P ridicat, E ridicat și N scăzut poate sugera, orientativ:",
        "options": [
            "sociabilitate combinată cu tendințe nonconformiste",
            "stabilitate emoțională relativ bună",
            "anxietate severă și retragere totală",
            "pattern care necesită interpretare contextuală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Structura factorială și fidelitatea EPQ-R includ, de regulă:",
        "options": [
            "4 factori confirmați: P, E, N, L",
            "Alpha Cronbach > 0,70 pentru majoritatea scalelor",
            "un singur factor general de inteligență",
            "N ca scală cu stabilitate test-retest relativ mare",
        ],
        "correct": "ab",
    },
    {
        "stem": "EPQ/EPQ-R poate fi utilizat de:",
        "options": [
            "psihologi acreditați",
            "medici și asistenți sociali calificați",
            "specialiști HR cu pregătire adecvată",
            "orice persoană fără instruire, fără restricții",
        ],
        "correct": "abc",
    },
    {
        "stem": "EPQ este aplicabil în context:",
        "options": [
            "educațional",
            "clinic",
            "organizațional",
            "exclusiv forensic, fără alte utilizări",
        ],
        "correct": "abc",
    },
    {
        "stem": "Eysenck este recunoscut pentru:",
        "options": [
            "rigoare metodologică în cercetarea personalității",
            "influență majoră asupra psihologiei personalității",
            "legătura cu evoluția spre modele Big Five",
            "crearea inventarului MMPI ca autor principal",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un profil cu N ridicat și E scăzut poate fi asociat, tipic, cu:",
        "options": [
            "anxietate și reactivitate emoțională",
            "retragere socială",
            "vulnerabilitate psihosomatică",
            "căutare activă a senzațiilor periculoase",
        ],
        "correct": "abc",
    },
    {
        "stem": "Despre fidelitatea EPQ-R, ce afirmații sunt corecte?",
        "options": [
            "Alpha Cronbach > 0,70 pentru majoritatea scalelor",
            "P poate avea fidelitate mai scăzută la unele grupe de femei",
            "test-retest indică stabilitate rezonabilă",
            "fidelitatea zero invalidă automat testul",
        ],
        "correct": "abc",
    },
    {
        "stem": "Structura factorială a IVE în România indică, de regulă:",
        "options": [
            "3 factori (Impulsivitate, Aventură, Empatie)",
            "aproximativ 26% din varianță explicată",
            "aceeași structură ca EPQ cu 4 factori P, E, N, L",
            "utilitate complementară față de EPQ",
        ],
        "correct": "ab",
    },
    {
        "stem": "Administrarea EPQ presupune, de regulă:",
        "options": [
            "instrucțiuni clare pentru răspuns Da/Nu",
            "posibilitatea administrării individuale sau de grup",
            "obligativitatea unui cabinet fără contact verbal",
            "posibilitatea citirii itemilor cu voce tare",
        ],
        "correct": "ab",
    },
    {
        "stem": "EPQ este utilizat în domenii precum:",
        "options": [
            "medical (comportament sănătate)",
            "judiciar/forensic",
            "cercetare științifică",
            "diagnostic formal al schizofreniei ca unic scop",
        ],
        "correct": "abc",
    },
    {
        "stem": "Comparativ, scoruri IVE scăzute la Empatie și ridicate la Impulsivitate pot sugera:",
        "options": [
            "tendință spre rece față de ceilalți",
            "lipsă de autocontrol",
            "altruism accentuat",
            "profil util în evaluarea riscului comportamental",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scară–descriere pentru scoruri ridicate sunt corecte?",
        "options": [
            "P — agresiv, dur, atras de neobișnuit",
            "E — sociabil, optimist, caută senzații",
            "N — calm, stabil, rezilient",
            "L — conformism / impresionare favorabilă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi scară–descriere pentru scoruri scăzute sunt corecte?",
        "options": [
            "E — introvert: retras, serios, planifică",
            "N — stabil emoțional: calm, controlat",
            "P — empatie accentuată și conformism",
            "Impulsivitate IVE — rațional, autocontrolat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Despre eșantioanele normative EPQ, ce afirmații sunt corecte?",
        "options": [
            "UK: ~408 M + 494 F, 16–70 ani",
            "RO: 2400–3741 persoane, 12–69 ani",
            "RO: eșantion reprezentativ",
            "UK: doar copii sub 12 ani",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care elemente descriu corect EPQ-R ca instrument?",
        "options": [
            "100 itemi: P=32, E=23, N=24, L=21",
            "autori: Eysenck & Eysenck (1991)",
            "adaptare RO: Pitariu, Iliescu, Băban (2008)",
            "format Adevărat/Fals, cu chei de scorare",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care afirmații despre diferențele culturale RO vs UK sunt corecte?",
        "options": [
            "P mai ridicat la bărbați români",
            "E mai ridicat la români, în general",
            "N mai ridicat la femei române",
            "identitate perfectă a profilurilor medii",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care scale IVE și EPQ se pot completa în evaluarea personalității?",
        "options": [
            "IVE: Impulsivitate, Aventură, Empatie",
            "EPQ: P, E, N, L",
            "IVE înlocuiește complet scala L",
            "Impulsivitate/Aventură corelează cu P și E",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care domenii de aplicare sunt documentate pentru EPQ/EPQ-R?",
        "options": [
            "educațional",
            "clinic și medical",
            "organizațional și HR",
            "judiciar/forensic și cercetare",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set rezumă corect psihometria EPQ-R?",
        "options": [
            "α > 0,70 pentru majoritatea scalelor",
            "N cel mai stabil la test-retest",
            "4 factori confirmați (P, E, N, L)",
            "congruență cross-culturală ~0,98 pentru N și E",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce afirmații despre IVE sunt corecte?",
        "options": [
            "63 itemi (versiune scurtă 54)",
            "3 factori: Impulsivitate, Aventură, Empatie",
            "~26% varianță explicată în eșantion RO",
            "măsoară direct diagnosticul psihotic",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care combinație sintetizează teoria și utilizarea Eysenck?",
        "options": [
            "N, E, P ca dimensiuni funcționale + L pentru validitate",
            "P ca factor de risc, nu diagnostic psihiatric direct",
            "influență majoră și rigoare metodologică",
            "EPQ creat de Gough pentru selecție organizațională",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set descrie complet administrarea și interpretarea EPQ?",
        "options": [
            "individual/grup; citire vocală permisă",
            "scorare manuală sau software",
            "interpretare contextuală a scalei L",
            "verificarea scalelor de validitate înainte de profil",
        ],
        "correct": "abcd",
    },
    {
        "stem": "La interpretarea unui profil EPQ, ce pași sunt recomandați?",
        "options": [
            "verificarea scalei L pentru validitate/disimulare",
            "integrarea scorurilor P, E, N în context clinic sau aplicat",
            "compararea cu norme relevante (vârstă, sex, cultură)",
            "diagnosticarea automată a tulburărililor psihotice din scorul P",
        ],
        "correct": "abc",
    },
]


def _count_dist(rows):
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


assert len(EPQ_IVE_ITEMS) == 60
assert _count_dist(EPQ_IVE_ITEMS) == {"1": 22, "2": 14, "3": 12, "4": 6, "TF": 6}
