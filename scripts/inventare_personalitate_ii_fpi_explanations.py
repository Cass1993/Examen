"""Explicații — Inventare de personalitate II: FPI Freiburg (ID 11566–11615)."""

from __future__ import annotations

from typing import List

FPI_EXPLANATIONS: List[str] = [
    # 11566
    (
        "Adevărat. FPI (Freiburger Persönlichkeitsinventar) a fost creat de "
        "Fahrenberg, Selg și Hampel (1970) — instrument german cu utilizare "
        "internațională extinsă."
    ),
    # 11567
    (
        "Adevărat. FPI folosește format clasic Da/Nu (Adevărat/Fals) — afirmații "
        "despre sine, ca multe inventare de personalitate."
    ),
    # 11568
    (
        "Adevărat. FPI-R: 138 itemi scorabili + 1 item de practică la început "
        "care familiarizează respondentul și nu intră în calculul scorurilor."
    ),
    # 11569
    (
        "Adevărat. Normele FPI arată diferențe semnificative după vârstă — "
        "tinerii tind să obțină scoruri mai ridicate pe multe scale decât "
        "vârstnicii."
    ),
    # 11570
    (
        "Fals. FPI este inventar standardizat, obiectiv, cu scale numerice și "
        "barem de scorare — nu test proiectiv nestandardizat."
    ),
    # 11571
    (
        "Autori FPI: Fahrenberg, Selg, Hampel. Eysenck = EPQ; Gough = CPI; "
        "Cattell = 16PF."
    ),
    # 11572
    (
        "Familia FPI: FPI-G (clasic), FPI-A/B/K (forme derivate), FPI-R "
        "(revizuit, versiunea actuală preferată). EPQ/CPI/MMPI = alte "
        "instrumente."
    ),
    # 11573
    (
        "FPI-G (versiunea lungă clasică): ~30–40 minute. FPI-R e mai scurt "
        "(10–30 min) datorită revizuirii itemilor."
    ),
    # 11574
    (
        "FPI-R: 10–30 minute — versiune revizuită, mai eficientă temporal. "
        "FPI-G necesită mai mult timp (~30–40 min)."
    ),
    # 11575
    (
        "Vârste: de la 13–14 ani, cu nivel intelectual cel puțin mediu. Nu e "
        "limitat la adulți sau populație activă."
    ),
    # 11576
    (
        "FPI-R conține 138 itemi care intră în scorare. 100 = EPQ-R; 63 = IVE; "
        "480 ≈ MMPI."
    ),
    # 11577
    (
        "Itemul de practică familiarizează cu formatul Da/Nu și nu este scorat. "
        "Nu invalidează profilul și nu măsoară extraversiune."
    ),
    # 11578
    (
        "Scalele Sat–PSan (primele 9) au câte ~12 itemi. Sinc, Extrav și Emo au "
        "câte ~14 itemi."
    ),
    # 11579
    (
        "Sinc (Sinceritate/validitate): 14 itemi — evaluare deschidere vs. "
        "impresionare favorabilă. Scalele 1–9 au câte 12 itemi."
    ),
    # 11580
    (
        "Extrav și Emo (scale globale FPI-R): câte 14 itemi fiecare. Sat–PSan "
        "au câte 12 itemi."
    ),
    # 11581
    (
        "FPI-G clasic: 9 scale (Nervozitate, Agresivitate, Depresie, "
        "Excitabilitate, Sociabilitate, Calm, Dominare, Inhibiție, Sinceritate) "
        "+ E, N, M. Sat/Real/Solic sunt scale FPI-R."
    ),
    # 11582
    (
        "Sat ↑: optimist, mulțumit de viață. Sat ↓: pesimist, depresiv. Nu "
        "agresivitate (Agres) sau somatizare (AcSom)."
    ),
    # 11583
    (
        "Inh ↑: timid, evită situații sociale, inhibat. Inh ↓: dezinhibat, "
        "sigur social. Nu impulsivitate (Exci) sau ambiție (Real)."
    ),
    # 11584
    (
        "AcSom ↑: plângeri somatice, acuze corporale frecvente. Diferit de "
        "PSan (teamă de boală) sau Sat (satisfacție)."
    ),
    # 11585
    (
        "PSan ↑: teamă de boală, preocupare ipohondră. AcSom = plângeri "
        "somatice; Solic = stres/solicitare."
    ),
    # 11586
    (
        "Norme RO: N = 2400–3161 persoane. Adaptare și utilizare documentată "
        "de peste 35 de ani (Pitariu, Ghițeanu, Mitrofan)."
    ),
    # 11587
    (
        "Alpha Cronbach FPI-R în RO: 0,67–0,84 — comparabil cu datele germane. "
        "Valori sub 0,40 sau peste 0,95 nu corespund literaturii FPI."
    ),
    # 11588
    (
        "Convergență FPI–CPI: r = 0,51–0,87, mediană ~0,69 — validitate "
        "convergentă solidă cu inventarul lui Gough."
    ),
    # 11589
    (
        "Sat: ↑ optimist/mulțumit; ↓ pesimist/depresiv. Ambele perechi din "
        "variantele a și b descriu corect polii scalei."
    ),
    # 11590
    (
        "Soc: ↑ altruist, responsabil social; ↓ individualist. Timiditatea "
        "aparține Inhibiției (Inh), nu orientării sociale."
    ),
    # 11591
    (
        "Real: ↑ ambițios, competitiv; ↓ lipsă motivație realizare. "
        "Relaxarea ține de Solic ↓, nu Real ↑."
    ),
    # 11592
    (
        "Exci: ↑ iritabil, impulsiv; ↓ autocontrol. Calmul e caracteristic "
        "Exci ↓, nu Exci ↑."
    ),
    # 11593
    (
        "Agres: ↑ agresiv, dominator; ↓ pasiv. Altruismul ține de Soc, nu "
        "Agres."
    ),
    # 11594
    (
        "Solic: ↑ suprasolicitat, tensionat; ↓ relaxat. Optimismul ține de "
        "Sat/Emo ↓, nu Solic."
    ),
    # 11595
    (
        "Extrav: ↑ sociabil, activ; ↓ introvert, rezervat. Anxietatea ține de "
        "Emo ↑, nu Extrav."
    ),
    # 11596
    (
        "Emo: ↑ instabil, anxios; ↓ stabil, optimist. Sociabilitatea ține de "
        "Extrav, nu Emo."
    ),
    # 11597
    (
        "Sinc: ↑ sincer, deschis; ↓ impresionare favorabilă (fake good). "
        "Conformismul accentuat poate apărea la Sinc ↓, nu ↑."
    ),
    # 11598
    (
        "FPI-G include 9 scale de bază + 3 compozite: Extraversiune (E), "
        "Nevrotism (N), Masculinitate (M). Sat e scară FPI-R."
    ),
    # 11599
    (
        "FPI-R: scalele Sat–PSan (1–9) au câte ~12 itemi. Sinc, Extrav, Emo "
        "au câte ~14 itemi."
    ),
    # 11600
    (
        "FPI în RO: >35 ani utilizare; Pitariu, Ghițeanu, Mitrofan; fidelitate "
        "comparabilă Germania. Normele nu sunt copiate identic fără recalibrare."
    ),
    # 11601
    (
        "Avantaje FPI: structură multidimensională, validitate criteriu, "
        "profil rapid, obiectivitate. Interpretarea intuitivă fără barem ar "
        "anula obiectivitatea."
    ),
    # 11602
    (
        "Aplicabilitate: clinic, psihoterapie, organizațional, educațional, "
        "consiliere. Nu e limitat la forensic."
    ),
    # 11603
    (
        "Fidelitate FPI-R: α 0,67–0,84; test-retest stabil (Inhibiție "
        "0,84–0,85); consistență internă rezonabilă. Fidelitate zero = fals."
    ),
    # 11604
    (
        "Validitate FPI: >1400 referințe; corelații CPI 0,51–0,87; peer "
        "nomination 0,51–0,87; convergență cu inventare consacrate. Validitatea "
        "e bine documentată."
    ),
    # 11605
    (
        "Demografice: vârsta influențează semnificativ scorurile; gen, educație "
        "și reședința nu produc variații sistematice mari; Emo poate fi mai "
        "evidentă la femei — nuanță față de regula generală."
    ),
    # 11606
    (
        "Scoruri ridicate: Sat=optimist; Soc=altruist; Real↓=lipsă motivație "
        "(nu Real↑); Inh=timid. Real↑=ambițios, competitiv."
    ),
    # 11607
    (
        "Scoruri scăzute: Agres=pasiv; Solic=relaxat; Exci=autocontrol. Teamă "
        "de boală = PSan ↑, nu PSan ↓."
    ),
    # 11608
    (
        "Interpretare FPI (6 pași): intercorelații scale, variabile demografice, "
        "trăsături dominante — profil holistic, nu diagnostic psihotic automat."
    ),
    # 11609
    (
        "FPI-R: 138+1 itemi; 10 scale + Sinc + Extrav + Emo; Da/Nu; autori "
        "Fahrenberg, Selg, Hampel (1970)."
    ),
    # 11610
    (
        "Psihometrie RO: N 2400–3161; α 0,67–0,84; test-retest Inhibiție "
        "~0,84–0,85; corelații CPI 0,51–0,87 (mediană ~0,69)."
    ),
    # 11611
    (
        "Aplicabilitate documentată: clinic, psihoterapie, organizațional, "
        "educațional, consiliere — toate patru domenii corecte."
    ),
    # 11612
    (
        "FPI-G clasic: Nervozitate, Depresie, Dominare = scale originale. Sat "
        "aparține FPI-R revizuit."
    ),
    # 11613
    (
        "Pași interpretare: intercorelații, demografice, trăsături dominante. "
        "Scorurile izolate, fără context, dau o imagine incompletă."
    ),
    # 11614
    (
        "FPI-G: 9 scale + E, N, M; ~30–40 min. FPI-R: revizuit, 138 itemi, "
        "10–30 min, scale Sat–Emo. Format Da/Nu, nu Likert."
    ),
    # 11615
    (
        "Validitate convergentă: >1400 referințe, corelații CPI, peer "
        "nomination. Validitatea de criteriu e documentată, nu inexistentă."
    ),
]

assert len(FPI_EXPLANATIONS) == 50
