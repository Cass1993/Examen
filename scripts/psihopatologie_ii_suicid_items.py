"""Itemi — Psihopatologie II: suicid — risc, evaluare, prevenție, intervenție."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SUICID_ITEMS: List[Item] = [
    # —— Definiție și ideatie (1–8) ——
    {
        "stem": "Ideea suicidară se referă la:",
        "options": [
            "gânduri despre moartea sau sinuciderea proprie",
            "tristețe tranzitorie fără gânduri despre moarte",
            "frică de moarte la altcineva",
            "dorința de a dormi mult după o zi obositoare",
        ],
        "correct": "a",
    },
    {
        "stem": "Intenția suicidară presupune, față de simpla ideatie:",
        "options": [
            "dorința sau hotărârea de a muri prin propria acțiune",
            "prezența unui plan concret de sinucidere",
            "absența oricărui gând legat de moarte",
            "frică normală de boală terminală",
        ],
        "correct": "a",
    },
    {
        "stem": "Planul suicidar include:",
        "options": [
            "modul, momentul sau mijloacele avute în vedere",
            "accesul la metode letale sau pregătirea actului",
            "doar starea de tristețe, fără detalii comportamentale",
            "refuzul de a discuta despre suferință",
        ],
        "correct": "ab",
    },
    {
        "stem": "Comportamentul suicidar non-fatal (tentativă) se deosebește de automutilarea non-suicidară prin faptul că:",
        "options": [
            "tentativa urmărește moartea, nu doar reglarea emoțională",
            "automutilarea non-suicidară vizează adesea eliberarea tensiunii",
            "ambele au întotdeauna același scop: moartea",
            "automutilarea exclude orice risc de vătămare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ideea suicidară pasivă („ar fi mai bine să mor”) diferă de cea activă prin faptul că:",
        "options": [
            "activa include dorința sau intenția de a se sinucide",
            "pasiva poate apărea fără plan sau intenție de acțiune",
            "pasiva presupune întotdeauna un plan detaliat",
            "activa exclude orice gând despre moarte",
        ],
        "correct": "ab",
    },
    {
        "stem": "Factori de risc pentru suicid pot include:",
        "options": [
            "tulburare depresivă sau bipolară",
            "tentativă anterioară de suicid",
            "izolare socială sau acces la mijloace letale",
            "rețea socială stabilă și suport constant",
        ],
        "correct": "abc",
    },
    {
        "stem": "Factori protectori împotriva suicidului includ:",
        "options": [
            "legături sociale semnificative și suport",
            "acces limitat la mijloace letale",
            "speranță și motive pentru a trăi",
            "consumul de alcool pentru a „ușura” durerea",
        ],
        "correct": "abc",
    },
    {
        "stem": "Prezența unui plan suicidar concret crește riscul iminent față de simpla ideatie.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Evaluare și semne (9–16) ——
    {
        "stem": "În evaluarea riscului suicidar, se investighează prioritar:",
        "options": [
            "ideea, intenția, planul și mijloacele disponibile",
            "tentative anterioare și factori precipitanți",
            "rețeaua de suport și factorii protectori",
            "exclusiv coeficientul de inteligență",
        ],
        "correct": "abc",
    },
    {
        "stem": "Semne de alarmă pentru risc suicidar pot include:",
        "options": [
            "predare de bunuri sau rezolvarea „treburilor”",
            "izolare bruscă sau rămas bun definitiv",
            "vorbe despre a fi o povară sau fără speranță",
            "planificarea unei vacanțe cu prietenii",
        ],
        "correct": "abc",
    },
    {
        "stem": "Un pacient spune: „Am pastile acasă și știu câte îmi trebuie.” Acest enunț indică:",
        "options": [
            "plan suicidar cu acces la mijloace",
            "risc crescut care necesită evaluare urgentă",
            "idee pasivă fără intenție de acțiune",
            "simptom obsesiv fără relevanță suicidară",
        ],
        "correct": "ab",
    },
    {
        "stem": "În evaluarea suicidului, întrebarea directă despre gânduri suicidare:",
        "options": [
            "este recomandată; nu „plantează” ideea la majoritatea pacienților",
            "permite estimarea riscului și planificarea intervenției",
            "trebuie evitată întotdeauna pentru a nu sugera suicidul",
            "înlocuiește evaluarea medicală în cazurile severe",
        ],
        "correct": "ab",
    },
    {
        "stem": "Tulburarea borderline de personalitate este asociată cu:",
        "options": [
            "risc crescut de automutilare și suicid",
            "instabilitate afectivă și impulsivitate",
            "absența oricărei idei suicidare pe parcursul vieții",
            "episoade de elație ca în manie",
        ],
        "correct": "ab",
    },
    {
        "stem": "Consumul de alcool în context suicidar poate:",
        "options": [
            "reduce inhibițiile și crește impulsivitatea",
            "agrava depresia și dezorganizarea",
            "proteja garantat împotriva tentativei",
            "interacționa cu medicamentele psihotrope",
        ],
        "correct": "abd",
    },
    {
        "stem": "Contractul de siguranță (safety plan) în criză suicidară:",
        "options": [
            "nu înlocuiește evaluarea clinică și monitorizarea",
            "poate include pași de autocontrol și contacte de urgență",
            "garantează absența oricărei tentative viitoare",
            "exclude spitalizarea când riscul este iminent",
        ],
        "correct": "ab",
    },
    {
        "stem": "Întrebarea directă despre suicid poate fi utilă în evaluarea riscului.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Intervenție și prevenție (17–24) ——
    {
        "stem": "În caz de risc suicidar iminent, prioritatea este:",
        "options": [
            "asigurarea siguranței imediate a persoanei",
            "evaluarea psihiatrică de urgență",
            "limitarea accesului la mijloace letale",
            "amânarea discuției până la următoarea ședință",
        ],
        "correct": "abc",
    },
    {
        "stem": "Spitalizarea psihiatrică involuntară poate fi indicată când:",
        "options": [
            "riscul suicidar este iminent și nu poate fi gestionat ambulatoriu",
            "persoana are plan concret și refuză tratamentul",
            "există doar tristețe ușoară, fără ideatie",
            "legea și protocoalele locale o permit în situația dată",
        ],
        "correct": "abd",
    },
    {
        "stem": "Prevenția suicidului pe termen lung poate include:",
        "options": [
            "tratamentul tulburării psihice de fond",
            "reducerea accesului la mijloace letale",
            "sprijinul rețelei sociale și psihoterapia",
            "plan de siguranță fără întrebare despre comportament autolesiv anterior",
        ],
        "correct": "abc",
    },
    {
        "stem": "După o tentativă de suicid, urmărirea este importantă deoarece:",
        "options": [
            "riscul de recidivă rămâne crescut",
            "perioada post-externare poate fi de risc",
            "tentativa anterioară nu influențează riscul viitor",
            "tratamentul poate reduce riscul pe termen lung",
        ],
        "correct": "abd",
    },
    {
        "stem": "Mitul „cine vorbește despre suicid nu se sinucide” este:",
        "options": [
            "fals; vorbele pot semnala risc real",
            "periculos, deoarece poate întârzia intervenția",
            "corect în toate cazurile clinice",
            "valabil doar la adolescenți",
        ],
        "correct": "ab",
    },
    {
        "stem": "La adolescenți, factori de risc suicidar pot include:",
        "options": [
            "bullying, excludere sau conflicte familiale",
            "tulburări de consum sau impulsivitate crescută",
            "rețea de suport stabilă și deschidere spre părinți",
            "identitate de gen neacceptată sau discriminare",
        ],
        "correct": "abd",
    },
    {
        "stem": "Liniile telefonice de criză au rolul de a:",
        "options": [
            "oferi sprijin imediat și evaluare preliminară",
            "orienta către servicii de urgență când e necesar",
            "înlocui tratamentul psihiatric de lungă durată",
            "reduce izolarea în momentul crizei",
        ],
        "correct": "abd",
    },
    {
        "stem": "Tentativa anterioară de suicid este un factor de risc pentru viitoare tentative.",
        "tf": True,
        "correct_tf": True,
    },
    # —— Capcane și sinteză (25–30) ——
    {
        "stem": "Care afirmații despre suicid sunt corecte?",
        "options": [
            "majoritatea persoanelor cu idei suicidare comunică suferința",
            "depresia netratată crește riscul suicidar",
            "suicidul apare doar la persoane cu psihoză",
            "planul concret și mijloacele cresc urgența",
        ],
        "correct": "abd",
    },
    {
        "stem": "Care afirmații despre suicid sunt greșite?",
        "options": [
            "ideea suicidară este mereu un semn de manipulare",
            "riscul dispare după ce persoana pare liniștită brusc",
            "evaluarea include intenția și planul",
            "factorii protectori pot reduce riscul",
        ],
        "correct": "ab",
    },
    {
        "stem": "Un pacient cu depresie majoră spune că „nu mai are sens.” Evaluarea următoare include:",
        "options": [
            "întrebări directe despre idee, plan și mijloace",
            "evaluarea tentativelor anterioare",
            "contactarea rețelei de suport, cu acord",
            "evitarea subiectului pentru a nu sugera suicidul",
        ],
        "correct": "abc",
    },
    {
        "stem": "Diferența dintre gânduri pasive și active de moarte este relevantă pentru:",
        "options": [
            "estimarea gradului de risc",
            "planificarea nivelului de intervenție",
            "diagnosticarea tulburării obsesiv-compulsive",
            "decizia privind siguranța imediată",
        ],
        "correct": "abd",
    },
    {
        "stem": "Suicidul este asociat doar cu tulburarea depresivă majoră, nu și cu alte afecțiuni.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Limitarea accesului la mijloace letale este o măsură de prevenție a suicidului.",
        "tf": True,
        "correct_tf": True,
    },
]
