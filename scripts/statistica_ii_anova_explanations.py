"""Explicații didactice — Statistică II segment 12: ANOVA (ID 11226–11245)."""

from __future__ import annotations

from typing import List

ANOVA_EXPLANATIONS: List[str] = [
    # 11226
    (
        "Adevărat. H₀ în ANOVA unifactorială: toate mediile populației sunt egale "
        "(μ₁ = μ₂ = … = μₖ). Testul verifică dacă există suficientă varianță între "
        "grupuri față de variabilitatea din interiorul grupurilor pentru a respinge "
        "această ipoteză."
    ),
    # 11227
    (
        "ANOVA compară mediile a trei sau mai multe grupuri/condiții. Pearson e "
        "corelație; frecvențele sunt descriptive; pentru exact două grupuri independente "
        "folosești de obicei testul t, nu ANOVA ca primă alegere (deși F = t²)."
    ),
    # 11228
    (
        "H₀: toate mediile egale. H₁: cel puțin una diferă — nu neapărat toate "
        "diferite între ele. Ultima variantă amestecă absurd varianțe zero/infinit "
        "în loc de formularea standard a ipotezelor."
    ),
    # 11229
    (
        "F = MS₍între₎ / MS₍în₎ — cât de mult variază mediile grupurilor față de "
        "zgomotul din grupuri. Nu e media generală, nu e corelația și nu înlocuiește "
        "interpretarea p."
    ),
    # 11230
    (
        "Trei presupuneri clasice: independența observațiilor, omogenitatea varianțelor "
        "(Levene), normalitatea aproximativă a VD în fiecare grup. Nu ceri medii egale "
        "înainte de test — tocmai asta testezi."
    ),
    # 11231
    (
        "Fiecare test t adaugă risc de eroare tip I; la multe perechi, șansa unei "
        "semnificări false crește. ANOVA face un test omnibus controlat la α. Testul t "
        "funcționează și la >2 grupuri tehnic, dar strategia multiplă e problematică; "
        "ANOVA nu elimină verificarea presupunerilor."
    ),
    # 11232
    (
        "Fals. ANOVA semnificativă spune că nu toate mediile sunt egale, dar nu "
        "identifică perechea — pentru asta folosești teste post-hoc (Tukey, Bonferroni "
        "etc.) cu ajustare pentru comparații multiple."
    ),
    # 11233
    (
        "Varianța totală se împarte în între grupuri (explicată de VI) și în grupuri "
        "(reziduală/eroare). SS₍în₎ reflectă variabilitatea participanților din același "
        "grup, nu „doar” eroarea instrumentului."
    ),
    # 11234
    (
        "Post-hoc compară perechi de medii după F semnificativ, cu control al erorii. "
        "Repetarea t pe fiecare pereche fără ajustare reproduce problema comparațiilor "
        "multiple. Media generală nu răspunde la „care grupuri diferă”."
    ),
    # 11235
    (
        "Între subiecți: grupuri independente de participanți. Măsurători repetate: "
        "aceiași oameni în toate condițiile — model și presupuneri diferite. Alegerea "
        "depinde de design. Măsurătorile repetate țin cont de corelația intra-subiecți, "
        "nu o ignoră."
    ),
    # 11236
    (
        "df între = k−1 (k grupuri); df eroare = N−k. Totalul df pentru SS nu e N+k "
        "și df între nu e N−1 — confuzii frecvente cu formula t pe eșantion."
    ),
    # 11237
    (
        "η² ≈ SS₍între₎/SS₍total₎ — proporția varianței VD asociată factorului. E "
        "mărime a efectului, nu probabilitatea lui H₀ și nu diferența brută între "
        "extreme."
    ),
    # 11238
    (
        "ANOVA parametrică: VD cantitativă (interval/raport), ≥3 grupuri, presupunerile "
        "rezonabile. VD nominală cu 2 categorii → alte teste (χ² etc.), nu ANOVA pe "
        "medii în sensul clasic."
    ),
    # 11239
    (
        "Between-subjects: fiecare participant într-un singur grup; grupuri independente. "
        "Within-subjects/repetate e opusul — aceiași participanți în toate condițiile. "
        "Variația în grupuri există mereu."
    ),
    # 11240
    (
        "Pentru două grupuri independente, ANOVA unifactorială și testul t sunt "
        "legate: F = t². Nu F = t/2 sau √t — relația e prin pătrat."
    ),
    # 11241
    (
        "Patru idei: test omnibus; ipoteze H₀/H₁; interpretarea F; η² pentru efect. "
        "Post-hoc rămâne necesar după F semnificativ — nu e înlocuit de η²."
    ),
    # 11242
    (
        "ANOVA nu localizează perechile; semnificarea ≠ efect clinic mare; η² ajută la "
        "evaluarea mărimii efectului. F nonsignificativ nu demonstrează egalitatea "
        "mediilor — doar lipsă de dovezi suficiente la puterea și α alese."
    ),
    # 11243
    (
        "VI = tip terapie cu 3 niveluri (A, B, C); VD = anxietate (cantitativă). "
        "ANOVA nu impune 2 niveluri; VD cantitativă nu anulează nivelurile VI."
    ),
    # 11244
    (
        "p = 0,003 < 0,05 → respingi H₀, semnificativ. Nu poți concluziona că fiecare "
        "grup diferă de toate — doar că nu sunt toate egale; post-hoc clarifică perechile."
    ),
    # 11245
    (
        "Sinteză finală: scop (3+ medii), descompunere SS și F, presupuneri, post-hoc "
        "după semnificare. Nicio variantă nu susține că F alege automat „cea mai bună” "
        "intervenție clinic."
    ),
]

assert len(ANOVA_EXPLANATIONS) == 20
