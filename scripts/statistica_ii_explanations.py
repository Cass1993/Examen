"""Explicații didactice — Statistică II (ID 10961–11225)."""

from __future__ import annotations

from typing import List

from scripts.statistica_ii_boxplot_explanations import BOXPLOT_EXPLANATIONS
from scripts.statistica_ii_central_tendency_explanations import (
    CENTRAL_TENDENCY_EXPLANATIONS,
)
from scripts.statistica_ii_dispersion_explanations import DISPERSION_EXPLANATIONS
from scripts.statistica_ii_distribution_shape_explanations import (
    DISTRIBUTION_SHAPE_EXPLANATIONS,
)
from scripts.statistica_ii_hypothesis_z_test_explanations import (
    HYPOTHESIS_Z_TEST_EXPLANATIONS,
)
from scripts.statistica_ii_recap_rapid_explanations import RECAP_RAPID_EXPLANATIONS
from scripts.statistica_ii_sampling_distribution_explanations import (
    SAMPLING_DISTRIBUTION_EXPLANATIONS,
)
from scripts.statistica_ii_standardized_scores_explanations import (
    STANDARDIZED_SCORES_EXPLANATIONS,
)
from scripts.statistica_ii_frequency_explanations import FREQUENCY_EXPLANATIONS
from scripts.statistica_ii_scales_sampling_explanations import (
    SCALES_SAMPLING_EXPLANATIONS,
)

STATISTICA_II_EXPLANATIONS: List[str] = [
    # 10961
    (
        "Adevărat. Statistica nu este o „metodă de cunoaștere” în același sens în care "
        "sunt observația sistematică sau experimentul: ea oferă reguli și proceduri "
        "pentru a organiza datele, a le descrie și a evalua ipoteze. Cercetarea "
        "psihologică rămâne ancorată în întrebări teoretice și în colectarea de date "
        "empirice; statistica le ajută să fie analizate riguros."
    ),
    # 10962
    (
        "Ca instrument, statistica susține întregul demers: planificare (ce și câți "
        "participanți), descriere (medie, dispersie), inferență (teste, intervale). "
        "Nu înlocuiește observația sau ipoteza și nu este o filozofie paralelă "
        "empirismului — se folosește pe baza unor date reale, cu presupunerile "
        "fiecărei metode înțelese."
    ),
    # 10963
    (
        "Cele trei dificultăți din curs: statisticofobia (evitarea numerelor și a "
        "testelor), naivitatea statistică (rulezi analize fără să înțelegi ce "
        "presupun și ce pot spune), epatantul statistic (metode sofisticate de "
        "fațadă, nepotrivite problemei). Calculul mediei ca obligație universală "
        "nu este o categorie didactică — e un exemplu de procedură simplă, nu o "
        "capcană conceptuală în sine."
    ),
    # 10964
    (
        "Metoda științifică, în varianta prezentată: observi un fenomen, formulezi "
        "o ipoteză, aduni date empirice relevante, apoi tragi concluzii proporționale "
        "cu dovezi. A trata ipoteza ca deja demonstrată înainte de date inversează "
        "logica cercetării și produce certitudine falsă."
    ),
    # 10965
    (
        "Variabilele observate sunt cele pe care le poți înregistra direct în studiu: "
        "un timp măsurat, un răspuns bifat, o reacție înregistrată de aparat. Nu "
        "sunt inferate din teorie fără indicator concret — deși un scor poate estima "
        "un construct, înregistrarea itemului rămâne observație."
    ),
    # 10966
    (
        "Timpul de reacție și răspunsul la item sunt observate direct. Scorul la "
        "test de inteligență este un indicator observat al unui construct latent — "
        "de aceea nu e exemplu simplu de variabilă observată „brută”. Definiția "
        "teoretică fără măsură nu este variabilă observată în studiu."
    ),
    # 10967
    (
        "Latent = construct teoretic (anxietate, inteligență, sociabilitate) pe care "
        "îl estimezi prin indicatori observabili. Nu îl vezi direct; îl reconstruiești "
        "din itemi, reacții, comportamente. Nu orice coloană numerică din fișier "
        "înseamnă automat construct latent valid."
    ),
    # 10968
    (
        "Variabila independentă este factorul pe care îl manipulezi sau îl alegi "
        "pentru a vedea dacă produce schimbare: tip de exercițiu, oboseală indusă, "
        "grup de vârstă comparat. Variabila dependentă este ce măsori ca efect — "
        "nu invers."
    ),
    # 10969
    (
        "Vârsta (ca grup comparat), oboseala indusă și tipul de exercițiu pot fi VI. "
        "Performanța la test măsurată la final este VD — este rezultatul, nu factorul "
        "manipulat. Confuzia VI/VD este una dintre cele mai frecvente erori la "
        "interpretarea designurilor experimentale."
    ),
    # 10970
    (
        "Variabila dependentă este efectul: conformismul, timpul de reacție, "
        "performanța. O măsori după ce ai stabilit sau manipulat VI. VD poate fi "
        "și observată (un scor), chiar dacă estimează un construct; regula este "
        "rolul în design (efect), nu eticheta latent/observat."
    ),
    # 10971
    (
        "Fals. Naivitatea statistică înseamnă tocmai folosirea procedurilor fără "
        "înțelegere — nu refuzul total al cantificării. Refuzul total se apropie "
        "mai mult de statisticofobie. Distincția ajută la diagnostic: teamă vs "
        "competență aparentă fără fond."
    ),
    # 10972
    (
        "În experiment, VD = ceea ce măsori ca rezultat (performanță, conformism, "
        "timp de reacție). VI = ce variezi sau compari pentru a produce efectul. "
        "Variabila de control ține alți factori constanți; nu este sinonim cu VD."
    ),
    # 10973
    (
        "Perechi corecte: manipulezi exercițiul → măsori performanța; induci "
        "oboseală → măsori timpul de reacție. Ultimele variante inversează rolurile "
        "(VD ca „cauză”) — capcană clasică când etichetele par plauzibile."
    ),
    # 10974
    (
        "Timpul, greutatea și înălțimea pot lua teoretic valori fine în interval "
        "(continuu). Numărul de răspunsuri corecte este discret (întreg, numărabil). "
        "Amestecul continu/discret apare des în itemi — verifică dacă valorile pot "
        "fi fracționate teoretic sau sunt numărate."
    ),
    # 10975
    (
        "Stevens (1946): măsurarea = atribuire de numere sau simboluri conform "
        "regulilor, nu etichetare aleatorie. Regulile stabilesc ce înseamnă o "
        "unitate de diferență între valori. Fără reguli explicite, un scor nu "
        "poate fi interpretat științific."
    ),
    # 10976
    (
        "Continue: infinitate teoretică de valori între două puncte (ex. 1,3 s vs "
        "1,31 s). Discrete: valori separate, număr finit sau numărabil (ex. 2 sau "
        "3 copii). Nu confunda unități de măsură (kg) cu discret — greutatea rămâne "
        "continuă."
    ),
    # 10977
    (
        "Număr persoane în familie și număr răspunsuri corecte sunt discrete "
        "(întregi, numărabile). Timpul de reacție este continuu; o scară cu zeci "
        "posibile poate fi tot interval, nu discretă în sensul cursului."
    ),
    # 10978
    (
        "Sociabilitatea este construct latent: o estimezi prin scale, observații "
        "codificate, raportări — nu o „vezi” direct ca pe o lungime. Operaționalizarea "
        "transformă constructul în indicatori măsurabili."
    ),
    # 10979
    (
        "Observate = înregistrate direct; latente = inferate din indicatori. "
        "Inteligența prin itemi de test este operaționalizare: itemii sunt observați, "
        "constructul rămâne latent. Anxietatea cu scor validat rămâne latentă ca "
        "fenomen, deși scorul este observat — nu confunda înregistrarea indicatorului "
        "cu accesul direct la construct."
    ),
    # 10980
    (
        "Timp de reacție: observată, continuă. Răspuns la item: observată. Anxietate "
        "(construct): latentă. Tipul de exercițiu manipulat este variabilă "
        "independentă, nu dependentă."
    ),
    # 10981
    (
        "Adevărat. În design experimental standard: manipulezi sau selectezi VI, "
        "apoi măsori VD. Ex.: induci oboseală (VI) și măsori performanța (VD). "
        "Fără această distincție, interpretarea cauzalității devine ambiguă."
    ),
    # 10982
    (
        "Statisticofobia = teamă, respingere sau evitare a gândirii cantitative. "
        "Nu este competență nici chiar folosirea reflexă a software-ului. "
        "Epatantul și naivitatea implică de obicei contact cu statistica, dar "
        "într-un mod distorsionat."
    ),
    # 10983
    (
        "Epatantul statistic: analize inutile sau prea complexe pentru impresie sau "
        "din obișnuință, nu din întrebarea de cercetare. Refuzul total ține de "
        "fobie; înțelegerea presupunerilor este opusul naivității, nu epatantului."
    ),
    # 10984
    (
        "Ordinea logică: observație → ipoteză → date empirice → concluzii. Toate "
        "patru etape sunt parte din metoda științifică; concluziile vin după analiza "
        "datelor, nu înaintea lor."
    ),
    # 10985
    (
        "Regulile de Stevens leagă simbolurile de proprietăți ale fenomenelor — "
        "ex. diferența între 2 și 3 pe o scară trebuie să aibă sens definit. "
        "Nu sunt preferințe personale ale cercetătorului și nu înlocuiesc "
        "definirea constructului teoretic."
    ),
    # 10986
    (
        "Confuzii de evitat: amestec VI/VD; latent tratat ca observat direct; "
        "statistica folosită fără întrebare clară sau date bune. Operaționalizarea "
        "corectă prin itemi nu este o confuzie — este soluția pentru măsurarea "
        "constructelor latente."
    ),
    # 10987
    (
        "Statisticofobia blochează folosirea utilă; naivitatea produce erori cu "
        "software modern; epatantul complică inutil. A folosi media nu garantează "
        "înțelegere — uneori nici măcar nu e statistica potrivită pentru tipul de "
        "date."
    ),
    # 10988
    (
        "Numărul de copii este discret: valori întregi, numărabile (nu poți avea "
        "2,5 copii în sensul categoriei). „Crește în timp” nu îl face continuu — "
        "tipul variabilei se referă la valorile posibile ale măsurii, nu la "
        "dinamica în timp."
    ),
    # 10989
    (
        "Timp de reacție și număr de răspunsuri corecte ilustrează bine continuă vs "
        "discretă. Codul nominal pentru gen nu este continuu cu origine absolută — "
        "e nominal. Greutatea rămâne continuă, chiar dacă folosești unități standard."
    ),
    # 10990
    (
        "Sinteză: VI vs VD; observate vs latente; continue vs discrete; măsurare "
        "Stevens = atribuire după reguli. Toate patru descrieri sunt nucleul "
        "primului modul de statistică aplicată în psihologie."
    ),
    # 10991
    (
        "Fals. Statistica nu elimină nevoia de ipoteză și de date empirice — le "
        "structurează analiza. Fără întrebare clară și fără date de calitate, "
        "orice test rămâne gol de sens, indiferent de p-value."
    ),
    # 10992
    (
        "Chestionarul validat oferă scoruri observate (răspunsuri la itemi) care "
        "estimează anxietatea ca construct latent. Nu „măsori direct” anxietatea "
        "pură — măsori indicatori agreați ca relevanți pentru construct."
    ),
    # 10993
    (
        "Inteligența nu se observă direct: o inferezi din performanța la sarcini "
        "standardizate. Scorul este operaționalizare, nu constructul în sine. "
        "Validitatea și teoria rămân necesare pentru interpretare."
    ),
    # 10994
    (
        "Integrare: observație și ipoteză deschid investigația; datele empirice "
        "o ancorează; statistica organizează analiza fără a înlocui gândirea "
        "teoretică; concluziile respectă limitele designului și ale măsurării. "
        "Toate patru sunt coerente cu rolul instrumentului statistic."
    ),
    # 10995
    (
        "Oboseala indusă înainte de sarcină este VI: o variezi/controlați pentru a "
        "vedea efectul asupra performanței. Nu este VD — aceea ar fi performanța "
        "măsurată după inducere."
    ),
    # 10996
    (
        "Conformismul măsurat după presiune socială este VD (efect). Poate fi "
        "observat prin comportament sau răspunsuri. Dacă l-ai manipula activ ca "
        "factor de intrare, ar deveni VI — în exemplul clasic din curs e rezultat."
    ),
    # 10997
    (
        "Înălțimea este variabilă continuă (valori reale în interval) și observată "
        "direct prin măsurare. Nu este discretă da/nu și nu e latentă doar prin "
        "autoraport verbal fără indicatori agreați."
    ),
    # 10998
    (
        "Măsurarea Stevens: reguli explicite, numere sau simboluri, legătură "
        "controlată între proprietate și reprezentare. Nu elimină definirea "
        "constructului — o completează cu proceduri de atribuire a valorilor."
    ),
    # 10999
    (
        "Datele empirice verifică sau infirma ipoteze în mod sistematic. Ele "
        "susțin concluzii după analiză, nu înlocuiesc observația inițială și "
        "nu justifică orice concluzie indiferent de design."
    ),
    # 11000
    (
        "Statistica organizează datele, nu le repară pe cele slabe; înțelegerea "
        "testelor reduce naivitatea; metoda trebuie să urmeze întrebarea, nu "
        "impresia tehnică. Ipotezele rămân necesare — statistica le evaluează, "
        "nu le face redundante."
    ),
] + SCALES_SAMPLING_EXPLANATIONS + FREQUENCY_EXPLANATIONS + CENTRAL_TENDENCY_EXPLANATIONS + BOXPLOT_EXPLANATIONS + DISPERSION_EXPLANATIONS + DISTRIBUTION_SHAPE_EXPLANATIONS + STANDARDIZED_SCORES_EXPLANATIONS + SAMPLING_DISTRIBUTION_EXPLANATIONS + HYPOTHESIS_Z_TEST_EXPLANATIONS + RECAP_RAPID_EXPLANATIONS


def attach_explanations(items: list) -> list:
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(STATISTICA_II_EXPLANATIONS):
            item["explanation"] = STATISTICA_II_EXPLANATIONS[i]
        out.append(item)
    return out


assert len(STATISTICA_II_EXPLANATIONS) == 265
