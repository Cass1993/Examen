"""Itemi — Motivație (Curs 9–10), lot evaluare psihologică II."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

MOTIVATIE_ITEMS: List[Item] = [
    # —— Definiții și conținutul motivației (1–12) ——
    {
        "stem": (
            "Conform lui Heinz Heckhausen, motivația este procesul care determină:"
        ),
        "options": [
            "energizarea comportamentului",
            "direcția comportamentului spre un obiectiv",
            "reducerea emoțiilor negative fără mobilizarea cognitivă",
            "un singur factor biologic fix, fără influență cognitivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce sugerează perspectiva lui Carol Dweck și a colaboratorilor săi "
            "despre legătura dintre motivație și inteligență?"
        ),
        "options": [
            "pentru a înțelege inteligența, trebuie înțeleasă și motivația",
            "inteligența este dinamică — factori o favorizează sau o inhibă",
            "inteligența este un potențial fix, independent de motivație",
            "motivația este relevantă doar în evaluarea personalității, nu a cogniției",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Motivația pentru învățare include, pe lângă capacitatea intelectuală:"
        ),
        "options": [
            "convingeri despre propria capacitate sau despre natura inteligenței",
            "abilități non-intellectuale, cum ar fi autodisciplina",
            "afect pozitiv, cum ar fi plăcerea de a învăța",
            "scorul la un test de aptitudine cognitivă la un singur moment",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Convingerea că inteligența este o trăsătură fixă, imuabilă, tinde să "
            "reducă efortul după eșec, spre deosebire de convingerea în inteligență "
            "ca abilitate dezvoltabilă."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Motivația este un „motor simplu” care depinde doar de stimul extern, "
            "fără convingeri, afect sau autodisciplină."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Cum influențează afectul, cum ar fi plăcerea de a învăța, atingerea "
            "obiectivelor intelectuale?"
        ),
        "options": [
            "susține persistența și implicarea în sarcină",
            "facilitează orientarea spre obiective pe termen lung",
            "elimină nevoia de strategii sau de autodisciplină",
            "suplimentează evaluarea performanței cognitive, nu o înlocuiește",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre perspectivele științifice asupra motivației integrează "
            "date neurobiologice și simulări computerizate ale proceselor "
            "motivaționale?"
        ),
        "options": [
            "perspectiva neuroștiinței cognitive și a modelelor computaționale",
            "perspectiva psihologiei sociale, afective și a personalității",
            "perspectiva dezvoltării, îmbătrânirii și duratei vieții",
            "perspectiva psihanalitică, fără componentă experimentală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perspective științifice asupra motivației sunt recunoscute "
            "în literatura de specialitate?"
        ),
        "options": [
            "neuroștiință cognitivă și abordări computaționale",
            "psihologie socială, afectivă și a personalității",
            "dezvoltare umană, îmbătrânire și parcursul vieții",
            "doar teoria behavioristă clasică, fără alte cadre",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce studiază perspectiva dezvoltării și a duratei vieții în raport "
            "cu motivația?"
        ),
        "options": [
            "modificarea motivelor de la copilărie la bătrânețe",
            "schimbarea obiectivelor pe parcursul vieții",
            "identitatea motivației la toate vârstele, fără variație",
            "motivația adulților tineri, fără alte grupe de vârstă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un elev crede că poate îmbunătăți matematica prin exercițiu susținut "
            "și își organizează timpul zilnic. Aceasta ilustrează rolul:"
        ),
        "options": [
            "convingerilor despre dezvoltabilitatea abilităților",
            "abilităților non-intellectuale, cum ar fi autodisciplina",
            "moștenirea genetică, fără strategii de autoregulare",
            "lipsei oricărei componente motivaționale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce nu este suficient să măsori doar capacitatea intelectuală pentru "
            "a prezice succesul școlar pe termen lung?"
        ),
        "options": [
            "motivația, convingerile și autoregularea influențează utilizarea capacității",
            "afectul și plăcerea de a învăța susțin persistența",
            "coeficientul de inteligență singur determină automat performanța",
            "obiectivele intelectuale nu depind de factori non-cognitivi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care factori pot inhiba manifestarea inteligenței, în perspectiva "
            "dinamică a motivației?"
        ),
        "options": [
            "frica de eșec",
            "anxietate și convingeri negative despre sine",
            "autodisciplina și plăcerea de a învăța",
            "convingerea în dezvoltabilitatea abilităților",
        ],
        "correct": "ab",
    },
    # —— Autoeficacitate Bandura (13–20) ——
    {
        "stem": (
            "Ce definește Albert Bandura prin conceptul de autoeficacitate?"
        ),
        "options": [
            "convingerea subiectivă că poți reuși la o anumită sarcină",
            "judecata despre propria capacitate de a organiza și executa acțiunile necesare",
            "scorul obținut la un test de aptitudini generale",
            "trăsura stabilă de neuroticism măsurată pe chestionar",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Autoeficacitatea este un predictor pentru care dintre următoarele?"
        ),
        "options": [
            "alegerea cursurilor sau a sarcinilor dificile",
            "persistența și efortul investit",
            "utilizarea strategiilor și a autoregulării",
            "performanța anterioară, ca singur factor fără influență reciprocă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care este diferența dintre performanță și învățare, în sensul "
            "folosit în literatura despre autoeficacitate?"
        ),
        "options": [
            "performanța reflectă starea cunoștințelor la un moment dat",
            "învățarea reflectă creșterea competenței în timp",
            "performanța și învățarea sunt mereu identice ca măsurătoare",
            "învățarea exclude orice modificare ulterioară a comportamentului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Autoeficacitatea înaltă garantează automat succesul, indiferent de "
            "pregătirea reală sau de dificultatea sarcinii."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Un student cu autoeficacitate scăzută la scris academic evită cursurile "
            "cu lucrări lungi, deși are aptitudini cognitive bune. Aceasta ilustrează "
            "legătura dintre autoeficacitate și:"
        ),
        "options": [
            "alegerea sarcinilor",
            "evitarea situațiilor percepute ca amenințătoare la stima de sine",
            "performanța anterioară ca unic determinant, fără convingeri",
            "lipsa strategiilor de autoregulare în modelul explicat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Sursele care pot crește autoeficacitatea, în teoria lui Bandura, includ:"
        ),
        "options": [
            "experiențe de măiestrie directă",
            "modelarea prin observarea altora",
            "persuasiunea verbală și interpretarea stărilor fiziologice",
            "feedback-ul negativ, fără reușite anterioare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Performanța măsurată la testul de la finalul semestrului reflectă, "
            "în principal, nivelul de învățare acumulat de la începutul semestrului "
            "până în același moment."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce include autoeficacitatea atât convingerea de reușită, cât și "
            "capacitatea de autoregulare?"
        ),
        "options": [
            "reușita presupune planificare, monitorizare și ajustare a efortului",
            "convingerea fără strategii nu se traduce automat în performanță",
            "autoregularea este irelevantă pentru performanță",
            "autoeficacitatea exclude utilizarea strategiilor cognitive",
        ],
        "correct": "ab",
    },
    # —— Teorii clasice ale motivației (21–32) ——
    {
        "stem": (
            "Ce a accentuat Henry Murray în studiul motivației?"
        ),
        "options": [
            "perseverența în urmărirea obiectivelor",
            "efortul depus pentru satisfacerea nevoilor psihologice",
            "nevoile fiziologice de bază, fără componentă socială",
            "motivul puterii ca singur construct valid",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care nevoi sociale distincte influențează, conform lui David "
            "McClelland (1961), comportamentul în context organizațional?"
        ),
        "options": [
            "motivul realizării",
            "motivul puterii",
            "motivul afilierii",
            "motivul evitării tuturor relațiilor sociale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În teoria lui John Atkinson, conflictul motivațional central în "
            "situațiile de performanță este între:"
        ),
        "options": [
            "speranța de succes",
            "frica de eșec",
            "motivul afilierii ca singur determinant",
            "lipsa componentei emoționale în modelul descris",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce contribuie Bernard Weiner la înțelegerea motivației pentru performanță?"
        ),
        "options": [
            "teoria atribuirilor cauzale pentru succes și eșec",
            "explicarea efortului viitor pe baza cauzelor percepute",
            "identificarea celor trei mari motive sociale",
            "eliminarea rolului emoției în motivație",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Cu ce este asociat Heinz Kuhl în literatura despre motivație?"
        ),
        "options": [
            "autoconcept și reglarea motivației",
            "stiluri de coping legate de atingerea obiectivelor",
            "identificarea motivului realizării, puterii și afilierii",
            "elaborarea inventarului de motivație pentru realizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Motivația pentru performanță poate fi definită ca un conflict emoțional "
            "între tendința de apropiere a succesului și tendința de evitare a eșecului."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care pereche asociază corect teoreticianul cu ideea principală?"
        ),
        "options": [
            "McClelland — realizare, putere, afiliere",
            "Atkinson — speranță de succes versus frică de eșec",
            "Murray — doar teoria atribuirilor pentru eșec",
            "Weiner — doar motive biologice fără componentă cognitivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un elev atribuie eșecul la examen lipsei de efort și crede că poate "
            "reuși data viitoare prin studiu mai mult. Aceasta ilustrează perspectiva:"
        ),
        "options": [
            "atribuirii interne și controlabile",
            "cauze percepute ca modificabile, care susțin efortul viitor",
            "atribuirii stabile și incontrolabile, care reduce efortul",
            "motivul puterii de la McClelland, fără alte nevoi",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce caracterizează motivul realizării, în teoria lui David McClelland?"
        ),
        "options": [
            "dorința de a reuși conform standardelor personale de excelență",
            "preferința pentru sarcini cu șanse moderate de succes",
            "evitarea permanentă a oricărei evaluări",
            "respingerea oricărui obiectiv profesional",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Motivul afilierii presupune evitarea permanentă a oricărui contact "
            "social și respingerea apartenenței la grup."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce este utilă distincția între speranța de succes și frica de eșec "
            "la Atkinson?"
        ),
        "options": [
            "explică de ce unele persoane aleg sarcini ușoare sau foarte dificile",
            "ajută la înțelegerea evitării situațiilor de evaluare",
            "elimină nevoia de a lua în calcul emoția",
            "arată că toți elevii preferă aceeași dificultate a sarcinii",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Atribuirea eșecului la lipsa abilității, considerată stabilă și "
            "incontrolabilă, tinde să reducă motivația pentru încercări viitoare."
        ),
        "tf": True,
        "correct_tf": True,
    },
    # —— Modelul ceapă Schuler și AMI (33–50) ——
    {
        "stem": (
            "În modelul „ceapă” al lui Heinz Schuler despre motivația performanței, "
            "ce se află în nucleul central?"
        ),
        "options": [
            "speranța de succes",
            "frica de eșec",
            "perseverența",
            "neuroticismul ca singur element din nucleu",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care componente aparțin straturilor periferice sau de fundal în modelul "
            "ceapă al lui Schuler?"
        ),
        "options": [
            "independența și orientarea spre succes",
            "conștiinciozitatea și neuroticismul",
            "stilul de atribuire și locul controlului",
            "speranța de succes, frica de eșec și perseverența",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Stratul teoretic din modelul ceapă al lui Schuler include:"
        ),
        "options": [
            "stilul de atribuire",
            "locul controlului",
            "încrederea în sine",
            "absorbirea în sarcină ca singur element teoretic",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce caracterizează inventarul de motivație pentru realizare "
            "(Achievement Motivation Inventory)?"
        ),
        "options": [
            "170 de itemi și 17 scale",
            "evaluarea motivației pentru performanță profesională",
            "măsurarea exclusivă a coeficientului de inteligență general",
            "administrare doar la copii mici, fără versiune pentru adulți",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dimensiuni fac parte din inventarul de motivație pentru realizare?"
        ),
        "options": [
            "persistența și angajamentul",
            "siguranța succesului și flexibilitatea",
            "dorința de învățare și preferința pentru dificultate",
            "raționamentul matricial și memoria de lucru",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Ce descrie dimensiunea „internalitate” din inventarul de motivație "
            "pentru realizare?"
        ),
        "options": [
            "tendința de a atribui rezultatele propriilor acțiuni",
            "responsabilitatea percepută pentru succes sau eșec",
            "atribuirea exclusivă a rezultatelor factorilor externi",
            "lipsa legăturii între efort și rezultat",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Cum se deosebesc „orientarea spre competiție” și „orientarea spre statut” "
            "în inventarul de motivație pentru realizare?"
        ),
        "options": [
            "competiția vizează compararea cu alții și depășirea lor",
            "statutul vizează poziția socială și recunoașterea ierarhică",
            "sunt scale identice, fără diferență conceptuală",
            "ambele măsoară scorul la testul de inteligență generală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dimensiuni ale inventarului de motivație pentru realizare reflectă "
            "toleranța la risc și încrederea în fața provocărilor?"
        ),
        "options": [
            "neînfricarea",
            "siguranța succesului",
            "fixarea exclusivă pe evitarea oricărui efort",
            "lipsa orientării spre obiective",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce măsoară dimensiunea „absorbire” din inventarul de motivație "
            "pentru realizare?"
        ),
        "options": [
            "implicarea profundă și concentrarea în sarcină",
            "pierderea senzației de timp când activitatea este captivantă",
            "evitarea sarcinilor solicitante, chiar și cele relevante",
            "preferința exclusivă pentru sarcini banale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce caracterizează dimensiunea „efort compensator” din inventarul "
            "de motivație pentru realizare?"
        ),
        "options": [
            "tendința de a munci mai mult când apar obstacole",
            "compensarea deficitelor prin intensificarea efortului",
            "renunțarea imediată la orice sarcină dificilă",
            "evitarea oricărei situații care solicită perseverență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Ce măsoară inventarul de motivație pentru realizare, spre deosebire "
            "de testele de inteligență generală?"
        ),
        "options": [
            "motivația pentru performanță profesională",
            "dimensiuni precum persistența, angajamentul și orientarea spre succes",
            "aptitudinea cognitivă abstractă, fără componentă practică",
            "doar trăsura de anxietate, fără componentă de realizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dimensiuni vizează orientarea spre obiective și controlul "
            "comportamentului în inventarul de motivație pentru realizare?"
        ),
        "options": [
            "fixarea scopului",
            "autocontrolul",
            "independența",
            "coeficientul de inteligență verbal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "„Mândria performanței” și „dominanța” în inventarul de motivație pentru "
            "realizare sunt legate de:"
        ),
        "options": [
            "satisfacția derivată din realizări reușite",
            "asumarea inițiativei și influenței în context profesional",
            "evitarea oricărei situații de evaluare",
            "lipsa interesului pentru competiție sau statut",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "De ce este modelul ceapă util pentru înțelegerea motivației performanței?"
        ),
        "options": [
            "integrează componente emoționale, de personalitate și cognitive",
            "arată cum straturile superficiale se sprijină pe nucleul speranță–frică–perseverență",
            "exclude orice influență a atribuirilor sau a locului controlului",
            "suplimentează instrumentele standardizate, nu le înlocuiește",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un manager cu scor ridicat la „dorința de învățare” și „preferința "
            "pentru dificultate”, dar scor scăzut la „autocontrol”, poate avea "
            "dificultăți de follow-through. Interpretarea se bazează pe:"
        ),
        "options": [
            "profilul pe multiple dimensiuni, nu un scor unic",
            "natura multidimensională a inventarului de motivație pentru realizare",
            "identitatea perfectă între toate scalele inventarului",
            "faptul că un singur scor rezumă motivația",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Locul controlului, în stratul teoretic al modelului ceapă, se referă "
            "la gradul în care persoana percepe că rezultatele depind de propriile "
            "acțiuni versus factori externi."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care dimensiuni ale inventarului de motivație pentru realizare sunt "
            "legate de poziția în grup și de comparația cu alții?"
        ),
        "options": [
            "dominanța",
            "orientarea spre competiție",
            "orientarea spre statut",
            "secvențierea cifrelor la testul de memorie",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Integrarea perspectivei lui Bandura, a teoriei atribuirilor lui Weiner "
            "și a inventarului de motivație pentru realizare oferă:"
        ),
        "options": [
            "o imagine mai completă a motivației pentru performanță",
            "complementaritate între convingeri, atribuiri și trăsături motivaționale",
            "dovada că un singur construct explică tot comportamentul",
            "eliminarea nevoiei de evaluare a efortului sau persistenței",
        ],
        "correct": "ab",
    },
]
