"""Itemi conceptuali — înlocuiesc liste administrative (Forme ale / Tipuri de …)."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.concept_clusters import rotate_options

ConceptItem = Dict[str, Any]

VALIDITATE_POOL: List[ConceptItem] = [
    {
        "stem": "Validitatea unui test psihologic se referă în principal la:",
        "options": {
            "a": "măsura în care testul evaluează ceea ce pretinde că evaluează",
            "b": "stabilitatea scorurilor obținute de aceeași persoană la testări repetate",
            "c": "asemănarea itemilor între ei în cadrul aceleiași scale",
            "d": "transformarea scorurilor brute în scoruri standardizate",
        },
        "correct": "a",
    },
    {
        "stem": "Validitatea de criteriu a unui test este susținută atunci când:",
        "options": {
            "a": "scorurile testului se asociază cu un criteriu extern relevant, cum ar fi performanța",
            "b": "itemii testului par formulați clar și ușor de înțeles",
            "c": "rezultatele sunt identice pentru toți participanții testați",
            "d": "testul are un număr mare de itemi, indiferent de conținutul lor",
        },
        "correct": "a",
    },
    {
        "stem": "Validitatea de construct privește în principal:",
        "options": {
            "a": "măsura în care instrumentul evaluează constructul teoretic vizat",
            "b": "acoperirea completă a tuturor itemilor posibili din domeniu",
            "c": "stabilitatea scorurilor la aplicări repetate ale testului",
            "d": "gradul în care rezultatele pot fi generalizate la alte populații",
        },
        "correct": "a",
    },
    {
        "stem": "Validitatea de conținut presupune că:",
        "options": {
            "a": "itemii acoperă în mod adecvat domeniul de conținut evaluat",
            "b": "scorurile se corelează cu un criteriu extern relevant",
            "c": "rezultatele rămân stabile în timp la aceeași persoană",
            "d": "constructul teoretic este susținut de relații prevăzute între variabile",
        },
        "correct": "a",
    },
    {
        "stem": "Validitatea externă a unui test se referă mai ales la:",
        "options": {
            "a": "posibilitatea de a generaliza rezultatele la alte contexte sau populații",
            "b": "consistența răspunsurilor în cadrul aceleiași administrări",
            "c": "gradul în care itemii acoperă conținutul domeniului evaluat",
            "d": "transformarea scorurilor brute prin norme de referință",
        },
        "correct": "a",
    },
]

FIDELITATE_POOL: List[ConceptItem] = [
    {
        "stem": "Fidelitatea test-retest indică mai ales:",
        "options": {
            "a": "stabilitatea scorurilor la același test aplicat în momente diferite",
            "b": "măsura în care testul acoperă domeniul de conținut evaluat",
            "c": "relația dintre scorul la test și un criteriu extern relevant",
            "d": "interpretarea scorurilor prin raportare la norme",
        },
        "correct": "a",
    },
    {
        "stem": "Consistența internă a unui test reflectă în principal:",
        "options": {
            "a": "gradul în care itemii măsoară același construct în cadrul scalei",
            "b": "acordul dintre scoruri la două testări separate în timp",
            "c": "relația dintre scorul la test și un criteriu de performanță",
            "d": "acoperirea exhaustivă a conținutului evaluat de itemi",
        },
        "correct": "a",
    },
    {
        "stem": "Fidelitatea inter-evaluator indică:",
        "options": {
            "a": "acordul dintre scorurile acordate de evaluatori diferiți",
            "b": "stabilitatea scorurilor unei persoane în timp",
            "c": "măsura în care testul evaluează constructul teoretic vizat",
            "d": "gradul în care itemii reprezintă domeniul de conținut",
        },
        "correct": "a",
    },
    {
        "stem": "Fidelitatea unui instrument psihologic se referă în principal la:",
        "options": {
            "a": "consistența sau stabilitatea măsurării",
            "b": "gradul în care instrumentul măsoară ceea ce pretinde",
            "c": "relația dintre scor și un criteriu extern",
            "d": "acoperirea domeniului de conținut prin itemi",
        },
        "correct": "a",
    },
]

VALIDITATE_FIDELITATE_POOL: List[ConceptItem] = [
    {
        "stem": "Diferența principală dintre validitate și fidelitate este că:",
        "options": {
            "a": "validitatea privește ce măsoară testul, iar fidelitatea privește consistența măsurării",
            "b": "validitatea se referă la scoruri stabile, iar fidelitatea la criterii externe",
            "c": "validitatea depinde doar de numărul itemilor, iar fidelitatea doar de norme",
            "d": "validitatea și fidelitatea sunt concepte identice în evaluarea psihologică",
        },
        "correct": "a",
    },
]

ATASAMENT_POOL: List[ConceptItem] = [
    {
        "stem": "Atașamentul securizant la copil se caracterizează prin:",
        "options": {
            "a": "folosirea figurii de atașament ca bază de siguranță și confort la explorare",
            "b": "minimizarea contactului și a semnalelor de nevoie la reunire cu îngrijitorul",
            "c": "căutare intensă de apropiere combinată cu rezistență și calmare dificilă",
            "d": "pattern contradictoriu sau dezorientat, fără strategie coerentă de atașament",
        },
        "correct": "a",
    },
    {
        "stem": "Atașamentul evitant se caracterizează prin:",
        "options": {
            "a": "minimizarea contactului și a semnalelor de nevoie la reunire cu îngrijitorul",
            "b": "folosirea figurii de atașament ca bază de siguranță la explorare",
            "c": "căutare intensă de apropiere cu rezistență la calmare",
            "d": "comportament dezorganizat și lipsă de strategie clară la stres",
        },
        "correct": "a",
    },
    {
        "stem": "Atașamentul ambivalent/rezistent se caracterizează prin:",
        "options": {
            "a": "căutare intensă de apropiere combinată cu rezistență și calmare dificilă",
            "b": "minimizarea contactului și a semnalelor de nevoie la reunire",
            "c": "explorare sigură folosind îngrijitorul ca bază de confort",
            "d": "pattern dezorganizat fără răspuns coerent la separare",
        },
        "correct": "a",
    },
    {
        "stem": "Atașamentul dezorganizat se caracterizează prin:",
        "options": {
            "a": "pattern contradictoriu sau dezorientat, fără strategie coerentă de atașament",
            "b": "folosirea îngrijitorului ca bază sigură pentru explorare",
            "c": "evitarea contactului și a semnalelor de nevoie la reunire",
            "d": "căutare de apropiere cu calmare rapidă după separare",
        },
        "correct": "a",
    },
]

STILURI_PARENTALE_POOL: List[ConceptItem] = [
    {
        "stem": "Stilul parental autoritativ se caracterizează prin:",
        "options": {
            "a": "căldură emoțională ridicată și limite clare, cu așteptări realiste",
            "b": "cerințe ridicate și control strict, cu puțină căldură emoțională",
            "c": "puține limite și toleranță ridicată față de comportament",
            "d": "lipsă de implicare și răspuns inconsistent la nevoile copilului",
        },
        "correct": "a",
    },
    {
        "stem": "Stilul parental autoritar se caracterizează prin:",
        "options": {
            "a": "cerințe ridicate și control strict, cu puțină căldură și comunicare unidirecțională",
            "b": "căldură ridicată și limite clare, cu explicații și negociere",
            "c": "puține așteptări și toleranță mare față de comportament",
            "d": "absența regulilor și a monitorizării comportamentului copilului",
        },
        "correct": "a",
    },
    {
        "stem": "Stilul parental permisiv se caracterizează prin:",
        "options": {
            "a": "puține limite, toleranță ridicată și așteptări scăzute privind comportamentul",
            "b": "căldură ridicată combinată cu limite ferme și consecvență",
            "c": "control strict și comunicare predominant unidirecțională",
            "d": "lipsă de implicare și supraveghere minimă",
        },
        "correct": "a",
    },
]

PIAGET_POOL: List[ConceptItem] = [
    {
        "stem": "Stadiul senzorio-motor al lui Piaget este marcat în principal de:",
        "options": {
            "a": "cunoaștere prin acțiuni senzoriale și motorii, cu apariția permanenței obiectului",
            "b": "gândire simbolică, egocentrism cognitiv și dificultăți cu reversibilitatea",
            "c": "operații logice aplicate obiectelor și situațiilor concrete",
            "d": "raționament abstract, ipotetico-deductiv și gândire combinatorie",
        },
        "correct": "a",
    },
    {
        "stem": "Stadiul preoperațional al lui Piaget este marcat în principal de:",
        "options": {
            "a": "gândire simbolică, egocentrism cognitiv și dificultăți cu reversibilitatea",
            "b": "cunoaștere prin acțiuni senzoriale și motorii directe",
            "c": "operații logice asupra obiectelor concrete",
            "d": "raționament ipotetico-deductiv și abstract",
        },
        "correct": "a",
    },
    {
        "stem": "Stadiul operațional concret al lui Piaget este marcat în principal de:",
        "options": {
            "a": "operații logice aplicate obiectelor și situațiilor concrete",
            "b": "gândire simbolică și egocentrism cognitiv",
            "c": "permanența obiectului și învățarea prin acțiune directă",
            "d": "raționament formal abstract și ipotetico-deductiv",
        },
        "correct": "a",
    },
    {
        "stem": "Stadiul formal operațional al lui Piaget este marcat în principal de:",
        "options": {
            "a": "raționament abstract, ipotetico-deductiv și gândire combinatorie",
            "b": "operații logice limitate la obiecte și situații concrete",
            "c": "gândire simbolică și centrare pe propria perspectivă",
            "d": "cunoaștere exclusiv prin acțiuni senzorio-motorii",
        },
        "correct": "a",
    },
]

SCALE_MASURARE_POOL: List[ConceptItem] = [
    {
        "stem": "Scala nominală de măsurare presupune:",
        "options": {
            "a": "clasificarea observațiilor în categorii distincte, fără ordine între ele",
            "b": "ordinea categoriilor, fără distanțe egale între ele",
            "c": "distanțe egale între valori, fără zero absolut",
            "d": "zero absolut și raporturi între valori",
        },
        "correct": "a",
    },
    {
        "stem": "Scala ordinală de măsurare presupune:",
        "options": {
            "a": "ordinea categoriilor, fără distanțe egale între ele",
            "b": "categorii fără ordine internă",
            "c": "distanțe egale și zero absolut",
            "d": "doar numărarea frecvențelor, fără ordine",
        },
        "correct": "a",
    },
    {
        "stem": "Scala de interval presupune:",
        "options": {
            "a": "distanțe egale între valori, fără zero absolut",
            "b": "categorii ordonate fără distanțe fixe",
            "c": "zero absolut și raporturi proporționale",
            "d": "simple etichete fără ordine",
        },
        "correct": "a",
    },
]

BIG_FIVE_POOL: List[ConceptItem] = [
    {
        "stem": "Extraversia în modelul Big Five reflectă mai ales:",
        "options": {
            "a": "sociabilitate, energie pozitivă și căutarea stimulării sociale",
            "b": "tendința spre anxietate, teamă și dispoziție negativă",
            "c": "cooperare, încredere interpersonală și empatie",
            "d": "organizare, perseverență și orientare spre obiective",
        },
        "correct": "a",
    },
    {
        "stem": "Neuroticismul în modelul Big Five reflectă mai ales:",
        "options": {
            "a": "tendința spre anxietate, instabilitate emoțională și dispoziție negativă",
            "b": "sociabilitate și energie pozitivă",
            "c": "deschidere către experiențe noi și imaginație",
            "d": "respectarea normelor și a obligațiilor",
        },
        "correct": "a",
    },
]

ERIKSON_POOL: List[ConceptItem] = [
    {
        "stem": "Criza vârstei de mijloc în teoria lui Erikson presupune în principal:",
        "options": {
            "a": "reevaluarea sensului vieții, a contribuției personale și a direcției viitoare",
            "b": "dezvoltarea încrederii de bază în îngrijitor în primul an de viață",
            "c": "afirmarea identității și a rolului în grupul de egali în adolescență",
            "d": "integrarea experiențelor de viață și acceptarea mortalității la bătrânețe",
        },
        "correct": "a",
    },
    {
        "stem": "Criza de identitate versus confuzie de rol, în teoria lui Erikson, apare în:",
        "options": {
            "a": "adolescență, când persoana caută un sens coerent al sinelui și al direcției",
            "b": "vârsta școlară mică, prin stăpânirea abilităților și a competenței",
            "c": "vârsta adultă tânără, prin formarea relațiilor intime stabile",
            "d": "bătrânețe, prin integrarea experiențelor și acceptarea vieții",
        },
        "correct": "a",
    },
]

TEORII_INVATARE_POOL: List[ConceptItem] = [
    {
        "stem": "Condiționarea clasică presupune în principal:",
        "options": {
            "a": "asocierea unui stimul neutru cu un stimul incondiționat, producând un răspuns condiționat",
            "b": "modificarea comportamentului prin consecințe care urmează răspunsului",
            "c": "învățarea prin observarea și imitarea comportamentului altora",
            "d": "construirea activă a cunoștințelor prin asimilare și acomodare",
        },
        "correct": "a",
    },
    {
        "stem": "Condiționarea operantă presupune în principal:",
        "options": {
            "a": "modificarea probabilității unui comportament prin consecințele sale",
            "b": "asocierea dintre stimuli prin contiguitate temporală",
            "c": "învățarea prin modelare și imitare",
            "d": "dezvoltarea cognitivă prin stadii fixe",
        },
        "correct": "a",
    },
]

POOLS: Dict[str, List[ConceptItem]] = {
    "validitate": VALIDITATE_POOL,
    "fidelitate": FIDELITATE_POOL,
    "validitate_fidelitate": VALIDITATE_FIDELITATE_POOL,
    "atașament": ATASAMENT_POOL,
    "stiluri_parentale": STILURI_PARENTALE_POOL,
    "piaget": PIAGET_POOL,
    "scale_masurare": SCALE_MASURARE_POOL,
    "big_five": BIG_FIVE_POOL,
    "teorii_invatare": TEORII_INVATARE_POOL,
    "erikson": ERIKSON_POOL,
}


def resolve_pool_key(stem: str) -> Optional[str]:
    low = re.sub(r"\s+", " ", (stem or "").strip().lower())
    if not low:
        return None

    if "diferen" in low and "validit" in low and "fidelit" in low:
        return "validitate_fidelitate"
    if "forme ale validit" in low or (
        "forme ale" in low and "validit" in low and "psihometr" in low
    ):
        return "validitate"
    if "forme ale fidelit" in low or ("forme ale" in low and "fidelit" in low):
        return "fidelitate"
    if "tipuri de atașament" in low or "tipuri de atasament" in low:
        return "atașament"
    if "atașament" in low and ("tipuri" in low or "tipul" in low):
        return "atașament"
    if "stiluri parentale" in low or ("stil" in low and "parental" in low):
        return "stiluri_parentale"
    if "piaget" in low and ("stadii" in low or "stadiu" in low or "cognitive" in low):
        return "piaget"
    if "big five" in low or "dimensiuni big" in low:
        return "big_five"
    if "scale de măsurare" in low or "scale de masurare" in low:
        return "scale_masurare"
    if "teorii ale" in low and ("învățării" in low or "invatarii" in low):
        return "teorii_invatare"
    if "erikson" in low or "criza vârstei" in low or "criza de identitate" in low:
        return "erikson"
    if "reevaluare personală" in low or "vârsta de mijloc" in low:
        return "erikson"

    if re.search(r"\b(?:forme ale|tipuri (?:de|ale))\b", low):
        if "fidelit" in low:
            return "fidelitate"
        if "validit" in low:
            return "validitate"
        if "atașament" in low or "atasament" in low:
            return "atașament"
        if "parental" in low:
            return "stiluri_parentale"
        if "piaget" in low:
            return "piaget"
    return None


def infer_pool_from_options(options: Dict[str, str]) -> Optional[str]:
    blob = " ".join(str(v) for v in options.values()).lower()
    if any(
        x in blob
        for x in ("securizant", "evitant", "dezorganizat", "ambivalent", "rezistent")
    ):
        return "atașament"
    if any(x in blob for x in ("autoritativ", "autoritar", "permisiv", "neglijent")):
        return "stiluri_parentale"
    if any(
        x in blob
        for x in (
            "senzorio",
            "preoperațional",
            "preoperational",
            "operațional concret",
            "formal operațional",
        )
    ):
        return "piaget"
    if any(
        x in blob
        for x in ("validitatea de", "validitatea crit", "validitate extern")
    ):
        return "validitate"
    if any(x in blob for x in ("fidelitatea", "consistența internă", "test-retest")):
        if "validitatea" in blob and "fidelitatea" in blob:
            pass
        elif sum(1 for x in ("fidelitatea", "consistența", "test-retest") if x in blob) >= 2:
            return "fidelitate"
    if any(x in blob for x in ("nominală", "ordinală", "interval", "raport")):
        return "scale_masurare"
    if any(
        x in blob
        for x in ("neuroticism", "extraversia", "agreabilitate", "conștiinciozitate")
    ):
        return "big_five"
    if any(
        x in blob
        for x in ("condiționarea clasică", "condiționarea operantă", "observațională")
    ):
        return "teorii_invatare"
    return None


def pick_conceptual_spec(
    stem: str, seed: int, options: Optional[Dict[str, str]] = None
) -> Optional[Tuple[str, Dict[str, str], str]]:
    key = resolve_pool_key(stem)
    if not key and options:
        key = infer_pool_from_options(options)
    if not key:
        return None
    pool = POOLS.get(key)
    if not pool:
        return None
    spec = pool[seed % len(pool)]
    return rotate_options(spec, seed)
