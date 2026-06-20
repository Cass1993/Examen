"""Explicații didactice — Statistică II segment 9: distribuție eșantionare și TLC (ID 11161–11175)."""

from __future__ import annotations

from typing import List

SAMPLING_DISTRIBUTION_EXPLANATIONS: List[str] = [
    # 11161
    (
        "Adevărat. Indiferent cum variază mediile eșantioanelor individuale, centrul "
        "distribuției lor teoretice rămâne μ — de aceea media eșantionului estimează "
        "corect media populației în medie."
    ),
    # 11162
    (
        "Nu e distribuția unui singur eșantion, ci a tuturor mediilor posibile la "
        "mărime N. E fundamentul inferenței despre μ. Nu e histogramă nominală."
    ),
    # 11163
    (
        "μm = μ și variabilitatea mediilor eșantioanelor e mai mică decât σ² "
        "populației (pentru medii). Un singur eșantion poate avea m ≠ μ — asta e "
        "normal, nu contrazice TLC."
    ),
    # 11164
    (
        "sm = σ/√N — eroarea standard a mediei, nu σ întreg. √N la numitor: N mai mare, "
        "sm mai mic. Nu σ×√N și nu σ/N."
    ),
    # 11165
    (
        "TLC descrie comportamentul mediilor eșantioanelor la N mare — nu al unui scor "
        "individual, nu al modului sau al sm per observație. De aceea z pentru medie "
        "folosește sm, nu σ pe un singur X."
    ),
    # 11166
    (
        "În practică σ e necunoscut → folosești s din eșantion: sm = s/√N. s²/(N−1) e "
        "varianța eșantionului, nu eroarea standard a mediei."
    ),
    # 11167
    (
        "sm scade cu √N — dublarea preciziei cere de ~4 ori mai mulți participanți. sm "
        "mic = interval de încredere mai îngust. σ nu dispare la N mare."
    ),
    # 11168
    (
        "Aleator, independent, N constant în plan — condiții pentru TLC și inferență. "
        "Normalitatea populației nu e obligatorie la N mare — tocmai asta e puterea TLC."
    ),
    # 11169
    (
        "z pentru medie: (m−μ)/sm — câte erori standard e media eșantionului de la μ. "
        "Nu folosești σ în loc de sm și nu un singur X."
    ),
    # 11170
    (
        "Două idei TLC: media mediilor → μ; forma distribuției mediilor → normal la N "
        "mare. Un eșantion nu are m=μ exact; populația nu trebuie normală la N mare."
    ),
    # 11171
    (
        "N ≥ 30 e regulă practică pentru „eșantion mare” și aplicarea aproximării "
        "normale a mediilor — nu teoremă rigidă, dar orientare din curs."
    ),
    # 11172
    (
        "TLC ține de distribuția mediilor, nu a valorilor individuale. Populația poate "
        "fi skewed; normalitatea apare la nivelul mediilor. Nu „niciodată” fără populație "
        "normală."
    ),
    # 11173
    (
        "N mare → sm mic → estimare mai precisă. σ rămâne același; μ nu se schimbă cu "
        "N — se estimează mai bine."
    ),
    # 11174
    (
        "Patru piloni: distribuția mediilor; sm și N; TLC + condiții; z pentru medie. "
        "Leagă descriptivul de inferența despre μ."
    ),
    # 11175
    (
        "Trei capcane: σ vs sm; TLC pe X individual; un eșantion ≠ μ. σ nu scade cu N — "
        "scade sm. Verifică mereu dacă lucrezi cu medii sau cu scoruri individuale."
    ),
]

assert len(SAMPLING_DISTRIBUTION_EXPLANATIONS) == 15
