"""Itemi — stiluri și preferințe de învățare VARK (20 itemi, ID 10731–10750)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

VARK_ITEMS: List[Item] = [
    # —— 1–10: model VARK, cele patru stiluri ——
    {
        "stem": (
            "Chestionarul VARK indică preferințe de învățare și modalități la care elevul "
            "răspunde mai ușor — nu etichete fixe sau tipuri permanente de personalitate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Acronimul VARK desemnează patru preferințe de învățare:"
        ),
        "options": [
            "vizual, auditiv (aural), citit/scriere (read/write), kinestezic",
            "verbal, analitic, reflexiv, cognitiv",
            "vizual, afectiv, rațional, kinestezic",
            "validare, aplicare, repetiție, cunoaștere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele activități se potrivesc preferinței vizuale (V) în modelul VARK?"
        ),
        "options": [
            "diagrame, scheme și organizatori grafici",
            "imagini, culori și hărți conceptuale",
            "ascultarea unei prelegeri fără suport grafic",
            "memorarea listelor scrise fără reprezentare grafică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele recomandări sunt frecvente pentru cursanții cu preferință vizuală "
            "pronunțată?"
        ),
        "options": [
            "folosirea diagramelor și a hărților conceptuale",
            "codificarea informației prin culori și simboluri",
            "organizatori grafici (ex. tabele, ierarhii, mind maps)",
            "dictarea orală lungă fără niciun suport vizual",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Preferința auditivă (A) în VARK se manifestă cel mai bine prin:"
        ),
        "options": [
            "explicații orale, discuții și ascultarea înregistrărilor audio",
            "copierea extinsă a textelor din manual, fără dialog",
            "manipularea obiectelor și experimente practice",
            "completarea fișelor fără a asculta explicația profesorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele strategii susțin învățarea elevului cu preferință auditivă?"
        ),
        "options": [
            "repetarea informației cu voce tare sau în șoaptă",
            "participarea la discuții de grup și dezbateri pe temă",
            "lucrul izolat cu diagrame fără explicație verbală",
            "citirea silențioasă fără componentă orală sau discuție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Preferința citit/scriere (R) în VARK include în principal:"
        ),
        "options": [
            "liste, texte, definiții, notițe scrise și reformulări",
            "simulări practice și jocuri de rol fără notițe",
            "experimente de laborator cu manipulare directă",
            "ascultarea podcasturilor fără a nota sau reformula",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care activitate se aliniază cel mai bine stilului citit/scriere (R)?"
        ),
        "options": [
            "completarea fișelor și reformularea cu propriile cuvinte a ideilor din curs",
            "urmărirea unui film demonstrativ fără a lua notițe",
            "rezolvarea problemelor practice fără a nota pașii",
            "ascultarea prelegerii fără a scrie sau reformula",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Preferința kinestezică (K) se caracterizează prin:"
        ),
        "options": [
            "învățare prin manipulare, exemple concrete și activități practice",
            "memorarea pasivă a definițiilor din manual",
            "ascultarea prelegerii fără implicare motorie",
            "analiza diagramelor statice, fără experiment sau mișcare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele forme de activitate favorizează cursantul cu preferință "
            "kinestezică?"
        ),
        "options": [
            "simulări și experimente hands-on",
            "jocuri de rol și scenarii practice",
            "exemple concrete legate de situații reale",
            "lectura îndelungată a textelor teoretice, fără aplicare",
        ],
        "correct": "abc",
    },
    # —— 11–20: concluzii pedagogice, capcane, sinteză ——
    {
        "stem": (
            "Învățarea eficientă se realizează cel mai bine folosind un singur stil VARK "
            "— cel cu scor maxim la chestionar — și evitând celelalte modalități."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care dintre următoarele concluzii pedagogice privind stilurile VARK sunt corecte?"
        ),
        "options": [
            "e util să cunoști preferințele, dar învățarea eficientă cere combinarea "
            "mai multor strategii și modalități",
            "profesorul ar trebui să ofere varietate (vizual, auditiv, scris, practic), "
            "nu să se limiteze la un canal unic",
            "elevul trebuie încadrat permanent într-un singur stil și evaluat după el",
            "preferința VARK înlocuiește nevoia de explicație clară și de feedback",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele confuzii frecvente despre VARK trebuie evitate?"
        ),
        "options": [
            "preferința nu este o capacitate fixă — se poate dezvolta și combina",
            "scorul la chestionar nu închide accesul la alte modalități de învățare",
            "stilul vizual înseamnă că elevul nu poate învăța din texte scrise",
            "stilul kinestezic presupune renunțarea la citire și la discuție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi preferință VARK–activitate recomandată sunt corecte?"
        ),
        "options": [
            "vizual — diagrame, hărți mentale, organizatori grafici",
            "auditiv — explicații orale, discuții, înregistrări audio",
            "citit/scriere — notițe, liste, definiții, reformulări scrise",
            "kinestezic — manipulare, simulări, jocuri de rol, exemple practice",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un elev care învață mai ușor din hărți mentale și scheme colorate are "
            "probabil preferință accentuată pe dimensiunea:"
        ),
        "options": [
            "vizuală (V)",
            "auditivă (A)",
            "citit/scriere (R)",
            "kinestezică (K)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele practici didactice reflectă concluzia că stilurile trebuie "
            "combinate, nu izolate?"
        ),
        "options": [
            "o lecție cu diagramă, explicație orală, notițe scurte și exercițiu practic",
            "alternarea modalităților chiar dacă elevul are o preferință clară la VARK",
            "predarea prin lectură silențioasă, indiferent de preferințele elevilor",
            "renunțarea la activități practice pentru elevii cu scor mare la R",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre interpretarea rezultatelor VARK sunt corecte?"
        ),
        "options": [
            "chestionarul indică tendințe și preferințe, nu diagnostice rigide",
            "un elev poate avea scoruri ridicate pe mai multe dimensiuni",
            "preferințele pot fi luate în calcul la planificare, fără a exclude alte canale",
            "rezultatul VARK fixează metoda unică de predare pentru acel elev",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ascultarea unui podcast educațional și discutarea conținutului cu colegii "
            "susțin în principal preferința:"
        ),
        "options": [
            "auditivă (A)",
            "vizuală (V)",
            "citit/scriere (R)",
            "kinestezică (K)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele idei explică de ce combinarea stilurilor sporește eficiența "
            "învățării?"
        ),
        "options": [
            "informația codificată pe mai multe canale se leagă mai bine în memorie",
            "conținutul complex cere adesea reprezentare grafică, verbală, scrisă și practică",
            "un singur canal reduce efortul cognitiv și produce retenție maximă",
            "preferința VARK înlocuiește repetiția și aplicarea practică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele recomandări generale pentru profesor derivă din modelul VARK "
            "și din concluzia pedagogică asociată?"
        ),
        "options": [
            "oferă suport vizual (scheme, imagini) acolo unde ajută înțelegerea",
            "include explicații orale, discuții și posibilitatea de a asculta/repetă vocal",
            "permite notițe, reformulări scrise și lucrul cu texte sau fișe",
            "propune activități practice, simulări sau exemple concrete când e posibil",
        ],
        "correct": "abcd",
    },
]

assert len(VARK_ITEMS) == 20
