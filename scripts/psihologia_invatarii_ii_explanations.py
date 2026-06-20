"""Explicații didactice — Psihologia învățării II (ID 10501–10960)."""

from __future__ import annotations

from typing import List

from scripts.psihologia_invatarii_ii_bandura_explanations import BANDURA_EXPLANATIONS
from scripts.psihologia_invatarii_ii_cognitive_explanations import COGNITIVE_EXPLANATIONS
from scripts.psihologia_invatarii_ii_atitudini_profesor_explanations import (
    ATITUDINI_PROFESOR_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_predare_stiluri_explanations import (
    PREDARE_STILURI_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_roluri_empatie_explanations import (
    ROLURI_EMPATIE_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_lider_grila_explanations import (
    LIDER_GRILA_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_diferente_grila_explanations import (
    DIFERENTE_GRILA_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_educatie_invatare_explanations import (
    EDUCATIE_INVATARE_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_profesor_eficient_explanations import (
    PROFESOR_EFICIENT_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_tipuri_forme_explanations import (
    TIPURI_FORME_EXPLANATIONS,
)
from scripts.psihologia_invatarii_ii_umanist_explanations import UMANIST_EXPLANATIONS
from scripts.psihologia_invatarii_ii_vark_explanations import VARK_EXPLANATIONS

PSIHOLOGIA_INVATARII_II_EXPLANATIONS: List[str] = [
    # 10501
    (
        "Adevărat. Teoriile asociaționiste și behavioriste pun în centru factorii "
        "externi: stimuli din mediu, legături între stimul și răspuns, și "
        "consecințele comportamentului (recompense, pedepse). Nu reduc totul la "
        "biologie innată sau la procese introspective — studiază ce se poate observa "
        "și măsura."
    ),
    # 10502
    (
        "În condiționarea clasică pavloviană, la început stimulul neutru (ex. "
        "clopoțelul) nu produce salivare. Stimulul necondiționat (mâncarea) produce "
        "răspunsul necondiționat (salivarea). După asocieri repetate SN+SI, stimulul "
        "devine condiționat și produce singur răspunsul condiționat."
    ),
    # 10503
    (
        "Achiziția este formarea legăturii SC–RC. Generalizarea înseamnă că organismul "
        "reacționează similar la stimuli asemănători cu stimulul condiționat. "
        "Extincția și discriminarea sunt procese distincte: extincția reduce RC, "
        "discriminarea diferențiază SC de stimuli similari."
    ),
    # 10504
    (
        "În condiționarea clasică: SI provoacă RI (reflex natural); după antrenare, "
        "SC provoacă RC. Înainte de antrenare, SN nu produce RC stabil — e neutru. "
        "Operantele skinneriene nu înlocuiesc această logică S–R reflexivă."
    ),
    # 10505
    (
        "Watson a fondat behaviorismul ca reacție la psihologia introspectivă: obiectul "
        "științei trebuie să fie comportamentul observabil, iar învățarea se produce "
        "prin condiționare în mediu — nu prin analiza viselor sau a experienței "
        "subiective inaccesibile altora. Hărțile cognitive (Tolman) și reducerea "
        "impulsului (Hull) aparțin altor orientări."
    ),
    # 10506
    (
        "Adevărat. Little Albert: un stimul neutru (șobolan) a fost asociat cu un "
        "sunet puternic care producea frică. Ulterior, copilul a devenit anxios față "
        "de șobolan și stimuli similari — demonstrând că emoțiile pot fi condiționate."
    ),
    # 10507
    (
        "Watson: comportament modelat de mediu și condiționare; emoții condiționabile, "
        "nu doar mișcări. Tolman (învățare latentă) și Hull (drive) aparțin altor "
        "orientări, deși dialoghează cu behaviorismul."
    ),
    # 10508
    (
        "Thorndike a observat că pisicile din puzzle-box învață prin încercare și "
        "eroare: conexiunile care duc la deschiderea ușii (satisfacție) se "
        "consolidează; cele care nu duc la scop se slăbesc. Legea efectului este "
        "baza conexionismului."
    ),
    # 10509
    (
        "Thorndike: încercare și eroare, întărirea conexiunilor utile, slăbirea celor "
        "inutile. Nu e vorba de gramatică innată (Chomsky) sau de stadii piagetiene — "
        "e învățare asociativă prin consecințe ale răspunsului."
    ),
    # 10510
    (
        "Fals. Thorndike pune accent pe consecințele răspunsului (legea efectului). "
        "Skinner dezvoltă condiționarea operantă. Salivarea la clopoțel e Pavlov "
        "(clasică), nu Thorndike sau Skinner în sensul operant."
    ),
    # 10511
    (
        "Hull: organismul acționează pentru a reduce drive-uri (foame, sete, tensiune). "
        "Comportamentul întărit devine habit — obișnuință care restabilește "
        "echilibrul. Nu e teorie cognitivă pură; leagă învățarea de stări "
        "fiziologice interne."
    ),
    # 10512
    (
        "Drive-ul motivează acțiunea (nevoie biologică sau tensiune). Habit-ul este "
        "tendința consolidată a unui răspuns după întăriri repetate. Latent learning "
        "e Tolman; salivarea la clopoțel e Pavlov."
    ),
    # 10513
    (
        "Adevărat. Skinner analizează relația răspuns–consecință: comportamentul "
        "operant este emis de organism, iar consecința care urmează determină dacă "
        "va fi repetat. Pavlov studiază asocierea între stimuli care precedă un "
        "reflex deja existent."
    ),
    # 10514
    (
        "Întărirea pozitivă adaugă ceva plăcut; întărirea negativă elimină ceva "
        "neplăcut — ambele cresc probabilitatea repetării comportamentului. Nu "
        "sunt același lucru și nu funcționează doar în condiționarea clasică."
    ),
    # 10515
    (
        "Operant: întărire pozitivă (adaugare stimul plăcut), negativă (eliminare "
        "aversiv), pedeapsă (scădere frecvență). Asimilarea piagetiană descrie "
        "integrarea informației în scheme — alt cadru teoretic."
    ),
    # 10516
    (
        "Clasică: stimuli asociați, răspuns reflexiv (Pavlov). Operantă: consecințe "
        "după comportament (Skinner). Ambele sunt behavioriste, dar mecanismele "
        "diferă — confuzia între ele e capcană frecventă la grilă."
    ),
    # 10517
    (
        "Condiționarea instrumentală/operantă modifică frecvența comportamentului "
        "prin recompensă, omisiune, pedeapsă sau evitare — nu prin asocierea "
        "unui clopoțel cu hrană în sens pavlovian pur."
    ),
    # 10518
    (
        "Cele patru consecințe operante: întărire pozitivă (+ stimul plăcut), "
        "negativă (− stimul aversiv), pedeapsă pozitivă (+ aversiv), pedeapsă "
        "negativă/omisiune (− stimul plăcut). Toate patru sunt categorii canonice "
        "în analiza skinneriană."
    ),
    # 10519
    (
        "Întărirea continuă ajută la învățarea inițială (fiecare răspuns e "
        "recompensat). Programele parțiale, mai ales variabile, mențin comportamentul "
        "mai greu de stins — de aceea jocurile de noroc și notificările imprevizibile "
        "sunt atât de captivante."
    ),
    # 10520
    (
        "Raportul variabil (recompensă după un număr imprevizibil de răspunsuri) "
        "produce comportament foarte persistent. Întărirea continuă facilitează "
        "achiziția, dar comportamentul se stinge rapid când recompensa dispare."
    ),
    # 10521
    (
        "Tolman: șobolanii în labirint învață ruta fără recompensă la fiecare "
        "încercare — învățare latentă. Când apare hrana, performanța sare — "
        "dovedind o reprezentare cognitivă (hartă) a mediului, nu doar obiceiuri "
        "mecanice."
    ),
    # 10522
    (
        "Tolman: comportament orientat spre scop, variabile intermediare (anticipări, "
        "cerințe), învățare latentă. Nu reduce totul la reflexe fără cogniție — "
        "depășește behaviorismul strict."
    ),
    # 10523
    (
        "Tolman introduce procese interne orientative (scopuri, hărți cognitive). "
        "Skinner strict insistă pe consecințe observabile și uneori evită "
        "explicațiile prin stări interne. Amândoi studiază învățarea animală și "
        "umană în mediu controlat."
    ),
    # 10524
    (
        "Învățarea latentă: performanța apare când recompensa e introdusă, deși "
        "învățarea avusese loc mai devreme fără întărire vizibilă. Experimentul "
        "clasic Tolman — labirintul cu șobolani."
    ),
    # 10525
    (
        "Extincție clasică: SC nu mai e urmat de SI → RC scade. Extincție operantă: "
        "întărirea încetează → comportamentul scade. Ambele reduc răspunsul, dar "
        "prin mecanisme diferite."
    ),
    # 10526
    (
        "Generalizare: reacție la stimuli similari cu SC (ex. tonuri apropiate). "
        "Discriminare: răspuns doar la SC, nu la similari — antrenată prin "
        "diferențierea consecințelor pentru stimuli diferiți."
    ),
    # 10527
    (
        "Interval fix: recompensă după trecerea unui timp constant (salariu la "
        "date fixe). Raport fix ar fi după N răspunsuri. Interval variabil = timp "
        "imprevizibil între recompense."
    ),
    # 10528
    (
        "Raport fix = după N răspunsuri constant; raport variabil = după N mediu "
        "imprevizibil; interval variabil = timp mediu imprevizibil. Interval fix "
        "la naștere nu are sens ca program de întărire legat de comportament."
    ),
    # 10529
    (
        "Raport variabil: jocuri de noroc (câștig imprevizibil), rețele sociale "
        "(notificări variabile). Salariul fix la dată calendaristică = interval fix, "
        "nu raport variabil."
    ),
    # 10530
    (
        "Pavlov — condiționare clasică; Watson — behaviorism și mediu; Skinner — "
        "operantă și programe; Tolman — latent learning și hărți cognitive. "
        "Asocierile sunt fundamentale pentru grilă."
    ),
    # 10531
    (
        "Behaviorismul strict explică bine comportamentul observabil și rolul "
        "consecințelor, dar tinde să ignore gândirea, motivația internă și "
        "sensul subiectiv — limite recunoscute chiar de criticii moderne."
    ),
    # 10532
    (
        "Critici: reducere la observabil, creativitate lingvistică greu de redus "
        "la întărire, motivație intrinsecă neglijată. Behaviorismul nu neagă mediul "
        "— dimpotrivă, îl pune în centru."
    ),
    # 10533
    (
        "Behaviorismul explică bine modificarea comportamentului prin consecințe și "
        "formarea obiceiurilor. Nu explică complet conștiința, sensul existențial "
        "sau reorganizarea cognitivă stadială piagetiană."
    ),
    # 10534
    (
        "Hull: drive biologic și habit. Skinner: consecințe observabile și programe "
        "de întărire. Hull nu e Tolman (hărți cognitive); Skinner nu respinge mediul "
        "— îl folosește prin întărire."
    ),
    # 10535
    (
        "Salivarea la clopoțel = Pavlov, condiționare clasică S–R reflex. Skinner "
        "a studiat operante și programe de recompensă. Watson a condus Albert; "
        "Thorndike — legea efectului în puzzle-box."
    ),
    # 10536
    (
        "Thorndike: legea efectului, încercare și eroare. Hull: drive reduction și "
        "habit. Amândoi leagă învățarea de consecințe, dar Hull formalizează "
        "tensiunea biologică mai explicit."
    ),
    # 10537
    (
        "Clasică: stimuli și reflexe; operantă: consecințe după comportament. "
        "Operantă: programe de întărire. Clasică: generalizare/discriminare stimul. "
        "Nu se limitează la sugari sau la moralitate adultă exclusiv."
    ),
    # 10538
    (
        "Watson: frică condiționată (Albert). Skinner: frecvența comportamentului "
        "modificată de consecințe. Contribuții complementare în cadrul behaviorismului."
    ),
    # 10539
    (
        "Procese clasice: achiziție, extincție, generalizare, discriminare. "
        "Toate patru sunt parte din vocabularul condiționării pavloviene și apar "
        "frecvent la examen."
    ),
    # 10540
    (
        "Tolman introduce scopuri și reprezentări cognitive — organismul nu e doar "
        "o „cutie neagră” care reacționează mecanic. Comportamentalismul intențional "
        "face pod către cognitivism."
    ),
    # 10541
    (
        "Legea efectului: strategii care duc la reușită se repetă; cele care eșuează "
        "se abandonează. Harta cognitivă fără recompensă e Tolman; salivarea reflexă "
        "e Pavlov fără încercare și eroare thorndikiană."
    ),
    # 10542
    (
        "Pedeapsă pozitivă = adăugare stimul aversiv după comportament pentru a-l "
        "reduce. Nu e recompensă și nu e eliminare de stimul neplăcut ca întărire "
        "negativă."
    ),
    # 10543
    (
        "Little Albert: asociere stimul neutru–stimul aversiv, generalizare a fricii, "
        "emoții condiționabile. Nu e despre operații formale — e behaviorism "
        "watssonian timpuriu."
    ),
    # 10544
    (
        "Omisiune: retragi recompensa după comportament nedorit (pedeapsă negativă). "
        "Evitare: comportament care previne stimulul aversiv (ex. pleci înainte să "
        "auzi sunetul). Diferit de extincția clasică Pavlov."
    ),
    # 10545
    (
        "Thorndike — legea efectului; Hull — drive și habit; Pavlov — clasică; "
        "Tolman — intențional și latent. Patru perechi canonice pentru sinteză."
    ),
    # 10546
    (
        "Patru limite: cogniție subestimată, creativitate lingvistică, motivație "
        "intrinsecă, sens personal. Behaviorismul rămâne util pentru comportament "
        "observabil, dar nu e teorie completă a învățării umane complexe."
    ),
    # 10547
    (
        "Sticker imprevizibil = raport variabil — menține comportamentul chiar când "
        "recompensele devin rare. Interval fix = timp constant; continuă = fiecare "
        "răspuns recompensat."
    ),
    # 10548
    (
        "Skinner: consecințe controlează operantele; programele de întărire explică "
        "menținerea și extincția. Latent learning e Tolman; legea efectului e "
        "Thorndike."
    ),
    # 10549
    (
        "Pavlov — clasică, reflexe; Watson — behaviorism, Albert; Skinner — operantă. "
        "Hărțile cognitive tolmaniene nu aparțin niciunuia dintre cei trei în forma "
        "strictă."
    ),
    # 10550
    (
        "Adevărat. Behaviorismul explică asocieri și consecințe — util pentru "
        "obiceiuri și comportament observabil. Dar cogniția complexă, creativitatea "
        "și motivația intrinsecă necesită și alte cadre (Tolman, cognitivism, "
        "constructivism)."
    ),
] + BANDURA_EXPLANATIONS + COGNITIVE_EXPLANATIONS + UMANIST_EXPLANATIONS + EDUCATIE_INVATARE_EXPLANATIONS + TIPURI_FORME_EXPLANATIONS + VARK_EXPLANATIONS + DIFERENTE_GRILA_EXPLANATIONS + PROFESOR_EFICIENT_EXPLANATIONS + ATITUDINI_PROFESOR_EXPLANATIONS + PREDARE_STILURI_EXPLANATIONS + ROLURI_EMPATIE_EXPLANATIONS + LIDER_GRILA_EXPLANATIONS

assert len(PSIHOLOGIA_INVATARII_II_EXPLANATIONS) == 460


def attach_explanations(items: list) -> list:
    """Atașează explicațiile la itemi, în ordinea listei."""
    out = []
    for i, row in enumerate(items):
        item = dict(row)
        if i < len(PSIHOLOGIA_INVATARII_II_EXPLANATIONS):
            item["explanation"] = PSIHOLOGIA_INVATARII_II_EXPLANATIONS[i]
        out.append(item)
    return out


def explanation_for_exam_id(item_id: int) -> str:
    """Explicație după id examen (10501–10960)."""
    if 10501 <= int(item_id) <= 10960:
        idx = int(item_id) - 10501
        if 0 <= idx < len(PSIHOLOGIA_INVATARII_II_EXPLANATIONS):
            return PSIHOLOGIA_INVATARII_II_EXPLANATIONS[idx]
    return ""
