"""Explicații pedagogice — JVIS (60 itemi)."""

from __future__ import annotations

from typing import List

JVIS_EXPLANATIONS: List[str] = [
    # 1–10 General
    (
        "Inventarul de interese vocaționale Jackson (JVIS) măsoară interesele vocaționale "
        "și sprijină consilierea vocațională — nu este un test de aptitudine "
        "sau de psihopatologie."
    ),
    (
        "Forma standard: 289 perechi de afirmații, 34 scale, câte 17 itemi pe "
        "scală. Subiectul alege preferința între afirmații din fiecare pereche."
    ),
    (
        "26 scale măsoară roluri profesionale (domenii/ocupații), 8 scale măsoară "
        "stiluri de muncă (mod preferat de lucru) — distincție structurală "
        "importantă la interpretare."
    ),
    (
        "Adaptarea românească pe N≈3500 permite compararea scorurilor cu norme "
        "locale — esențială pentru interpretare validă în practică."
    ),
    (
        "JVIS poate fi administrat individual sau colectiv — flexibilitate utilă "
        "în școli, centre de consiliere sau recrutare."
    ),
    (
        "Spre deosebire de testele de aptitudine, JVIS măsoară preferințe și "
        "orientări vocaționale — ce vrei să faci, nu doar ce poți face."
    ),
    (
        "Fiecare scală are 17 itemi în format perechi forțate — design care "
        "reduce răspunsurile socialmente dorite și clarifică preferințele."
    ),
    (
        "Fals: JVIS include atât roluri profesionale (26 scale), cât și stiluri "
        "de muncă (8 scale) — nu măsoară doar stiluri."
    ),
    (
        "Normele românești transformă scorurile brute în comparații cu populația "
        "locală — fără ele, interpretarea T ar fi invalidă în context românesc."
    ),
    (
        "În consiliere, JVIS structurează discuția și oferă profil ocupațional "
        "multidimensional — nu înlocuiește interviul, îl completează."
    ),
    # 11–20 Concepte și teme
    (
        "Profilul ocupațional = configurația scorurilor pe dimensiunile "
        "fundamentale ale intereselor — imaginea preferințelor vocaționale "
        "a persoanei."
    ),
    (
        "Rolul de muncă = domeniu sau ocupație concretă (Drept, Științe fizice). "
        "Stilul de muncă = mod preferat de lucru (planificare, independență)."
    ),
    (
        "Stilurile de muncă sunt transversale — se aplică în mai multe domenii. "
        "Rolurile sunt legate de conținutul ocupațional specific."
    ),
    (
        "Scalele JVIS sunt construite să măsoare conceptul din nume și să fie "
        "relativ necorelate — pentru a diferenția dimensiuni distincte."
    ),
    (
        "Cele 10 teme Holland extinse includ: expresiv, logic, curios, practic, "
        "asertiv, socializat, orientat spre ajutorare, convențional, "
        "întreprinzător, comunicativ."
    ),
    (
        "Temele acoperă spectrul vocațional de la creativitate și știință la "
        "social, afaceri și comunicare — cadru teoretic extins față de RIASEC "
        "clasic."
    ),
    (
        "Rolul = ce domeniu te atrage; stilul = cum preferi să lucrezi în "
        "acel domeniu sau în general — două niveluri de analiză."
    ),
    (
        "Orientat spre ajutorare = preferință pentru sprijin, consiliere, "
        "asistență — legat de scale sociale, medicale, educaționale."
    ),
    (
        "Fals: designul JVIS urmărește corelări reduse între scale — nu "
        "corelare maximă — pentru a diferenția interesele."
    ),
    (
        "Drept = rol de muncă; Planificare = stil de muncă. Inversarea "
        "arată confuzia frecventă între cele două tipuri de scale."
    ),
    # 21–30 Familii de scale și interpretare profil
    (
        "Scalele de arte și expresiv din JVIS indică interes pentru creativitate, "
        "estetică sau performanță — nu pentru laborator sau birocrație."
    ),
    (
        "Familiile știință/matematică acoperă domenii investigative, analitice "
        "și tehnice — nucleul interesului pentru cercetare și rezolvare de probleme."
    ),
    (
        "Scalele outdoor reflectă preferința pentru activități practice în aer "
        "liber — natură, mișcare, lucru fizic în mediu natural."
    ),
    (
        "JVIS distinge familii tematice: servicii administrative, sănătate/medical "
        "și afaceri/management — fiecare cu profil de activitate distinct."
    ),
    (
        "Stilurile interpersonale la job (relacionare, cooperare) se deosebesc de "
        "scalele de predare și social (educație, formare, domenii sociale)."
    ),
    (
        "Scalele juridice măsoară interesul pentru drept, legislație și cariere "
        "legale — nu outdoor, planificare sau medicină."
    ),
    (
        "Scalele academice = cercetare și învățământ superior. Stilurile de "
        "activitate = preferințe transversale (independență, planificare etc.), "
        "nu domenii ocupaționale concrete."
    ),
    (
        "Stilurile de activitate la muncă din JVIS: independență, planificare și "
        "încredere interpersonală — preferințe aplicabile în mai multe domenii."
    ),
    (
        "Profil ridicat la știință/matematică + academic sugerează orientare "
        "spre facultăți analitice, cercetare sau universitate — profil coerent."
    ),
    (
        "Familia afacerilor acoperă management, vânzări, antreprenoriat și "
        "activități comerciale — nu artă sau laborator izolat."
    ),
    # 31–40 Fidelitate profil
    (
        "≥10 răspunsuri nescorabile → profilul nu se calculează — protecție "
        "împotriva interpretării datelor incomplete sau nevalide."
    ),
    (
        "Consistență <0,50 → interpretare cu precauție — posibile răspunsuri "
        "contradictorii, neatenție sau lipsă de implicare."
    ),
    (
        "Infrecvența măsoară răspunsuri „da” neobișnuit de frecvente — acceptare "
        "excesivă a afirmațiilor atipice pentru populație."
    ),
    (
        "Invalidare: ambele anormale (consistență ȘI infrecvență) → profil "
        "invalid — nu se interpretează ca vocațional valid."
    ),
    (
        "12 nescorabile depășesc pragul de 10 → readministrare sau clarificare "
        "instrucțiuni, nu interpretare de profil."
    ),
    (
        "0,42 < 0,50 → sub pragul de consistență — interpretare rezervată, "
        "verificare suplimentară recomandată."
    ),
    (
        "Infrecvență ridicată = prea multe „da” atipice — distorsionează "
        "profilul prin acceptare indiscriminată."
    ),
    (
        "Trei indici administrativi: nescorabile, consistență, infrecvență — "
        "verificați înainte de orice interpretare a scorurilor T."
    ),
    (
        "Validitatea profilului protejează împotriva răspunsurilor aleatorii "
        "sau neatenționate — altfel recomandările vocaționale sunt riscante."
    ),
    (
        "Fals: infrecvență extremă poate invalida profilul chiar dacă consistența "
        "e normală — ambele indici se evaluează împreună la invalidare."
    ),
    # 41–50 Aplicare și distorsiuni
    (
        "JVIS se aplică în orientare școlară/universitară, consiliere vocațională, "
        "recrutare și cercetare în psihologia muncii — utilizare largă."
    ),
    (
        "În recrutare, JVIS evaluează potrivirea interes–post și completează "
        "interviul — nu înlocuiește proba practică."
    ),
    (
        "Fake good: desirabilitate socială, profil plat, multe T>70 — persoana "
        "încearcă să pară ideală pe toate dimensiunile."
    ),
    (
        "Fake bad: prezentare negativă exagerată, scoruri foarte scăzute — "
        "opusul fake good, tot distorsiune self-report."
    ),
    (
        "Răspuns aleatoriu: pattern bizar, timp prea scurt, scale contradictorii "
        "— semne de neatenție sau completare fără implicare."
    ),
    (
        "Distorsiunile self-report pot masca interesele reale — de aceea "
        "se coroborează cu interviul și indicii de validitate."
    ),
    (
        "Profil plat (toate scalele ~50) poate indica fake good sau lipsă de "
        "diferențiere — nu un profil vocațional informativ."
    ),
    (
        "Consilierul coroborează datele cu interviul și verifică validitatea "
        "administrativă — nu interpretează orb scorurile."
    ),
    (
        "La orientarea universitară, JVIS identifică domenii compatibile cu "
        "interesele — completează notele școlare cu preferințe vocaționale."
    ),
    (
        "Scale contradictorii fără logică = semn de răspuns neatenționat sau "
        "aleatoriu, nu profil vocațional coerent."
    ),
    # 51–60 Scoruri T și pași interpretare
    (
        "T 40–60 = mediu (±1σ), ~68% populație — zona obișnuită, fără deviație "
        "semnificativă."
    ),
    (
        "T 60–70 sau 30–40 = înalt/scăzut (±1–2σ), ~14% populație per capăt — "
        "merită atenție la interpretare."
    ),
    (
        "T >70 sau <30 = extrem (±2σ), ~2% populație — necesită atenție specială; "
        "poate indica interes foarte puternic sau foarte slab."
    ),
    (
        "Pasul 1 = validitatea profilului (nescorabile, consistență, infrecvență) "
        "— fără validitate, restul pașilor nu are sens."
    ),
    (
        "Ordinea: validitate → scoruri relevante → grupări → pattern → concluzii. "
        "Nu se emit recomandări înainte de verificarea validității."
    ),
    (
        "Pasul 2 = găsești scalele cu T înalt sau scăzut față de medie — "
        "acolo unde interesul sau dezinteresul e semnificativ."
    ),
    (
        "Pasul 3 = grupări de scale în familii tematice (arte, știință, afaceri, "
        "stiluri) — literele A–K sunt doar coduri pentru aceste familii."
    ),
    (
        "Pasul 4 = după validitate, scoruri și grupări, analizezi cum arată "
        "împreună scalele: profil coerent sau combinații contradictorii "
        "(ex. știință foarte ridicată + outdoor foarte ridicat — de verificat "
        "în discuție cu clientul)."
    ),
    (
        "Pasul 5 = concluzii și recomandări practice — sinteza pentru client, "
        "după toți pașii anteriori."
    ),
    (
        "T=72 la știință și T=28 la convențional, după validare: interes extrem "
        "analitic și dezinteres pentru birocrație — profil diferențiat clar."
    ),
]
