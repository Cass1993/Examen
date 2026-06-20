"""Explicații didactice — Statistică II segment 10: ipoteze și testul z (ID 11176–11185)."""

from __future__ import annotations

from typing import List

HYPOTHESIS_Z_TEST_EXPLANATIONS: List[str] = [
    # 11176
    (
        "Adevărat. H₀ este ipoteza „nulă”: presupunerea de lucru că nu există efect sau "
        "diferență în populație — de exemplu μ₁ = μ₂ sau μ egal cu o valoare de "
        "referință. Testul statistic caută dovezi împotriva lui H₀; dacă nu apar "
        "suficient de puternice, nu o respingi."
    ),
    # 11177
    (
        "H₁ (ipoteza de cercetare) este cea pe care o susții dacă datele o "
        "confirmă: există diferență, efect sau direcție (ex. μșah > μpop). H₀ spune "
        "inversul — lipsa diferenței. α e pragul de decizie, nu o ipoteză; sm e "
        "eroarea standard a mediei, nu H₁."
    ),
    # 11178
    (
        "La șahiști: H₀ — IQ mediu al șahiștilor = IQ mediu populație (fără avantaj); "
        "H₁ — μșah > μpop (șahiștii au medie mai mare). H₁ = μșah = μpop ar anula "
        "ipoteza de cercetare; H₀ > μpop ar presupune deja efectul pe care vrei să-l "
        "testezi — rolurile sunt inversate."
    ),
    # 11179
    (
        "Eroarea standard a mediei măsoară cât de mult „oscilează” mediile "
        "eșantioanelor în jurul lui μ: sm = σ/√N. Cu N mai mare, sm scade. z = "
        "(m−μ)/sm vine după sm; σ×√N sau sm = (m−μ)/z inversează formula."
    ),
    # 11180
    (
        "zcalculat spune cu câte erori standard (sm) se abate media eșantionului m "
        "de la valoarea din H₀ (μ). Formula corectă: (m−μ)/sm. (μ−m)/σ amestecă "
        "semnul și folosește σ în loc de sm; celelalte variante nu sunt transformări "
        "standard valide."
    ),
    # 11181
    (
        "Două căi echivalente de decizie: compară zcalculat cu zcritic (unilateral "
        "sau bilateral, după H₁) sau compară p cu α. p ≤ α → respingi H₀. Că m ≠ μ "
        "în eșantion e normal — fără test nu știi dacă diferența depășește variabilitatea "
        "așteptată din eșantionare. La p > α nu respingi H₀ — varianta care sugerează "
        "respingerea „pentru a limita riscul” inversează regula."
    ),
    # 11182
    (
        "Unilateral dreapta, α = 0,05: zcritic ≈ 1,65. zcalculat = 2,18 > 1,65 → "
        "rezultat în zona de respingere → respingi H₀, semnificativ statistic. „m "
        "aproape de μ” sau „N prea mic” nu înlocuiesc regula — ai deja z și pragul "
        "stabilit."
    ),
    # 11183
    (
        "Pașii din exemplu: sm = 15/√30 ≈ 2,74; z = (106−100)/2,74 ≈ 2,18; pentru "
        "acest z, p ≈ 0,014 < 0,05 → respingi H₀. Varianta cu sm = 15×√30 și z = 0,5 "
        "folosește greșit formula sm și duce la o concluzie opusă — de aceea e "
        "capcană plauzibilă dacă confunzi σ/√N cu σ×√N."
    ),
    # 11184
    (
        "p > α sau z sub prag → nu respingi H₀: datele nu oferă suficientă dovadă "
        "contra ipotezei nule la nivelul ales (nonsignificativ). Nu „demonstrăm” că H₀ "
        "e adevărată cu certitudine și nici că μ = m în populație — doar că efectul "
        "nu depășește pragul la α."
    ),
    # 11185
    (
        "Patru idei de sinteză: rolul H₀/H₁; sm și z; prag unilateral 1,65 și p ≤ α; "
        "când nu respingi H₀. Toate sunt nucleul testului z pe un eșantion din curs — "
        "fără a confunda observația (m ≠ μ) cu decizia formală."
    ),
]

assert len(HYPOTHESIS_Z_TEST_EXPLANATIONS) == 10
