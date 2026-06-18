"""Itemi — behaviorism clasic: Pavlov, Watson, Skinner, Krumboltz, Eysenck, Miller, Dollard."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

BEHAVIORISM_ITEMS: List[Item] = [
    # —— Pavlov & condiționarea clasică (1–10) ——
    {
        "stem": "Ivan P. Pavlov a descoperit condiționarea clasică studiind inițial:",
        "options": [
            "reflexele digestive ale câinilor și secreția salivară",
            "întărirea comportamentelor la șobolani în labirint",
            "transferul în relația terapeutică umană",
            "schemele cognitive disfuncționale la depresie",
        ],
        "correct": "a",
    },
    {
        "stem": "În paradigma lui Ivan P. Pavlov, un stimul condiționat (SC) este:",
        "options": [
            "un stimul inițial neutru care, prin asociere repetată, declanșează răspunsul",
            "un stimul care întărește sau slăbește o comportare voluntară",
            "o reprezentare mentală a consecinței viitoare",
            "un conflict între tendința de apropiere și cea de evitare",
        ],
        "correct": "a",
    },
    {
        "stem": "John B. Watson a preluat de la Ivan P. Pavlov ideea că:",
        "options": [
            "emoțiile umane pot fi explicate prin asociere stimul–răspuns",
            "personalitatea se reduce la tipuri jungiene de bază",
            "neuroza apare din conflicte inconștiente infantile",
            "comportamentul se schimbă doar prin insight verbal",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de Ivan P. Pavlov, John B. Watson a mers mai departe prin:",
        "options": [
            "aplicarea condiționării la comportamentul uman și respingerea introspectiei",
            "introducerea condiționării operate și a programelor de întărire",
            "dezvoltarea teoriei învățării întâmplătoare în consilierea vocațională",
            "formularea modelului de personalitate PEN",
        ],
        "correct": "a",
    },
    {
        "stem": "Experimentul „Little Albert” (John B. Watson și Rosalie Rayner, 1920) a urmărit să arate că:",
        "options": [
            "frica poate fi condiționată clasic prin asocierea unui obiect neutru cu un stimul aversiv",
            "agresivitatea apare doar din frustrarea unui scop blocat",
            "personalitatea se moștenește exclusiv prin gene",
            "întărirea negativă este singura metodă de modificare comportamentală",
        ],
        "correct": "a",
    },
    {
        "stem": "În experimentul Little Albert, stimulul necondiționat aversiv a fost:",
        "options": [
            "un zgomot puternic produs de lovirea unei bare de metal",
            "privarea de hrană timp de 24 de ore",
            "o mustrare verbală din partea experimentatorului",
            "o pedeapsă electrică aplicată la nivelul labei",
        ],
        "correct": "a",
    },
    {
        "stem": "Controversa etică a experimentului Little Albert include faptul că:",
        "options": [
            "nu există dovezi clare că decondiționarea a fost realizată complet înainte de încheiere",
            "Albert a fost un adult care și-a dat consimțământul informat",
            "experimentul a demonstrat imposibilitatea condiționării emoționale",
            "Watson a renunțat ulterior la behaviorism în favoarea psihanalizei",
        ],
        "correct": "a",
    },
    {
        "stem": "John B. Watson este cunoscut pentru afirmația că, dat fiind un grup de sugari sănătoși, ar putea:",
        "options": [
            "antrena orice copil spre orice specializare profesională, indiferent de talente",
            "demonstra existența inconștientului colectiv la vârsta preșcolară",
            "dovedi superioritatea terapiei psihanalitice pe termen lung",
            "elimina necesitatea mediului social în formarea comportamentului",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi autor–aport sunt corecte pentru condiționarea clasică?",
        "options": [
            "Ivan P. Pavlov — asocierea reflexului condiționat la câini",
            "John B. Watson — extinderea ideilor clasice la emoții umane",
            "B.F. Skinner — condiționarea clasică ca paradigma principală",
            "John B. Watson — manifestul behaviorismului împotriva psihologiei conștiinței",
        ],
        "correct": "abd",
    },
    {
        "stem": "Generalizarea stimulului în condiționarea clasică (ex. la Little Albert) înseamnă că:",
        "options": [
            "răspunsul condiționat apare și la stimuli asemănători cu stimulul condiționat",
            "comportamentul este menținut doar prin întărire intermitentă",
            "frustrarea unui scop produce automat agresivitate",
            "personalitatea se stabilizează după vârsta de 6 ani",
        ],
        "correct": "a",
    },
    # —— Skinner & condiționarea operantă (11–22) ——
    {
        "stem": "B.F. Skinner se deosebește de Ivan P. Pavlov prin accentul pus pe:",
        "options": [
            "consecințele comportamentului (întăriri și pedepse), nu doar asocierea stimulilor",
            "reflexele fiziologice ale sistemului digestiv",
            "interpretarea simbolică a viselor",
            "conflictele din copilărie ca sursă unică a neurozei",
        ],
        "correct": "a",
    },
    {
        "stem": "În condiționarea operantă a lui B.F. Skinner, întărirea pozitivă presupune:",
        "options": [
            "prezentarea unui stimul plăcut după comportament, crescând probabilitatea lui",
            "eliminarea unui stimul aversiv după comportament",
            "asocierea a doi stimuli neutri fără consecință",
            "interpretarea inconștientă a motivației comportamentului",
        ],
        "correct": "a",
    },
    {
        "stem": "Întărirea negativă, la B.F. Skinner, înseamnă:",
        "options": [
            "eliminarea unui stimul neplăcut după comportament, crescând probabilitatea lui",
            "aplicarea unei pedepse după comportamentul nedorit",
            "absența oricărei reacții din partea mediului",
            "respingerea conștientă a unei recompense materiale",
        ],
        "correct": "a",
    },
    {
        "stem": "„Cutia Skinner” (chamber) a fost folosită pentru a studia mai ales:",
        "options": [
            "modul în care programele de întărire controlează comportamentul șobolanului",
            "reflexul condiționat salivar la câini",
            "transferul și contratransferul în psihoterapie",
            "tipurile de personalitate introvertă și extravertă",
        ],
        "correct": "a",
    },
    {
        "stem": "Întărirea cu raport fix (ex. la fiecare 5 apăsări) produce, de regulă:",
        "options": [
            "o rată relativ constantă a comportamentului, cu pauză după recompensă",
            "o rată foarte stabilă, fără pauze după recompensă",
            "extincție rapidă când întărirea încetează",
            "generalizarea fricii la stimuli similari",
        ],
        "correct": "a",
    },
    {
        "stem": "Întărirea cu raport variabil (ex. recompensă imprevizibilă) tinde să producă:",
        "options": [
            "un comportament foarte persistent și rezistent la extincție",
            "extincție imediată la prima absență a recompensei",
            "scăderea generalizării stimulului condiționat",
            "apariția neurozei prin frustrare",
        ],
        "correct": "a",
    },
    {
        "stem": "Behaviorismul radical al lui B.F. Skinner susține că:",
        "options": [
            "comportamentul este determinat de istoria întăririlor, nu de stări mentale ca cauze",
            "libertatea umană este absolută și imposibil de studiat științific",
            "inconștientul este singurul obiect valid al psihologiei",
            "emoțiile sunt entități spirituale independente de mediu",
        ],
        "correct": "a",
    },
    {
        "stem": "Cartea „Beyond Freedom and Dignity” (B.F. Skinner) a stârnit controverse deoarece:",
        "options": [
            "propunea redesenarea societății prin control comportamental planificat",
            "respingea orice formă de întărire în educație",
            "susținea revenirea la psihanaliza freudiană",
            "nega existența învățării la animale",
        ],
        "correct": "a",
    },
    {
        "stem": "Extincția în condiționarea operantă (B.F. Skinner) apare atunci când:",
        "options": [
            "comportamentul nu mai este urmat de întărire și scade în frecvență",
            "se adaugă un stimul aversiv care crește comportamentul",
            "se asociază un stimul neutru cu un reflex necondiționat",
            "clientul obține insight despre cauza inconștientă",
        ],
        "correct": "a",
    },
    {
        "stem": "Un educator notează că un elev ridică mâna doar când profesorul îl privește. În logica lui B.F. Skinner, comportamentul este menținut prin:",
        "options": [
            "întărire socială (atenție, aprobare) după răspuns",
            "condiționare clasică între două stimuli neutri",
            "sublimarea pulsului în activitate academică",
            "analiza conflictului Oedip",
        ],
        "correct": "a",
    },
    {
        "stem": "Care distincții Pavlov–Skinner sunt corecte?",
        "options": [
            "Pavlov — răspuns reflex, elicitat de stimul; Skinner — răspuns operant, emis de organism",
            "Pavlov — asociere stimul–stimul; Skinner — relație comportament–consecință",
            "Pavlov — programe de întărire; Skinner — reflex salivar",
            "ambii reduc psihologia la introspectia conștientă",
        ],
        "correct": "ab",
    },
    {
        "stem": "În aplicarea clinică derivată din B.F. Skinner, token economy presupune:",
        "options": [
            "întărirea comportamentelor țintă prin jetoane schimbabile cu privilegii",
            "interpretarea visului ca material inconștient",
            "expunerea imaginară la stimuli fobici fără ierarhie",
            "disputa convingerilor iraționale",
        ],
        "correct": "a",
    },
    # —— Dollard & Miller (23–32) ——
    {
        "stem": "John Dollard și Neal E. Miller sunt cunoscuți pentru ipoteza:",
        "options": [
            "frustrare–agresivitate: frustrarea unui scop produce tendința de agresiune",
            "condiționare clasică a reflexului salivar",
            "tipologia introvertit–extravertit a personalității",
            "învățarea întâmplătoare în carieră",
        ],
        "correct": "a",
    },
    {
        "stem": "Ipoteza frustrare–agresivitate (John Dollard și Neal E. Miller, 1939) a fost criticată ulterior deoarece:",
        "options": [
            "agresivitatea poate fi redirecționată (deplasare), nu apare întotdeauna direct",
            "frustrarea nu are legătură cu comportamentul uman",
            "experimentele lui Pavlov au infirmat-o complet",
            "Skinner a demonstrat că frustrarea întărește orice comportament",
        ],
        "correct": "a",
    },
    {
        "stem": "Neal E. Miller a studiat conflictul abordare–evitare la șobolani. Concluzia relevantă pentru psihoterapie este că:",
        "options": [
            "comportamentul apare când tendințele de apropiere și evitare sunt aproximativ egale",
            "conflictele inconștiente sunt singura cauză a anxietății",
            "întărirea negativă nu influențează comportamentul",
            "frustrarea elimină orice învățare anterioară",
        ],
        "correct": "a",
    },
    {
        "stem": "Aportul lui Neal E. Miller la psihofiziologie include dezvoltarea:",
        "options": [
            "biofeedback-ului — învățarea controlului voluntar asupra răspunsurilor autonome",
            "analizei transferului în psihoterapie",
            "testelor proiective de tip Rorschach",
            "teoriei arhetipurilor din inconștientul colectiv",
        ],
        "correct": "a",
    },
    {
        "stem": "John Dollard și Neal E. Miller au încercat să integreze:",
        "options": [
            "concepte psihanalitice (nevoi, drive) cu principii de învățare behavioristă",
            "teoria gestaltică cu analiza tranzacțională",
            "cognitivismul beckian cu terapia strategică",
            "existențialismul cu psihodrama moreniană",
        ],
        "correct": "a",
    },
    {
        "stem": "La Neal E. Miller, un drive învățat (learned drive) este:",
        "options": [
            "o motivație dobândită prin asociere cu stimuli care reduc disconfortul",
            "un instinct fix, imuabil genetic",
            "o trăsătură de personalitate măsurată prin chestionar",
            "un arhetip din inconștientul colectiv",
        ],
        "correct": "a",
    },
    {
        "stem": "Un șofer în coloană blochează drumul. Conform ipotezei Dollard–Miller, reacția de furie poate fi înțeleasă ca:",
        "options": [
            "răspuns la frustrarea obiectivului de a avansa",
            "dovadă a fixării în stadiul oral freudian",
            "rezultat al condiționării clasice a fricii",
            "manifestare a individuării jungiene",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de B.F. Skinner, Dollard și Miller pun accent suplimentar pe:",
        "options": [
            "motive interne (drive-uri) și conflicte între răspunsuri incompatibile",
            "programe de întărire fără referință la nevoi",
            "respingerea oricărei influențe psihodinamice",
            "tipologia genetică a personalității",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu corect aportul lui Neal E. Miller?",
        "options": [
            "conflictul abordare–evitare în laborator",
            "biofeedback și control voluntar al răspunsurilor fiziologice",
            "condiționarea clasică a câinilor lui Pavlov",
            "frustrare–agresivitate, formulată împreună cu John Dollard",
        ],
        "correct": "abd",
    },
    {
        "stem": "John Dollard, spre deosebire de Ivan P. Pavlov, a fost interesat mai ales de:",
        "options": [
            "integrarea învățării cu dinamica socială și psihodinamică a comportamentului uman",
            "secreția salivară ca reflex fiziologic pur",
            "programele de întărire în cutia Skinner",
            "măsurarea factorilor genetici PEN",
        ],
        "correct": "a",
    },
    # —— Eysenck (33–42) ——
    {
        "stem": "Hans J. Eysenck a promovat în Marea Britanie:",
        "options": [
            "terapia comportamentală ca alternativă la psihoterapia psihanalitică lungă",
            "respingerea oricărei intervenții pe comportament observabil",
            "analiza asociației libere ca unică tehnică",
            "terapia centrată pe realitate a lui William Glasser",
        ],
        "correct": "a",
    },
    {
        "stem": "Hans J. Eysenck este asociat cu modelul de personalitate:",
        "options": [
            "extraversiune–introversiune, neuroticism și (ulterior) psihoticism (PEN)",
            "Parent–Adult–Copil din analiza tranzacțională",
            "inferioritate–compensare din psihologia individuală",
            "sinele real–idealizat din teoria Karei Horney",
        ],
        "correct": "a",
    },
    {
        "stem": "Controversa dintre Hans J. Eysenck și psihanaliști a vizat mai ales:",
        "options": [
            "eficacitatea și durata necesară a psihoterapiei psihanalitice",
            "utilitatea condiționării clasice la câini",
            "existența inconștientului colectiv jungian",
            "rolul întâmplării în carieră",
        ],
        "correct": "a",
    },
    {
        "stem": "Hans J. Eysenck a susținut că multe forme de neuroză pot fi tratate prin:",
        "options": [
            "intervenții comportamentale directe, nu doar prin explorarea inconștientului",
            "interpretarea autoritară a viselor din copilărie",
            "acceptarea necondiționată ca singură metodă",
            "scaunul gol gestaltic",
        ],
        "correct": "a",
    },
    {
        "stem": "Legătura lui Hans J. Eysenck cu desensibilizarea sistematică se referă la faptul că:",
        "options": [
            "a popularizat și susținut terapia comportamentală pentru anxietate în Europa",
            "a inventat cutia Skinner pentru expunere",
            "a formulat ipoteza frustrare–agresivitate",
            "a dezvoltat teoria învățării întâmplătoare",
        ],
        "correct": "a",
    },
    {
        "stem": "Hans J. Eysenck a folosit studii pe gemeni pentru a argumenta:",
        "options": [
            "componenta ereditară a trăsăturilor de personalitate",
            "imposibilitatea condiționării la oameni",
            "superioritatea absolută a mediului asupra geneticii",
            "inexistența diferențelor individuale",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de John B. Watson, Hans J. Eysenck a adus în psihoterapie:",
        "options": [
            "evaluare empirică a eficacității tratamentelor și protocoale comportamentale",
            "experimentul Little Albert pe sugari",
            "manifestul împotriva conștiinței ca obiect de studiu",
            "condiționarea salivară la câini",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client cu fobie socială. Abordarea inspirată de Hans J. Eysenck ar include mai probabil:",
        "options": [
            "expunere graduală și restructurare comportamentală, cu măsurare a progresului",
            "analiza liberă a asociațiilor timp de cinci ani",
            "interpretarea simbolică obligatorie a viselor",
            "prescrierea simptomului în terapia de familie",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi autor–aport sunt corecte pentru Hans J. Eysenck?",
        "options": [
            "modelul PEN al personalității",
            "promovarea terapiei comportamentale în locul psihanalizei lungi",
            "condiționarea operantă în cutia Skinner",
            "criticarea empirică a unor forme de psihoterapie",
        ],
        "correct": "abd",
    },
    {
        "stem": "Hans J. Eysenck se deosebește de B.F. Skinner prin faptul că a pus accent mai mare pe:",
        "options": [
            "personalitate, diferențe individuale și aplicații clinice la anxietate",
            "programe de întărire în laborator la șobolani",
            "respingerea măsurătorii comportamentului",
            "utopia socială din „Walden Two”",
        ],
        "correct": "a",
    },
    # —— Krumboltz (43–50) ——
    {
        "stem": "John D. Krumboltz este cunoscut în consilierea vocațională pentru:",
        "options": [
            "teoria învățării sociale aplicată la carieră și ulterior planned happenstance",
            "experimentul Little Albert asupra fricii condiționate",
            "ipoteza frustrare–agresivitate din Yale",
            "modelul PEN al personalității",
        ],
        "correct": "a",
    },
    {
        "stem": "Teoria învățării sociale a carierei (John D. Krumboltz) explică alegerea profesională prin:",
        "options": [
            "învățare (modelare, întăriri, asocieri) și factori cognitiv-comportamentali",
            "fixarea freudiană în stadiul genital",
            "arhetipurile din inconștientul colectiv",
            "triangularea obligatorie în familie",
        ],
        "correct": "a",
    },
    {
        "stem": "„Planned happenstance” (John D. Krumboltz) sugerează că:",
        "options": [
            "evenimentele neplanificate pot deveni oportunități dacă clientul dezvoltă curiozitate și flexibilitate",
            "cariera este determinată exclusiv de testele de aptitudine la 14 ani",
            "orice întâmplare este irrelevantă pentru decizia vocațională",
            "frustrarea produce automat agresivitate în carieră",
        ],
        "correct": "a",
    },
    {
        "stem": "Față de B.F. Skinner, John D. Krumboltz aplică învățarea comportamentală mai ales la:",
        "options": [
            "consilierea carierei și deciziilor educaționale, nu la contingențe de laborator",
            "reflexul condiționat salivar",
            "biofeedback-ul autonom",
            "tratarea psihozei prin electroșoc",
        ],
        "correct": "a",
    },
    {
        "stem": "Un student spune: „Am ajuns psiholog pentru că un profesor m-a încurajat la olimpiadă.” John D. Krumboltz ar sublinia:",
        "options": [
            "rolul modelelor, întăririlor și experiențelor de învățare în alegerea carierei",
            "destinul arhetipal fixat la naștere",
            "complexul Oedip ca explicație unică",
            "condiționarea clasică a fricii de eșec",
        ],
        "correct": "a",
    },
    {
        "stem": "John D. Krumboltz critică abordările care:",
        "options": [
            "tratează alegerea carierei ca pe o decizie unică, statică, fără învățare continuă",
            "folosesc deloc conceptul de învățare în consiliere",
            "iau în calcul curiozitatea și flexibilitatea clientului",
            "integrează modelarea socială",
        ],
        "correct": "a",
    },
    {
        "stem": "Care afirmații descriu John D. Krumboltz, nu Ivan P. Pavlov?",
        "options": [
            "focus pe consilierea vocațională și decizii de carieră",
            "planned happenstance și oportunități neașteptate",
            "studii pe secreția salivară a câinilor",
            "integrarea învățării în planificarea educațională",
        ],
        "correct": "abd",
    },
    {
        "stem": "În practica inspirată de John D. Krumboltz, terapeutul/consilierul poate:",
        "options": [
            "ajuta clientul să experimenteze comportamente noi și să observe consecințele",
            "interpreta autoritar visul ca profeție",
            "prescrie o singură profesie potrivită pe viață",
            "evita orice discuție despre factorii de mediu",
        ],
        "correct": "a",
    },
    # —— Comparativ & controverse (51–60) ——
    {
        "stem": "Care autor a condus paradigma condiționării clasice la animale, fără focus inițial pe psihoterapie?",
        "options": [
            "Ivan P. Pavlov",
            "B.F. Skinner",
            "Hans J. Eysenck",
            "John D. Krumboltz",
        ],
        "correct": "a",
    },
    {
        "stem": "Care autor a fost implicat direct în controversa etică Little Albert?",
        "options": [
            "John B. Watson",
            "Ivan P. Pavlov",
            "Neal E. Miller",
            "John D. Krumboltz",
        ],
        "correct": "a",
    },
    {
        "stem": "Care autor a formulat utopia controlului comportamental social în „Walden Two”?",
        "options": [
            "B.F. Skinner",
            "John Dollard",
            "Hans J. Eysenck",
            "John B. Watson",
        ],
        "correct": "a",
    },
    {
        "stem": "Un experimentator dorește să crească frecvența unui comportament prin consecințe, nu prin asocierea a doi stimuli. Paradigma potrivită este:",
        "options": [
            "condiționarea operantă (B.F. Skinner)",
            "condiționarea clasică (Ivan P. Pavlov)",
            "ipoteza frustrare–agresivitate (Dollard–Miller)",
            "modelul PEN (Hans J. Eysenck)",
        ],
        "correct": "a",
    },
    {
        "stem": "Un client învață să relaxeze musculatura pentru a controla tensiunea arterială. Aportul relevant este asociat cu:",
        "options": [
            "Neal E. Miller — biofeedback",
            "Ivan P. Pavlov — reflex condiționat",
            "John B. Watson — Little Albert",
            "John D. Krumboltz — planned happenstance",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi autor–temă sunt greșite?",
        "options": [
            "Ivan P. Pavlov — cutia Skinner",
            "John Dollard — frustrare–agresivitate",
            "Hans J. Eysenck — terapie comportamentală",
            "John D. Krumboltz — consiliere vocațională",
        ],
        "correct": "a",
    },
    {
        "stem": "În psihoterapie, tranziția de la behaviorismul strict Watson la aportul lui Hans J. Eysenck a însemnat mai ales:",
        "options": [
            "de la manifest programatic la protocoale clinice evaluate empiric",
            "de la întărire la respingerea oricărei măsurători",
            "explicații strict intrapsihice, fără date comportamentale sistematice",
            "de la psihanaliză la exclusiv meditație",
        ],
        "correct": "a",
    },
    {
        "stem": "Diferența dintre întărirea la B.F. Skinner și asocierea la Ivan P. Pavlov constă în faptul că:",
        "options": [
            "la Pavlov, stimulii elicitează reflexe; la Skinner, consecințele modelează comportamente emise",
            "la Pavlov, consecințele modelează comportamente emise; la Skinner, stimulii elicitează reflexe",
            "ambii folosesc doar pedeapsa ca metodă principală",
            "niciunul nu a aplicat principii la om",
        ],
        "correct": "a",
    },
    {
        "stem": "John Dollard și Neal E. Miller, John B. Watson și B.F. Skinner au în comun:",
        "options": [
            "accentul pe învățare și pe observarea comportamentului, nu pe introspectie",
            "respingerea completă a experimentului de laborator",
            "orientarea spre psihanaliza freudiană clasică",
            "utilizarea exclusivă a teoriei arhetipurilor",
        ],
        "correct": "a",
    },
    {
        "stem": "Afirmația: „Toți autorii enumerați au contribuit la aplicarea ideilor behavioriste, dar pe domenii diferite” este corectă deoarece:",
        "options": [
            "Pavlov și Watson — condiționare clasică; Skinner — operant; Dollard–Miller — conflict și frustrare; Eysenck — terapie și personalitate; Krumboltz — carieră",
            "toți au condus experimentul Little Albert",
            "toți au respins ideea de învățare",
            "toți au formulat modelul PEN",
        ],
        "correct": "a",
    },
]
