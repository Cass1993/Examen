"""Itemi — Psihopatologie II: spectrul schizofreniei și tulburările depresive."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SCHIZOFRENIE_DEPRESIE_ITEMS: List[Item] = [
    # —— Spectrul schizofreniei: repere (1–6) ——
    {
        "stem": (
            "Spectrul schizofreniei și al altor tulburări psihotice este organizat, "
            "în clasificarea actuală, ca un continuum de la:"
        ),
        "options": [
            "forme mai puțin severe la forme severe",
            "tulburări cu componentă psihotică variabilă",
            "episoade scurte, complet normale, fără urme",
            "tulburări exclusiv de personalitate, fără psihoză",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburările incluse în spectrul schizofreniei includ:",
        "options": [
            "tulburarea delirantă și tulburarea psihotică scurtă",
            "schizofrenia și tulburarea schizoafectivă",
            "tulburarea obsesiv-compulsivă",
            "tulburarea de panică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate schizotipală este, de obicei, clasificată "
            "ca tulburare de personalitate, dar este considerată parte a spectrului "
            "schizofreniei."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Simptomele pozitive în psihoză includ:",
        "options": [
            "halucinații și idei delirante",
            "gândire sau vorbire dezorganizată",
            "comportament dezorganizat sau catatonic",
            "avoliție și alogie",
        ],
        "correct": "abc",
    },
    {
        "stem": "Simptomele negative în psihoză includ:",
        "options": [
            "diminuarea expresiei emoționale",
            "avoliție, alogie și anhedonie",
            "asocialitate",
            "iluzii de persecuție",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Simptomele negative presupun adăugarea unor experiențe noi, "
            "cum ar fi vocile sau ideile delirante."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Simptome pozitive detaliate (7–14) ——
    {
        "stem": "Halucinațiile sunt definite ca:",
        "options": [
            "experiențe senzoriale fără stimul real",
            "percepții care apar în absența unui obiect sau eveniment",
            "convingeri false, ferme, rezistente la dovezi",
            "interpretări greșite ale unui stimul real prezent",
        ],
        "correct": "ab",
    },
    {
        "stem": "În schizofrenie, halucinațiile cele mai frecvente sunt:",
        "options": [
            "halucinațiile auditive",
            "vocile care comentează sau dau ordine",
            "halucinațiile olfactive, ca regulă obligatorie",
            "iluziile vizuale simple, ca simptom central",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tipuri frecvente de idei delirante includ:",
        "options": [
            "persecuție, grandoare și control",
            "referință, nihiliste și erotomanice",
            "anhedonie și avoliție",
            "lentoare psihomotorie și insomnie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O iluzie diferă de o idee delirantă prin faptul că iluzia presupune "
            "interpretarea greșită a unui stimul real, nu o convingere falsă fără stimul."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Gândirea dezorganizată poate include:",
        "options": [
            "derieri și asocieri libere",
            "răspunsuri irelevante sau neologisme",
            "salată de cuvinte",
            "alogie și afect plat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Comportamentul dezorganizat sau anormal poate include:",
        "options": [
            "comportament copilăresc sau nepotrivit contextului",
            "agitație și imprevizibilitate",
            "dificultăți în finalizarea activităților orientate spre scop",
            "postură rigidă, imobilă, cu reactivitate redusă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Comportamentul catatonic poate include:",
        "options": [
            "scăderea reactivității la mediu",
            "menținerea unor posturi rigide, imobile",
            "înfățișare neîngrijită sau nepotrivită",
            "căutarea activă a atenției și dramatizare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Diminuarea expresiei emoționale presupune reducerea:",
        "options": [
            "expresiilor faciale și a contactului vizual",
            "intonției și mișcărilor expresive",
            "ideilor delirante de persecuție",
            "halucinațiilor auditive",
        ],
        "correct": "ab",
    },
    # —— Simptome negative și diagnostic psihotic (15–22) ——
    {
        "stem": "Avoliția se referă la:",
        "options": [
            "incapacitatea de a iniția sau finaliza activități orientate spre scop",
            "interes redus pentru muncă sau activități sociale",
            "convingeri false de grandoare",
            "agitație psihomotorie și insomnie",
        ],
        "correct": "ab",
    },
    {
        "stem": "Alogia este caracterizată prin:",
        "options": [
            "sărăcirea vorbirii",
            "răspunsuri scurte, goale sau vagi",
            "gândire de tip salată de cuvinte",
            "dramatizare și emoționalitate excesivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Anhedonia și asocialitatea aparțin simptomelor negative și implică "
            "plăcere redusă și lipsă de interes pentru interacțiuni sociale."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Criteriul central al tulburării delirante este:",
        "options": [
            "una sau mai multe idei delirante de cel puțin o lună",
            "funcționare nesemnificativ afectată în afara delirului",
            "comportament evident bizar, ca regulă",
            "prezența obligatorie a halucinațiilor auditive",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea delirantă se deosebește de schizofrenie prin:",
        "options": [
            "absența comportamentului evident bizar",
            "funcționare relativ conservată în afara delirului",
            "prezența obligatorie a simptomelor negative marcate",
            "durata obligatorie de minimum șase luni de psihoză",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea psihotică scurtă presupune:",
        "options": [
            "idei delirante, halucinații sau vorbire dezorganizată",
            "durată între o zi și o lună",
            "revenire la funcționarea anterioară",
            "durată obligatorie de minimum doi ani",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un pacient dezvoltă brusc idei delirante și halucinații auditive, "
            "simptomele dispar complet după trei săptămâni. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare psihotică scurtă",
            "schizofrenie",
            "tulburare delirantă",
            "episod depresiv major cu caracteristici psihotice",
        ],
        "correct": "a",
    },
    {
        "stem": "Pentru diagnosticul schizofreniei este necesar:",
        "options": [
            "cel puțin două simptome caracteristice",
            "cel puțin unul dintre: delir, halucinații sau vorbire dezorganizată",
            "activitate psihotică de cel puțin o lună",
            "semne de continuare timp de cel puțin șase luni",
        ],
        "correct": "abcd",
    },
    # —— Schizoafectivă, evoluție, etiologie, tratament (23–30) ——
    {
        "stem": "Tulburarea schizoafectivă presupune:",
        "options": [
            "simptome de schizofrenie",
            "un episod major de dispoziție concomitent sau în istoric",
            "delir sau halucinații de cel puțin două săptămâni fără episod afectiv major",
            "absența oricărei componente afective",
        ],
        "correct": "abc",
    },
    {
        "stem": "Fazele evoluției schizofreniei pot include:",
        "options": [
            "faza prodromală: deteriorare și retragere",
            "faza activă: psihoză completă",
            "faza reziduală: simptome pozitive reduse, negative persistente",
            "faza de remisiune obligatorie după 48 de ore",
        ],
        "correct": "abc",
    },
    {
        "stem": "Explicațiile etiologice ale schizofreniei includ:",
        "options": [
            "modelul diateză-stres și vulnerabilitate genetică",
            "ipoteza dopaminei și anomalii cerebrale",
            "deficite cognitive și emoție exprimată familială ridicată",
            "exclusiv o cauză psihanalitică unică, demonstrată",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tratamentul schizofreniei poate include:",
        "options": [
            "medicație antipsihotică",
            "spitalizare când este necesară",
            "terapie cognitiv-comportamentală pentru psihoză",
            "intervenții familiale și asistență comunitară",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În faza reziduală a schizofreniei, simptomele pozitive sunt adesea "
            "reduse, iar simptomele negative pot persista."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea delirantă poate include episoade maniacale sau depresive "
            "majore scurte, în raport cu durata episodului delirant."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "O persoană are de un an idei delirante de persecuție, fără "
            "halucinații sau comportament bizar evident; funcționează relativ "
            "normal în afara convingerilor. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare delirantă",
            "tulburare psihotică scurtă",
            "schizofrenie",
            "tulburare de personalitate paranoidă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de personalitate paranoidă diferă de tulburarea delirantă "
            "prin faptul că delirantă presupune idei delirante clare, iar paranoidă "
            "implică un tipar de personalitate fără psihoză completă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Tulburările depresive: diagnostic (31–42) ——
    {
        "stem": "Tulburările depresive sunt tulburări de dispoziție caracterizate prin:",
        "options": [
            "simptome emoționale, cognitive și motivaționale",
            "modificări comportamentale și fizice",
            "episoade de elație și grandiozitate obligatorii",
            "halucinații persistente, fără componentă afectivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Simptome frecvente în depresie includ:",
        "options": [
            "tristețe, lipsă de speranță și anhedonie",
            "oboseală, somn sau apetit modificat",
            "concentrare slabă, vinovăție sau idei suicidare",
            "grandiozitate și energie crescută, ca regulă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Pentru episodul depresiv major este necesar:",
        "options": [
            "minimum cinci simptome timp de cel puțin două săptămâni",
            "dispoziție depresivă sau pierderea interesului sau plăcerii",
            "prezența obligatorie a ideilor delirante de persecuție",
            "durată obligatorie de minimum doi ani",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O pacientă raportează tristețe zilnică, anhedonie, insomnie, oboseală, "
            "vinovăție și dificultăți de concentrare de trei săptămâni. "
            "Diagnosticul probabil:"
        ),
        "options": [
            "episod depresiv major",
            "distimie",
            "tulburare de personalitate borderline",
            "schizofrenie",
        ],
        "correct": "a",
    },
    {
        "stem": "Distimia presupune:",
        "options": [
            "dispoziție depresivă cea mai mare parte a timpului",
            "durată de minimum doi ani",
            "simptome mai puțin intense, dar cronice",
            "episoade maniacale obligatorii",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Distimia se deosebește de episodul depresiv major prin faptul că "
            "distimia este mai cronica și, de regulă, mai puțin intensă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Forme sau tipuri asociate tulburărilor depresive includ:",
        "options": [
            "depresie majoră și distimie",
            "tulburarea afectivă sezonieră",
            "tulburarea disforică premenstruală",
            "tulburarea de panică ca formă principală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Episodul depresiv major și tulburarea bipolară pot include simptome "
            "depresive, dar bipolară necesită și episoade de dispoziție crescută."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un bărbat descrie stare depresivă aproape zilnic de doi ani și jumătate, "
            "fără episoade clare de exaltare. Diagnosticul probabil:"
        ),
        "options": [
            "distimie",
            "episod depresiv major curent",
            "tulburare psihotică scurtă",
            "tulburare delirantă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea schizoafectivă și schizofrenia cu simptome depresive "
            "pot fi diferențiate prin prezența unui episod major de dispoziție "
            "în cadrul tulburării schizoafective."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Episodul depresiv major cu caracteristici psihotice include simptome "
            "depresive împreună cu delir sau halucinații legate de starea afectivă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În evaluarea depresiei, ideile suicidare reprezintă un semn de "
            "severitate care necesită evaluare atentă a riscului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Etiologie depresie și capcane (43–50) ——
    {
        "stem": "Explicațiile biologice ale depresiei includ:",
        "options": [
            "vulnerabilitate genetică",
            "implicarea serotoninei, norepinefrinei și dopaminei",
            "dereglarea axei hipotalamo-hipofizo-adrenale și a cortizolului",
            "absența oricărei componente neurobiologice",
        ],
        "correct": "abc",
    },
    {
        "stem": "Conform modelului lui Beck, depresia poate fi menținută prin:",
        "options": [
            "scheme negative despre sine, lume și viitor",
            "biasuri în procesarea informațiilor",
            "retragere și reducerea recompenselor",
            "absența oricărei componente cognitive",
        ],
        "correct": "ab",
    },
    {
        "stem": "Neajutorarea și deznădejdea în depresie presupun:",
        "options": [
            "interpretarea evenimentelor negative ca globale și stabile",
            "atribuire internă a eșecurilor",
            "risc crescut pentru suicid",
            "certitudinea că viitorul va fi pozitiv",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ruminația în depresie:",
        "options": [
            "presupune reflectare repetată asupra simptomelor sau cauzelor",
            "poate menține și prezice episoade depresive",
            "reduce automat severitatea depresiei",
            "este echivalentul gândirii orientate spre soluții",
        ],
        "correct": "ab",
    },
    {
        "stem": "Explicațiile psihodinamice ale depresiei pun accent pe:",
        "options": [
            "pierdere și furie întoarsă spre sine",
            "conflict intrapsihic și vinovăție",
            "exclusiv o cauză genetică unică",
            "absența oricărei componente afective",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Modelul comportamental al depresiei evidențiază reducerea recompenselor "
            "și retragerea sau inactivitatea ca factori de menținere."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care pereche distinge corect o tulburare psihotică de una depresivă?"
        ),
        "options": [
            "schizofrenie — delir/halucinații centrale; depresie majoră — dispoziție scăzută",
            "tulburare delirantă — delir persistent; distimie — depresie cronică ușoară",
            "tulburare psihotică scurtă — sub o lună; episod depresiv major — minimum două săptămâni",
            "schizofrenie — minimum cinci simptome depresive; distimie — psihoză activă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un pacient are vocile auditive, gândire dezorganizată și simptome "
            "negative de opt luni. Diagnosticul probabil:"
        ),
        "options": [
            "schizofrenie",
            "tulburare delirantă",
            "tulburare psihotică scurtă",
            "distimie",
        ],
        "correct": "a",
    },
]
