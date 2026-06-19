"""Itemi — Psihologia dezvoltării II: bătrânețe (401–440, ID 10401–10440)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

BATRANETE_ITEMS: List[Item] = [
    # —— 401–410: caracter general, stereotipuri, reziliență, stadii ——
    {
        "stem": (
            "Bătrânețea este etapă de bilanț al vieții, de adaptare la pierderi, "
            "dar și de consolidare a sensului, a înțelepciunii și a rezilienței — "
            "nu doar declin uniform."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care afirmație despre stereotipurile negative legate de bătrânețe "
            "este adevărată din perspectivă științifică?"
        ),
        "options": [
            "pot reduce stima de sine și integrarea socială a persoanelor în vârstă",
            "descriu obligatoriu starea fiecărui adult peste 65 de ani",
            "sunt lipsite de orice efect asupra comportamentului social",
            "reflectă exclusiv realitatea medicală, fără componentă socială",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care factori susțin reziliența la bătrânețe — capacitatea de a se "
            "adapta la pierderi, boli și stres?"
        ),
        "options": [
            "relații semnificative și sprijin social",
            "activitate intelectuală și implicare în sens",
            "izolarea completă pentru a evita dezamăgirile",
            "umor, spiritualitate sau perspective care dau coerență vieții",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "O persoană de 67 de ani își reorganizează viața după pensionare, "
            "acceptă pierderi și caută noi roluri. Etapa descrisă în clasificarea "
            "pe subperioade este cel mai probabil:"
        ),
        "options": [
            "marea bătrânețe (peste 90 de ani)",
            "a doua bătrânețe (80–90 de ani)",
            "trecerea spre bătrânețe (aproximativ 65–70/75 de ani)",
            "prima bătrânețe (70/75–80 de ani)",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Care patru subperioade ale bătrâneței sunt formulate corect în curs?"
        ),
        "options": [
            "trecere spre bătrânețe: aproximativ 65–70/75 ani",
            "prima bătrânețe: aproximativ 70/75–80 ani",
            "a doua bătrânețe: aproximativ 80–90 ani",
            "marea bătrânețe: peste 90 de ani",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "În prima bătrânețe (aproximativ 70/75–80 ani), dezvoltarea psihică "
            "poate include în special:"
        ),
        "options": [
            "reorganizarea activităților după pensionare",
            "consolidarea competențelor relaționale și a sensului",
            "revenirea la stadiul operațiilor concrete piagetiene",
            "pierderea obligatorie a oricărei autonomie decizionale",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care două distincții între inteligența fluidă și cea cristalizată "
            "sunt corecte la bătrânețe?"
        ),
        "options": [
            "fluida: rezolvare de probleme noi, viteză de procesare; tinde să scadă",
            "cristalizată: cunoștințe, vocabular, experiență; poate rămâne stabilă",
            "fluida crește mereu cu vârsta; cristalizata dispare complet",
            "cristalizată = doar memoria pe termen scurt; fluida = doar cultura generală",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La un test de viteză de procesare și rezolvare de probleme noi, "
            "un adult de 78 de ani obține scor mai mic decât la 40 de ani, "
            "deși cunoștințele generale rămân bogate. Abilitatea testată "
            "este în principal:"
        ),
        "options": [
            "inteligența cristalizată exclusiv",
            "înțelepciunea morală ca singur construct",
            "memoria procedurală pentru rutine vechi",
            "inteligența fluidă",
        ],
        "correct": "d",
    },
    {
        "stem": (
            "Care două afirmații despre inteligența cristalizată la persoanele "
            "în vârstă sunt corecte?"
        ),
        "options": [
            "reflectă acumularea de cunoștințe, vocabular și experiență",
            "poate rămâne relativ stabilă mult timp, spre deosebire de fluidă",
            "scade obligatoriu la fel de rapid ca viteza de procesare",
            "exclude complet orice influență a educației sau culturii",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Un bătrân oferă un sfat echilibrat într-un conflict familial, "
            "ținând cont de perspective diferite și de limitele situației. "
            "Constructul psihologic ilustrat este cel mai probabil:"
        ),
        "options": [
            "reflexul de startle neonatal",
            "înțelepciunea — discernământ, experiență, echilibru emoțional",
            "atașamentul evitant timpuriu",
            "inteligența fluidă măsurată prin viteză pură",
        ],
        "correct": "b",
    },
    # —— 411–420: sănătate mentală, Alzheimer, teorii îmbătrânire ——
    {
        "stem": (
            "Demența și pierderile cognitive severe apar la toți adulții "
            "care depășesc 70 de ani — este o consecință normală și universală "
            "a îmbătrânirii."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei trăsături descriu înțelepciunea psihologică la bătrânețe?"
        ),
        "options": [
            "discernământ în judecarea situațiilor complexe",
            "echilibru emoțional și toleranță la ambiguitate",
            "viteză maximă de reacție la stimuli noi",
            "integrarea experienței de viață în perspective echilibrate",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "La bătrânețe, depresia poate fi subdiagnosticată deoarece simptomele "
            "sunt uneori atribuite greșit:"
        ),
        "options": [
            "exclusiv îmbătrânirii normale sau bolilor somatice",
            "doar lipsei de inteligență fluidă",
            "exclusiv demenței, chiar când nu există",
            "doar pierderii memoriei pe termen scurt la orice adult",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două consecințe pot amplifica anxietatea și izolarea la "
            "persoanele în vârstă?"
        ),
        "options": [
            "pierderi afective repetate (soț, prieteni)",
            "scăderea mobilității sau a autonomiei funcționale",
            "implicarea constantă în rețele sociale dense",
            "accesul facil la activități cu sens și utilitate percepută",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "O persoană uită ocazional unde și-a pus cheile, dar își amintește "
            "evenimente recente și își menține rutina. Cel mai probabil este vorba de:"
        ),
        "options": [
            "boala Alzheimer în stadiu avansat",
            "demență obligatorie la orice vârstă peste 65 de ani",
            "variație normală sau atenție scăzută, nu neapărat demență",
            "pierdere completă a orientării în timp și spațiu",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Care două domenii sunt afectate progresiv în boala Alzheimer?"
        ),
        "options": [
            "memoria și orientarea în timp/spațiu",
            "limbajul și capacitatea de funcționare cotidiană",
            "reflexele neonatale și stadiul senzorio-motor timpuriu",
            "atașamentul la obiectul tranzițional la 12 luni",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Boala Alzheimer se caracterizează prin deteriorare cognitivă "
            "progresivă care:"
        ),
        "options": [
            "afectează treptat memoria, gândirea, limbajul și autonomia zilnică",
            "alterează progresiv orientarea și judecata în activitățile cotidiene",
            "dispare spontan fără intervenție dacă persoana rămâne activă social",
            "limitează-se exclusiv la stări trecătoare de tristețe",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care trei pierderi frecvente la bătrânețe pot afecta sănătatea "
            "mentală?"
        ),
        "options": [
            "pierderi afective (partener, prieteni apropiați)",
            "scăderea autonomiei și a controlului asupra vieții cotidiene",
            "câștigarea obligatorie a unor competențe cognitive noi",
            "limitări de rol (pensionare, boală, dependență de îngrijire)",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care două afirmații descriu corect legătura dintre autonomie și "
            "bătrânețe?"
        ),
        "options": [
            "scăderea autonomiei poate amplifica vulnerabilitatea psihică",
            "menținerea unor alegeri și control perceput susține demnitatea",
            "orice pierdere de autonomie este irelevantă pentru starea emoțională",
            "autonomia totală rămâne identică la 90 de ani ca la 30 de ani",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Teoria programării a îmbătrânirii susține că declinul este:"
        ),
        "options": [
            "un proces biologic intern normal, reglat genetic",
            "produs exclusiv de accidente și infecții, fără componentă internă",
            "inexistent — organismul nu se modifică după maturitate",
            "determinat doar de stereotipurile sociale negative",
        ],
        "correct": "a",
    },
    # —— 421–430: teorii, personalitate, nevoi sociale ——
    {
        "stem": (
            "Teoria uzurii (uzurii organismului) explică îmbătrânirea prin "
            "acumularea deteriorărilor produse de stres, boală și factori de mediu."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Care două teorii ale îmbătrânirii pun accent pe acumularea de "
            "deteriorări în timp?"
        ),
        "options": [
            "teoria uzurii — uzura organismului sub stres și boală",
            "teoria acumulării de deșeurilor metabolice — produși toxici, erori celulare",
            "teoria programării — îmbătrânire ca proces intern normal reglat",
            "teoria atașamentului — tipare timpurii de relaționare",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Teoria acumulării de deșeurilor metabolice explică declinul prin:"
        ),
        "options": [
            "pierderea completă a limbajului în primii doi ani",
            "revenirea la stadiul preoperațional piagetian",
            "acumularea produselor toxice și a erorilor celulare",
            "absența oricărei modificări biologice după 20 de ani",
        ],
        "correct": "c",
    },
    {
        "stem": (
            "Care trei distincții între teoriile îmbătrânirii sunt corecte?"
        ),
        "options": [
            "programare: proces intern normal; uzură: deteriorări acumulate",
            "deșeuri metabolice: toxine și erori celulare; uzură: stres și boală",
            "programare și uzura exclud orice influență a mediului",
            "toate cele trei teorii negă existența modificărilor biologice",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "O persoană în vârstă își acceptă limitările, își integrează "
            "experiențele și menține o imagine de sine coerentă. Tipul de "
            "personalitate descris este:"
        ),
        "options": [
            "personalitate integrată",
            "personalitate pasiv-dependentă",
            "personalitate dezorganizată",
            "personalitate defensivă rigidă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două trăsături descriu personalitatea defensivă la bătrânețe?"
        ),
        "options": [
            "rigiditate și rezistență excesivă la schimbare",
            "protecția imaginii de sine prin evitarea amenințărilor",
            "integrare flexibilă a experiențelor de viață",
            "dependență totală de alții fără inițiativă proprie",
        ],
        "correct": "ac",
    },
    {
        "stem": (
            "Personalitatea pasiv-dependentă la bătrânețe se caracterizează "
            "prin:"
        ),
        "options": [
            "lăsarea inițiativei în totalitate la alții și lipsa autonomiei",
            "discernământ matur și toleranță la ambiguitate",
            "reorganizare activă a sensului vieții după pierderi",
            "variații deliberate ale comportamentului pentru explorare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care trei descrieri se potrivesc personalității dezorganizate "
            "la bătrânețe?"
        ),
        "options": [
            "fragmentare a imaginii de sine",
            "dificultate de integrare după pierderi majore",
            "coerență stabilă și acceptare echilibrată a limitelor",
            "dezorientare și instabilitate psihică marcată",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care două nevoi sociale centrale la bătrânețe sunt evidențiate "
            "în curs?"
        ),
        "options": [
            "încredere și ghidare în situații noi sau dificile",
            "integrare socială și sentiment de utilitate",
            "izolare deliberată ca singură cale de adaptare",
            "excluderea oricărui respect din partea comunității",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Un centru comunitar oferă activități unde bătrânii contribuie cu "
            "experiență și mentorat. Nevoia socială adresată este în principal:"
        ),
        "options": [
            "utilitatea și respectul — a fi valorizat, nu doar îngrijit",
            "revenirea la dependența totală de părinți",
            "eliminarea oricărei autonomii decizionale",
            "atașamentul anxios-rezistent din primii ani",
        ],
        "correct": "a",
    },
    # —— 431–440: sinteză, capcane, aplicare ——
    {
        "stem": (
            "Persoanele în vârstă nu au nevoie de sentiment de utilitate sau "
            "de respect — doar de îngrijire medicală."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care trei nevoi sociale ale persoanelor în vârstă sunt enumerate "
            "în curs?"
        ),
        "options": [
            "încredere, ghidare, integrare socială",
            "îngrijire, autonomie, respect",
            "utilitate percepută în comunitate",
            "evitarea oricărui contact intergenerațional",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care două tensiuni pot apărea în îngrijirea persoanelor în vârstă?"
        ),
        "options": [
            "nevoia de sprijin și nevoia de păstrare a autonomiei",
            "protejarea demnității vs. supraprotecția care reduce inițiativa",
            "utilitatea socială și respectul sunt mereu incompatibile",
            "integrarea socială exclude orice nevoie de intimitate",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "După moartea partenerului, o femeie de 72 de ani își reface treptat "
            "rețeaua de prieteni, participă la un club de lectură și găsește "
            "un rol de voluntariat. Procesul ilustrează cel mai bine:"
        ),
        "options": [
            "negarea patologică obligatorie a pierderii",
            "revenirea la stadiul senzorio-motor piagetian",
            "absența completă a oricărei adaptări posibile la bătrânețe",
            "reziliența — adaptare activă la pierdere prin relații, sens și activitate",
        ],
        "correct": "d",
    },
    {
        "stem": (
            "Care patru stereotipuri negative despre bătrânețe sunt criticate "
            "în literatura de specialitate?"
        ),
        "options": [
            "fragilitate fizică și psihică considerată universală",
            "inutilitate socială — persoana nu ar mai conta",
            "rigiditate psihică și incapacitate de adaptare",
            "dependență obligatorie față de alții",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care trei factori pot proteja sănătatea mentală la bătrânețe?"
        ),
        "options": [
            "relații semnificative și sprijin social",
            "activitate intelectuală sau implicare cu sens",
            "izolarea totală pentru a evita stresul interpersonal",
            "autonomie parțială păstrată și respect din partea celorlalți",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "La 82 de ani, un profesor emerit rezolvă mai lent un puzzle nou, "
            "dar explică clar un subiect complex din domeniul său. Combinația "
            "reflectă cel mai probabil:"
        ),
        "options": [
            "scăderea fluidă și păstrarea relativă a cristalizatei",
            "dispariția completă a oricărei competențe cognitive",
            "creșterea obligatorie a fluidă și a cristalizatei la fel de mult",
            "doar înțelepciune, fără nicio componentă cognitivă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care două distincții între înțelepciune și inteligența fluidă "
            "sunt corecte?"
        ),
        "options": [
            "înțelepciunea integrează experiența și echilibrul emoțional",
            "fluida se referă mai ales la viteză și probleme noi",
            "înțelepciunea este identică cu scorul la un test de viteză",
            "fluida crește obligatoriu după 70 de ani",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care patru idei rezumă corect perspectiva psihologică asupra "
            "bătrâneței din curs?"
        ),
        "options": [
            "etapă de bilanț, adaptare, sens și reziliență posibilă",
            "stereotipurile negative pot dăuna stimei de sine și integrării",
            "inteligența fluidă tinde să scadă; cristalizată poate rămâne bogată",
            "toți bătrânii devin automat dependenți, inutili și demenți",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care trei nevoi sociale — alături de îngrijire — trebuie luate "
            "în calcul pentru o persoană de 85 de ani?"
        ),
        "options": [
            "respect și sentiment că încă contează (utilitate)",
            "păstrarea unor alegeri și a autonomiei acolo unde e posibil",
            "excluderea din orice comunitate pentru a nu deranja",
            "integrare și contact, nu izolare forțată",
        ],
        "correct": "abd",
    },
]

assert len(BATRANETE_ITEMS) == 40
