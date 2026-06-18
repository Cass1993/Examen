"""Reformulări gramaticale și metodologice pentru enunțuri de itemi."""

from __future__ import annotations



import re



ZONE_PHRASES: dict[str, str] = {

    "organizațional": "psihologia organizațională",

    "psihometric": "psihometria",

    "psihometrie": "psihometria",

    "comportamental": "abordarea comportamentală",

    "inferential": "statistica inferențială",

    "genetică": "factorii genetici în psihologie",

    "genomică": "genomica comportamentală",

    "epigenetică": "epigenetica",

    "interacționist": "perspectiva interacționistă",

    "umanist": "abordarea umanistă",

    "psihodinamic": "abordarea psihodinamică",

    "metodologie": "metodologia cercetării psihologice",

    "anxietate": "tulburările de anxietate",

    "analiza muncii": "analiza muncii",

    "eșantionare": "eșantionarea în cercetare",

    "terapia cognitiv-comportamentală": "terapia cognitiv-comportamentală",

    "motivație": "motivația la locul de muncă",

    "selecție": "selecția personalului",

    "job design": "proiectarea postului (job design)",

    "cluster": "clusterele de tulburări de personalitate",

    "clusterc": "clusterul C de tulburări de personalitate",

    "evaluare": "evaluarea psihologică",

    "etică": "etica în psihologie",

    "parentalitate": "parentalitatea și stilurile parentale",

    "teste": "testele psihologice",

    "învățare": "procesele de învățare",

    "măsurare": "măsurarea în psihologie",

    "substanțe": "tulburările legate de substanțe",

    "validitate": "validitatea în evaluare",

    "atașament": "teoria atașamentului",

    "personalitate": "psihologia personalității",

    "performanță": "evaluarea performanței profesionale",

    "modelul cerințelor și resurselor postului": "modelul cerințelor și resurselor postului",

    "psihoză": "tulburările psihotice",

    "aptitudini": "evaluarea aptitudinilor",

    "stres": "stresul ocupațional",

    "curente": "curentele psihoterapeutice",

    "design": "designul cercetării",

    "familie": "terapia de familie",

    "variabile": "variabilele în cercetare",

    "erikson": "teoria dezvoltării psihosociale a lui Erikson",

    "piaget": "teoria cognitivă a lui Piaget",

    "freud": "teoria psihodinamică a lui Freud",

    "kohlberg": "teoria dezvoltării morale a lui Kohlberg",

}



IN_ZONE_RE = re.compile(

    r"^În zona «([^»]+)», care dintre următoarele asocieri sunt corecte\?\s*$",

    re.IGNORECASE,

)

SELECT_CATEGORY_RE = re.compile(

    r"^Selectează variantele care se încadrează corect la «([^»]+)»:?\s*$",

    re.IGNORECASE,

)



# Itemi «alege definiția pentru X»

CONCEPT_AUTHOR_LABEL_RE = re.compile(

    r"^Care variantă descrie cel mai bine conceptul/autorul:\s*(.+?)\?\s*$",

    re.IGNORECASE | re.DOTALL,

)

# Itemi «alege conceptul pentru descriere»

REVERSE_CONCEPT_RE = re.compile(

    r"^Cărui concept/autor îi corespunde descrierea:\s*«(.+?)»\?\s*$",

    re.IGNORECASE | re.DOTALL,

)

REVERSE_TERM_RE = re.compile(

    r"^Ce termen/autor corespunde cel mai bine descrierii:\s*(.+?)\?\s*$",

    re.IGNORECASE | re.DOTALL,

)

# Meta-enunț redundant («într-un item de examen…») — reformulat direct pe țintă

EXAM_META_RE = re.compile(

    r"^Într-un item de examen, care formulare este cea mai potrivită pentru\s+(.+?)\?\s*$",

    re.IGNORECASE | re.DOTALL,

)



AUTHOR_INITIALS_RE = re.compile(

    r"^[A-Z]\.\s*(?:[A-Z]\.\s*)?[A-ZĂÂÎȘȚÀ-Ž][a-zăâîșțà-ž\-]+(?:\s+(?:și|and)\s+[A-ZĂÂÎȘȚÀ-Ž][a-zăâîșțà-ž\-]+)?$"

)



STEM_BY_KIND = {

    "autor": "Care variantă descrie cel mai bine contribuția teoretică a lui {label}?",

    "instrument": "Care variantă descrie cel mai bine instrumentul/testul psihologic «{label}»?",

    "model": "Care variantă descrie cel mai bine modelul teoretic «{label}»?",

    "terapie": "Care variantă descrie cel mai bine abordarea terapeutică «{label}»?",

    "tulburare": "Care variantă descrie cel mai bine categoria clinică «{label}»?",

    "metoda": "Care variantă descrie cel mai bine procedura/metoda «{label}»?",

    "trasatura": "Care variantă descrie cel mai bine trăsătura psihologică «{label}»?",

    "concept": "Care variantă descrie cel mai bine conceptul «{label}»?",

}





def _zone_phrase(tag: str) -> str:

    key = tag.strip().lower()

    if key in ZONE_PHRASES:

        return ZONE_PHRASES[key]

    for variant in (tag.strip(), tag.strip().title(), tag.strip().lower()):

        if variant.lower() in ZONE_PHRASES:

            return ZONE_PHRASES[variant.lower()]

    return tag.strip()





def _classify_target(label: str) -> str:

    """Clasifică ținta itemului: concept, autor, instrument, model etc."""

    l = label.strip()

    ll = l.lower()



    if AUTHOR_INITIALS_RE.match(l):

        return "autor"



    if l.startswith(("Modelul ", "Model ", "Teoria ", "Abordarea transdiagnostică")):

        return "model"



    if l.startswith(

        (

            "Terapia ",

            "Psihoterapia",

            "Psihanaliza",

            "Schema Therapy",

            "Schema ",

            "Abordarea ",

        )

    ):

        return "terapie"

    if "terapie" in ll and not l.startswith("Etica"):

        return "terapie"



    stat_test_markers = (
        "testul t",
        "testul chi",
        "testul f",
        "testul z",
        "testul mann",
        "testul wilcoxon",
        "testul mcnemar",
    )
    if l.lower().startswith("testul ") and any(m in ll for m in stat_test_markers):
        return "metoda"

    if l.startswith(

        (

            "Inventarul",

            "Chestionarul",

            "Testul ",

            "Scala Binet",

            "Scala Wechsler",

            "Instrumentele ",

        )

    ):

        return "instrument"

    if any(k in l for k in ("Inventar", "Chestionar")) and "(" in l:

        return "instrument"



    if l.startswith(

        (

            "Tulburările",

            "Tulburarea",

            "Atacul ",

            "Anxietatea",

            "Fobia ",

            "Depresia",

            "Mania",

            "Schizofrenia",

            "Delirul",

            "Halucinația",

            "Anhedonia",

            "Hipomania",

            "Simptomele negative",

        )

    ):

        return "tulburare"

    if "tulburare" in ll or "tulburări" in ll:

        return "tulburare"



    if l.startswith(

        (

            "Metodele",

            "Metoda ",

            "Analiza ",

            "Evaluarea",

            "Testarea",

            "Screeningul",

            "Proiectarea",

            "Job design",

            "Strange Situation",

            "Situația stranie",

        )

    ):

        return "metoda"



    if l.startswith(

        (

            "Extraversia",

            "Agreabilitatea",

            "Conștiinciozitatea",

            "Neuroticismul",

            "Deschiderea",

            "Onestitate-umilință",

        )

    ):

        return "trasatura"



    return "concept"





def _stem_for_label(label: str) -> str:

    kind = _classify_target(label)

    return STEM_BY_KIND[kind].format(label=label.strip())





def _normalize_description(desc: str) -> str:

    d = desc.strip()

    if d.startswith("«") and d.endswith("»"):

        return d

    if not d.startswith("«"):

        return f"«{d}»"

    return d





def fix_intrebare(text: str) -> str:

    """Returnează enunțul reformulat gramatical/metodologic."""

    t = (text or "").strip()

    if not t:

        return t



    m = CONCEPT_AUTHOR_LABEL_RE.match(t)

    if m:

        return _stem_for_label(m.group(1))



    m = EXAM_META_RE.match(t)

    if m:

        return _stem_for_label(m.group(1))



    m = REVERSE_CONCEPT_RE.match(t)

    if m:

        desc = _normalize_description(m.group(1))

        return f"Care concept este descris de formularea {desc}?"



    m = REVERSE_TERM_RE.match(t)

    if m:

        desc = m.group(1).strip()

        desc = _normalize_description(desc)

        return f"Ce concept corespunde cel mai bine descrierii {desc}?"



    m = IN_ZONE_RE.match(t)

    if m:

        phrase = _zone_phrase(m.group(1))

        return (

            f"Referitor la {phrase}, care dintre următoarele asocieri "

            f"concept–definiție sunt corecte?"

        )



    m = SELECT_CATEGORY_RE.match(t)

    if m:

        category = m.group(1).strip()

        return f"Care dintre următoarele variante aparțin categoriei «{category}»?"



    return t


