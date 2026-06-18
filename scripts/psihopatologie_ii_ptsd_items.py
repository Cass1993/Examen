"""Itemi — Psihopatologie II: tulburarea de stres posttraumatic."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PTSD_ITEMS: List[Item] = [
    # —— Definiție și expunere (1–8) ——
    {
        "stem": (
            "Tulburarea de stres posttraumatic apare, în principal, după expunerea la:"
        ),
        "options": [
            "moarte, amenințare cu moartea, vătămare gravă sau violență sexuală",
            "stres cotidian la locul de muncă, fără pericol real",
            "conflict marital fără componentă de violență",
            "eșec academic sau profesional izolat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care modalități de expunere la traumă pot declanșa tulburarea de stres posttraumatic?"
        ),
        "options": [
            "trăirea directă a evenimentului traumatic",
            "asistarea ca martor la traumă",
            "aflarea că o persoană apropiată a fost traumatizată",
            "expunerea repetată la detalii traumatice (de exemplu, cadre medicale)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Expunerea la traumă în tulburarea de stres posttraumatic poate include:",
        "options": [
            "experiența directă a evenimentului",
            "martoriatul evenimentului la altcineva",
            "aflarea despre trauma unei persoane apropiate",
            "exclusiv vizionarea la televizor a unui accident rutier",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un pompier expus repetat la detalii ale unor accidente grave poate dezvolta "
            "tulburarea de stres posttraumatic prin:"
        ),
        "options": [
            "expunere repetată la detalii traumatice în munca profesională",
            "trăirea directă a unei amenințări cu moartea",
            "aflarea despre boala unei rude îndepărtate",
            "stresul unui examen dificil",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Evenimentul traumatic în tulburarea de stres posttraumatic trebuie să implice, "
            "de regulă:"
        ),
        "options": [
            "moarte reală sau amenințată, vătămare gravă sau violență sexuală",
            "pericol iminent pentru viață sau integritate corporală",
            "orice neplăcere emoțională, indiferent de severitate",
            "conflict interpersonal fără componentă de pericol",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Aflarea că un copil al pacientului a fost victima unei agresiuni violente poate constitui:"
        ),
        "options": [
            "expunere indirectă la traumă, în sens diagnostic",
            "martoriat direct la eveniment",
            "stres cotidian fără relevanță clinică",
            "expunere validă doar dacă pacientul a văzut agresiunea",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Tulburarea de stres posttraumatic se dezvoltă după orice eveniment neplăcut, "
            "indiferent de severitate."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Expunerea la traumă poate fi directă, prin martoriat sau prin aflarea "
            "traumei unei persoane apropiate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Simptome: intruziune, evitare (9–16) ——
    {
        "stem": "Simptomele de intruziune în tulburarea de stres posttraumatic includ:",
        "options": [
            "flashback-uri sau retrăirea evenimentului",
            "amintiri sau gânduri intrusive despre traumă",
            "reacții fiziologice intense la indicii traumatice",
            "evitarea deliberată a oricărei amintiri",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un veteran aude un zgomot puternic și retrăiește momentul exploziei, "
            "cu transpirație și tahicardie. Aceasta ilustrează:"
        ),
        "options": [
            "intruziune — flashback cu reacție fiziologică",
            "evitare cognitivă a amintirilor",
            "hipervigilență fără retrăire",
            "anxietate generalizată, fără legătură cu traumă",
        ],
        "correct": "a",
    },
    {
        "stem": "Evitarea în tulburarea de stres posttraumatic se referă la:",
        "options": [
            "evitarea gândurilor sau amintirilor legate de traumă",
            "evitarea locurilor, persoanelor sau situațiilor asociate",
            "evitarea oricărei emoții, inclusiv cele pozitive",
            "căutarea activă a amintirilor pentru a le procesa",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O pacientă refuză să treacă pe strada unde a avut loc accidentul. "
            "Acest comportament indică:"
        ),
        "options": [
            "evitare comportamentală legată de traumă",
            "intruziune sub formă de flashback",
            "hipervigilență fără evitare",
            "tulburare obsesiv-compulsivă primară",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Modificările negative ale cognițiilor și dispoziției în tulburarea de stres "
            "posttraumatic pot include:"
        ),
        "options": [
            "vinovăție, rușine sau frică persistentă",
            "convingeri negative despre sine, lume sau alții",
            "detașare sau incapacitate de a simți emoții pozitive",
            "grandiozitate și dispoziție exaltată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Hiperactivarea în tulburarea de stres posttraumatic se manifestă prin:"
        ),
        "options": [
            "hipervigilență și stare de alertă crescută",
            "iritabilitate sau reacții exagerate de sperietură",
            "dificultăți de somn sau de concentrare",
            "lentoare psihomotorie și anhedonie izolată",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care simptome aparțin hiperactivării în tulburarea de stres posttraumatic?"
        ),
        "options": [
            "sare la cel mai mic zgomot — hipervigilență",
            "nu poate dormi din cauza gândurilor despre traumă",
            "evită complet discuția despre eveniment",
            "reacție de panică la un sunet similar celui traumatic",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Flashback-ul în tulburarea de stres posttraumatic diferă de o amintire obișnuită "
            "prin faptul că:"
        ),
        "options": [
            "persoana retrăiește evenimentul ca și cum s-ar întâmpla acum",
            "apar adesea reacții fiziologice intense",
            "este o amintire voluntară, controlată și distantă",
            "nu implică conținut legat de traumă",
        ],
        "correct": "ab",
    },
    # —— Criterii de timp și diferențiere (17–22) ——
    {
        "stem": (
            "Criteriul de durată pentru diagnosticul tulburării de stres posttraumatic "
            "presupune că simptomele:"
        ),
        "options": [
            "persistă peste o lună după evenimentul traumatic",
            "cauzează afectare semnificativă a funcționării",
            "nu sunt explicate mai bine de substanțe sau altă boală",
            "dispar obligatoriu în primele 48 de ore",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Reacția acută la stres (sub o lună) se deosebește de tulburarea de stres "
            "posttraumatic prin faptul că aceasta din urmă necesită:"
        ),
        "options": [
            "persistența simptomelor peste o lună",
            "afectare clinică semnificativă",
            "absența oricărui simptom de intruziune",
            "prezența obligatorie a unei psihoze",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Simptomele tulburării de stres posttraumatic nu trebuie atribuite în principal:"
        ),
        "options": [
            "efectelor substanțelor sau medicației",
            "unei alte afecțiuni medicale",
            "expunerii la un eveniment traumatic valid",
            "intoxicației acute care explică complet tabloul",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Detașarea afectivă în tulburarea de stres posttraumatic se referă la:"
        ),
        "options": [
            "incapacitatea de a simți emoții pozitive",
            "sentimentul de distanțare față de ceilalți",
            "grandiozitate și energie crescută",
            "pierderea interesului față de activități plăcute",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Tulburarea de stres posttraumatic necesită simptome care persistă peste o lună "
            "și produc afectare semnificativă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Evitarea în tulburarea de stres posttraumatic include evitarea gândurilor, "
            "locurilor și persoanelor asociate traumei."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Etiologie și vulnerabilitate (23–26) ——
    {
        "stem": (
            "Factori de vulnerabilitate la tulburarea de stres posttraumatic pot include:"
        ),
        "options": [
            "responsabilizare personală exagerată pentru traumă",
            "anxietate preexistentă sau istoric familial de tulburări",
            "familie instabilă sau lipsă de suport",
            "absența totală a oricărei reacții emoționale la traumă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Disocierea în momentul traumei este asociată, în unele studii, cu:",
        "options": [
            "risc crescut de tulburare de stres posttraumatic ulterior",
            "dificultăți de integrare a amintirii traumatice",
            "protecție garantată împotriva oricărui simptom",
            "absența oricărei reacții de evitare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Responsabilizarea exagerată („ar fi trebuit să previn”) după traumă poate:",
        "options": [
            "menține vinovăția și cognițiile negative",
            "îngreuna recuperarea și perpetua simptomele",
            "proteja automat împotriva flashback-urilor",
            "elimina nevoia de tratament psihologic",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Istoricul familial de tulburări anxioase poate crește vulnerabilitatea la "
            "tulburarea de stres posttraumatic."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Teoria reprezentării duale și tratament (27–30) ——
    {
        "stem": "Teoria reprezentării duale a memoriei traumatice postulează:",
        "options": [
            "memorie autobiografică accesibilă verbal",
            "memorie situațională legată de flashback-uri",
            "o singură reprezentare unitară, complet conștientă",
            "absența oricărei componente somatice a amintirii",
        ],
        "correct": "ab",
    },
    {
        "stem": "Flashback-urile sunt explicate, în teoria reprezentării duale, prin:",
        "options": [
            "activarea memoriei situaționale, mai puțin verbalizabile",
            "reexperiențierea senzorială a evenimentului traumatic",
            "lipsa oricărei amintiri legate de traumă",
            "funcționarea normală a memoriei autobiografice",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Tratamentele cu evidență pentru tulburarea de stres posttraumatic includ:"
        ),
        "options": [
            "terapia de expunere la amintiri traumatice",
            "restructurare cognitivă a cognițiilor posttraumatice",
            "desensibilizarea și reprocesarea prin mișcări oculare",
            "debriefing psihologic obligatoriu imediat după orice traumă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Debriefing-ul psihologic imediat după traumă este:",
        "options": [
            "controversat; poate fi contraproductiv la unii indivizi",
            "recomandat universal ca prevenție",
            "înlocuitorul terapiei de expunere validate",
            "interzis în toate ghidurile clinice actuale",
        ],
        "correct": "a",
    },
]
