"""Itemi — Educație vs învățare, eficiență și succes (20 itemi, ID 10671–10690)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

EDUCATIE_INVATARE_ITEMS: List[Item] = [
    # —— 1–5: distincții fundamentale ——
    {
        "stem": (
            "Învățarea este o activitate umană permanentă, începută din prima clipă a "
            "vieții, care dezvoltă, transformă și creează cunoaștere — nu se limitează "
            "la perioada școlară formală."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare diferențiază cel mai clar învățarea de educație?"
        ),
        "options": [
            "învățarea poate apărea spontan și continuă în viața de zi cu zi; "
            "educația este proces organizat, cu obiective și curriculum",
            "educația și învățarea sunt același proces — distincția e instituțională, "
            "fără consecințe practice",
            "învățarea se produce în principal în instituții, educația în afara lor",
            "educația apare fără planificare, învățarea presupune programă strictă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două elemente definesc educația ca proces formal și organizat?"
        ),
        "options": [
            "obiective didactice stabilite și curriculum structurat",
            "valori și finalități sociale asumate instituțional",
            "orice modificare accidentală de comportament din mediu",
            "memorarea mecanică ca singur criteriu de reușită",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei componente descriu succesul autentic în învățare, dincolo de "
            "memorarea mecanică?"
        ),
        "options": [
            "înțelegerea sensului și a relațiilor dintre idei",
            "aplicarea cunoștințelor în situații noi — transfer",
            "organizarea informației și autoreglarea parcursului",
            "repetarea fidelă a textului fără reorganizare mentală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În piramida învățării (niveluri de retenție), activitățile asociate cu "
            "procente mai mari de păstrare a informației includ:"
        ),
        "options": [
            "implicarea activă, predarea către alții, aplicarea practică și discuția",
            "lectura pasivă și ascultarea neinteractivă a expunerii",
            "sublinierea mecanică a textului fără reflecție",
            "copierea conținutului de pe tablă fără procesare",
        ],
        "correct": "a",
    },
    # —— 6–10: învățare continuă, transfer, educație ghidată ——
    {
        "stem": (
            "Care două distincții între învățare și educație sunt formulate corect?"
        ),
        "options": [
            "învățarea poate avea loc în afara instituțiilor; educația presupune "
            "organizare intenționată",
            "învățarea transformă cunoașterea pe tot parcursul vieții; educația "
            "orientează dezvoltarea spre obiective asumate",
            "educația precede orice formă de învățare la sugar",
            "învățarea formală exclude dimensiunea socială sau valorică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei activități din piramida învățării favorizează retenția mai "
            "mare decât lectura pasivă?"
        ),
        "options": [
            "aplicarea practică a cunoștințelor în exerciții și situații reale",
            "discuția și dezbaterea pe baza materialului studiat",
            "predarea sau explicarea conținutului către colegi",
            "ascultarea neinteractivă a unei prelegeri lungi, fără participare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Transferul în învățare înseamnă că elevul:"
        ),
        "options": [
            "folosește ceea ce a învățat într-un context nou, diferit de cel al lecției",
            "reproduce mecanic aceeași formulă din manual în caiet",
            "obține scor similar la teste repetate din același capitol",
            "memorează lista de termeni fără a le aplica în sarcini",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Autoreglarea în învățare presupune că elevul:"
        ),
        "options": [
            "își monitorizează înțelegerea și progresul",
            "își ajustează strategiile când observă dificultăți",
            "urmează indicațiile profesorului fără reflecție asupra propriului parcurs",
            "renunță la planificarea personală în favoarea notei finale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Educația se deosebește de învățarea incidentală prin faptul că:"
        ),
        "options": [
            "este ghidată de obiective, curriculum și finalități sociale asumate",
            "apare spontan, fără planificare sau evaluare",
            "se limitează la experiențe de joacă din prima copilărie",
            "exclude feedback-ul și evaluarea formativă",
        ],
        "correct": "a",
    },
    # —— 11–15: rolul învățării, activ vs pasiv, educație organizată ——
    {
        "stem": (
            "Care patru formulări descriu corect rolul învățării ca activitate "
            "permanentă?"
        ),
        "options": [
            "dezvoltă capacități cognitive și comportamentale pe tot parcursul vieții",
            "transformă experiențele și reprezentările anterioare",
            "creează și reorganizează cunoaștere, nu o stochează pasiv",
            "începe din primele interacțiuni cu mediul, nu la intrarea în școală",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Față de lectura pasivă, învățarea activă în clasă:"
        ),
        "options": [
            "solicită implicarea elevului în procesare și decizie",
            "favorizează retenția mai durabilă a informației",
            "profesorul își pierde rolul de ghidare în activitatea activă",
            "reduce la minimum timpul alocat expunerii conținutului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Organizarea cunoștințelor în învățare reușită presupune:"
        ),
        "options": [
            "legarea informației noi de structuri existente și crearea de sens",
            "acumularea de enunțuri izolate fără relații între ele",
            "memorarea ordinii exacte a paginilor din manual",
            "repetarea vocală fără înțelegere până la oboseală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Educația și învățarea sunt același proces; distincția dintre ele este "
            "una instituțională, fără consecințe practice pentru planificare sau evaluare."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei caracteristici aparțin educației ca proces organizat?"
        ),
        "options": [
            "planificare didactică și obiective de învățare",
            "curriculum și evaluare aliniate la competențe",
            "transmitere de valori și finalități sociale",
            "învățare accidentală, fără intenție pedagogică",
        ],
        "correct": "abc",
    },
    # —— 16–20: piramida, eficiență, sinteză ——
    {
        "stem": (
            "„Predarea către alții” apare în piramida învățării ca activitate "
            "eficientă deoarece:"
        ),
        "options": [
            "obligă elevul să reorganizeze și să explice materialul cu propriile cuvinte",
            "înlocuiește nevoia de înțelegere — e suficient să citești textul altcuiva",
            "e eficientă în principal la exerciții de calcul, nu la explicări verbale",
            "presupune transmiterea conținutului fără ca elevul să fi înțeles tema",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două idei leagă eficiența învățării școlare de succesul real al "
            "elevului?"
        ),
        "options": [
            "înțelegere profundă, nu suprafața memorării",
            "capacitatea de a aplica și transfera în situații diverse",
            "viteza de copiere a notițelor de pe tablă",
            "numărul de pagini parcurse fără reflecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru activități sunt plasate în zona superioară a piramidei "
            "retenției (procente ridicate de păstrare)?"
        ),
        "options": [
            "învățare prin implicare activă — ex. rezolvare de probleme",
            "predare sau explicare către colegi",
            "aplicare practică în exerciții și proiecte",
            "discuție și dezbatere pe baza materialului",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Memorarea mecanică fără înțelegere:"
        ),
        "options": [
            "poate funcționa pe termen scurt la test, dar nu asigură succes durabil",
            "este singurul indicator valid al progresului școlar",
            "garantează transferul automat în orice context nou",
            "înlocuiește nevoia de organizare și autoreglare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Eficiența unei lecții crește cel mai probabil când elevul:"
        ),
        "options": [
            "procesează activ materialul — aplică, discută sau explică altora",
            "ascultă pasiv, fără întrebări sau sarcini de rezolvare",
            "memorează definiții fără a le lega de exemple concrete",
            "evită activitățile care solicită gândirea și reorganizarea informației",
        ],
        "correct": "a",
    },
]

assert len(EDUCATIE_INVATARE_ITEMS) == 20
