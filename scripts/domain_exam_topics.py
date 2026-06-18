"""Expansiuni tematice pentru itemi de domeniu — formulări de examen, nu filtre evidente."""

from __future__ import annotations

import re
from typing import Dict, Optional

DOMAIN_EXAM_STEM = (
    "Care dintre următoarele teme aparțin explicit «{domain}» în tematica de examen?"
)

DOMAIN_SHORT_NAMES: Dict[str, str] = {
    "Psihologia personalității": "psihologiei personalității",
    "Psihologia dezvoltării, educației și învățării": "psihologiei dezvoltării, educației și învățării",
    "Psihologia dezvoltării, învățării și educației": "psihologiei dezvoltării, învățării și educației",
    "Metodologie și evaluare psihologică": "metodologiei și evaluării psihologice",
    "Metodologia cercetării psihologice și evaluare psihologică": "metodologiei cercetării și evaluării psihologice",
    "Statistică": "statisticii aplicate în psihologie",
    "Psihologia organizațională și a muncii": "psihologiei organizaționale și a muncii",
    "Psihopatologie": "psihopatologiei",
}

# Etichetă scurtă → formulare extinsă pentru examen
TOPIC_PHRASES: Dict[str, str] = {
    "programarea epigenetică": "programarea epigenetică și expresia genetică în personalitate",
    "epigenetica": "epigenetica și influența mediului asupra expresiei genetice",
    "moștenirea epigenetică a fricii": "moștenirea epigenetică a fricii în personalitate",
    "patternul dacă-atunci": "patternul comportamental de tip „dacă situația X, atunci răspunsul Y”",
    "modelul condițional-dispozițional": "modelul condițional-dispozițional al lui Jack Wright și Walter Mischel",
    "modelul caps": "modelul cognitiv-afectiv al personalității (CAPS) al lui Walter Mischel",
    "sistemul cognitiv-afectiv al personalității": "modelul CAPS — personalitatea ca sistem dinamic de construcții cognitive-afective",
    "neuroticismul": "neuroticismul ca dimensiune a personalității",
    "extraversia": "extraversia ca dimensiune a personalității",
    "deschiderea către experiență": "deschiderea către experiență în modelul celor cinci mari factori",
    "modelul big five": "modelul celor cinci mari factori ai personalității",
    "instrumentele big five": "instrumentele de evaluare a celor cinci mari factori",
    "modelul eredității: gene, mediu comun, mediu unic": "modelul eredității (gene, mediu comun, mediu unic) în studiile de personalitate",
    "eritabilitatea": "eritabilitatea trăsăturilor de personalitate",
    "studiile gemelare": "studiile gemelare în cercetarea personalității",
    "eroarea consistenței la nivel grupal": "eroarea consistenței la nivel grupal în interpretarea trăsăturilor",
    "întărirea pozitivă": "întărirea pozitivă în învățarea asociaționistă",
    "întărirea negativă": "întărirea negativă în învățarea asociaționistă",
    "pedeapsa pozitivă": "pedeapsa pozitivă în condiționarea operantă",
    "validitatea internă": "validitatea internă în designul cercetării",
    "validitatea externă": "validitatea externă și generalizarea rezultatelor",
    "validitatea de construct": "validitatea de construct în evaluarea psihologică",
    "validitatea de conținut": "validitatea de conținut a instrumentelor psihologice",
    "validitatea de criteriu": "validitatea de criteriu ca relație între test și performanță",
    "fidelitatea test-retest": "fidelitatea test-retest în evaluarea psihologică",
    "fidelitatea inter-evaluatori": "fidelitatea inter-evaluatori în evaluarea psihologică",
    "eroarea standard a măsurării": "eroarea standard a măsurării în testarea psihologică",
    "scorul brut": "scorurile brute transformate în norme standardizate",
    "eșantionul": "eșantionarea participanților și reprezentativitatea",
    "populația": "populația țintă și generalizarea în statistica inferențială",
    "analiza de putere": "analiza de putere pentru stabilirea eșantionului",
    "variabila independentă": "variabila independentă în designul experimental",
    "variabila dependentă": "variabila dependentă ca rezultat măsurat",
    "zona proximei dezvoltării": "zona proximei dezvoltării la Lev Vygotsky",
    "atașamentul securizant": "atașamentul securizant în teoria atașamentului",
    "atașamentul ambivalent/rezistent": "atașamentul ambivalent/rezistent la Mary Ainsworth",
    "situația stranie": "Situația stranie (Strange Situation)",
    "efectul halo": "efectul halo în evaluarea performanței organizaționale",
    "burnoutul": "burnoutul și epuizarea profesională",
    "stresul ocupațional": "stresul ocupațional și factorii de risc la locul de muncă",
}

# Distractori plauzibili din alte arii — formulare paralelă
CROSS_DOMAIN_PHRASES: Dict[str, str] = {
    "validitatea de criteriu": "validitatea de criteriu ca relație între test și performanță",
    "eșantionul": "analiza de putere pentru stabilirea eșantionului",
    "populația": "definirea populației și a unității de analiză în cercetare",
    "eroarea standard a măsurării": "eroarea standard a măsurării în testarea psihologică",
    "analiza varianței (anova)": "analiza varianței pentru compararea mai multor medii",
    "scala nominală": "scala nominală și clasificarea fără ordine",
    "delirul": "delirul ca simptom în tulburările psihotice",
    "mania": "mania ca episod în tulburările de dispoziție",
    "hipomania": "hipomania ca stare de dispoziție ridicată",
    "tulburările de personalitate": "tulburările de personalitate ca patternuri persistente",
    "terapia cognitiv-comportamentală": "terapia cognitiv-comportamentală ca abordare terapeutică",
    "evaluarea 360": "evaluarea 360° în managementul performanței",
    "analiza muncii": "analiza muncii orientată spre sarcină în psihologia organizațională",
    "identitatea sarcinii": "identitatea sarcinii în modelul Hackman-Oldham",
    "fidelitatea inter-evaluatori": "fidelitatea inter-evaluatori în codarea datelor",
    "scala binet-simon": "scala Binet-Simon ca prim test de inteligență",
    "testul stanford-binet": "testul Stanford-Binet ca revizuire a scalei Binet",
}

# Item contextual unic — pentru concepte-ancoră
CONTEXTUAL_SINGLE: Dict[str, dict] = {
    "modelul condițional-dispozițional": {
        "stem": "În tematica psihologiei personalității, modelul condițional-dispozițional al lui Jack Wright și Walter Mischel este asociat cu:",
        "options": {
            "a": "validitatea de criteriu ca relație între test și performanță",
            "b": "patternul comportamental de tip „dacă situația X, atunci răspunsul Y”",
            "c": "eșantionarea participanților pentru analiza de putere",
            "d": "scorurile brute transformate în norme standardizate",
        },
        "correct": "b",
    },
    "patternul dacă-atunci": {
        "stem": "În abordarea interacționistă a personalității, patternul dacă-atunci descrie:",
        "options": {
            "a": "regularitatea prin care o situație activă un răspuns comportamental specific",
            "b": "validitatea externă a unui instrument psihologic",
            "c": "procedura de eșantionare stratificată",
            "d": "coeficientul de corelație între două variabile",
        },
        "correct": "a",
    },
}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def exam_stem_for_domain(domain: str) -> str:
    short = DOMAIN_SHORT_NAMES.get(domain, domain.lower())
    return DOMAIN_EXAM_STEM.format(domain=short)


def expand_topic(label: str, domain: str = "") -> str:
    key = _norm(label)
    if key in TOPIC_PHRASES:
        return TOPIC_PHRASES[key]
    # potrivire parțială
    for k, phrase in TOPIC_PHRASES.items():
        if k in key or key in k:
            return phrase
    # păstrează eticheta dar o face mai clară
    t = label.strip()
    if len(t) < 40 and not t.endswith("."):
        return t[0].lower() + t[1:] if t else t
    return t


def expand_distractor(label: str) -> str:
    key = _norm(label)
    if key in CROSS_DOMAIN_PHRASES:
        return CROSS_DOMAIN_PHRASES[key]
    if key in TOPIC_PHRASES:
        return TOPIC_PHRASES[key]
    return expand_topic(label)


def match_contextual_single(correct_labels: list[str]) -> Optional[dict]:
    if len(correct_labels) != 1:
        return None
    key = _norm(correct_labels[0])
    for anchor, spec in CONTEXTUAL_SINGLE.items():
        if anchor in key or key in anchor:
            return spec
    return None
