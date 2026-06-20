"""Itemi — Psihologia personalității II: COMPORTAMENTALĂ (40 itemi, ID 12126–12165)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

COMPORTAMENTALA_ITEMS: List[Item] = [
    {
        "stem": (
            "Condiționarea clasică (Pavlov) presupune asocierea repetată "
            "stimulus–răspuns: un stimulus neutru devine condiționat."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În condiționarea operantă (Skinner), pedeapsa este echivalentul "
            "întăririi negative — ambele cresc probabilitatea comportamentului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Programul de întărire cu frecvență variabilă (ex. jocuri de noroc) "
            "produce cel mai stabil răspuns, greu de stins."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Bandura consideră agresivitatea un comportament învățat prin "
            "observare, nu un instinct pur."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Condiționarea operantă (Skinner) se bazează pe principiul:",
        "options": [
            "R → S: consecința după comportament determină probabilitatea repetării",
            "SNc + SN repetat → RN: asociere stimulus–răspuns reflex",
            "expunere → achiziție → acceptanță: învățare prin observare",
            "anticiparea evenimentelor canalizează procesele psihice (Kelly)",
        ],
        "correct": "a",
    },
    {
        "stem": "Învățarea observațională (Bandura) presupune:",
        "options": [
            "învățare prin observarea altora și modelare",
            "asocierea repetată a unui stimulus neutru cu unul necondiționat",
            "modificarea frecvenței comportamentului prin consecințe post-comportament",
            "evaluarea experiențelor după contribuția la dezvoltarea sinelui (Rogers)",
        ],
        "correct": "a",
    },
    {
        "stem": "Faza pre-condițională (CC) se caracterizează prin:",
        "options": [
            "SN → fără răspuns; SNc → RN (răspuns necondiționat reflex)",
            "SC → RC: stimulus condiționat declanșează răspuns condiționat",
            "SNc + SN repetat → RN: faza de achiziție",
            "R urmat de întărire: consecința crește frecvența comportamentului",
        ],
        "correct": "a",
    },
    {
        "stem": "Faza post-condițională (CC) înseamnă:",
        "options": [
            "SC (stimulus condiționat) → RC (răspuns condiționat)",
            "SN → fără răspuns; SNc → RN",
            "SNc + SN repetat până la asociere",
            "eliminarea întăririi → scăderea RC treptată",
        ],
        "correct": "a",
    },
    {
        "stem": "Achiziția, în condiționarea clasică, se referă la:",
        "options": [
            "formarea asocierii SN → SC prin perechi repetate SNc + SN",
            "memorarea modelului observat fără imitare imediată (Bandura)",
            "recompensarea treptată a apropierii de comportamentul țintă (shaping)",
            "scăderea RC când SC apare fără SNc (extincție)",
        ],
        "correct": "a",
    },
    {
        "stem": "Extincția în condiționarea clasică apare când:",
        "options": [
            "SC e prezentat repetat fără SNc → RC scade treptat",
            "întărirea consecinței e oprită după comportament operant",
            "modelul agresiv dispare din mediu (Bandura)",
            "stimulusul neutru e asociat cu un nou răspuns reflex",
        ],
        "correct": "a",
    },
    {
        "stem": "Experimentul «Micul Albert» (Watson & Rayner, 1920) a arătat:",
        "options": [
            "șobolan + zgomot → frică condiționată; generalizare la obiecte similare",
            "ton + poze violente → răspuns electrodermal condiționat",
            "cal = simbol al tatălui; anxietate prin refulare libidinală",
            "copiii imită agresivitatea unui model adult (Bobo doll)",
        ],
        "correct": "a",
    },
    {
        "stem": "Geer (1968), în condiționarea clasică, a condiționat:",
        "options": [
            "un ton + poze violente → răspuns electrodermal condiționat",
            "percepția controlului → reducerea stresului (fără control real)",
            "șobolan + zgomot → fobie la obiecte albe și blănoase",
            "salariu lunar → răspuns moderat la muncă (interval fix)",
        ],
        "correct": "a",
    },
    {
        "stem": "Dezensibilizarea sistematică (Wolpe) presupune:",
        "options": [
            "ierarhie de stimuli fobici + relaxare progresivă (CC terapeutică)",
            "pedeapsă imediată după comportament nedorit (CO aversivă)",
            "observarea unui model care face față fără frică (Bandura)",
            "interpretarea simbolică a fricii ca simbol Oedip (Freud)",
        ],
        "correct": "a",
    },
    {
        "stem": "Terapia aversivă (ex. Antabuse la alcoolism):",
        "options": [
            "asociază consumul cu consecințe neplăcute; eficacitate slabă la alcoolism, mai bună la enurezis/fumat",
            "elimină frica prin expunere graduală și relaxare (Wolpe)",
            "recompensează treptat apropierile de sobrietate (shaping Skinner)",
            "funcționează prin întărire negativă — eliminarea poftei ca recompensă",
        ],
        "correct": "a",
    },
    {
        "stem": "La condiționarea clasică, diferența față de operantă include:",
        "options": [
            "SN devine SC; ordinea: SNc + SN → RN (nu R apoi consecință)",
            "consecința după R determină frecvența; SN nu devine SC",
            "modelul observat e memorat fără imitare obligatorie",
            "anticiparea canalizează procesele psihice, nu asocierea reflexă",
        ],
        "correct": "a",
    },
    {
        "stem": "Întărirea pozitivă (Skinner) înseamnă:",
        "options": [
            "adăugarea unui stimul plăcut → crește probabilitatea comportamentului",
            "eliminarea unui stimul aversiv → crește probabilitatea comportamentului",
            "adăugarea unui stimul aversiv → scade probabilitatea comportamentului",
            "eliminarea unui stimul plăcut → scade probabilitatea comportamentului",
        ],
        "correct": "a",
    },
    {
        "stem": "Întărirea negativă (Skinner) înseamnă:",
        "options": [
            "eliminarea unui stimul aversiv → crește probabilitatea comportamentului",
            "adăugarea unui stimul plăcut → crește probabilitatea comportamentului",
            "adăugarea unui stimul aversiv → scade probabilitatea comportamentului",
            "eliminarea recompensei → scăderea treptată a răspunsului condiționat",
        ],
        "correct": "a",
    },
    {
        "stem": "Shaping (modelare, Skinner) presupune:",
        "options": [
            "recompensarea treptată a apropierii de comportamentul țintă",
            "asocierea repetată SN + SNc până la formarea SC",
            "observarea modelului urmată de imitare spontană (Bandura)",
            "prezentarea ierarhice a stimuli fobici cu relaxare (Wolpe)",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi autor–tip de învățare sunt corecte?",
        "options": [
            "Pavlov — condiționare clasică (asociere stimulus–răspuns)",
            "Skinner — condiționare operantă (consecința determină probabilitatea)",
            "Bandura — condiționare clasică (SN devine SC)",
            "Wolpe — învățare observațională (Bobo doll)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi fază CC–descriere sunt corecte?",
        "options": [
            "Pre-condițională — SN fără răspuns; SNc → RN",
            "Condițională — SNc + SN repetat → RN",
            "Post-condițională — SNc + SN repetat (achiziție)",
            "Condițională — SC → RC (răspuns condiționat stabilit)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Cazul «Micul Hans» — Freud vs Wolpe:",
        "options": [
            "Freud — Oedip/simbolism: calul simbolizează tatăl",
            "Wolpe — condiționare simplă, tratabilă prin dezensibilizare",
            "Freud — condiționare clasică: ton + frică",
            "Wolpe — interpretare simbolică a libido refulat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi tip întărire–efect (Skinner) sunt corecte?",
        "options": [
            "Întărire pozitivă — adăugare stimul plăcut → ↑ comportament",
            "Întărire negativă — eliminare stimul aversiv → ↑ comportament",
            "Pedeapsă — eliminare stimul aversiv → ↑ comportament",
            "Întărire negativă — adăugare stimul aversiv → ↓ comportament",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care distincții pedeapsă vs întărire negativă sunt corecte?",
        "options": [
            "Pedeapsa ↓ probabilitatea comportamentului",
            "Întărirea negativă ↑ probabilitatea (prin eliminarea aversivului)",
            "Pedeapsa ↑ probabilitatea prin eliminarea stimulului aversiv",
            "Întărirea negativă = adăugarea unui stimul neplăcut",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi program întărire–exemplu sunt corecte?",
        "options": [
            "Interval fix — salariu lunar",
            "Frecvență fixă — plată la bucată",
            "Interval variabil — jocuri de noroc",
            "Frecvență variabilă — salariu lunar",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi program–efect asupra răspunsului sunt corecte?",
        "options": [
            "Interval fix — răspuns moderat",
            "Frecvență fixă — răspuns puternic",
            "Frecvență variabilă — răspuns moderat, ușor de stins",
            "Interval variabil — răspuns moderat (ex. pescuit)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Bandura — efecte imitative directe:",
        "options": [
            "Imitativ direct — copiază exact comportamentul modelului",
            "Contraimitativ direct — face opusul comportamentului modelului",
            "Imitativ indirect — aceeași clasă comportamentală, formă diferită",
            "Contraimitativ indirect — inhibiție față de clasa comportamentală",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi concept CC–descriere sunt corecte?",
        "options": [
            "Generalizare — RC la stimuli similari cu SC",
            "Discriminare — RC diferențiat doar la SC specific",
            "Extincție — RC crește când SC apare fără SNc",
            "Achiziție — RC scade când SNc lipsește",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care aplicații ale condiționării clasice sunt corecte?",
        "options": [
            "Fobii — formare prin asociere traumată",
            "Marketing — asocierea brandului cu emoții plăcute",
            "Shaping — recompensarea apropierii treptate de țintă",
            "Interpretarea simbolică a fricii ca simbol Oedip (Freud)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care enunțuri despre condiționarea clasică (CC) sunt corecte?",
        "options": [
            "Faza condițională: SNc + SN repetat → RN",
            "Post-condițională: SC → RC",
            "Concepte: achiziție, generalizare, discriminare, extincție",
            "Extincția la fobii traumatice/PTSD e ușoară, fără reactivare",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre condiționarea operantă (CO) sunt corecte?",
        "options": [
            "R → S: consecința după comportament determină probabilitatea",
            "Shaping = recompensarea treptată a apropierii de țintă",
            "Întărire pozitivă = adăugare plăcut; negativă = eliminare aversiv",
            "SN + SNc repetat → SN devine SC (ca la Pavlov)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care programe de întărire și efecte (Skinner) sunt corecte?",
        "options": [
            "Interval fix (salariu) — răspuns moderat",
            "Frecvență fixă (plată la bucată) — răspuns puternic",
            "Frecvență variabilă (jocuri noroc) — cel mai stabil, greu de stins",
            "Interval variabil (pescuit) — cel mai stabil, greu de stins",
        ],
        "correct": "abc",
    },
    {
        "stem": "Bandura (1961, Bobo doll) — etapele învățării observaționale:",
        "options": [
            "Expunere la model",
            "Achiziție (memorarea comportamentului observat)",
            "Acceptanță (imitare spontană)",
            "Extincție (SC fără SNc → RC scade)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Bandura — efecte imitative indirecte:",
        "options": [
            "Imitativ indirect — aceeași clasă comportamentală, altă formă",
            "Contraimitativ indirect — inhibiție față de clasa comportamentală",
            "Imitativ indirect — nu copiază exact, ci transferă clasa comportamentală",
            "Contraimitativ direct — face opusul comportamentului modelului",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre CC vs CO sunt corecte?",
        "options": [
            "CC: SNc + SN → RN; SN devine SC",
            "CO: R apoi consecință; frecvența R e modificată",
            "CC: răspuns reflex; CO: comportament voluntar/emis",
            "CO: SC → RC fără implicarea SNc",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre experimente CC/IO sunt corecte?",
        "options": [
            "Micul Albert (1920): șobolan + zgomot → frică; generalizare",
            "Geer (1968): ton + poze violente → răspuns electrodermal",
            "Bobo doll (1961): agresivitate învățată prin observare",
            "Geer (1970): percepția controlului reduce stresul",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre aplicații comportamentale sunt corecte?",
        "options": [
            "Dezensibilizare Wolpe — CC terapeutică: ierarhie + relaxare",
            "Terapie aversivă — Antabuse slab la alcoolism; mai bun la enurezis",
            "Marketing — asociere brand–emoție plăcută (CC)",
            "Shaping — asociere SN + SNc pentru formarea SC",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care enunțuri despre cele 3 tipuri de învățare sunt corecte?",
        "options": [
            "CC (Pavlov) — asociere repetată stimulus–răspuns",
            "CO (Skinner) — consecința determină probabilitatea comportamentului",
            "IO (Bandura) — învățare prin observarea altora",
            "Cele trei mecanisme: asociere reflexă, consecințe, modelare socială",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care enunțuri despre terminologia CC (Pavlov) sunt corecte?",
        "options": [
            "SN — stimulus neutru, inițial fără răspuns reflex",
            "SNc — stimulus necondiționat → RN (răspuns necondiționat)",
            "SC — stimulus condiționat (fost SN) → RC",
            "RC — răspuns condiționat elicitate de SC (fost SN)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care enunțuri despre programele de întărire (Skinner) sunt corecte?",
        "options": [
            "Interval fix — salariu lunar; răspuns moderat",
            "Frecvență fixă — plată la bucată; răspuns puternic",
            "Interval variabil — pescuit; răspuns moderat",
            "Frecvență variabilă — jocuri de noroc; cel mai stabil, greu de stins",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set sintetizează abordarea comportamentală?",
        "options": [
            "CC Pavlov: faze, generalizare/discriminare/extincție; Albert, Geer 1968",
            "CO Skinner: R→S, întărire/pedeapsă, shaping, programe (FV cel mai stabil)",
            "IO Bandura: expunere–achiziție–acceptanță; agresivitate învățată",
            "Aplicații: Wolpe (dezensibilizare), aversivă; extincție dificilă la PTSD",
        ],
        "correct": "abcd",
    },
]


def _count_dist(rows: List[Item]) -> Dict[str, int]:
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


SEG_DIST_40 = {"1": 14, "2": 10, "3": 8, "4": 4, "TF": 4}

assert len(COMPORTAMENTALA_ITEMS) == 40
assert _count_dist(COMPORTAMENTALA_ITEMS) == SEG_DIST_40
