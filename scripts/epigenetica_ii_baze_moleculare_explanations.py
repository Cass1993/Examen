"""Explicații — Epigenetica II: BAZE MOLECULARE (ID 11726–11805)."""

from __future__ import annotations

from typing import List

BAZE_MOLECULARE_EXPLANATIONS: List[str] = [
    # 11726
    (
        "Adevărat. În 1953, James Watson și Francis Crick au propus modelul "
        "dublu-helix al ADN-ului: două catene antiparale, cu bazele azotate "
        "orientate spre interior și legate prin punți de hidrogen. Contribuțiile "
        "datelor de difracție a razelor X (Rosalind Franklin, Maurice Wilkins) "
        "au fost esențiale, dar modelul structural clasic poartă numele Watson "
        "și Crick."
    ),
    # 11727
    (
        "Adevărat. ADN-ul (acid dezoxiribonucleic) este materialul ereditar "
        "principal: stochează secvența de informație genetică sub formă de "
        "ordinea bazelor azotate (A, T, C, G) de-a lungul catenelor."
    ),
    # 11728
    (
        "Fals. ADN-ul este, de regulă, bicatenar (două catene complementare). "
        "ARN-ul este, de regulă, monocatenar — o singură filă de nucleotide "
        "ribonucleice. Există excepții (ex. anumite virusuri cu ARN dublu-catenar), "
        "dar regula generală pentru celulele eucariote este ADN bicatenar, "
        "ARN monocatenar."
    ),
    # 11729
    (
        "Fals. Perechea A–T formează două legături de hidrogen, nu trei. "
        "Trei legături de hidrogen apar între citozină și guanină (C–G). "
        "De aceea regiunile bogate în C–G sunt termodinamic mai stabile decât "
        "cele bogate în A–T."
    ),
    # 11730
    (
        "Adevărat. Celulele somatice (corporale) umane conțin 23 de perechi "
        "de cromozomi, adică 46 de cromozomi în total. Gameții (ovule, "
        "spermatozoizi) au jumătate — 23 de cromozomi — pentru ca la fertilizare "
        "să se restabilească numărul diploid."
    ),
    # 11731
    (
        "Watson și Crick (1953) au descris structura dublu-helix. Mendel a "
        "formulat legile eredității; Darwin teoria selecției naturale. Franklin "
        "a contribuit cu date experimentale, dar nu este co-autor al modelului "
        "structural clasic Watson–Crick."
    ),
    # 11732
    (
        "Nucleotidul = unitatea de bază a acizilor nucleici: bază azotată + "
        "zahăr (dezoxiriboză în ADN, riboză în ARN) + grupare fosfat. "
        "Aminoacizii, codonii și ribozomii apar la nivel proteic / traducție, "
        "nu la structura nucleotidului."
    ),
    # 11733
    (
        "Cele patru baze din ADN: Adenină (A), Timină (T), Citozină (C), "
        "Guanină (G). Uracilul (U) apare în ARN, în locul timinei — nu face "
        "parte din ADN-ul standard."
    ),
    # 11734
    (
        "Timina există în ADN; în ARN timina este înlocuită de uracil (U). "
        "Uracilul se poate perechea cu adenina prin două legături de hidrogen, "
        "similar mecanismului A–T din ADN."
    ),
    # 11735
    (
        "Perechea adenină–timină (A–T) are 2 legături de hidrogen. Este "
        "complementară și stabilă, dar mai puțin stabilă decât perechea C–G "
        "(3 legături de hidrogen)."
    ),
    # 11736
    (
        "Perechea citozină–guanină (C–G) are 3 legături de hidrogen — cea "
        "mai stabilă dintre cele două perechi canonice din ADN. Regiunile "
        "bogate în C–G necesită temperaturi mai mari pentru denaturare."
    ),
    # 11737
    (
        "Purinele au structură biciclică (două inele): adenina (A) și guanina "
        "(G). Citozina, timina și uracilul sunt pirimidine (un inel)."
    ),
    # 11738
    (
        "Pirimidinele (un inel): citozină (C), timină (T) în ADN, uracil (U) "
        "în ARN. Adenina și guanina sunt purine (două inele), nu pirimidine."
    ),
    # 11739
    (
        "Complementaritatea Watson–Crick: A se leagă doar cu T, C doar cu G "
        "(pe fiecare catenă). Această regulă permite replicarea fidelă: fiecare "
        "catenă servește ca șablon pentru sinteza celeilalte."
    ),
    # 11740
    (
        "Human Genome Project (1990–2003) a secvențiat genomul uman — harta "
        "completă a ADN-ului nuclear uman. Structura dublu-helix fusese "
        "descoperită în 1953; HGP a cartografiat secvența la scară de genom întreg."
    ),
    # 11741
    (
        "Dogma centrală (Francis Crick): fluxul informației ADN → ARNm → "
        "proteină. Transcripția copiază informația din ADN în ARNm; translația "
        "decodează ARNm în lanț de aminoacizi. Fluxul invers (proteină → ADN) "
        "nu apare în expresia genică standard."
    ),
    # 11742
    (
        "Transcripția (ADN → ARNm) are loc în nucleu la eucariote. Enzima "
        "cheie este ARN polimeraza. Ribozomii și translația sunt citoplasmatici; "
        "mitocondria are propria transcripție pentru ADN mitocondrial, dar "
        "transcripția nucleară clasică = nucleu."
    ),
    # 11743
    (
        "Translația (ARNm → proteină) are loc la ribozomi, în citoplasmă "
        "(sau pe reticulul endoplasmatic rugos). Nucleul găzduiește transcripția, "
        "nu asamblarea aminoacizilor în proteine."
    ),
    # 11744
    (
        "Codonul = triplet de 3 nucleotide din ARNm care codifică un aminoacid "
        "(sau semnal START/STOP). Genetic code-ul este citit consecutiv, "
        "fără spații, în grupuri de trei."
    ),
    # 11745
    (
        "AUG codifică metionina și funcționează ca codon START — inițiază "
        "translația. UAA, UAG, UGA sunt codoni STOP (terminare, fără aminoacid "
        "corespunzător)."
    ),
    # 11746
    (
        "Codonii STOP: UAA, UAG, UGA — semnalează eliberarea lanțului "
        "polipeptidic de pe ribozom. AUG este START, nu STOP. Codonii GUA/GUG "
        "codifică valină, nu oprirea traducerii."
    ),
    # 11747
    (
        "ARNt (ARN de transfer) transportă aminoacizii activați la ribozom "
        "și se leagă prin anticodon de codonul complementar din ARNm. Nu "
        "stochează informația genetică pe termen lung (rolul ADN-ului) și "
        "nu formează perechi A–T în dublu-helix."
    ),
    # 11748
    (
        "Proteomul = totalitatea proteinelor exprimate într-o celulă, țesut "
        "sau organism la un moment dat. Include proteine modificate post-sinteză "
        "(fosforilare, glicozilare etc.). Nu se confundă cu numărul de cromozomi "
        "sau cu setul de gene din ADN."
    ),
    # 11749
    (
        "Complementaritate în ADN: A–T și C–G. A–G sau C–T nu respectă "
        "geometria perechilor Watson–Crick și nu apar ca perechi stabile în "
        "dublu-helix."
    ),
    # 11750
    (
        "A–T: 2 legături H, stabilitate relativ mai mică. C–G: 3 legături H, "
        "stabilitate mai mare. Varianta inversă (A–T cu 3H sau C–G cu 2H) "
        "contrazice structura cristalografică cunoscută."
    ),
    # 11751
    (
        "ADN: bicatenar (două catene). ARN: monocatenar (de regulă). "
        "Inversarea (ADN monocatenar / ARN bicatenar ca regulă generală) "
        "descrie incorect majoritatea moleculelor din celula eucariotă."
    ),
    # 11752
    (
        "ADN conține timină (T); ARN conține uracil (U) în locul timinei. "
        "Uracilul lipsește din ADN-ul standard; timina lipsește din ARN-ul "
        "matur. Această diferență ajută enzimele celulare să distingă cele "
        "două tipuri de acizi nucleici."
    ),
    # 11753
    (
        "Transcripție → nucleu (ADN → ARNm). Translație → ribozomi/citoplasmă "
        "(ARNm → proteină). Confundarea locațiilor (transcripție la ribozomi "
        "sau translație exclusiv în nucleu) este o capcană frecventă în grile."
    ),
    # 11754
    (
        "Transcripția produce ARNm din șablonul ADN. Translația produce "
        "proteina din ARNm. Transcripția nu sintetizează direct proteina; "
        "translația nu copiază ADN în ARNm."
    ),
    # 11755
    (
        "AUG = START (inițiere translație). UAA, UAG, UGA = STOP (terminare). "
        "Atribuirea inversă (AUG ca STOP sau UAA ca START) contrazice codul "
        "genetic universal."
    ),
    # 11756
    (
        "Celule somatice: 46 cromozomi (2n = diploid). Gameți: 23 cromozomi "
        "(n = haploid). La fertilizare, 23 + 23 = 46. Gameții cu 46 ar fi "
        "diploidi — incorect."
    ),
    # 11757
    (
        "Genomul uman somatic: 22 perechi de autozomi + 1 pereche de "
        "cromozomi sexuali (XX sau XY) = 23 perechi = 46 cromozomi. "
        "Autozomii poartă majoritatea genelor; cromozomii sexuali determină "
        "sexul biologic și gene legate de sex."
    ),
    # 11758
    (
        "ADN mitocondrial (ADNmt): moștenire predominant maternă — ovulul "
        "contribuie cu mitocondrii, spermatozoidul cu foarte puține. ADNmt "
        "este distinct de ADN-ul nuclear ca origine și secvență. Nu lipsește "
        "din celulele umane normale."
    ),
    # 11759
    (
        "Proteinele sunt polimeri de aminoacizi. Gruparea R (radical lateral) "
        "diferențiază fiecare aminoacid. Forma tridimensională (plierea) "
        "determină funcția (enzimatică, structurală, de semnalizare). Proteinele "
        "nu se formează direct din baze azotate — acestea sunt componente ale "
        "acizilor nucleici."
    ),
    # 11760
    (
        "Nucleotid = bază azotată + zahăr (dezoxiriboză în ADN) + fosfat. "
        "Gruparea R aparține aminoacizilor, nu nucleotidelor. Histonele și "
        "nucleozomii sunt niveluri de organizare a cromatinei, nu unitatea "
        "elementară."
    ),
    # 11761
    (
        "Purine (A, G): două inele. Pirimidine (C, T, U): un inel. "
        "A și C nu sunt ambele pirimidine (A e purină). G și T nu sunt "
        "ambele purine (T e pirimidină)."
    ),
    # 11762
    (
        "Transcripție: nucleu; enzimă ARN polimeraza; pe ARNm, uracil "
        "înlocuiește timina din șablon. Rezultatul direct este ARNm, nu "
        "proteina — proteina apare după translație."
    ),
    # 11763
    (
        "Translație: ribozomi + citoplasmă; citește codonii ARNm; ARNt "
        "aduce aminoacizii. Producerea ARNm din ADN este transcripție, "
        "nu translație."
    ),
    # 11764
    (
        "Dogma centrală: ADN → ARNm → proteină. Transcripția precede "
        "translația. Proteina nu se copiază direct în ADN în expresia "
        "genică standard. ARNm este șablonul pentru sinteza proteinelor "
        "la ribozom."
    ),
    # 11765
    (
        "Model Watson–Crick: dublu helix, complementaritate A–T și C–G, "
        "C–G mai stabil (3 vs 2 legături H). ADN-ul nu este monocatenar "
        "ca formă obișnuită în celulă — forma monocatenară apare tranzitor "
        "la replicare/transcripție."
    ),
    # 11766
    (
        "Toate patru afirmațiile sunt corecte: ADN stochează informația "
        "genetică; ARN participă la sinteza proteinelor; ADN conține timină, "
        "ARN conține uracil; ADN este bicatenar, ARN monocatenar (de regulă). "
        "Aceasta este sinteza comparativă esențială ADN vs ARN."
    ),
    # 11767
    (
        "HGP (1990–2003): secvențiere genom uman. Somatic: 46 cromozomi. "
        "Gameți: 23. ADN mitocondrial: moștenire maternă, nu paternă "
        "dominantă."
    ),
    # 11768
    (
        "Expresia genelor: transcripție (nucleu, ADN → ARNm), translație "
        "(ribozomi, ARNm → proteină), codon = 3 baze, AUG = START. "
        "UAA/UAG/UGA sunt STOP, nu START — confuzia START/STOP e frecventă."
    ),
    # 11769
    (
        "Toate patru enunțurile descriu corect proteinele: lanț de aminoacizi "
        "(NH₂, COOH, grup R); grup R = identitatea aminoacidului; forma 3D "
        "determină funcția; proteomul = totalitatea proteinelor exprimate, "
        "inclusiv variantele modificate post-sinteză — nu totalitatea genelor."
    ),
    # 11770
    (
        "Recapitulare integrată: nucleotid (bază + zahăr + fosfat); dublu "
        "helix Watson–Crick 1953; perechi A–T (2H) / C–G (3H); purine vs "
        "pirimidine; 46 somatic / 23 gameti; ADNmt matern; dogma centrală "
        "cu transcripție și translație. Toate cele patru enunțuri sintetizează "
        "corect baza moleculară a eredității."
    ),
    # 11771
    (
        "ADN: bicatenar, timină, stochează info. ARN: monocatenar, uracil, "
        "rol în sinteza proteinelor. Transcripția: ADN → ARNm (U în loc de T). "
        "Translația: ribozomi, ARNm → proteină — nu face parte din comparația "
        "directă structură/rol ADN vs ARN, deși este etapa următoare în "
        "dogma centrală. Replicarea ARNm → ADN în citoplasmă este falsă."
    ),
    # 11772
    (
        "Translație completă: ribozomi + citoplasmă; codon 3 baze; AUG start; "
        "UAA/UAG/UGA stop; ARNt transportă aminoacizi. Varianta d descrie "
        "transcripția (ribozomi, ADN → ARNm) — confuzie frecventă între cele "
        "două procese și locațiile lor."
    ),
    # 11773
    (
        "23 perechi somatici = 46 cromozomi (22 autozomi + 1 pereche sexuală). "
        "Gameți: 23. HGP 1990–2003: secvențiere. ADN mitocondrial: transmis "
        "predominant pe linie maternă."
    ),
    # 11774
    (
        "Legătura structură–funcție: translația transformă ARNm în lanț "
        "de aminoacizi; grup R identifică aminoacidul; plierea 3D determină "
        "funcția; proteomul cuprinde toate proteinele celulei, inclusiv cele "
        "modificate după sinteză (post-traducțional). Aminoacizii au NH₂, "
        "COOH și grup R."
    ),
    # 11775
    (
        "ARN polimeraza catalizează transcripția: sintetizează ARNm pe "
        "șablonul ADN, în nucleu. Nu asamblează aminoacizi (translație, "
        "ribozomi) și nu produce proteină direct — între ADN și proteină "
        "intervine ARNm, conform dogmei centrale."
    ),
]

assert len(BAZE_MOLECULARE_EXPLANATIONS) == 50
