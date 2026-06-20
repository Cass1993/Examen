"""Explicații didactice — Statistică II segment 11: recapitulare rapidă (ID 11186–11225)."""

from __future__ import annotations

from typing import List

RECAP_RAPID_EXPLANATIONS: List[str] = [
    # 11186
    (
        "Adevărat. Eroarea aleatorie produce deviații aleatorii în jurul valorii reale — "
        "unele măsurători sunt peste, altele sub, dar nu împing sistematic media într-o "
        "direcție. Spre deosebire de bias (eroare sistematică), nu schimbă centrul "
        "adevărat al distribuției."
    ),
    # 11187
    (
        "M/F sunt categorii fără ordine naturală și fără magnitudine — scară nominală. "
        "Ordinală presupune ordine; interval și raport permit operații suplimentare pe "
        "care genul nu le justifică."
    ),
    # 11188
    (
        "Genul e nominal → frecvent teste neparametrice (χ², Mann-Whitney pe ranguri "
        "etc.). Timpul de reacție are zero absolut și raporturi sensibile → scară de "
        "raport → teste parametrice pot fi adecvate dacă presupunerile sunt îndeplinite. "
        "Genul nu devine raport doar pentru că e codat numeric; timpul nu e nominal."
    ),
    # 11189
    (
        "Timpul de reacție se măsoară în unități cu zero absolut (0 s = absența "
        "timpului) și raporturi interpretabile (0,64 s e de două ori 0,32 s). Asta "
        "îl plasează pe scară de raport, nu nominală sau pur ordinală."
    ),
    # 11190
    (
        "Notele școlare ordonează elevii, dar distanțele între note nu sunt garantat "
        "egale — de aceea sunt discutate ca ordinal, nu ca interval sau raport pur. "
        "Nu e nominală (există ordine) și nu are zero absolut „lipsă totală de "
        "performanță”."
    ),
    # 11191
    (
        "Numărul de răspunsuri corecte e o numărătoare (0, 1, 2…) — variabilă discretă. "
        "Se apropie de scară de raport/numărătoare, nu de nominală (categorii fără "
        "ordine) și nu e latentă (se vede direct în scor)."
    ),
    # 11192
    (
        "Fals. Corelația arată asociere statistică, nu mecanism cauzal. Fără "
        "manipulare experimentală, controlul confuzilor sau design longitudinal "
        "adecvat, nu poți concluziona că X o determină pe Y."
    ),
    # 11193
    (
        "Aleatorie = zgomot în jurul mediei; sistematică = bias care deplasează "
        "estimarea. Biasul nu dispare doar mărind N — trebuie corectat la sursă. "
        "Aleatoria nu împinge media mereu într-o direcție fixă."
    ),
    # 11194
    (
        "Definiția mediei ca „balanță” implică Σ(Xᵢ − m) = 0: suma abaterilor pozitive "
        "anulează suma negative. Nu e N−1 (împărțitor la dispersie), nu 1 și nu s²."
    ),
    # 11195
    (
        "Adunarea unei constante translatează toți indicatorii de locație (M, Me, Mo) "
        "cu +5, dar nu schimbă distanțele relative → s rămâne aceeași. cv poate varia "
        "ușor pentru că m se schimbă, dar nu „obligatoriu +5 puncte” — formularea "
        "aceea e capcană."
    ),
    # 11196
    (
        "Înmulțirea cu 2 scalează media și abaterea standard (și s² cu k²). Unitatea se "
        "schimbă, dar nu rămâne doar media — dispersia crește. „Doar media se schimbă” "
        "și „s² identică” sunt false."
    ),
    # 11197
    (
        "Pentru eșantion, s² folosește N−1 (estimare fără bias al varianței populației). "
        "N e pentru dispersia populației σ² când ai tot setul. N+1 sau N−2 nu sunt "
        "convențiile standard din curs."
    ),
    # 11198
    (
        "Pragurile din curs: cv < 15% dispersie mică; ~25% moderată; > 30% mare. 25% "
        "e în zona medie, nu minimă și nu extremă. cv = 0 ar însemna s = 0."
    ),
    # 11199
    (
        "Adevărat. Simetria plasează modul, mediana și media în același punct — "
        "relația Mo = Me = M. La asimetrie pozitivă ordinea se schimbă (Mo < Me < M)."
    ),
    # 11200
    (
        "Coada lungă la dreapta trage media în sus peste mediană, iar modul rămâne cel "
        "mai jos. De aceea Mo < Me < M. Celelalte ordini corespund asimetriei negative "
        "sau simetriei."
    ),
    # 11201
    (
        "Standardizarea z: M = 0, s = 1, forma distribuției (asimetrie, relativ) se "
        "păstrează — doar scalează pe axă. Nu inversează media și SD (1 și 0)."
    ),
    # 11202
    (
        "Regula empirică 68–95–99,7: ~68% între ±1σ, ~95% între ±2σ, ~99,7% între "
        "±3σ. Intervalul ±1σ e primul prag, nu ±2σ sau ±3σ."
    ),
    # 11203
    (
        "μₘ = μ: distribuția teoretică a mediilor eșantioanelor e centrată pe media "
        "populației. Un eșantion concret poate avea m ≠ μ — asta nu contrazice TLC. "
        "μₘ nu e m observat și nu e σ/√N (ăla e sm)."
    ),
    # 11204
    (
        "sm = σ/√N: mai mulți participanți → precizie mai mare a estimării mediei. "
        "sm nu crește cu N și nu devine σ×√N — confuzia σ/√N vs σ×√N e capcană "
        "frecventă."
    ),
    # 11205
    (
        "Adevărat. N ≥ 30 e regulă practică pentru „eșantion mare” și aplicarea "
        "aproximării normale a mediilor — orientare din curs, nu teoremă rigidă "
        "pentru orice populație."
    ),
    # 11206
    (
        "Respingi H₀ când p ≤ α sau când z depășește pragul critic (conform tipului de "
        "test). m = μ în eșantion nu e suficient — contează semnificația statistică. "
        "α singur, fără p sau z, nu decide."
    ),
    # 11207
    (
        "Unilateral α = 0,05 → zcritic ≈ 1,65. 1,96 e bilateral 5%; 2,58 e pentru "
        "α = 0,01 bilateral; 0,05 e nivelul α, nu valoarea critică z."
    ),
    # 11208
    (
        "Histograma: bare contigue pe intervale pentru variabile continue. Diagrama cu "
        "bare: categorii discrete separate, cu spații. Nu inversați — histograma nu e "
        "pentru nominal fără ordine pe axă continuă."
    ),
    # 11209
    (
        "Mediana și RQ (IQR) se bazează pe ranguri/percentile — nu sunt trase de "
        "extreme ca media. Media și suma pătratelor abaterilor sunt sensibile la "
        "outliers."
    ),
    # 11210
    (
        "Pe nominală permiți numărarea și modul (categoria cea mai frecventă). Mediana "
        "și media presupun ordine sau magnitudine — nejustificate strict pe nominală."
    ),
    # 11211
    (
        "Medie simplă: ΣX/N. Medie grupată: Σ(X·f)/Σf. Σ(Xᵢ−m)/N nu e medie; √s² e "
        "abaterea standard, nu media."
    ),
    # 11212
    (
        "s² cu N−1 e convenția eșantionului din curs; s = √s². Varianta cu N la "
        "numitor e pentru populație sau alte contexte — capcană plauzibilă. s nu e "
        "suma abaterilor împărțită la N−1."
    ),
    # 11213
    (
        "cv = (s/m)×100 compară dispersia relativ la medie. Praguri: <15% mică, "
        "~25% medie, >30% mare. cv nu e s+m — unitățile nu se adună așa."
    ),
    # 11214
    (
        "z = (X−m)/s pentru un scor individual în eșantion. (m−X)/s inversează semnul; "
        "(X−μ)/sm e z pentru media eșantionului față de populație, nu pentru fiecare X."
    ),
    # 11215
    (
        "Transformare inversă X = m + z·s. sm = σ/√N pentru eroarea mediei. z "
        "eșantion = (m−μ)/sm testează ipoteza despre μ. z = (X−m)/s e per "
        "participant, nu același lucru."
    ),
    # 11216
    (
        "Amplitudinea R = max − min; RQ = Q₃ − Q₁ (spreadul central 50%). R ≠ Q₃+Q₁; "
        "RQ nu e tot R — R e mai sensibil la extreme."
    ),
    # 11217
    (
        "Patru idei: ierarhia Stevens; exemple gen/raport/ordinal; teste parametrice vs "
        "neparametrice depind de scară și distribuție. Toate patru variantele sunt "
        "corecte — nu confunda cod numeric cu scară de raport."
    ),
    # 11218
    (
        "VI = predictor/manipulare; VD = rezultat. Observate = măsurate direct; "
        "latente = inferate (anxietate, g). Latenta nu e sinonim VD; observatele se "
        "măsoară direct — afirmația contrară e falsă."
    ),
    # 11219
    (
        "Mod pe nominală; mediană când asimetrie/outliers; medie pe date simetrice "
        "interval/raport. Media pe nominală e nejustificată teoretic — variantă "
        "capcană frecventă."
    ),
    # 11220
    (
        "p ≤ α → respingi H₀ (semnificativ). Nu demonstrezi automat efect mare sau H₁ "
        "cu certitudine — doar că dovada contra H₀ depășește pragul. Respingerea "
        "indiferent de p e incorectă."
    ),
    # 11221
    (
        "Patru proprietăți de reținut la ±k și ×k: locația (M, Me) se translatează; "
        "s nu se schimbă la adunare; s și M scalează la înmulțire; s² scalează cu k². "
        "Esential pentru itemi de transformare."
    ),
    # 11222
    (
        "sm scade cu N; μₘ = μ; TLC: forma normală a mediilor la N mare. TLC nu "
        "garantează m = μ în fiecare eșantion mic — asta ar confunda teorema cu "
        "observația unică."
    ),
    # 11223
    (
        "H₀ vs H₁; respingere la p ≤ α sau z ≥ zcritic; zcritic 1,65 unilateral. "
        "p > α nu demonstrează H₀ cu certitudine — doar lipsă de dovezi suficiente "
        "contra H₀ la α ales."
    ),
    # 11224
    (
        "Patru blocuri de formule must-know din curs: tendință centrală și dispersie; "
        "cv și z; inferență (sm, z eșantion) și amplitudini; identități Σ(X−m)=0 și "
        "medie grupată. Ultima variantă greșită amesteca N−1 cu suma abaterilor."
    ),
    # 11225
    (
        "Recapitulare finală: scale și tipuri de teste; erori și indicatori centrali; "
        "asimetrie și transformări; inferență (sm, TLC, ipoteze, z). Cauzalitatea din "
        "corelație nu face parte — e capcană de eliminat din checklist."
    ),
]

assert len(RECAP_RAPID_EXPLANATIONS) == 40
