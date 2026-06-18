"""Itemi dificili — terapia gestaltistă vs consilierea centrată pe persoană; apărare vs rezistențe la contact."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

TRICKY_ITEMS: List[Item] = [
    # —— Terapia gestaltistă vs consilierea centrată pe persoană (1–18) ——
    {
        "stem": (
            "Un client spune: „Spune-mi tu ce e bine pentru mine.” Intervenția care se potrivește "
            "mai degrabă cu consilierea centrată pe persoană decât cu terapia gestaltistă este:"
        ),
        "options": [
            "reflectarea sentimentului de confuzie și clarificarea propriei experiențe",
            "experimentul scaunului gol cu partea dependentă și partea autonomă",
            "confruntarea imediată cu evitarea contactului prin umor",
            "amplificarea gesturilor corporale pentru a intensifica figura emergentă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Terapeutul observă că un client își schimbă subiectul de fiecare dată când apare tristețea. "
            "În terapia gestaltistă, accentul cade mai ales pe:"
        ),
        "options": [
            "conștientizarea modului în care contactul este întrerupt în prezent",
            "oferirea de acceptare necondiționată fără intervenție activă",
            "interpretarea transferului ca repetare a relației cu părintele",
            "restructurarea gândurilor automate despre viitor",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care perechi tehnică–orientare sunt corecte pentru consilierea centrată pe persoană "
            "și terapia gestaltistă?"
        ),
        "options": [
            "parafrazarea — consilierea centrată pe persoană",
            "reflectarea sentimentelor — consilierea centrată pe persoană",
            "experimentul cu polarități — psihoterapia Gestalt",
            "disputa cognitivă a convingerilor absolute — psihoterapia Gestalt",
        ],
        "correct": "abc",
    },
    {
        "stem": "La Carl R. Rogers, incongruența apare când există o tensiune între:",
        "options": [
            "experiența trăită și imaginea de sine",
            "figura emergentă și fondul percepției gestaltice",
            "Sinele și Supraeul în aparatul psihic freudian",
            "stările ego Parent și Adult din analiza tranzacțională",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un terapeut în abordarea gestaltistă îl invită pe client să spună „eu mă enervez” "
            "în loc de „te enervează situația”. Scopul principal este:"
        ),
        "options": [
            "recuperarea responsabilității experienței în prezent",
            "validarea necondiționată a clientului ca persoană",
            "identificarea distorsiunilor cognitive beckiene",
            "analiza visului ca material inconștient",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații descriu mai degrabă consilierea centrată pe persoană "
            "decât terapia gestaltistă?"
        ),
        "options": [
            "terapeutul evită directivele și interpretările autoritare",
            "schimbarea este facilitată prin relație autentică, nu prin tehnici prescriptive",
            "accentul cade pe experimente dramatice și confruntări structurate",
            "clientul este văzut ca având tendință de actualizare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care afirmații descriu mai degrabă terapia gestaltistă "
            "decât consilierea centrată pe persoană?"
        ),
        "options": [
            "lucrul cu corpul și cu polaritățile interne în aici și acum",
            "utilizarea experimentelor pentru a intensifica conștientizarea",
            "ascultarea reflectivă ca intervenție centrală nondirectivă",
            "accent pe figura care iese în evidență pe fondul experienței",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un student confundă condițiile facilitatoare rogersiene cu rezistențele gestaltice. "
            "Care asociere este greșită?"
        ),
        "options": [
            "empatia autentică — introiecție gestaltică",
            "congruența terapeutului — condiție facilitatoare rogersiană",
            "acceptarea necondiționată — condiție facilitatoare rogersiană",
            "confluența — confundarea granițelor, nu o condiție facilitatoare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În grupurile centrate pe persoană, coordonatorul rogersian se deosebește de un terapeut "
            "în abordarea gestaltistă prin faptul că primul:"
        ),
        "options": [
            "facilitează procesul fără a conduce autoritar grupul",
            "folosește scena și rolurile ca tehnică principală",
            "prescrie experimente obligatorii pentru fiecare participant",
            "interpretează simbolic visul fiecărui membru",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Clientul relatează: „Simt că nu știu ce vreau; parcă trăiesc după regulile altora.” "
            "În consilierea centrată pe persoană (Carl R. Rogers), terapeutul ar pune accent pe:"
        ),
        "options": [
            "explorarea condițiilor de valoare și a propriei experiențe autentice",
            "interpretarea imediată a fixării în stadiul anal freudian",
            "prescrierea unui plan comportamental de expunere graduală",
            "restructurarea ierarhiei generaționale în familie",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Clientul relatează: „Simt că nu știu ce vreau; parcă trăiesc după regulile altora.” "
            "În terapia gestaltistă, acest enunț ar fi abordat mai ales prin:"
        ),
        "options": [
            "identificarea introiecției și a pierderii contactului cu propriile nevoi",
            "disputarea convingerii iraționale „trebuie să fiu perfect”",
            "analiza transferului ca relație repetată din copilărie",
            "antrenarea relaxării progresive înainte de expunere",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care intervenții aparțin mai probabil consilierii centrate pe persoană "
            "decât terapiei gestaltiste?"
        ),
        "options": [
            "reflectarea tip ecou a mesajului clientului",
            "parafrazarea conținutului verbal",
            "tehnica scaunului gol cu două părți opuse",
            "clarificarea sentimentelor exprimate indirect",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Un client spune: „Mă simt gol când nu primesc aprobare.” Consilierea centrată pe persoană "
            "și terapia gestaltistă s-ar întâlni în ideea că:"
        ),
        "options": [
            "problema ține de pierderea contactului cu sine, nu doar de simptom",
            "soluția este interpretarea autoritară a inconștientului",
            "clientul trebuie condus pas cu pas de terapeut",
            "emoția trebuie eliminată prin raționalizare intelectuală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client spune: „Mă simt gol când nu primesc aprobare.” Ambele orientări recunosc o "
            "problemă de contact cu sine, dar terapia gestaltistă ar tinde mai mult să:"
        ),
        "options": [
            "transforme experiența în conștientizare activă și experiment în prezent",
            "reflectare empatică fără intervenții experiențiale",
            "lucreze exclusiv cu istoricul infantil în interpretare",
            "aplice desensibilizarea sistematică pentru anxietate",
        ],
        "correct": "a",
    },
    {
        "stem": "„Locusul de evaluare intern” la Carl R. Rogers se apropie cel mai mult de ideea gestaltică că:",
        "options": [
            "clientul poate recupera capacitatea de a-și asuma propria experiență",
            "terapeutul devine autoritatea morală principală",
            "contactul autentic este imposibil fără interpretarea visului",
            "schimbarea apare doar prin întărire externă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care pereche client–intervenție este potrivită pentru terapia gestaltistă, "
            "nu pentru consilierea centrată pe persoană clasică?"
        ),
        "options": [
            "client care își strânge pumnii când spune „nu sunt supărat” — lucrul cu corpul",
            "client care cere sfaturi directe — reflectarea dependenței de expert",
            "client care plânge în tăcere — reflectarea emoției",
            "client care exprimă ambivalență — clarificarea mesajului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Afirmația că consilierea centrată pe persoană și terapia gestaltistă sunt "
            "nondirective în același sens este:"
        ),
        "options": [
            "parțial adevărată: Rogers e mai nondirectiv; terapia gestaltistă folosește intervenții active",
            "complet adevărată: terapia gestaltistă nu folosește experimente",
            "falsă: Rogers folosește interpretarea freudiană central",
            "falsă: terapia gestaltistă respinge contactul cu prezentul",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Terapeutul în consilierea centrată pe persoană răspunde la o confuzie identitară mai ales "
            "prin empatie și reflectare. Terapeutul în abordarea gestaltistă ar adăuga mai probabil:"
        ),
        "options": [
            "un experiment pentru a aduce în conștiență blocajul din contact",
            "o interpretare a complexului Oedip",
            "o ierarhie de expunere la stimuli fobici",
            "prescrierea simptomului în terapia de familie",
        ],
        "correct": "a",
    },
    # —— Mecanisme de apărare vs rezistențe la contact (19–44) ——
    {
        "stem": (
            "Un adolescent spune: „Profesorul e idiot”, deși e furios că a fost mustrat. "
            "În terapia gestaltistă, explicația prioritară este:"
        ),
        "options": [
            "proiecție — atribuirea propriei trăiri altcuiva",
            "sublimare — canalizarea impulsului spre activitate valoroasă",
            "formare reactivă — comportament opus față de impuls",
            "reprimare — excluderea din conștiință a conținutului dureroase",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un adolescent spune: „Profesorul e idiot”, deși e furios că a fost mustrat. "
            "Perspectiva psihodinamică ar putea invoca tot proiecția, dar diferența față de "
            "terapia gestaltistă este că:"
        ),
        "options": [
            "terapia gestaltistă pune accent pe întreruperea contactului în prezent, nu pe explicația istorică",
            "terapia gestaltistă consideră proiecția un mecanism de apărare al Eului freudian",
            "psihodinamica lucrează doar cu corpul și experimentul",
            "ambele reduc proiecția la o tehnică rogersiană",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Clientul repetă mecanic: „Trebuie să fiu cuminte, altfel nu mă iubesc.” "
            "Rezistența gestaltică ilustrată este:"
        ),
        "options": [
            "introiecție — preluarea unei reguli fără asimilare personală",
            "deflecție — evitarea contactului prin schimbarea subiectului",
            "regresie — revenirea la comportamente infantile",
            "deplasare — redirecționarea impulsului spre o țintă mai sigură",
        ],
        "correct": "a",
    },
    {
        "stem": "În psihodinamic, introiecția se referă mai ales la:",
        "options": [
            "internalizarea unor figuri, norme sau atitudini în structura psihică",
            "evitarea contactului prin glume și deviere de subiect",
            "confundarea granițelor dintre sine și partener",
            "întoarcerea energiei împotriva propriului corp",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Confuzia frecventă apare deoarece termenul „introiecție” în terapia gestaltistă "
            "accentuează mai mult:"
        ),
        "options": [
            "„înghițirea” unei reguli fără a o digera sau a o asimila",
            "reprimarea conținutului inconștient în Eul freudian",
            "canalizarea impulsului sexual spre artă",
            "refuzul de a percepe o realitate medicală amenințătoare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "O persoană își mușcă buzele când e nervoasă, dar spune că „e calmă”. "
            "Conceptul gestaltic cel mai potrivit:"
        ),
        "options": [
            "retroflexie — energia îndreptată împotriva propriei persoane",
            "negare — refuzul de a recunoaște o realitate amenințătoare",
            "intelectualizare — explicarea abstractă fără trăire emoțională",
            "confluență — pierderea granițelor cu celălalt",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Formarea reactivă s-ar asemăna superficial cu retroflexia, dar se deosebește prin faptul că:"
        ),
        "options": [
            "formarea reactivă înlocuiește impulsul cu un comportament opus, nu îl întoarce spre sine",
            "retroflexia presupune comportament excesiv de amabil față de alții",
            "formarea reactivă este o rezistență la contact gestaltică standard",
            "retroflexia exclude orice implicare corporală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Într-o ședință, clientul râde permanent când atinge tema abandonului. "
            "Rezistența gestaltică:"
        ),
        "options": [
            "deflecție — devierea contactului direct cu experiența",
            "raționalizare freudiană — motive „logice” pentru comportament",
            "sublimare — orientarea impulsului spre activitate acceptată",
            "compensare — acoperirea unui defect perceput prin realizări",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Raționalizarea ca mecanism de apărare se apropie de deflecție, dar diferența esențială "
            "este că raționalizarea:"
        ),
        "options": [
            "construiește explicații plauzibile pentru un motiv inacceptabil",
            "evită contactul prin umor fără a oferi neapărat o explicație elaborată",
            "presupune confundarea granițelor cu partenerul de relație",
            "canalizează impulsul agresiv spre sport competitiv",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un student se dizolvă în grup: „Spuneți voi ce cred, eu sunt de acord cu toți.” "
            "Rezistența gestaltică:"
        ),
        "options": [
            "confluență — pierderea graniței dintre sine și ceilalți",
            "proiecție — atribuirea furiei proprii liderului de grup",
            "reprimare — uitarea conștientă a unui eveniment traumatic",
            "regresie — revenirea la comportamente de vârstă fragedă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Confluența nu trebuie confundată cu regresia, deoarece regresia presupune mai ales:"
        ),
        "options": [
            "revenirea la un nivel mai infantil de funcționare sub stres",
            "pierderea granițelor în relația actuală fără nevoie de protecție infantilă",
            "atribuirea altora a propriilor sentimente",
            "canalizarea impulsului spre activități social valoroase",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care exemple ilustrează rezistențe la contact gestaltice, nu mecanisme de apărare freudiene?"
        ),
        "options": [
            "clientul schimbă subiectul când apare emoția — deflecție",
            "clientul își critică corpul în loc să exprime furia — retroflexie",
            "clientul uită complet o amintire traumatică — reprimare",
            "clientul preia o regulă familială fără a o asimila — introiecție gestaltică",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care exemple ilustrează mecanisme de apărare freudiene, nu rezistențe gestaltice clasice?"
        ),
        "options": [
            "negarea unui diagnostic grav în ciuda dovezilor",
            "sublimarea agresivității prin pictură",
            "experimentul scaunului gol cu două părți interne",
            "deplasarea furiei de la șef spre partener",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Confuzia frecventă „proiecție gestaltică = proiecție freudiană” este:"
        ),
        "options": [
            "parțial justificată ca etichetă, dar cadrele teoretice și intervenția diferă",
            "total greșită: terapia gestaltistă nu folosește termenul proiecție",
            "identică: ambele vizează doar atribuirea propriilor dorințe sexuale",
            "inversă: doar Freud vorbește despre atribuire către altul",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Clientul spune: „Știu că părinții m-au iubit, dar nu simt nimic când vorbesc despre asta.” "
            "Mecanismul de apărare cel mai probabil:"
        ),
        "options": [
            "reprimare — conținutul emoțional rămâne în afara conștiinței",
            "deflecție — schimbarea subiectului prin glume",
            "confluență — pierderea granițelor în relație",
            "retroflexie — criticarea propriului corp",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Clientul spune: „Știu că părinții m-au iubit, dar nu simt nimic când vorbesc despre asta.” "
            "Abordat din perspectiva terapiei gestaltiste, accentul ar cădea pe:"
        ),
        "options": [
            "posibilă desensibilizare sau blocaj în contactul cu experiența trăită",
            "interpretarea obligatorie a complexului Oedip",
            "disputa convingerii „trebuie să fiu recunoscător”",
            "prescrierea simptomului în terapia strategică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un manager devine excesiv de amabil după ce are gânduri agresive despre subalterni. "
            "Mecanismul de apărare:"
        ),
        "options": [
            "formare reactivă",
            "introiecție gestaltică",
            "confluență",
            "deflecție",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client în terapia gestaltistă își strânge gâtul și vocea devine șoptită când exprimă furie. "
            "Aceasta sugerează mai degrabă:"
        ),
        "options": [
            "retroflexie — inhibarea expresiei prin întoarcerea tensiunii spre sine",
            "formare reactivă — înlocuirea furiei cu amabilitate excesivă",
            "sublimare — canalizarea furiei spre activitate artistică",
            "negare — refuzul de a recunoaște existența conflictului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Intelectualizarea se apropie de deflecție, dar clientul care intelectualizează:"
        ),
        "options": [
            "vorbește analitic despre durere, evitând trăirea emoțională",
            "schimbă subiectul prin glume fără analiză elaborată",
            "se identifică complet cu opinia interlocutorului",
            "își atribuie altora propriile impulsuri",
        ],
        "correct": "a",
    },
    {
        "stem": "Care perechi fenomen–cadru sunt corecte?",
        "options": [
            "deplasare — mecanism de apărare freudian",
            "retroflexie — rezistență la contact gestaltică",
            "retroflexie — mecanism de apărare standard al Eului freudian",
            "confluență — rezistență la contact gestaltică",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "În ciclul experienței gestaltice, blocajul la contact poate menține o rezistență. "
            "Mecanismele de apărare freudiene:"
        ),
        "options": [
            "aparțin mai degrabă aparatului psihic și conflictului inconștient",
            "sunt identice cu deflecția și confluența în orice manual",
            "nu au nicio legătură cu evitarea experienței dureroase",
            "explică doar comportamentele observabile, nu procesul subiectiv",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un copil devine „perfect” după ce a fost pedepsit pentru greșeli. "
            "Interpretarea psihodinamică probabilă:"
        ),
        "options": [
            "formare reactivă sau reacție la amenințarea retragerii afecțiunii",
            "confluență cu părintele în sens gestaltic",
            "desensibilizare sistematică a anxietății sociale",
            "triangulare în terapia de familie structurală",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client își critică dur propriile reacții, respectă standarde rigide de perfecțiune "
            "și își întoarce energia critică spre sine, evitând confruntarea directă. "
            "Din perspectiva terapiei gestaltiste, acest tipar corespunde mai probabil:"
        ),
        "options": [
            "introiecției unor standarde rigide și retroflexiei criticii spre sine",
            "sublimării complete a impulsului fără tensiune internă",
            "funcționării doar din Adult în analiza tranzacțională",
            "rezolvării conflictului prin interpretarea visului",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care afirmații contrazic confuzia „rezistența = mecanism de apărare, termenii sunt interșanjabili”?"
        ),
        "options": [
            "rezistențele gestaltice descriu moduri de a evita contactul autentic în prezent",
            "mecanismele de apărare freudiene mediază conflicte inconștiente în aparatul psihic",
            "deflecția și reprimarea sunt același fenomen în orice cadru",
            "introiecția gestaltică nu este identică cu introiecția ca mecanism de internalizare",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Clientul spune: „Nu e vorba de furie, doar analizez obiectiv situația” — timp de 40 de minute. "
            "Cel mai probabil:"
        ),
        "options": [
            "intelectualizare ca mecanism de apărare",
            "retroflexie gestaltică prin critică corporală",
            "confluență cu terapeutul",
            "transfer pozitiv în relația terapeutică",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă terapeutul în abordarea gestaltistă intervine, ar putea transforma asta în lucru cu:"
        ),
        "options": [
            "deflecția sau evitarea contactului direct cu emoția",
            "reprimarea unui conținut din prima copilărie, fără prezent",
            "ierarhia de expunere în fobie socială",
            "restructurarea granițelor familiale difuze",
        ],
        "correct": "a",
    },
    # —— Mix avansat (45–50) ——
    {
        "stem": (
            "Un client în consilierea centrată pe persoană ar putea beneficia de reflectare empatică; "
            "același client, în terapia gestaltistă, ar putea fi invitat la un experiment. "
            "Diferența logică este că:"
        ),
        "options": [
            "consilierea centrată pe persoană facilitează autoexplorarea relațională; "
            "terapia gestaltistă activează conștientizarea experiențială",
            "consilierea centrată pe persoană folosește interpretarea freudiană; "
            "terapia gestaltistă respinge empatia",
            "terapia gestaltistă este nondirectivă în același mod cu Rogers",
            "consilierea centrată pe persoană lucrează obligatoriu cu scaunul gol",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În terapia psihodinamică, analiza rezistențelor urmărește materialul inconștient. "
            "În terapia gestaltistă, „rezistența la contact”:"
        ),
        "options": [
            "marchează modul în care clientul evită experiența și contactul în prezent",
            "este sinonimă cu mecanismul de apărare reprimare",
            "se rezolvă doar prin interpretarea visului",
            "exclude corpul și emoția din ședință",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care scenarii cer concept gestaltic, nu mecanism de apărare freudian?"
        ),
        "options": [
            "clientul vorbește despre durere în al treilea persoană — deflecție",
            "clientul uită complet o întâmplare traumatică — reprimare",
            "clientul își pierde granițele în cuplu — confluență",
            "clientul atribuie altora propria invidie — proiecție gestaltică",
        ],
        "correct": "acd",
    },
    {
        "stem": (
            "Un terapeut spune: „În terapia gestaltistă, proiecția întrerupe contactul; "
            "în psihodinamic, proiecția apără Eul.” Afirmația este:"
        ),
        "options": [
            "corectă ca distincție de accent, deși termenul este comun",
            "greșită: doar Freud folosește proiecția",
            "greșită: terapia gestaltistă respinge conceptul de proiecție",
            "corectă doar dacă proiecția nu apare niciodată în terapia gestaltistă",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "La Carl R. Rogers, acceptarea necondiționată contracarează condițiile de valoare. "
            "În terapia gestaltistă, echivalentul funcțional al eliberării de reguli neasimilate "
            "este mai apropiat de:"
        ),
        "options": [
            "conștientizarea introiecției și recuperarea contactului cu propria experiență",
            "reprimarea conținutului inconștient",
            "sublimarea impulsului spre activitate artistică",
            "interpretarea transferului negativ",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un client își mușcă buzele și spune că e calm. Din perspectiva terapiei gestaltiste, "
            "fenomenul evidențiat este cel mai probabil:"
        ),
        "options": [
            "retroflexie — îndreptarea impulsului spre sine, nu spre contact",
            "condiții facilitatoare rogersiene",
            "triada cognitivă a depresiei la Aaron T. Beck",
            "stările ego Parent–Adult–Copil",
        ],
        "correct": "a",
    },
]
