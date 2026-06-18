"""Itemi — lot examen Psihologia muncii II (analiza postului + ierarhia muncii)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

PSIHOLOGIA_MUNCII_ITEMS: List[Item] = [
    # —— Definiție și rol în resurse umane (1–8) ——
    {
        "stem": (
            "Care afirmație surprinde cel mai bine scopul central al analizei "
            "postului (job analysis)?"
        ),
        "options": [
            "leagă descrierea postului, cerințele rolului și standardele de performanță",
            "documentează impresiile informale ale colegilor despre un angajat",
            "înlocuiește evaluarea performanței cu un singur interviu nestructurat",
            "se limitează la actualizarea organigramei, fără date despre sarcini",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Analiza postului este, în esență, o conversație informală despre cum "
            "își petrece cineva ziua la birou, fără procedură sistematică și fără "
            "document final."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "În ce funcții ale managementului resurselor umane este folosită "
            "analiza postului?"
        ),
        "options": [
            "recrutare și selecție de personal",
            "instruire și dezvoltare profesională",
            "evaluarea performanței și salarizarea",
            "promovare și planificarea carierei",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un analist notează procedurile zilnice, fluxul de lucru și "
            "responsabilitățile unui rol, fără a detalia încă profilul cunoștințe, deprinderi, aptitudini și altele (KSAO) al "
            "candidatului ideal. Această etapă corespunde analizei:"
        ),
        "options": [
            "orientate spre sarcină",
            "orientate spre angajat",
            "orientate spre redactarea job specification",
            "orientate spre clasificarea ocupațiilor în rețeaua ocupațională de "
            "informații (O*NET)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care întrebare este specifică analizei orientate spre angajat "
            "(worker-oriented)?"
        ),
        "options": [
            "ce cunoștințe, deprinderi și aptitudini trebuie să aibă ocupantul postului?",
            "ce activități și proceduri sunt efectiv realizate în rol?",
            "câte poziții vacante există în organigramă?",
            "ce echipament tehnic este instalat la locul de muncă?",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi de afirmații descriu corect relația dintre cele două "
            "orientări ale analizei postului?"
        ),
        "options": [
            "orientarea spre sarcină răspunde la „Ce face?” — orientarea spre angajat la „Ce trebuie să aibă?”",
            "ambele orientări pot alimenta decizii de resurse umane (HR), dar accentul "
            "informațional diferă",
            "orientarea spre angajat se limitează la descrierea sarcinilor zilnice",
            "orientarea spre sarcină furnizează criterii pentru evaluarea performanței pe activități",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Fără un rezultat tangibil al analizei postului, care risc apare cel "
            "mai frecvent în resurse umane (HR)?"
        ),
        "options": [
            "criterii de selecție și evaluare inconsistente sau arbitrare",
            "decizii de resurse umane (HR) greu de justificat în lipsa reperelor despre rol",
            "documente de resurse umane (HR) mai puțin comparabile între posturi similare",
            "analiză mai rapidă, dar cu același grad de acuratețe garantat",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un consultant redactează sarcinile zilnice, responsabilitățile și "
            "condițiile de lucru ale unui post de tehnician. Produsul principal "
            "al acestei etape este:"
        ),
        "options": [
            "descrierea de post (job description)",
            "specificația de post (job specification)",
            "profilul vocațional Holland (RIASEC) al candidatului ideal",
            "profilul vocațional Holland (RIASEC) al ocupantului",
        ],
        "correct": "a",
    },
    # —— KSAO (9–16) ——
    {
        "stem": (
            "În modelul cunoștințe, deprinderi, aptitudini și altele (KSAO), un post cere „cunoașterea regulamentului intern”. "
            "Această cerință se încadrează la:"
        ),
        "options": [
            "K — cunoștințe învățate",
            "S — deprinderi practicate",
            "A — aptitudini relativ stabile",
            "O — factori din categoria „other”",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În modelul cunoștințe, deprinderi, aptitudini și altele (KSAO), capacitatea de a opera fluent un software după "
            "instruire repetată relevă în principal:"
        ),
        "options": [
            "S — skill deprins prin practică",
            "K — cunoștință teoretică neatinsă de exercițiu",
            "A — aptitudine senzorial-perceptuală din taxonomia Fleishman (FJAS)",
            "O — valoare organizațională abstractă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În modelul cunoștințe, deprinderi, aptitudini și altele (KSAO), „raționament verbal” sau „coordonare manuală fină” "
            "se încadrează cel mai probabil la:"
        ),
        "options": [
            "A — abilities (aptitudini)",
            "K — knowledge (cunoștințe)",
            "S — skills (deprinderi automate)",
            "O — other (motivație și valori)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care exemple sunt încadrate corect în categoria „altele” (O) din cunoștințe, deprinderi, aptitudini și altele (KSAO)?"
        ),
        "options": [
            "motivația pentru muncă în echipă",
            "valorile personale relevante pentru cultura organizațională",
            "procedura de arhivare documente deja automatizată",
            "cunoștințele teoretice din manualul de proceduri",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În modelul cunoștințe, deprinderi, aptitudini și altele (KSAO), cunoștințele (knowledge) și aptitudinile (abilities) "
            "pot fi folosite interchangeabil, deoarece ambele se dobândesc "
            "exclusiv prin experiență la job."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un post cere „cunoștințe de legislația muncii” și „aptitudine pentru "
            "raționament verbal”. În modelul cunoștințe, deprinderi, aptitudini și altele (KSAO), acestea corespund:"
        ),
        "options": [
            "K — cunoștințe învățate",
            "A — aptitudine relativ stabilă",
            "S — deprindere motorie automată",
            "O — atestat profesional obligatoriu pentru ocuparea postului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care pereche ilustrează corect diferența dintre cunoștințe (K) și "
            "deprinderi (S) în cunoștințe, deprinderi, aptitudini și altele (KSAO)?"
        ),
        "options": [
            "K: știe teoria contabilității — S: întocmește bilanțul conform procedurii",
            "K: cunoaște regulamentul — S: aplică procedura de siguranță în practică",
            "K și S sunt identice dacă persoana a urmat un curs",
            "S desemnează doar talente înnăscute, fără practică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce include modelul cunoștințe, deprinderi, aptitudini și altele "
            "(KSAO) categoria „altele” (O)?"
        ),
        "options": [
            "unele cerințe de succes la job nu sunt reduse la cunoștințe sau skills tehnice",
            "motivația și personalitatea pot influența performanța în rol",
            "O înlocuiește descrierea sarcinilor din job description",
            "categoria O desemnează aptitudini cognitive măsurate prin teste IQ",
        ],
        "correct": "ab",
    },
    # —— Ierarhia muncii (17–22) ——
    {
        "stem": (
            "Care este ordinea corectă a nivelurilor din ierarhia muncii, de la "
            "cel mai mic la cel mai larg?"
        ),
        "options": [
            "element → sarcină → obligație → poziție → job → familie de joburi → ocupație → carieră",
            "element → obligație → sarcină → job → poziție → ocupație → familie de joburi → carieră",
            "sarcină → element → poziție → job → obligație → carieră → ocupație → familie de joburi",
            "poziție → job → element → sarcină → obligație → familie de joburi → carieră → ocupație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care definiții sunt corecte în ierarhia muncii?"
        ),
        "options": [
            "sarcina = activitate concretă cu început și sfârșit clar",
            "obligația (duty) = grup de sarcini înrudite",
            "elementul = echivalentul ocupației la nivel național",
            "jobul = același lucru cu poziția din organigramă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În ierarhia muncii, „jobul” se deosebește de „poziție” deoarece:"
        ),
        "options": [
            "jobul descrie un tipar de sarcini care poate exista în mai multe locuri",
            "poziția este instanța concretă ocupată de o persoană în organigramă",
            "poziția este mereu mai largă decât ocupația",
            "jobul nu include sarcini, ci doar titlul administrativ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Familia de joburi” și „ocupația” se plasează în ierarhia muncii:"
        ),
        "options": [
            "deasupra unui singur job, grupând roluri înrudite sau domenii largi",
            "sub nivelul de carieră, dar deasupra unui post individual",
            "sub nivelul elementului de muncă",
            "în afara oricărei legături cu sarcinile concrete",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un analist descompune munca unui operator call-center: răspuns la "
            "apel, înregistrare solicitare, transfer către coleg. Aceste unități "
            "corespund nivelului:"
        ),
        "options": [
            "sarcină (task)",
            "element",
            "obligație (duty)",
            "ocupație",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Nivelul „carieră” din ierarhia muncii desemnează:"
        ),
        "options": [
            "parcursul profesional pe termen lung al unei persoane",
            "un singur post ocupat într-o zi de lucru",
            "grupul de sarcini dintr-o obligație",
            "familia de joburi dintr-o singură companie",
        ],
        "correct": "a",
    },
    # —— Metode de analiză (23–30) ——
    {
        "stem": (
            "Care avantaje ale observării directe în analiza postului sunt "
            "recunoscute în literatura de specialitate?"
        ),
        "options": [
            "înregistrează activități reale, nu doar declarații despre ele",
            "permite notarea comportamentului în contextul efectiv al jobului",
            "captează procesele mentale interne doar când apar în comportament observabil",
            "reduce, dar nu anulează, subiectivitatea observatorului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care limită a observării directe este cel mai frecvent invocată?"
        ),
        "options": [
            "procesele mentale interne pot rămâne invizibile fără comportament exterior",
            "planificarea cognitivă poate să nu apară în acțiuni observabile",
            "metoda este mai puțin utilă pentru sarcini cu componentă cognitivă invizibilă",
            "observația singură poate subestima planificarea internă a muncii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Interviul structurat în analiza postului este preferat când analistul "
            "are nevoie de:"
        ),
        "options": [
            "informații detaliate despre sarcini și context de la ocupant sau supervizor",
            "date standardizate de la mulți respondenți în timp scurt",
            "înregistrarea distribuției timpului pe parcursul mai multor zile",
            "identificarea comportamentelor excepțional de eficiente sau ineficiente",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Chestionarul în analiza postului este ales în principal pentru că:"
        ),
        "options": [
            "permite colectare rapidă și standardizată de la mulți incumbenți",
            "facilitează compararea răspunsurilor pe aceleași întrebări",
            "înlocuiește nevoia de orice interviu sau observație",
            "reduce, dar nu elimină, răspunsurile social-desirabile",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Jurnalul de lucru (diary method) este util mai ales atunci când:"
        ),
        "options": [
            "munca este variată și analistul vrea să vadă distribuția timpului",
            "ocupantul postului înregistrează periodic activitățile efectuate",
            "se dorește un singur interviu scurt cu directorul general",
            "se urmăresc doar incidentele critice de performanță",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Metoda incidentelor critice (critical incidents) se concentrează pe:"
        ),
        "options": [
            "comportamente foarte eficiente sau foarte ineficiente la job",
            "situații cu impact clar asupra performanței",
            "rutina zilnică repetată identic, fără variație",
            "cunoștințe teoretice din manuale, fără comportament",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Metoda incidentelor critice include în mod obișnuit și comportamentele "
            "medii, de rutină, care nu marchează un succes sau un eșec clar."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Pentru identificarea comportamentelor excepțional de bune sau rele, "
            "metoda recomandată în mod clasic este:"
        ),
        "options": [
            "incidentele critice",
            "chestionarul standardizat despre cunoștințe, deprinderi, aptitudini și "
            "altele (KSAO), fără exemple comportamentale",
            "jurnalul de lucru pe activități de rutină",
            "jurnalul de lucru pe activități repetitive zilnice",
        ],
        "correct": "a",
    },
    # —— FJAS (31–36) ——
    {
        "stem": (
            "Taxonomia aptitudinilor Fleishman (FJAS) cuprinde aproximativ:"
        ),
        "options": [
            "73 de aptitudini relevante pentru muncă",
            "52 de aptitudini listate în Dicționarul titlurilor de ocupații (DOT), "
            "fără legătură directă cu taxonomia Fleishman (FJAS)",
            "10 scale de personalitate clinice",
            "doar cunoștințe declarative din educație formală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care domenii de aptitudini sunt incluse în taxonomia Fleishman (FJAS)?"
        ),
        "options": [
            "aptitudini cognitive",
            "aptitudini psihomotorii și fizice",
            "aptitudini senzorial-perceptuale",
            "aptitudini sociale și interpersonale",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În taxonomia Fleishman (FJAS), aptitudinile cognitive pot include:"
        ),
        "options": [
            "raționament verbal și numeric",
            "memorie și viteză de învățare",
            "forță musculară și rezistență fizică",
            "coordonare ochi-mână fără componentă de gândire",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmație despre taxonomia Fleishman (FJAS) este corectă?"
        ),
        "options": [
            "oferă vocabular standardizat pentru cerințe umane în analiza orientată spre angajat",
            "acoperă aptitudini cognitive, psihomotorii, fizice, senzorial-perceptuale și sociale",
            "substituie description cu lista cerințelor cunoștințe, deprinderi, aptitudini și altele (KSAO) din specification",
            "se limitează la forță fizică, fără componentă cognitivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Taxonomia Fleishman (FJAS) este utilă în analiza postului deoarece:"
        ),
        "options": [
            "permite legătura între cerințe, selecție și training",
            "uniformizează descrierea aptitudinilor cerute de rol",
            "substituie job description cu lista procedurilor zilnice",
            "elimină nevoia de interviu structural în orice selecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Aptitudinile senzorial-perceptuale din taxonomia Fleishman (FJAS) "
            "vizează:"
        ),
        "options": [
            "discriminarea vizuală, auditivă sau tactilă relevantă pentru job",
            "perceperea diferențelor între stimuli în context de lucru",
            "negocierea și influențarea comportamentului echipei",
            "cunoștințe juridice memorate din legislația muncii",
        ],
        "correct": "ab",
    },
    # —— Job description vs job specification (37–44) ——
    {
        "stem": (
            "Care distincție între job description și job specification este corectă?"
        ),
        "options": [
            "description descrie postul — specification descrie persoana potrivită",
            "description vizează activități și responsabilități — specification vizează cerințele umane",
            "ambele documente au același scop și pot fi publicate identic la recrutare",
            "specification enumeră procedurile zilnice, iar description cerințele "
            "cunoștințe, deprinderi, aptitudini și altele (KSAO)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce informații apar tipic în descrierea de post (job description)?"
        ),
        "options": [
            "activități și sarcini principale",
            "responsabilități și relații organizaționale",
            "condiții de lucru și contextul rolului",
            "studii minime obligatorii ale candidatului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce informații apar tipic în specificația de post (job specification)?"
        ),
        "options": [
            "educație și experiență necesară",
            "cunoștințe, skills, aptitudini și alte cerințe (KSAO)",
            "certificări sau autorizații cerute",
            "relațiile de raportare și condițiile de mediu ale postului",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Un anunț de angajare menționează „studii superioare în informatică, "
            "experiență minim 2 ani, cunoștințe SQL”. Informațiile provin din:"
        ),
        "options": [
            "specificația de post (job specification)",
            "profilul cerințelor orientate spre angajat",
            "descrierea zilnică a procedurilor de fabricație",
            "evaluarea performanței pe sarcinile lunare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un document intern enumeră raportarea către șef, sarcinile lunare "
            "și condițiile de lucru. Acesta este cel mai probabil:"
        ),
        "options": [
            "descrierea de post (job description)",
            "document orientat spre sarcină",
            "specificația de post (job specification)",
            "profilul cunoștințe, deprinderi, aptitudini și altele (KSAO) pentru selecție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Specificația de post (job specification) enumeră în principal "
            "procedurile zilnice și responsabilitățile postului, nu cerințele "
            "candidatului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce au nevoie organizațiile de ambele documente — job description "
            "și job specification?"
        ),
        "options": [
            "description explică ce se face în rol — specification cine poate reuși în rol",
            "împreună leagă postul, cerințele și criteriile de performanță",
            "un singur document este suficient dacă include și sarcini, și studii minime",
            "specification înlocuiește evaluarea performanței pe sarcini",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă la recrutare se publică doar job description, fără job "
            "specification, consecința probabilă este:"
        ),
        "options": [
            "candidații nu cunosc clar cerințele umane ale rolului",
            "selecția devine mai subiectivă sau inconsistentă",
            "dispar informațiile despre sarcinile postului",
            "nu mai este necesar niciun interviu de angajare",
        ],
        "correct": "ab",
    },
    # —— O*NET, integrare (45–50) ——
    {
        "stem": (
            "Baza de date ocupațională online (O*NET) este folosită în psihologia "
            "muncii ca:"
        ),
        "options": [
            "resursă standardizată de informații despre ocupații și cerințe",
            "referință pentru aptitudini, context și caracteristici ale muncii",
            "substitut obligatoriu al oricărei analize interne a postului",
            "instrument clinic de diagnostic al personalității",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Rețeaua ocupațională de informații (O*NET) a înlocuit treptat vechiul "
            "Dicționar al titlurilor de ocupații (DOT) ca principală sursă "
            "ocupațională detaliată."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Dicționarul titlurilor de ocupații (DOT) și rețeaua ocupațională de "
            "informații (O*NET) au în comun faptul că:"
        ),
        "options": [
            "clasifică ocupații și cerințe relevante pentru muncă",
            "sprijină legătura între analiza postului și informația ocupațională",
            "standardizează baremele de salarizare obligatorii în orice organizație",
            "înlocuiesc analiza internă a postului în companii mari",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O firmă compară cerințele unui post intern cu standardele rețelei "
            "ocupaționale de informații (O*NET). "
            "Scopul principal este:"
        ),
        "options": [
            "calibrarea descrierilor și specificațiilor de post",
            "ancorarea cerințelor cunoștințe, deprinderi, aptitudini și altele (KSAO) în referințe ocupaționale",
            "standardizarea selecției doar prin scoruri de chestionar",
            "diagnosticarea tulburărilor de personalitate ale candidaților",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care lanț logic rezumă corect rolul analizei postului în organizație?"
        ),
        "options": [
            "analiză post → documente (description + specification) → decizii de "
            "resurse umane (HR)",
            "cerințe clare → selecție și training potrivite → performanță evaluabilă",
            "analiză post → eliminarea evaluării performanței",
            "interviu informal → promovare automată pe vechime",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un specialist în resurse umane (HR) combină observația, interviul și "
            "incidentele critice "
            "pentru același post. Care obiective justifică această abordare?"
        ),
        "options": [
            "validarea reciprocă a datelor din surse diferite",
            "compensarea limitelor fiecărei metode luate separat",
            "o imagine mai completă a sarcinilor și a comportamentelor relevante",
            "reducerea duratei analizei prin renunțarea la interviu după observație",
        ],
        "correct": "abc",
    },
    # —— Ierarhia muncii: descrieri și diferențe (51–60) ——
    {
        "stem": (
            "În ierarhia muncii, „elementul” (work element) reprezintă:"
        ),
        "options": [
            "cea mai mică unitate observabilă a muncii",
            "un gest sau o acțiune elementară din care se construiesc sarcinile",
            "grupul de posturi similare dintr-o industrie",
            "parcursul profesional pe termen lung al unei persoane",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O „sarcină” (task) se caracterizează prin:"
        ),
        "options": [
            "activitate concretă cu început și sfârșit clar",
            "rezultat tangibil sau observabil",
            "identitate cu o ocupație la nivel național",
            "echivalență cu familia de joburi din organizație",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Obligația” (duty) se deosebește de „sarcină” (task) prin faptul că:"
        ),
        "options": [
            "duty grupează sarcini înrudite care revin aceluiași rol",
            "task este o activitate singulară; duty le agregă pe cele similare",
            "duty este mai îngustă decât un element de muncă",
            "task descrie postul vacant din organigramă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În ierarhia muncii, „poziția” (position) desemnează:"
        ),
        "options": [
            "un loc organizațional concret ocupat de o persoană",
            "un slot din organigramă cu titlu și raportare definite",
            "clasificarea națională a unei ocupații",
            "lista gesturilor elementare dintr-o zi de lucru",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Jobul” (job) diferă de „poziție” (position) deoarece:"
        ),
        "options": [
            "jobul este tiparul de muncă replicabil în mai multe locuri",
            "poziția este instanța concretă a acelui tipar în organizație",
            "jobul este mai îngust decât un element de muncă",
            "poziția grupează toate ocupațiile dintr-o țară",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "„Familia de joburi” și „ocupația” în ierarhia muncii:"
        ),
        "options": [
            "grupează roluri înrudite sau domenii largi de muncă",
            "se situează deasupra unui singur job, sub nivelul de carieră",
            "sunt sub nivelul elementului de muncă",
            "nu au legătură cu sarcinile concrete",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Nivelul „carieră” (career) se referă la:"
        ),
        "options": [
            "parcursul profesional pe termen lung al unei persoane",
            "succesiunea de posturi, experiențe și dezvoltare profesională",
            "o singură sarcină executată într-o oră",
            "familia de joburi dintr-o singură companie",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care ordine reflectă corect ierarhia muncii, de la îngust la larg?"
        ),
        "options": [
            "element → sarcină → obligație → poziție → job → familie de joburi → ocupație → carieră",
            "element → sarcină → poziție → obligație → job → familie de joburi → ocupație → carieră",
            "sarcină → element → carieră → poziție → ocupație → job",
            "poziție → element → familie de joburi → sarcină → carieră",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un analist notează: „apasă tasta Enter”, „completează formularul”, "
            "„grupul de formulare zilnice”, „postul de operator birou din sediu”. "
            "Nivelurile, în ordine, sunt:"
        ),
        "options": [
            "element → sarcină → obligație → poziție",
            "sarcină → element → obligație → job",
            "element → obligație → sarcină → ocupație",
            "obligație → sarcină → element → carieră",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În ierarhia muncii, „familia de joburi” este mai îngustă decât un "
            "„job”, iar „ocupația” este mai îngustă decât „cariera”."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Metode, FJAS, description/specification (61–70) ——
    {
        "stem": (
            "De ce combină analiștii mai multe metode pentru același post?"
        ),
        "options": [
            "fiecare metodă compensează limitele celorlalte",
            "datele din surse diferite se pot valida reciproc",
            "o singură metodă bine aleasă face redundante celelalte",
            "combinarea metodelor elimină necesitatea documentelor de resurse umane "
            "(HR)",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Resursele umane (HR) au nevoie de date rapide de la 80 de angajați pe "
            "aceleași "
            "întrebări despre sarcini. Metoda cea mai potrivită este:"
        ),
        "options": [
            "chestionarul standardizat",
            "interviul individual detaliat cu fiecare persoană",
            "incidentele critice aplicate rutinei zilnice",
            "observația continuă a fiecărui angajat timp de o lună",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Jurnalul de lucru este deosebit de util când analistul urmărește:"
        ),
        "options": [
            "distribuția timpului pe activități de-a lungul zilei",
            "frecvența și durata sarcinilor repetitive",
            "distribuția timpului pe activități de rutină, nu pe variație",
            "profilul de personalitate al ocupantului postului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Observația directă permite accesul complet și fiabil la procesele "
            "mentale pure, fără comportament exterior observabil."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Taxonomia Fleishman (FJAS) este folosită în analiza orientată spre "
            "angajat deoarece:"
        ),
        "options": [
            "oferă vocabular standardizat de aptitudini cerute de muncă",
            "descrie cerințe umane, nu lista procedurilor zilnice",
            "înlocuiește job description în documentația internă",
            "măsoară doar cunoștințe declarative din educația formală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care afirmații despre structura taxonomiei Fleishman (FJAS) sunt "
            "corecte?"
        ),
        "options": [
            "cuprinde aproximativ 73 de aptitudini relevante pentru muncă",
            "include domenii cognitive, psihomotorii, fizice, senzorial-perceptuale și sociale",
            "se limitează la aptitudini fizice, fără componentă socială",
            "descrie procedurile din job description, nu cerințele umane",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În taxonomia Fleishman (FJAS), aptitudinile sociale pot include:"
        ),
        "options": [
            "lucrul eficient cu alte persoane sau echipe",
            "înțelegerea și influențarea comportamentului altora la job",
            "forța musculară necesară manipulării încărcăturilor",
            "discriminarea vizuală a detaliilor fine pe bandă de producție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce informații apar tipic în job description, dar nu în job specification?"
        ),
        "options": [
            "sarcinile și responsabilitățile principale ale rolului",
            "relațiile organizaționale și condițiile de lucru",
            "educația minimă și certificările cerute candidatului",
            "contextul activităților efectiv realizate în post",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Ce informații apar tipic în job specification, dar nu în job description?"
        ),
        "options": [
            "educația și experiența minimă cerute candidatului",
            "cunoștințe, skills, aptitudini și alte cerințe — cunoștințe, deprinderi, "
            "aptitudini și altele (KSAO)",
            "procedurile zilnice și obligațiile postului",
            "certificări sau autorizații necesare ocupantului viitor",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Job description și job specification pot fi publicate identic la "
            "recrutare, deoarece ambele descriu aceleași cerințe umane și aceleași "
            "sarcini ale rolului."
        ),
        "tf": True,
        "correct_tf": False,
    },
    # —— Rol HR, POST–cerințe–performanță (71–80) ——
    {
        "stem": (
            "Rezultatele analizei postului stau la baza căror funcții de resurse "
            "umane (HR)?"
        ),
        "options": [
            "recrutare și selecție de personal",
            "instruire și evaluarea performanței",
            "salarizare și promovare",
            "planificarea campaniilor publicitare externe",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În recrutare, analiza postului furnizează informații despre:"
        ),
        "options": [
            "sarcinile și responsabilitățile comunicate candidaților",
            "profilul cerințelor umane — cunoștințe, deprinderi, aptitudini și altele "
            "(KSAO) — pentru filtrarea inițială",
            "compararea scorurilor brute între candidați, fără raportare la cerințele postului",
            "istoricul medical al angajaților existenți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În selecție, datele din analiza postului servesc în principal la:"
        ),
        "options": [
            "compararea candidaților cu cerințele din job specification",
            "evaluarea potrivirii persoanei cu cerințele cunoștințe, deprinderi, "
            "aptitudini și altele (KSAO) ale rolului",
            "selecția bazată doar pe scoruri de personalitate, fără probă practică",
            "măsurarea satisfacției la locul de muncă, fără criterii de job",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Trainingul bazat pe analiza postului pornește cel mai frecvent de la:"
        ),
        "options": [
            "decalajul dintre competențele actuale și cerințele rolului",
            "skills și cunoștințe necesare performanței documentate în analiză",
            "preferințele personale ale trainerului, fără date despre post",
            "profilul de competențe tehnice, fără legătură cu sarcinile documentate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Evaluarea performanței se ancorează în analiza postului pentru că:"
        ),
        "options": [
            "oferă criterii pe sarcini, responsabilități și standarde așteptate",
            "permite compararea comportamentului real cu cerințele documentate",
            "elimină feedback-ul calitativ de la supervizor",
            "compararea performanței cu media echipei, fără criterii din analiza postului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Salarizarea echitabilă se sprijină pe analiza postului prin:"
        ),
        "options": [
            "documentarea complexității și responsabilităților rolului",
            "compararea valorii relative a muncii între posturi",
            "calculul salarial bazat doar pe gradul ierarhic, fără date despre sarcini",
            "fixarea salariilor doar pe baza orelor suplimentare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La promovare, analiza postului ajută la:"
        ),
        "options": [
            "clarificarea cerințelor postului țintă",
            "verificarea îndeplinirii cerințelor cunoștințe, deprinderi, aptitudini și altele (KSAO) ale rolului superior",
            "promovarea automată pe vechime, fără criterii de rol",
            "evitarea comparării performanței cu cerințele noului post",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Lanțul POST → CERINȚE → PERFORMANȚĂ presupune că:"
        ),
        "options": [
            "fără analiză clară a postului, performanța nu are repere obiective",
            "descriem postul și cerințele înainte de a evalua munca prestată",
            "performanța se măsoară doar prin teste de personalitate",
            "cerințele sunt opționale dacă există un interviu informal",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un manager folosește rezultatele analizei orientate spre sarcină "
            "în principal pentru:"
        ),
        "options": [
            "job description și criterii de evaluare pe activități",
            "definirea certificărilor minime din job specification",
            "clasificarea ocupațiilor în baze precum rețeaua ocupațională de "
            "informații (O*NET)",
            "măsurarea trăsăturilor din categoria „altele” (O) din cunoștințe, "
            "deprinderi, aptitudini și altele (KSAO)",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Analiza orientată spre angajat — cunoștințe, deprinderi, aptitudini și "
            "altele (KSAO) — este relevantă doar la "
            "recrutare și selecție, nu și la instruire sau promovare."
        ),
        "tf": True,
        "correct_tf": False,
    },
]

from scripts.psihologia_muncii_design_munca_bank_data import DESIGN_MUNCII_ITEMS
from scripts.psihologia_muncii_selectie_bank_data import SELECTIE_PERSONAL_ITEMS
from scripts.psihologia_muncii_performanta_bank_data import PERFORMANTA_MUNCII_ITEMS

PSIHOLOGIA_MUNCII_ALL_ITEMS: List[Item] = (
    PSIHOLOGIA_MUNCII_ITEMS
    + DESIGN_MUNCII_ITEMS
    + SELECTIE_PERSONAL_ITEMS
    + PERFORMANTA_MUNCII_ITEMS
)
