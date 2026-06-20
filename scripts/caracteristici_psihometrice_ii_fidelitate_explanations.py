"""Explicații — Caracteristici psihometrice II, cap. 2: fidelitate (ID 11296–11345)."""

from __future__ import annotations

from typing import List

FIDELITATE_TEST_EXPLANATIONS: List[str] = [
    # 11296
    (
        "Adevărat. α (Alpha Cronbach) estimează consistența internă — itemii scalei "
        "„ merg împreună”. E indice de fidelitate, nu de validitate."
    ),
    # 11297
    (
        "Test-retest: aceeași formă, timp diferit. Formele paralele imediate, "
        "half-split și inter-rater sunt alte metode cu surse de eroare diferite."
    ),
    # 11298
    (
        "Test-retest → eșantionare temporală (stare, practică, maturare). Nu "
        "e despre examinatori sau jumătăți de test într-o sesiune."
    ),
    # 11299
    (
        "Forme alternative imediate: două forme paralele, eroare de eșantionare "
        "de conținut (itemi diferiți). Nu e doar temporală și nu e inter-rater."
    ),
    # 11300
    (
        "Forme alternative întârziate combină timp + conținut. Nu e consistență "
        "internă dintr-o singură administrare."
    ),
    # 11301
    (
        "Half-split: corelația rhh între jumătăți — eșantionare de conținut în "
        "cadrul aceluiași test. Nu e retest și nu e acord inter-rater."
    ),
    # 11302
    (
        "KR-20 și α estimează consistența internă dintr-o administrare. Validitatea "
        "de criteriu și inter-rater sunt alte tipuri de fidelitate/ acord."
    ),
    # 11303
    (
        "Inter-rater: acordul scorerilor — eroarea vine de la diferențe de "
        "examinator. Nu e half-split sau forme paralele."
    ),
    # 11304
    (
        "Patru asocieri corecte din tabel: test-retest temporal; forme alternative "
        "conținut; half-split conținut; inter-rater diferențe examinator. Ultima "
        "nu e temporală pură."
    ),
    # 11305
    (
        "Spearman-Brown half-split: rtt = 2·rhh/(1+rhh). Celelalte formule "
        "inversează sau amestecă relația."
    ),
    # 11306
    (
        "rhh = 0,50 → rtt = 2×0,50/(1+0,50) = 1/(1,5) ≈ 0,66. Nu rămâne 0,50 "
        "fără corecție."
    ),
    # 11307
    (
        "Formula lungimii: rnn = n·rtt/[1+(n−1)·rtt]. Nu rtt/n sau rtt²·n — "
        "Spearman-Brown extrapolează efectul numărului de itemi paraleli."
    ),
    # 11308
    (
        "Exemplu curs: 20 itemi, rtt=0,87 → n≈2,82 → ~56 itemi pentru rtt≈0,95. "
        "Presupune itemi paraleli de aceeași calitate."
    ),
    # 11309
    (
        "KR-20 pentru itemi dicotomici (corect/greșit). Likert și proiective "
        "folosesc de regulă Alpha, nu KR-20."
    ),
    # 11310
    (
        "Alpha pentru itemi multi-punct și consistență internă. Necesită varianță "
        "între itemi. Nu măsoară validitate de criteriu sau inter-rater."
    ),
    # 11311
    (
        "Fals. Alpha e fidelitate (consistență internă), nu validitate. Validitatea "
        "cere dovezi că măsori constructul/criteriul țintă."
    ),
    # 11312
    (
        "KR-20: n, SDt², Σpq pentru itemi dicotomici. rxy e validitate criterială, "
        "nu componentă KR-20."
    ),
    # 11313
    (
        "Alpha: factor n/(n−1) și 1 − Σ(SDi²)/SDt². rhh e pentru half-split, nu "
        "Alpha direct."
    ),
    # 11314
    (
        "α indică consistența internă — fidelitatea itemilor scalei. Nu garantează "
        "validitate, retest temporal sau mărimea efectului."
    ),
    # 11315
    (
        "Adevărat. SEM = SDt·√(1−rtt): când rtt crește, (1−rtt) scade → SEM "
        "scade. Legătură directă fidelitate–precizie."
    ),
    # 11316
    (
        "Decizii individuale cu miză mare: rtt orientativ 0,90–0,95. 0,70–0,80 "
        "e pentru cercetare; 0,50 e prea mic; 1,00 e ideal teoretic, nu prag fix."
    ),
    # 11317
    (
        "În cercetare exploratorie, 0,70–0,80 poate fi acceptabil contextual. "
        "Nu e același standard ca pentru decizii clinice individuale."
    ),
    # 11318
    (
        "Pragurile depind de scop și consecințe; deciziile individuale cer "
        "fidelitate mai mare; 0,70–0,80 poate merge în cercetare. Nu există "
        "prag universal mecanic."
    ),
    # 11319
    (
        "SEM = SDt·√(1−rtt). Nu SDt·rtt sau SDt/rtt — formula leagă dispersia "
        "testului de fidelitate."
    ),
    # 11320
    (
        "SDt=10, rtt=0,80 → SEM = 10·√0,20 = 10·0,447 ≈ 4,47 → rotunjit ~5 în "
        "exemplul din curs."
    ),
    # 11321
    (
        "Interval de încredere al scorului real: X ± z·SEM. Nu X±SDt fără fidelitate "
        "și nu X±rtt."
    ),
    # 11322
    (
        "Reguli orientative: 95% → ±2·SEM; 99% → ±3·SEM. Nu inversați multiplicatorii."
    ),
    # 11323
    (
        "QI=120, SEM=5: 95% ≈ 120±10 → 110–130; 99% ≈ 120±15 → 105–135. "
        "Intervalele înguste (115–125) subestimează incertitudinea."
    ),
    # 11324
    (
        "rtt mare → SEM mic; SEM reflectă imprecizia scorului. SEM nu crește cu "
        "rtt și nu e zero indiferent de fidelitate."
    ),
    # 11325
    (
        "Adevărat. rhh din half-split subestimează rtt — de aceea se aplică "
        "Spearman-Brown pentru extrapolare la testul complet."
    ),
    # 11326
    (
        "Test-retest când constructul e relativ stabil și poți aștepta între "
        "administrări. Nu când constructul sau itemii se schimbă rapid/definiție."
    ),
    # 11327
    (
        "Forme alternative când ai forme paralele și vrei să reduci memorarea "
        "itemilor. Subiectivitatea fără barem nu le înlocuiește."
    ),
    # 11328
    (
        "Limite test-retest: practică, oboseală, schimbări reale, construct instabil. "
        "Nu elimină eroarea de conținut — aceea e pentru alte metode."
    ),
    # 11329
    (
        "Inter-rater când scorarea depinde de judecata examinatorului. Itemii "
        "auto-corectați nu necesită acord inter-rater."
    ),
    # 11330
    (
        "Consistența internă (KR-20, α) se calculează dintr-o singură administrare, "
        "folosind variația itemilor vs total. Nu din retest sau inter-rater."
    ),
    # 11331
    (
        "Eșantionare de conținut: half-split, forme alternative, KR-20/α (itemi "
        "diferiți eșantionează constructul). Test-retest aceeași formă = temporală."
    ),
    # 11332
    (
        "Eroare temporală: test-retest și forme alternative întârziate. Inter-rater "
        "și Alpha într-o sesiune au alte surse."
    ),
    # 11333
    (
        "Sinteză tabel capitol 2: fiecare metodă cu sursa de eroare potrivită — "
        "temporală, conținut, examinator, consistență internă."
    ),
    # 11334
    (
        "Spearman-Brown lungime: itemii adăugați trebuie paraleli; mai mulți itemi "
        "buni pot crește rtt. Nu scade automat cu n."
    ),
    # 11335
    (
        "Fals. Când rtt crește, SEM scade — nu devine mai mare decât SDt "
        "obligatoriu; la rtt→1, SEM→0."
    ),
    # 11336
    (
        "SEM mic = scor mai precis, interval mai îngust. Nu garantează validitate "
        "și nu elimină complet eroarea."
    ),
    # 11337
    (
        "X±z·SEM estimează zona probabilă a scorului real, legată de fidelitate. "
        "Nu e validitate de criteriu sau diferență față de medie."
    ),
    # 11338
    (
        "rhh = corelația dintre scorurile celor două jumătăți ale testului — "
        "baza half-split înainte de Spearman-Brown."
    ),
    # 11339
    (
        "KR-20 pentru dicotomici; Alpha pentru multi-punct cu varianță item. "
        "Nu inversați — KR-20 pe Likert e nepotrivit."
    ),
    # 11340
    (
        "Trei formule corecte: Spearman-Brown half-split, Spearman-Brown lungime, "
        "SEM. SEM = SDt·√rtt e capcană — sub radical e (1−rtt)."
    ),
    # 11341
    (
        "Patru idei praguri: clinic 0,90–0,95; cercetare 0,70–0,80; depind de "
        "scop; interpretare contextuală — nu mecanică."
    ),
    # 11342
    (
        "Half-split: împărțire test, rhh, corecție Spearman-Brown. Nu forme "
        "paralele independent create separat."
    ),
    # 11343
    (
        "SEM scade cu rtt; intervale 95%/99%; exemplu QI. Intervalul nu elimină "
        "eroarea — o cuantifică."
    ),
    # 11344
    (
        "Forme paralele: itemi diferiți, construct similar; echivalența perfectă e "
        "rare; imediat reduce efectul timpului. Nu garantează validitate maximă."
    ),
    # 11345
    (
        "Sinteză capitol: metode–erori; Spearman-Brown; KR-20/α; SEM și interval "
        "de încredere leagă fidelitatea de precizia scorului observat."
    ),
]

assert len(FIDELITATE_TEST_EXPLANATIONS) == 50
