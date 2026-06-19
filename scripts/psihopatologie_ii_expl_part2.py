"""Explicații Psihopatologie II — partea 2 (index 80–189, exam 8081–8190). Suicid + TOC + Anxietate."""

from __future__ import annotations

from typing import List

# ---------------------------------------------------------------------------
# SUICID (index 80–109, itemi 0–29 din SUICID_ITEMS)
# ---------------------------------------------------------------------------

PART2_EXPLANATIONS: List[str] = [
    # ── 80 ── Ideea suicidară — definiție (multi, corect: a)
    (
        "✅ a) gânduri despre moartea sau sinuciderea proprie — aceasta este definiția ideatiei suicidare. "
        "❌ b) tristețe tranzitorie — tristețea nu implică implicit gânduri suicidare. "
        "❌ c) frică de moartea altcuiva — nu constituie ideație suicidară proprie. "
        "❌ d) dorința de a dormi mult — este oboseală, nu ideație. "
        "Ideația suicidară cuprinde orice gând legat de propria moarte sau sinucidere, variind de la gânduri pasive "
        "(„ar fi mai bine să nu mă trezesc») până la planuri active de a-și lua viața. "
        "Distincția față de simpla tristețe sau oboseală este esențială în evaluarea clinică."
    ),

    # ── 81 ── Intenția suicidară vs. ideație (multi, corect: a)
    (
        "✅ a) dorința sau hotărârea de a muri prin propria acțiune — aceasta diferențiază intenția de ideație. "
        "❌ b) prezența unui plan concret — planul poate lipsi inițial; intenția poate exista fără detalii. "
        "❌ c) absența oricărui gând despre moarte — contrar definiției, intenția presupune gând despre moarte. "
        "❌ d) frică normală de boală terminală — nu este intenție suicidară. "
        "Intenția suicidară adaugă față de simplă ideație o dimensiune motivațională activă: dorința sau hotărârea de a acționa pentru a-și lua viața. "
        "Nu presupune neapărat un plan detaliat, dar semnalează o escaladare a riscului față de ideația pasivă."
    ),

    # ── 82 ── Planul suicidar (multi, corect: ab)
    (
        "✅ a) modul, momentul sau mijloacele avute în vedere — elementele constitutive ale planului. "
        "✅ b) accesul la metode letale sau pregătirea actului — cresc iminența riscului. "
        "❌ c) doar starea de tristețe — tristețea singură nu constituie plan. "
        "❌ d) refuzul de a discuta despre suferință — este evitare, nu plan. "
        "Planul suicidar concretizează intenția: persoana a identificat o metodă, a ales un moment sau un loc, "
        "ori a acumulat deja mijloacele necesare. "
        "Cu cât planul este mai detaliat și mijloacele mai accesibile, cu atât urgența intervenției clinice este mai mare."
    ),

    # ── 83 ── Tentativă vs. automutilare non-suicidară (multi, corect: ab)
    (
        "✅ a) tentativa urmărește moartea, nu doar reglarea emoțională — aceasta este distincția de scop definitorie. "
        "✅ b) automutilarea non-suicidară vizează adesea eliberarea tensiunii — scopul este reglarea afectivă, nu decesul. "
        "❌ c) ambele au același scop — fals; scopurile sunt fundamental diferite. "
        "❌ d) automutilarea exclude orice risc de vătămare — fals, vătămarea fizică apare și în automutilare. "
        "Tentativa suicidară și automutilarea non-suicidară (NSSI) sunt comportamente distincte ca intenție. "
        "Tentativa urmărește decesul; NSSI urmărește adesea reducerea unei stări emoționale intolerabile fără intenție letală. "
        "Distincția ghidează planul de intervenție, dar ambele necesită evaluare și suport."
    ),

    # ── 84 ── Ideea pasivă vs. activă (multi, corect: ab)
    (
        "✅ a) activa include dorința sau intenția de a se sinucide — marchează escaladarea față de ideația pasivă. "
        "✅ b) pasiva poate apărea fără plan sau intenție de acțiune — apare și în depresii comune. "
        "❌ c) pasiva presupune întotdeauna un plan detaliat — fals, prin definiție pasiva este lipsită de plan. "
        "❌ d) activa exclude orice gând despre moarte — absurd, activa implică gând orientat spre acțiune. "
        "Ideea pasivă ('ar fi mai bine să nu exist') poate apărea în depresii ușoare fără intenție sau plan. "
        "Ideea activă indică o schimbare motivațională semnificativă și necesită evaluare mai aprofundată a riscului și a planului de siguranță."
    ),

    # ── 85 ── Factori de risc suicidar (multi, corect: abc)
    (
        "✅ a) tulburare depresivă sau bipolară — tulburările psihiatrice majore cresc semnificativ riscul. "
        "✅ b) tentativă anterioară de suicid — cel mai puternic predictor individual al tentativelor viitoare. "
        "✅ c) izolare socială sau acces la mijloace letale — factori de risc comportamental și contextual. "
        "❌ d) rețea socială stabilă și suport constant — acesta este un factor protector, nu de risc. "
        "Factorii de risc suicidar sunt aditivi: prezența simultană a unui diagnostic psihiatric major, a unui "
        "antecedent de tentativă și a izolării sociale cresc probabilitatea unui comportament suicidar. "
        "Suportul social solid funcționează în sens invers, ca factor protector."
    ),

    # ── 86 ── Factori protectori (multi, corect: abc)
    (
        "✅ a) legături sociale semnificative și suport — conectivitatea socială reduce riscul suicidar. "
        "✅ b) acces limitat la mijloace letale — restricția accesului este una dintre cele mai eficiente intervenții. "
        "✅ c) speranță și motive pentru a trăi — orientarea spre viitor protejează în fața crizei. "
        "❌ d) consumul de alcool pentru a 'ușura' durerea — alcoolul reduce inhibițiile și crește impulsivitatea. "
        "Factorii protectori nu elimină riscul, dar îl atenuează semnificativ. "
        "Conectivitatea socială, speranța și restricția accesului la mijloace letale sunt printre cele mai robuste "
        "elemente protective identificate în literatura de specialitate."
    ),

    # ── 87 ── Plan concret crește riscul (TF, corect: Adevărat)
    (
        "Adevărat. Prezența unui plan concret — care include metoda, momentul și accesul la mijloace — semnalează "
        "o escaladare a riscului față de simpla ideație. "
        "Un plan detaliat cu mijloace disponibile constituie un semn de alarmă major și impune evaluare clinică imediată, "
        "deoarece probabilitatea trecerii la act este considerabil mai mare decât în cazul ideației fără plan."
    ),

    # ── 88 ── Evaluarea riscului suicidar (multi, corect: abc)
    (
        "✅ a) ideea, intenția, planul și mijloacele disponibile — componente nucleu ale evaluării. "
        "✅ b) tentative anterioare și factori precipitanți — context esențial pentru estimarea riscului. "
        "✅ c) rețeaua de suport și factorii protectori — completează tabloul clinic. "
        "❌ d) exclusiv coeficientul de inteligență — IQ nu este indicator relevant pentru riscul suicidar. "
        "Evaluarea riscului suicidar este multimodală. Clinicianul explorează ideația, intenția, planul și mijloacele, "
        "istoricul de tentative, factorii precipitanți actuali și resursele de protecție disponibile. "
        "O evaluare completă fundamentează decizia de intervenție."
    ),

    # ── 89 ── Semne de alarmă (multi, corect: abc)
    (
        "✅ a) predarea de bunuri sau rezolvarea 'treburilor' — comportament de pregătire a actului. "
        "✅ b) izolare bruscă sau rămas bun definitiv — retragere socială și comunicare de despărțire. "
        "✅ c) vorbe despre a fi o povară sau fără speranță — exprimarea verbală a disperării. "
        "❌ d) planificarea unei vacanțe cu prietenii — semn pozitiv de orientare spre viitor. "
        "Semnele de alarmă comportamentale și verbale sunt indicatori importanți ai unui risc crescut. "
        "Punerea în ordine a problemelor personale, izolarea, cuvintele de rămas bun și exprimarea sentimentului de inutilitate "
        "sau lipsă de speranță trebuie luate întotdeauna în serios și evaluate clinic."
    ),

    # ── 90 ── Pacientul cu pastile acasă (multi, corect: ab)
    (
        "✅ a) plan suicidar cu acces la mijloace — pacientul a identificat metoda și cunoaște doza letală. "
        "✅ b) risc crescut care necesită evaluare urgentă — combinația plan-mijloace impune intervenție imediată. "
        "❌ c) idee pasivă fără intenție de acțiune — declarația indică clar intenție și pregătire. "
        "❌ d) simptom obsesiv fără relevanță suicidară — contextul clinic exclude interpretarea obsesivă. "
        "Declarația pacientului indică atât un plan (medicamentele ca metodă) cât și cunoașterea dozei, "
        "ceea ce semnifică acces la mijloace și pregătire deliberată. "
        "Acesta este un semnal de alarmă major care necesită evaluare imediată și plan de siguranță."
    ),

    # ── 91 ── Întrebarea directă (multi, corect: ab)
    (
        "✅ a) este recomandată; nu 'plantează' ideea la majoritatea pacienților — cercetările infirmă mitul. "
        "✅ b) permite estimarea riscului și planificarea intervenției — facilitează comunicarea deschisă. "
        "❌ c) trebuie evitată întotdeauna — mitul că întrebarea sugerează sinuciderea este clinic infirmat. "
        "❌ d) înlocuiește evaluarea medicală — întrebarea directă completează, nu înlocuiește evaluarea clinică. "
        "Dovezile clinice arată că întrebarea directă despre gânduri suicidare nu crește riscul și nu sugerează ideea. "
        "Dimpotrivă, permite evaluarea riscului, construirea unui plan de siguranță și comunicarea empatică — "
        "de aceea este o practică recomandată în ghidurile internaționale."
    ),

    # ── 92 ── Borderline și suicid (multi, corect: ab)
    (
        "✅ a) risc crescut de automutilare și suicid — TBP are una dintre cele mai ridicate rate de tentative. "
        "✅ b) instabilitate afectivă și impulsivitate — trăsături centrale care amplifică riscul. "
        "❌ c) absența oricărei idei suicidare — fals, aproximativ 70-75% dintre pacienți raportează tentative. "
        "❌ d) episoade de elație ca în manie — specifice tulburării bipolare, nu TBP. "
        "Tulburarea de personalitate borderline se caracterizează prin instabilitate emoțională marcată, relații interpersonale "
        "intense și impulsivitate crescută. "
        "Automutilarea non-suicidară este frecventă ca mecanism de reglare emoțională, iar tentativele suicidare sunt comune, "
        "ceea ce face evaluarea continuă a riscului esențială."
    ),

    # ── 93 ── Alcool și risc suicidar (multi, corect: abd)
    (
        "✅ a) reduce inhibițiile și crește impulsivitatea — mecanism central de amplificare a riscului. "
        "✅ b) agravează depresia și dezorganizarea — alcoolul are efect depresogen pe termen lung. "
        "❌ c) protejează garantat împotriva tentativei — fals; alcoolul crește riscul, nu îl reduce. "
        "✅ d) interacționează cu medicamentele psihotrope — poate potența efectele sedative sau toxicitatea. "
        "Alcoolul este un factor de risc suicidar bine documentat: reduce inhibițiile comportamentale, amplifică "
        "disperarea și starea disforizică și poate potența efectul toxic al medicamentelor. "
        "Consumul de alcool în perioadele de criză necesită evaluare clinică atentă."
    ),

    # ── 94 ── Safety plan (multi, corect: ab)
    (
        "✅ a) nu înlocuiește evaluarea clinică și monitorizarea — este un instrument complementar. "
        "✅ b) poate include pași de autocontrol și contacte de urgență — structura tipică a planului. "
        "❌ c) garantează absența oricărei tentative viitoare — nu există o astfel de garanție. "
        "❌ d) exclude spitalizarea când riscul este iminent — când riscul e iminent, spitalizarea poate fi necesară. "
        "Planul de siguranță este un instrument clinic structurat care ajută persoana să identifice semnele de avertizare, "
        "strategii de coping, resurse de suport și contacte de urgență. "
        "El completează evaluarea clinică și monitorizarea, fără să le poată substitui."
    ),

    # ── 95 ── Întrebarea directă — TF (TF, corect: Adevărat)
    (
        "Adevărat. Cercetările clinice confirmă că adresarea directă a subiectului suicidului nu crește riscul "
        "și nu 'plantează' ideea suicidară. "
        "Dimpotrivă, întrebarea directă facilitează comunicarea deschisă, permite estimarea nivelului de risc "
        "și creează premisele construirii unui plan de intervenție adecvat — de aceea este recomandată de toate ghidurile internaționale."
    ),

    # ── 96 ── Risc iminent — prioritate (multi, corect: abc)
    (
        "✅ a) asigurarea siguranței imediate a persoanei — prioritatea absolută în criza suicidară. "
        "✅ b) evaluarea psihiatrică de urgență — necesară pentru estimarea riscului și decizia de tratament. "
        "✅ c) limitarea accesului la mijloace letale — reducerea disponibilității metodei reduce riscul. "
        "❌ d) amânarea discuției — este contraindicată în situații de risc iminent. "
        "Când riscul suicidar este iminent, prioritatea absolută este siguranța persoanei. "
        "Aceasta include îndepărtarea sau restricția mijloacelor letale, obținerea unei evaluări psihiatrice imediate "
        "și menținerea supravegherii sau a unui contact continuu până la stabilizare."
    ),

    # ── 97 ── Spitalizare involuntară (multi, corect: abd)
    (
        "✅ a) riscul suicidar este iminent și nu poate fi gestionat ambulatoriu — indicație principală. "
        "✅ b) persoana are plan concret și refuză tratamentul — refuzul cooperării justifică măsura. "
        "❌ c) există doar tristețe ușoară, fără ideație — nu justifică internarea involuntară. "
        "✅ d) legea și protocoalele locale o permit — cadrul legal este o condiție necesară. "
        "Spitalizarea involuntară este o măsură excepțională, aplicabilă când riscul este iminent, persoana nu cooperează "
        "cu tratamentul și nu există alternative sigure. "
        "Condițiile legale și etice variază în funcție de jurisdicție, dar principiul primar este protejarea vieții."
    ),

    # ── 98 ── Prevenție pe termen lung (multi, corect: abc)
    (
        "✅ a) tratamentul tulburării psihice de fond — abordarea cauzei principale reduce riscul structural. "
        "✅ b) reducerea accesului la mijloace letale — intervenție cu dovezi solide de eficiență. "
        "✅ c) sprijinul rețelei sociale și psihoterapia — consolidarea resurselor protectoare. "
        "❌ d) plan de siguranță fără întrebare despre comportament autolesiv anterior — neglijează istoricul esențial. "
        "Prevenția suicidului pe termen lung este multistratificată. "
        "Tratarea depresiei, tulburării bipolare sau a schizofreniei reduce semnificativ riscul, iar restricția accesului "
        "la mijloace letale și consolidarea suportului social sunt intervenții cu dovezi robuste."
    ),

    # ── 99 ── Urmărire post-tentativă (multi, corect: abd)
    (
        "✅ a) riscul de recidivă rămâne crescut — tentativa anterioară este cel mai puternic predictor individual. "
        "✅ b) perioada post-externare poate fi de risc — tranziția din spital este o fereastră vulnerabilă. "
        "❌ c) tentativa anterioară nu influențează riscul viitor — fals; este factorul predictor cel mai robust. "
        "✅ d) tratamentul poate reduce riscul pe termen lung — continuarea terapiei este esențială. "
        "Tentativa anterioară crește semnificativ probabilitatea unor noi tentative. "
        "Perioada imediat post-externare este considerată de risc crescut, motiv pentru care urmărirea activă, "
        "contactarea proactivă a pacientului și continuarea tratamentului sunt recomandate în toate protocoalele."
    ),

    # ── 100 ── Mitul 'cine vorbește nu se sinucide' (multi, corect: ab)
    (
        "✅ a) fals; vorbele pot semnala risc real — comunicarea suferinței este un semnal de ajutor. "
        "✅ b) periculos, deoarece poate întârzia intervenția — minimalizarea comunicărilor poate fi fatală. "
        "❌ c) corect în toate cazurile clinice — fals; studiile infirmă categoric acest mit. "
        "❌ d) valabil doar la adolescenți — fals pentru orice grupă de vârstă. "
        "Studiile arată că până la 80% dintre persoanele care și-au luat viața au comunicat în prealabil intenția, "
        "direct sau indirect. "
        "Ignorarea sau minimalizarea comunicărilor verbale despre suicid poate duce la întârzieri fatale în intervenție "
        "și trebuie evitată în practica clinică."
    ),

    # ── 101 ── Factori de risc la adolescenți (multi, corect: abd)
    (
        "✅ a) bullying, excludere sau conflicte familiale — presiunile socio-familiale specifice adolescenței. "
        "✅ b) tulburări de consum sau impulsivitate crescută — reduc controlul comportamental. "
        "❌ c) rețea de suport stabilă și deschidere spre părinți — factori protectori, nu de risc. "
        "✅ d) identitate de gen neacceptată sau discriminare — factor de risc documentat la tineri LGBTQ+. "
        "La adolescenți, contextul socio-familial și presiunile grupului de egali joacă un rol semnificativ. "
        "Bullying-ul, discriminarea legată de identitate de gen sau orientare sexuală, conflictele familiale "
        "și impulsivitatea specifică vârstei sunt factori de risc cu relevanță clinică dovedită."
    ),

    # ── 102 ── Linii telefonice de criză (multi, corect: abd)
    (
        "✅ a) oferi sprijin imediat și evaluare preliminară — funcția principală a serviciilor de criză. "
        "✅ b) orienta către servicii de urgență când e necesar — facilitează accesul la îngrijire specializată. "
        "❌ c) înlocui tratamentul psihiatric de lungă durată — liniile de criză sunt servicii de urgență, nu tratament. "
        "✅ d) reduce izolarea în momentul crizei — contactul uman imediat are valoare terapeutică. "
        "Liniile telefonice de criză sunt servicii de prim contact, disponibile 24/7, care oferă suport emoțional, "
        "evaluare inițială a riscului și orientare spre servicii de urgență. "
        "Nu substituie tratamentul psihiatric, dar reduc izolarea și pot stabiliza persoana în criză."
    ),

    # ── 103 ── Tentativă anterioară — TF (TF, corect: Adevărat)
    (
        "Adevărat. Tentativa anterioară de suicid este considerată cel mai puternic predictor individual al "
        "tentativelor viitoare. "
        "Persoanele cu antecedente de tentativă au un risc semnificativ mai mare comparativ cu populația generală, "
        "ceea ce face urmărirea pe termen lung, monitorizarea și continuarea tratamentului absolut esențiale."
    ),

    # ── 104 ── Afirmații corecte despre suicid (multi, corect: abd)
    (
        "✅ a) majoritatea persoanelor cu idei suicidare comunică suferința — comunicarea este un semnal de ajutor. "
        "✅ b) depresia netratată crește riscul suicidar — relație cauzală documentată. "
        "❌ c) suicidul apare doar la persoane cu psihoză — fals; depresia și bipolarul sunt mai frecvent implicate. "
        "✅ d) planul concret și mijloacele cresc urgența — elementele planului amplifică iminența riscului. "
        "Suicidul nu este exclusiv asociat psihozei; depresia, tulburarea bipolară și alte afecțiuni sunt mai des implicate. "
        "Comunicarea suferinței este un apel la ajutor, iar prezența planului cu mijloace concrete impune intervenție imediată."
    ),

    # ── 105 ── Afirmații greșite despre suicid (multi, corect: ab)
    (
        "✅ a) ideea suicidară este mereu un semn de manipulare — fals și periculos clinic; etichetarea descurajează ajutorul. "
        "✅ b) riscul dispare după ce persoana pare liniștită brusc — fals; liniștea bruscă poate indica decizia luată. "
        "❌ c) evaluarea include intenția și planul — aceasta este o afirmație corectă. "
        "❌ d) factorii protectori pot reduce riscul — aceasta este o afirmație corectă. "
        "Etichetarea ideatiei suicidare ca 'manipulare' este o prejudecată clinică periculoasă care poate întârzia intervenția. "
        "De asemenea, liniștea bruscă după o perioadă de agitație poate semnala că persoana a luat decizia și "
        "nu mai este ambivalentă, ceea ce de fapt crește riscul iminent."
    ),

    # ── 106 ── Pacient cu depresie majoră 'nu mai are sens' (multi, corect: abc)
    (
        "✅ a) întrebări directe despre idee, plan și mijloace — explorarea componentelor suicidare. "
        "✅ b) evaluarea tentativelor anterioare — context esențial pentru estimarea riscului. "
        "✅ c) contactarea rețelei de suport, cu acord — consolidarea resurselor de protecție. "
        "❌ d) evitarea subiectului pentru a nu sugera suicidul — contraindicată, perpetuează riscul neevaluat. "
        "Expresia 'nu mai are sens' este un semnal verbal care necesită explorare directă și sistematică. "
        "Clinicianul evaluează ideația, planul, mijloacele și istoricul de tentative, putând implica rețeaua de suport "
        "cu acordul pacientului pentru a crește siguranța."
    ),

    # ── 107 ── Gânduri pasive vs. active — relevanță (multi, corect: abd)
    (
        "✅ a) estimarea gradului de risc — tipul ideatiei influențează direct nivelul de risc evaluat. "
        "✅ b) planificarea nivelului de intervenție — ideea activă poate necesita intervenție imediată. "
        "❌ c) diagnosticarea tulburării obsesiv-compulsive — această distincție nu are relevanță diagnostică pentru TOC. "
        "✅ d) decizia privind siguranța imediată — ideea activă cu plan și mijloace impune acțiune promptă. "
        "Distincția dintre ideea pasivă (dorința de a muri, fără intenție) și cea activă (cu intenție de a acționa) "
        "ghidează estimarea riscului și nivelul de intervenție necesar. "
        "Ideea activă, mai ales combinată cu un plan și mijloace disponibile, justifică deseori intervenție imediată."
    ),

    # ── 108 ── Suicidul asociat DOAR cu depresia — TF (TF, corect: Fals)
    (
        "Fals. Suicidul este asociat cu o gamă largă de tulburări psihice, nu exclusiv cu depresia majoră. "
        "Tulburarea bipolară, schizofrenia, tulburarea de personalitate borderline, tulburările anxioase "
        "și tulburările de consum de substanțe sunt de asemenea associate cu risc suicidar crescut. "
        "Evaluarea riscului trebuie realizată indiferent de diagnosticul principal."
    ),

    # ── 109 ── Limitarea accesului la mijloace — TF (TF, corect: Adevărat)
    (
        "Adevărat. Limitarea accesului la mijloace letale este una dintre intervențiile de prevenție a suicidului "
        "cu cele mai solide dovezi empirice. "
        "Restricționarea accesului la arme de foc, medicamente în cantități mari sau alte metode letale reduce "
        "semnificativ numărul de sinucideri complete, chiar dacă nu elimină ideația. "
        "Această intervenție este eficientă tocmai în perioadele de impulsivitate crescută, când intervalul de timp "
        "dintre intenție și acces la metodă este critic."
    ),

    # ---------------------------------------------------------------------------
    # TOC (index 110–139, itemi 0–29 din TOC_ITEMS)
    # ---------------------------------------------------------------------------

    # ── 110 ── Definiția TOC (multi, corect: a)
    (
        "✅ a) obsesiilor și/sau compulsiilor — aceasta este definiția TOC. "
        "❌ b) episoadelor de elație și grandiozitate — specifice maniei, nu TOC. "
        "❌ c) fricii de spații publice, fără ritualuri — descrie agorafobia. "
        "❌ d) halucinațiilor auditive persistente — simptom psihotic. "
        "Tulburarea obsesiv-compulsivă se definește prin prezența obsesiilor (gânduri, impulsuri sau imagini intruzive "
        "și recurente, percepute ca perturbatoare) și/sau a compulsiilor (comportamente sau ritualuri mentale repetitive). "
        "Nu include simptome psihotice, afective sau fobice."
    ),

    # ── 111 ── Obsesiile în TOC (multi, corect: ab)
    (
        "✅ a) gânduri, impulsuri sau imagini intruzive și recurente — definiția obsesiei. "
        "✅ b) percepute ca deranjante și incontrolabile — caracterul ego-distonic. "
        "❌ c) comportamente repetitive vizibile din afară — acestea sunt compulsii, nu obsesii. "
        "❌ d) preferințe estetice pentru ordine — preferințele conștiente nu sunt obsesii patologice. "
        "Obsesiile sunt fenomene mentale involuntare, percepute ca intruzive și ego-distonice (nedorite, contrare valorilor persoanei). "
        "Le deosebesc de simplele preferințe tocmai caracterul nedorit, recurent și generatorul de anxietate sau suferință marcată."
    ),

    # ── 112 ── Tipuri de obsesii (multi, corect: abc)
    (
        "✅ a) teamă de contaminare — una dintre obsesiile cele mai frecvente în TOC. "
        "✅ b) gânduri agresive, accidentale sau sexuale nedorite — gânduri intruzive ego-distonice. "
        "✅ c) îndoială și indecizie patologică — 'am greșit?', 'am lovit pe cineva?'. "
        "❌ d) planificarea realistă a activităților zilnice — aceasta nu este obsesie. "
        "Obsesiile frecvente includ preocupări privind contaminarea, gânduri agresive sau sexuale intruzive (nedorite, "
        "contrare valorilor persoanei) și îndoiala patologică. "
        "Planificarea realistă a zilei este o activitate adaptativă, nu un simptom obsesiv."
    ),

    # ── 113 ── Compulsiile în TOC (multi, corect: abc)
    (
        "✅ a) comportamente repetitive sau ritualuri mentale — definiția compulsiei. "
        "✅ b) executate pentru a reduce anxietatea sau a preveni un rău — scopul funcțional. "
        "✅ c) simțite ca necesare, deși excesive sau iraționale — insight parțial prezent în TOC tipic. "
        "❌ d) activități plăcute, făcute din proprie inițiativă — compulsiile nu sunt plăcute, ci obligatorii anxios. "
        "Compulsiile pot fi comportamente observabile (spălat, verificat) sau ritualuri mentale (numărare, rugăciuni). "
        "Sunt executate ca răspuns la obsesii sau la reguli rigide, cu scopul de a reduce anxietatea, "
        "nu din plăcere sau liberă alegere."
    ),

    # ── 114 ── Exemple de compulsii (multi, corect: abc)
    (
        "✅ a) verificare repetată (uși, aragaz, fapte) — compulsie legată de îndoiala patologică. "
        "✅ b) spălare sau curățare excesivă — compulsie legată de frica de contaminare. "
        "✅ c) numărare, ordonare sau ritualuri mentale — compulsii mentale interne sau de ordonare. "
        "❌ d) evitarea gândurilor intruzive, fără ritual — evitarea cognitivă nu este o compulsie în sens tehnic. "
        "Compulsiile clasice din TOC includ verificarea repetată (combate îndoiala), spălarea excesivă (combate "
        "contaminarea) și ritualurile de ordonare sau numărare. "
        "Evitarea cognitivă simplă, fără ritual, nu constituie o compulsie, deși și aceasta poate menține tulburarea."
    ),

    # ── 115 ── Verificarea repetată a încuietorii (multi, corect: ab)
    (
        "✅ a) prevenirea unui eveniment catastrofal imaginar — logica magică: 'dacă nu verific, se va întâmpla ceva rău'. "
        "✅ b) reducerea anxietății generate de îndoială — compulsia are funcție de reglare anxioasă pe termen scurt. "
        "❌ c) plăcerea de a ordona obiectele — compulsiile nu sunt plăcute; sunt dictate de anxietate. "
        "❌ d) confirmarea unei amintiri reale incomplete — îndoiala obsesivă este irațională, nu bazată pe deficit real de memorie. "
        "Verificarea repetată răspunde îndoielii obsesive: 'dacă nu verific, se va produce un accident'. "
        "Paradoxal, verificarea repetată întărește îndoiala în loc să o rezolve, perpetuând ciclul TOC."
    ),

    # ── 116 ── Ritualurile pot deveni consumatoare de timp (multi, corect: ab)
    (
        "✅ a) rigide și consumatoare de timp — ritualurile tind să escaladeze în extensie și rigiditate. "
        "✅ b) atât de lungi încât afectează munca sau relațiile — disfuncția funcțională poate fi severă. "
        "❌ c) scurte și flexibile, fără suferință — în TOC sever, dimpotrivă, ritualurile sunt inflexibile. "
        "❌ d) absente la persoanele cu doar obsesii — pot apărea ritualuri mentale (ruminare, neutralizare). "
        "Ritualurile tind să se extindă în timp datorită sensibilizării și escaladării. "
        "Pot ajunge să ocupe mai mult de o oră pe zi, perturbând funcționarea profesională, socială și familială. "
        "Persoanele cu obsesii fără compulsii vizibile pot dezvolta totuși ritualuri mentale interne."
    ),

    # ── 117 ── Insight prezent, dar imposibil de rezistat (multi, corect: ab)
    (
        "✅ a) simte că trebuie să le execute oricum — imperativul anxios depășește conștiința rațională. "
        "✅ b) crede că previn un dezastru, deși legătura este nerealistă — logică magică persistentă. "
        "❌ c) nu are niciodată conștientizarea excesului — în TOC tipic insight-ul este parțial prezent. "
        "❌ d) nu resimte anxietate dacă nu le execută — dimpotrivă, blocarea ritualului generează anxietate marcată. "
        "Insight-ul (recunoașterea caracterului excesiv al ritualurilor) este prezent în majoritatea cazurilor de TOC, "
        "dar nu protejează persoana de imperativul anxios de a efectua compulsia. "
        "Conștientizarea rațională coexistă cu obligativitatea subiectivă, ceea ce generează suferință suplimentară."
    ),

    # ── 118 ── Obsesii = gânduri intruzive incontrolabile — TF (TF, corect: Adevărat)
    (
        "Adevărat. Obsesiile sunt gânduri, impulsuri sau imagini percepute ca intruzive, recurente și incontrolabile. "
        "Caracterul ego-distonic (nedorit, contrar valorilor persoanei) le distinge de simple preferințe sau de "
        "planificarea conștientă. "
        "Suferința generată de obsesii este un criteriu diagnostic central al TOC."
    ),

    # ── 119 ── Compulsiile nu sunt DOAR vizibile — TF (TF, corect: Fals)
    (
        "Fals. Compulsiile nu sunt exclusiv comportamente vizibile. "
        "Ele pot fi și ritualuri mentale interne, cum ar fi numărarea, repetarea mentală a unor fraze, rugăciunile "
        "sau verificarea mentală a unor fapte. "
        "Această formă este mai puțin vizibilă din exterior, dar la fel de perturbatoare funcțional și trebuie "
        "evaluată în procesul clinic."
    ),

    # ── 120 ── Criterii diagnostice pentru TOC (multi, corect: abc)
    (
        "✅ a) produc suferință marcată sau afectare funcțională — criteriu central de diagnostic. "
        "✅ b) consumă mult timp (de exemplu, peste o oră pe zi) — indicator al severității. "
        "✅ c) nu sunt explicate mai bine de altă tulburare sau substanță — necesită diagnostic diferențial. "
        "❌ d) apar doar în contextul consumului de alcool — dacă simptomele sunt cauzate de substanțe, diagnosticul de TOC este exclus. "
        "Diagnosticul de TOC necesită ca simptomele să genereze suferință semnificativă sau afectare funcțională, "
        "să consume timp substanțial și să nu fie mai bine explicate de alte tulburări sau substanțe. "
        "Simpla prezență a obsesiilor sau compulsiilor nu este suficientă pentru diagnostic."
    ),

    # ── 121 ── Debut TOC (multi, corect: ab)
    (
        "✅ a) gradual — debutul tipic este insidios, nu brusc. "
        "✅ b) în adolescență sau la începutul vârstei adulte — vârful de debut este în jur de 19-20 de ani. "
        "❌ c) obligatoriu după vârsta de 60 de ani — fals; debutul tardiv este rar. "
        "❌ d) brusc, după orice stres minor — debutul brusc este posibil, dar nu tipic. "
        "TOC debutează de regulă gradual, în adolescență sau la vârsta adultă tânără. "
        "Debutul după 35 de ani este mai rar și poate fi asociat cu comorbidități sau factori precipitanți specifici, "
        "justificând o evaluare medicală suplimentară."
    ),

    # ── 122 ── Prevalența TOC 2-3% (multi, corect: a)
    (
        "✅ a) aproximativ 2–3% — prevalența pe parcursul vieții acceptată în literatura de specialitate. "
        "❌ b) sub 0,1% — subestimare importantă a prevalenței reale. "
        "❌ c) peste 20% la adulți — supraestimare majoră. "
        "❌ d) identică cu cea a schizofreniei — schizofrenia are prevalență de aproximativ 1%, diferită de TOC. "
        "TOC afectează aproximativ 2-3% din populație pe parcursul vieții, ceea ce îl plasează printre cele mai "
        "frecvente tulburări psihice. "
        "Este recunoscut de Organizația Mondială a Sănătății ca una dintre primele zece cauze de dizabilitate."
    ),

    # ── 123 ── Excluderi diagnostice (multi, corect: abc)
    (
        "✅ a) efectelor substanțelor sau medicației — simptomele induse de substanțe exclud diagnosticul de TOC. "
        "✅ b) unei alte tulburări mentale — de exemplu, ritualurile din tulburarea de spectru autist. "
        "✅ c) unei afecțiuni medicale generale — unele afecțiuni neurologice pot mima TOC. "
        "❌ d) obsesiilor și compulsiilor care definesc tulburarea — acestea sunt simptomele centrale, nu excluderi. "
        "Diagnosticul diferențial al TOC necesită excluderea altor cauze: substanțe, tulburări comorbide sau afecțiuni medicale. "
        "Un diagnostic precis ghidează alegerea intervenției și evitarea tratamentelor inadecvate."
    ),

    # ── 124 ── Ritual previne dezastrul — legătură iraționala (multi, corect: ab)
    (
        "✅ a) legătura cu evenimentul este nerealistă sau excesivă — logica magică specifică TOC. "
        "✅ b) convingerea persistă în ciuda lipsei de dovezi — rezistentă la argumentare logică. "
        "❌ c) ritualul este întotdeauna logic și proporțional — fals în TOC; ritualul este excesiv prin definiție. "
        "❌ d) anxietatea nu scade niciodată după ritual — scade temporar, ceea ce întărește compulsia. "
        "Compulsia produce o reducere temporară a anxietății, ceea ce o întărește prin condiționare negativă. "
        "Legătura dintre ritual și evenimentul temut este de tip magic ('dacă număr până la 10, mama nu se va îmbolnăvi'). "
        "Persoana poate recunoaște că este lipsită de sens, dar nu poate rezista imperativului."
    ),

    # ── 125 ── TOC 2-3% din populație — TF (TF, corect: Adevărat)
    (
        "Adevărat. TOC afectează aproximativ 2-3% din populație de-a lungul vieții, o prevalență considerabilă "
        "care îl plasează printre tulburările psihice cu impact funcțional major. "
        "Simptomele pot fi debilitante și sunt adesea asociate cu suferință marcată, dacă nu sunt recunoscute și tratate adecvat."
    ),

    # ── 126 ── Tulburarea dismorfică corporală (multi, corect: ab)
    (
        "✅ a) preocupare excesivă pentru defecte percepute ale aspectului fizic — caracteristica definitorie a TDC. "
        "✅ b) verificare în oglindă sau căutare de reasigurări — comportamente asociate frecvente. "
        "❌ c) smulgerea compulsivă a părului — aceasta definește tricotilomania. "
        "❌ d) dificultatea de a arunca obiecte — aceasta definește tulburarea de acumulare. "
        "Tulburarea dismorfică corporală face parte din spectrul TOC și implică preocupare persistentă față de un "
        "defect fizic perceput (de regulă minor sau inexistent). "
        "Comportamentele asociate, cum ar fi verificarea repetată în oglindă, pot fi extrem de consumatoare de timp."
    ),

    # ── 127 ── Tulburarea de acumulare (multi, corect: ab)
    (
        "✅ a) dificultate de a arunca obiecte, indiferent de valoare — trăsătura centrală a tulburării. "
        "✅ b) aglomerarea severă a locuinței la unii pacienți — consecință comportamentală directă. "
        "❌ c) ritualuri de spălare pentru contaminare — specifice TOC cu obsesii de contaminare. "
        "❌ d) gânduri sexuale intruzive nedorite — obsesie din TOC clasic, nu din tulburarea de acumulare. "
        "Tulburarea de acumulare compulsivă se caracterizează prin incapacitatea de a arunca obiecte, datorită "
        "distresului anticipat la gândul pierderii lor. "
        "DSM-5 o clasifică ca tulburare separată, deși poate fi comorbidă cu TOC."
    ),

    # ── 128 ── Tricotilomania și dermatilomania (multi, corect: abd)
    (
        "✅ a) comportamente repetitive legate de păr sau piele — caracteristica definitorie a acestor tulburări. "
        "✅ b) dificultatea de a opri actul, cu daune vizibile — pierderea controlului cu consecințe fizice. "
        "❌ c) obsesii de contaminare ca singur simptom — nu caracterizează tricotilomania sau dermatilomania. "
        "✅ d) apartenența la spectrul tulburărilor legate de controlul impulsurilor — clasificare diagnostică actuală. "
        "Tricotilomania (smulgerea compulsivă a părului) și dermatilomania (excoriația compulsivă a pielii) "
        "fac parte din spectrul comportamentelor repetitive centrate pe corp. "
        "Impulsul de a smulge sau excoria este dificil de controlat și duce la daune fizice vizibile."
    ),

    # ── 129 ── Perechi tulburare-caracteristică (multi, corect: abc)
    (
        "✅ a) tulburarea dismorfică corporală — defect perceput al aspectului — asociere corectă. "
        "✅ b) tulburarea de acumulare — dificultate de a arunca obiecte — asociere corectă. "
        "✅ c) tricotilomania — smulgerea compulsivă a părului — asociere corectă. "
        "❌ d) tulburarea obsesiv-compulsivă — delir persecutoriu persistent — fals; TOC nu implică delir. "
        "Fiecare tulburare din spectrul TOC are o caracteristică definitorie distinctă. "
        "TOC clasic nu implică delir persecutoriu; dacă acesta este prezent, trebuie investigată o tulburare psihotic comorbidă "
        "sau un diagnostic alternativ."
    ),

    # ── 130 ── Etiologia TOC (multi, corect: abc)
    (
        "✅ a) biologici (circuite fronto-striatale) — neuroimagistica arată hiperactivitate în aceste circuite. "
        "✅ b) cognitivi și comportamentali — responsabilitate exagerată, fuziune gând-acțiune, evitare. "
        "✅ c) genetici, cu contribuție din studii pe gemeni — heritabilitate estimată la 40-65%. "
        "❌ d) exclusiv psihodinamici, fără bază biologică — modelul actual este multifactorial, cu bază biologică solidă. "
        "Etiologia TOC este multifactorială. Studiile de neuroimagistică evidențiază hiperactivitate în circuitele "
        "fronto-striatale (cortex orbitofrontal-nucleul caudat). "
        "Studiile pe gemeni confirmă o contribuție genetică moderată, completată de factori cognitivi și comportamentali."
    ),

    # ── 131 ── Responsabilitatea exagerată (multi, corect: ab)
    (
        "✅ a) convingerea că trebuie să prevină rezultate negative — datoria morală percepută excesiv. "
        "✅ b) sentimentul că are putere morală peste evenimente improbabile — control supraevaluat. "
        "❌ c) absența oricărei vinovății după ritual — vinovăția poate persista și după ritual. "
        "❌ d) acceptarea limitelor reale ale controlului — contrar constructului de responsabilitate exagerată. "
        "Responsabilitatea exagerată, concept central în modelul cognitiv Salkovskis, descrie convingerea că persoana "
        "are datoria de a preveni orice rezultat negativ și că are o influență cauzală sau morală asupra unor "
        "evenimente improbabile. "
        "Aceasta alimentează ritualuri de verificare sau neutralizare."
    ),

    # ── 132 ── Fuziunea gând-acțiune (multi, corect: ab)
    (
        "✅ a) ideea că a gândi ceva echivalează cu a face acțiunea — bias cognitiv central în TOC. "
        "✅ b) convingere morală sau magică legată de gânduri intruzive — 'a gândi e la fel de rău ca a face'. "
        "❌ c) capacitatea de a distinge clar gândul de fapt — tocmai această capacitate este afectată. "
        "❌ d) absența oricărei reacții emoționale la gânduri — dimpotrivă, gândurile generează anxietate marcată. "
        "Fuziunea gând-acțiune este un bias cognitiv specific TOC: convingerea că a gândi ceva crește probabilitatea "
        "evenimentului (fuziune de probabilitate) sau că a gândi este moral echivalent cu a face (fuziune morală). "
        "Aceasta amplifică suferința legată de gândurile intruzive."
    ),

    # ── 133 ── Contaminarea psihică (multi, corect: ab)
    (
        "✅ a) sentiment de murdărie fără contact fizic contaminant — caracteristica definitorie. "
        "✅ b) asociere cu rușine, vinovăție sau amintiri aversive — sursa psihică a 'murdăriei'. "
        "❌ c) spălarea mâinilor după atingerea unui obiect — aceasta este contaminarea fizică, nu psihică. "
        "❌ d) frică realistă de bacterii dovedite în laborator — frica realistă nu este simptom de TOC. "
        "Contaminarea psihică diferă de contaminarea fizică prin absența contactului obiectiv cu o substanță. "
        "Sentimentul de murdărie provine din amintiri aversive, rușine sau experiențe de violare a integrității. "
        "Spălarea este ineficientă, deoarece 'murdăria' este de natură mentală, nu fizică."
    ),

    # ── 134 ── Supresia gândurilor — efect de rebound (multi, corect: ab)
    (
        "✅ a) crește frecvența gândurilor (efect de rebound) — paradoxul descris de Wegner. "
        "✅ b) întărește asocierea cu emoții negative — supresia menține legătura gând-anxietate. "
        "❌ c) elimina definitiv obsesiile fără ritual — contrar dovezilor experimentale. "
        "❌ d) reduce anxietatea pe termen lung, garantat — efectul este paradoxal, nu benefic. "
        "Efectul de rebound ('ursul alb') arată că tentativa deliberată de a suprima un gând crește frecvența sa ulterioară. "
        "În TOC, supresia activă a obsesiilor menține ciclul și consolidează asocierea lor cu anxietatea, "
        "fără a aduce ameliorare pe termen lung."
    ),

    # ── 135 ── Deficite de memorie în TOC (multi, corect: abc)
    (
        "✅ a) încredere scăzută în validitatea amintirilor — nu un deficit obiectiv, ci neîncredere subiectivă. "
        "✅ b) dificultate de a diferenția acțiunea reală de cea imaginată — 'am închis gazul sau am imaginat-o?'. "
        "✅ c) susținerea verificării repetate — neîncrederea în memorie justifică compulsia de verificare. "
        "❌ d) memorie perfectă care exclude orice îndoială — exact contrariul; îndoiala patologică persiste. "
        "Paradoxal, persoanele cu TOC nu au neapărat un deficit obiectiv de memorie, ci o încredere scăzută în "
        "propriile amintiri. "
        "Această neîncredere alimentează verificarea repetată, care, în loc să rezolve îndoiala, o întărește progresiv."
    ),

    # ── 136 ── Tratamentul de primă linie TOC (multi, corect: abd)
    (
        "✅ a) TCC cu expunere și prevenirea răspunsului (ERP) — tratament psihologic de primă linie. "
        "✅ b) inhibitori selectivi ai recaptării serotoninei (ISRS) — tratament farmacologic de primă linie. "
        "❌ c) psihanaliză clasică ca singură intervenție obligatorie — nu are dovezi ca tratament de primă linie pentru TOC. "
        "✅ d) restructurare cognitivă a convingerilor despre responsabilitate — componentă esențială a TCC. "
        "Ghidurile clinice internaționale recomandă TCC cu ERP și ISRS (fluoxetina, sertralina, fluvoxamina) "
        "ca tratamente de primă linie pentru TOC. "
        "ERP implică expunerea la stimulii obsesivi și prevenirea ritualurilor, permițând habituarea anxietății "
        "și infirmarea convingerilor catastrofice."
    ),

    # ── 137 ── Expunerea cu prevenirea răspunsului — ERP (multi, corect: abd)
    (
        "✅ a) confruntare treptată cu factorii declanșatori — ierarhia de expuneri ghidează procesul. "
        "✅ b) blocarea ritualurilor până când anxietatea scade — habituarea naturală este mecanismul central. "
        "❌ c) confirmarea ritualurilor pentru a reduce stresul — contrar principiului ERP; ritualurile sunt blocate. "
        "✅ d) infirmarea treptată a convingerilor catastrofice — experiența directă infirmă predicțiile negative. "
        "ERP funcționează prin expunerea graduală la stimulii care declanșează obsesia, fără a permite executarea compulsiei. "
        "Persoana învață că anxietatea scade natural și că evenimentul temut nu se produce, "
        "infirmând convingerile catastrofice susținute de ritualuri."
    ),

    # ── 138 ── Regula de finalizare afectivă (multi, corect: ab)
    (
        "✅ a) regula de încheiere legată de stare afectivă, nu de criteriu obiectiv — 'simt că e gata'. "
        "✅ b) perseverența comportamentală care menține tulburarea — ciclul ritual nu are un final obiectiv. "
        "❌ c) succesul expunerii fără disconfort — nu descrie expunere; descrie ritualul nerezolvat. "
        "❌ d) absența responsabilității exagerate — dimpotrivă, responsabilitatea exagerată explică comportamentul. "
        "Regula de finalizare afectivă (not just right experience) descrie fenomenul în care persoana nu poate "
        "opri ritualul până nu 'simte că e complet', independent de criterii obiective. "
        "Aceasta reflectă dependența de starea afectivă ca indicator de securitate și perpetuează ciclul compulsiv."
    ),

    # ── 139 ── Afirmații greșite despre TOC (multi, corect: a)
    (
        "✅ a) înseamnă doar ordine și perfecționism, fără suferință — mitul popular cel mai dăunător clinic. "
        "❌ b) ritualurile reduc anxietatea pe termen scurt, dar o mențin pe termen lung — afirmație corectă. "
        "❌ c) inhibitorii selectivi ai serotoninei pot fi utili — afirmație corectă, sunt tratament de primă linie. "
        "❌ d) fuziunea gând-acțiune poate susține compulsia — afirmație corectă. "
        "Un mit comun este că TOC înseamnă a fi 'ordonat și perfecționist'. "
        "TOC real implică obsesii intruzive nedorite și compulsii care cauzează suferință marcată și afectare funcțională "
        "semnificativă, diferite fundamental de simplele preferințe pentru ordine."
    ),

    # ---------------------------------------------------------------------------
    # ANXIETATE (index 140–189, itemi 0–49 din ANXIETATE_ITEMS)
    # ---------------------------------------------------------------------------

    # ── 140 ── Caracteristicile tulburărilor anxioase (multi, corect: ab)
    (
        "✅ a) frică, îngrijorare sau incertitudine excesivă — nucleul tulburărilor anxioase. "
        "✅ b) răspuns anxios disproporționat sau persistent — patologic prin intensitate și durată. "
        "❌ c) episoade de elație și grandiozitate — specifice maniei, nu tulburărilor anxioase. "
        "❌ d) halucinații persistente, fără insight — specific psihozei. "
        "Tulburările anxioase implică frică sau îngrijorare care depășesc proporțional amenințarea reală sau sunt "
        "disproportionate față de aceasta. "
        "Răspunsul anxios devine patologic prin persistență, intensitate și impactul funcțional negativ."
    ),

    # ── 141 ── Consecințele tulburărilor anxioase (multi, corect: ab)
    (
        "✅ a) sănătății fizice și funcționării profesionale — anxietatea cronică afectează sistemele corporale. "
        "✅ b) relațiilor și calității vieții — evitarea și tensiunea perturbă relațiile interpersonale. "
        "❌ c) inteligenței generale, în mod obligatoriu — nu există o relație cauzală directă. "
        "❌ d) memoriei pe termen lung, ca simptom central — nu este simptom central al tulburărilor anxioase. "
        "Tulburările anxioase pot afecta calitatea somnului, sănătatea cardiovasculară, productivitatea profesională "
        "și relațiile interpersonale. "
        "Impactul funcțional este unul dintre criteriile de diagnostic și principala motivație pentru tratament."
    ),

    # ── 142 ── Procese comune în tulburările anxioase (multi, corect: abc)
    (
        "✅ a) simptome fiziologice de panică — activare autonomă (palpitații, transpirație, tremur). "
        "✅ b) prejudecăți cognitive și selectarea stimulilor amenințători — bias atențional spre pericol. "
        "✅ c) evitare și perseverarea gândurilor anxioase — procese menținătoare comune. "
        "❌ d) absența oricărei componente fiziologice — fals; tulburările anxioase au o componentă fiziologică centrală. "
        "Modelele transdiagnostice identifică procese comune: hipervigilență față de pericol, bias în procesarea "
        "informațiilor amenințătoare, evitare comportamentală și cognitivă, și activare fiziologică de tip anxios. "
        "Aceste procese susțin atât evaluarea cât și tratamentul transdiagnostic."
    ),

    # ── 143 ── Comorbiditate în tulburările anxioase (multi, corect: abc)
    (
        "✅ a) alte tulburări anxioase — comorbiditatea intra-anxioasă este frecventă. "
        "✅ b) episoade depresive — aproximativ 50% dintre pacienții anxioși prezintă și depresie. "
        "✅ c) tulburarea obsesiv-compulsivă, în unele cazuri — posibilă asociere, deși TOC e clasificat separat. "
        "❌ d) schizofrenia, ca regulă diagnostică — nu există o asociere sistematică cu psihozelele. "
        "Tulburările anxioase au comorbiditate ridicată între ele și cu depresia. "
        "Studiile epidemiologice arată că aproximativ 50% dintre persoanele cu o tulburare anxioasă îndeplinesc criteriile "
        "pentru cel puțin o altă tulburare psihică, ceea ce complică diagnosticul și tratamentul."
    ),

    # ── 144 ── Amenințare reală și iminentă — TF (TF, corect: Fals)
    (
        "Fals. Tulburările anxioase implică deseori o amenințare percepută care este disproporționată față de "
        "pericolul real sau absența unui pericol obiectiv identificabil. "
        "Tocmai caracterul excesiv, neproporțional și persistent al fricii față de stimulii reali sau imaginar este "
        "ceea ce definește răspunsul anxios ca patologic."
    ),

    # ── 145 ── Experiențe timpurii și vulnerabilitate — TF (TF, corect: Adevărat)
    (
        "Adevărat. Experiențele timpurii adverse, cum ar fi atașamentul nesigur, evenimentele traumatice din copilărie "
        "sau stiluri parentale anxioase, pot crește vulnerabilitatea la dezvoltarea tulburărilor anxioase. "
        "Aceste experiențe contribuie la formarea unor scheme cognitive dezadaptative și modele emoționale "
        "de reacție la pericol."
    ),

    # ── 146 ── Fobia specifică — definiție (multi, corect: a)
    (
        "✅ a) un obiect sau o situație specifică — element definitoriu al fobiei specifice. "
        "❌ b) orice interacțiune socială, fără excepție — aceasta definește tulburarea anxioasă socială. "
        "❌ c) îngrijorare generalizată despre viitor — caracteristică TAG, nu fobiei specifice. "
        "❌ d) atacuri de panică neașteptate, fără context — caracteristice tulburării de panică. "
        "Fobia specifică este definită prin frica intensă și disproporționată față de un obiect sau o situație "
        "bine-definită (animale, înălțimi, sânge, zbor etc.). "
        "Specificitatea stimulului fobic o distinge clar de tulburarea anxioasă socială sau de panică."
    ),

    # ── 147 ── Stimuli fobici (multi, corect: abc)
    (
        "✅ a) animale, înălțimi sau zbor — subtipurile animale, mediu natural și situațional. "
        "✅ b) injecții, sânge sau proceduri medicale — subtipul sânge-injecții-leziuni. "
        "✅ c) spații închise sau situații specifice — subtipul situațional. "
        "❌ d) orice loc public, fără stimul concret — aceasta descrie agorafobia, nu fobia specifică. "
        "DSM-5 clasifică fobia specifică în subtipuri: animale, mediu natural, sânge-injecții-leziuni, situațional "
        "și alte fobii. "
        "Fobia față de spații publice fără un stimul concret identificabil este mai degrabă agorafobia."
    ),

    # ── 148 ── Criterii fobie specifică (multi, corect: abc)
    (
        "✅ a) frică imediată și disproporționată față de stimul — răspuns anxios prompt la expunere. "
        "✅ b) evitare sau suportare cu frică intensă — impact comportamental. "
        "✅ c) durată de minimum șase luni — criteriu temporal de diagnostic. "
        "❌ d) prezența obligatorie a atacurilor de panică — acestea pot apărea, dar nu sunt criteriu obligatoriu. "
        "Diagnosticul de fobie specifică necesită frică imediată la expunere, evitare sau suportare cu suferință intensă, "
        "durată de cel puțin 6 luni și afectare funcțională semnificativă. "
        "Atacurile de panică pot apărea situațional, dar nu sunt un criteriu obligatoriu."
    ),

    # ── 149 ── Subtipuri fobie specifică (multi, corect: abc)
    (
        "✅ a) animale și mediu natural — subtipuri recunoscute în clasificările actuale. "
        "✅ b) sânge, injecții și leziuni — subtip cu răspuns fiziologic distinct (vasovagal). "
        "✅ c) situațional și alte fobii — avioane, lifturi, spații închise și alte stimuli. "
        "❌ d) socială și generalizată — acestea sunt tulburări distincte, nu subtipuri ale fobiei specifice. "
        "Fobia specifică se clasifică în subtipuri pentru a orienta tratamentul: subtipul sânge-injecții-leziuni "
        "necesită, de exemplu, tehnica tensionării aplicate pentru a preveni reacția vasovagală. "
        "Fobia socială și TAG sunt entități diagnostice separate."
    ),

    # ── 150 ── Studenta care evită lifturile (multi, corect: a)
    (
        "✅ a) fobie specifică de tip situațional — frica de a rămâne blocată în lift, cu insight prezent. "
        "❌ b) tulburare de panică, ca diagnostic principal — nu sunt descrise atacuri neașteptate recurente. "
        "❌ c) tulburare obsesiv-compulsivă cu ritualuri — nu sunt descrise obsesii sau compulsii. "
        "❌ d) tulburare anxioasă generalizată izolată — TAG implică îngrijorare politemă, nu un singur stimul. "
        "Frica de lifturi bazată pe teama de a rămâne blocată este tipică fobiei situaționale. "
        "Recunoașterea că frica este excesivă (insight prezent) este consistent cu diagnosticul de fobie specifică "
        "și orientează tratamentul spre expunere gradată."
    ),

    # ── 151 ── Fobia de sânge/injecții (multi, corect: ab)
    (
        "✅ a) reacție fiziologică specifică, uneori leșin — răspunsul vasovagal bifazic este caracteristic. "
        "✅ b) evitarea stimulului sau suportarea cu frică intensă — criteriu comportamental comun fobiei. "
        "❌ c) absența oricărei componente corporale — fals; componenta fiziologică este distinctivă. "
        "❌ d) prezența obligatorie a agorafobiei — nu există această cerință diagnostică. "
        "Fobia de sânge-injecții-leziuni este unică prin răspunsul vasovagal bifazic: activare inițială urmată de "
        "scăderea bruscă a tensiunii arteriale și a frecvenței cardiace, care poate duce la leșin. "
        "Tehnica tensionării aplicate (applied tension) este recomandată pentru a contracara această reacție."
    ),

    # ── 152 ── Etiologia fobiei specifice (multi, corect: abc)
    (
        "✅ a) condiționarea clasică și experiențe traumatice — dobândire directă prin experiență aversivă. "
        "✅ b) învățare observațională și informații amenințătoare — condiționare vicariată și verbală. "
        "✅ c) vulnerabilitate biologică pentru anumite stimuli — prepared learning (stimuli evolutiv relevanți). "
        "❌ d) exclusiv o cauză psihanalitică unică, demonstrată — modelele moderne sunt multifactoriale. "
        "Fobia specifică poate fi dobândită prin condiționare clasică directă (experiență traumatică), observarea "
        "fricii altei persoane sau informații verbale amenințătoare. "
        "Există și o vulnerabilitate biologică preparată pentru stimuli evolutiv relevanți (șerpi, înălțimi, sânge)."
    ),

    # ── 153 ── Experimentul Little Albert — TF (TF, corect: Adevărat)
    (
        "Adevărat. Experimentul lui Little Albert (Watson și Rayner, 1920) a demonstrat că un copil poate fi "
        "condiționat să se teamă de un șobolan alb (stimul neutru), prin asocierea repetată a acestuia cu un "
        "zgomot puternic (stimul aversiv necondiționat). "
        "Acesta a oferit un argument fundamental pentru modelul condiționării clasice în dobândirea fobiilor "
        "și a influențat profund psihologia clinică."
    ),

    # ── 154 ── Tratamentul fobiei specifice (multi, corect: ab)
    (
        "✅ a) expunere gradată sau intensivă la stimulul fobic — cel mai eficient tratament dovedit. "
        "✅ b) reducerea evitării și infirmarea convingerilor catastrofice — mecanisme terapeutice centrale. "
        "❌ c) evitarea permanentă a stimulului — nu rezolvă fobia, ci o menține prin consolidarea evitării. "
        "❌ d) psihanaliză clasică ca singură intervenție obligatorie — nu are dovezi de eficiență ca tratament principal. "
        "Expunerea este tratamentul cu cele mai solide dovezi pentru fobia specifică. "
        "Poate fi gradată (ierarhie de expuneri cu anxietate crescătoare) sau intensivă (flooding). "
        "Obiectivul este habituarea răspunsului anxios și infirmarea predicțiilor catastrofice prin experiență directă."
    ),

    # ── 155 ── Intervenții în fobia specifică (multi, corect: abc)
    (
        "✅ a) desensibilizare sistematică și flooding — tehnici de expunere cu paradigme diferite. "
        "✅ b) restructurare cognitivă și experimente comportamentale — abordare cognitiv-comportamentală. "
        "✅ c) contracondiționare — asocierea stimulului fobic cu o experiență pozitivă. "
        "❌ d) confirmarea evitării ca strategie centrală — evitarea menține și întărește fobia. "
        "Desensibilizarea sistematică (Wolpe) combină relaxarea cu expunerea graduală. "
        "Flooding expune direct la stimulul maxim. "
        "Restructurarea cognitivă abordează convingerile catastrofice, iar contracondiționarea creează "
        "asocieri noi, incompatibile cu frica."
    ),

    # ── 156 ── Tulburarea anxioasă socială — definiție (multi, corect: ab)
    (
        "✅ a) situații sociale sau de performanță — contextul social este element definitoriu. "
        "✅ b) evaluare negativă de către ceilalți — frica de judecată este nucleul cognitiv al TAS. "
        "❌ c) stimuli fobici concreți, cum ar fi animalele — aceasta definește fobia specifică. "
        "❌ d) atacuri de panică neașteptate, fără context social — caracteristice tulburării de panică. "
        "Tulburarea anxioasă socială se caracterizează prin frica intensă față de situații sociale sau de performanță, "
        "în special frica de a fi judecat negativ, criticat sau umilitor. "
        "Contextul social este definitoiu și o distinge de celelalte tulburări anxioase."
    ),

    # ── 157 ── Evitare în TAS (multi, corect: abd)
    (
        "✅ a) conversații, mâncat sau băut în public — situații frecvent evitate în TAS. "
        "✅ b) vorbitul în fața altora sau situațiile de observare — frică de evaluare publică. "
        "❌ c) orice activitate solitară, fără contact social — activitățile solitare sunt de regulă confortabile. "
        "✅ d) interacțiunile în care se simte evaluată — criteriul evaluativ este central. "
        "Persoanele cu TAS evită o gamă largă de situații în care se simt observate sau judecate: prezentări publice, "
        "mese în public, conversații cu autorități sau persoane necunoscute. "
        "Activitățile solitare sunt de regulă confortabile, spre deosebire de situațiile sociale."
    ),

    # ── 158 ── Criterii TAS (multi, corect: abc)
    (
        "✅ a) frică marcată de interacțiuni sociale — caracteristică centrală. "
        "✅ b) evitare sau suportare cu anxietate intensă — impact comportamental. "
        "✅ c) durată de cel puțin șase luni — criteriu temporal de diagnostic. "
        "❌ d) prezența obligatorie a agorafobiei — TAS și agorafobia sunt diagnostice separate care pot coexista. "
        "Diagnosticul de TAS necesită frică marcată față de situații sociale, evitarea sau suportarea cu suferință intensă, "
        "durată de cel puțin 6 luni și afectare funcțională semnificativă. "
        "Agorafobia nu este un criteriu obligatoriu."
    ),

    # ── 159 ── Adolescent care refuză să prezinte în clasă (multi, corect: a)
    (
        "✅ a) tulburare anxioasă socială — frică de evaluare negativă în context educațional, persistentă un an. "
        "❌ b) fobie specifică de tip animalier — nu există un stimul fobic concret de tip animal. "
        "❌ c) tulburare de panică, fără componentă socială — nu sunt descrise atacuri neașteptate recurente. "
        "❌ d) tulburare obsesiv-compulsivă cu verificări — nu sunt descrise obsesii sau compulsii. "
        "Tabloul clinic descrie frica de evaluare negativă specific contextualizată social (prezentare în clasă), "
        "simptome persistente de peste un an cu impact funcțional. "
        "Acestea sunt caracteristice TAS; debutul în adolescență este tipic pentru această tulburare."
    ),

    # ── 160 ── Factori de risc TAS (multi, corect: abc)
    (
        "✅ a) inhibiție comportamentală la copilărie — predictor timpuriu documentat pentru TAS. "
        "✅ b) părinți anxioși sau protecție excesivă — modelarea parentală a anxietății sociale. "
        "✅ c) timiditate și retragere în situații noi — trăsătură temperamentală predispozantă. "
        "❌ d) absența oricărei componente familiale — studiile arată transmitere familială semnificativă. "
        "Inhibiția comportamentală (tendința de retragere în fața noutăților) este un predictor timpuriu al TAS. "
        "Modelarea parentală a anxietății și supraprotecția pot contribui la formarea unor scheme negative despre "
        "propria competență socială și despre evaluarea celorlalți."
    ),

    # ── 161 ── Procese cognitive în TAS (multi, corect: abc)
    (
        "✅ a) predicții negative despre evenimente sociale — anticiparea eșecului social. "
        "✅ b) atenție excesivă asupra propriei persoane — autofocalizare care îngreunează performanța. "
        "✅ c) procesare negativă după evenimentul social — ruminare post-eveniment și subminarea succesului. "
        "❌ d) interpretarea performanței ca excelentă — contrar; TAS implică autoevaluare negativă marcată. "
        "Modelul Clark și Wells descrie un ciclu cognitiv: anticipare negativă, autofocalizare în situație, "
        "comportamente de siguranță, și procesare negativă post-eveniment (ruminarea după interacțiune). "
        "Atenția excesivă pe sine îngreunează performanța efectivă și confirmă predicțiile negative."
    ),

    # ── 162 ── Terapia Clark-Wells în TAS (multi, corect: abc)
    (
        "✅ a) reducerea comportamentelor de siguranță — acestea mențin credința în pericol social. "
        "✅ b) mutarea atenției spre exterior și feedback video — corectarea autofocalizării și a imaginii catastrofice. "
        "✅ c) experimente comportamentale și restructurare post-eveniment — testarea predicțiilor negative. "
        "❌ d) evitarea situațiilor sociale ca obiectiv principal — contrar; obiectivul este expunerea și angajarea socială. "
        "Modelul Clark-Wells intervine prin: reducerea comportamentelor de siguranță, redirecționarea atenției spre "
        "exterior (reducerea autofocalizării), feedback video pentru a infirma imaginea catastrofică despre sine "
        "și restructurarea procesărilor post-eveniment negative."
    ),

    # ── 163 ── TCC în TAS (multi, corect: abc)
    (
        "✅ a) expunere la situații sociale — confruntarea graduală cu situațiile evitate. "
        "✅ b) training al abilităților sociale — util pentru persoanele cu deficite reale de abilități. "
        "✅ c) restructurare cognitivă — infirmarea convingerilor negative despre evaluarea celorlalți. "
        "❌ d) izolarea completă de stimuli sociali — contrar obiectivelor terapiei; ar perpetua evitarea. "
        "TCC pentru TAS combină expunerea treptată la situații sociale cu antrenamentul abilităților sociale "
        "(pentru cei cu deficite reale) și restructurarea convingerilor negative. "
        "Izolarea ar perpetua evitarea și ar agrava progresiv simptomele."
    ),

    # ── 164 ── Debut timpuriu TAS — TF (TF, corect: Adevărat)
    (
        "Adevărat. TAS debutează de regulă în adolescență sau la începutul vârstei adulte, frecvent înainte de 18 ani. "
        "Aceasta coincide cu perioada în care conștientizarea socială și presiunea evaluativă a grupului de egali "
        "sunt la maxim, ceea ce face adolescenții deosebit de vulnerabili. "
        "Diagnosticul precoce permite intervenție înainte de consolidarea evitării și impactului funcțional."
    ),

    # ── 165 ── Medicație și TCC în TAS — TF (TF, corect: Adevărat)
    (
        "Adevărat. Medicația (de exemplu, ISRS) poate reduce rapid simptomele TAS și poate facilita participarea la terapie, "
        "dar nu produce modificări cognitive de durată prin sine. "
        "Intervențiile TCC urmăresc schimbări cognitive stabile și reducerea evitării, diminuând astfel riscul de "
        "recădere după oprirea medicamentelor."
    ),

    # ── 166 ── Tulburarea de panică — definiție (multi, corect: abc)
    (
        "✅ a) atacuri repetate de panică, bruște și intense — caracteristică definitorie. "
        "✅ b) simptome fiziologice: palpitații, transpirație, tremur — activare somatică marcată. "
        "✅ c) frică de moarte, pierdere a controlului sau 'a înnebuni' — interpretare catastrofică a senzațiilor. "
        "❌ d) îngrijorare cronică despre mai multe domenii, fără atacuri — caracteristică TAG, nu panicii. "
        "Tulburarea de panică se caracterizează prin atacuri recurente, neașteptate, cu simptome fiziologice intense "
        "și interpretare catastrofică. "
        "Îngrijorarea cronică politemă, fără atacuri discrete, este caracteristică TAG."
    ),

    # ── 167 ── Simptomele unui atac de panică (multi, corect: abc)
    (
        "✅ a) dificultăți respiratorii, greață sau amețeală — simptome fiziologice frecvente în panică. "
        "✅ b) depersonalizare sau derealizare — pot apărea și adaugă dezorientare. "
        "✅ c) hiperventilație și senzație de sufocare — contribuie la ciclul de amplificare al panicii. "
        "❌ d) lentoare psihomotorie și anhedonie prelungită — simptome depresive, nu de panică. "
        "Un atac de panică implică un vârf de frică intensă cu multiple simptome fiziologice și cognitive. "
        "Depersonalizarea și derealizarea pot agrava senzația de pierdere a controlului. "
        "Lentorea psihomotorie și anhedonia sunt caracteristice depresiei, nu panicii."
    ),

    # ── 168 ── Criterii pentru tulburarea de panică (multi, corect: abc)
    (
        "✅ a) atacuri recurente și neașteptate — element central al diagnosticului. "
        "✅ b) cel puțin o lună de îngrijorare persistentă față de atacuri — îngrijorarea anticipatorie. "
        "✅ c) schimbări comportamentale dezadaptative legate de atacuri — evitare, restricție activitate. "
        "❌ d) prezența obligatorie a agorafobiei — agorafobia este un diagnostic distinct care poate fi comorbid. "
        "Diagnosticul tulburării de panică necesită atacuri recurente neașteptate, urmate de cel puțin o lună de "
        "îngrijorare anticipatorie sau modificări comportamentale semnificative. "
        "Agorafobia poate fi comorbidă, dar nu este un criteriu obligatoriu."
    ),

    # ── 169 ── Pacienta care evită metroul (multi, corect: a)
    (
        "✅ a) agorafobie — frica de situații de 'prindere' fără posibilitate de scăpare sau ajutor. "
        "❌ b) fobie specifică de tip animalier — nu există un stimul fobic concret de tip animal. "
        "❌ c) tulburare anxioasă generalizată izolată — TAG implică îngrijorare politemă, nu frica de prindere. "
        "❌ d) tulburare obsesiv-compulsivă cu ritualuri — nu sunt descrise obsesii sau ritualuri. "
        "Frica de situații de 'prindere' (transport public, cozi, mulțimi) în care ar fi dificil să scape sau "
        "să primească ajutor în caz de panică este definitorie pentru agorafobie. "
        "Se distinge de fobia de metrou prin focusul pe imposibilitatea scăpării, nu pe un stimul concret."
    ),

    # ── 170 ── Agorafobia — definiție (multi, corect: abc)
    (
        "✅ a) locuri unde persoana se simte prinsă sau nesigură — nucleul fricii agorafobice. "
        "✅ b) situații în care ajutorul ar putea lipsi la panică — context de vulnerabilitate percepută. "
        "✅ c) transport public, spații deschise, cozi sau mulțimi — tipuri frecvente de situații evitate. "
        "❌ d) un singur obiect specific, cum ar fi șerpii — aceasta definește fobia specifică. "
        "Agorafobia implică frica față de o gamă diversă de situații în care persoana s-ar simți prinsă sau lipsită "
        "de ajutor dacă ar apărea panică sau simptome similare. "
        "DSM-5 specifică că trebuie să vizeze cel puțin două tipuri de situații."
    ),

    # ── 171 ── Criterii agorafobie (multi, corect: abc)
    (
        "✅ a) frică față de cel puțin două tipuri de situații — criteriu specific DSM-5. "
        "✅ b) evitare sau trăire cu frică intensă — impact comportamental semnificativ. "
        "✅ c) durată de cel puțin șase luni — criteriu temporal de diagnostic. "
        "❌ d) prezența obligatorie a unui stimul fobic unic — dimpotrivă, agorafobia vizează multiple contexte. "
        "DSM-5 specifică că agorafobia presupune frică față de minimum două categorii de situații "
        "(transport public, spații deschise, locuri aglomerate, cozi, ieșire singur din casă), "
        "durată de cel puțin 6 luni și afectare funcțională semnificativă."
    ),

    # ── 172 ── Tulburarea de panică și agorafobia (multi, corect: ab)
    (
        "✅ a) probleme înrudite, dar separabile diagnostic — DSM-5 le clasifică ca tulburări distincte. "
        "✅ b) posibil comorbide la unii pacienți — suprapunerea este frecventă clinic. "
        "❌ c) identice și nedistincte în toate cazurile — au criterii de diagnostic diferite. "
        "❌ d) mutual exclusive, fără suprapunere — pot coexista la același pacient. "
        "Din DSM-5, tulburarea de panică și agorafobia sunt diagnostice separate, putând fi comorbide. "
        "Agorafobia poate apărea și fără tulburarea de panică (aproximativ 40% din cazuri), "
        "deși istoric au fost considerate o singură entitate diagnostică."
    ),

    # ── 173 ── Etiologia panicii (multi, corect: abc)
    (
        "✅ a) hiperventilație și creșterea dioxidului de carbon — mecanisme fiziologice în ciclul panicii. "
        "✅ b) condiționarea clasică cu indici interni sau situaționali — dobândire prin asociere. "
        "✅ c) sensibilitate la anxietate și interpretare catastrofală — factori cognitivi centrali. "
        "❌ d) absența oricărei componente fiziologice — fals; panica implică o componentă fiziologică centrală. "
        "Modelul cognitiv Clark al panicii descrie un cerc vicios: senzații corporale, interpretare catastrofică "
        "(infarct, moarte), anxietate amplificată, mai multe senzații. "
        "Sensibilitatea la anxietate (frica de senzațiile anxioase în sine) este un factor de vulnerabilitate major."
    ),

    # ── 174 ── Sensibilitatea la anxietate — TF (TF, corect: Adevărat)
    (
        "Adevărat. Sensibilitatea la anxietate se referă la tendința de a interpreta senzațiile fiziologice ale anxietății "
        "(palpitații, amețeală) ca semne de pericol iminent (infarct, moarte, leșin). "
        "Persoanele cu sensibilitate ridicată la anxietate au risc crescut de a dezvolta tulburare de panică, "
        "deoarece senzațiile normale de activare devin declanșatori ai atacurilor."
    ),

    # ── 175 ── Comportamente de siguranță în panică (multi, corect: ab)
    (
        "✅ a) mențin problema prin evitarea infirmării convingerilor — senzațiile nu sunt niciodată testate fără protecție. "
        "✅ b) împiedică învățarea că senzațiile nu sunt periculoase — habituarea nu are loc. "
        "❌ c) elimină automat riscul de atacuri viitoare — dimpotrivă, mențin sensibilizarea. "
        "❌ d) sunt recomandate ca strategie principală pe termen lung — contraindicate; trebuie reduse în terapie. "
        "Comportamentele de siguranță (statul aproape de o ieșire, evitarea efortului fizic, respirarea controlată) "
        "oferă alinare temporară, dar împiedică persoana să testeze că senzațiile nu sunt periculoase. "
        "Prin aceasta, mențin ciclul tulburării de panică."
    ),

    # ── 176 ── Tratamentul tulburării de panică (multi, corect: abc)
    (
        "✅ a) educație despre fiziologia panicii — psihoeducația reduce interpretările catastrofice. "
        "✅ b) restructurare cognitivă și expunere interoceptivă — tehnici specifice TCC pentru panică. "
        "✅ c) prevenirea comportamentelor de siguranță — elimină menținătorii ciclului anxios. "
        "❌ d) evitarea oricărei senzații corporale neplăcute — contrar principiului expunerii interoceptive. "
        "TCC pentru tulburarea de panică include psihoeducație (rolul hiperventilației, ciclul panicii), "
        "restructurarea interpretărilor catastrofale, expunere interoceptivă (inducerea controlată a senzațiilor temute) "
        "și eliminarea comportamentelor de siguranță."
    ),

    # ── 177 ── Expunerea interoceptivă — TF (TF, corect: Adevărat)
    (
        "Adevărat. Expunerea interoceptivă este o tehnică specifică tratamentului tulburării de panică. "
        "Prin exerciții controlate (respirare rapidă, rotire în loc, inhalare de aer cald), sunt induse deliberat "
        "senzațiile corporale temute, cu scopul de a demonstra că acestea nu sunt periculoase "
        "și de a reduce progresiv sensibilizarea față de ele."
    ),

    # ── 178 ── Tulburarea anxioasă generalizată — definiție (multi, corect: ab)
    (
        "✅ a) îngrijorare excesivă, cronică și greu de controlat — nucleul simptomatologic al TAG. "
        "✅ b) preocupare despre mai multe domenii ale vieții — caracter politem al îngrijorării. "
        "❌ c) frică de un singur obiect sau situație specifică — aceasta definește fobia specifică. "
        "❌ d) atacuri de panică neașteptate ca simptom central — caracteristice tulburării de panică. "
        "TAG se caracterizează prin îngrijorare persistentă, cronică, dificil de controlat, care acoperă multiple "
        "domenii (muncă, sănătate, familie, finanțe). "
        "Spre deosebire de fobii sau panică, nu există un declanșator specific bine delimitat."
    ),

    # ── 179 ── Simptome fizice în TAG (multi, corect: ab)
    (
        "✅ a) neliniște și tensiune musculară — simptome somatice centrale în TAG. "
        "✅ b) oboseală, dureri sau greață — manifestări somatice frecvente ale anxietății cronice. "
        "❌ c) grandiozitate și energie crescută — simptome maniacale, specifice tulburării bipolare. "
        "❌ d) halucinații auditive persistente — simptome psihotice, specifice schizofreniei. "
        "Simptomele fizice asociate TAG includ neliniște sau senzația de a fi 'pe muchie de cuțit', tensiune musculară, "
        "oboseală, dificultăți de concentrare, iritabilitate și tulburări de somn. "
        "Cel puțin trei astfel de simptome sunt necesare pentru diagnostic."
    ),

    # ── 180 ── Criterii pentru TAG (multi, corect: abc)
    (
        "✅ a) anxietate și îngrijorare excesivă despre două sau mai multe domenii — îngrijorare politemă. "
        "✅ b) prezența simptomelor mai multe zile decât nu, timp de cel puțin trei luni — caracter cronic. "
        "✅ c) suferință sau afectare funcțională semnificativă — criteriu de impact. "
        "❌ d) durată obligatorie de minimum șase luni, ca la fobii — comparația cu fobiile este inexactă; "
        "criteriile temporale diferă între clasificările ICD-11 și DSM-5 și nu sunt identice cu cele ale fobiilor. "
        "Criteriile pentru TAG includ îngrijorare politemă excesivă și cronică, simptome fizice asociate, "
        "suferință sau afectare funcțională semnificativă și excluderea altor cauze. "
        "Durata criteriu variază ușor între clasificări, dar caracterul cronic este comun."
    ),

    # ── 181 ── Bărbat cu îngrijorare zilnică politemă (multi, corect: a)
    (
        "✅ a) tulburare anxioasă generalizată — îngrijorare cronică, politemă, incontrolabilă, persistentă. "
        "❌ b) fobie specifică de tip situațional — nu există un stimul fobic unic identificat. "
        "❌ c) tulburare de panică, ca diagnostic principal — nu sunt descrise atacuri discrete recurente. "
        "❌ d) tulburare obsesiv-compulsivă cu compulsii — nu sunt descrise obsesii sau ritualuri. "
        "Tabloul clinic descrie îngrijorare cronică, politemă (muncă, sănătate, familie) și dificil de controlat, "
        "persistentă de mai mult de trei luni. "
        "Aceasta este caracteristică TAG; fobia specifică vizează un singur stimul, iar tulburarea de panică implică "
        "atacuri discrete, nu îngrijorare difuză."
    ),

    # ── 182 ── Factori etiologici în TAG (multi, corect: abc)
    (
        "✅ a) componentă genetică moderată și reglare emoțională dificilă — heritabilitate estimată la 30-40%. "
        "✅ b) bias în procesarea informațiilor amenințătoare — hipervigilență față de stimuli ambigui. "
        "✅ c) catastrofizarea și credințe metacognitive despre îngrijorare — factori cognitivi centrali în TAG. "
        "❌ d) absența oricărei îngrijorări cognitive — absurdă ca opțiune; îngrijorarea cognitivă definește TAG. "
        "TAG are o componentă genetică moderată, sensibilitate la amenințări și tendință spre catastrofizare. "
        "Modelul metacognitiv (Wells) subliniază rolul credințelor despre îngrijorare în menținerea tulburării."
    ),

    # ── 183 ── Credințe metacognitive în TAG (multi, corect: ab)
    (
        "✅ a) ideea că îngrijorarea previne pericolul — credință metacognitivă pozitivă ('îngrijorarea mă ajută'). "
        "✅ b) convingerea că îngrijorarea este periculoasă și incontrolabilă — credință metacognitivă negativă. "
        "❌ c) certitudinea că îngrijorarea este mereu inutilă — persoanele cu TAG au credințe pozitive despre utilitatea ei. "
        "❌ d) absența oricărei evaluări a utilității îngrijorării — evaluarea metacognitivă este centrală în TAG. "
        "Modelul metacognitiv al lui Adrian Wells distinge credințe pozitive ('îngrijorarea mă ajută să fiu pregătit') "
        "și negative ('îngrijorarea mă va înnebuni; nu pot controla îngrijorarea') despre îngrijorare. "
        "Ambele tipuri contribuie la menținerea TAG."
    ),

    # ── 184 ── Caracteristici dispoziționale în TAG (multi, corect: abc)
    (
        "✅ a) intoleranță la incertitudine — construct central în TAG; orice ambiguitate este percepută ca amenințare. "
        "✅ b) perfecționism și responsabilitate exagerată — amplifică nevoia de certitudine. "
        "✅ c) încredere scăzută în propria capacitate de coping — 'nu voi face față dacă se întâmplă'. "
        "❌ d) indiferență totală față de consecințe — contrar profilului TAG; preocuparea pentru consecințe este excesivă. "
        "Intoleranța la incertitudine este considerată un construct central în TAG: tendința de a percepe orice situație "
        "ambiguă ca amenințătoare și de a reacționa cu îngrijorare. "
        "Perfecționismul și neîncrederea în sine perpetuează îngrijorarea."
    ),

    # ── 185 ── Tratamentul psihologic al TAG (multi, corect: abc)
    (
        "✅ a) controlul stimulilor de îngrijorare — amânarea îngrijorării la un interval stabilit. "
        "✅ b) restructurare cognitivă și relaxare — infirmarea catastrofizării și reducerea activării. "
        "✅ c) repetare comportamentală și antrenarea copingului — consolidarea toleranței la incertitudine. "
        "❌ d) generalizarea îngrijorării în toată ziua — contrar obiectivului terapeutic; scopul este limitarea. "
        "TCC pentru TAG combină controlul stimulilor (îngrijorarea limitată la un interval specific), "
        "restructurarea cognitivă (testarea convingerilor catastrofale), tehnici de relaxare și antrenarea "
        "toleranței la incertitudine."
    ),

    # ── 186 ── Controlul stimulilor de îngrijorare — TF (TF, corect: Adevărat)
    (
        "Adevărat. Controlul stimulilor de îngrijorare (worry postponement) este o tehnică utilizată în tratamentul TAG: "
        "persoana amână îngrijorarea până la un moment și un loc stabilit (de exemplu, 20 de minute seara), "
        "reducând îngrijorarea intruzivă din restul zilei. "
        "Aceasta ajută la câștigarea unui sentiment de control și la limitarea impactului îngrijorării asupra funcționării."
    ),

    # ── 187 ── Comorbiditate ridicată în TAG — TF (TF, corect: Adevărat)
    (
        "Adevărat. TAG are una dintre cele mai ridicate rate de comorbiditate din tulburările anxioase. "
        "Depresia majoră apare la aproximativ 60-70% dintre pacienți, iar alte tulburări anxioase (fobie socială, "
        "tulburare de panică) coexistă frecvent. "
        "Această comorbiditate complicădiagnosticul și necesită un plan de tratament integrat."
    ),

    # ── 188 ── Tratamentul farmacologic al TAG (multi, corect: abc)
    (
        "✅ a) inhibitori selectivi ai recaptării serotoninei (ISRS) — tratament farmacologic de primă linie. "
        "✅ b) inhibitori ai recaptării serotoninei și noradrenalinei (IRSN) — de asemenea de primă linie. "
        "✅ c) anxiolitice, cu eficiență variabilă pe termen lung — eficiente pe termen scurt, risc de dependență. "
        "❌ d) antipsihotice ca tratament de primă linie obligatoriu — nu sunt indicație primară pentru TAG. "
        "Ghidurile clinice recomandă ISRS și IRSN ca tratament farmacologic de primă linie pentru TAG. "
        "Benzodiazepinele pot fi eficiente pe termen scurt, dar prezintă riscuri de dependență și toleranță. "
        "Antipsihoticele nu sunt tratament de primă linie, dar pot fi utilizate ca augmentare în cazuri refractare."
    ),

    # ── 189 ── Îngrijorare incontrolabilă și catastrofizare — TF (TF, corect: Adevărat)
    (
        "Adevărat. În TAG, îngrijorarea este percepută de persoană ca imposibil de oprit și tinde spre gândire "
        "catastrofală repetată: scenariul cel mai rău este constant anticipat. "
        "Această caracteristică diferențiază TAG de îngrijorarea normală, care este proporțională, controlabilă "
        "și se oprește după ce problema este rezolvată sau evaluată rațional."
    ),
]

assert len(PART2_EXPLANATIONS) == 110
