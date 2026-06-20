"""Itemi — Statistică II, segment 2: scale, erori, eșantionare (50 itemi, ID 11001–11050)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

SCALES_SAMPLING_ITEMS: List[Item] = [
    # —— 1–10: ierarhia scalelor Stevens ——
    {
        "stem": (
            "În ierarhia scalelor de măsurare Stevens, ordinea corectă este: "
            "nominală < ordinală < de interval < de raport."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "La scara nominală, operația statistică permisă în mod fundamental este:"
        ),
        "options": [
            "numărarea frecvențelor categoriilor",
            "calculul mediei aritmetice a codurilor atribuite categoriilor",
            "raportarea valorilor ca „de două ori mai mult” fără altă justificare",
            "calculul diferenței exacte între două categorii fără ordine",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele exemple sunt, de regulă, măsurători pe scară nominală?"
        ),
        "options": [
            "genul codificat M/F",
            "tipul de temperament încadrat în categorii distincte",
            "religia raportată ca apartenență la o categorie",
            "temperatura în grade Celsius comparată ca intensitate dublă",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre scara ordinală sunt corecte?"
        ),
        "options": [
            "permite ordonarea cazurilor după magnitudine",
            "nu garantează distanțe egale între treptele scalei",
            "notele școlare sunt discutate frecvent ca exemplu ordinal",
            "permite afirmația automată că 4 note este de două ori mai mult decât 2 note",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Scara ordinală se deosebește de cea nominală prin faptul că:"
        ),
        "options": [
            "introduce o relație de ordine între valori",
            "permite compararea „mai mult / mai puțin” în sensul ordinii",
            "permite orice operație algebrică ca la scara de raport",
            "elimină nevoia de a defini categoriile studiate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele exemple sunt frecvent discutate ca scale ordinale?"
        ),
        "options": [
            "note școlare (A, B, C sau 1–10, în funcție de sistem)",
            "timpul de reacție în secunde cu zecimale",
            "numărul de răspunsuri corecte la un test",
            "temperatura Kelvin ca scară de raport",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele caracterizează scara de interval?"
        ),
        "options": [
            "distanțe egale între unități pe scară",
            "lipsa unui zero absolut cu sens fizic sau natural",
            "scorurile unui test standardizat sau QI tratate frecvent ca interval",
            "posibilitatea de a spune că 20°C este dublu față de 10°C",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Temperatura în grade Celsius este un exemplu clasic de scară de interval "
            "pentru că:"
        ),
        "options": [
            "intervalele au sens egal, dar 0°C nu marchează absența totală a căldurii",
            "poți ordona valorile și calcula diferențe, dar raportul 20/10 nu are sens "
            "fizic de „dublu”",
            "este identică cu scara Kelvin la raportare proporțională",
            "este o scară nominală, pentru că folosește numere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele proprietăți aparțin scalei de raport?"
        ),
        "options": [
            "zero absolut cu sens (absența cantității măsurate)",
            "posibilitatea raporturilor (ex. de două ori mai mult)",
            "distanțe egale între unități",
            "ordine fără distanțe egale, ca la preferințe Likert",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele perechi scară–exemplu sunt corecte?"
        ),
        "options": [
            "nominală — gen M/F",
            "ordinală — preferință Likert 1–5",
            "interval — scor la un test psihologic standardizat",
            "raport — temperatura Kelvin sau timpul de reacție",
        ],
        "correct": "abcd",
    },
    # —— 11–20: capcane scale, categorii, parametric ——
    {
        "stem": (
            "Un item Likert 1–5 este, în mod obișnuit în interpretarea prudentă, "
            "o scară de interval cu zero absolut."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "De ce afirmația „20°C este de două ori mai cald decât 10°C” este o capcană?"
        ),
        "options": [
            "pentru că Celsius este scară de interval, nu de raport — raportul nu are "
            "sens fizic",
            "pentru că zero Celsius nu este absența totală a energiei termice",
            "pentru că orice diferență de 10 grade ar fi mereu proporțională la Kelvin "
            "fără conversie",
            "pentru că temperatura este întotdeauna nominală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele capcane legate de scale sunt frecvente?"
        ),
        "options": [
            "tratarea Likert 1–5 ca interval fără discuție despre distanțe egale",
            "considerarea notelor școlare ca interval doar pentru că sunt numere",
            "gruparea unui scor continuu (ex. QI 85–89 → categoria „1”) și tratarea "
            "ca ordinală/categorială",
            "recunoașterea că genul codificat M/F este nominal",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă grupezi scoruri continue de QI în intervale și le codifici 1, 2, 3…, "
            "variabila rezultată devine, de regulă:"
        ),
        "options": [
            "ordinală sau categorială, nu continuă de raport",
            "aceeași scară de raport ca scorul brut nemodificat",
            "nominală fără ordine, ca genul M/F",
            "interval cu zero absolut, pentru că intervalele sunt numerotate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Variabilele categorice bine definite trebuie să fie, în mod ideal:"
        ),
        "options": [
            "mutual exclusive — un caz într-o singură categorie",
            "exhaustive — acoperă toate posibilitățile relevante",
            "suprapuse — același caz în mai multe categorii simultan",
            "incomplete — lasă cazuri neîncadrate fără categorie reziduală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi scară–tip de statistică sunt, de regulă, "
            "asociate corect?"
        ),
        "options": [
            "nominală / ordinală — statistici neparametrice",
            "interval / raport — statistici parametrice (cu presupunerile îndeplinite)",
            "nominală — media aritmetică ca indicator central obligatoriu",
            "ordinală — raporturi de tip „de două ori mai mult” fără precizare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Statistica parametrică presupune, în general, că datele provin din scale "
            "cu proprietăți mai puternice. Care afirmații sunt corecte?"
        ),
        "options": [
            "intervalul și raportul permit multe proceduri parametrice",
            "nominala și ordinala conduc frecvent spre alternative neparametrice",
            "parametric înseamnă „cu medie” indiferent de tipul scalei",
            "neparametric înseamnă „date lipsite de ordine” în orice situație",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Notele școlare sunt, din perspectiva strictă a scalelor Stevens, discutate "
            "mai ales ca:"
        ),
        "options": [
            "ordinale — ordine fără distanțe garantat egale",
            "raport — pentru că folosesc cifre",
            "nominală — fără ordine între note",
            "interval cu zero absolut, ca timpul de reacție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele operații sunt nepotrivite pentru o scară pur "
            "nominală?"
        ),
        "options": [
            "calculul mediei codurilor numeric atribuite genului M=1, F=2",
            "raportarea „de două ori mai mult” între categorii",
            "numărarea frecvențelor și procentelor",
            "realizarea de tabele de contingență",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele descrieri despre scale și utilizarea statisticilor "
            "sunt corecte?"
        ),
        "options": [
            "ierarhia nominal < ordinal < interval < raport reflectă proprietăți "
            "cumulative",
            "Celsius: interval; Kelvin: raport",
            "Likert: de obicei ordinal, nu automat interval",
            "QI grupat pe intervale devine categorial/ordinal",
        ],
        "correct": "abcd",
    },
    # —— 21–30: erori de măsurare, descriptiv vs inferențial ——
    {
        "stem": (
            "În modelul clasic al erorii de măsurare, scorul observat se descompune "
            "în scor adevărat plus eroare: X = T + E."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În formula X = T + E, simbolul X reprezintă:"
        ),
        "options": [
            "scorul observat obținut la măsurare",
            "scorul adevărat al trăsăturii măsurate",
            "eroarea de măsurare",
            "media populației la variabila studiată",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Trăsătura centrală a erorii aleatorii de măsurare este că produce:"
        ),
        "options": [
            "variație în ambele direcții în jurul valorii reale",
            "tendința de a se compensa parțial la nivel de grup mare",
            "modificarea sistematică a mediei în aceeași direcție",
            "zgomot de măsurare care nu produce bias constant",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Eroarea sistematică de măsurare se caracterizează prin:"
        ),
        "options": [
            "aceeași direcție de abatere pentru toate măsurătorile afectate",
            "modificarea mediei observate față de valoarea adevărată",
            "echivalentul conceptului de bias",
            "anulare perfectă garantată la orice mărime de eșantion",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Sinonimul frecvent folosit pentru eroarea sistematică este:"
        ),
        "options": [
            "bias (înclinație / distorsiune sistematică)",
            "zgomot aleator care se anulează mereu după 30 de cazuri",
            "variație legitimă a constructului măsurat",
            "fiabilitate perfectă a instrumentului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Diferența esențială între eroarea aleatorie și cea sistematică este că:"
        ),
        "options": [
            "aleatoria variază ± în jurul valorii reale, iar cea sistematică tinde "
            "în aceeași direcție",
            "aleatoria se atenuează la agregare pe grupuri mari, iar cea sistematică "
            "alterează media",
            "aleatoria este mereu bias, iar cea sistematică este mereu zgomot",
            "eroarea sistematică nu afectează concluziile la nivel de medie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Relația var(X) = var(T) + var(E) este legată de interpretarea:"
        ),
        "options": [
            "fiabilității măsurării — cât din variația observată reflectă trăsătura "
            "adevărată",
            "faptului că o parte din variație provine din eroare",
            "imposibilității oricărei erori în măsurarea psihologică",
            "identității dintre scor observat și scor adevărat",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Statistica descriptivă are ca scop principal:"
        ),
        "options": [
            "organizarea și descrierea datelor colectate",
            "sintetizarea informației prin indicatori (medie, dispersie etc.)",
            "demonstrarea cauzalității fără design experimental",
            "generalizarea automată la populație fără inferență",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele distincții între statistica descriptivă și cea "
            "inferențială sunt corecte?"
        ),
        "options": [
            "descriptivă: „care sunt datele?”; inferențială: „ce putem concluziona "
            "dincolo de eșantion?”",
            "descriptivă: media vârstei din eșantion; inferențială: testarea "
            "semnificației unei diferențe",
            "inferențială: estimează parametri ai populației pe baza eșantionului",
            "descriptivă: testează ipoteze despre populație fără model",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele exemple ilustrează corect descriptiv vs "
            "inferențial?"
        ),
        "options": [
            "descriptiv: „media vârstei = 24,5 ani în eșantion”",
            "inferențial: „diferența între grupuri este semnificativă statistic?”",
            "descriptiv: „respingem H0 pentru populație cu certitudine absolută”",
            "inferențial: „frecvența genului în tabelul dat”",
        ],
        "correct": "abcd",
    },
    # —— 31–40: tipuri de studiu, populație, eșantion ——
    {
        "stem": (
            "Un studiu corelațional bine condus demonstrează, în sine, cauzalitatea "
            "dintre variabile."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Studiul experimental permite inferențe cauzale mai puternice atunci când:"
        ),
        "options": [
            "variabila independentă este manipulată sau controlată",
            "confuzorii relevanți sunt controlați",
            "se observă doar asocierea între variabile fără manipulare",
            "eșantionul este ales prin conveniență fără plan",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele descriu studiul corelațional / observațional?"
        ),
        "options": [
            "examinează relații între variabile măsurate, fără manipulare experimentală",
            "nu demonstrează definitiv cauzalitatea, deși poate sugera ipoteze",
            "manipulează sistematic VI pentru a observa efectul asupra VD",
            "exclude măsurarea simultană a mai multor variabile",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre populație și eșantion sunt "
            "corecte?"
        ),
        "options": [
            "populația = totalitatea unităților de interes pentru întrebarea de "
            "cercetare",
            "eșantionul = subset selectat din populație pentru studiu",
            "eșantionul este mereu identic cu populația",
            "populația se referă întotdeauna la toți oamenii de pe planetă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Reprezentativitatea unui eșantion înseamnă că:"
        ),
        "options": [
            "eșantionul reflectă în bună măsură caracteristicile populației țintă",
            "generalizarea la populație devine mai justificabilă",
            "eșantionul este mereu mai mare decât populația",
            "orice eșantion convenabil este automat reprezentativ",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Eșantionul mare este indicat adesea, ca regulă orientativă, prin:"
        ),
        "options": [
            "N ≥ 30",
            "eșantion mic: N < 30",
            "N ≥ 30 garantează reprezentativitate perfectă",
            "N < 30 face imposibilă orice analiză descriptivă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele metode de eșantionare sunt aleatoare (probabilistice)?"
        ),
        "options": [
            "eșantionare aleatoare globală (simplă aleatoare)",
            "eșantionare stratificată multistadială",
            "eșantionare prin clasificare unistadială (cluster unistadial)",
            "eșantionare prin conveniență (subiecți disponibili)",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Eșantionarea prin conveniență este, de regulă, mai puțin reprezentativă "
            "pentru că:"
        ),
        "options": [
            "selectează cazuri ușor accesibile, nu prin procedură aleatoare",
            "poate supra-reprezenta anumite subgrupuri",
            "asigură distribuție egală a tuturor straturilor populației",
            "elimină biasul de selecție prin definiție",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele perechi tip de studiu–inferență cauzală sunt "
            "corecte?"
        ),
        "options": [
            "experimental bine controlat — da, cu rezerve metodologice",
            "corelațional / observațional — nu definitiv pentru cauzalitate",
            "observațional — demonstrează automat manipularea VI",
            "experimental — exclude măsurarea VD",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele descrieri despre eșantionare sunt corecte?"
        ),
        "options": [
            "stratificată multistadială: straturi, apoi etape succesive de selecție",
            "clasificare unistadială: grupuri/clustere selectate într-o etapă",
            "aleatoare globală: fiecare unitate are șansă cunoscută de includere",
            "conveniență: preferată când vrei generalizare largă fără limitări",
        ],
        "correct": "abc",
    },
    # —— 41–50: sinteză scale, erori, eșantion ——
    {
        "stem": (
            "Un eșantion reprezentativ reflectă, în principiu, structura populației "
            "din care provine."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Statistica inferențială se folosește, în principal, pentru a:"
        ),
        "options": [
            "testa ipoteze și estima parametri ai populației pe baza eșantionului",
            "evalua dacă o diferență observată poate fi datorată hazardului",
            "înlocui complet descrierea datelor din eșantion",
            "garanta adevărul unei teorii fără date",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele exemple respectă tipul scalei indicat?"
        ),
        "options": [
            "Kelvin — raport (zero absolut)",
            "timp de reacție — raport",
            "religie — nominală",
            "Likert 1–5 — automat raport cu zero absolut",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care dintre următoarele legături directe între tipul erorii și efectul "
            "său asupra măsurării sunt corecte?"
        ),
        "options": [
            "erori aleatorii contribuie la var(E)",
            "erori sistematice produc bias",
            "variația observată include și componenta de eroare",
            "bias aleator se anulează prin definire la orice N",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Temperatura Kelvin este exemplu de scară de raport pentru că:"
        ),
        "options": [
            "zero Kelvin marchează absența mișcării termice moleculare",
            "raporturile între valori au sens fizic",
            "este ordinală, deoarece poate fi ordonată",
            "nu permite compararea intervalelor egale",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Numărul de răspunsuri corecte la un test este, de regulă, pe scară de:"
        ),
        "options": [
            "raport — zero real (niciun răspuns corect) și raporturi interpretabile",
            "interval — fără zero absolut",
            "nominală — fără ordine",
            "ordinală — fără distanțe între valori",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele capcane privind scalele și eșantionarea trebuie "
            "avute în vedere?"
        ),
        "options": [
            "confundarea intervalului cu raportul la temperatură",
            "tratarea Likert ca interval fără argument",
            "generalizare largă din eșantion de conveniență",
            "verificarea exhaustivității categoriilor la variabile categoriale",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Temperamentul încadrat în tipuri discrete (ex. categorii clinice sau "
            "tipologice) este tratat, de regulă, ca variabilă:"
        ),
        "options": [
            "nominală sau ordinală, în funcție de cum sunt definite categoriile",
            "de raport, pentru că tipurile pot fi numerotate",
            "continuă, pentru că trăsătura există în grade",
            "de interval cu zero absolut",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care dintre următoarele afirmații despre eșantion mare vs mic sunt "
            "corecte?"
        ),
        "options": [
            "N ≥ 30 este o orientare frecventă pentru „eșantion mare”",
            "sub N = 30 se vorbește adesea de eșantion mic",
            "mărimea eșantionului înlocuiește reprezentativitatea",
            "N mare elimină erorile sistematice de măsurare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele sintezează corect modulele scale–erori–eșantion?"
        ),
        "options": [
            "scale Stevens: nominal < ordinal < interval < raport",
            "X = T + E; aleator vs sistematic (bias)",
            "descriptiv descrie; inferențial testează și generalizează cu prudență",
            "experimental → cauzalitate mai credibilă; corelațional → relații, nu "
            "cauză definitivă",
        ],
        "correct": "abcd",
    },
]

assert len(SCALES_SAMPLING_ITEMS) == 50
