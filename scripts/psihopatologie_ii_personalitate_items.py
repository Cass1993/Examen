"""Itemi — Psihopatologie II: tulburările de personalitate."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PERSONALITATE_ITEMS: List[Item] = [
    # —— Introducere și criterii generale (1–6) ——
    {
        "stem": "Tulburările de personalitate se caracterizează prin:",
        "options": [
            "tipare persistente, inflexibile și dezadaptative",
            "dezvoltare din adolescență sau începutul vieții adulte",
            "afectare a funcționării personale sau interpersonale",
            "episoade scurte, complet remisive fără urme",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Conform criteriilor generale, modelul de personalitate patologic "
            "trebuie manifestat rigid în cel puțin două domenii, precum:"
        ),
        "options": [
            "cogniție și afectivitate",
            "funcționare interpersonală",
            "controlul impulsurilor",
            "inteligența generală măsurată",
        ],
        "correct": "abc",
    },
    {
        "stem": "Afectarea funcționării personalității poate include dificultăți în:",
        "options": [
            "reglarea emoțională și empatie",
            "intimitate și relații interpersonale",
            "imaginea de sine",
            "memoria pe termen scurt, ca simptom central",
        ],
        "correct": "abc",
    },
    {
        "stem": "Clusterele tulburărilor de personalitate din clasificarea actuală sunt:",
        "options": [
            "A — ciudat/eccentric",
            "B — dramatic/emoțional",
            "C — anxios/temător",
            "D — psihotic/acut",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate este definită ca model durabil de experiență "
            "interioară și comportament care se abate de la așteptările culturii, "
            "este stabil, inflexibil și produce suferință sau afectare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Tulburările de personalitate apar brusc la vârsta mijlocie, "
            "fără antecedente în adolescență."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Fațete și domenii patologice (7–10) ——
    {
        "stem": "Fațeta antagonism în modelul trăsăturilor patologice include:",
        "options": [
            "manipulativitate și înșelăciune",
            "grandiozitate și insensibilitate",
            "retragere socială și anhedonie",
            "perfecționism rigid și ordine excesivă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Fațeta detașare este asociată, în principal, cu:",
        "options": [
            "retragere și evitarea intimității",
            "anhedonie și afectivitate restrânsă",
            "căutarea atenției și dramatizare",
            "impulsivitate și asumarea riscurilor",
        ],
        "correct": "ab",
    },
    {
        "stem": "Fațetele dezinhibiție și psihotism pot include:",
        "options": [
            "impulsivitate și iresponsabilitate",
            "excentricitate și experiențe neobișnuite",
            "supunere excesivă și teamă de abandon",
            "suspiciozitate și ranchiună persistentă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Afectivitatea negativă în modelul trăsăturilor patologice poate include "
            "anxietate, labilitate emoțională, depresivitate și suspiciozitate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Cluster A (11–18) ——
    {
        "stem": "Clusterul A al tulburărilor de personalitate include:",
        "options": [
            "tulburarea de personalitate paranoidă",
            "tulburarea de personalitate schizoidă",
            "tulburarea de personalitate schizotipală",
            "tulburarea de personalitate antisocială",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburările din clusterul A se deosebesc de schizofrenie prin faptul că, "
            "de regulă, nu implică:"
        ),
        "options": [
            "halucinații senzoriale persistente",
            "pierderea completă a contactului cu realitatea",
            "gândire ciudată sau suspiciozitate",
            "retragere socială marcată",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea de personalitate paranoidă presupune:",
        "options": [
            "neîncredere și suspiciune persistentă față de ceilalți",
            "interpretarea intențiilor altora ca amenințătoare",
            "retragere voluntară din orice contact uman",
            "emoționalitate excesivă și căutarea atenției",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate paranoidă:",
        "options": [
            "suspiciuni nejustificate privind loialitatea altora",
            "interpretarea amenințătoare a remarcilor neutre",
            "ranchiună persistentă și perceperea atacurilor",
            "lipsa oricărei suspiciuni față de partener",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tulburarea de personalitate schizoidă se caracterizează prin:",
        "options": [
            "detașare persistentă de relațiile sociale",
            "gamă restrânsă de exprimare emoțională",
            "comportament seductiv și teatral",
            "grandiozitate și nevoie de admirație",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un bărbat preferă activități solitare, nu dorește relații apropiate, "
            "pare indiferent la laude și are afect plat. Tabloul sugerează:"
        ),
        "options": [
            "tulburare de personalitate schizoidă",
            "tulburare de personalitate histrionică",
            "tulburare de personalitate antisocială",
            "tulburare de personalitate dependentă",
        ],
        "correct": "a",
    },
    {
        "stem": "Tulburarea de personalitate schizotipală poate include:",
        "options": [
            "idei de referință și gândire magică",
            "experiențe perceptive neobișnuite",
            "discurs vag sau ciudat și comportament excentric",
            "halucinații persistente cu pierderea insightului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate schizotipală este asociată cu anxietate "
            "socială ridicată, dar și cu credințe paranormale sau superstiții."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Cluster B (19–30) ——
    {
        "stem": "Clusterul B al tulburărilor de personalitate include:",
        "options": [
            "tulburarea de personalitate antisocială",
            "tulburarea de personalitate borderline",
            "tulburarea de personalitate narcisistă",
            "tulburarea de personalitate evitantă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Trăsătura centrală a tulburării de personalitate antisociale este:",
        "options": [
            "disprețul față de drepturile celorlalți",
            "încălcarea normelor sociale din adolescență",
            "teamă intensă de abandon și instabilitate afectivă",
            "retragere socială și lipsa dorinței de intimitate",
        ],
        "correct": "ab",
    },
    {
        "stem": "Pentru tulburarea de personalitate antisocială este necesar:",
        "options": [
            "vârsta de cel puțin 18 ani la evaluare",
            "istoric de încălcări din adolescență",
            "prezența obligatorie a unei psihoze",
            "absența oricărei impulsivități",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate antisocială:",
        "options": [
            "minciună, înșelăciune și impulsivitate",
            "iritabilitate, agresivitate și iresponsabilitate",
            "lipsa remușcării pentru acțiunile dăunătoare",
            "nevoie excesivă de a fi îngrijit și supunere",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tulburarea de personalitate borderline presupune, în principal:",
        "options": [
            "instabilitate a relațiilor, imaginii de sine și afectului",
            "impulsivitate ridicată",
            "grandiozitate stabilă și lipsă de empatie",
            "preferință constantă pentru solitudine",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate borderline:",
        "options": [
            "eforturi disperate de evitare a abandonului",
            "comportament suicidar sau autovătămare",
            "instabilitate afectivă și senzație de gol interior",
            "lipsa oricărei frici de respingere",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O pacientă alternează relații intense cu respingere, are frică de abandon, "
            "autovătămare și schimbări rapide de dispoziție. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate borderline",
            "tulburare de personalitate schizoidă",
            "tulburare de personalitate paranoidă",
            "tulburare de personalitate obsesiv-compulsivă",
        ],
        "correct": "a",
    },
    {
        "stem": "Comorbiditățile frecvente ale tulburării de personalitate borderline includ:",
        "options": [
            "episoade depresive și tulburări anxioase",
            "consum de substanțe",
            "tulburarea de stres posttraumatic",
            "tulburarea obsesiv-compulsivă ca regulă obligatorie",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tulburarea de personalitate narcisistă presupune:",
        "options": [
            "grandiozitate și nevoie de admirație",
            "lipsă de empatie și exploatarea celorlalți",
            "retragere socială și afect plat",
            "teamă de critică și evitare interpersonală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În tulburarea de personalitate narcisistă, stima de sine este adesea fragilă, "
            "iar lipsa admirației poate declanșa furie sau agresivitate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tulburarea de personalitate histrionică se caracterizează prin:",
        "options": [
            "emoționalitate excesivă și căutarea atenției",
            "disconfort când nu este în centrul atenției",
            "comportament seductiv sau teatral inadecvat",
            "indiferență față de laude sau critici",
        ],
        "correct": "abc",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate histrionică:",
        "options": [
            "emoții superficiale și schimbătoare",
            "dramatizare și sugestibilitate",
            "perceperea relațiilor ca mai intime decât sunt",
            "lipsa oricărei nevoie de validare socială",
        ],
        "correct": "abc",
    },
    # —— Cluster C (31–42) ——
    {
        "stem": "Clusterul C al tulburărilor de personalitate include:",
        "options": [
            "tulburarea de personalitate evitantă",
            "tulburarea de personalitate dependentă",
            "tulburarea de personalitate obsesiv-compulsivă",
            "tulburarea de personalitate schizotipală",
        ],
        "correct": "abc",
    },
    {
        "stem": "Elementele comune clusterului C includ:",
        "options": [
            "anxietate și teamă",
            "evitare și nevoie de control sau sprijin",
            "impulsivitate dramatică și grandiozitate",
            "gândire magică și excentricitate marcată",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea de personalitate evitantă presupune:",
        "options": [
            "reticență socială și sentimente de inadecvare",
            "hipersensibilitate la critică sau respingere",
            "lipsa dorinței de relații apropiate",
            "dispreț față de drepturile celorlalți",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate evitantă:",
        "options": [
            "evitarea activităților cu contact interpersonal",
            "frică de dezaprobare și sentiment de inferioritate",
            "inhibiție în situații noi din teamă de jenă",
            "nevoie de a fi în centrul atenției publice",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O persoană dorește relații, dar evită colegii de teamă să fie respinsă; "
            "se simte inferioară și nu își asumă proiecte noi. Tabloul sugerează:"
        ),
        "options": [
            "tulburare de personalitate evitantă",
            "tulburare de personalitate schizoidă",
            "tulburare de personalitate antisocială",
            "tulburare de personalitate narcisistă",
        ],
        "correct": "a",
    },
    {
        "stem": "Tulburarea de personalitate dependentă presupune:",
        "options": [
            "nevoie excesivă de a fi îngrijit",
            "comportament supus, agățat și teamă de separare",
            "grandiozitate și exploatarea celorlalți",
            "preferință constantă pentru solitudine",
        ],
        "correct": "ab",
    },
    {
        "stem": "Criterii frecvente în tulburarea de personalitate dependentă:",
        "options": [
            "dificultăți în decizii fără reasigurări",
            "disconfort când este singură",
            "căutarea rapidă a unei noi relații de sprijin",
            "lipsa oricărei frici de abandon",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Tulburarea de personalitate dependentă se asociază cu frică de incompetență, "
            "dependență de ghidaj și dificultăți de autonomie."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tulburarea de personalitate obsesiv-compulsivă se caracterizează prin:",
        "options": [
            "preocupare pentru ordine, perfecțiune și control",
            "perfecționism rigid și iresponsabilitate interpersonală redusă",
            "ritualuri de spălare pentru teamă de contaminare",
            "obsesii intruzive cu compulsii obligatorii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate obsesiv-compulsivă diferă de tulburarea "
            "obsesiv-compulsivă prin faptul că accentul cade pe:"
        ),
        "options": [
            "tiparul rigid de personalitate, nu pe obsesii și compulsii clinice",
            "perfecționism și control, nu pe ritualuri specifice",
            "absența oricărei preocupări pentru ordine",
            "prezența obligatorie a halucinațiilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate evitantă poate fi comorbidă cu tulburarea "
            "anxioasă socială."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Clusterul C include tulburarea de personalitate histrionică și "
            "tulburarea de personalitate antisocială."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Diferențieri și capcane (43–50) ——
    {
        "stem": (
            "Care pereche distinge corect două tulburări de personalitate din același cluster?"
        ),
        "options": [
            "paranoidă — suspiciune; schizoidă — detașare și afect plat",
            "borderline — instabilitate afectivă; narcisistă — grandiozitate",
            "evitantă — teamă de critică; dependentă — nevoie de îngrijire",
            "antisocială — teamă de abandon; histrionică — retragere socială",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un pacient interpretează remarci neutre ca atacuri, poartă ranchiuni "
            "și este hipervigilent la intențiile altora, fără halucinații. "
            "Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate paranoidă",
            "tulburare de personalitate schizotipală",
            "tulburare de personalitate borderline",
            "schizofrenie cu delir persistent",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "O persoană încalcă repetat legea, minte pentru profit, este impulsivă "
            "și nu simte remușcare; are 25 de ani. Diagnosticul probabil:"
        ),
        "options": [
            "tulburare de personalitate antisocială",
            "tulburare de personalitate narcisistă",
            "tulburare de personalitate dependentă",
            "tulburare de personalitate evitantă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații descriu corect tulburarea de personalitate schizotipală, "
            "nu tulburarea de personalitate schizoidă?"
        ),
        "options": [
            "gândire magică și comportament excentric",
            "experiențe perceptive neobișnuite",
            "preferință pentru solitudine fără excentricitate",
            "lipsa ideilor de referință sau a suspiciunii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate borderline și tulburarea de personalitate "
            "narcisistă pot fi ambele asociate cu relații conflictuale, dar borderline "
            "se distinge prin:"
        ),
        "options": [
            "instabilitate afectivă și frică de abandon",
            "autovătămare sau comportament suicidar",
            "grandiozitate stabilă ca trăsătură centrală",
            "lipsa impulsivității",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tulburarea de personalitate histrionică și tulburarea anxioasă socială "
            "pot implica disconfort social, dar histrionica se distinge prin:"
        ),
        "options": [
            "căutarea activă a atenției și comportament teatral",
            "emoții superficiale, schimbătoare și dramatizare",
            "evitarea contactului interpersonal din teamă de critică",
            "retragere preferențială și afect plat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În evaluarea tulburărilor de personalitate, este important să se distingă "
            "tiparul persistent de:"
        ),
        "options": [
            "simptome episodice ale unei tulburări de dispoziție",
            "efectele substanțelor sau ale unei afecțiuni medicale",
            "trăsături culturale normative, fără afectare",
            "orice trăsătură de personalitate din spectrul normal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Toate tulburările de personalitate din clusterul B necesită vârsta "
            "de cel puțin 18 ani pentru diagnostic."
        ),
        "tf": True,
        "correct_tf": False,
    },
]
