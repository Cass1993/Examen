"""Itemi clar separați — genetică comportamentală și epigenetică."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.concept_clusters import ConceptSpec, rotate_options

# Perechi concept — definiție (asocieri omogene)
GENETICS_PAIRS: List[Tuple[str, str]] = [
    (
        "Modelul ACE",
        "separă variația trăsăturilor în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
    ),
    (
        "Studiile gemelare",
        "compară asemănarea gemenilor monozigoți și dizigoți pentru estimarea influențelor genetice și de mediu",
    ),
    (
        "Ereditabilitatea",
        "estimează proporția variației unei trăsături într-o populație atribuită diferențelor genetice",
    ),
    (
        "Epigenetica",
        "studiază modificări ale expresiei genelor fără schimbarea secvenței ADN",
    ),
    (
        "Metilarea ADN",
        "mecanism epigenetic care poate reduce sau modifica expresia unei gene",
    ),
    (
        "Studiile de adopție",
        "compară asemănarea dintre copii adoptați și părinții biologici versus cei adoptivi",
    ),
    (
        "Studiul de asociere la nivelul întregului genom (GWAS)",
        "caută asocieri între numeroase variante genetice și o trăsătură la nivel populational",
    ),
    (
        "Polimorfismul nucleotidic unic (SNP)",
        "variație la nivelul unui singur nucleotid în secvența ADN",
    ),
    (
        "Programarea epigenetică prin îngrijire maternă",
        "influența comportamentului matern asupra reglării stresului prin mecanisme epigenetice",
    ),
    (
        "Moștenirea epigenetică a fricii",
        "transmiterea unor efecte epigenetice ale experienței parentale asupra răspunsului la amenințare la urmași",
    ),
]

# Itemi rotație — înlocuiesc «Concepte genetice și epigenetice»
ROTATION_SPECS: List[ConceptSpec] = [
    {
        "stem": "Care afirmații descriu corect genetica comportamentală în studiul personalității?",
        "options": {
            "a": "studiile gemelare compară asemănarea gemenilor monozigoți și dizigoți",
            "b": "ereditabilitatea estimează contribuția diferențelor genetice la variația unei trăsături într-o populație",
            "c": "modelul ACE separă influențele genetice aditive, mediul comun și mediul neîmpărtășit",
            "d": "epigenetica studiază modificări ale expresiei genelor fără schimbarea secvenței ADN",
        },
        "correct": ["a", "b", "c", "d"],
        "kind": "multi",
    },
    {
        "stem": "În genetica comportamentală, modelul ACE este folosit pentru:",
        "options": {
            "a": "separarea variației trăsăturilor în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
            "b": "compararea asemănării gemenilor monozigoți și dizigoți fără estimarea mediului",
            "c": "măsurarea validității de criteriu a unui test de personalitate",
            "d": "descrierea stadiilor psihosociale ale dezvoltării umane",
        },
        "correct": "a",
    },
    {
        "stem": "În genetica comportamentală, studiile gemelare permit estimarea:",
        "options": {
            "a": "contribuției relative a factorilor genetici și de mediu prin compararea gemenilor monozigoți și dizigoți",
            "b": "influențelor genetice aditive, mediului comun și mediului neîmpărtășit fără date despre gemeni",
            "c": "modificării directe a secvenței ADN prin intervenții educaționale",
            "d": "nivelului de atașament securizant în relația părinte–copil",
        },
        "correct": "a",
    },
    {
        "stem": "Ereditabilitatea, în genetica comportamentală, exprimă:",
        "options": {
            "a": "proporția variației unei trăsături într-o populație atribuită diferențelor genetice",
            "b": "gradul în care un test măsoară constructul teoretic vizat",
            "c": "diferența dintre gemenii monozigoți și dizigoți pentru o trăsătură",
            "d": "modificări ale expresiei genelor fără schimbarea secvenței ADN",
        },
        "correct": "a",
    },
    {
        "stem": "Epigenetica se referă la:",
        "options": {
            "a": "modificări ale expresiei genelor fără schimbarea secvenței ADN",
            "b": "compararea asemănării gemenilor monozigoți și dizigoți",
            "c": "separarea variației în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
            "d": "proporția variației unei trăsături atribuită exclusiv mediului neîmpărtășit",
        },
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu corect aspecte ale geneticii comportamentale, fără epigenetică?",
        "options": {
            "a": "studiile gemelare compară asemănarea gemenilor monozigoți și dizigoți",
            "b": "ereditabilitatea estimează contribuția diferențelor genetice la variația unei trăsături",
            "c": "modelul ACE separă influențele genetice aditive, mediul comun și mediul neîmpărtășit",
            "d": "studiile de adopție compară asemănarea cu părinții biologici și adoptivi",
        },
        "correct": ["a", "b", "c", "d"],
        "kind": "multi",
    },
]

SINGLE_SPECS: Dict[str, ConceptSpec] = {
    "modelul ace": {
        "stem": "În genetica comportamentală, modelul ACE separă variația unei trăsături în:",
        "options": {
            "a": "influențe genetice aditive, mediu comun și mediu neîmpărtășit",
            "b": "gemeni monozigoți, gemeni dizigoți și eșantioane de adopție",
            "c": "validitate de criteriu, validitate de construct și fidelitate test-retest",
            "d": "extraversie, neuroticism, deschidere și agreabilitate",
        },
        "correct": "a",
        "aliases": ["model ace", "modelul eredității", "gene mediu comun mediu neîmpărtășit"],
    },
    "studiile gemelare": {
        "stem": "În genetica comportamentală, studiile gemelare sunt folosite mai ales pentru:",
        "options": {
            "a": "estimarea contribuției relative a factorilor genetici și de mediu la diferențele individuale",
            "b": "separarea directă a influențelor genetice aditive, mediului comun și mediului neîmpărtășit fără comparație între gemeni",
            "c": "modificarea expresiei genelor prin intervenții standardizate de învățare",
            "d": "evaluarea atașamentului prin procedura Situația stranie",
        },
        "correct": "a",
    },
    "ereditabilitatea": {
        "stem": "Ereditabilitatea, în genetica comportamentală, exprimă:",
        "options": {
            "a": "proporția variației unei trăsături într-o populație atribuită diferențelor genetice",
            "b": "gradul în care gemenii monozigoți sunt identici genetic în totalitate",
            "c": "relația dintre scorul unui test și un criteriu extern de performanță",
            "d": "modificări epigenetice transmise între generații fără schimbarea ADN-ului",
        },
        "correct": "a",
    },
    "epigenetica": {
        "stem": "Epigenetica se referă la:",
        "options": {
            "a": "modificări ale expresiei genelor fără schimbarea secvenței ADN",
            "b": "compararea asemănării gemenilor monozigoți și dizigoți",
            "c": "proporția variației unei trăsături atribuită diferențelor genetice",
            "d": "separarea variației în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
        },
        "correct": "a",
        "aliases": ["epigenetică", "programarea epigenetică"],
    },
    "gwas": {
        "stem": "Studiul de asociere la nivelul întregului genom (GWAS) presupune:",
        "options": {
            "a": "căutarea asocierilor între numeroase variante genetice și o trăsătură la nivel populational",
            "b": "compararea asemănării gemenilor monozigoți și dizigoți pentru o singură trăsătură",
            "c": "măsurarea proporției variației atribuită mediului neîmpărtășit",
            "d": "evaluarea dimensiunilor Big Five prin chestionar standardizat",
        },
        "correct": "a",
        "aliases": ["studiile de asociere", "genom-wide"],
    },
    "scorul poligenic": {
        "stem": "Scorul poligenic, în genetica comportamentală, se referă la:",
        "options": {
            "a": "sumă ponderată a mai multor variante genetice asociate probabilistic cu o trăsătură",
            "b": "separarea variației în influențe genetice aditive, mediu comun și mediu neîmpărtășit",
            "c": "relația dintre scorul unui test și un criteriu extern de performanță",
            "d": "compararea asemănării gemenilor monozigoți și dizigoți pentru o trăsătură",
        },
        "correct": "a",
        "aliases": ["scor poligenic", "poligenic score", "prs"],
    },
    "efectul poligenic": {
        "stem": "Efectul poligenic se referă la:",
        "options": {
            "a": "influența cumulată a multor variante genetice cu efecte mici asupra unei trăsături",
            "b": "proporția variației unei trăsături atribuită diferențelor genetice într-o populație",
            "c": "modificări ale expresiei genelor fără schimbarea secvenței ADN",
            "d": "compararea copiilor adoptați cu părinții biologici și adoptivi",
        },
        "correct": "a",
        "aliases": ["efect poligenic"],
    },
    "metilarea": {
        "stem": "Metilarea ADN este un mecanism epigenetic care:",
        "options": {
            "a": "poate reduce sau modifica expresia unei gene fără schimbarea secvenței ADN",
            "b": "estimează contribuția genetică și de mediu prin comparația gemenilor",
            "c": "măsoară validitatea de criteriu a unui instrument psihologic",
            "d": "descrie stadiile cognitive ale dezvoltării la copil",
        },
        "correct": "a",
        "aliases": ["metilarea adn", "metilarea acid dezoxiribonucleic"],
    },
}


def normalize_genetics_text(text: str) -> str:
    """Terminologie standard — mediu neîmpărtășit, fără «modelul modelul»."""
    if not text:
        return text
    out = str(text)
    replacements = [
        (
            r"Modelul\s+modelul\s+genetic\s+aditiv,\s*mediu\s+comun\s+și\s+mediu\s+(?:unic|necomun|neîmpărtășit)",
            "Modelul ACE",
        ),
        (r"\bmodelul\s+modelul\b", "modelul"),
        (r"\bModelul\s+modelul\b", "Modelul"),
        (r"\bmediu\s+unic\b", "mediu neîmpărtășit"),
        (r"\bmediu\s+necomun\b", "mediu neîmpărtășit"),
        (r"\bmediul\s+unic\b", "mediul neîmpărtășit"),
        (r"\bmediul\s+necomun\b", "mediul neîmpărtășit"),
        (r"modelul genetic aditiv,\s*mediu comun și mediu unic", 
         "influențe genetice aditive, mediu comun și mediu neîmpărtășit"),
        (r"Modelul genetic aditiv,\s*mediu comun și mediu unic",
         "influențe genetice aditive, mediu comun și mediu neîmpărtășit"),
        (r"\bModelul ACE\b", "modelul ACE"),
        (r"\bmodelul ACE\b", "modelul ACE"),
    ]
    for pat, repl in replacements:
        out = re.sub(pat, repl, out, flags=re.IGNORECASE)
    # titluri: Modelul ACE cu majusculă la început de propoziție
    out = re.sub(
        r"(^|[.!?]\s+)modelul ACE\b",
        lambda m: m.group(1) + "Modelul ACE",
        out,
    )
    return out


def pick_rotation_spec(seed: int) -> ConceptSpec:
    return ROTATION_SPECS[seed % len(ROTATION_SPECS)]


def lookup_single_spec(label: str) -> Optional[ConceptSpec]:
    key = re.sub(r"\s+", " ", (label or "").strip().lower())
    key = re.sub(r"\([^)]*\)", "", key).strip()
    for spec_key, spec in SINGLE_SPECS.items():
        if spec_key in key or key in spec_key:
            return spec
        for alias in spec.get("aliases", []):
            if alias in key or key in alias:
                return spec
    if "gemen" in key:
        return SINGLE_SPECS["studiile gemelare"]
    if "ace" in key or ("genetic" in key and "mediu comun" in key):
        return SINGLE_SPECS["modelul ace"]
    if "poligenic" in key:
        return SINGLE_SPECS["efectul poligenic" if "efect" in key else "scorul poligenic"]
    if "eritabil" in key:
        return SINGLE_SPECS["ereditabilitatea"]
    if "epigenet" in key or "metilare" in key:
        return SINGLE_SPECS["epigenetica"]
    if "gwas" in key or "asociere la nivelul întregului genom" in key:
        return SINGLE_SPECS["gwas"]
    return None


def build_from_spec(spec: ConceptSpec, seed: int) -> Tuple[str, Dict[str, str], List[str]]:
    if spec.get("kind") == "multi" or isinstance(spec.get("correct"), list):
        stem = spec["stem"]
        opts = dict(spec["options"])
        corr = [str(c).lower() for c in spec["correct"]]
        return stem, opts, corr
    stem, opts, letter = rotate_options(spec, seed)
    return stem, opts, [letter]
