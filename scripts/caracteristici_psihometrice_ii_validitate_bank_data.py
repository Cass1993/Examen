"""Itemi — Caracteristici psihometrice II, cap. 3: validitatea testului (60 itemi)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

VALIDITATE_TEST_ITEMS: List[Item] = [
    {
        "stem": "Validitatea de conținut verifică dacă itemii acoperă reprezentativ domeniul de comportamente vizat.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Validitatea predictivă implică măsurarea predictorului după ce criteriul a fost deja observat.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "În analiza validității de construct, convergența ridicată între metode diferite pentru același construct susține validitatea.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Dacă rxy depășește rtt, validitatea criterială este considerată imposibilă teoretic.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Eroarea standard de estimare (SEE) crește când validitatea criterială rxy crește.",
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Contaminarea criteriului apare când scorul la predictor influențează direct măsura criteriului.",
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": "Ce descrie cel mai bine validitatea de conținut?",
        "options": [
            "gradul în care itemii eșantionează reprezentativ universul domeniului",
            "corelația testului cu un criteriu măsurat ulterior",
            "stabilitatea scorurilor la retestare",
            "capacitatea itemilor de a discrimina extremitățile distribuției",
        ],
        "correct": "a",
    },
    {
        "stem": "În validitatea de criteriu, „predictorul” este:",
        "options": [
            "testul folosit pentru anticiparea unui comportament relevant",
            "variabila externă folosită exclusiv pentru normare",
            "scorul corectat pentru ghicire la itemi obiectivi",
            "indicatorul intern de consistență între itemi",
        ],
        "correct": "a",
    },
    {
        "stem": "Validitatea concurentă presupune, de regulă:",
        "options": [
            "măsurarea predictorului și criteriului aproximativ în același interval temporal",
            "estimarea validității doar pe baza consistenței interne",
            "măsurarea criteriului exclusiv la distanță de câțiva ani",
            "eliminarea completă a erorii de criteriu prin randomizare",
        ],
        "correct": "a",
    },
    {
        "stem": "În formula Lawshe pentru CVR, termenul Ne reprezintă:",
        "options": [
            "numărul experților care consideră itemul esențial",
            "numărul total de itemi ai scalei",
            "numărul respondenților care au răspuns corect",
            "numărul itemilor eliminați după analiză factorială",
        ],
        "correct": "a",
    },
    {
        "stem": "Un coeficient rxy este interpretat direct ca:",
        "options": [
            "indicator al relației dintre predictor și criteriu",
            "coeficient de fidelitate internă",
            "măsură a reprezentativității eșantionului normativ",
            "indice al dificultății medii a itemilor",
        ],
        "correct": "a",
    },
    {
        "stem": "Relația corectă dintre validitate și fidelitate este că, în practică:",
        "options": [
            "validitatea este limitată superior de fidelitate",
            "validitatea nu depinde deloc de fidelitate",
            "fidelitatea este mereu mai mică decât validitatea",
            "validitatea înlocuiește analiza fidelității",
        ],
        "correct": "a",
    },
    {
        "stem": "Care este formula de corecție a scorului pentru ghicire la itemi obiectivi?",
        "options": [
            "X - W/(n-1)",
            "X + W/(n-1)",
            "X - W*n",
            "(X-W)/n",
        ],
        "correct": "a",
    },
    {
        "stem": "În regulile Thorndike pentru itemi cu alegere multiplă, o recomandare centrală este:",
        "options": [
            "distractori plauzibili, apropiați semantic de răspunsul corect",
            "alternanță rigidă a poziției răspunsului corect la fiecare 4 itemi",
            "folosirea frecventă a variantelor „toate sunt corecte”",
            "accentuarea răspunsului corect prin formulare mai lungă",
        ],
        "correct": "a",
    },
    {
        "stem": "Validitatea de construct urmărește în principal:",
        "options": [
            "coerența rețelei teoretice și a dovezilor convergente/discriminante",
            "estimarea rapidă a timpului mediu de completare",
            "mărimea eșantionului necesar pentru normare",
            "raportul dintre itemii ușori și dificili",
        ],
        "correct": "a",
    },
    {
        "stem": "În matricea MTMM, validitatea convergentă este susținută când:",
        "options": [
            "măsurile aceluiași construct prin metode diferite corelează ridicat",
            "corelațiile heterotrait-monomethod sunt cele mai mari",
            "toate corelațiile sunt apropiate de zero",
            "corelațiile monotrait-monomethod lipsesc",
        ],
        "correct": "a",
    },
    {
        "stem": "În etapele propuse de Cronbach pentru validitatea de construct, un pas major este:",
        "options": [
            "formularea rețelei nomologice și testarea predicțiilor derivate",
            "înlocuirea oricărui criteriu extern cu judecata intuitivă",
            "fixarea validității exclusiv prin CVR",
            "evitarea revizuirii itemilor după date empirice",
        ],
        "correct": "a",
    },
    {
        "stem": "Ce exprimă SEE în contextul validității criteriale?",
        "options": [
            "eroarea medie de predicție a criteriului din scorul la predictor",
            "numărul minim de itemi necesar pentru fidelitate ridicată",
            "diferența dintre două forme paralele",
            "proporția de răspunsuri ghicite corect",
        ],
        "correct": "a",
    },
    {
        "stem": "Dacă rxy este mic, predicția criteriului va fi de regulă:",
        "options": [
            "mai imprecisă, cu SEE mai mare",
            "mai precisă, cu SEE mai mică",
            "independentă de SEE",
            "neinfluențată de dispersia criteriului",
        ],
        "correct": "a",
    },
    {
        "stem": "Un criteriu „relevant” în validitatea de criteriu este acela care:",
        "options": [
            "reflectă direct comportamentul sau performanța de interes",
            "este cel mai ușor de colectat logistic",
            "are distribuție normală perfectă",
            "nu se corelează cu predictorul",
        ],
        "correct": "a",
    },
    {
        "stem": "Un criteriu „contaminat” este:",
        "options": [
            "influențat de informații derivate din predictor",
            "măsurat cu întârziere mare",
            "format exclusiv din indicatori obiectivi",
            "lipsit de varianță",
        ],
        "correct": "a",
    },
    {
        "stem": "În tipologia itemilor, un item obiectiv este caracterizat de:",
        "options": [
            "scorare neambiguă, pe bază de cheie explicită",
            "interpretare simbolică dependentă de evaluator",
            "răspuns narativ fără barem",
            "notare exclusiv holistică",
        ],
        "correct": "a",
    },
    {
        "stem": "Itemii semiobiectivi se diferențiază prin faptul că:",
        "options": [
            "au criterii de scorare definite, dar cer uneori judecată în aplicare",
            "nu permit deloc barem de notare",
            "au un singur răspuns literal posibil, fără interpretare",
            "elimină complet variabilitatea între evaluatori",
        ],
        "correct": "a",
    },
    {
        "stem": "Itemii subiectivi implică în mod tipic:",
        "options": [
            "pondere mai mare a interpretării evaluatorului",
            "scorare exclusiv automată",
            "lipsa unui protocol formal de evaluare",
            "validitate de criteriu obligatoriu superioară",
        ],
        "correct": "a",
    },
    {
        "stem": "În tabela de interpretare Smith pentru rxy, valorile mai mari indică de regulă:",
        "options": [
            "utilitate predictivă mai ridicată",
            "eroare mai mare de predicție",
            "dovezi mai slabe de relație predictor-criteriu",
            "inevitabil contaminare de criteriu",
        ],
        "correct": "a",
    },
    {
        "stem": "Care formulare respectă cel mai bine regula Thorndike privind claritatea itemului?",
        "options": [
            "enunț clar, o singură problemă cognitivă per item",
            "enunț lung cu două negații pentru a crește dificultatea",
            "amestec de cerințe în aceeași întrebare pentru economie de spațiu",
            "introducerea de termeni ambigui pentru discriminare fină",
        ],
        "correct": "a",
    },
    {
        "stem": "Obligația principală a constructorului de test, în validitatea de conținut, este:",
        "options": [
            "definirea domeniului și maparea explicită item-domeniu",
            "maximizarea numărului de itemi indiferent de relevanță",
            "înlocuirea evaluării experților cu popularitatea itemilor",
            "menținerea itemilor chiar dacă experții îi consideră periferici",
        ],
        "correct": "a",
    },
    {
        "stem": "În evaluarea judecătorilor pentru validitate de conținut, criterii centrale sunt:",
        "options": [
            "esențialitatea itemului pentru constructul țintă",
            "relevanța itemului pentru domeniul măsurat",
            "poziția itemului în test",
            "nivelul de dificultate dorit de autor",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce relație este corectă pentru validitatea criterială și SEE?",
        "options": [
            "SEE depinde de validitate (rxy), nu de fidelitate (rtt)",
            "SEE reflectă în principal fidelitatea predictorului",
            "SEE este identică numeric cu rxy",
            "SEE nu folosește deviația standard a criteriului",
        ],
        "correct": "a",
    },
    {
        "stem": "Selectează perechile corecte dintre tipul de validitate și focalizarea lui principală.",
        "options": [
            "validitate de conținut - acoperirea reprezentativă a domeniului",
            "validitate de criteriu - relația predictor-criteriu",
            "validitate de construct - estimarea exclusivă a stabilității temporale",
            "validitate de conținut - estimarea fidelității test-retest",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații diferențiază adecvat validitatea predictivă de cea concurentă?",
        "options": [
            "predictiva implică separare temporală între predictor și criteriu",
            "concurenta măsoară predictorul și criteriul aproximativ simultan",
            "predictiva exclude complet utilizarea criteriilor comportamentale",
            "concurenta necesită întotdeauna urmărire longitudinală extinsă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce condiții sunt dorite pentru un criteriu bun în validarea criterială?",
        "options": [
            "relevanță pentru performanța de interes",
            "fidelitate suficientă a măsurii criteriului",
            "contaminare deliberată pentru creșterea corelației",
            "disponibilitate practică rezonabilă",
        ],
        "correct": "abd",
    },
    {
        "stem": "În modelul Lawshe, care enunțuri sunt corecte?",
        "options": [
            "CVR = (Ne - N/2) / (N/2)",
            "CVR poate lua valori negative dacă puțini experți marchează „esențial”",
            "valoarea minimă acceptabilă este aceeași indiferent de numărul de experți",
            "CVR se calculează din scorurile respondenților la test",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce descrie corect contaminarea criteriului?",
        "options": [
            "criteriul include informații influențate de predictor",
            "duce artificial la supraestimarea validității",
            "este de dorit când selecția trebuie accelerată",
            "poate apărea când evaluatorii cunosc scorurile la test",
        ],
        "correct": "abd",
    },
    {
        "stem": "Despre relația rxy și rtt, care afirmații sunt corecte?",
        "options": [
            "în mod obișnuit rxy nu ar trebui să depășească rtt al predictorului",
            "fidelitatea scăzută limitează plafonul validității",
            "rxy > rtt confirmă automat validitate excepțională a testului",
            "rxy și rtt sunt același coeficient raportat în scale diferite",
        ],
        "correct": "ab",
    },
    {
        "stem": "Selectează formulările corecte despre SEE în validitatea de criteriu.",
        "options": [
            "SEE = SDy * sqrt(1-rxy^2)",
            "rxy mai mare tinde să reducă SEE",
            "SEE exprimă direct consistența internă a predictorului",
            "SEE este formula standard pentru consistență internă",
        ],
        "correct": "ab",
    },
    {
        "stem": "În matricea MTMM, ce pattern susține validitatea discriminantă?",
        "options": [
            "corelațiile monotrait-heteromethod depășesc corelațiile heterotrait",
            "corelațiile heterotrait-heteromethod rămân relativ mai mici",
            "orice corelație mare între constructe diferite este preferabilă",
            "constructele distincte nu trebuie să devină empiric indistincte",
        ],
        "correct": "abd",
    },
    {
        "stem": "În etapele lui Cronbach privind constructul, ce practici sunt potrivite?",
        "options": [
            "definirea explicită a constructului",
            "derivarea predicțiilor teoretice testabile",
            "menținerea neschimbată a itemilor chiar dacă datele contrazic teoria",
            "blocarea permanentă a instrumentului după prima administrare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce afirmații sunt adecvate pentru clasificarea itemilor după scorare?",
        "options": [
            "itemii obiectivi au cheie de răspuns clară",
            "itemii semiobiectivi pot necesita rubrici și judecată",
            "itemii subiectivi elimină aproape complet diferențele între evaluatori",
            "itemii obiectivi elimină complet eroarea de măsurare",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care recomandări sunt compatibile cu regulile Thorndike pentru alegere multiplă?",
        "options": [
            "evitarea indiciilor gramaticale către cheia corectă",
            "distractori omogeni ca lungime și stil",
            "introducerea deliberată a dublului negativ pentru a crește dificultatea",
            "folosirea frecventă a opțiunii „niciuna” pentru a compensa itemii slabi",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce condiții definesc cel mai bine validitatea de conținut?",
        "options": [
            "delimitarea universului domeniului",
            "eșantionare reprezentativă a conținutului prin itemi",
            "evitarea evaluării de către judecători pentru a reduce variabilitatea",
            "obținerea unui rxy ridicat cu un criteriu extern",
        ],
        "correct": "ab",
    },
    {
        "stem": "În evaluarea judecătorilor pentru conținut, ce triadă de criterii este uzuală?",
        "options": [
            "esențialitate",
            "relevanță",
            "claritate",
            "viteză de răspuns",
        ],
        "correct": "abc",
    },
    {
        "stem": "Selectează afirmațiile corecte despre validitatea predictivă.",
        "options": [
            "folosește criteriu colectat la un moment ulterior predictorului",
            "este utilă când decizia vizează performanță viitoare",
            "poate fi afectată de schimbări contextuale între momentele măsurării",
            "elimină necesitatea unui criteriu bine definit",
        ],
        "correct": "abc",
    },
    {
        "stem": "Selectează afirmațiile corecte despre validitatea concurentă.",
        "options": [
            "predictorul și criteriul sunt măsurate în același interval",
            "este frecvent utilizată pentru comparație cu instrumente deja consacrate",
            "nu garantează automat putere predictivă pe termen lung",
            "presupune obligatoriu design experimental randomizat",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații descriu adecvat interpretarea coeficientului rxy după tabele orientative (ex. Smith)?",
        "options": [
            "valorile foarte mici indică utilitate practică redusă",
            "valorile moderate pot fi utile în decizii de grup",
            "valorile mai mari susțin predicții mai stabile",
            "orice valoare pozitivă, indiferent cât de mică, e suficientă pentru decizii individuale cu miză mare",
        ],
        "correct": "abc",
    },
    {
        "stem": "În rețeaua nomologică, ce dovezi sunt în acord cu validitatea de construct?",
        "options": [
            "corelații cu variabile teoretic apropiate",
            "diferențiere față de constructe distincte",
            "pattern-uri de relații conforme predicțiilor anterioare",
            "lipsa relațiilor empirice așteptate teoretic",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care set de afirmații despre SEE este corect?",
        "options": [
            "SEE este exprimată în unitățile criteriului",
            "SEE scade când crește asocierea predictor-criteriu",
            "SEE mare semnalează predicții mai dispersate în jurul valorii reale",
            "SEE este substitutul direct al coeficientului alfa",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce enunțuri despre corecția pentru ghicire X-W/(n-1) sunt corecte?",
        "options": [
            "W reprezintă numărul răspunsurilor greșite",
            "n reprezintă numărul alternativelor de răspuns",
            "corecția reduce avantajul răspunsului aleator",
            "formula crește scorul când numărul de erori crește",
        ],
        "correct": "abc",
    },
    {
        "stem": "Ce propoziții sintetizează corect cele trei tipuri majore de validitate?",
        "options": [
            "conținutul examinează acoperirea domeniului",
            "criteriul evaluează legătura cu un indicator extern",
            "constructul testează coerența teoretică și empirică",
            "toate trei sunt complet interschimbabile metodologic",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care combinație de afirmații despre validitatea de conținut este corectă?",
        "options": [
            "constructorul definește clar domeniul și specificațiile",
            "itemii trebuie să reprezinte proporțional zonele domeniului",
            "judecătorii apreciază esențialitatea/relevanța/claritatea",
            "validitatea de conținut se reduce la o singură corelație externă",
        ],
        "correct": "abc",
    },
    {
        "stem": "În evaluarea criterială, ce afirmații sunt corecte?",
        "options": [
            "predictorul este scorul la testul evaluat",
            "criteriul poate fi comportamental, academic sau profesional",
            "contaminarea criteriului poate umfla artificial rxy",
            "rxy nu poate fi interpretat fără contextul fidelității și al scopului deciziei",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Selectează setul corect privind validitatea de construct și MTMM.",
        "options": [
            "convergența cere corelații ridicate pentru același construct prin metode diferite",
            "discriminarea cere corelații mai mici între constructe diferite",
            "Campbell și Fiske au propus matricea multitrait-multimethod",
            "pattern-ul corelațiilor se evaluează comparativ, nu pe o singură valoare izolată",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care afirmații despre relația rxy, rtt și SEE sunt corecte?",
        "options": [
            "rxy tinde să fie plafonat de fidelitatea predictorului",
            "dacă fidelitatea este mică, validitatea observată poate fi subestimată",
            "SEE depinde de rxy și de dispersia criteriului",
            "validitate mai mare este asociată, în general, cu SEE mai mică",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce recomandări sunt conforme regulilor Thorndike pentru itemi cu alegere multiplă?",
        "options": [
            "enunțul să fie clar și focalizat pe o singură problemă",
            "distractorii să fie plauzibili și omogeni",
            "să se evite indicii formale spre răspunsul corect",
            "să se minimizeze ambiguitatea lexicală inutilă",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Care afirmații despre tipurile de itemi după scorare sunt corecte?",
        "options": [
            "itemii obiectivi permit scorare standardizată cu cheie explicită",
            "itemii semiobiectivi folosesc rubrici, dar lasă loc judecății evaluatorului",
            "itemii subiectivi necesită control sporit al acordului între evaluatori",
            "alegerea tipului de item influențează calitatea datelor pentru validare",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce afirmații rezumă corect utilizarea tabelelor orientative de interpretare rxy (ex. Smith)?",
        "options": [
            "magnitudinea lui rxy se interpretează în raport cu scopul deciziei",
            "aceeași valoare poate avea utilitate diferită în contexte diferite",
            "interpretarea necesită și verificarea calității criteriului",
            "pragurile orientative ghidează, dar nu înlocuiesc judecata profesională",
        ],
        "correct": "abcd",
    },
    {
        "stem": "În practica validării de conținut, ce acțiuni sunt recomandate înainte de pilotare?",
        "options": [
            "construirea unei matrice specificații-conținut pentru itemi",
            "revizuire de către experți independenți față de autori",
            "excluderea itemilor cu indici de dificultate ridicată",
            "înlocuirea evaluării experților cu ordonarea aleatoare a itemilor",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce combinație descrie adecvat predictorul și criteriul într-un studiu de validitate?",
        "options": [
            "predictorul este instrumentul evaluat pentru utilitate practică",
            "criteriul este indicatorul extern relevant pentru decizie",
            "predictorul și criteriul trebuie să fie mereu aceeași măsură",
            "criteriul trebuie ales doar pentru că este cel mai ieftin de colectat",
        ],
        "correct": "ab",
    },
    {
        "stem": "Pentru reducerea riscului de contaminare a criteriului, ce măsuri sunt potrivite?",
        "options": [
            "separarea surselor de date pentru predictor și criteriu",
            "orbirea evaluatorilor criteriului la scorurile predictorului",
            "instruirea evaluatorilor pe cheia predictorului înainte de notare",
            "ajustarea criteriului după scorurile predictorului pentru consistență",
        ],
        "correct": "ab",
    },
    {
        "stem": "În interpretarea lui rxy după ghiduri orientative, ce este prudent metodologic?",
        "options": [
            "corelarea magnitudinii cu consecințele deciziei",
            "analiza împreună cu fidelitatea și calitatea criteriului",
            "acceptarea automată a oricărui rxy pozitiv în selecție individuală",
            "ignorarea SEE când rxy depășește 0,20",
        ],
        "correct": "ab",
    },
]


def _count_dist(rows):
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
        else:
            counts[str(len(set(row["correct"])))] += 1
    return counts


assert len(VALIDITATE_TEST_ITEMS) == 60
assert _count_dist(VALIDITATE_TEST_ITEMS) == {"1": 22, "2": 14, "3": 12, "4": 6, "TF": 6}
