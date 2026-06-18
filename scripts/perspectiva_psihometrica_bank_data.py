"""Itemi — Perspectiva psihometrică."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PSIHOMETRIC_ITEMS: List[Item] = [
    # —— Măsurare și scor brut (1–6) ——
    {
        "stem": "Măsurarea psihometrică presupune, în principal:",
        "options": [
            "atribuirea unei valori numerice unui construct psihologic",
            "eșantionarea comportamentelor relevante pentru construct",
            "descrierea calitativă, fără posibilitate de comparare",
            "eliminarea oricărei variabilități individuale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Scorul brut obținut la un test are sens diagnostic util doar atunci "
            "când este comparat cu o populație de referință."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Ce caracterizează scorul brut la un test?",
        "options": [
            "reflectă performanța directă la itemi",
            "nu are, singur, semnificație diagnostică fără norme",
            "este echivalentul unui percentile fără calcul suplimentar",
            "elimină nevoia de standardizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul clasic al măsurătorii, scorul obținut este egal cu scorul real "
            "plus eroarea de măsurare. Aceasta înseamnă că:"
        ),
        "options": [
            "orice scor observat include o componentă de eroare",
            "scorul real nu poate fi cunoscut perfect, ci estimat",
            "eroarea de măsurare este mereu zero la teste standardizate",
            "scorul obținut este identic cu adevărul psihologic fără reziduu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un adolescent obține 34 de răspunsuri corecte la un test de aptitudini. "
            "Fără norme, acest număr:"
        ),
        "options": [
            "nu permite interpretarea comparativă a nivelului",
            "este un scor brut, nu încă standardizat",
            "indică automat un coeficient de inteligență de 100",
            "înlocuiește nevoia de populație de referință",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Scorul brut poate fi interpretat direct ca diagnostic clinic, "
            "fără norme sau transformări."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Standardizare (7–12) ——
    {
        "stem": "Standardizarea unui test presupune uniformitate în:",
        "options": [
            "proba sau situația de stimulare prezentată",
            "administrarea și scorarea testului",
            "interpretarea: același scor are aceeași semnificație",
            "administrarea testului cu formulări diferite de itemi între subiecți",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă doi candidați obțin același scor brut la un test standardizat, "
            "de ce ar trebui interpretarea lor să fie echivalentă?"
        ),
        "options": [
            "standardizarea conferă același sens aceluiași scor",
            "normele și regulile de interpretare sunt comune",
            "scorurile brute diferite au mereu același sens",
            "standardizarea elimină nevoia de populație de referință",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce presupune standardizarea probei la un test?",
        "options": [
            "aceleași condiții de prezentare a materialului",
            "aceleași instrucțiuni de lucru",
            "itemi diferiți pentru fiecare persoană, fără regulă",
            "absența oricărui protocol de administrare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce include standardizarea administrării și a scorării?",
        "options": [
            "reduce variabilitatea datorată procedurii",
            "permite compararea rezultatelor între persoane",
            "reducerea semnificativă a erorii de măsurare, nu eliminarea ei",
            "înlocuiește nevoia de norme",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce presupune standardizarea interpretării scorurilor?",
        "options": [
            "se bazează pe norme și transformări convenite",
            "permite comunicarea rezultatelor între specialiști",
            "face inutilă orice populație de referință",
            "exclude utilizarea percentilelor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un test poate fi standardizat la administrare, dar să nu aibă norme "
            "actualizate. Consecința este că:"
        ),
        "options": [
            "interpretarea comparativă rămâne limitată sau incertă",
            "scorul brut nu poate fi plasat sigur față de populația actuală",
            "standardizarea administrării devine inutilă",
            "nu mai este nevoie de reguli de scorare",
        ],
        "correct": "ab",
    },
    # —— Normativă versus ipsativă (13–20) ——
    {
        "stem": "Măsurarea normativă se caracterizează prin:",
        "options": [
            "comparație interindividuală cu o normă de grup",
            "scor absolut interpretat față de populația de referință",
            "comparație doar cu preferințele proprii ale subiectului",
            "format obligatoriu de tip forced-choice",
        ],
        "correct": "ab",
    },
    {
        "stem": "Măsurarea ipsativă se caracterizează prin:",
        "options": [
            "comparație intraindividuală, cu propriul profil",
            "format de tip forced-choice sau ierarhie a preferințelor",
            "comparație directă cu media populației la fiecare item",
            "scor absolut independent de alegerile subiectului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce caracterizează instrumentele cu abordare ipsativă, cum ar fi "
            "inventarul Jackson sau tipologia Myers-Briggs?"
        ),
        "options": [
            "subiectul alege între opțiuni, nu raportează un nivel absolut",
            "profilul reflectă ordinea preferințelor personale",
            "scorul este mereu un percentile normativ pe fiecare scală",
            "nu există nicio comparație în cadrul profilului propriu",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Majoritatea testelor psihometrice clasice folosesc măsurare normativă. "
            "Ce înseamnă aceasta?"
        ),
        "options": [
            "scorul se interpretează față de o populație de referință",
            "comparația principală este interindividuală",
            "profilul reflectă doar ordinea preferințelor interne",
            "formatul este obligatoriu forced-choice ipsativ",
        ],
        "correct": "ab",
    },
    {
        "stem": "Cum se interpretează un scor mare pe o scală în măsurarea ipsativă?",
        "options": [
            "interpretarea este relativă în cadrul profilului personal",
            "nu se poate deduce automat un nivel normativ înalt",
            "este identică cu un scor z peste media populației",
            "exclude orice ierarhizare a preferințelor",
        ],
        "correct": "ab",
    },
    {
        "stem": "Prin ce sunt definite, de regulă, normele unui test?",
        "options": [
            "permit transformarea scorului brut în scor standardizat",
            "necesită un eșantion reprezentativ",
            "sunt identice pentru toate vârstele, fără excepții",
            "elimină orice eroare de măsurare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Normele pentru testele de aptitudini sunt adesea diferențiate pe vârstă, "
            "iar cele pentru personalitate pot fi diferențiate pe gen."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Măsurarea normativă și ipsativă oferă aceleași informații despre "
            "poziția persoanei față de populație."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Scale de măsurare și scoruri (21–30) ——
    {
        "stem": "Scala nominală de măsurare permite, în principal:",
        "options": [
            "clasificarea în categorii distincte",
            "calculul modului și al frecvențelor",
            "calculul mediei aritmetice cu sens psihologic direct",
            "ordonarea persoanelor pe o ierarhie clară",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scala ordinală de măsurare permite, în principal:",
        "options": [
            "ordonarea valorilor, fără distanțe egale garantate",
            "utilizarea medianei și a percentilelor",
            "calculul varianței cu interpretare strictă a distanței",
            "transformarea directă în scor z fără alte presupuneri",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scala de interval permite, în principal:",
        "options": [
            "calculul mediei și al varianței",
            "utilizarea corelației Pearson",
            "transformarea în percentile cu distanțe egale garantate",
            "clasificarea doar în categorii fără ordine",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scala de raport permite, în principal:",
        "options": [
            "transformări precum scorul z, scorul T sau coeficientul de inteligență",
            "origine absolută sau raport proporțional cu zero real",
            "doar numărarea categoriilor fără ordine",
            "exclusiv mediană, fără alte statistici",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Transformarea liniară a scorului z în scor T folosește formula: "
            "scor T = 50 + 10 × scor z."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La scala Wechsler, coeficientul de inteligență are media 100 "
            "și deviația standard 15."
        ),
        "options": [
            "corespunde unei transformări liniare a scorului z",
            "facilitează interpretarea comparativă",
            "are media 50 și deviația standard 10, ca scorul T",
            "nu necesită norme de populație",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scorurile standardizate liniar:",
        "options": [
            "păstrează forma distribuției originale",
            "includ scorul z, scorul T și coeficientul de inteligență Wechsler",
            "sunt identice cu percentilele ca tip de transformare",
            "schimbă forma distribuției în mod obligatoriu",
        ],
        "correct": "ab",
    },
    {
        "stem": "Scorurile standardizate neliniare includ:",
        "options": [
            "percentilele",
            "staninele, cu nouă intervale",
            "scorul brut fără nicio transformare",
            "doar media și deviația standard brute",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Percentilele transformă distribuția în formă uniformă. Consecința este că:"
        ),
        "options": [
            "diferențele din zonele extreme pot fi comprimate",
            "transformarea este neliniară, spre deosebire de scorul z",
            "percentilele păstrează exact forma distribuției originale",
            "nu pot fi folosite în interpretarea clinică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pe o scală nominală se poate calcula în mod corect media aritmetică "
            "a categoriilor, ca și pe o scală de interval."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Clasificarea instrumentelor (31–36) ——
    {
        "stem": "Criterii frecvente de clasificare a instrumentelor psihometrice:",
        "options": [
            "constructul măsurat: aptitudine, personalitate sau interese",
            "unidimensional versus multidimensional",
            "mod de administrare: hârtie, computer sau aparate",
            "absența oricărui format de răspuns",
        ],
        "correct": "abc",
    },
    {
        "stem": "Alte criterii de clasificare a instrumentelor psihometrice:",
        "options": [
            "administrare individuală versus colectivă",
            "auto-evaluare versus hetero-evaluare",
            "tip de sarcină: test versus chestionar",
            "exclusiv validitate, fără fidelitate",
        ],
        "correct": "abc",
    },
    {
        "stem": "Formate de răspuns în instrumentele psihometrice:",
        "options": [
            "deschis sau închis",
            "scală Likert sau forced-choice",
            "ranking sau ierarhizare a preferințelor",
            "doar răspuns binar, fără alte formate",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un inventar de personalitate cu mai multe scale pentru trăsături diferite "
            "este, de regulă, multidimensional."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Un test de inteligență administrat individual, cu răspunsuri deschise "
            "la unele subteste, poate combina hetero-evaluare și format deschis."
        ),
        "options": [
            "examinatorul notează răspunsurile după barem",
            "unele subteste permit răspunsuri elaborate",
            "exclude orice componentă de scorare standardizată",
            "este obligatoriu auto-administrat în grup",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce caracterizează chestionarul cu scală Likert?",
        "options": [
            "permite cuantificarea intensității acordului",
            "se încadrează adesea la tipul chestionar, nu test de aptitudini",
            "este identic cu formatul forced-choice ipsativ",
            "nu poate fi administrat pe computer",
        ],
        "correct": "ab",
    },
    # —— Fidelitate și validitate (37–44) ——
    {
        "stem": "Toate instrumentele psihometrice trebuie evaluate în privința:",
        "options": [
            "validității",
            "fidelității",
            "discriminării itemilor, ca regulă obligatorie",
            "dificultății itemilor, indiferent de tipul testului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Discriminarea și dificultatea itemului sunt evaluate, în principal, "
            "la testele de aptitudini sau de inteligență."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Tipuri de fidelitate includ:",
        "options": [
            "test–retest și forme alternative",
            "split-half și coeficientul alfa Cronbach",
            "formula Kuder-Richardson 20 pentru itemi cu două variante",
            "validitatea de fațadă, ca tip de fidelitate",
        ],
        "correct": "abc",
    },
    {
        "stem": "Tipuri de validitate includ:",
        "options": [
            "validitate de conținut și de criteriu",
            "validitate de construct: convergentă, discriminativă, factorială",
            "validitate de fațadă, când subiectul prezintă o imagine socială dorită",
            "split-half, ca formă de validitate",
        ],
        "correct": "abc",
    },
    {
        "stem": "Validitatea de criteriu poate fi:",
        "options": [
            "predictivă, dacă testul anticipează un rezultat viitor",
            "concurentă, dacă testul se compară cu un criteriu actual",
            "factorială, ca singur tip posibil de validitate",
            "identică cu fidelitatea test–retest",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce demonstrează validitatea de construct convergentă?",
        "options": [
            "susține că instrumentul măsoară ceea ce pretinde",
            "se verifică prin corelații cu măsuri similare",
            "exclude orice corelație cu alte teste",
            "este echivalentă cu validitatea de fațadă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Fidelitatea și validitatea măsoară același lucru: dacă un test este "
            "fidel, este automat și valid pentru orice scop."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Pentru ce se folosește eroarea standard a măsurătorii?",
        "options": [
            "interval de încredere de 95% folosește aproximativ ±2 erori standard",
            "interval de încredere de 99% folosește aproximativ ±3 erori standard",
            "eroarea standard este zero la orice test perfect",
            "intervalul exclude nevoia de fidelitate",
        ],
        "correct": "ab",
    },
    # —— Evaluare computerizată și perspective (45–50) ——
    {
        "stem": "Evaluarea computerizată oferă avantaje precum:",
        "options": [
            "eficiență în administrare, scorare și raportare",
            "posibilitatea testării adaptative computerizate",
            "reducerea erorii de măsurare prin standardizare, nu eliminarea ei",
            "absența nevoii de validare a instrumentului",
        ],
        "correct": "ab",
    },
    {
        "stem": "Testarea adaptivă computerizată presupune:",
        "options": [
            "selectarea itemului următor în funcție de răspunsul anterior",
            "estimare mai precisă, adesea cu mai puțini itemi",
            "aceeași listă fixă de itemi pentru toți subiecții",
            "cost redus garantat în orice implementare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Testarea adaptivă computerizată poate fi mai precisă și mai scurtă, "
            "dar implică de obicei costuri mai mari de dezvoltare, deoarece:"
        ),
        "options": [
            "necesită o bancă calibrată de itemi",
            "algoritmul selectează itemul următor după fiecare răspuns",
            "folosește aceeași probă fixă pentru toți subiecții",
            "exclude orice administrare pe computer",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce caracterizează perspectiva psihometrică, de tip nomotetic?",
        "options": [
            "accent pe generalizare și norme de grup",
            "interpretare comparativă a scorurilor",
            "accent exclusiv pe unicitatea unui singur caz",
            "respingerea oricărei standardizări",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce caracterizează perspectiva clinică, de tip idiografic?",
        "options": [
            "psihometria este instrument, nu scop în sine",
            "datele obiective se integrează cu contextul cazului",
            "exclude utilizarea oricărui test standardizat",
            "respinge compararea cu normele de grup",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În practica clinică, un test psihometric standardizat înlocuiește "
            "complet înțelegerea idiografică a cazului."
        ),
        "tf": True,
        "correct_tf": False,
    },
]
