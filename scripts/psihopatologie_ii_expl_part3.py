"""Explicații didactice — Psihopatologie II: tulburările de personalitate.

Acoperă itemii 190–289 (exam 8191–8290):
  • 190–239 → PERSONALITATE_ITEMS (50 itemi)
  • 240–289 → PERSONALITATE_EXTRA_ITEMS (50 itemi)
"""

from __future__ import annotations

PART3_EXPLANATIONS: list[str] = [
    # ── PERSONALITATE_ITEMS ── index 190
    # Item 190: tulburările de personalitate se caracterizează prin (abc)
    (
        "Tulburările de personalitate sunt definite prin trei caracteristici esențiale care "
        "trebuie să coexiste: (a) tipare persistente, inflexibile și dezadaptative de "
        "experiență interioară și comportament; (b) debut din adolescență sau începutul vieții "
        "adulte; (c) afectarea semnificativă a funcționării personale sau interpersonale. "
        "Opțiunea 'd' (episoade scurte, complet remisive) este falsă — tocmai stabilitatea "
        "și rezistența la schimbare diferențiază tulburările de personalitate de tulburările "
        "de axă I cu remisie completă."
    ),
    # Item 191: modelul patologic trebuie manifestat rigid în cel puțin două domenii (abc)
    (
        "Criteriile generale DSM precizează că modelul patologic trebuie să se manifeste "
        "rigid în cel puțin două dintre domeniile: cogniție, afectivitate, funcționare "
        "interpersonală și controlul impulsurilor. Opțiunile (a), (b) și (c) corespund "
        "primelor trei domenii. Opțiunea 'd' — inteligența generală măsurată — nu este "
        "un domeniu diagnostic pentru tulburările de personalitate."
    ),
    # Item 192: afectarea funcționării personalității (abc)
    (
        "Afectarea funcționării personalității vizează domenii interpersonale și de sine: "
        "(a) reglarea emoțională și empatia, (b) intimitatea și relațiile interpersonale, "
        "(c) imaginea de sine coerentă. Memoria pe termen scurt nu este un criteriu central "
        "al tulburărilor de personalitate — dificultățile mnezice specifice aparțin altor "
        "categorii diagnostice (ex. tulburări neurocognitive)."
    ),
    # Item 193: clusterele A, B, C (abc)
    (
        "Clasificarea DSM grupează tulburările de personalitate în trei clustere: "
        "A (ciudat/excentric: paranoidă, schizoidă, schizotipală), "
        "B (dramatic/emoțional: antisocială, borderline, narcisistă, histrionică), "
        "C (anxios/temător: evitantă, dependentă, obsesiv-compulsivă). "
        "Nu există un cluster D psihotic/acut — psihoza activă reprezintă un criteriu de "
        "excludere pentru multe tulburări de personalitate, nu un cluster separat."
    ),
    # Item 194: TF — model durabil, stabil, inflexibil (True)
    (
        "Afirmația este adevărată. Definiția operațională a tulburării de personalitate "
        "cuprinde: model durabil (persistent în timp), abatere de la așteptările culturale, "
        "stabilitate și inflexibilitate, precum și producerea de suferință sau afectare "
        "funcțională. Toate aceste componente sunt obligatorii pentru diagnostic."
    ),
    # Item 195: TF — apar brusc la vârsta mijlocie (False)
    (
        "Afirmația este falsă. Tulburările de personalitate nu apar brusc la vârsta mijlocie; "
        "ele au, prin definiție, debut recunoscut în adolescență sau la începutul vieții "
        "adulte și prezintă un tipar stabil, care poate fi identificat retrospectiv. "
        "Apariția bruscă a unor schimbări de personalitate la vârsta mijlocie ridică suspiciunea "
        "unei cauze organice (tumoră, traumatism cranian, boală neurologică)."
    ),
    # Item 196: fațeta antagonism (ab)
    (
        "Fațeta antagonism din modelul dimensional al trăsăturilor patologice include "
        "manipulativitate, înșelăciune, grandiozitate și insensibilitate față de ceilalți. "
        "Retragerea socială și anhedonia caracterizează fațeta detașare, iar perfecționismul "
        "rigid și ordinea excesivă sunt specifice fațetei constrângere/compulsivitate."
    ),
    # Item 197: fațeta detașare (ab)
    (
        "Fațeta detașare cuprinde retragerea socială, evitarea intimității, anhedonia "
        "și afectivitatea restrânsă — toate reflectând un deficit de implicare emoțională "
        "și socială. Căutarea atenției și dramatizarea aparțin fațetei antagonism/histrionic, "
        "iar impulsivitatea și asumarea riscurilor sunt parte din fațeta dezinhibiție."
    ),
    # Item 198: fațetele dezinhibiție și psihotism (ab)
    (
        "Dezinhibiția include impulsivitate și iresponsabilitate — dificultăți de reglare "
        "comportamentală. Psihotismul include excentricitate, credințe neobișnuite și "
        "experiențe perceptive atipice. Supunerea excesivă și teama de abandon aparțin "
        "fațetei afectivitate negativă/nesiguranță, iar suspiciozitatea și ranchiuna "
        "aparțin fațetei afectivitate negativă cu nuanță paranoidă."
    ),
    # Item 199: TF — afectivitatea negativă (True)
    (
        "Afirmația este adevărată. Afectivitatea negativă este un domeniu larg al "
        "trăsăturilor patologice care cuprinde fațete multiple: anxietate, labilitate "
        "emoțională, depresivitate, suspiciozitate și nesiguranță față de separare. "
        "Aceste fațete sunt prezente, în grade diferite, la mai multe tulburări de "
        "personalitate (ex. borderline, evitantă, dependentă)."
    ),
    # Item 200: clusterul A include (abc)
    (
        "Clusterul A cuprinde tulburările de personalitate paranoidă, schizoidă și "
        "schizotipală — grupate sub eticheta 'ciudat/excentric' datorită similarității "
        "cu simptomele din spectrul schizofrenic, dar fără psihoză activă susținută. "
        "Tulburarea antisocială face parte din clusterul B (dramatic/emoțional)."
    ),
    # Item 201: tulburările din clusterul A se deosebesc de schizofrenie (ab)
    (
        "Tulburările din clusterul A nu implică, de regulă, halucinații senzoriale "
        "persistente și nici pierderea completă a contactului cu realitatea — acestea "
        "sunt elementele care definesc psihoza activă din schizofrenie. "
        "Gândirea ciudată, suspiciozitatea și retragerea socială pot apărea atât în "
        "clusterul A, cât și în schizofrenie, deci nu sunt elemente distinctive."
    ),
    # Item 202: TP paranoidă presupune (ab)
    (
        "Trăsăturile centrale ale tulburării de personalitate paranoide sunt neîncrederea "
        "și suspiciunea persistentă față de ceilalți, precum și interpretarea intențiilor "
        "altora ca răuvoitoare sau amenințătoare — fără a atinge nivelul delirant. "
        "Retragerea voluntară din orice contact uman este specifică TP schizoide, iar "
        "emoționalitatea excesivă și căutarea atenției caracterizează TP histrionică."
    ),
    # Item 203: criterii frecvente în TP paranoidă (abc)
    (
        "Criteriile frecvent citate în TP paranoidă includ: suspiciuni nejustificate privind "
        "loialitatea prietenilor sau partenerului, interpretarea amenințătoare a remarcilor "
        "neutre ('citirea în rău' a intenției celorlalți) și ranchiuna persistentă față de "
        "jigniri percepute. Lipsa oricărei suspiciuni față de partener este contrariul "
        "tabloului — TP paranoidă implică frecvent gelozie patologică nejustificată."
    ),
    # Item 204: TP schizoidă se caracterizează prin (ab)
    (
        "TP schizoidă se definește prin detașarea persistentă de relațiile sociale (persoana "
        "nu dorește și nu se bucură de relații apropiate) și printr-o gamă restrânsă de "
        "exprimare emoțională în context interpersonal (afect plat). "
        "Comportamentul seductiv și teatral aparțin TP histrionice, iar grandiozitatea "
        "și nevoia de admirație aparțin TP narcisiste."
    ),
    # Item 205: bărbat cu activități solitare, afect plat (a)
    (
        "Tabloul clinic prezentat — preferință pentru activități solitare, absența dorinței "
        "de relații apropiate, indiferență la laude și critici, afect plat — este caracteristic "
        "tulburării de personalitate schizoide. TP histrionică implică căutarea atenției, "
        "TP antisocială implică încălcarea drepturilor altora, iar TP dependentă implică "
        "nevoia excesivă de sprijin și teamă de separare — toate incompatibile cu tabloul descris."
    ),
    # Item 206: TP schizotipală poate include (abc)
    (
        "TP schizotipală este marcată de simptome cvasi-psihotice: idei de referință (evenimentele "
        "par a fi legate de propria persoană), gândire magică, experiențe perceptive neobișnuite "
        "(ex. a simți prezența cuiva) și discurs vag sau metaforic greu de urmărit. "
        "Halucinațiile persistente cu pierderea insightului indică psihoză activă (ex. schizofrenie), "
        "nu TP schizotipală."
    ),
    # Item 207: TF — TP schizotipală și anxietate socială + credințe paranormale (True)
    (
        "Afirmația este adevărată. TP schizotipală include anxietate socială care nu scade "
        "odată cu familiarizarea (spre deosebire de fobia socială), deoarece este alimentată "
        "de suspiciozitate și idei paranoide. De asemenea, credințele în fenomene paranormale, "
        "superstiții sau puterea gândirii sunt manifestări tipice ale gândirii magice din "
        "această tulburare."
    ),
    # Item 208: clusterul B include (abc)
    (
        "Clusterul B (dramatic/emoțional) cuprinde tulburările de personalitate antisocială, "
        "borderline și narcisistă — toate menționate în opțiunile (a), (b) și (c). "
        "TP histrionică face de asemenea parte din clusterul B, dar nu este printre opțiunile "
        "corecte oferite. TP evitantă aparține clusterului C (anxios/temător)."
    ),
    # Item 209: trăsătura centrală a TP antisociale (ab)
    (
        "Trăsăturile centrale ale TP antisociale sunt disprețul față de drepturile celorlalți "
        "și încălcarea normelor sociale, care trebuie să fi debutat anterior vârstei de 15 ani "
        "(criterii de conduită din adolescență). Teama de abandon și instabilitatea afectivă "
        "sunt caracteristice TP borderline, iar retragerea socială și lipsa dorinței de "
        "intimitate caracterizează TP schizoidă."
    ),
    # Item 210: pentru TP antisocială este necesar (ab)
    (
        "DSM impune două condiții diagnostice obligatorii pentru TP antisocială: vârsta "
        "minimă de 18 ani la momentul evaluării și dovezi ale unui pattern de conduită "
        "problematică din adolescență (ex. tulburarea de conduită). "
        "Prezența unei psihoze nu este necesară și, de fapt, excluderea unei cauze psihotice "
        "este importantă. Impulsivitatea este frecventă, dar nu 'absentă' obligatoriu."
    ),
    # Item 211: criterii frecvente în TP antisocială (abc)
    (
        "TP antisocială cuprinde o constelație de comportamente: minciună repetată și "
        "înșelăciune în scop personal, impulsivitate, iritabilitate și agresivitate recurentă, "
        "iresponsabilitate cronică și, în mod definitoriu, lipsa remușcării față de "
        "consecințele acțiunilor dăunătoare. Nevoia excesivă de a fi îngrijit și supunerea "
        "sunt caracteristice TP dependente — diametral opuse."
    ),
    # Item 212: TP borderline presupune (ab)
    (
        "Nucleul TP borderline este instabilitatea — a relațiilor interpersonale, a imaginii "
        "de sine și a afectului — combinată cu impulsivitate ridicată. "
        "Grandiozitatea stabilă și lipsa de empatie ca trăsătură centrală definesc TP narcisistă, "
        "nu borderline. Preferința constantă pentru solitudine este specifică TP schizoide."
    ),
    # Item 213: criterii frecvente în TP borderline (abc)
    (
        "Criteriile frecvente în TP borderline includ: eforturi disperate de evitare a "
        "abandonului real sau imaginar, comportament suicidar recurent sau autovătămare, "
        "instabilitate afectivă (dispoziție reactivă) și senzația cronică de gol interior. "
        "Lipsa oricărei frici de respingere este contrariul tabloului borderline — "
        "teama de abandon este un criteriu cardinal."
    ),
    # Item 214: pacientă cu relații alternative și autovătămare (a)
    (
        "Tabloul clinic descris — alternarea idealizare/devalorizare în relații, frică de "
        "abandon, autovătămare și schimbări rapide de dispoziție — este clasic pentru TP "
        "borderline. TP schizoidă nu implică relații intense. TP paranoidă nu se asociază "
        "cu autovătămare ca trăsătură centrală. TP obsesiv-compulsivă implică rigiditate "
        "și control, nu instabilitate afectivă."
    ),
    # Item 215: comorbidități frecvente ale TP borderline (abc)
    (
        "TP borderline are rate ridicate de comorbiditate cu: tulburările depresive (episoade "
        "majore, distimie), tulburările anxioase (inclusiv PTSD, dat fiind că trauma este "
        "frecventă în antecedente) și tulburările de uz de substanțe (consum impulsiv). "
        "TOC poate coexista ocazional, dar nu este 'o regulă obligatorie' — afirmarea "
        "obligativității este incorectă."
    ),
    # Item 216: TP narcisistă presupune (ab)
    (
        "TP narcisistă este definită de grandiozitate (sentiment exagerat de importanță), "
        "nevoia de admirație constantă și lipsa de empatie față de ceilalți, asociate cu "
        "exploatarea relațiilor interpersonale. Retragerea socială și afectul plat aparțin "
        "TP schizoide, iar teama de critică și evitarea interpersonală sunt caracteristice "
        "TP evitante."
    ),
    # Item 217: TF — stima de sine fragilă în TP narcisistă (True)
    (
        "Afirmația este adevărată. În ciuda aparenței de grandoare, stima de sine în TP "
        "narcisistă este adesea fragilă și dependentă de validarea externă. "
        "Lipsa admirației sau critica poate declanșa furie narcisistă sau agresivitate "
        "reactivă — fenomen cunoscut ca 'rușine narcisistă' transformată în furie. "
        "Această fragilitate internă stă la baza comportamentelor exploatative."
    ),
    # Item 218: TP histrionică se caracterizează prin (abc)
    (
        "TP histrionică se caracterizează prin: emoționalitate excesivă și nevoia permanentă "
        "de a fi în centrul atenției, disconfort marcat atunci când nu primește atenție și "
        "comportament seductiv sau teatral inadecvat contextului. "
        "Indiferența față de laude sau critici este specifică TP schizoide — opusul tabloului "
        "histrionic, care este extrem de sensibil la reacțiile celorlalți."
    ),
    # Item 219: criterii frecvente în TP histrionică (abc)
    (
        "Criteriile TP histrionice includ: emoții superficiale și rapid schimbătoare (labilitate "
        "afectivă superficială), dramatizare și teatralitate în exprimare, sugestibilitate "
        "(influențabilă de ceilalți sau de circumstanțe) și tendința de a percepe relațiile ca "
        "mai intime decât sunt în realitate. Lipsa oricărei nevoi de validare este contrariul "
        "acestui tablou."
    ),
    # Item 220: clusterul C include (abc)
    (
        "Clusterul C (anxios/temător) cuprinde tulburările de personalitate evitantă, "
        "dependentă și obsesiv-compulsivă. TP schizotipală face parte din clusterul A "
        "(ciudat/excentric). Toate cele trei tulburări din clusterul C au anxietatea și "
        "teama drept trăsătură comună, deși manifestările diferă semnificativ."
    ),
    # Item 221: elemente comune clusterului C (ab)
    (
        "Trăsăturile comune clusterului C sunt anxietatea și teama (ex. de critică, abandon "
        "sau pierderea controlului) și comportamentele de evitare sau de menținere a sprijinului "
        "și controlului. Impulsivitatea dramatică și grandiozitatea definesc clusterul B, "
        "iar gândirea magică și excentricitatea sunt caracteristice clusterului A."
    ),
    # Item 222: TP evitantă presupune (ab)
    (
        "TP evitantă combină reticența socială marcată cu sentimentele de inadecvare și "
        "inferioritate, precum și hipersensibilitatea la critică sau respingere. "
        "Spre deosebire de TP schizoidă, persoana evitantă dorește relații, dar le evită "
        "din teama de a fi respinsă sau judecată negativ. "
        "Disprețul față de drepturile celorlalți este caracteristic TP antisociale."
    ),
    # Item 223: criterii frecvente în TP evitantă (abc)
    (
        "Criteriile TP evitante includ: evitarea activităților profesionale sau sociale cu "
        "contact interpersonal semnificativ, frica intensă de dezaprobare și sentimentul de "
        "inferioritate, precum și inhibiția în situații noi din teama de a fi pus în situații "
        "jenante. Nevoia de a fi în centrul atenției este caracteristică TP histrionice — "
        "opusul comportamentului evitant."
    ),
    # Item 224: persoană care evită din teamă de respingere (a)
    (
        "Tabloul descris — dorința de relații dar evitarea lor din teama de respingere, "
        "sentimentul de inferioritate și refuzul de a-și asuma proiecte noi din teama de "
        "eșec și judecată — este tipic pentru TP evitantă. "
        "TP schizoidă nu implică dorința de relații. TP antisocială și narcisistă nu implică "
        "teamă de respingere ca element central."
    ),
    # Item 225: TP dependentă presupune (ab)
    (
        "TP dependentă se definește prin nevoia excesivă de a fi îngrijit de alții, care "
        "determină comportament supus, dificultate de separare și teamă de abandon. "
        "Grandiozitatea și exploatarea celorlalți definesc TP narcisistă, iar preferința "
        "pentru solitudine definește TP schizoidă — ambele incompatibile cu tabloul "
        "de dependență marcată descris."
    ),
    # Item 226: criterii frecvente în TP dependentă (abc)
    (
        "Criteriile TP dependente cuprind: dificultăți în luarea deciziilor fără reasigurări "
        "repetate din partea altora, disconfort semnificativ când rămâne singură (teama de a "
        "nu fi capabilă să se descurce) și căutarea rapidă a unei noi relații de sprijin "
        "imediat după încheierea uneia. Lipsa oricărei frici de abandon este exact opusul "
        "acestui tablou clinic."
    ),
    # Item 227: TF — TP dependentă și frica de incompetență (True)
    (
        "Afirmația este adevărată. TP dependentă se asociază cu convingerea că persoana "
        "este incapabilă să funcționeze independent — frică de incompetență — ceea ce "
        "alimentează dependența de ghidaj și dificultățile de autonomie. "
        "Această schemă cognitivă (eu sunt neajutorat, ceilalți mă pot proteja) menține "
        "tiparul comportamental supus și agățat."
    ),
    # Item 228: TP obsesiv-compulsivă se caracterizează prin (ab)
    (
        "TP obsesiv-compulsivă (OCPD) este definită de preocuparea excesivă pentru ordine, "
        "perfecțiune și control — atât al mediului, cât și al celorlalți — și de "
        "perfecționism rigid care adesea împiedică finalizarea sarcinilor. "
        "Ritualurile de spălare și obsesiile intruzive sunt caracteristice TOC (tulburarea "
        "obsesiv-compulsivă), o categorie distinctă de OCPD."
    ),
    # Item 229: OCPD diferă de TOC (ab)
    (
        "Distincția esențială: OCPD (tulburarea de personalitate obsesiv-compulsivă) implică "
        "un tipar ego-sintonic de rigiditate, perfecționism și control ca trăsătură de "
        "personalitate stabilă. TOC implică obsesii ego-distonice și compulsii clinice "
        "specifice (ritualuri pentru reducerea anxietății). OCPD nu presupune obligatoriu "
        "halucinații sau absența preocupărilor pentru ordine — ci tocmai accentul pe ordine "
        "ca trăsătură de personalitate rigidă."
    ),
    # Item 230: TF — TP evitantă și tulburarea anxioasă socială pot fi comorbide (True)
    (
        "Afirmația este adevărată. TP evitantă și tulburarea anxioasă socială (fobia socială "
        "generalizată) sunt frecvent comorbide și au un profil simptomatologic similar — "
        "teama de evaluare negativă, evitare socială, sentimente de inadecvare. "
        "Diferența principală: TP evitantă este pervasivă și egosinctonă, pe când fobia "
        "socială poate fi mai circumscrisă situațional."
    ),
    # Item 231: TF — clusterul C include histrionică și antisocială (False)
    (
        "Afirmația este falsă. Clusterul C (anxios/temător) cuprinde TP evitantă, dependentă "
        "și obsesiv-compulsivă. TP histrionică și TP antisocială aparțin clusterului B "
        "(dramatic/emoțional). Confuzia clusterelor este o capcană frecventă de examen — "
        "reținerea caracteristicii generale a fiecărui cluster ajută la memorare."
    ),
    # Item 232: pereche care distinge corect tulburări din același cluster (abc)
    (
        "Perechile corecte sunt: (a) paranoidă — suspiciune vs. schizoidă — detașare și "
        "afect plat (ambele în clusterul A); (b) borderline — instabilitate afectivă vs. "
        "narcisistă — grandiozitate (ambele în clusterul B); (c) evitantă — teamă de critică "
        "vs. dependentă — nevoie de îngrijire (ambele în clusterul C). "
        "Opțiunea 'd' este falsă — antisocială nu se caracterizează prin teamă de abandon, "
        "iar histrionica nu se caracterizează prin retragere socială."
    ),
    # Item 233: pacient care interpretează remarci neutre ca atacuri (a)
    (
        "Tabloul descris — interpretarea remarcilor neutre ca atacuri personale, ranchiună "
        "persistentă, hipervigilență față de intențiile altora, fără halucinații sau deliruri "
        "structurate — este caracteristic TP paranoide. "
        "TP schizotipală ar include gândire magică și excentricitate. TP borderline ar include "
        "instabilitate afectivă și autovătămare. Schizofrenia ar implica psihoză activă."
    ),
    # Item 234: persoană care încalcă repetat legea (a)
    (
        "Tabloul clinic — încălcarea repetată a legii, minciuni pentru profit personal, "
        "impulsivitate și absența remușcării, la o persoană de 25 de ani — satisface "
        "criteriile TP antisociale (vârstă ≥ 18 ani, pattern de conduită). "
        "TP narcisistă poate implica exploatare, dar fără infracționalitate sistematică. "
        "TP dependentă și evitantă sunt incompatibile cu tabloul descris."
    ),
    # Item 235: care afirmații descriu TP schizotipală, nu schizoidă (ab)
    (
        "Distinctivele TP schizotipale față de TP schizoidă sunt: gândirea magică, "
        "comportamentul excentric și experiențele perceptive neobișnuite. "
        "Preferința pentru solitudine fără excentricitate și lipsa ideilor de referință "
        "sau a suspiciunii descriu mai degrabă TP schizoidă. "
        "Ambele implică retragere socială, dar TP schizotipală adaugă dimensiunea cvasi-psihotic."
    ),
    # Item 236: TP borderline vs narcisistă — borderline se distinge prin (ab)
    (
        "Ambele tulburări pot implica relații conflictuale, dar TP borderline se distinge "
        "prin instabilitate afectivă marcată (dispoziție rapid schimbătoare în răspuns la "
        "factorii interpersonali) și frica intensă de abandon, alături de autovătămare sau "
        "comportament suicidar. Grandiozitatea stabilă ca trăsătură centrală și lipsa "
        "impulsivității definesc mai degrabă TP narcisistă."
    ),
    # Item 237: TP histrionică vs tulburarea anxioasă socială — histrionica se distinge prin (ab)
    (
        "Deși ambele pot implica un anumit disconfort social, TP histrionică se distinge "
        "prin căutarea activă a atenției, comportament teatral și emoții superficiale, "
        "schimbătoare, dramatizate. Tulburarea anxioasă socială implică evitarea contactului "
        "interpersonal din teama de critică — exact opusul comportamentului histrionic de "
        "căutare a atenției."
    ),
    # Item 238: în evaluarea TP, important să se distingă tiparul de (abc)
    (
        "La evaluarea tulburărilor de personalitate este esențial să se diferențieze tiparul "
        "persistent de: (a) simptomele episodice ale tulburărilor de dispoziție (ex. "
        "schimbări de personalitate în episoadele depresive); (b) efectele substanțelor sau "
        "ale afecțiunilor medicale (care pot mima orice tulburare de personalitate); "
        "(c) trăsăturile culturale normative (nu orice abatere culturală e patologie). "
        "Orice trăsătură de personalitate din spectrul normal nu este prin sine patologică — "
        "criteriul de afectare funcțională este obligatoriu."
    ),
    # Item 239: TF — toate TP din clusterul B necesită vârsta de 18 ani (False)
    (
        "Afirmația este falsă. Doar TP antisocială impune explicit criteriul vârstei de "
        "cel puțin 18 ani. Celelalte tulburări din clusterul B (borderline, narcisistă, "
        "histrionică) pot fi diagnosticate și la adolescenți dacă tiparul este stabil, "
        "pervasiv și produce afectare. Condiția de 18 ani este specifică TP antisociale "
        "pentru a exclude tulburarea de conduită ca diagnostic unic."
    ),

    # ── PERSONALITATE_EXTRA_ITEMS ── index 240
    # Item 240: TF — în TP paranoidă, reticentă să se confie (True)
    (
        "Afirmația este adevărată. Una dintre manifestările frecvente ale TP paranoide "
        "este reticența de a se confida altora din teama că informațiile divulgate vor "
        "fi folosite împotriva persoanei în viitor. Aceasta reflectă neîncrederea "
        "generalizată și anticiparea răuvoitoare a intențiilor celorlalți, care este "
        "nucleul tulburării."
    ),
    # Item 241: manifestări frecvente în TP paranoidă (abc)
    (
        "Manifestările TP paranoide includ: suspiciuni nejustificate privind fidelitatea "
        "partenerului sau loialitatea prietenilor, nevoie crescută de control și "
        "hipervigilență față de semne de înșelăciune sau amenințare, și interpretarea "
        "criticilor ca atacuri personale direcționate. Căutarea atenției prin comportament "
        "teatral este caracteristică TP histrionice — incompatibilă cu retragerea suspicioasă "
        "din TP paranoidă."
    ),
    # Item 242: criterii asociate TP schizoide (abc)
    (
        "Criteriile TP schizoide includ: interes redus sau absent pentru activitățile sexuale "
        "cu altă persoană, puțini sau niciun prieten apropiat (în afara rudelor de gradul I) "
        "și indiferența față de laude sau critici — absența rezonanței afective la feedbackul "
        "social. Dramatizarea evenimentelor cotidiene este caracteristică TP histrionice, "
        "opusul afectului plat schizoidal."
    ),
    # Item 243: TP schizoidă vs schizotipală — schizotipala se distinge prin (ab)
    (
        "Ambele tulburări implică preferința pentru activități solitare și retragere socială, "
        "dar TP schizotipală adaugă comportament excentric (vestimentație, maniere), gândire "
        "magică și experiențe perceptive neobișnuite. "
        "TP schizoidă nu implică anxietate socială marcată, gândire magică sau idei de "
        "referință — acestea sunt elementele distinctive ale schizotipalei."
    ),
    # Item 244: în TP schizotipală pot apărea (abc)
    (
        "TP schizotipală poate include: afect nepotrivit sau constrâns (răspunsuri emoționale "
        "inadecvate contextului), discurs vag, metaforic sau greu de urmărit, și lipsa "
        "prietenilor apropiați (cu excepția rudelor). "
        "Grandiozitatea și nevoia de admirație sunt specifice TP narcisiste — un tablou "
        "contrastant cu excentricitatea suspicioasă a TP schizotipale."
    ),
    # Item 245: tânăr cu idei de referință și credințe paranormale (a)
    (
        "Tabloul clinic descris — evitarea prieteniilor, credința că evenimentele din jur "
        "îl vizează personal (idei de referință) și convingeri paranormale, fără psihoză "
        "clară — corespunde TP schizotipale. "
        "TP schizoidă nu implică idei de referință sau credințe paranormale. "
        "TP paranoidă pune accentul pe suspiciune față de intenții, nu pe credințe magice. "
        "TP evitantă implică teamă de respingere, nu idei de referință."
    ),
    # Item 246: TP paranoidă diferă de TP schizotipală — paranoidă pune accentul pe (ab)
    (
        "Deși ambele includ suspiciozitate, TP paranoidă pune accentul specific pe: "
        "suspiciune față de intențiile răuvoitoare ale celorlalți și ranchiună persistentă "
        "față de jigniri percepute. "
        "Gândirea magică și excentricitatea ca trăsături centrale definesc TP schizotipală. "
        "Afirmația că paranoidă implică 'lipsa oricărei suspiciuni' este evident incorectă."
    ),
    # Item 247: TF — TP schizoidă și activități abstracte sau mecanice (True)
    (
        "Afirmația este adevărată. Persoanele cu TP schizoidă preferă adesea activități "
        "care nu implică contact social — activități abstracte (matematică, programe de "
        "calculator, filosofie) sau mecanice (reparații, munci solitare). "
        "Această preferință reflectă absența dorinței de contact interpersonal, nu teama "
        "de acesta (ca în TP evitantă)."
    ),
    # Item 248: TF — clusterul A asemănător spectrului schizofrenic, dar fără psihoză (True)
    (
        "Afirmația este adevărată. Tulburările din clusterul A (paranoidă, schizoidă, "
        "schizotipală) sunt considerate parte a spectrului schizofrenic larg — prezintă "
        "vulnerabilitate genetică și simptome subclinice asemănătoare. "
        "Diferența esențială față de schizofrenie: nu implică halucinații persistente și "
        "nici pierderea completă a contactului cu realitatea."
    ),
    # Item 249: TF — TP schizoidă presupune lipsa dorinței de relații, nu evitarea din teamă (True)
    (
        "Afirmația este adevărată și marchează distincția fundamentală față de TP evitantă: "
        "în TP schizoidă, persoana nu dorește relații apropiate — absența dorinței, nu "
        "teama. "
        "În TP evitantă, persoana dorește relații, dar le evită din teama de respingere "
        "și critică. Această diferență de motivație este crucială diagnostic."
    ),
    # Item 250: manifestări frecvente în TP antisocială (abc)
    (
        "TP antisocială se manifestă prin: conduită imprudentă față de propria siguranță "
        "sau a altora (ex. condus periculos, ignorarea riscurilor), manipulare și lipsă "
        "cronică de responsabilitate profesională, și agresivitate repetată cu posibil "
        "comportament infracțional. "
        "Nevoia de reasigurare înainte de decizii este specifică TP dependente — "
        "diametral opusă impulsivității antisociale."
    ),
    # Item 251: TF — TP antisocială nu se diagnostichează sub 18 ani (True)
    (
        "Afirmația este adevărată. DSM specifică explicit că TP antisocială nu poate fi "
        "diagnosticată la persoane sub 18 ani. Înainte de această vârstă, tabloul clinic "
        "similar (încălcări repetate ale normelor sociale) se diagnostichează ca tulburare "
        "de conduită. Criteriul de vârstă există pentru a nu stigmatiza adolescenții "
        "a căror personalitate este încă în formare."
    ),
    # Item 252: în TP borderline sub stres pot apărea (ab)
    (
        "Sub stres sever sau în contextul relațional, persoanele cu TP borderline pot dezvolta "
        "simptome tranzitorii cvasi-psihotice: idei paranoide tranzitorii (suspiciuni scurte, "
        "non-sistematizate) și simptome disociative severe (depersonalizare, derealizare). "
        "Episoadele de grandiozitate stabilă nu sunt caracteristice TP borderline, iar lipsa "
        "fricii de abandon este opusul tabloului clinic."
    ),
    # Item 253: criterii suplimentare în TP borderline (abc)
    (
        "Criteriile suplimentare ale TP borderline includ: imagine de sine instabilă sau "
        "identitate difuză (schimbări marcate în scopuri, valori, orientare sexuală), furie "
        "intensă și nepotrivită, greu de controlat, și relații interpersonale intense dar "
        "instabile (alternând între idealizare și devalorizare). "
        "Indiferența față de respingere sau abandon este exact opusul criteriului cardinal "
        "al TP borderline."
    ),
    # Item 254: pacientă cu idealizare/devalorizare și senzație de gol interior (a)
    (
        "Tabloul clinic — idealizarea urmată de devalorizarea partenerului (clivaj relațional), "
        "impulsivitate în consum și senzația cronică de gol interior — satisface criteriile "
        "TP borderline. "
        "TP narcisistă nu implică senzație de gol sau clivaj relațional intens. "
        "TP histrionică implică teatralitate, nu clivaj. "
        "TP obsesiv-compulsivă implică rigiditate și control — opusul impulsivității."
    ),
    # Item 255: TP borderline diferă de tulburarea bipolară prin instabilitatea afectivă (ab)
    (
        "Instabilitatea afectivă din TP borderline este reactivă la factori interpersonali "
        "(mai legată de relații și teama de abandon) și mai de scurtă durată (ore, nu zile). "
        "În tulburarea bipolară, episoadele au durată mai lungă și sunt mai puțin legate "
        "de factorii relaționali. "
        "Episoadele maniacale clare nu sunt caracteristice TP borderline."
    ),
    # Item 256: criterii frecvente în TP narcisistă (abc)
    (
        "Criteriile TP narcisiste includ: sentiment exagerat de importanță personală "
        "(grandiozitate), preocupare pentru fantezii de succes nelimitat, putere sau "
        "perfecțiune, și convingerea că este special și unic, care poate fi înțeles doar "
        "de persoane sau instituții speciale. "
        "Teama dominantă de critică și inferioritate definesc TP evitantă — opusul "
        "grandiozității narcisiste."
    ),
    # Item 257: în TP narcisistă pot apărea (abc)
    (
        "TP narcisistă poate include: așteptări nerezonabile de favorizare sau tratament "
        "special, invidie față de alții sau convingerea că alții îl invidiază, și "
        "exploatarea celorlalți pentru atingerea propriilor scopuri. "
        "Comportamentul supus și teama de separare sunt caracteristice TP dependente — "
        "incompatibile cu narcisismul."
    ),
    # Item 258: coleg care se consideră superior și răspunde agresiv la feedback (a)
    (
        "Tabloul descris — sentiment de superioritate, cerere de tratament special, "
        "răspuns agresiv la feedback (furie narcisistă) și lipsă de empatie — este tipic "
        "pentru TP narcisistă. "
        "TP evitantă implică teamă de critică și inferioritate. "
        "TP dependentă implică supunere și nevoie de sprijin. "
        "TP schizoidă implică detașare și afect plat."
    ),
    # Item 259: TP histrionică vs narcisistă — histrionica se distinge prin (ab)
    (
        "Ambele tulburări pot căuta admirație, dar TP histrionică se distinge prin: "
        "emoționalitate teatrală și superficială (emoții exprimate dramatic, dar superficial) "
        "și utilizarea aspectului fizic ca instrument pentru atragerea atenției. "
        "Grandiozitatea stabilă ca nucleu central este caracteristica definitorie a TP "
        "narcisiste, nu a celei histrionice. TP histrionică este mai puțin legată de "
        "un sentiment fix de superioritate."
    ),
    # Item 260: manifestări frecvente în TP histrionică (abc)
    (
        "Manifestările TP histrionice includ: stil de vorbire impresionist, lipsit de "
        "detalii concrete (superficialitate cognitivă), comportament seductiv sau provocator "
        "inadecvat contextului social sau profesional, și utilizarea aspectului fizic pentru "
        "a atrage atenția celorlalți. "
        "Retragerea preferențială și afectul restrâns descriu TP schizoidă."
    ),
    # Item 261: TF — clusterul B caracterizat prin impulsivitate și instabilitate (True)
    (
        "Afirmația este adevărată. Clusterul B (dramatic/emoțional) este caracterizat "
        "general prin: impulsivitate (antisocială, borderline), instabilitate emoțională "
        "(borderline), dificultăți în respectarea drepturilor celorlalți (antisocială, "
        "narcisistă) și dramatism (histrionică, borderline). "
        "Aceste caracteristici comune justifică gruparea în același cluster."
    ),
    # Item 262: criterii suplimentare în TP evitantă (abc)
    (
        "Criteriile suplimentare ale TP evitante includ: nevoia de a fi sigur că va fi "
        "plăcut înainte de a intra în contact interpersonal, reținere în relații intime "
        "din teama de a fi ridiculizat sau respins, și evitarea activităților noi din "
        "teama de a fi pus în situații jenante. "
        "Disconfortul când nu este în centrul atenției este caracteristic TP histrionice."
    ),
    # Item 263: TP evitantă diferă de TP schizoidă — evitanta prin (ab)
    (
        "Distincția fundamentală: persoana cu TP evitantă dorește relații apropiate, dar "
        "le evită din teama de critică și respingere; se simte inadecvată și inferioară. "
        "Persoana cu TP schizoidă nu dorește deloc relații apropiate și este indiferentă "
        "la laude și critici. "
        "Motivul retragerii sociale diferă esențial: teamă (evitantă) versus indiferență (schizoidă)."
    ),
    # Item 264: criterii suplimentare în TP dependentă (abc)
    (
        "Criteriile suplimentare ale TP dependente includ: dificultatea de a exprima "
        "dezacordul din teama de a pierde sprijinul sau aprobarea, dificultatea de a "
        "iniția proiecte sau de a acționa independent (lipsă de inițiativă autonomă), și "
        "eforturi excesive pentru a obține îngrijire și sprijin (ex. acceptarea sarcinilor "
        "dezagreabile). "
        "Interpretarea neutră a intențiilor ca amenințătoare este caracteristică TP paranoide."
    ),
    # Item 265: femeie care rămâne în relație dăunătoare din teamă (a)
    (
        "Tabloul clinic — rămânerea într-o relație dăunătoare din teama de singurătate, "
        "incapacitatea de a lua decizii fără aprobare și acceptarea tratamentului "
        "necorespunzător pentru a menține relația — este clasic pentru TP dependentă. "
        "TP antisocială, paranoidă și schizotipală nu implică această dinamică de "
        "supunere și teamă de separare."
    ),
    # Item 266: TP dependentă diferă de TP borderline — dependenta pune accentul pe (ab)
    (
        "Deși ambele implică teama de abandon, TP dependentă se axează pe nevoia de "
        "îngrijire și sprijin și pe supunere cu dificultăți de autonomie — tiparul este "
        "relativ stabil și lipsit de impulsivitate. "
        "TP borderline se caracterizează suplimentar prin instabilitate afectivă marcată, "
        "autovătămare și relații intense cu clivaj (idealizare/devalorizare)."
    ),
    # Item 267: manifestări frecvente în TP obsesiv-compulsivă (abc)
    (
        "Manifestările OCPD includ: perfecționism care interferează cu finalizarea sarcinilor "
        "(standardele sunt atât de ridicate că sarcina nu poate fi niciodată 'terminată'), "
        "preocupare excesivă pentru reguli, liste, ordine și detalii până la pierderea "
        "scopului activității, și rigiditate morală excesivă (scrupulozitate, etică inflexibilă). "
        "Ritualurile de verificare pentru teama de contaminare aparțin TOC."
    ),
    # Item 268: manager cu reguli stricte și refuz de delegare (a)
    (
        "Tabloul clinic — insistența pe reguli stricte, refuzul delegării (nimeni nu face "
        "suficient de bine), rigiditate morală și prioritizarea muncii în detrimentul "
        "relațiilor — este caracteristic OCPD (TP obsesiv-compulsive). "
        "TOC ar implica obsesii și compulsii clinice specifice. "
        "TP antisocială implică încălcarea normelor, nu aplicarea rigidă a acestora. "
        "TP histrionică implică teatralitate și emoționalitate."
    ),
    # Item 269: TF — OCPD și perfecționism rigid fără obsesii și compulsii clinice (True)
    (
        "Afirmația este adevărată. OCPD este caracterizată de perfecționism rigid și "
        "dificultăți de flexibilitate cognitivă și comportamentală — ca trăsătură stabilă "
        "de personalitate. "
        "Spre deosebire de TOC, OCPD nu presupune obligatoriu prezența obsesiilor "
        "ego-distonice sau a compulsiilor clinice structurate menite să reducă anxietatea."
    ),
    # Item 270: TF — TP evitantă și tulburarea anxioasă socială pot coexista (True)
    (
        "Afirmația este adevărată. TP evitantă și tulburarea anxioasă socială (TAS) pot "
        "coexista și prezintă suprapunere simptomatologică semnificativă. "
        "TP evitantă adaugă, în plus față de TAS, sentimente cronice de inadecvare și "
        "inferioritate, care se manifestă dincolo de situațiile sociale specifice. "
        "Comorbiditatea este frecventă în practica clinică."
    ),
    # Item 271: TF — TP dependentă și acceptarea tratamentului necorespunzător (True)
    (
        "Afirmația este adevărată. Persoanele cu TP dependentă pot tolera sau accepta "
        "tratament necorespunzător, abuz sau exploatare în relații pentru a evita "
        "singurătatea și pierderea sursei de sprijin. "
        "Aceasta reflectă prioritizarea menținerii relației față de propriul bine, "
        "alimentată de convingerea că nu se pot descurca singure."
    ),
    # Item 272: clusterul C caracterizat prin (abc)
    (
        "Clusterul C (anxios/temător) este caracterizat prin trei teme principale: "
        "(a) anxietate și teamă ca stare fundamentală, (b) evitare interpersonală sau "
        "comportamentală ca mecanism de coping, și (c) nevoia de control (OCPD) sau "
        "de sprijin extern (dependentă). "
        "Impulsivitatea și căutarea atenției sunt caracteristice clusterului B."
    ),
    # Item 273: TF — în TP dependentă, căutarea rapidă a unei noi relații (True)
    (
        "Afirmația este adevărată. Teama de abandon și convingerea că nu se poate descurca "
        "singură determină persoana cu TP dependentă să caute urgent o nouă relație de "
        "sprijin imediat după încheierea celei anterioare. "
        "Această caracteristică poate duce la relații precipitate și la perpetuarea "
        "tiparului dependent."
    ),
    # Item 274: fațeta afectivitate negativă poate include (abc)
    (
        "Fațeta afectivitate negativă este un domeniu larg care cuprinde: labilitate "
        "emoțională și anxietate (reactivitate emoțională crescută), nesiguranță față de "
        "separare și depresivitate (teama de abandon, dispoziție depresivă), și ostilitate, "
        "perseverare și suspiciozitate (tendința de a rumina jignirile și de a suspecta "
        "ceilalți). "
        "Grandiozitatea și căutarea atenției aparțin fațetei antagonism."
    ),
    # Item 275: fațeta dezinhibiție poate include (ab)
    (
        "Fațeta dezinhibiție reflectă dificultăți de control comportamental: impulsivitate "
        "(acțiuni fără reflecție), distractibilitate, iresponsabilitate (nerespectarea "
        "obligațiilor) și asumarea imprudentă a riscurilor. "
        "Perfecționismul rigid și ordinea excesivă aparțin fațetei constrângere "
        "(opusul dezinhibiției). "
        "Retragerea socială și anhedonia aparțin fațetei detașare."
    ),
    # Item 276: comorbiditatea între tulburările de personalitate (ab)
    (
        "Comorbiditatea între tulburările de personalitate este frecventă în practica clinică, "
        "inclusiv între tulburări din clustere diferite (ex. TP borderline și TP narcisistă, "
        "sau TP evitantă și TP dependentă). "
        "De asemenea, comorbiditatea cu tulburările de dispoziție (depresie) și tulburările "
        "anxioase este foarte comună. Afirmațiile că este absentă sau limitată la un cluster "
        "sunt false."
    ),
    # Item 277: TF — tiparul trebuie să fie durabil, inflexibil și să producă suferință (True)
    (
        "Afirmația este adevărată. Criteriul de durabilitate, inflexibilitate și afectare "
        "funcțională este esențial pentru diagnosticul oricărei tulburări de personalitate. "
        "O reacție tranzitorie la stres sau o schimbare temporară de comportament nu "
        "satisface criteriile — tiparul trebuie să fie stabil pe perioade îndelungate, "
        "indiferent de context."
    ),
    # Item 278: TF — TP nu se diagnostichează dacă explicat de substanțe sau afecțiuni medicale (True)
    (
        "Afirmația este adevărată. Criteriile DSM pentru tulburările de personalitate cer "
        "excluderea efectelor directe ale substanțelor (ex. cocaină, corticosteroizi) sau "
        "ale unei afecțiuni medicale (ex. traumatism cranian, encefalită, hipotiroidism). "
        "Acestea pot produce schimbări de personalitate care mimează tulburările de "
        "personalitate, dar au o cauză organică tratabilă."
    ),
    # Item 279: TF — trăsăturile normale pot deveni patologice când sunt extreme, persistente (True)
    (
        "Afirmația este adevărată. Trăsăturile de personalitate există pe un continuum de "
        "la normal la patologic. O trăsătură devine tulburare de personalitate când este: "
        "extremă (depășind semnificativ media normativă), persistentă (stabilă în timp), "
        "inflexibilă (rigidă, neadaptativă la contexte diverse) și produce afectare "
        "funcțională sau suferință semnificativă."
    ),
    # Item 280: în modelul actual, TP pot fi evaluate și prin (abc)
    (
        "Modelul actual (DSM-5 Secțiunea III și ICD-11) permite evaluarea tulburărilor de "
        "personalitate prin trei perspective complementare: (a) nivelul de funcționare a "
        "personalității (sine și interpersonal), (b) trăsăturile patologice pe fațete "
        "specifice, și (c) tipare pe clustere tradiționale (pentru compatibilitate clinică). "
        "Scorul unic de inteligență emoțională nu este un instrument diagnostic recunoscut "
        "pentru tulburările de personalitate."
    ),
    # Item 281: TF — afectarea funcționării personalității poate include empatie, intimitate, reglare (True)
    (
        "Afirmația este adevărată. Modelul dimensional al funcționării personalității "
        "identifică două domenii majore: funcționarea de sine (identitate, autodeterminare) "
        "și funcționarea interpersonală (empatie, intimitate). "
        "Dificultățile în empatie, intimitate și reglarea emoțională sunt indicatori cheie "
        "ai nivelului de afectare a funcționării personalității."
    ),
    # Item 282: care afirmații descriu TP paranoidă, nu schizotipală (ab)
    (
        "TP paranoidă se distinge prin: ranchiună persistentă față de jigniri percepute "
        "și suspiciune față de loialitatea altora, și interpretarea amenințătoare a "
        "remarcilor neutre (hipervigilență paranoidă). "
        "Gândirea magică și superstițiile ca element central, alături de discursul vag și "
        "excentric, sunt caracteristice TP schizotipale, nu TP paranoide."
    ),
    # Item 283: adolescent de 16 ani cu tulburare de conduită (ab)
    (
        "Diagnosticul de TP antisocială este prematur la 16 ani — criteriul de vârstă "
        "minimă de 18 ani nu este satisfăcut. Tabloul clinic descris (încălcări grave ale "
        "regulilor, minciuni, agresivitate) este diagnosticat ca tulburare de conduită "
        "la adolescenți. "
        "TP antisocială poate fi luată în considerare după 18 ani dacă există dovezi de "
        "tulburare de conduită din adolescență. Impulsivitatea nu exclude diagnosticul."
    ),
    # Item 284: TP borderline vs histrionică — borderline se distinge prin (ab)
    (
        "Ambele tulburări pot căuta atenție, dar TP borderline se distinge prin: frică "
        "intensă de abandon și relații instabile (clivaj idealizare/devalorizare) și "
        "autovătămare sau comportament suicidar. "
        "Emoțiile superficiale și teatrale fără instabilitate profundă și lipsa "
        "impulsivității și furiei intense sunt mai caracteristice TP histrionice."
    ),
    # Item 285: TP schizoidă vs evitantă — evitanta se distinge prin (ab)
    (
        "Ambele tulburări pot implica retragere socială, dar TP evitantă se distinge prin: "
        "dorința de relații, inhibată de teama de critică și respingere, și sentimentele "
        "de inadecvare și inferioritate față de ceilalți. "
        "Indiferența la laude și lipsa dorinței de intimitate descriu TP schizoidă. "
        "Comportamentul seductiv și dramatizarea sunt caracteristice TP histrionice."
    ),
    # Item 286: TOC vs OCPD — TOC presupune (ab)
    (
        "Distincția esențială: TOC (tulburarea obsesiv-compulsivă) presupune prezența "
        "obsesiilor ego-distonice (gânduri intruzive, nedorite) și/sau compulsii clinice "
        "recurente (ritualuri structurate menite să reducă anxietatea), care produc "
        "suferință semnificativă. "
        "OCPD implică doar perfecționism de personalitate și rigiditate fără obsesii "
        "clinice obligatorii — este un tipar de personalitate, nu o tulburare episodică."
    ),
    # Item 287: care tulburări aparțin clusterului B (abc)
    (
        "Clusterul B (dramatic/emoțional) cuprinde: TP antisocială, TP borderline și "
        "TP histrionică — toate menționate în opțiunile (a), (b) și (c). "
        "TP narcisistă face de asemenea parte din clusterul B, dar nu este în opțiunile "
        "corecte. TP evitantă aparține clusterului C (anxios/temător) — este o capcană "
        "frecventă de examen."
    ),
    # Item 288: persoană cu haine stridente și comportament dramatic (a)
    (
        "Tabloul descris — haine stridente pentru a atrage atenția, vorbire dramatică, "
        "exagerarea legăturilor interpersonale (perceperea relațiilor ca mai intime decât "
        "sunt) și tendința de a deveni rapid centrul atenției — este clasic pentru "
        "TP histrionică. "
        "TP evitantă și schizoidă implică retragere, nu căutarea atenției. "
        "TP paranoidă implică suspiciune, nu dramatism social."
    ),
    # Item 289: TF — toate TP necesită manifestare rigidă în cel puțin două domenii (True)
    (
        "Afirmația este adevărată. Criteriile generale DSM pentru toate tulburările de "
        "personalitate cer că modelul patologic să se manifeste rigid și inflexibil în "
        "cel puțin două dintre domeniile: cogniție (modalități de percepere și interpretare), "
        "afectivitate (gamă, intensitate, labilitate), funcționare interpersonală și "
        "controlul impulsurilor. Această pervasivitate distinge tulburările de personalitate "
        "de trăsăturile izolate."
    ),
]

assert len(PART3_EXPLANATIONS) == 100, (
    f"Expected 100 explanations, got {len(PART3_EXPLANATIONS)}"
)
