"""Explicații pedagogice — lot examen Psihologia dezvoltării II (490 itemi, IDs 10001–10490)."""

from __future__ import annotations

from typing import Dict, List, Any

from scripts.psihologia_dezvoltarii_ii_metode_explanations import (
    METODE_CERCETARE_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_teorii_explanations import (
    TEORII_INVATARII_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_senzorio_motor_explanations import (
    SENZORIO_MOTOR_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_limbaj_explanations import (
    LIMBAJ_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_atasament_explanations import (
    ATASAMENT_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_simbol_joc_explanations import (
    SIMBOL_JOC_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_scolaritate_explanations import (
    SCOLARITATE_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_adolescenta_explanations import (
    ADOLESCENTA_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_tinereete_explanations import (
    TINERETE_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_batranete_explanations import (
    BATRANETE_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_durere_explanations import (
    DURERE_EXPLANATIONS,
)
from scripts.psihologia_dezvoltarii_ii_autori_explanations import (
    AUTORI_CLASICI_EXPLANATIONS,
)
from scripts.explanation_prose import to_prose_explanation

Item = Dict[str, Any]

PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS: List[str] = [
    (
        "Adevărat. Dezvoltarea psihică îmbină simultan trei caracteristici: caracter unitar (dimensiunile cognitivă, emoțională și socială evoluează împreună, nu separat), caracter stadial (există etape calitativ distincte, recognoscibile și cu o ordine relativ constantă) și caracter individual (fiecare copil parcurge aceste etape în propriul ritm și cu propria viteză, fără a ajunge la un rezultat identic cu al celorlalți). Stadialitatea nu presupune că toți copiii ating o anumită etapă exact la aceeași lună sau an calendaristic, ci că ordinea etapelor este relativ constantă la nivel de specie. Caracterul individual înseamnă că doi copii de aceeași vârstă cronologică pot fi în etape psihologice diferite — ceea ce educatorul trebuie să recunoască și să respecte în practica sa."
    ),
    (
        "Procesul de dezvoltare psihică este descris prin patru trăsături esențiale care se completează reciproc: continuitate (achizițiile actuale se construiesc pe baza celor anterioare și le pregătesc pe cele viitoare), caracter individual (ritmul și viteza parcurgerii etapelor diferă de la copil la copil), sens direcțional (există o orientare generală spre complexitate și integrare, nu o simplă acumulare aleatoare de schimbări) și caracter stadial (există etape recognoscibile, cu structuri calitativ distincte). Nicio trăsătură nu o anulează pe cealaltă: continuitatea explică de ce un copil nu poate sări o etapă esențială, iar individualitatea explică de ce doi copii de aceeași vârstă cronologică pot arăta diferit în plan social-emoțional sau cognitiv."
    ),
    (
        "diferențele reflectă caracterul individual al ritmului de dezvoltare. Psihologia dezvoltării recunoaște că vârsta cronologică și vârsta psihologică nu coincid întotdeauna perfect: doi elevi de aceeași vârstă pot fi la niveluri diferite de maturitate emoțională sau cognitivă, deoarece fiecare individ parcurge etapele în propriul ritm, influențat de ereditate, mediu și experiențe personale unice."
    ),
    (
        "Fals. Deși etapele de dezvoltare psihică sunt recognoscibile și au o ordine relativ constantă, conținuturile finale la care ajunge fiecare individ diferă semnificativ în funcție de ereditate, mediu, educație și experiențe personale unice. Stadialitatea descrie ordinea și structura etapelor, nu uniformizarea rezultatelor. La finalul adolescenței, oamenii diferă considerabil prin personalitate, valori, abilități cognitive și emoționale, stil de relaționare și identitate — tocmai datorită caracterului individual al dezvoltării și interacțiunii cu medii diverse. A confunda stadialitatea cu identitatea perfectă a rezultatelor finale reprezintă o eroare frecventă în înțelegerea psihologiei dezvoltării, cu consecințe grave în practica educațională."
    ),
    (
        "Ideea că dezvoltarea are propria durată și propriul sens se referă la: faptul că schimbările actuale pregătesc achizițiile viitoare, deci există o logică internă a progresiei; faptul că există o direcție generală spre complexitate, integrare și autonomie crescândă; faptul că un copil poate parcurge o etapă mai rapid sau mai lent față de media grupului, fără ca aceasta să semnifice patologie."
    ),
    (
        "Spre deosebire de o lecție punctuală care adaugă o informație specifică, dezvoltarea psihică are caracter global — restructurează moduri de gândire, relaționare și acțiune în ansamblu, nu doar adaugă un element izolat — și caracter de durată — se construiește treptat pe parcursul mai multor ani, nu într-un singur moment sau eveniment. Înțelegerea acestei distincții ajută la evitarea confuziei dintre acumularea de cunoștințe și schimbarea structurală profundă a psihicului."
    ),
    (
        "Etapa reprezintă un tipar general de funcționare psihologică, recognoscibil la copiii dintr-un interval de vârstă, caracterizat prin achiziții calitative specifice; ritmul individual se referă la viteza sau durata cu care un anumit copil parcurge acea etapă. Etapa nu se reduce la o vârstă cronologică exactă, iar ritmul nu este uniform la toți copiii. Cele două concepte nu sunt sinonime, ci complementare — descriu aspecte diferite ale aceluiași proces. Individualitatea ritmului nu neagă existența etapelor comune."
    ),
    (
        "Succesiunea cooperare la joacă, negociere a regulilor, asumare a perspectivelor celorlalți ilustrează că dezvoltarea psihosocială urmează o direcție clară (de la comportamente concrete și egocentriste spre capacități abstracte și sociale complexe) și că fiecare achiziție o pregătește pe cea următoare — aceasta este esența caracterului stadial și direcționat."
    ),
    (
        "Ereditatea transmite potențial biologic și psihologic — predispoziții, tendințe, capacități de maturare — nu un traseu prestabilit în detaliu. Această „materie primă” are nevoie de maturare și de experiență adecvată pentru a se transforma în competențe reale și vizibile. Afirmațiile care fac mediul complet irelevant sau care exclud total influența experienței exagerează rolul eredității și contrazic perspectiva interacționistă din psihologia dezvoltării."
    ),
    (
        "Fals. Viziunea deterministă rigidă conform căreia ereditatea fixează complet traseul psihic este respinsă de psihologia contemporană a dezvoltării. Ereditatea furnizează un potențial sau o materie primă ce poate fi valorificată, amplificată sau limitată în funcție de condițiile de mediu, de calitatea relațiilor, de experiențele educaționale și de cultura în care trăiește individul. Studiile cu gemeni monozigoti crescuți în medii diferite arată că, deși există similarități genetice, experiența diferită produce diferențe semnificative în personalitate, abilități și comportament. Prin urmare, ereditatea stabilește tendințe și limite de timp pentru anumite achiziții, dar nu scrie în detaliu scenariul psihologic al unui individ — interacțiunea cu mediul și educația rămân decisive."
    ),
    (
        "Mediul, în sens larg, cuprinde totalitatea condițiilor externe în care se desfășoară dezvoltarea: condițiile naturale și fizice — climă, habitat, nutriție, spațiu de locuit; relațiile sociale și normele culturale — familie, grup de prieteni, instituții, valori comunitare; experiențele educaționale atât formale (grădiniță, școală) cât și informale — joc liber, interacțiuni cotidiene, media."
    ),
    (
        "Exemplul cu gemenele monozigote crescute în familii diferite ilustrează că potențialul genetic poate fi valorificat sau frânat în funcție de condițiile de mediu: deși au aptitudini cognitive similare, încrederea în sine s-a dezvoltat diferit datorită experiențelor familiale distincte. Totodată, explicația cea mai completă recunoaște că genele și mediul acționează împreună, nu separat — aceleași gene se exprimă diferit în contexte diferite."
    ),
    (
        "Un copil cu potențial lingvistic ridicat, dar expus foarte puțin la conversație, povești și lectură, nu va reuși să transforme acea predispoziție în competențe lingvistice reale — aceasta ilustrează cel mai clar modul în care absența stimulării din mediu poate bloca valorificarea unui potențial ereditar. Conceptul central este că ereditatea oferă potențialul, dar mediul decide dacă acel potențial devine competență vizibilă și funcțională."
    ),
    (
        "Ereditatea transmite tendințe și predispoziții, în timp ce mediul oferă ocazii concrete de exprimare sau limitare a acestora. Mediul poate amplifica o capacitate ereditară — prin stimulare, practică, modele — sau o poate reduce — prin privare senzorială, stres cronic sau absența ocaziilor. Nicio explicație completă a dezvoltării nu poate ignora nici ereditatea și nici mediul — ambii factori sunt necesari pentru a înțelege tabloul real."
    ),
    (
        "Potențialul ereditar pentru coordonarea motrică fină există ca predispoziție biologică, dar fără un mediu care să ofere materiale adecvate, modele și încurajare, acel potențial rămâne latent și nu se transformă în competență vizibilă, cum ar fi desenul sau scrisul."
    ),
    (
        "Educația, în sens pedagogic, se definește prin influență organizată, conștientă și sistematică asupra dezvoltării — spre deosebire de simpla expunere întâmplătoare la mediu, care nu implică intenție sau planificare. Totodată, educația valorifică potențialul ereditar prin structurarea experienței, prin exercițiu ghidat, feedback și progresie a dificultăților."
    ),
    (
        "Educația se distinge de simpla influență a mediului prin faptul că structurează experiența copilului într-un mod planificat și progresiv, urmând o logică pedagogică. De asemenea, valorifică aptitudinile ereditare prin exercițiu ghidat — un copil cu predispoziție pentru muzică se va dezvolta prin lecții structurate, nu doar prin expunere întâmplătoare. Educația reprezintă o formă deliberată de influență, cu obiective asumate de educator și evaluate în raport cu progresul copilului."
    ),
    (
        "Situația în care un copil este lăsat să descopere întâmplător, fără obiective, fără feedback și fără progresie planificată nu constituie educație în sens pedagogic, ci mai degrabă o influență generală, nestructurată a mediului."
    ),
    (
        "Practicile descrise — proiectarea activităților de la simplu la complex, oferirea de modele, corectarea erorilor și urmărirea obiectivelor clare — sunt caracteristice educației ca influență organizată și conștientă asupra dezvoltării."
    ),
    (
        "Educația creează contexte în care potențialul ereditar poate fi exprimat și transformat în competențe — un copil cu aptitudini matematice nu le va manifesta complet fără exercițiu ghidat și stimulare adecvată. Totodată, educația nu poate face orice din oricine: fără un minim de potențial sau fără atingerea maturității biologice necesare, chiar și educația de calitate are limite, dar poate susține progresul în mod semnificativ."
    ),
    (
        "Fals. Educația se distinge fundamental de influențele întâmplătoare ale mediului prin trei caracteristici esențiale: intenție — există scopuri pedagogice conștiente și asumate de educator; organizare — activitățile sunt structurate sistematic, cu resurse și metode gândite; și progresie — conținuturile avansează de la simplu la complex, în funcție de nivelul copilului. O simplă expunere la mediu — de exemplu, un copil care urmărește desene animate fără nicio îndrumare — poate oferi informații, dar nu constituie educație în sens pedagogic. Confundarea educației cu influența ambientală generală duce la subestimarea rolului pedagogiei în dezvoltarea psihică și la neglijarea importanței planificării didactice."
    ),
    (
        "Educația se diferențiază de simpla expunere la mediu prin organizare și intenție — educatorul știe de ce face ceea ce face și urmărește scopuri precise. Conținuturile urmează o logică pedagogică de sistematizare și progresie, nu sunt prezentate în mod aleator. Educatorul valorifică în mod conștient potențialul copilului, adaptând intervențiile la nevoile și resursele individuale."
    ),
    (
        "Jocul structurat, poveștile și regulile de grup stabilite de educator reprezintă o formă de educație organizată care urmărește explicit dezvoltarea emoțională a copilului: exprimarea adecvată a emoțiilor, gestionarea frustrărilor, cooperarea cu ceilalți."
    ),
    (
        "Perspectiva biologică pune accent pe maturarea internă a organismului ca principal factor explicativ al ritmului și ordinii etapelor de dezvoltare. Din această perspectivă, mediul are un rol secundar față de programul biologic de maturare, care pregătește treptat apariția unor noi competențe."
    ),
    (
        "Conform perspectivei biologice, există un program intern de maturare care pregătește treptat anumite competențe: creierul și sistemul nervos ating niveluri succesive de organizare biologică, permițând noi achiziții comportamentale și cognitive. Momentul debutului mersului independent sau al vorbirii articulate este corelat cu pregătirea biologică a organismului — nivelul de mielinizare nervoasă, forța musculară, maturarea centrilor cerebrali — nu doar cu imitarea."
    ),
    (
        "Afirmația că un copil nu poate însuși operații logice formale până când sistemul nervos nu atinge un anumit nivel de maturare — indiferent de cantitatea exercițiilor — reflectă accentul biologic pe maturarea internă ca precondție pentru anumite achiziții cognitive. Aceasta se aliniază și cu ideile piagetiene despre stadiile cognitive, care au o bază biologică și nu pot fi forțate artificial prin antrenament."
    ),
    (
        "O primă capcană frecventă în interpretarea perspectivei biologice este confundarea ei cu determinismul rigid: potențialul biologic nu echivalează cu un destin fix, nemodificabil de nicio experiență. O a doua capcană este credința că mediul nu contează deloc în viața reală a copilului — perspectiva biologică nuanțată recunoaște că potențialul are nevoie de un context minim pentru a se exprima. O a treia capcană este ignorarea completă a rolului maturării interne, ceea ce ar echivala cu negarea perspectivei biologice și cu o reducție ambientalistă."
    ),
    (
        "Faptul că percepția și reprezentarea perspectivei spațiale în desen apar abia după ce anumite structuri corticale ating maturitatea necesară ilustrează perspectiva biologică: maturarea internă a creierului pregătește apariția competenței perceptive și grafice."
    ),
    (
        "Afirmația că mediul este întotdeauna factorul principal, iar maturarea internă este neglijabilă, contrazice direct esența perspectivei biologice, care susține tocmai că programul intern de maturare are un rol central în explicarea ritmului și ordinii etapelor de dezvoltare. A identifica afirmația falsă dintr-un set presupune cunoașterea nu doar a ceea ce susține o perspectivă, ci și a ceea ce ea respinge în mod explicit."
    ),
    (
        "Perspectiva biologică pune accentul pe maturarea internă ca motor principal al ritmului etapelor, iar perspectiva ambientală pune accentul pe experiență, învățare și consecințele mediului. Perspectiva biologică vede mediul ca factor secundar în explicarea etapelor, în timp ce perspectiva ambientală îl consideră factorul central al schimbărilor comportamentale. Ambele perspective pot fi integrate într-o viziune interacționistă care recunoaște rolul ambilor factori și interacțiunea lor dinamică."
    ),
    (
        "Perspectiva biologică singură nu este suficientă pentru psihologia educației deoarece ignoră modul în care experiența, activitățile școlare și contextul educațional pot accelera sau încetini manifestarea competențelor în practică. Totodată, potențialul ereditar are nevoie de un context adecvat pentru a se actualiza: un copil cu predispoziții muzicale, de exemplu, nu va deveni muzician fără educație structurată și practică ghidată."
    ),
    (
        "Perspectiva ambientală (behavioristă) susține că experiența și învățarea modelează comportamentul: copilul este în mare parte ceea ce a trăit, practicat și experimentat în interacțiunea cu mediul. Recompensele și pedepsele sunt mecanisme centrale prin care mediul modifică frecvența și forma comportamentelor — condiționarea operantă descrisă de Skinner. Stimularea din mediu — obiecte, persoane, situații, limbaj — este considerată sursa principală a schimbărilor comportamentale."
    ),
    (
        "Perspectivele ambientale și behavioriste operează cu mecanisme de modificare a comportamentului prin factori externi: învățarea prin asociere și repetiție — conexiunile dintre stimuli și răspunsuri se consolidează prin practică sistematică; modificarea comportamentului prin recompense și pedepse — principiul condiționării operante; stimularea din mediu ca sursă principală de schimbare comportamentală — fără input extern adecvat, comportamentele dezirabile nu se formează."
    ),
    (
        "Exemplul descrie un proces tipic de condiționare operantă: comportamentul de împărțire a jucăriilor a crescut în frecvență datorită consecințelor pozitive (laude), ilustrând faptul că mediul social modifică comportamentul copilului prin consecințele pe care le produce. Laudele și pierderea privilegiilor sunt forme concrete de influență a mediului social asupra comportamentului, demonstrând că educatorii și părinții pot modela deliberat conduite dezirabile."
    ),
    (
        "Ideea că dezvoltarea ar exista identic fără nicio experiență postnatală este fundamentalmente falsă din perspectivă ambientală — și din orice perspectivă modernă — deoarece experiența postnatală modelează semnificativ comportamentul, cogniția, emoțiile și personalitatea. Cunoașterea acestei afirmații false ajută la înțelegerea corectă a limitelor reale ale perspectivei ambientale."
    ),
    (
        "Utilizarea recompenselor simbolice, a feedback-ului imediat și a repetiției ghidate pentru a forma un obicei de lectură reflectă principiile perspectivei ambientale: comportamentul este modelat prin consecințe pozitive și prin practică sistematică, până când devine automatizat. Aceasta corespunde condiționării operante și abordărilor behavioriste aplicate în educație."
    ),
    (
        "O limită importantă a perspectivei ambientale strict simplificate este că poate subestima rolul maturării biologice și al predispozițiilor ereditare în explicarea traseelor de dezvoltare individuale. De asemenea, poate ignora semnificația culturală a practicilor sociale și rolul limbajului interior în autoreglare și gândire — aspecte centrale în teoriile lui Vygotsky și Bruner. O altă limită este că riscă să reducă copilul la un organism pasiv, complet modelat din exterior, negând agentivitatea, gândirea internă și structurile cognitive proprii."
    ),
    (
        "Explicația că un copil devine anxios în situații sociale datorită criticilor repetate — nu datorită unei trăsături înnăscute — este tipică pentru perspectiva ambientală, care pune accentul pe experiența acumulată și pe modul în care mediul modelează emoțiile și comportamentul. Aceasta reflectă principiul condiționării clasice: o asociere repetată între situație socială și consecință negativă (critica dureroasă) creează treptat un răspuns emoțional conditionat de anxietate."
    ),
    (
        "Perspectiva ambientală operează cu trei mecanisme principale ale schimbării comportamentale: stimularea — mediul oferă ocazii de exercițiu, de contact cu materiale și de activare a comportamentelor potențiale; recompensa — consecințe plăcute sau valoroase care cresc probabilitatea ca un comportament să fie repetat; pedeapsa — consecințe neplăcute care reduc frecvența unui comportament nedorit."
    ),
    (
        "Adevărat. Perspectiva interacționistă reprezintă o viziune integrativă care depășește opoziția simplistă dintre ereditate și mediu, susținând că ambii factori acționează simultan și se influențează reciproc în mod dinamic pe toată durata vieții. Nu există un moment în care numai genele contează și mediul este neutru, sau invers: interacțiunea este permanentă și subtilă. Această perspectivă explică, de exemplu, de ce gemeni identici crescuți în contexte diferite pot ajunge la personalități distincte, sau de ce copii cu ereditate diferită pot atinge niveluri similare de competență în condiții educaționale echivalente. Psihologia educației moderne se fundamentează în mare parte pe această viziune interacționistă, care justifică intervenția pedagogică fără a nega rolul biologic."
    ),
    (
        "Perspectiva interacționistă susține că același potențial ereditar se poate manifesta diferit în medii diferite, ceea ce explică variabilitatea comportamentului și competențelor chiar și la copiii cu predispoziții similare. Experiența educațională, calitatea relațiilor și stimularea pot amplifica sau limita aptitudinile înnăscute — rezultatul depinde de combinația specifică ereditate-mediu trăită de fiecare individ. O explicație completă și riguroasă a dezvoltării necesită luarea în considerare a ambilor factori, nu a unuia exclusiv."
    ),
    (
        "Exemplul cu copilul cu temperament reactiv ilustrează un mecanism central al perspectivei interacționiste: o predispoziție temperamentală — probabil cu baze ereditare — produce efecte complet diferite în funcție de calitatea mediului educațional cu care interacționează. Același temperament reactiv devine sursă de anxietate în medii punitive și imprevizibile, dar se transformă în adaptare funcțională în medii calde și previzibile. Aceasta dovedește că nici temperamentul singur și nici mediul singur nu explică rezultatul — ci interacțiunea lor specifică."
    ),
    (
        "Determinismul genetic total — care afirmă că mediul este simplu decor, fără influență reală asupra traseului de dezvoltare — este incompatibil cu perspectiva interacționistă, deoarece aceasta atribuie mediului un rol esențial. Tabula rasa absolută — care afirmă că individul se naște complet neprogramat și că numai mediul îl formează — este la fel de incompatibilă, deoarece interacționismul recunoaște potențialul ereditar ca punct real de plecare."
    ),
    (
        "Perspectiva interacționistă este valoroasă în practica școlară deoarece evită atât fatalismul genetic — nu mai spunem că un copil nu poate progresa deoarece nu are genele potrivite — cât și neglijarea mediului — nu mai considerăm că mediul decide totul și că ereditatea nu contează. Permite adaptarea educației la potențialul real și la nevoile specifice ale fiecărui copil, înțelegând că există combinații unice de factori biologici și de mediu. Susține intervenții diferențiate și personalizate, în loc de un singur tipar educațional aplicat uniform tuturor."
    ),
    (
        "Metafora „genele deschid uși, mediul decide prin care treci» exprimă esența perspectivei interacționiste: ereditatea stabilește posibilități, tendințe și limite — nu certitudini — iar mediul, experiența și educația activează, orientează sau inhibă acele posibilități."
    ),
    (
        "Perspectiva culturală, reprezentată de Vygotsky și Bruner, susține că limbajul, valorile, simbolurile și interacțiunea socială mediată cultural modelează în profunzime modul în care se construiește cogniția și comportamentul uman. Din această perspectivă, nu există dezvoltare cognitivă autentică în absența participării la practici culturale specifice, a uneltelor cognitive transmise de comunitate și a ghidării oferite de adulți sau parteneri mai competenți."
    ),
    (
        "Perspectiva culturală susține că gândirea și cogniția se construiesc prin participare activă la practici sociale specifice culturii — matematică, limbaj, artă, ritualuri, meserii — nu prin maturare biologică izolată. Limbajul este văzut de Vygotsky ca unealtă fundamentală ce mediază atât comunicarea interpersonală, cât și gândirea interioară — vorbirea interiorizată devine instrument al autoreglării cognitive. Adultul sau partenerul mai competent poate ghida copilul în zona proximală de dezvoltare, sprijinindu-l să atingă niveluri pe care nu le-ar putea atinge singur."
    ),
    (
        "Conceptul vygotskian de zonă proximală de dezvoltare (ZPD) descrie exact distanța dintre ceea ce copilul poate realiza singur în prezent și ceea ce poate realiza cu sprijinul unui partener mai competent. Exemplul — rezolvarea problemei cu ajutorul colegului avansat, urmată de reușita ulterioară independentă — ilustrează perfect modul în care interacțiunea socială mediată extinde competența cognitivă actuală, transformând zona proximală de azi în nivelul independent de mâine."
    ),
    (
        "Bruner a propus că învățarea urmează trei moduri succesive de reprezentare: enactiv (prin acțiune directă și manipulare), iconic (prin imagini și scheme perceptive) și simbolic (prin limbaj și simboluri abstracte) — ceea ce explică progresia naturală de la concret la abstract în educație. El a subliniat că orice cultură oferă unelte cognitive — limbaj, narațiune, sisteme de notație, instituții — transmise noilor generații prin interacțiune socială. Educația poate și trebuie să organizeze experiența în forme accesibile vârstei și nivelului copilului — principiul scaffolding-ului, adică sprijinul gradual retras pe măsura dobândirii competenței."
    ),
    (
        "Perspectiva biologică pune în centru maturarea internă a organismului, iar perspectiva ambientală pune în centru experiența, consecințele și stimularea din mediu. Perspectiva interacționistă integrează ereditatea și mediul ca factori co-determinanți care interacționează permanent, iar perspectiva culturală adaugă limbajul, practicile sociale și transmisia culturală ca motoare ale dezvoltării cognitive superioare. Toate patru perspectivele pot fi recunoscute și diferențiate după factorul pe care îl plasează în centrul explicației: maturare biologică, experiență de mediu, interacțiunea ereditate-mediu sau respectiv cultura și limbajul."
    )
]

PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(METODE_CERCETARE_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(TEORII_INVATARII_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(SENZORIO_MOTOR_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(LIMBAJ_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(ATASAMENT_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(SIMBOL_JOC_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(SCOLARITATE_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(ADOLESCENTA_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(TINERETE_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(BATRANETE_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(DURERE_EXPLANATIONS)
PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS.extend(AUTORI_CLASICI_EXPLANATIONS)

assert len(PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS) == 490


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (10001–10490)."""
    if 10001 <= int(item_id) <= 10490:
        idx = int(item_id) - 10001
        if 0 <= idx < len(PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS):
            return to_prose_explanation(PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS[idx])
    return ""


def attach_explanations(items: List[Item]) -> List[Item]:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out: List[Item] = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS):
            item["explanation"] = to_prose_explanation(
                PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS[i]
            )
        out.append(item)
    return out
