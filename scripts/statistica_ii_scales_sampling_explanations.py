"""Explicații didactice — Statistică II segment 2: scale, erori, eșantionare (ID 11001–11050)."""

from __future__ import annotations

from typing import List

SCALES_SAMPLING_EXPLANATIONS: List[str] = [
    # 11001
    (
        "Adevărat. Stevens ordonează scalele după proprietăți cumulative: nominală "
        "(categorii), ordinală (+ ordine), interval (+ distanțe egale), raport (+ zero "
        "absolut). Fiecare nivel adaugă posibilități statistice, dar și restricții "
        "de interpretare."
    ),
    # 11002
    (
        "La nominală numeri câte cazuri apar în fiecare categorie (frecvențe, procente). "
        "Media codurilor arbitrare (M=1, F=2) sau raporturi „de două ori” nu au sens "
        "teoretic. Tabelul de contingență și frecvențele sunt operațiile de bază."
    ),
    # 11003
    (
        "Genul, temperamentul încadrat tipologic și religia ca apartenență sunt "
        "exemple clasice nominal-e. Celsius nu este nominal — are ordine și intervale. "
        "Trei exemple corecte ilustrează categorii fără ordine obligatorie sau fără "
        "distanțe egale."
    ),
    # 11004
    (
        "Ordinală = poți ordona (1 < 2 < 3 pe Likert), dar distanța 2→3 nu e garantat "
        "egală cu 1→2. Notele școlare sunt discutate ca ordinal. Nu poți deduce "
        "automat că patru puncte e dublu față de două puncte."
    ),
    # 11005
    (
        "Ordinala adaugă ordinea față de nominală: „mai mare / mai mic” în sensul "
        "rânduirii. Nu înseamnă automat raport sau zero absolut — acelea apar la "
        "niveluri superioare."
    ),
    # 11006
    (
        "Notele școlare sunt exemplul didactic clasic de ordinală: ordine clară, "
        "distanțe între note nu sunt neapărat egale. Timpul de reacție și numărul "
        "de răspunsuri corecte sunt de regulă raport, nu ordinal."
    ),
    # 11007
    (
        "Interval: unități egale, dar fără zero absolut (0°C nu înseamnă lipsa "
        "căldurii). Scorurile de test și QI sunt adesea tratate ca interval, cu "
        "precauție. Raportul „dublu” la Celsius este capcana tipică."
    ),
    # 11008
    (
        "Celsius permite diferențe și ordine, dar 0°C nu e absența energiei termice — "
        "de aceea 20°C nu e „de două ori mai cald” decât 10°C. Kelvin are zero "
        "absolut și raporturi fizice valide."
    ),
    # 11009
    (
        "Raport = zero absolut + raporturi (de două ori) + distanțe egale între unități. "
        "Kelvin, timpul și numărul de răspunsuri corecte sunt exemple. Likert ordinal "
        "nu are zero absolut al intensității."
    ),
    # 11010
    (
        "Patru perechi corecte: nominal-gen, ordinal-Likert, interval-scor test, "
        "raport-Kelvin/timp. Această mapare este nucleul itemilor de scale Stevens "
        "în psihologie."
    ),
    # 11011
    (
        "Fals. Likert 1–5 este de obicei tratat ordinal: ordinea e clară, dar "
        "distanțele între trepte nu sunt demonstrate ca egale. A-l folosi ca interval "
        "fără argument teoretic sau analitic este o capcană frecventă."
    ),
    # 11012
    (
        "Celsius e interval, nu raport: intervalele au sens, raportul 20/10 nu descrie "
        "o dublare fizică a căldurii. Zero Celsius e arbitrar. Kelvin rezolvă problema "
        "zero-ului absolut."
    ),
    # 11013
    (
        "Capcane: Likert ca interval fără discuție; note ca interval doar pentru că "
        "sunt cifre; gruparea QI continu în categorii ordinal/categorial. Genul M/F "
        "ca nominal este corect, nu capcană."
    ),
    # 11014
    (
        "Gruparea unui scor continuu (QI pe intervale) îl transformă în categorii "
        "ordonate sau nominale — pierzi finețea valorilor originale. Nu rămâne scară "
        "de raport continuă."
    ),
    # 11015
    (
        "Categorii bine definite: mutual exclusive (un caz, o categorie) și "
        "exhaustive (acoperă toate cazurile relevante, eventual cu „altul/necunoscut”). "
        "Suprapunerea sau golurile distorsionează analiza."
    ),
    # 11016
    (
        "Nominal și ordinal → frecvent neparametric (Mann-Whitney, chi-pătrat etc.). "
        "Interval și raport → parametric (t, ANOVA, Pearson), dacă presupunerile "
        "sunt îndeplinite. Nu aplica medie pe orice cod numeric."
    ),
    # 11017
    (
        "Parametric nu înseamnă „orice medie”, ci proceduri cu presupuneri (adesea "
        "distribuție, varianță). Neparametric nu înseamnă lipsă de ordine — Mann-Whitney "
        "folosește ranguri ordinale."
    ),
    # 11018
    (
        "Notele sunt ordinal în interpretarea strictă Stevens. În practică uneori sunt "
        "tratate ca interval — risc de supra-interpretare. Nu sunt raport sau nominal "
        "pur."
    ),
    # 11019
    (
        "Pe nominal pur nu calculezi medii de coduri sau raporturi între categorii. "
        "Frecvențele și tabelele de contingență sunt potrivite. Media pe coduri M/F "
        "este statistic lipsită de sens."
    ),
    # 11020
    (
        "Sinteză scale: ierarhie Stevens; Celsius interval vs Kelvin raport; Likert "
        "ordinal prudent; QI grupat devine categorial. Patru afirmații coerente cu "
        "cursul."
    ),
    # 11021
    (
        "Adevărat. Modelul clasic: X (observat) = T (adevărat) + E (eroare). Orice "
        "măsură psihologică include zgomot; scopul este să înțelegi cât din X reflectă "
        "constructul și cât este eroare."
    ),
    # 11022
    (
        "X este scorul înregistrat la test sau chestionar. T este nivelul „real” al "
        "trăsăturii — latent, estimat. E este componenta de eroare. Nu confunda X cu "
        "media populației."
    ),
    # 11023
    (
        "Eroarea aleatorie se definește prin fluctuația în ambele direcții în jurul "
        "valorii reale — zgomot fără direcție fixă. Compensarea pe grupuri mari și "
        "lipsa biasului constant sunt consecințe, nu definiția centrală."
    ),
    # 11024
    (
        "Eroarea sistematică tinde în aceeași direcție (ex. întrebări formulate tendențios), "
        "modifică media și echivalează cu bias. Nu se anulează automat prin mărirea "
        "eșantionului."
    ),
    # 11025
    (
        "Bias = înclinație sistematică. Eroarea sistematică trage scorurile în mod "
        "constant spre supra- sau subestimare. Nu este zgomot aleator care se anulează "
        "la N=30."
    ),
    # 11026
    (
        "Diferența esențială: aleatoria variază ± în jurul valorii reale, iar "
        "sistematica tinde constant într-o direcție. Atenuarea la agregare și "
        "alterarea mediei sunt consecințe secundare ale acestei distincții."
    ),
    # 11027
    (
        "var(X) = var(T) + var(E) arată că variabilitatea observată include și "
        "eroarea. Cu cât var(E) e mai mică față de var(T), cu atât măsura e mai "
        "fiabilă — scorurile reflectă mai fidel trăsătura."
    ),
    # 11028
    (
        "Descriptiv organizează datele din eșantionul tău: tabele, grafice, medii. "
        "Nu testează ipoteze despre populație și nu demonstrează cauzalitate. "
        "Este primul pas înainte de inferență."
    ),
    # 11029
    (
        "Descriptiv răspunde „ce arată datele?” (ex. media vârstei în eșantion). "
        "Inferențial răspunde „putem generaliza / e semnificativ?” — testează ipoteze "
        "și estimează parametri ai populației. Nu înlocuiesc unul pe altul și "
        "descriptivul nu testează ipoteze despre populație fără model."
    ),
    # 11030
    (
        "Patru exemple corecte: medie descriptivă; test de semnificație inferențial; "
        "respingerea automată a H0 nu e descriptiv; frecvența în tabelul dat e "
        "descriptiv, nu inferențială despre populație."
    ),
    # 11031
    (
        "Fals. Corelația arată asociere, nu cauză definitivă — pot interveni variabile "
        "confuze. Cauzalitatea necesită design experimental sau alte strategii "
        "puternice, nu doar corelație observată."
    ),
    # 11032
    (
        "Experimentul manipulează VI și controlează confuzorii — permite inferențe "
        "cauzale mai credibile. Observarea pasivă a asocierilor fără manipulare nu "
        "înlocuiește controlul experimental."
    ),
    # 11033
    (
        "Corelațional/observațional măsoară variabile cum sunt, fără manipulare "
        "sistematică. Poate genera ipoteze cauzale, dar nu le demonstrează definitiv. "
        "Manipularea VI este specifică experimentalului."
    ),
    # 11034
    (
        "Populația = toate unitățile relevante (ex. toți studenții unei facultăți). "
        "Eșantionul = subset studiat. Nu sunt mereu identice și populația nu înseamnă "
        "automat „toată planeta”."
    ),
    # 11035
    (
        "Reprezentativ = structura eșantionului oglindește populația țintă, ceea ce "
        "susține generalizarea. Conveniența nu garantează reprezentativitate; N mare "
        "fără selecție bună nu rezolvă biasul de selecție."
    ),
    # 11036
    (
        "Regulă orientativă din curs: N ≥ 30 eșantion „mare”, N < 30 „mic” — util "
        "pentru alegeri de teste (ex. t). Nu garantează reprezentativitate și nu "
        "interzice analiza descriptivă la N mic."
    ),
    # 11037
    (
        "Aleatoare: simplă aleatoare, stratificată multistadială, cluster unistadial — "
        "fiecare unitate sau cluster are șansă cunoscută în plan. Conveniența nu e "
        "probabilistică."
    ),
    # 11038
    (
        "Conveniența alege cazuri ușor de accesat (studenți din preajmă) — risc de "
        "bias și sub-reprezentare. Nu distribuie egal straturile populației și nu "
        "elimină eroarea de selecție."
    ),
    # 11039
    (
        "Experimental controlat → cauzalitate mai plauzibilă. Observațional → relații, "
        "nu cauză definitivă. Manipularea VI nu aparține designului pur observațional."
    ),
    # 11040
    (
        "Stratificată multistadială: straturi apoi etape; cluster unistadial: grupe "
        "selectate într-o etapă; aleatoare simplă: șansă egală; conveniența nu e "
        "metodă pentru generalizare largă."
    ),
    # 11041
    (
        "Adevărat. Reprezentativitatea înseamnă că eșantionul reflectă populația — "
        "prerequisite pentru generalizare inferențială validă, deși nu o garantează "
        "singură."
    ),
    # 11042
    (
        "Inferențial testează ipoteze despre populație pe baza eșantionului: "
        "semnificație, intervale de încredere. Nu înlocuiește descriptivul și nu "
        "dovedește teorii fără date."
    ),
    # 11043
    (
        "Kelvin și timpul = raport; religie = nominal; Likert nu e automat raport. "
        "Trei perechi corecte — a patra capcană tratează Likert ca interval/raport."
    ),
    # 11044
    (
        "Legături directe: erorile aleatorii umplu var(E); cele sistematice se "
        "manifestă ca bias. Faptul că variația observată include eroarea derivă din "
        "var(X) = var(T) + var(E), dar nu e sinonim cu perechea aleator–sistematic."
    ),
    # 11045
    (
        "Kelvin are zero absolut (0 K = oprire moleculară termică) — raporturi fizice "
        "valide. Ordinală insuficientă pentru „dublu”; interval fără zero absolut "
        "insuficient pentru raport."
    ),
    # 11046
    (
        "Număr răspunsuri corecte: zero real (0 corecte), valori întregi, raporturi "
        "interpretabile (6 vs 3 corecte). Nu e interval fără zero și nici nominal "
        "fără ordine."
    ),
    # 11047
    (
        "Trei capcane frecvente: Celsius ca raport; Likert ca interval; generalizare "
        "din conveniență. Verificarea categoriilor exhaustive e bună practică, nu "
        "capcană — de aceea nu e a patra variantă corectă aici."
    ),
    # 11048
    (
        "Temperament tipologic = categorii — nominal sau ordinal dacă există ordine "
        "teoretică între tipuri. Nu devine raport doar prin numerotare. Trăsătura "
        "continuă e alt nivel de măsură decât tipologia."
    ),
    # 11049
    (
        "N ≥ 30 vs N < 30 sunt orientări didactice pentru tipul de eșantion. Nu "
        "înlocuiesc reprezentativitatea și nu elimină erorile sistematice de "
        "măsurare."
    ),
    # 11050
    (
        "Sinteză finală segment: ierarhia Stevens; X=T+E și tipuri de eroare; "
        "descriptiv vs inferențial; experimental vs observațional. Patru piloni "
        "pentru scale, măsurare și eșantionare."
    ),
]

assert len(SCALES_SAMPLING_EXPLANATIONS) == 50
