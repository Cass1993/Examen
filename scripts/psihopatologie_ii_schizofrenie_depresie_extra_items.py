"""Itemi suplimentari — Psihopatologie II: schizofrenie și tulburări depresive."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SCHIZOFRENIE_DEPRESIE_EXTRA_ITEMS: List[Item] = [
    # —— Psihoză: capcane și criterii fine (1–10) ——
    {
        "stem": "Faza prodromală a schizofreniei poate include:",
        "options": [
            "deteriorarea funcționării și retragerea socială",
            "suspiciozitate și anxietate crescută",
            "idei delirante și halucinații clare, ca regulă",
            "remisiune completă după 48 de ore",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Halucinațiile auditive în schizofrenie pot fi asociate cu un deficit "
            "de automonitorizare, astfel încât vocea este percepută ca externă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburarea psihotică scurtă și tulburarea delirantă se deosebesc "
            "prin durată: psihotică scurtă durează maximum o lună, delirantă "
            "cel puțin o lună."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un pacient prezintă delir și halucinații timp de două săptămâni în "
            "cadrul unui episod depresiv major sever, fără simptome psihotice "
            "în afara episodului afectiv. Diagnosticul probabil:"
        ),
        "options": [
            "episod depresiv major cu caracteristici psihotice",
            "schizofrenie",
            "tulburare delirantă",
            "tulburare schizoafectivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Pentru tulburarea schizoafectivă, delirul sau halucinațiile trebuie "
            "să fie prezente cel puțin două săptămâni în absența unui episod "
            "major de dispoziție."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "O pacientă are episoade repetate de dispoziție depresivă majoră și, "
            "în aceeași perioadă, halucinații auditive și delir, dar psihoza "
            "persistă și când dispoziția se normalizează. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare schizoafectivă",
            "episod depresiv major cu caracteristici psihotice",
            "tulburare delirantă",
            "distimie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburările din spectrul schizofreniei nu trebuie atribuite în principal "
            "efectelor substanțelor sau unei afecțiuni medicale."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Simptomele negative din schizofrenie pot fi confundate cu depresia, "
            "dar anhedonia și avoliția din psihoză apar în contextul unui tablou "
            "psihotic mai larg."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Idei delirante de tip erotomanic presupun convingerea că:",
        "options": [
            "o altă persoană este îndrăgostită de subiect",
            "relația există în ciuda refuzului evident",
            "subiectul este persecutat de autorități",
            "organismul este gol sau distrus",
        ],
        "correct": "ab",
    },
    {
        "stem": "Idei delirante nihiliste pot include convingerea că:",
        "options": [
            "organismul sau lumea nu mai există",
            "s-a produs o catastrofă ireversibilă",
            "subiectul are o misiune specială de salvare",
            "o celebritate este îndrăgostită de subiect",
        ],
        "correct": "ab",
    },
    # —— Depresie: forme, simptome, etiologie (11–20) ——
    {
        "stem": "Tulburarea afectivă sezonieră se caracterizează prin:",
        "options": [
            "episoade depresive legate de anumite anotimpuri",
            "remisiune în alte perioade ale anului",
            "episoade maniacale obligatorii în fiecare lună",
            "durată obligatorie de minimum doi ani, fără excepții",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea disforică premenstruală presupune:",
        "options": [
            "simptome afective și somatice înaintea menstruației",
            "îmbunătățire după debutul menstruației",
            "episoade de grandiozitate și energie crescută",
            "absența oricărei componente emoționale",
        ],
        "correct": "ab",
    },
    {
        "stem": "În episodul depresiv major pot apărea:",
        "options": [
            "lentoare psihomotorie sau agitație",
            "modificări ale somnului și apetitului",
            "sentimente de inutilitate sau vinovăție excesivă",
            "halucinații auditive obligatorii, fără dispoziție scăzută",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Explicațiile biologice ale depresiei pot implica modificări ale "
            "hipocampului, amigdalei și cortexului prefrontal."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Modelul interpersonal al depresiei evidențiază:",
        "options": [
            "căutarea excesivă de reasigurare",
            "reacții negative din partea celorlalți",
            "retragerea care reduce recompensele sociale",
            "absența oricărei componente relaționale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Distimia și episodul depresiv major pot coexista: dispoziție cronică "
            "de fond cu suprapuneri de episoade mai severe."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un student dezvoltă brusc delir de vinovată și halucinații în timpul "
            "unui episod depresiv sever; simptomele psihotice dispar odată cu "
            "remisia depresiei. Diagnosticul probabil:"
        ),
        "options": [
            "episod depresiv major cu caracteristici psihotice",
            "schizofrenie",
            "tulburare delirantă",
            "tulburare psihotică scurtă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În tratamentul schizofreniei, formarea competențelor sociale și "
            "asistența comunitară urmăresc reintegrarea și aderența la tratament."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație descrie corect diferența dintre simptomele pozitive "
            "și cele negative?"
        ),
        "options": [
            "pozitive — adăugiri anormale, cum ar fi vocile",
            "negative — pierderi sau diminuări ale funcțiilor normale",
            "pozitive — avoliție și alogie",
            "negative — delir și halucinații",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un pacient are idei delirante de referință și gândire dezorganizată "
            "de șase săptămâni, fără simptome înainte; funcționarea s-a "
            "deteriorat brusc. Dacă simptomele continuă peste șase luni, "
            "diagnosticul devine probabil:"
        ),
        "options": [
            "schizofrenie",
            "tulburare psihotică scurtă",
            "tulburare delirantă",
            "distimie",
        ],
        "correct": "a",
    },
]
