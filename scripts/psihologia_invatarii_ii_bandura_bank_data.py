"""Itemi Bandura — teoria social-cognitivă (40 itemi, ID 10551–10590)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

BANDURA_ITEMS: List[Item] = [
    # —— 1–8: învățare prin observare, determinism reciproc ——
    {
        "stem": (
            "Conform teoriei social-cognitive a lui Albert Bandura, învățarea poate "
            "avea loc prin observarea și imitarea altora, nu doar prin întărire directă "
            "a propriului comportament."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare surprinde cel mai bine ideea centrală a învățării "
            "observaționale în teoria lui Bandura?"
        ),
        "options": [
            "comportamentele noi pot fi dobândite urmărind modele și imitându-le",
            "orice învățare necesită recompensă imediată după fiecare răspuns propriu",
            "imitarea necesită prezența fizică continuă a modelului în același spațiu",
            "observarea înlocuiește nevoia de practică și feedback individual",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între Bandura și behaviorismul strict skinnerian "
            "sunt corecte?"
        ),
        "options": [
            "Bandura: învățare prin observare și modelare, nu doar consecințe proprii",
            "Bandura: procese cognitive (atenție, reprezentare) mediează învățarea",
            "Bandura: minimizează influența mediului social asupra învățării",
            "Skinner și Bandura: amândoi negă imitația ca mecanism de învățare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Determinismul reciproc în teoria lui Bandura înseamnă că "
            "comportamentul, mediul și factorii personali se influențează reciproc."
        ),
        "options": [
            "adevărat — niciun factor nu acționează unilateral asupra celorlalți",
            "fals — doar mediul determină comportamentul, ca la Watson",
            "adevărat — determinismul reciproc e documentat la copii, nu la adulți",
            "fals — personalitatea este fixă și nu modifică mediul",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei componente intră în determinismul reciproc bandurian?"
        ),
        "options": [
            "comportamentul (acțiunile observabile ale persoanei)",
            "mediul (contextul social și fizic, inclusiv reacțiile altora)",
            "factorii personali (cogniții, așteptări, autoeficacitate, emoții)",
            "doar impulsurile biologice și reflexele necondiționate pavloviene",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care trei exemple ilustrează cum comportamentul influențează mediul "
            "în cadrul determinismului reciproc?"
        ),
        "options": [
            "un elev participă mai mult și schimbă atmosfera clasei",
            "un copil agresiv provoacă reacții de la colegi și adulți",
            "alegerile unei persoane modifică oportunitățile din jurul ei",
            "mediul acționează întotdeauna înaintea comportamentului, fără feedback invers",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În determinismul reciproc, „factorii personali” includ în special:"
        ),
        "options": [
            "cognițiile, așteptările, credințele despre sine (ex. autoeficacitate)",
            "doar trăsăturile ereditare fixe, fără influență a experienței",
            "consecințele imediate ale ultimului răspuns, ca la Skinner",
            "reflexele fiziologice necondiționate, ca la Pavlov",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Determinismul reciproc se deosebește de determinismul unidirecțional "
            "prin faptul că:"
        ),
        "options": [
            "persoana nu este doar produs pasiv al mediului — îl și modelează",
            "comportamentul, mediul și cogniția se influențează reciproc",
            "doar genetica decide comportamentul, mediul e irelevant",
            "imitarea înlocuiește gândirea și planificarea în teoria social-cognitivă",
        ],
        "correct": "ab",
    },
    # —— 9–16: experimentul Bobo doll ——
    {
        "stem": (
            "În experimentul cu păpușa Bobo, copiii expuși unui model agresiv au imitat "
            "mai frecvent comportamente agresive față de copiii din grupurile de control."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Concluzia principală a experimentului Bobo doll este că:"
        ),
        "options": [
            "expunerea la un model agresiv crește imitarea comportamentului agresiv",
            "agresivitatea la copii apare doar din pedepse corporale directe",
            "copiii nu pot învăța comportamente noi fără recompensă imediată personală",
            "modelele filmate produc imitație mai slabă decât cele live, indiferent de context",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei tipuri de model pot produce învățare observațională, "
            "conform cercetărilor lui Bandura?"
        ),
        "options": [
            "model adult real (prezent fizic)",
            "model filmat sau înregistrat (mediat)",
            "model simbolic (personaje, povești, figuri din media)",
            "doar model verbal abstract, fără exemplu concret de comportament",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două idei despre modelarea prin media (film, înregistrare) sunt "
            "susținute de teoria social-cognitivă?"
        ),
        "options": [
            "comportamentele pot fi învățate și din modele mediate, nu doar live",
            "expunerea repetată la modele agresive în media poate modela comportament",
            "doar modelul fizic prezent produce imitație — media e complet inertă",
            "imitarea din media necesită recompensă materială imediată pentru observator",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "În experimentul Bobo, imitația a apărut și atunci când copiii nu au "
            "primit recompensă directă pentru propriul comportament agresiv. "
            "Acest rezultat sugerează:"
        ),
        "options": [
            "învățarea observațională nu depinde exclusiv de întărirea proprie imediată",
            "copiii pot imita comportamente văzute la model fără recompensă personală instantanee",
            "copiii imită comportamentele modelelor similare vârstei, indiferent de context",
            "condiționarea clasică explică singură tot experimentul Bobo",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Întărirea vicariantă (observarea consecințelor modelului) poate influența "
            "dacă un comportament observat va fi imitat, deoarece:"
        ),
        "options": [
            "persoana învață ce se întâmplă când modelul este recompensat sau pedepsit",
            "imitarea devine mai probabilă când modelul pare să obțină rezultate pozitive",
            "întărirea vicariantă înlocuiește complet cele patru procese ale modelării",
            "doar pedeapsa modelului crește imitarea — recompensa o inhibă mereu",
        ],
        "correct": "a",
    },
    # —— 17–24: cele patru procese ale modelării ——
    {
        "stem": (
            "Primul proces necesar pentru învățarea observațională în schema lui "
            "Bandura este atenția — persoana trebuie să observe caracteristicile "
            "relevante ale modelului."
        ),
        "options": [
            "adevărat — fără atenție, modelul nu este procesat",
            "fals — retenția precede întotdeauna atenția",
            "adevărat — atenția e automată la copii, fără selecție a informației relevante",
            "fals — motivația este primul pas, înaintea atenției",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două factori influențează dacă modelul captează atenția observatorului?"
        ),
        "options": [
            "caracteristicile modelului (status, similaritate, atractivitate)",
            "complexitatea și claritatea comportamentului observat",
            "doar vârsta biologică — atenția e fixă genetic",
            "similaritatea sau statusul modelului nu influențează atenția observatorului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Procesul de retenție (memorie) în modelare presupune că comportamentul "
            "observat este păstrat sub formă de:"
        ),
        "options": [
            "reprezentări mentale — imagini, simboluri, descrieri verbale",
            "doar modificări reflexe permanente, fără reprezentare cognitivă",
            "întărire operantă directă asupra observatorului, ca la Skinner",
            "uitare imediată dacă nu există recompensă în aceeași secundă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei modalități de reținere a comportamentului modelului sunt "
            "menționate în teoria social-cognitivă?"
        ),
        "options": [
            "imagini mentale ale acțiunilor modelului",
            "simboluri și coduri cognitive",
            "verbalizare — descrierea în cuvinte a comportamentului",
            "doar condiționare clasică a reflexelor, fără reprezentare",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două condiții sunt necesare pentru procesul de reproducere "
            "(imitare) a comportamentului observat?"
        ),
        "options": [
            "capacitatea motorie și cognitivă de a executa acțiunea",
            "practică sau încercări repetate pentru rafinarea comportamentului",
            "prezența permanentă a modelului în același spațiu fizic",
            "reproducerea reușește fără etapa de retenție mentală a comportamentului",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Procesul de motivație în modelare determină dacă comportamentul reținut "
            "va fi efectiv realizat. Aceasta depinde în special de:"
        ),
        "options": [
            "valoarea percepută, recompensele anticipate și scopurile personale",
            "doar de reflexele necondiționate ale observatorului",
            "pedeapsa imediată, indiferent de expectanțe sau valoare percepută",
            "motivația depinde de reflexe, nu de așteptări sau recompense anticipate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care patru procese trebuie să aibă loc, în ordinea logică a modelării "
            "banduriene, pentru ca învățarea observațională să se traducă în comportament?"
        ),
        "options": [
            "atenție — observarea caracteristicilor relevante ale modelului",
            "retenție — păstrarea comportamentului în memorie (imagini, simboluri, verbal)",
            "reproducere — capacitatea de a executa comportamentul imitat",
            "motivație — motive și consecințe anticipate care determină acțiunea",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Un elev urmărește o demonstrație la tablă, o reține mental, dar nu încearcă "
            "să rezolve singur exercițiul pentru că crede că „oricum nu i-ar ieși”. "
            "Care procese sunt blocate în principal?"
        ),
        "options": [
            "motivația — lipsa credinței că acțiunea merită sau poate reuși",
            "autoeficacitatea scăzută — credința redusă în propria capacitate de reușită",
            "atenția — elevul nu a privit demonstrația",
            "retenția — informația nu a fost stocată deloc în memorie",
        ],
        "correct": "ab",
    },
  # —— 25–32: efecte ale expunerii la model ——
    {
        "stem": (
            "Efectul de modelare (achiziție) presupune că expunerea la model poate "
            "introduce comportamente noi. Aceasta înseamnă:"
        ),
        "options": [
            "observatorul poate manifesta acțiuni pe care nu le făcea înainte de expunere",
            "repertoriul comportamental se extinde prin observare, nu doar prin întărire directă",
            "modelarea modifică frecvența comportamentelor existente, fără apariție de unele noi",
            "modelarea necesită recompensă imediată pentru observator, ca la Skinner",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei consecințe pot apărea din expunerea la un model pedepsit pentru "
            "un comportament?"
        ),
        "options": [
            "efect inhibitor — scade frecvența comportamentului la observator",
            "copilul evită comportamentul după ce vede consecințe negative pentru model",
            "frecvența comportamentului crește mereu, indiferent de pedeapsa modelului",
            "modelarea produce inhibiție doar la comportamente motorii complet noi",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care patru efecte sau procese sunt centrale în teoria social-cognitivă "
            "a expunerii la model?"
        ),
        "options": [
            "achiziție/modelare — apar comportamente noi",
            "inhibiție — scade frecvența unui comportament observat pedepsit la model",
            "dezinhibiție — crește frecvența unui comportament interzis dar observat",
            "provocare (elicitation) — stimulul modelului declanșează răspunsul",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Efectul de provocare (elicitation) apare atunci când:"
        ),
        "options": [
            "un stimul asociat modelului declanșează un răspuns deja învățat",
            "modelul prezintă un comportament motor complet nou, neasociat stimulului",
            "observatorul uită comportamentul imediat după expunere",
            "doar pedeapsa directă produce răspunsul observatorului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un copil vede la televizor un personaj care fură fără consecințe vizibile "
            "și devine mai dispus să încerce comportamente similare, deși știa că sunt "
            "interzise. Acest fenomen ilustrează:"
        ),
        "options": [
            "dezinhibiție prin modelare — modelul reduce inhibiția comportamentului",
            "modelare prin media — comportamente învățate din modele mediate",
            "extincție operantă — comportamentul dispare prin lipsa recompensei",
            "condiționare clasică — asociere stimul neutru cu reflex",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Dacă un profesor modelează calm în conflict, iar elevii devin mai puțin "
            "agresivi în pauză fără a copia gesturile exacte, poate fi vorba despre:"
        ),
        "options": [
            "influență prin modelare asupra tiparelor de comportament existente",
            "modificarea frecvenței unor comportamente deja posibile, nu neapărat copiere exactă",
            "învățare observațională care nu necesită imitație motorie identică",
            "doar achiziție de comportamente motorii noi, identice cu modelul",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Persuasiunea verbală (încurajarea de la alții) ca sursă a autoeficacității "
            "este mai eficientă când:"
        ),
        "options": [
            "mesajul este credibil și susținut de competența reală a persoanei",
            "persoana are deja indicii de succes, nu doar laude goale",
            "vine de la cineva considerat competent în domeniul respectiv",
            "înlocuiește complet nevoia de experiențe directe de reușită",
        ],
        "correct": "abc",
    },
    # —— 33–40: autoeficacitate ——
    {
        "stem": (
            "Autoeficacitatea este credința persoanei că poate organiza și executa "
            "acțiunile necesare pentru a obține un anumit rezultat — nu este același "
            "lucru cu stima de sine."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care formulare definește corect autoeficacitatea în teoria lui Bandura?"
        ),
        "options": [
            "credința că pot realiza acțiunile necesare pentru succes la o sarcină",
            "evaluarea globală a valorii proprii ca persoană (stima de sine)",
            "certitudinea că voi obține succesul, indiferent de pregătire",
            "aptitudinea genetică fixă, nemodificabilă prin experiență",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între autoeficacitate și alte construcții sunt corecte?"
        ),
        "options": [
            "autoeficacitate = credință despre capacitatea de acțiune; stima de sine = "
            "evaluare globală a sinelui",
            "autoeficacitate este specifică domeniului/sarcinii, nu o etichetă generală",
            "autoeficacitate și stima de sine sunt mereu identice ca măsură",
            "autoeficacitatea înseamnă doar rezultatul final, nu credința în propria acțiune",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei surse ale autoeficacității sunt formulate de Bandura?"
        ),
        "options": [
            "experiențe de performanță anterioară (mastery) — reușite directe",
            "experiențe vicariante — observarea altora care reușesc (modelare)",
            "persuasiune verbală — încurajare credibilă din partea altora",
            "doar moștenirea genetică, fără influență a experienței sau a modelării",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două afirmații despre experiențele de performanță (mastery) ca sursă "
            "a autoeficacității sunt corecte?"
        ),
        "options": [
            "sunt considerată cea mai puternică sursă a autoeficacității",
            "reușitele proprii consolidate cresc credința în capacitatea de acțiune",
            "o singură eșec minor anulează permanent orice autoeficacitate",
            "performanțele anterioare nu contează dacă există modelare vicariantă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care este a patra sursă a autoeficacității în teoria lui Bandura, "
            "alături de performanțe anterioare, modelare și persuasiune verbală?"
        ),
        "options": [
            "stări fiziologice și emoționale interpretate ca semnale despre capacitate",
            "analiza viselor și a refulării inconștiente",
            "reflexele necondiționate pavloviene",
            "moștenirea genetică ca singur factor determinant",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două consecințe sunt asociate cu autoeficacitate ridicată?"
        ),
        "options": [
            "motivație mai mare și perseverență în fața dificultăților",
            "sarcinile dificile sunt interpretate ca provocări, nu ca amenințări",
            "evitarea sistematică a oricărei sarcini noi",
            "atribuirea eșecului mereu factorilor externi, fără încercare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei consecințe sunt tipice pentru autoeficacitate scăzută?"
        ),
        "options": [
            "evitarea sarcinilor și renunțare prematură",
            "anxietate ridicată și interpretarea dificultăților ca amenințări",
            "tendința de a atribui eșecul propriei incapacități",
            "perseverență crescută și căutarea activă a provocărilor",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Așteptarea rezultatului (outcome expectation) se deosebește de autoeficacitate "
            "prin faptul că:"
        ),
        "options": [
            "autoeficacitatea vizează credința în propria capacitate de acțiune",
            "așteptarea rezultatului vizează ce se va întâmpla dacă acționezi, nu dacă poți acționa",
            "cele două construcții sunt identice în teoria lui Bandura",
            "autoeficacitatea se referă doar la stimă de sine globală, nu la sarcini",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Efectul de dezinhibiție în modelare apare atunci când observarea unui model "
            "care manifestă un comportament interzis, fără consecințe negative vizibile, "
            "crește probabilitatea acelui comportament la observator."
        ),
        "options": [
            "adevărat — modelul reduce inhibiția internă față de comportamentul interzis",
            "fals — modelarea scade mereu frecvența comportamentelor interzise",
            "adevărat — dezinhibiția apare la modele live, nu la cele din media",
            "fals — dezinhibiția presupune apariția unor comportamente complet noi",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Teoria social-cognitivă a lui Bandura integrează învățarea observațională, "
            "procesele cognitive și influența reciprocă între persoană, comportament "
            "și mediu — depășind behaviorismul strict fără a neglija rolul social."
        ),
        "tf": True,
        "correct_tf": True,
    },
]

assert len(BANDURA_ITEMS) == 40
