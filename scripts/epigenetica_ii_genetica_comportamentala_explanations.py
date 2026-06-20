"""Explicații — Epigenetica II: GENETICĂ COMPORTAMENTALĂ (ID 11806–11855)."""

from __future__ import annotations

from typing import List

GENETICA_COMPORTAMENTALA_EXPLANATIONS: List[str] = [
    # 11806
    (
        "Adevărat. Genetica comportamentală investighează cum diferențele genetice "
        "contribuie la variația comportamentului, cogniției și trăsăturilor "
        "psihologice — nu negă mediul, ci estimează contribuțiile relative."
    ),
    # 11807
    (
        "Adevărat. H² (eritabilitate) = Vg / Vp: proporția varianței fenotipice "
        "din populație explicată de diferențele genetice. Nu se aplică la un "
        "singur individ, ci la variația între indivizi."
    ),
    # 11808
    (
        "Fals. Gemenii MZ au ~100% ADN comun (identici genetic). Gemenii DZ "
        "au ~50%, ca frații obișnuiți. Confundarea procentelor distruge logica "
        "studii gemelare."
    ),
    # 11809
    (
        "Fals. În modelul ACE: C = mediu comun/familial (factori împărtășiți). "
        "E = mediu unic/individual (experiențe neîmpărtășite + eroare). "
        "Inversarea C și E este capcană frecventă."
    ),
    # 11810
    (
        "Adevărat. GWAS scanează genomul pentru SNP-uri asociate statistic "
        "cu o trăsătură (ex. scor la un test, simptome). Identifică "
        "variante candidate, nu explică singur tot comportamentul."
    ),
    # 11811
    (
        "Genetica comportamentală vizează legătura gene–comportament și "
        "diferențele individuale. Mutațiile cromozomiale sau numărul de "
        "cromozomi aparțin altor capitole (patologii), nu scopului central."
    ),
    # 11812
    (
        "Vg = varianța genetică — partea din diferențele fenotipice atribuită "
        "diferențelor genetice dintre indivizi. Vp e totalul; C și E sunt "
        "componente de mediu din modelul ACE."
    ),
    # 11813
    (
        "Vp = varianța fenotipică totală — toate diferențele observate în "
        "trăsătură (gen + mediu + interacțiuni + eroare). Numitorul formulei "
        "H² = Vg / Vp."
    ),
    # 11814
    (
        "H² apropiat de 1: diferențele genetice explică o parte mare din "
        "variația trăsăturii în populația studiată. Nu înseamnă determinism "
        "absolut al fiecărui individ."
    ),
    # 11815
    (
        "H² apropiat de 0: diferențele de mediu (și alte surse non-genetice) "
        "explică relativ mai mult din variație. Nu demonstrează absența genelor."
    ),
    # 11816
    (
        "MZ (monozigoți): același zigot → ~100% ADN comun → gemeni identici. "
        "Baza comparației cu DZ în studiile de eritabilitate."
    ),
    # 11817
    (
        "DZ (dizigoți): ovule diferite → ~50% ADN comun, ca frații obișnuiți → "
        "gemeni fraterni. Dacă MZ sunt mai similari decât DZ, diferența nu "
        "poate fi explicată doar prin mediu familial comun."
    ),
    # 11818
    (
        "MZ = gemeni identici, din același ovul fertilizat. DZ = gemeni "
        "fraterni. Fenotip similar nu implică automat 50% ADN (MZ au 100%)."
    ),
    # 11819
    (
        "DZ = gemeni fraterni, din fertilizări separate. Nu sunt clonă "
        "identică (100% ADN) — aceasta descrie MZ."
    ),
    # 11820
    (
        "Logica studiilor gemelare: MZ și DZ cresc adesea în medii similare. "
        "Dacă MZ sunt mai similari la o trăsătură decât DZ, diferența extra "
        "de similitudine la MZ (100% vs 50% ADN) sugerează influență genetică."
    ),
    # 11821
    (
        "A (Additive genetic) = influența genetică aditivă — efectul cumulativ "
        "al variantelor genetice asupra trăsăturii. Nu e mediu comun (C) "
        "nici mediu unic (E)."
    ),
    # 11822
    (
        "C (Common environment) = factori de mediu împărtășiți: familie, "
        "socioeconomic, școală aceeași etc. Diferit de E (experiențe unice)."
    ),
    # 11823
    (
        "E (Unique environment) = mediu neîmpărtășit + eroare de măsurare. "
        "Include experiențe pe care doar un geamăn le are, accidente, "
        "relații unice etc."
    ),
    # 11824
    (
        "SNP = polymorphism la o singură bază (A/T/C/G diferă între indivizi). "
        "Unitatea de analiză în GWAS. GPS combină multe SNP-uri, nu unul singur."
    ),
    # 11825
    (
        "GWAS = studiu asociativ la nivel de genom: testează milioane de SNP-uri "
        "pentru asociere cu o trăsătură. Nu măsoară direct H² din interviu."
    ),
    # 11826
    (
        "GPS (Polygenic Score) = scor calculat din efectele estimate ale "
        "multor SNP-uri, asociate cu o trăsătură. Util ca index al "
        "predispoziției genetice, nu ca diagnostic individual."
    ),
    # 11827
    (
        "H² = proporția varianței fenotipice explicate genetic (Vg/Vp). "
        "Eritabilitatea se referă la variație în populație, nu la cât de "
        "mult contează genele pentru un singur individ."
    ),
    # 11828
    (
        "Modelul ACE descompune varianța fenotipică în A (genetic aditiv), "
        "C (mediu comun) și E (mediu unic + eroare). A+C+E explică Vp "
        "în cadrul modelului clasic al studiilor gemelare."
    ),
    # 11829
    (
        "MZ ~100% ADN; DZ ~50%. Asocierea inversă (MZ 50%, DZ 100%) "
        "contrazice definiția biologică a tipurilor de gemeni."
    ),
    # 11830
    (
        "H² → 1: influență genetică mare la variație; H² → 0: influență "
        "mediu mare. H² = Vg/Vp este formula corectă. H² → 1 nu înseamnă "
        "varianță genetică zero — ci opusul."
    ),
    # 11831
    (
        "A = genetic aditiv; C = mediu comun/familial. A ≠ mediu unic; "
        "E = mediu unic (în celălalt item ACE). Confuzia A/C/E e frecventă."
    ),
    # 11832
    (
        "C = mediu comun/familial; E = mediu unic/individual. C ≠ genetic "
        "(A). E ≠ Vp total — Vp include A+C+E."
    ),
    # 11833
    (
        "Studii gemelare: MZ 100% ADN, DZ 50%. Dacă MZ > DZ la similaritate "
        "→ influență genetică. DZ nu sunt din același ovul; MZ nu sunt "
        "fraterni."
    ),
    # 11834
    (
        "SNP = o bază variabilă; GWAS = asocieri SNP–trăsături la scară "
        "genomică. SNP ≠ GPS; GWAS nu măsoară H² direct prin interviu."
    ),
    # 11835
    (
        "GWAS identifică SNP-uri asociate; GPS combină efecte multiple. "
        "Ambele abordează SNP–trăsături. GPS nu înlocuiește studiile "
        "gemelare — metode complementare."
    ),
    # 11836
    (
        "H² = Vg/Vp; Vg = varianță genetică; Vp = varianță fenotipică totală. "
        "Vp nu e doar mediul unic (E) — include toate sursele de varianță."
    ),
    # 11837
    (
        "MZ: 100% ADN, același ovul. DZ: 50% ADN, ovule diferite. "
        "DZ nu provin din același ovul fertilizat."
    ),
    # 11838
    (
        "H² = Vg/Vp. H² mare → genetic explică mai mult din variație; "
        "H² mic → mediul explică mai mult. H² = 1 nu = determinism "
        "individual absolut."
    ),
    # 11839
    (
        "SNP: variație unei baze. GWAS: SNP–trăsături. GPS: scor poligenic. "
        "GPS nu e variație a unei singure baze — combină multe variante."
    ),
    # 11840
    (
        "ACE: A genetic, C mediu comun, E mediu unic. E ≠ mediu comun (C). "
        "Toate trei sunt componente distincte ale modelului."
    ),
    # 11841
    (
        "Inferență validă: MZ > DZ → influență genetică. MZ și DZ pot "
        "împărtăși mediu familial similar (C). Similaritate MZ > DZ nu "
        "exclude mediul — ambele contribuie; diferența MZ–DZ indică genetic."
    ),
    # 11842
    (
        "GPS: combină SNP-uri; estimează tendință genetică; adesea derivat "
        "din GWAS. Nu e identic cu un singur SNP."
    ),
    # 11843
    (
        "Genetica comportamentală: gene → comportament; diferențe individuale; "
        "H² ca indicator al contribuției genetice la variație. Nu postulează "
        "că mediul e irelevant — studiază ambele surse."
    ),
    # 11844
    (
        "A = genetic aditiv; E = mediu unic (+ eroare). A ≠ mediu comun; "
        "E ≠ genetic. Perechea corectă descrie cele două componente opuse "
        "ca natură (gen vs mediu neîmpărtășit)."
    ),
    # 11845
    (
        "Vg = varianță genetică; Vp = varianță fenotipică totală. "
        "Inversarea lor (Vg = Vp total) contrazice formula H² = Vg/Vp."
    ),
    # 11846
    (
        "H² = Vg/Vp; Vg = varianță genetică. Vp nu e doar E (mediu unic) — "
        "include genetic, mediu comun, mediu unic și alte surse."
    ),
    # 11847
    (
        "ACE complet: A genetic aditiv, C mediu comun, E mediu unic. "
        "A+C+E descompun varianța fenotipică în modelul clasic. Toate "
        "patru enunțuri sunt corecte."
    ),
    # 11848
    (
        "Gemeni: MZ 100% identici; DZ 50% fraterni; inferență genetică din "
        "MZ > DZ; pot crește în același mediu familial. Recapitulare "
        "completă a logicii studiilor gemelare."
    ),
    # 11849
    (
        "H² = Vg/Vp; H² → 1 genetic mare; H² → 0 mediu mare; H² e măsură "
        "populațională (variație între indivizi), nu etichetă individuală."
    ),
    # 11850
    (
        "Tehnici moderne: SNP (o bază), GWAS (asocieri), GPS (scor poligenic). "
        "GPS se construiește adesea pe baza rezultatelor GWAS — legătură "
        "metodologică importantă."
    ),
    # 11851
    (
        "Recapitulare integrată: scop (gene → comportament); H² = Vg/Vp; "
        "gemeni MZ/DZ; ACE (A, C, E). Patru piloni ai geneticii "
        "comportamentale clasice."
    ),
    # 11852
    (
        "SNP = variație o bază; GWAS = asocieri SNP–trăsături. GPS confundat "
        "cu SNP e capcană frecventă — GPS combină multe SNP-uri."
    ),
    # 11853
    (
        "C = mediu comun/familial: factori împărtășiți (familie, școală). "
        "Nu e mediu unic (E) și nu e influență genetică (A)."
    ),
    # 11854
    (
        "Gemeni: MZ/DZ procente ADN; tip identic/fratern; inferență din "
        "MZ > DZ. Similaritate MZ = DZ ar sugera lipsă diferență genetică "
        "relevantă — nu eritabilitate maximă."
    ),
    # 11855
    (
        "Recapitulare finală: scop → H²/ACE → gemeni → SNP/GWAS/GPS. "
        "H² = 1 nu înseamnă că mediul nu contează pentru niciun individ — "
        "descrie variația populațională, nu destin individual."
    ),
]

assert len(GENETICA_COMPORTAMENTALA_EXPLANATIONS) == 50
