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

Item = Dict[str, Any]

PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS: List[str] = [
    # —— 10001 — Natura dezvoltării: unitar, stadial, individual (TF Adevărat) ——
    (
        "Adevărat. Dezvoltarea psihică îmbină simultan trei caracteristici: "
        "caracter unitar (dimensiunile cognitivă, emoțională și socială evoluează "
        "împreună, nu separat), caracter stadial (există etape calitativ distincte, "
        "recognoscibile și cu o ordine relativ constantă) și caracter individual "
        "(fiecare copil parcurge aceste etape în propriul ritm și cu propria viteză, "
        "fără a ajunge la un rezultat identic cu al celorlalți). "
        "Stadialitatea nu presupune că toți copiii ating o anumită etapă exact la "
        "aceeași lună sau an calendaristic, ci că ordinea etapelor este relativ "
        "constantă la nivel de specie. "
        "Caracterul individual înseamnă că doi copii de aceeași vârstă cronologică "
        "pot fi în etape psihologice diferite — ceea ce educatorul trebuie să "
        "recunoască și să respecte în practica sa."
    ),
    # —— 10002 — Trăsăturile procesului de dezvoltare psihică (Multi ABCD) ——
    (
        "✅ a, ✅ b, ✅ c, ✅ d — toate variantele sunt corecte. "
        "Procesul de dezvoltare psihică este descris prin patru trăsături esențiale "
        "care se completează reciproc: continuitate (achizițiile actuale se "
        "construiesc pe baza celor anterioare și le pregătesc pe cele viitoare), "
        "caracter individual (ritmul și viteza parcurgerii etapelor diferă de la "
        "copil la copil), sens direcțional (există o orientare generală spre "
        "complexitate și integrare, nu o simplă acumulare aleatoare de schimbări) "
        "și caracter stadial (există etape recognoscibile, cu structuri calitativ "
        "distincte). "
        "Nicio trăsătură nu o anulează pe cealaltă: continuitatea explică de ce un "
        "copil nu poate sări o etapă esențială, iar individualitatea explică de ce "
        "doi copii de aceeași vârstă cronologică pot arăta diferit în plan "
        "social-emoțional sau cognitiv."
    ),
    # —— 10003 — Diferențe individuale la aceeași vârstă cronologică (Multi B) ——
    (
        "✅ b — diferențele reflectă caracterul individual al ritmului de dezvoltare. "
        "Psihologia dezvoltării recunoaște că vârsta cronologică și vârsta psihologică "
        "nu coincid întotdeauna perfect: doi elevi de aceeași vârstă pot fi la "
        "niveluri diferite de maturitate emoțională sau cognitivă, deoarece fiecare "
        "individ parcurge etapele în propriul ritm, influențat de ereditate, mediu "
        "și experiențe personale unice. "
        "Varianta a este incorectă deoarece diferențele individuale sunt perfect "
        "compatibile cu stadialitatea — ele nu o neagă. "
        "Varianta c este incorectă deoarece reduce explicația la un singur factor "
        "(ereditatea), ignorând rolul experienței. "
        "Varianta d implică absența totală a dezvoltării la unul dintre elevi, ceea "
        "ce nu este susținut de teorie și ar constitui o eroare gravă de interpretare "
        "pedagogică."
    ),
    # —— 10004 — Toți copiii ajung identici la adolescență (TF Fals) ——
    (
        "Fals. Deși etapele de dezvoltare psihică sunt recognoscibile și au o ordine "
        "relativ constantă, conținuturile finale la care ajunge fiecare individ diferă "
        "semnificativ în funcție de ereditate, mediu, educație și experiențe personale "
        "unice. "
        "Stadialitatea descrie ordinea și structura etapelor, nu uniformizarea "
        "rezultatelor. "
        "La finalul adolescenței, oamenii diferă considerabil prin personalitate, "
        "valori, abilități cognitive și emoționale, stil de relaționare și "
        "identitate — tocmai datorită caracterului individual al dezvoltării și "
        "interacțiunii cu medii diverse. "
        "A confunda stadialitatea cu identitatea perfectă a rezultatelor finale "
        "reprezintă o eroare frecventă în înțelegerea psihologiei dezvoltării, cu "
        "consecințe grave în practica educațională."
    ),
    # —— 10005 — Propria durată și propriul sens al dezvoltării (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "Ideea că dezvoltarea are propria durată și propriul sens se referă la: "
        "faptul că schimbările actuale pregătesc achizițiile viitoare, deci există "
        "o logică internă a progresiei (varianta a); faptul că există o direcție "
        "generală spre complexitate, integrare și autonomie crescândă (varianta b); "
        "faptul că un copil poate parcurge o etapă mai rapid sau mai lent față de "
        "media grupului, fără ca aceasta să semnifice patologie (varianta c). "
        "Varianta d este falsă deoarece durata etapelor nu este fixată biologic la "
        "aceleași luni pentru fiecare copil — tocmai individualitatea ritmului este "
        "trăsătura definitorie care distinge psihologia dezvoltării de o schemă "
        "rigidă, calendaristică."
    ),
    # —— 10006 — Dezvoltarea față de învățarea punctuală (Multi AB) ——
    (
        "✅ a, ✅ b — variantele corecte; ❌ c și ❌ d sunt incorecte. "
        "Spre deosebire de o lecție punctuală care adaugă o informație specifică, "
        "dezvoltarea psihică are caracter global — restructurează moduri de gândire, "
        "relaționare și acțiune în ansamblu, nu doar adaugă un element izolat "
        "(varianta a) — și caracter de durată — se construiește treptat pe parcursul "
        "mai multor ani, nu într-un singur moment sau eveniment (varianta b). "
        "Varianta c este greșită deoarece dezvoltarea implică tocmai continuitate cu "
        "experiențele anterioare, pe care le valorifică și le integrează. "
        "Varianta d este greșită deoarece mediul are un rol esențial în modelarea "
        "dezvoltării. "
        "Înțelegerea acestei distincții ajută la evitarea confuziei dintre acumularea "
        "de cunoștințe și schimbarea structurală profundă a psihicului."
    ),
    # —— 10007 — Distincție etapă vs. ritm individual (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Etapa reprezintă un tipar general de funcționare psihologică, recognoscibil "
        "la copiii dintr-un interval de vârstă, caracterizat prin achiziții calitative "
        "specifice; ritmul individual se referă la viteza sau durata cu care un "
        "anumit copil parcurge acea etapă. "
        "Varianta b este greșită deoarece etapa nu se reduce la o vârstă cronologică "
        "exactă, iar ritmul nu este uniform la toți copiii — ceea ce face varianta b "
        "o contrazicere a caracterului individual al dezvoltării. "
        "Varianta c este greșită deoarece cele două concepte nu sunt sinonime, ci "
        "complementare — ele descriu aspecte diferite ale aceluiași proces. "
        "Varianta d este greșită deoarece individualitatea ritmului nu neagă "
        "existența etapelor comune, ambele coexistând ca adevăruri ale psihologiei "
        "dezvoltării."
    ),
    # —— 10008 — Succesiunea psihosocială: cooperare, negociere, perspectivare (Multi B) ——
    (
        "✅ b — singura variantă corectă. "
        "Succesiunea cooperare la joacă, negociere a regulilor, asumare a "
        "perspectivelor celorlalți ilustrează că dezvoltarea psihosocială urmează "
        "o direcție clară (de la comportamente concrete și egocentriste spre "
        "capacități abstracte și sociale complexe) și că fiecare achiziție o "
        "pregătește pe cea următoare — aceasta este esența caracterului stadial și "
        "direcționat. "
        "Varianta a este falsă deoarece tocmai succesiunea logică demonstrează "
        "continuitatea, nu absența ei. "
        "Varianta c este incorectă deoarece mediul social — familia, grupul de "
        "prieteni, școala — joacă un rol central în această succesiune. "
        "Varianta d este incorectă deoarece copiii nu trec prin aceste etape la "
        "vârste identice, tocmai datorită caracterului individual al ritmului de "
        "dezvoltare."
    ),
    # —— 10009 — Ereditatea: potențial, nu destin fix (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Ereditatea transmite un potențial biologic și psihologic — predispoziții, "
        "tendințe, capacități de maturare — nu un traseu prestabilit în detaliu "
        "(varianta a). "
        "Această materie primă are nevoie de maturare și de experiență adecvată "
        "pentru a se transforma în competențe reale și vizibile (varianta b). "
        "Ereditatea și mediul nu sunt opuși absoluti care se exclud reciproc, ci "
        "factori care interacționează permanent în mod dinamic (varianta d). "
        "Varianta c este falsă deoarece una dintre ideile centrale ale psihologiei "
        "contemporane este tocmai că nici ereditatea și nici mediul singure nu pot "
        "explica complet tabloul dezvoltării individuale."
    ),
    # —— 10010 — Ereditatea determină rigid traseul dezvoltării (TF Fals) ——
    (
        "Fals. Viziunea deterministă rigidă conform căreia ereditatea fixează complet "
        "traseul psihic este respinsă de psihologia contemporană a dezvoltării. "
        "Ereditatea furnizează un potențial sau o materie primă ce poate fi "
        "valorificată, amplificată sau limitată în funcție de condițiile de mediu, "
        "de calitatea relațiilor, de experiențele educaționale și de cultura în care "
        "trăiește individul. "
        "Studiile cu gemeni monozigoti crescuți în medii diferite arată că, deși "
        "există similarități genetice, experiența diferită produce diferențe "
        "semnificative în personalitate, abilități și comportament. "
        "Prin urmare, ereditatea stabilește tendințe și limite de timp pentru "
        "anumite achiziții, dar nu scrie în detaliu scenariul psihologic al unui "
        "individ — interacțiunea cu mediul și educația rămân decisive."
    ),
    # —— 10011 — Mediul include condiții naturale, sociale, educaționale (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "Mediul, în sens larg, cuprinde totalitatea condițiilor externe în care se "
        "desfășoară dezvoltarea: condițiile naturale și fizice — climă, habitat, "
        "nutriție, spațiu de locuit (varianta a); relațiile sociale și normele "
        "culturale — familie, grup de prieteni, instituții, valori comunitare "
        "(varianta b); experiențele educaționale atât formale (grădiniță, școală) "
        "cât și informale — joc liber, interacțiuni cotidiene, media (varianta c). "
        "Varianta d este fundamental greșită deoarece genele aparțin eredității, "
        "nu mediului — această distincție conceptuală este esențială: ereditatea "
        "vine dinlăuntru, mediul vine din afară, chiar dacă interacțiunea lor este "
        "permanentă și subtilă."
    ),
    # —— 10012 — Gemene monozigote în familii diferite (Multi BD) ——
    (
        "✅ b, ✅ d — variantele corecte; ❌ a și ❌ c sunt incorecte. "
        "Exemplul cu gemenele monozigote crescute în familii diferite ilustrează că "
        "potențialul genetic poate fi valorificat sau frânat în funcție de condițiile "
        "de mediu: deși au aptitudini cognitive similare, încrederea în sine s-a "
        "dezvoltat diferit datorită experiențelor familiale distincte (varianta b). "
        "Totodată, explicația cea mai completă recunoaște că genele și mediul "
        "acționează împreună, nu separat — aceleași gene se exprimă diferit în "
        "contexte diferite (varianta d). "
        "Varianta a este greșită deoarece tocmai diferențele dintre gemene "
        "demonstrează că mediul contează. "
        "Varianta c este greșită deoarece a nega complet ereditatea ar contrazice "
        "similitudinile cognitive observate între cele două surori."
    ),
    # —— 10013 — Mediul blochează: potențial lingvistic fără stimulare (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Un copil cu potențial lingvistic ridicat, dar expus foarte puțin la "
        "conversație, povești și lectură, nu va reuși să transforme acea predispoziție "
        "în competențe lingvistice reale — aceasta ilustrează cel mai clar modul în "
        "care absența stimulării din mediu poate bloca valorificarea unui potențial "
        "ereditar. "
        "Variantele b, c și d descriu situații în care mediul este stimulativ și "
        "susținător — grădiniță cu activități variate, mentorat, atenție emoțională "
        "— deci nu ilustrează blocarea, ci favorizarea dezvoltării. "
        "Conceptul central este că ereditatea oferă potențialul, dar mediul decide "
        "dacă acel potențial devine competență vizibilă și funcțională."
    ),
    # —— 10014 — Distincții corecte ereditate / mediu (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Ereditatea transmite tendințe și predispoziții, în timp ce mediul oferă "
        "ocazii concrete de exprimare sau limitare a acestora (varianta a). "
        "Mediul poate amplifica o capacitate ereditară — prin stimulare, practică, "
        "modele — sau o poate reduce — prin privare senzorială, stres cronic sau "
        "absența ocaziilor (varianta b). "
        "Nicio explicație completă a dezvoltării nu poate ignora nici ereditatea și "
        "nici mediul — ambii factori sunt necesari pentru a înțelege tabloul real "
        "(varianta d). "
        "Varianta c este falsă deoarece ereditatea și mediul nu sunt mereu în "
        "opoziție totală: perspectiva interacționistă tocmai descrie interdependența "
        "lor dinamică."
    ),
    # —— 10015 — Potențial motric fin fără materiale sau încurajare (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Potențialul ereditar pentru coordonarea motrică fină există ca predispoziție "
        "biologică, dar fără un mediu care să ofere materiale adecvate, modele și "
        "încurajare, acel potențial rămâne latent și nu se transformă în competență "
        "vizibilă, cum ar fi desenul sau scrisul (varianta a). "
        "Varianta b este falsă deoarece ereditatea nu garantează automat performanța "
        "în absența practicii și a contextului favorabil — potențialul nu este "
        "competență. "
        "Varianta c exagerează în sens opus, reducând totul la mediu și negând "
        "contribuția reală a predispozițiilor ereditare. "
        "Varianta d este falsă deoarece cercetările arată că dezvoltarea motrică "
        "depinde atât de maturarea biologică, cât și de practicarea activă și de "
        "stimularea oferită de mediu."
    ),
    # —— 10016 — Educația: influență organizată, conștientă, sistematică (Multi AB) ——
    (
        "✅ a, ✅ b — variantele corecte; ❌ c și ❌ d sunt incorecte. "
        "Educația, în sens pedagogic, se definește prin influență organizată, "
        "conștientă și sistematică asupra dezvoltării — spre deosebire de simpla "
        "expunere întâmplătoare la mediu, care nu implică intenție sau planificare "
        "(varianta a). "
        "Totodată, educația valorifică potențialul ereditar prin structurarea "
        "experienței, prin exercițiu ghidat, feedback și progresie a dificultăților "
        "(varianta b). "
        "Varianta c este greșită deoarece nu orice influență din mediu este educație "
        "— aceasta din urmă implică întotdeauna intenție și plan pedagogic. "
        "Varianta d este greșită deoarece educația nu poate elimina sau înlocui "
        "maturarea biologică, ci o acompaniază și o valorifică în momentele optime."
    ),
    # —— 10017 — Rolul educației în dezvoltare (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Educația se distinge de simpla influență a mediului prin faptul că "
        "structurează experiența copilului într-un mod planificat și progresiv, "
        "urmând o logică pedagogică (varianta a). "
        "De asemenea, valorifică aptitudinile ereditare prin exercițiu ghidat — "
        "un copil cu predispoziție pentru muzică se va dezvolta prin lecții "
        "structurate, nu doar prin expunere întâmplătoare (varianta b). "
        "Educația reprezintă o formă deliberată de influență, cu obiective asumate "
        "de educator și evaluate în raport cu progresul copilului (varianta d). "
        "Varianta c este falsă: educația nu înlocuiește maturarea biologică — nu "
        "poți preda operații formale unui copil care nu a atins nivelul cognitiv "
        "corespunzător, oricât de bine ai planifica lecția."
    ),
    # —— 10018 — Copilul lasă să învețe singur întâmplător (Multi B) ——
    (
        "✅ b — singura variantă corectă. "
        "Situația în care un copil este lăsat să descopere întâmplător, fără "
        "obiective, fără feedback și fără progresie planificată nu constituie "
        "educație în sens pedagogic, ci mai degrabă o influență generală, "
        "nestructurată a mediului (varianta b). "
        "Varianta a este incorectă deoarece educația pedagogică presupune tocmai "
        "elementele absente din situația descrisă: intenție, organizare, obiective, "
        "sistematizare. "
        "Varianta c este incorectă deoarece valorificarea sistematică a potențialului "
        "ereditar presupune structurare și ghidare, care lipsesc. "
        "Varianta d este incorectă deoarece o intervenție conștientă implică scop "
        "explicit și monitorizarea progresului — caracteristici absente în scenariul "
        "descris."
    ),
    # —— 10019 — Profesorul planifică progresiv, oferă modele, evaluează (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Practicile descrise — proiectarea activităților de la simplu la complex, "
        "oferirea de modele, corectarea erorilor și urmărirea obiectivelor clare — "
        "sunt caracteristice educației ca influență organizată și conștientă asupra "
        "dezvoltării (varianta a). "
        "Varianta b este incorectă deoarece educația nu se reduce la ereditate, care "
        "este un factor intern și biologic, nu o practică pedagogică. "
        "Varianta c este incorectă deoarece mediul natural necontrolat nu implică "
        "proiectare didactică — tocmai caracterul deliberat al activităților descrise "
        "le diferențiază de influențele accidentale ale ambientului. "
        "Varianta d este incorectă deoarece maturarea biologică este un proces intern "
        "care nu necesită și nu poate fi înlocuit de planificarea lecțiilor."
    ),
    # —— 10020 — Relația educație, ereditate și dezvoltare (Multi AC) ——
    (
        "✅ a, ✅ c — variantele corecte; ❌ b și ❌ d sunt incorecte. "
        "Educația creează contexte în care potențialul ereditar poate fi exprimat "
        "și transformat în competențe — un copil cu aptitudini matematice nu le "
        "va manifesta complet fără exercițiu ghidat și stimulare adecvată (varianta a). "
        "Totodată, educația nu poate face orice din oricine: fără un minim de "
        "potențial sau fără atingerea maturității biologice necesare, chiar și "
        "educația de calitate are limite, dar poate susține progresul în mod "
        "semnificativ (varianta c). "
        "Varianta b este falsă: educația de calitate tocmai ține cont de "
        "individualitatea și potențialul unic al fiecărui copil. "
        "Varianta d este falsă: educația este o formă deliberată de influență, "
        "distinctă de influențele întâmplătoare și nestructurate ale mediului."
    ),
    # —— 10021 — Educația este influență întâmplătoare (TF Fals) ——
    (
        "Fals. Educația se distinge fundamental de influențele întâmplătoare ale "
        "mediului prin trei caracteristici esențiale: intenție — există scopuri "
        "pedagogice conștiente și asumate de educator; organizare — activitățile "
        "sunt structurate sistematic, cu resurse și metode gândite; și progresie — "
        "conținuturile avansează de la simplu la complex, în funcție de nivelul "
        "copilului. "
        "O simplă expunere la mediu — de exemplu, un copil care urmărește desene "
        "animate fără nicio îndrumare — poate oferi informații, dar nu constituie "
        "educație în sens pedagogic. "
        "Confundarea educației cu influența ambientală generală duce la "
        "subestimarea rolului pedagogiei în dezvoltarea psihică și la neglijarea "
        "importanței planificării didactice."
    ),
    # —— 10022 — Caracteristici definitorii ale educației față de mediu (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Educația se diferențiază de simpla expunere la mediu prin organizare și "
        "intenție — educatorul știe de ce face ceea ce face și urmărește scopuri "
        "precise (varianta a). "
        "Conținuturile urmează o logică pedagogică de sistematizare și progresie, "
        "nu sunt prezentate în mod aleator (varianta b). "
        "Educatorul valorifică în mod conștient potențialul copilului, adaptând "
        "intervențiile la nevoile și resursele individuale (varianta d). "
        "Varianta c este falsă deoarece tocmai prezența unui obiectiv asumat de "
        "adult este ceea ce definește educația și o separă de influențele "
        "accidentale ale ambientului."
    ),
    # —— 10023 — Grădinița: joc structurat, emoții, reguli de grup (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Jocul structurat, poveștile și regulile de grup stabilite de educator "
        "reprezintă o formă de educație organizată care urmărește explicit "
        "dezvoltarea emoțională a copilului: exprimarea adecvată a emoțiilor, "
        "gestionarea frustrărilor, cooperarea cu ceilalți (varianta a). "
        "Varianta b este incorectă deoarece tocmai implicarea activă și ghidarea "
        "educatorului sunt elementele centrale care conferă activității caracter "
        "educativ. "
        "Varianta c este incorectă deoarece exemplul nu ilustrează determinism "
        "genetic, ci intervenție pedagogică deliberată. "
        "Varianta d este falsă deoarece jocul de grup implică interacțiune socială "
        "intensă și susținută, nu absența influenței sociale."
    ),
    # —— 10024 — Perspectiva biologică: maturare internă, mediu secundar (Multi AB) ——
    (
        "✅ a, ✅ b — variantele corecte; ❌ c și ❌ d sunt incorecte. "
        "Perspectiva biologică pune accent pe maturarea internă a organismului ca "
        "principal factor explicativ al ritmului și ordinii etapelor de dezvoltare "
        "(varianta a). "
        "Din această perspectivă, mediul are un rol secundar față de programul "
        "biologic de maturare, care pregătește treptat apariția unor noi competențe "
        "(varianta b). "
        "Varianta c este greșită deoarece perspectiva biologică nu exclude complet "
        "rolul mediului, ci îl plasează pe un plan secundar față de maturarea internă. "
        "Varianta d este greșită deoarece perspectiva biologică tocmai recunoaște "
        "existența etapelor recognoscibile ca efect al maturării sistematice a "
        "sistemului nervos."
    ),
    # —— 10025 — Program intern de maturare; debut mers și vorbire (Multi AB) ——
    (
        "✅ a, ✅ b — variantele corecte; ❌ c și ❌ d sunt incorecte. "
        "Conform perspectivei biologice, există un program intern de maturare care "
        "pregătește treptat anumite competențe: creierul și sistemul nervos ating "
        "niveluri succesive de organizare biologică, permițând noi achiziții "
        "comportamentale și cognitive (varianta a). "
        "Momentul debutului mersului independent sau al vorbirii articulate este "
        "corelat cu pregătirea biologică a organismului — nivelul de mielinizare "
        "nervoasă, forța musculară, maturarea centrilor cerebrali — nu doar cu "
        "imitarea (varianta b). "
        "Varianta c este incorectă deoarece perspectiva biologică plasează tocmai "
        "maturarea internă, nu mediul, ca factor principal. "
        "Varianta d este incorectă deoarece perspectiva biologică recunoaște că "
        "vârsta biologică influențează semnificativ capacitățile cognitive disponibile."
    ),
    # —— 10026 — Operații logice formale condiționate de maturarea SN (Multi C) ——
    (
        "✅ c — singura variantă corectă. "
        "Afirmația că un copil nu poate însuși operații logice formale până când "
        "sistemul nervos nu atinge un anumit nivel de maturare — indiferent de "
        "cantitatea exercițiilor — reflectă accentul biologic pe maturarea internă "
        "ca precondție pentru anumite achiziții cognitive (varianta c). "
        "Aceasta se aliniază și cu ideile piagetiene despre stadiile cognitive, "
        "care au o bază biologică și nu pot fi forțate artificial prin antrenament. "
        "Varianta a este incorectă deoarece perspectiva interacționistă ar acorda "
        "un rol important atât eredității, cât și mediului, fără a insista pe "
        "limitele absolute ale maturării biologice. "
        "Varianta b este incorectă deoarece perspectiva culturală (Vygotsky) ar "
        "pune accentul pe limbaj și interacțiunea socială ca motoare ale gândirii. "
        "Varianta d este incorectă deoarece behaviorismul ar explica totul prin "
        "recompense și pedepse, fără referire la maturarea biologică."
    ),
    # —— 10027 — Capcane în înțelegerea perspectivei biologice (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "O primă capcană frecventă în interpretarea perspectivei biologice este "
        "confundarea ei cu determinismul rigid: potențialul biologic nu echivalează "
        "cu un destin fix, nemodificabil de nicio experiență (varianta a). "
        "O a doua capcană este credința că mediul nu contează deloc în viața reală "
        "a copilului — perspectiva biologică nuanțată recunoaște că potențialul are "
        "nevoie de un context minim pentru a se exprima (varianta b). "
        "O a treia capcană este ignorarea completă a rolului maturării interne, "
        "ceea ce ar echivala cu negarea perspectivei biologice și cu o reducție "
        "ambientalistă (varianta c). "
        "Varianta d nu este o capcană, ci o afirmație justă: organismul pune în "
        "mod real anumite limite de timp pentru apariția unor competențe, și "
        "recunoașterea acestui fapt este corectă."
    ),
    # —— 10028 — Perspectivă spațială în desen și maturare corticală (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Faptul că percepția și reprezentarea perspectivei spațiale în desen apar "
        "abia după ce anumite structuri corticale ating maturitatea necesară "
        "ilustrează perspectiva biologică: maturarea internă a creierului pregătește "
        "apariția competenței perceptive și grafice (varianta a). "
        "Varianta b este incorectă deoarece pedeapsa ca unic mecanism de schimbare "
        "reprezintă o caricatură behavioristă, nu o explicație valabilă a apariției "
        "perspectivei spațiale în desen. "
        "Varianta c este incorectă deoarece exemplul nu neagă rolul educației, ci "
        "sugerează că există o condiție biologică prealabilă care face posibilă "
        "beneficierea de acea educație. "
        "Varianta d este incorectă deoarece exemplul tocmai ilustrează existența "
        "etapelor în dezvoltare, nu negarea lor."
    ),
    # —— 10029 — Afirmație falsă despre perspectiva biologică (Multi A) ——
    (
        "✅ a — aceasta este afirmația falsă despre perspectiva biologică. "
        "Afirmația că mediul este întotdeauna factorul principal, iar maturarea "
        "internă este neglijabilă, contrazice direct esența perspectivei biologice, "
        "care susține tocmai că programul intern de maturare are un rol central în "
        "explicarea ritmului și ordinii etapelor de dezvoltare. "
        "Variantele b, c și d sunt afirmații corecte despre această perspectivă: "
        "există un program intern de maturare biologic (b), debutul unor competențe "
        "este corelat cu pregătirea organismului (c), iar potențialul ereditar nu "
        "înseamnă un destin fix și nemodificabil (d). "
        "A identifica afirmația falsă dintr-un set presupune cunoașterea nu doar "
        "a ceea ce susține o perspectivă, ci și a ceea ce ea respinge în mod explicit."
    ),
    # —— 10030 — Opoziție perspectivă biologică vs. ambientală (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Perspectiva biologică pune accentul pe maturarea internă ca motor principal "
        "al ritmului etapelor, iar perspectiva ambientală pune accentul pe experiență, "
        "învățare și consecințele mediului (varianta a). "
        "Perspectiva biologică vede mediul ca factor secundar în explicarea "
        "etapelor, în timp ce perspectiva ambientală îl consideră factorul central "
        "al schimbărilor comportamentale (varianta b). "
        "Ambele perspective pot fi integrate într-o viziune interacționistă care "
        "recunoaște rolul ambilor factori și interacțiunea lor dinamică (varianta d). "
        "Varianta c inversează greșit cele două perspective: perspectiva biologică "
        "nu se bazează pe recompense — acestea aparțin perspectivei ambientale; "
        "iar perspectiva ambientală nu susține că totul este genetic."
    ),
    # —— 10031 — Limitele perspectivei biologice în psihologia educației (Multi AC) ——
    (
        "✅ a, ✅ c — variantele corecte; ❌ b și ❌ d sunt incorecte. "
        "Perspectiva biologică singură nu este suficientă pentru psihologia educației "
        "deoarece ignoră modul în care experiența, activitățile școlare și contextul "
        "educațional pot accelera sau încetini manifestarea competențelor în practică "
        "(varianta a). "
        "Totodată, potențialul ereditar are nevoie de un context adecvat pentru a se "
        "actualiza: un copil cu predispoziții muzicale, de exemplu, nu va deveni "
        "muzician fără educație structurată și practică ghidată (varianta c). "
        "Varianta b este incorectă deoarece perspectiva biologică singură nu explică "
        "diferențele individuale cauzate de cultură și limbaj — tocmai acestea sunt "
        "absente din această perspectivă. "
        "Varianta d este incorectă deoarece nicio perspectivă singulară nu răspunde "
        "complet la toate întrebările despre diferențele individuale în dezvoltare."
    ),
    # —— 10032 — Perspectiva ambientală: experiență, recompense, stimulare (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "Perspectiva ambientală (behavioristă) susține că experiența și învățarea "
        "modelează comportamentul: copilul este în mare parte ceea ce a trăit, "
        "practicat și experimentat în interacțiunea cu mediul (varianta a). "
        "Recompensele și pedepsele sunt mecanisme centrale prin care mediul "
        "modifică frecvența și forma comportamentelor — condiționarea operantă "
        "descrisă de Skinner (varianta b). "
        "Stimularea din mediu — obiecte, persoane, situații, limbaj — este "
        "considerată sursa principală a schimbărilor comportamentale (varianta c). "
        "Varianta d este falsă: maturarea internă nu este un mecanism ambiental, "
        "ci unul biologic; perspectiva ambientală tocmai se distinge de cea "
        "biologică prin accentul pe factorii externi, nu pe cei interni."
    ),
    # —— 10033 — Mecanisme behavioriste: asociere, recompensă, stimulare (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "Perspectivele ambientale și behavioriste operează cu mecanisme de "
        "modificare a comportamentului prin factori externi: învățarea prin "
        "asociere și repetiție — conexiunile dintre stimuli și răspunsuri se "
        "consolidează prin practică sistematică (varianta a); modificarea "
        "comportamentului prin recompense și pedepse — principiul condiționării "
        "operante (varianta b); stimularea din mediu ca sursă principală de "
        "schimbare comportamentală — fără input extern adecvat, comportamentele "
        "dezirabile nu se formează (varianta c). "
        "Varianta d este falsă: ignorarea completă a oricărei experiențe "
        "postnatale este tocmai contrariul orientării behavioriste, care pune "
        "experiența postnatală în centrul explicației."
    ),
    # —— 10034 — Laude și pierderea privilegiilor modifică cooperarea (Multi AD) ——
    (
        "✅ a, ✅ d — variantele corecte; ❌ b și ❌ c sunt incorecte. "
        "Exemplul descrie un proces tipic de condiționare operantă: comportamentul "
        "de împărțire a jucăriilor a crescut în frecvență datorită consecințelor "
        "pozitive (laude), ilustrând faptul că mediul social modifică comportamentul "
        "copilului prin consecințele pe care le produce (varianta a). "
        "Laudele și pierderea privilegiilor sunt forme concrete de influență a "
        "mediului social asupra comportamentului, demonstrând că educatorii și "
        "părinții pot modela deliberat conduite dezirabile (varianta d). "
        "Varianta b este greșită: exemplul arată că mediul (recompensele) a "
        "modificat comportamentul, deci genele nu explică singure totul. "
        "Varianta c este greșită: exemplul nu dovedește absența maturării interne, "
        "ci demonstrează eficiența influenței mediului social."
    ),
    # —— 10035 — Afirmație falsă despre perspectiva ambientală (Multi A) ——
    (
        "✅ a — aceasta este afirmația falsă. "
        "Ideea că dezvoltarea ar exista identic fără nicio experiență postnatală "
        "este fundamentalmente falsă din perspectivă ambientală — și din orice "
        "perspectivă modernă — deoarece experiența postnatală modelează semnificativ "
        "comportamentul, cogniția, emoțiile și personalitatea. "
        "Variantele b, c și d sunt afirmații corecte din perspectivă ambientală: "
        "mediul poate modela comportamente noi prin asociere și consecințe (b); "
        "învățarea observațională, prin imitarea modelelor, este o formă "
        "importantă de influență ambientală, descrisă de Bandura (c); "
        "iar stimularea precoce a competențelor cognitive este susținută de "
        "numeroase studii (d). "
        "Cunoașterea acestei afirmații false ajută la înțelegerea corectă a "
        "limitelor reale ale perspectivei ambientale."
    ),
    # —— 10036 — Recompense, feedback, repetiție ghidată formează obiceiul (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Utilizarea recompenselor simbolice, a feedback-ului imediat și a repetiției "
        "ghidate pentru a forma un obicei de lectură reflectă principiile perspectivei "
        "ambientale: comportamentul este modelat prin consecințe pozitive și prin "
        "practică sistematică, până când devine automatizat (varianta a). "
        "Aceasta corespunde condiționării operante și abordărilor behavioriste "
        "aplicate în educație. "
        "Varianta b este incorectă deoarece perspectiva biologică pură ar spune că "
        "numai maturarea biologică contează și că intervențiile externe au efect "
        "limitat. "
        "Varianta c este incorectă deoarece strategia descrisă tocmai structurează "
        "deliberat experiența de învățare. "
        "Varianta d este incorectă deoarece recompensele și feedback-ul sunt, "
        "prin definiție, stimulare venită din exterior."
    ),
    # —— 10037 — Limitele perspectivei ambientale simplificate (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "O limită importantă a perspectivei ambientale strict simplificate este că "
        "poate subestima rolul maturării biologice și al predispozițiilor ereditare "
        "în explicarea traseelor de dezvoltare individuale (varianta a). "
        "De asemenea, poate ignora semnificația culturală a practicilor sociale și "
        "rolul limbajului interior în autoreglare și gândire — aspecte centrale în "
        "teoriile lui Vygotsky și Bruner (varianta b). "
        "O altă limită este că riscă să reducă copilul la un organism pasiv, complet "
        "modelat din exterior, negând agentivitatea, gândirea internă și structurile "
        "cognitive proprii (varianta d). "
        "Varianta c este falsă: perspectiva ambientală nu explică bine creativitatea, "
        "care implică procese interne complexe ce nu se reduc la simpla combinare "
        "a stimulilor externi."
    ),
    # —— 10038 — Anxietate socială din critică repetată: accent ambiental (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Explicația că un copil devine anxios în situații sociale datorită criticilor "
        "repetate — nu datorită unei trăsături înnăscute — este tipică pentru "
        "perspectiva ambientală, care pune accentul pe experiența acumulată și pe "
        "modul în care mediul modelează emoțiile și comportamentul (varianta a). "
        "Aceasta reflectă principiul condiționării clasice: o asociere repetată "
        "între situație socială și consecință negativă (critica dureroasă) creează "
        "treptat un răspuns emoțional conditionat de anxietate. "
        "Varianta b este greșită deoarece exclusivismul genetic este contrazis "
        "tocmai de accentul pe experiența trăită. "
        "Varianta c este greșită deoarece perspectiva ambientală pune interacțiunea "
        "socială în centrul explicației, nu etapele interne independente de mediu. "
        "Varianta d este greșită deoarece tocmai consecințele sociale (criticile "
        "repetate) sunt factorul central al explicației."
    ),
    # —— 10039 — Mecanisme ambientale: stimulare, recompensă, pedeapsă (Multi ABC) ——
    (
        "✅ a, ✅ b, ✅ c — variantele corecte; ❌ d este incorectă. "
        "Perspectiva ambientală operează cu trei mecanisme principale ale schimbării "
        "comportamentale: stimularea — mediul oferă ocazii de exercițiu, de contact "
        "cu materiale și de activare a comportamentelor potențiale (varianta a); "
        "recompensa — consecințe plăcute sau valoroase care cresc probabilitatea "
        "ca un comportament să fie repetat (varianta b); pedeapsa — consecințe "
        "neplăcute care reduc frecvența unui comportament nedorit (varianta c). "
        "Varianta d este falsă deoarece maturarea internă este un mecanism "
        "biologic, nu ambiental; perspectiva ambientală tocmai se distinge de "
        "cea biologică prin accentul exclusiv pe factorii externi ca surse ale "
        "schimbării."
    ),
    # —— 10040 — Perspectiva interacționistă: ereditate și mediu împreună (TF Adevărat) ——
    (
        "Adevărat. Perspectiva interacționistă reprezintă o viziune integrativă care "
        "depășește opoziția simplistă dintre ereditate și mediu, susținând că ambii "
        "factori acționează simultan și se influențează reciproc în mod dinamic pe "
        "toată durata vieții. "
        "Nu există un moment în care numai genele contează și mediul este neutru, "
        "sau invers: interacțiunea este permanentă și subtilă. "
        "Această perspectivă explică, de exemplu, de ce gemeni identici crescuți "
        "în contexte diferite pot ajunge la personalități distincte, sau de ce "
        "copii cu ereditate diferită pot atinge niveluri similare de competență "
        "în condiții educaționale echivalente. "
        "Psihologia educației moderne se fundamentează în mare parte pe această "
        "viziune interacționistă, care justifică intervenția pedagogică fără a "
        "nega rolul biologic."
    ),
    # —— 10041 — Afirmații corecte despre perspectiva interacționistă (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Perspectiva interacționistă susține că același potențial ereditar se poate "
        "manifesta diferit în medii diferite, ceea ce explică variabilitatea "
        "comportamentului și competențelor chiar și la copiii cu predispoziții "
        "similare (varianta a). "
        "Experiența educațională, calitatea relațiilor și stimularea pot amplifica "
        "sau limita aptitudinile înnăscute — rezultatul depinde de combinația "
        "specifică ereditate-mediu trăită de fiecare individ (varianta b). "
        "O explicație completă și riguroasă a dezvoltării necesită luarea în "
        "considerare a ambilor factori, nu a unuia exclusiv (varianta d). "
        "Varianta c este falsă deoarece tocmai interacționismul neagă separarea "
        "completă a eredității de mediu, afirmând coexistența și "
        "interdependența lor permanentă."
    ),
    # —— 10042 — Copil reactiv: mediu punitiv vs. mediu calm (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Exemplul cu copilul cu temperament reactiv ilustrează un mecanism central "
        "al perspectivei interacționiste: o predispoziție temperamentală — probabil "
        "cu baze ereditare — produce efecte complet diferite în funcție de calitatea "
        "mediului educațional cu care interacționează. "
        "Același temperament reactiv devine sursă de anxietate în medii punitive "
        "și imprevizibile, dar se transformă în adaptare funcțională în medii calde "
        "și previzibile (varianta a). "
        "Aceasta dovedește că nici temperamentul singur și nici mediul singur nu "
        "explică rezultatul — ci interacțiunea lor specifică. "
        "Varianta b este greșită deoarece exemplul arată că mediul contează "
        "esențial în determinarea rezultatelor dezvoltării. "
        "Varianta c este greșită deoarece mediul educațional influențează copiii "
        "la toate vârstele, nu doar la maturitate."
    ),
    # —— 10043 — Poziții incompatibile cu perspectiva interacționistă (Multi AB) ——
    (
        "✅ a, ✅ b — variantele incompatibile cu interacționismul; "
        "❌ c și ❌ d sunt compatibile. "
        "Determinismul genetic total — care afirmă că mediul este simplu decor, fără "
        "influență reală asupra traseului de dezvoltare — este incompatibil cu "
        "perspectiva interacționistă, deoarece aceasta atribuie mediului un rol "
        "esențial (varianta a). "
        "Tabula rasa absolută — care afirmă că individul se naște complet "
        "neprogramat și că numai mediul îl formează — este la fel de incompatibilă, "
        "deoarece interacționismul recunoaște potențialul ereditar ca punct real "
        "de plecare (varianta b). "
        "Varianta c — potențial ereditar modelat de experiență — este chiar esența "
        "perspectivei interacționiste. "
        "Varianta d — educația valorifică aptitudini diferite la copii diferiți — "
        "este, de asemenea, compatibilă și chiar derivă logic din interacționism."
    ),
    # —— 10044 — Utilitatea perspectivei interacționiste în practica școlară (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Perspectiva interacționistă este valoroasă în practica școlară deoarece "
        "evită atât fatalismul genetic — nu mai spunem că un copil nu poate "
        "progresa deoarece nu are genele potrivite — cât și neglijarea mediului "
        "— nu mai considerăm că mediul decide totul și că ereditatea nu contează "
        "(varianta a). "
        "Permite adaptarea educației la potențialul real și la nevoile specifice "
        "ale fiecărui copil, înțelegând că există combinații unice de factori "
        "biologici și de mediu (varianta b). "
        "Susține intervenții diferențiate și personalizate, în loc de un singur "
        "tipar educațional aplicat uniform tuturor (varianta d). "
        "Varianta c este falsă: tocmai perspectiva interacționistă recunoaște că "
        "copiii diferă biologic, și de aceea recomandă diferențierea, nu uniformizarea."
    ),
    # —— 10045 — Metafora: genele deschid uși, mediul decide prin care treci (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Metafora „genele deschid uși, mediul decide prin care treci» exprimă esența "
        "perspectivei interacționiste: ereditatea stabilește posibilități, tendințe "
        "și limite — nu certitudini — iar mediul, experiența și educația activează, "
        "orientează sau inhibă acele posibilități (varianta a). "
        "Varianta b este greșită deoarece determinismul biologic rigid ar spune că "
        "genele determină complet traseul, nu că simplu „deschid uși» pe care "
        "altcineva le trece sau nu. "
        "Varianta c este greșită deoarece metafora recunoaște explicit și "
        "esențialmente rolul genelor ca punct de plecare. "
        "Varianta d este greșită deoarece metafora tocmai recunoaște că mediul "
        "și educația au puterea reală de a orienta traseul prin ușile deschise "
        "de ereditate."
    ),
    # —— 10046 — Perspectiva culturală: limbaj, valori, interacțiune socială (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Perspectiva culturală, reprezentată de Vygotsky și Bruner, susține că "
        "limbajul, valorile, simbolurile și interacțiunea socială mediată cultural "
        "modelează în profunzime modul în care se construiește cogniția și "
        "comportamentul uman (varianta a). "
        "Din această perspectivă, nu există dezvoltare cognitivă autentică în "
        "absența participării la practici culturale specifice, a uneltelor cognitive "
        "transmise de comunitate și a ghidării oferite de adulți sau parteneri "
        "mai competenți. "
        "Varianta b este falsă deoarece tocmai perspectiva culturală afirmă că "
        "dezvoltarea cognitivă are loc în context social și cultural, nu în vid. "
        "Varianta c este falsă deoarece cultura este privită ca factor central "
        "și constitutiv, nu ca simplu decor. "
        "Varianta d este falsă deoarece gândirea simbolică are rădăcini sociale "
        "și culturale, nu genetice exclusive."
    ),
    # —— 10047 — Idei ale perspectivei culturale (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Perspectiva culturală susține că gândirea și cogniția se construiesc prin "
        "participare activă la practici sociale specifice culturii — matematică, "
        "limbaj, artă, ritualuri, meserii — nu prin maturare biologică izolată "
        "(varianta a). "
        "Limbajul este văzut de Vygotsky ca unealtă fundamentală ce mediază atât "
        "comunicarea interpersonală, cât și gândirea interioară — vorbirea "
        "interiorizată devine instrument al autoreglării cognitive (varianta b). "
        "Adultul sau partenerul mai competent poate ghida copilul în zona proximală "
        "de dezvoltare, sprijinindu-l să atingă niveluri pe care nu le-ar putea "
        "atinge singur (varianta d). "
        "Varianta c este falsă deoarece perspectiva culturală susține tocmai opusul: "
        "fără limbaj, simboluri și interacțiune socială, dezvoltarea cognitivă "
        "superioară nu are loc."
    ),
    # —— 10048 — Zona proximală de dezvoltare: Vygotsky (Multi A) ——
    (
        "✅ a — singura variantă corectă. "
        "Conceptul vygotskian de zonă proximală de dezvoltare (ZPD) descrie exact "
        "distanța dintre ceea ce copilul poate realiza singur în prezent și ceea "
        "ce poate realiza cu sprijinul unui partener mai competent (varianta a). "
        "Exemplul — rezolvarea problemei cu ajutorul colegului avansat, urmată "
        "de reușita ulterioară independentă — ilustrează perfect modul în care "
        "interacțiunea socială mediată extinde competența cognitivă actuală, "
        "transformând zona proximală de azi în nivelul independent de mâine. "
        "Varianta b — extincția comportamentală — aparține behaviorismului, "
        "nu teoriei vygotskiene. "
        "Varianta c — maturarea reflexă — aparține perspectivei biologice. "
        "Varianta d neagă tocmai rolul partenerului social, care este central "
        "în teoria culturală a lui Vygotsky."
    ),
    # —— 10049 — Bruner: reprezentări enactiv-iconic-simbolice, cultură (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Bruner a propus că învățarea urmează trei moduri succesive de reprezentare: "
        "enactiv (prin acțiune directă și manipulare), iconic (prin imagini și "
        "scheme perceptive) și simbolic (prin limbaj și simboluri abstracte) — "
        "ceea ce explică progresia naturală de la concret la abstract în educație "
        "(varianta a). "
        "El a subliniat că orice cultură oferă unelte cognitive — limbaj, narațiune, "
        "sisteme de notație, instituții — transmise noilor generații prin interacțiune "
        "socială (varianta b). "
        "Educația poate și trebuie să organizeze experiența în forme accesibile "
        "vârstei și nivelului copilului — principiul scaffolding-ului, adică "
        "sprijinul gradual retras pe măsura dobândirii competenței (varianta d). "
        "Varianta c este falsă deoarece pentru Bruner, copilul nu învață în "
        "izolare, ci prin contactul nemijlocit cu modele culturale, adulți și "
        "artefacte simbolice ale comunității."
    ),
    # —— 10050 — Distincții între cele patru perspective (Multi ABD) ——
    (
        "✅ a, ✅ b, ✅ d — variantele corecte; ❌ c este incorectă. "
        "Perspectiva biologică pune în centru maturarea internă a organismului, "
        "iar perspectiva ambientală pune în centru experiența, consecințele "
        "și stimularea din mediu (varianta a). "
        "Perspectiva interacționistă integrează ereditatea și mediul ca factori "
        "co-determinanți care interacționează permanent, iar perspectiva culturală "
        "adaugă limbajul, practicile sociale și transmisia culturală ca motoare "
        "ale dezvoltării cognitive superioare (varianta b). "
        "Toate patru perspectivele pot fi recunoscute și diferențiate după factorul "
        "pe care îl plasează în centrul explicației: maturare biologică, experiență "
        "de mediu, interacțiunea ereditate-mediu sau respectiv cultura și limbajul "
        "(varianta d). "
        "Varianta c este falsă deoarece inversează greșit caracteristicile: "
        "perspectiva culturală susține că dezvoltarea are loc tocmai prin "
        "participare socială intensă, nu în vid social; iar perspectiva biologică "
        "se bazează pe maturare internă, nu pe recompense — acestea aparțin "
        "perspectivei ambientale."
    ),
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
            return PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS[idx]
    return ""


def attach_explanations(items: List[Item]) -> List[Item]:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out: List[Item] = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS):
            item["explanation"] = PSIHOLOGIA_DEZVOLTARII_II_EXPLANATIONS[i]
        out.append(item)
    return out
