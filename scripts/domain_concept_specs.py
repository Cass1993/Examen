"""Itemi conceptuali directi — înlocuiesc filtrele «tematica de examen»."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from scripts.concept_clusters import ConceptSpec, build_concept_item, rotate_options
from scripts.domain_exam_topics import TOPIC_PHRASES, match_contextual_single
from scripts.upgrade_tf_items import LABEL_CLUSTER, _cluster_options, _normalize_label

ConceptResult = Tuple[str, Dict[str, str], str]

# Etichetă scurtă / frază extinsă → item conceptual unic
DOMAIN_CONCEPT_SPECS: Dict[str, ConceptSpec] = {
    "validitatea de criteriu": {
        "stem": "Validitatea de criteriu a unui test se referă la:",
        "options": {
            "a": "relația dintre scorurile testului și un criteriu extern relevant, cum ar fi performanța",
            "b": "transformarea scorurilor brute în scoruri standardizate pe baza normelor",
            "c": "stabilitatea scorurilor la retestare în condiții similare",
            "d": "dificultatea itemilor în raport cu nivelul persoanelor evaluate",
        },
        "correct": "a",
    },
    "scorul brut": {
        "stem": "În evaluarea psihologică, standardizarea unui test presupune în principal:",
        "options": {
            "a": "transformarea și interpretarea scorurilor brute prin raportare la norme clare",
            "b": "explicarea comportamentului prin moștenirea epigenetică a fricii",
            "c": "alegerea unui eșantion fără reguli de reprezentativitate",
            "d": "înlocuirea fidelității cu impresia evaluatorului",
        },
        "correct": "a",
        "aliases": ["scoruri brute", "norme standardizate", "standardizare"],
    },
    "fidelitatea test-retest": {
        "stem": "Fidelitatea test-retest a unui instrument psihologic indică:",
        "options": {
            "a": "stabilitatea scorurilor la administrări repetate în condiții similare",
            "b": "gradul în care itemii acoperă domeniul de conținut al constructului",
            "c": "relația dintre scorurile testului și un criteriu extern de performanță",
            "d": "transformarea scorurilor brute prin norme de referință",
        },
        "correct": "a",
        "aliases": ["test-retest", "fidelitate test retest"],
    },
    "fidelitatea inter-evaluatori": {
        "stem": "Fidelitatea inter-evaluatori se referă la:",
        "options": {
            "a": "consistența codării sau evaluării între evaluatori diferiți",
            "b": "relația dintre scorul testului și un criteriu extern relevant",
            "c": "acoperirea domeniului de conținut prin itemii instrumentului",
            "d": "transformarea scorurilor brute în scoruri standardizate",
        },
        "correct": "a",
        "aliases": ["inter-evaluatori", "inter evaluatori"],
    },
    "validitatea de construct": {
        "stem": "Validitatea de construct a unui test indică:",
        "options": {
            "a": "măsura în care instrumentul evaluează constructul teoretic vizat",
            "b": "stabilitatea scorurilor la retestare în condiții similare",
            "c": "relația dintre scor și un criteriu extern de performanță",
            "d": "procedura de transformare a scorurilor brute în norme",
        },
        "correct": "a",
    },
    "validitatea de conținut": {
        "stem": "Validitatea de conținut a unui instrument psihologic se referă la:",
        "options": {
            "a": "gradul în care itemii acoperă reprezentativ domeniul de conținut al constructului",
            "b": "consistența scorurilor la administrări repetate",
            "c": "corelația dintre scorul testului și un criteriu extern",
            "d": "compararea scorurilor cu normele standardizate ale populației",
        },
        "correct": "a",
    },
    "validitatea internă": {
        "stem": "Validitatea internă într-un studiu experimental se referă la:",
        "options": {
            "a": "gradul în care efectul observat poate fi atribuit manipulării variabilei independente",
            "b": "generalizarea rezultatelor la alte populații și contexte",
            "c": "relația dintre scorul unui test și un criteriu extern",
            "d": "stabilitatea scorurilor la retestare în condiții similare",
        },
        "correct": "a",
    },
    "validitatea externă": {
        "stem": "Validitatea externă a unui studiu se referă la:",
        "options": {
            "a": "gradul în care rezultatele pot fi generalizate la alte populații, contexte sau momente",
            "b": "măsura în care itemii acoperă domeniul de conținut al constructului",
            "c": "consistența scorurilor la administrări repetate ale aceluiași test",
            "d": "relația dintre scorurile testului și un criteriu de performanță",
        },
        "correct": "a",
    },
    "eroarea standard a măsurării": {
        "stem": "Eroarea standard a măsurării indică:",
        "options": {
            "a": "dispersia estimată a scorurilor observate în jurul valorii reale a constructului",
            "b": "relația dintre scorul testului și un criteriu extern de performanță",
            "c": "gradul în care itemii acoperă domeniul de conținut",
            "d": "stabilitatea scorurilor la retestare în condiții similare",
        },
        "correct": "a",
    },
    "validitatea incrementală": {
        "stem": "Validitatea incrementală a unui predictor se referă la:",
        "options": {
            "a": "contribuția suplimentară a unui predictor față de alți predictori deja incluși",
            "b": "transformarea scorurilor brute în scoruri standardizate",
            "c": "consistența evaluării între doi evaluatori independenți",
            "d": "acoperirea reprezentativă a domeniului de conținut al testului",
        },
        "correct": "a",
    },
    "eșantionul": {
        "stem": "În statistica inferențială, eșantionarea participanților presupune în principal:",
        "options": {
            "a": "selectarea unui subset din populație după reguli care permit generalizarea",
            "b": "transformarea scorurilor brute în norme standardizate",
            "c": "măsurarea stabilității scorurilor la retestare",
            "d": "evaluarea relației dintre test și un criteriu extern de performanță",
        },
        "correct": "a",
        "aliases": ["eșantionarea", "reprezentativitate"],
    },
    "populația": {
        "stem": "Populația țintă într-un studiu statistic se referă la:",
        "options": {
            "a": "mulțimea de indivizi sau unități la care cercetătorul dorește să generalizeze rezultatele",
            "b": "subsetul de participanți selectați efectiv pentru colectarea datelor",
            "c": "distribuția normelor standardizate ale unui test psihologic",
            "d": "coeficientul de corelație dintre două variabile măsurate",
        },
        "correct": "a",
    },
    "analiza de putere": {
        "stem": "Analiza de putere statistică vizează în principal:",
        "options": {
            "a": "estimarea probabilității de a detecta un efect real, dacă acesta există",
            "b": "transformarea scorurilor brute în scoruri standardizate",
            "c": "evaluarea acoperirii domeniului de conținut al unui test",
            "d": "măsurarea consistenței scorurilor la retestare",
        },
        "correct": "a",
        "aliases": ["puterea testului", "putere statistică"],
    },
    "variabila independentă": {
        "stem": "Variabila independentă într-un experiment se referă la:",
        "options": {
            "a": "factorul manipulat sau controlat de cercetător pentru a observa efectul asupra rezultatului",
            "b": "rezultatul măsurat ca efect al manipulării experimentale",
            "c": "factorul menținut constant pentru a reduce explicațiile alternative",
            "d": "dispersia scorurilor în jurul mediei într-un set de date",
        },
        "correct": "a",
    },
    "variabila dependentă": {
        "stem": "Variabila dependentă într-un studiu experimental este:",
        "options": {
            "a": "rezultatul măsurat, a cărui variație este analizată ca efect al manipulării",
            "b": "factorul manipulat intenționat de cercetător",
            "c": "variabila menținută constantă pe parcursul experimentului",
            "d": "mulțimea de indivizi la care se generalizează concluziile",
        },
        "correct": "a",
    },
    "neuroticismul": {
        "stem": "Neuroticismul, în modelul celor cinci mari factori, descrie mai ales:",
        "options": {
            "a": "tendința la experiențe emoționale negative, anxietate și vulnerabilitate la stres",
            "b": "energia socială, vioiciunea și căutarea stimulării pozitive",
            "c": "deschiderea față de experiențe noi, idei și valori",
            "d": "organizarea, perseverența și orientarea spre realizare",
        },
        "correct": "a",
    },
    "extraversia": {
        "stem": "Extraversia, ca dimensiune a personalității, se caracterizează prin:",
        "options": {
            "a": "sociabilitate, energie pozitivă și căutarea stimulării din mediu",
            "b": "tendința la anxietate, iritabilitate și dispoziție negativă",
            "c": "respectarea normelor, cooperare și încredere interpersonală",
            "d": "deschidere față de idei noi, fantezie și curiozitate intelectuală",
        },
        "correct": "a",
    },
    "agreabilitatea": {
        "stem": "Agreabilitatea, ca dimensiune Big Five, se caracterizează prin:",
        "options": {
            "a": "cooperare, empatie, încredere interpersonală și respect față de ceilalți",
            "b": "sociabilitate, energie pozitivă și căutarea stimulării din mediu",
            "c": "organizare, perseverență și orientare spre realizare",
            "d": "tendința la experiențe emoționale negative și vulnerabilitate la stres",
        },
        "correct": "a",
    },
    "conștiinciozitatea": {
        "stem": "Conștiinciozitatea, ca dimensiune Big Five, se caracterizează prin:",
        "options": {
            "a": "organizare, perseverență, autodisciplină și orientare spre realizare",
            "b": "deschidere față de idei noi, fantezie și curiozitate intelectuală",
            "c": "sociabilitate, vioiciune și căutarea stimulării pozitive",
            "d": "tendința la anxietate, iritabilitate și dispoziție negativă",
        },
        "correct": "a",
        "aliases": ["constiinciozitatea"],
    },
    "deschiderea către experiență": {
        "stem": "Deschiderea către experiență, în modelul Big Five, se caracterizează prin:",
        "options": {
            "a": "curiozitate intelectuală, imaginație, flexibilitate cognitivă și aprecierea artei",
            "b": "respectarea normelor, cooperare și încredere interpersonală",
            "c": "sociabilitate, energie pozitivă și căutarea stimulării din mediu",
            "d": "tendința la experiențe emoționale negative și vulnerabilitate la stres",
        },
        "correct": "a",
        "aliases": ["deschiderea spre experiență"],
    },
    "terapia centrată pe client": {
        "stem": "Terapia centrată pe client este asociată în principal cu:",
        "options": {
            "a": "abordarea umanist-experiențială",
            "b": "abordarea psihodinamică clasică",
            "c": "abordarea sistemică de familie",
            "d": "abordarea comportamentală radicală",
        },
        "correct": "a",
        "aliases": ["terapia centrata pe client", "client-centered"],
    },
    "psihanaliza": {
        "stem": "Psihanaliza aparține în principal orientării:",
        "options": {
            "a": "psihodinamice",
            "b": "umanist-experiențiale",
            "c": "cognitiv-comportamentale",
            "d": "sistemice de familie",
        },
        "correct": "a",
        "aliases": ["psihanaliză"],
    },
    "psihoterapiile cu suport empiric": {
        "stem": "Psihoterapiile cu suport empiric sunt discutate mai ales în contextul:",
        "options": {
            "a": "intervențiilor validate prin dovezi de cercetare empirică",
            "b": "explorării exclusive a viselor și a transferului ca mecanism de schimbare",
            "c": "evaluării factorială a trăsăturilor fără intervenție terapeutică",
            "d": "standardizării normelor pe scări de măsurare psihologică",
        },
        "correct": "a",
        "aliases": ["suport empiric", "empirically supported"],
    },
    "psihoterapia umanist-experiențială": {
        "stem": "Psihoterapia umanist-experiențială pune accent pe:",
        "options": {
            "a": "experiența subiectivă, autenticitate și dezvoltarea personală în relația terapeutică",
            "b": "protocoluri standardizate aplicate rigid pentru fiecare diagnostic",
            "c": "interpretarea conflictelor inconștiente ca unic mecanism de schimbare",
            "d": "restructurarea sistemului familial fără lucrul cu cognițiile individuale",
        },
        "correct": "a",
        "aliases": ["umanist-experiențială", "umanist experiențială"],
    },
    "psihoterapia psihodinamică": {
        "stem": "Psihoterapia psihodinamică se centrează mai ales pe:",
        "options": {
            "a": "procese inconștiente, conflicte intrapsihice, mecanisme de apărare și relația terapeutică",
            "b": "restructurarea cognitivă a gândurilor automate fără explorarea conflictelor timpurii",
            "c": "acceptarea necondiționată ca singură intervenție terapeutică",
            "d": "stabilirea obiectivelor SMART și monitorizarea consecințelor comportamentale",
        },
        "correct": "a",
        "aliases": ["psihodinamică"],
    },
    "relațiile duale": {
        "stem": "În etica psihoterapiei, relațiile duale se referă la:",
        "options": {
            "a": "relații suplimentare între terapeut și client, în afara cadrului terapeutic, care pot afecta limitele și obiectivitatea",
            "b": "protejarea informațiilor clientului în limitele legale și etice ale confidențialității",
            "c": "explicarea procesului terapeutic, a riscurilor, beneficiilor și drepturilor clientului",
            "d": "comunicarea empatică a înțelegerii experienței subiective a clientului",
        },
        "correct": "a",
        "aliases": ["relații duale", "relația duală"],
    },
    "alianța terapeutică": {
        "stem": "În psihoterapie, alianța terapeutică se referă la:",
        "options": {
            "a": "colaborarea activă dintre client și terapeut în atingerea obiectivelor terapiei",
            "b": "interpretarea simbolurilor din vis ca mecanism principal de schimbare",
            "c": "aplicarea rigidă a unui protocol standardizat pentru fiecare diagnostic",
            "d": "evaluarea factorială a trăsăturilor de personalitate fără intervenție",
        },
        "correct": "a",
    },
    "confidențialitatea": {
        "stem": "În etica psihoterapiei, confidențialitatea presupune:",
        "options": {
            "a": "protecția informațiilor obținute în relația terapeutică, cu excepțiile prevăzute etic",
            "b": "publicarea rezultatelor cercetării fără consimțământul clientului",
            "c": "discutarea cazului cu membrii familiei clientului fără acord",
            "d": "utilizarea datelor clinice în scop publicitar al cabinetului",
        },
        "correct": "a",
        "aliases": ["confidențialitate"],
    },
    "empatia": {
        "stem": "În etica psihoterapiei, empatia terapeutică se referă la:",
        "options": {
            "a": "înțelegerea experienței clientului și comunicarea acestei înțelegeri",
            "b": "identificarea automată a diagnosticului pe baza simptomelor vizibile",
            "c": "aplicarea aceluiași protocol pentru toți clienții indiferent de context",
            "d": "evitarea oricărei reacții emoționale față de client",
        },
        "correct": "a",
        "aliases": ["empatie"],
    },
    "colaborarea": {
        "stem": "În relația terapeutică, colaborarea presupune:",
        "options": {
            "a": "participarea activă a clientului și a terapeutului la procesul de schimbare",
            "b": "conformarea pasivă a clientului la directivele terapeutului",
            "c": "lucrul exclusiv cu conflicte inconștiente, fără obiective comune",
            "d": "evaluarea performanței organizaționale prin criterii de muncă",
        },
        "correct": "a",
    },
    "scala ordinală": {
        "stem": "Scala ordinală de măsurare se caracterizează prin:",
        "options": {
            "a": "ordonarea categoriilor după o ierarhie, fără distanțe egale între trepte",
            "b": "clasificarea observațiilor în categorii fără ordine internă",
            "c": "existența unui zero absolut și a rapoartelor proporționale",
            "d": "transformarea scorurilor brute prin norme standardizate",
        },
        "correct": "a",
    },
    "scala interval": {
        "stem": "Scala de interval de măsurare permite:",
        "options": {
            "a": "compararea distanțelor între valori, fără un zero absolut cu semnificație",
            "b": "doar clasificarea în categorii nominale fără ordine",
            "c": "formarea rapoartelor proporționale față de un zero absolut",
            "d": "interpretarea scorurilor exclusiv prin frecvențe procentuale",
        },
        "correct": "a",
        "aliases": ["scala de interval"],
    },
    "scala raport": {
        "stem": "Scala de raport (proporție) se caracterizează prin:",
        "options": {
            "a": "existența unui zero absolut și posibilitatea formării rapoartelor proporționale",
            "b": "ordonarea categoriilor fără distanțe egale între trepte",
            "c": "clasificarea observațiilor în categorii distincte, fără ordine",
            "d": "măsurarea consistenței scorurilor la retestare",
        },
        "correct": "a",
        "aliases": ["scala de raport"],
    },
    "studiile gemelare": {
        "stem": "Studiile gemelare în genetica comportamentală sunt folosite în principal pentru:",
        "options": {
            "a": "estimarea contribuției genetice și de mediu la variația trăsăturilor",
            "b": "compararea mediilor a trei sau mai multor grupuri experimentale",
            "c": "măsurarea validității de criteriu a unui test psihologic",
            "d": "evaluarea caracteristicilor postului în modelul Hackman-Oldham",
        },
        "correct": "a",
        "aliases": ["studiile de gemeni", "gemeni monozigoți"],
    },
    "eritabilitatea": {
        "stem": "Eritabilitatea unei trăsături psihologice indică:",
        "options": {
            "a": "proporția variației trăsăturii în populație atribuită diferențelor genetice",
            "b": "relația dintre scorul unui test și un criteriu extern de performanță",
            "c": "stabilitatea scorurilor la administrări repetate ale aceluiași test",
            "d": "gradul în care itemii acoperă domeniul de conținut al constructului",
        },
        "correct": "a",
    },
    "modelul big five": {
        "stem": "Modelul celor cinci mari factori ai personalității postulează că:",
        "options": {
            "a": "personalitatea poate fi descrisă prin cinci dimensiuni largi și relativ stabile",
            "b": "personalitatea se explică exclusiv prin conflicte inconștiente din copilărie",
            "c": "trăsăturile sunt relevante doar în contextul unei singure situații concrete",
            "d": "evaluarea personalității nu necesită instrumente standardizate",
        },
        "correct": "a",
        "aliases": ["big five", "cinci mari factori"],
    },
    "moștenirea epigenetică a fricii": {
        "stem": "Moștenirea epigenetică a fricii în personalitate se referă la:",
        "options": {
            "a": "transmiterea unor modificări epigenetice care influențează răspunsul la stimuli amenințători",
            "b": "relația dintre scorul unui test și un criteriu extern de performanță",
            "c": "transformarea scorurilor brute în norme standardizate",
            "d": "efectul halo în evaluarea performanței organizaționale",
        },
        "correct": "a",
        "aliases": ["epigenetică", "programarea epigenetică"],
    },
    "modelul eredității: gene, mediu comun, mediu neîmpărtășit": {
        "stem": "Modelul ACE în genetica comportamentală separă variația trăsăturilor în:",
        "options": {
            "a": "influențe genetice aditive, mediu comun și mediu neîmpărtășit",
            "b": "sumă ponderată a variantelor genetice asociate probabilistic cu o trăsătură",
            "c": "compararea asemănării gemenilor monozigoți și dizigoți",
            "d": "modificări ale expresiei genelor fără schimbarea secvenței ADN",
        },
        "correct": "a",
        "aliases": [
            "eritabilitatea",
            "studiile gemelare",
            "modelul eredității",
            "modelul ace",
        ],
    },
    "modelul caps": {
        "stem": "Modelul CAPS (cognitiv-afectiv al personalității) al lui Walter Mischel descrie personalitatea ca:",
        "options": {
            "a": "sistem dinamic de construcții cognitive-afective activate în interacțiune cu situația",
            "b": "set fix de trăsături care determină comportamentul indiferent de context",
            "c": "rezultat exclusiv al condiționării operante a răspunsurilor",
            "d": "produs al normelor standardizate aplicate scorurilor brute",
        },
        "correct": "a",
        "aliases": ["caps", "sistemul cognitiv-afectiv"],
    },
    "zona proximei dezvoltării": {
        "stem": "Zona proximei dezvoltării, la Lev Vygotsky, se referă la:",
        "options": {
            "a": "distanța dintre nivelul actual de dezvoltare și cel pe care copilul îl poate atinge cu sprijin",
            "b": "stadiul în care copilul operează cu raționament abstract și ipotetico-deductiv",
            "c": "perioada în care apare permanența obiectului în stadiul senzorio-motor",
            "d": "procedura de evaluare a atașamentului prin separări și reuniri scurte",
        },
        "correct": "a",
        "aliases": ["proxima dezvoltării", "vygotsky"],
    },
    "atașamentul securizant": {
        "stem": "Atașamentul securizant, în teoria atașamentului, se caracterizează prin:",
        "options": {
            "a": "folosirea figurii de atașament ca bază de siguranță și confort la explorare",
            "b": "minimizarea contactului și a semnalelor de nevoie la reunire cu îngrijitorul",
            "c": "căutare intensă de apropiere combinată cu rezistență și calmare dificilă",
            "d": "pattern contradictoriu sau dezorientat, fără strategie coerentă de atașament",
        },
        "correct": "a",
    },
    "situația stranie": {
        "stem": "Procedura Situația stranie (Strange Situation) este folosită în principal pentru:",
        "options": {
            "a": "observarea tipului de atașament al copilului față de îngrijitor prin separări și reuniri",
            "b": "evaluarea aptitudinilor intelectuale prin itemi progresivi de dificultate",
            "c": "măsurarea consistenței scorurilor la retestare în condiții similare",
            "d": "estimarea contribuției genetice și de mediu asupra trăsăturilor",
        },
        "correct": "a",
        "aliases": ["strange situation"],
    },
    "efectul halo": {
        "stem": "Efectul halo în evaluarea performanței organizaționale presupune:",
        "options": {
            "a": "generalizarea unei impresii pozitive sau negative de pe o dimensiune pe altele",
            "b": "relația dintre scorul unui test și un criteriu extern de performanță",
            "c": "transformarea scorurilor brute în norme standardizate",
            "d": "transmiterea modificărilor epigenetice între generații",
        },
        "correct": "a",
    },
    "burnoutul": {
        "stem": "Burnoutul profesional se caracterizează mai ales prin:",
        "options": {
            "a": "epuizare emoțională, detașare cinică și scăderea sentimentului de competență profesională",
            "b": "generalizarea unei impresii pozitive de pe o dimensiune de performanță pe altele",
            "c": "relația dintre cerințele jobului și resursele disponibile în modelul JD-R",
            "d": "validitatea de criteriu a unui instrument de evaluare organizațională",
        },
        "correct": "a",
    },
    "structurile psihosociale în câmpul școlar": {
        "stem": "Structurile psihosociale în câmpul școlar se referă la:",
        "options": {
            "a": "configurațiile relaționale și normative din mediul educațional care influențează dezvoltarea",
            "b": "procedura de standardizare a scorurilor brute prin norme de referință",
            "c": "evaluarea aptitudinilor intelectuale prin teste progresive",
            "d": "transmiterea epigenetică a răspunsului la stimuli amenințători",
        },
        "correct": "a",
    },
    "întărirea pozitivă": {
        "stem": "Întărirea pozitivă în învățarea asociaționistă presupune:",
        "options": {
            "a": "prezentarea unui stimulus apetitiv după un răspuns, crescând probabilitatea acestuia",
            "b": "eliminarea unui stimulus aversiv după răspuns, crescând probabilitatea acestuia",
            "c": "prezentarea unui stimulus aversiv după răspuns, scăzând probabilitatea acestuia",
            "d": "eliminarea unui stimulus apetitiv după răspuns, scăzând probabilitatea acestuia",
        },
        "correct": "a",
    },
    "întărirea negativă": {
        "stem": "Întărirea negativă în învățarea asociaționistă presupune:",
        "options": {
            "a": "eliminarea unui stimulus aversiv după răspuns, crescând probabilitatea acestuia",
            "b": "prezentarea unui stimulus apetitiv după răspuns, crescând probabilitatea acestuia",
            "c": "prezentarea unui stimulus aversiv după răspuns, scăzând probabilitatea acestuia",
            "d": "eliminarea unui stimulus apetitiv după răspuns, scăzând probabilitatea acestuia",
        },
        "correct": "a",
    },
    "pedeapsa pozitivă": {
        "stem": "Pedeapsa pozitivă în condiționarea operantă presupune:",
        "options": {
            "a": "prezentarea unui stimulus aversiv după răspuns, scăzând probabilitatea acestuia",
            "b": "eliminarea unui stimulus apetitiv după răspuns, scăzând probabilitatea acestuia",
            "c": "prezentarea unui stimulus apetitiv după răspuns, crescând probabilitatea acestuia",
            "d": "eliminarea unui stimulus aversiv după răspuns, crescând probabilitatea acestuia",
        },
        "correct": "a",
    },
    "mediana": {
        "stem": "Mediana unui set de date reprezintă:",
        "options": {
            "a": "valoarea care împarte distribuția ordonată în două părți egale",
            "b": "suma valorilor împărțită la numărul de observații",
            "c": "măsura dispersiei obținută ca medie a pătratelor abaterilor",
            "d": "indicatorul dispersiei scorurilor în jurul mediei aritmetice",
        },
        "correct": "a",
        "aliases": ["media aritmetică", "abaterea standard", "varianța"],
    },
    "scala nominală": {
        "stem": "Scala nominală de măsurare se caracterizează prin:",
        "options": {
            "a": "clasificarea observațiilor în categorii distincte, fără ordine sau distanță între ele",
            "b": "ordonarea categoriilor cu distanțe egale între trepte",
            "c": "existența unui zero absolut și a rapoartelor proporționale",
            "d": "transformarea scorurilor brute prin norme standardizate",
        },
        "correct": "a",
    },
    "analiza varianței (anova)": {
        "stem": "Analiza varianței (ANOVA) este folosită în principal pentru:",
        "options": {
            "a": "compararea mediilor a trei sau mai multe grupuri sau condiții",
            "b": "estimarea relației liniare dintre două variabile continue",
            "c": "descrierea frecvențelor și procentelor într-un set de date",
            "d": "măsurarea consistenței scorurilor la retestare",
        },
        "correct": "a",
        "aliases": ["anova", "analiza varianței"],
    },
    "eroarea de tip i": {
        "stem": "Eroarea de tip I în testarea statistică a ipotezelor înseamnă:",
        "options": {
            "a": "respingerea greșită a ipotezei nule atunci când aceasta este adevărată",
            "b": "acceptarea greșită a ipotezei nule atunci când aceasta este falsă",
            "c": "alegerea unui eșantion nereprezentativ pentru populația țintă",
            "d": "confundarea variabilei independente cu variabila dependentă",
        },
        "correct": "a",
        "aliases": ["eroarea de tip 1", "tip i"],
    },
    "valoarea p": {
        "stem": "Valoarea p într-un test statistic indică:",
        "options": {
            "a": "probabilitatea de a obține un rezultat la fel de extrem sau mai extrem, dacă ipoteza nulă este adevărată",
            "b": "mărimea efectului observat în unități standardizate",
            "c": "puterea statistică a studiului pentru detectarea unui efect real",
            "d": "proporția varianței explicate de modelul de regresie",
        },
        "correct": "a",
        "aliases": ["nivelul de semnificație", "p-value"],
    },
    "coeficientul pearson r": {
        "stem": "Coeficientul de corelație Pearson r măsoară:",
        "options": {
            "a": "tăria și direcția relației liniare dintre două variabile continue",
            "b": "diferența dintre mediile a două grupuri independente",
            "c": "proporția varianței explicate de un set de predictori",
            "d": "stabilitatea scorurilor la administrări repetate ale aceluiași test",
        },
        "correct": "a",
        "aliases": ["corelația pozitivă", "corelația negativă", "corelația"],
    },
    "normele": {
        "stem": "În evaluarea psihologică, normele unui test servesc la:",
        "options": {
            "a": "compararea scorului individual cu performanța unui grup de referință",
            "b": "manipularea variabilei independente în designul experimental",
            "c": "respingerea sau acceptarea ipotezei nule în testarea statistică",
            "d": "clasificarea observațiilor în categorii fără ordine internă",
        },
        "correct": "a",
        "aliases": ["norma", "norme", "norme standardizate"],
    },
    "testul t pentru eșantioane dependente": {
        "stem": "Testul t pentru eșantioane dependente (perechi) este folosit când:",
        "options": {
            "a": "aceleași participanți sunt măsurați de două ori sau în două condiții legate",
            "b": "se compară mediile a două grupuri independente de participanți",
            "c": "se compară simultan mediile a patru sau mai multe grupuri",
            "d": "se estimează relația dintre două variabile continue fără grupuri",
        },
        "correct": "a",
        "aliases": ["testul t", "eșantioane dependente"],
    },
    "statistica inferențială": {
        "stem": "Statistica inferențială se ocupă în principal cu:",
        "options": {
            "a": "formularea concluziilor despre populație pe baza datelor din eșantion",
            "b": "descrierea și sintetizarea datelor observate fără generalizare",
            "c": "transformarea scorurilor brute în norme standardizate",
            "d": "evaluarea acoperirii domeniului de conținut al unui test",
        },
        "correct": "a",
    },
    "statistica descriptivă": {
        "stem": "Statistica descriptivă are ca scop principal:",
        "options": {
            "a": "organizarea, descrierea și sintetizarea datelor observate",
            "b": "generalizarea concluziilor de la eșantion la populație",
            "c": "testarea ipotezelor despre diferențe între medii populationale",
            "d": "estimarea puterii statistice a unui studiu experimental",
        },
        "correct": "a",
    },
    "statistica parametrică": {
        "stem": "Statisticile parametrice presupun în general:",
        "options": {
            "a": "îndeplinirea unor condiții privind distribuția și tipul de măsurare a variabilelor",
            "b": "utilizarea exclusivă a scorurilor pe scări nominale sau ordinale",
            "c": "absența oricărei ipoteze despre forma distribuției datelor",
            "d": "transformarea scorurilor brute fără referință la norme",
        },
        "correct": "a",
    },
    "mărimea efectului": {
        "stem": "Mărimea efectului într-un studiu indică:",
        "options": {
            "a": "importanța practică sau magnitudinea fenomenului observat, independent de semnificația statistică",
            "b": "probabilitatea de a respinge greșit ipoteza nulă adevărată",
            "c": "numărul minim de participanți necesar pentru analiza de putere",
            "d": "gradul în care itemii acoperă domeniul de conținut al testului",
        },
        "correct": "a",
        "aliases": ["effect size"],
    },
    "identitatea sarcinii": {
        "stem": "Identitatea sarcinii, în modelul Hackman și Oldham, se referă la:",
        "options": {
            "a": "gradul în care lucrul implică desfășurarea unei activități complete, cu început și sfârșit vizibile",
            "b": "feedbackul direct despre eficacitatea propriei munci",
            "c": "libertatea de a decide cum și când se execută sarcinile",
            "d": "varietatea aptitudinilor și activităților implicate în post",
        },
        "correct": "a",
        "aliases": ["hackman", "oldham"],
    },
    "stresul ocupațional": {
        "stem": "Stresul ocupațional se referă mai ales la:",
        "options": {
            "a": "răspunsul la solicitări profesionale percepute ca depășind resursele persoanei",
            "b": "epuizarea emoțională, detașarea cinică și scăderea competenței profesionale",
            "c": "generalizarea unei impresii pozitive de pe o dimensiune de performanță pe altele",
            "d": "echilibrul dintre cerințele jobului și resursele disponibile în modelul JD-R",
        },
        "correct": "a",
    },
}

_ALIAS_INDEX: Dict[str, str] = {}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _build_alias_index() -> None:
    if _ALIAS_INDEX:
        return
    for key, spec in DOMAIN_CONCEPT_SPECS.items():
        _ALIAS_INDEX[_norm(key)] = key
        for alias in spec.get("aliases", []):
            _ALIAS_INDEX[_norm(alias)] = key
    for topic_key in TOPIC_PHRASES:
        nk = _norm(topic_key)
        if nk not in _ALIAS_INDEX:
            for spec_key in DOMAIN_CONCEPT_SPECS:
                if nk in _norm(spec_key) or _norm(spec_key) in nk:
                    _ALIAS_INDEX[nk] = spec_key
                    break


def _topic_key_from_label(label: str) -> Optional[str]:
    key = _norm(label)
    for topic_key, phrase in TOPIC_PHRASES.items():
        if _norm(phrase) == key or topic_key in key or key in _norm(phrase):
            return topic_key
    return None


def lookup_domain_concept(label: str) -> Optional[ConceptSpec]:
    _build_alias_index()
    key = _norm(label)
    key = re.sub(r"\([^)]*\)", " ", key)
    key = re.sub(r"\s+", " ", key).strip()

    if key in _ALIAS_INDEX:
        return DOMAIN_CONCEPT_SPECS[_ALIAS_INDEX[key]]

    topic_key = _topic_key_from_label(label)
    if topic_key and topic_key in _ALIAS_INDEX:
        return DOMAIN_CONCEPT_SPECS[_ALIAS_INDEX[topic_key]]
    if topic_key and topic_key in DOMAIN_CONCEPT_SPECS:
        return DOMAIN_CONCEPT_SPECS[topic_key]

    for alias, spec_key in _ALIAS_INDEX.items():
        if len(alias) > 6 and (alias in key or key in alias):
            return DOMAIN_CONCEPT_SPECS[spec_key]

    for spec_key, spec in DOMAIN_CONCEPT_SPECS.items():
        if _norm(spec_key) in key or key in _norm(spec_key):
            return spec

    return None


def _strip_label_noise(label: str) -> str:
    """Elimină prefixe redundante din opțiunile deja extinse."""
    t = (label or "").strip()
    t = re.sub(r"^variabila dependentă ca rezultat măsurat$", "variabila dependentă", t, flags=re.I)
    t = re.sub(r"^variabila independentă în designul experimental$", "variabila independentă", t, flags=re.I)
    t = re.sub(r"^eșantionarea participanților și reprezentativitatea$", "eșantionul", t, flags=re.I)
    t = re.sub(r"^validitatea externă și generalizarea rezultatelor$", "validitatea externă", t, flags=re.I)
    return t


def build_domain_concept_item(label: str, seed: int = 0) -> Optional[ConceptResult]:
    """Construiește item conceptual din eticheta unei opțiuni corecte."""
    label = _strip_label_noise((label or "").strip())
    if not label:
        return None

    ctx = match_contextual_single([label])
    if ctx:
        return ctx["stem"], dict(ctx["options"]), str(ctx["correct"]).lower()

    spec = lookup_domain_concept(label)
    if spec:
        return rotate_options(spec, seed)

    built = build_concept_item(label, seed)
    if built:
        return built

    cluster_id = LABEL_CLUSTER.get(_norm(label)) or LABEL_CLUSTER.get(
        _norm(_normalize_label(label))
    )
    if cluster_id:
        cluster = _cluster_options(cluster_id, label, seed)
        if cluster:
            return cluster

    return None


def pick_concept_from_labels(labels: List[str], seed: int) -> Optional[ConceptResult]:
    """Alege un concept testabil din etichetele corecte (rotație după seed)."""
    if not labels:
        return None
    ordered = labels[seed % len(labels) :] + labels[: seed % len(labels)]
    for label in ordered:
        built = build_domain_concept_item(label, seed)
        if built:
            return built
    return None
