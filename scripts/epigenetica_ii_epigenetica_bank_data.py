"""Itemi — Epigenetica II: EPIGENETICĂ (50 itemi, ID 11856–11905)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

EPIGENETICA_ITEMS: List[Item] = [
    {
        "stem": (
            "Epigenetica studiază mecanisme prin care genele sunt activate "
            "sau dezactivate fără modificarea secvenței ADN."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Epigenetica modifică ordinea bazelor din secvența ADN, "
            "similar mutațiilor clasice."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Toate celulele unui organism au același ADN, dar tipuri celulare "
            "diferite (neuron, muscular, hepatic) datorită expresiei genetice "
            "diferite, nu a unui ADN diferit."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Metilarea ADN, ca mecanism epigenetic principal, tinde să "
            "crească expresia genelor vizate."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Sindromul Prader-Willi este asociat deleției pe cromozomul 15 "
            "pe linie maternă (imprint matern)."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": "Definiția centrală a epigeneticii este:",
        "options": [
            "mecanisme de activare/dezactivare a genelor fără schimbarea secvenței ADN",
            "modificarea permanentă a secvenței ADN prin mutații punctiforme",
            "înlocuirea completă a ADN-ului nuclear cu ADN mitocondrial",
            "sinteza proteinelor fără intermediar ARNm",
        ],
        "correct": "a",
    },
    {
        "stem": "Epigenetica NU:",
        "options": [
            "schimbă secvența (ordinea bazelor) ADN",
            "reglează expresia genelor",
            "poate fi influențată de mediu",
            "implică modificări ale cromatinei",
        ],
        "correct": "a",
    },
    {
        "stem": "Epigenetica DA:",
        "options": [
            "reglează expresia genelor (activare/inactivare)",
            "schimbă secvența ADN ca o mutație clasică",
            "elimină necesitatea transcripției",
            "produce cromozomi diferiți în fiecare tip celular",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "De ce contează epigenetica pentru diferențierea celulară?"
        ),
        "options": [
            "același ADN poate fi exprimat diferit → tipuri celulare diferite",
            "fiecare tip celular are un genom complet diferit",
            "neuronii și hepatocitele au cromozomi diferiți ca număr",
            "expresia genetică este identică în toate celulele",
        ],
        "correct": "a",
    },
    {
        "stem": "Nucleozomul este format din:",
        "options": [
            "ADN înfășurat pe un octamer de histone (8 histone)",
            "ADN + 4 histone + ribozom",
            "ARNm + histone + nucleotid",
            "8 molecule de ADN fără proteine",
        ],
        "correct": "a",
    },
    {
        "stem": "Histonele sunt:",
        "options": [
            "proteine alcaline din nucleu care compactează ADN și reglează expresia",
            "baze azotate care înlocuiesc citozina în metilare",
            "enzime care copiază ADN-ul în timpul transcripției",
            "lipide de membrană care protejează cromozomii",
        ],
        "correct": "a",
    },
    {
        "stem": "Cromatina reprezintă:",
        "options": [
            "ADN + histone (nucleozomi) împachetați; protejează ADN, reglează gene",
            "doar lanțul dublu catenar de ADN fără proteine asociate",
            "totalitatea ARNm din citoplasmă",
            "structura ribozomului implicată în translație",
        ],
        "correct": "a",
    },
    {
        "stem": "Metilarea ADN implică, de regulă, adăugarea:",
        "options": [
            "grupului CH₃ (metil) pe citozină",
            "grupului fosfat pe adenină",
            "grupului acetil exclusiv pe guanină",
            "grupului hidroxil pe timină",
        ],
        "correct": "a",
    },
    {
        "stem": "Enzima asociată metilării ADN este:",
        "options": [
            "ADN-metiltransferaza (DNMT)",
            "ARN polimeraza",
            "ligaza ADN",
            "telomeraza",
        ],
        "correct": "a",
    },
    {
        "stem": "Efectul tipic al metilării ADN asupra expresiei genelor este:",
        "options": [
            "reduce sau inactivă expresia genelor",
            "crește obligatoriu transcripția genelor",
            "schimbă secvența ADN prin substituție de baze",
            "elimină necesitatea histonelor",
        ],
        "correct": "a",
    },
    {
        "stem": "Inactivarea cromozomului X la femei (XX) presupune:",
        "options": [
            "inactivarea unui cromozom X (heterocromatinizare)",
            "inactivarea ambilor cromozomi X",
            "inactivarea cromozomului Y",
            "păstrarea activi a ambilor cromozomi X funcționali",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Inactivarea cromozomului X are loc, de regulă, la femei:"
        ),
        "options": [
            "aleator, la stadiul de morulă, permanent, transmis celulelor fiice",
            "la pubertate, reversibil la fiecare ciclu menstrual",
            "la bărbați XY, pentru compensarea lipsei cromozomului X",
            "doar în celulele somatice masculine",
        ],
        "correct": "a",
    },
    {
        "stem": "Imprimarea genomică (genomic imprinting) înseamnă:",
        "options": [
            "expresia unei gene depinde de părintele de origine (matern/patern)",
            "fiecare genă e exprimată identic indiferent de părinte",
            "ștergerea completă a cromozomului 15 la naștere",
            "replicarea ADN fără histone",
        ],
        "correct": "a",
    },
    {
        "stem": "Sindromul Prader-Willi este cauzat de:",
        "options": [
            "deleție cromozom 15 pe linie paternă (imprint patern)",
            "deleție cromozom 15 pe linie maternă",
            "trisomia cromozomului 21",
            "monosomia cromozomului X",
        ],
        "correct": "a",
    },
    {
        "stem": "Sindromul Angelman este cauzat de:",
        "options": [
            "aceeași deleție cromozom 15, dar pe linie maternă",
            "deleție cromozom 15 pe linie paternă (ca Prader-Willi)",
            "duplicarea cromozomului Y",
            "translocația 14/21",
        ],
        "correct": "a",
    },
    {
        "stem": "Experimentul Agouti (șoareci) a arătat că:",
        "options": [
            "dietă cu donori de metil (acid folic, B12, colină) → metilare ↑ → fenotip mai sănătos",
            "șoarecii cu ADN identic au întotdeauna același fenotip indiferent de dietă",
            "metilarea ADN elimină complet influența dietei",
            "acidul folic reduce metilarea ADN-ului",
        ],
        "correct": "a",
    },
    {
        "stem": "Studiul Weaver et al. (2004) a evidențiat că:",
        "options": [
            "îngrijire maternă redusă → anxietate ↑; mecanism: expresia genei GR (receptor glucocorticoid)",
            "îngrijire maternă nu influențează epigenomul",
            "GR este o histonă, nu o genă reglată epigenetic",
            "metilarea ADN crește obligatoriu îngrijirea maternă",
        ],
        "correct": "a",
    },
    {
        "stem": "Dias & Ressler (2014) au raportat că:",
        "options": [
            "descendenții șoarecilor condiționați cu frică de un miros pot fi sensibili la același miros",
            "epigenetica nu poate fi transmisă între generații",
            "condiționarea olfactivă modifică secvența ADN a descendenților",
            "experiența parentală nu lasă urme epigenetice",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi afirmație–epigenetică sunt corecte?",
        "options": [
            "Epigenetica — NU schimbă secvența ADN",
            "Epigenetica — DA reglează expresia genelor",
            "Epigenetica — schimbă ordinea bazelor ADN",
            "Epigenetica — înlocuiește transcripția",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre histone și nucleozom sunt corecte?",
        "options": [
            "histonele compactează ADN și reglează expresia",
            "nucleozom = ADN + 8 histone",
            "histonele sunt baze azotate din ADN",
            "nucleozomul exclude complet proteinele",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre metilarea ADN sunt corecte?",
        "options": [
            "CH₃ pe citozină",
            "enzimă: ADN-metiltransferaza",
            "tinde să crească expresia genelor",
            "metilarea se aplică, ca regulă, pe adenină (nu citozină)",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care modificări epigenetice ale histonelor sunt enumerate în curs?",
        "options": [
            "metilare",
            "acetilare",
            "fosforilare",
            "replicare semiconservativă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre inactivarea cromozomului X sunt corecte?",
        "options": [
            "femei XX: un cromozom X inactiv",
            "aleator, la morulă, permanent",
            "bărbați XY: inactivare a cromozomului X",
            "inactivare permanentă la stadiul de morulă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care perechi sindrom–linie parentală sunt corecte?",
        "options": [
            "Prader-Willi — deleție chr 15, linie paternă",
            "Angelman — aceeași deleție chr 15, linie maternă",
            "Prader-Willi — linie maternă",
            "Angelman — linie paternă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care consecințe sunt asociate Iernii foamete olandeze (1944–45)?",
        "options": [
            "malnutriție intrauterină → la maturitate: obezitate, diabet, BCV",
            "risc crescut de schizofrenie la expuși prenatal",
            "epigenomul fetal poate fi modificat de malnutriție",
            "expunerea prenatală la hrană abundentă crește obligatoriu IQ-ul",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care factori de mediu pot modifica epigenomul?",
        "options": [
            "dietă, stres, traumă, abuz, substanțe, radiații",
            "pot modifica metilarea și fenotipul",
            "mediul acționează doar prin mutații ale secvenței ADN",
            "epigenomul rămâne identic indiferent de experiențe",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care efecte sunt asociate maltratarea/abuzul în studii epigenetice?",
        "options": [
            "modificări de metilare ADN",
            "↓ BDNF, modificări hipocampice",
            "persistente, posibil transgeneraționale",
            "creșterea obligatorie a expresiei tuturor genelor",
        ],
        "correct": "abc",
    },
    {
        "stem": "Studiul McGowan (abuz/sinucidere) a evidențiat:",
        "options": [
            "abuz în copilărie → hipermetilare",
            "↓ receptori glucocorticoizi",
            "răspuns anormal la stres",
            "↑ expresie GR prin demetilare masivă",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre gemenii monozigoți și epigenetica sunt corecte?",
        "options": [
            "ADN aproape identic",
            "cu vârsta/experiențe diferite → diferențe epigenetice și fenotipice",
            "fenotipul la MZ rămâne obligatoriu identic indiferent de mediu",
            "metilarea ADN este identică la naștere la toți gemenii MZ",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre moștenirea epigenetică sunt corecte?",
        "options": [
            "modificările epigenetice pot fi transmise transgenerațional",
            "nu doar genele, ci și pattern-uri de activare/inactivare",
            "secvența ADN se transmite transgenerațional modificată",
            "epigenomul se resetează complet la fiecare generație, fără excepții",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care elemente descriu structura cromatinei?",
        "options": [
            "ADN înfășurat pe histone",
            "nucleozom = ADN + 8 histone",
            "cromatină = nucleozomi împachetați",
            "cromatină = ARNm + ribozomi",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care mecanisme epigenetice principale sunt enumerate?",
        "options": [
            "metilarea ADN",
            "modificarea histonelor",
            "inactivarea cromozomului X",
            "transcripția ARNm → proteină",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care modificări ale histonelor schimbă accesibilitatea ADN?",
        "options": [
            "metilare, acetilare, fosforilare",
            "ubiquitinare",
            "substituția bazelor A→G în ADN",
            "toate pot influența compactarea și expresia",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații despre imprimarea genomică sunt corecte?",
        "options": [
            "expresia depinde de părintele de origine",
            "implică metilare ADN + histone",
            "Prader-Willi și Angelman: aceeași regiune chr 15, părinte diferit",
            "toate genele sunt imprimate matern și patern identic",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care experimente ilustrează mediul → epigenom?",
        "options": [
            "Iarna foametei olandeze (1944–45)",
            "Agouti (dietă → metilare → fenotip)",
            "Weaver (îngrijire maternă → GR)",
            "Watson & Crick (structura dublu helix)",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care afirmații leagă mediul de epigenom și fenotip?",
        "options": [
            "factori: dietă, stres, traumă, abuz, substanțe, radiații",
            "pot modifica metilarea ADN",
            "pot influența activarea genelor și fenotipul",
            "mediul acționează doar prin mutații ale secvenței ADN",
        ],
        "correct": "abc",
    },
    {
        "stem": "Care studii susțin epigenetica comportamentală/stres?",
        "options": [
            "Weaver et al. (2004) — GR, îngrijire maternă",
            "McGowan — abuz, hipermetilare, receptori glucocorticoizi",
            "maltratarea nu lasă urme epigenetice măsurabile",
            "Dias & Ressler — structura dublu helix ADN",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care afirmații despre gemenii MZ și mediul epigenetic sunt corecte?",
        "options": [
            "genotip aproape identic",
            "experiențe diferite → diferențe epigenetice",
            "fenotipul rămâne identic indiferent de epigenom",
            "vârsta poate accentua diferențele epigenetice",
        ],
        "correct": "ab",
    },
    {
        "stem": "Care enunțuri definesc corect epigenetica?",
        "options": [
            "activează/dezactivează gene fără schimbarea secvenței ADN",
            "reglează expresia; mediul influențează epigenomul",
            "schimbă secvența ADN ca mutația clasică",
            "fiecare tip celular are o secvență ADN diferită ca bază",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce set descrie corect structura cromatinei și rolurile?",
        "options": [
            "Histone: compactează ADN, reglează expresia",
            "Nucleozom: ADN + 8 histone",
            "Cromatină: nucleozomi împachetați; protejează ADN, reglează gene",
            "Cromatină: reglează replicarea ADN",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set cuprinde mecanismele epigenetice principale?",
        "options": [
            "Metilare ADN (CH₃ pe citozină; DNMT)",
            "Modificări histone (metilare, acetilare etc.)",
            "Inactivare cromozom X; imprimare genomică",
            "Ubiquitinare histone (modificare epigenetică)",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set leagă imprimarea genomică de sindroame?",
        "options": [
            "Prader-Willi: deleție chr 15 paternă",
            "Angelman: aceeași deleție chr 15 maternă",
            "Prader-Willi: linie maternă",
            "Angelman: deleție chr 15 paternă",
        ],
        "correct": "ab",
    },
    {
        "stem": "Ce set sintetizează experimentele epigenetice clasice?",
        "options": [
            "Foamete olandeză: epigenom prenatal → fenotip adult",
            "Agouti: dietă → metilare → culoare/sănătate",
            "Weaver: îngrijire maternă → GR → stres/anxietate",
            "Dias & Ressler: frică condiționată → sensibilitate la miros la descendenți",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set integrează mediul, epigenomul și moștenirea?",
        "options": [
            "Mediul (dietă, stres, traumă) modifică metilarea și expresia",
            "Maltratare/McGowan: modificări persistente, răspuns stres alterat",
            "Moștenire epigenetică posibil transgenerațională",
            "Dias & Ressler: sensibilitate la miros la descendenți",
        ],
        "correct": "abcd",
    },
    {
        "stem": "Ce set recapitulează PARTEA D — Epigenetica?",
        "options": [
            "Definiție: reglare expresie fără schimbare secvență ADN",
            "Cromatină: histone, nucleozom, metilare/modificări histone",
            "Mediu → epigenom; gemeni MZ; moștenire transgenerațională",
            "Imprinting: Prader-Willi (patern) / Angelman (matern), chr 15",
        ],
        "correct": "abcd",
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


SEG_DIST_50 = {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}

assert len(EPIGENETICA_ITEMS) == 50
assert _count_dist(EPIGENETICA_ITEMS) == SEG_DIST_50
