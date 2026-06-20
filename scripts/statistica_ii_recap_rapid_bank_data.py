"""Itemi — Statistică II, segment 11: recapitulare rapidă (40 itemi, ID 11186–11225)."""

from __future__ import annotations

from typing import Any, Dict, List

Item = Dict[str, Any]

RECAP_RAPID_ITEMS: List[Item] = [
    {
        "stem": (
            "Eroarea aleatorie, în medie pe repetări, nu deplasează media reală a "
            "grupului — produce fluctuații în jurul valorii adevărate."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "Variabila „gen codificat M/F” este, de regulă, măsurată pe scară:"
        ),
        "options": [
            "nominală",
            "ordinală",
            "de interval",
            "de raport",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Pentru gen (M/F) și pentru timpul de reacție (secunde cu zero absolut), "
            "care asocieri scară–tip de test sunt uzual corecte?"
        ),
        "options": [
            "gen → nominală → teste neparametrice frecvente",
            "timp de reacție → de raport → teste parametrice posibile",
            "gen → de raport pentru că are două categorii",
            "timp de reacție → nominală pentru că se numără trialuri",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Timpul de reacție (ex. 0,32 s vs 0,64 s) se încadrează, de obicei, pe scară:"
        ),
        "options": [
            "de raport (zero absolut, raporturi interpretabile)",
            "nominală (categorii fără ordine)",
            "ordinală (note calitative)",
            "nominală binară indiferent de unitate",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Nota școlară (1–10) este discutată în curs, de regulă, ca exemplu de scară:"
        ),
        "options": [
            "ordinală",
            "de raport cu zero absolut",
            "nominală pură",
            "de interval cu raporturi exacte între note",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "„Număr de răspunsuri corecte” la un test este, de obicei, o variabilă:"
        ),
        "options": [
            "discretă, pe scară de raport sau numărătoare",
            "nominală, pentru că e un scor",
            "ordinală fără sens de magnitudine",
            "latentă, nevăzută direct",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un studiu corelațional demonstrează direct cauza dintre două variabile "
            "măsurate, fără alte condiții de design."
        ),
        "tf": True,
        "correct_tf": False,
    },
    {
        "stem": (
            "Care dintre următoarele diferențe între eroarea aleatorie și cea "
            "sistematică sunt corecte?"
        ),
        "options": [
            "aleatorie: fluctuații în jurul mediei, fără bias constant",
            "sistematică: deplasează media estimată (bias)",
            "sistematică: dispare automat la N mare, fără corecție",
            "aleatorie: schimbă mereu media grupului într-o direcție fixă",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Pentru un set de date, suma abaterilor față de medie Σ(Xᵢ − m) este:"
        ),
        "options": [
            "0",
            "N − 1",
            "1",
            "egala cu dispersia s²",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Dacă adaugi +5 la toate valorile unui set de date, ce se întâmplă cu "
            "indicatorii de tendință centrală și dispersie?"
        ),
        "options": [
            "media crește cu 5",
            "abaterea standard s rămâne neschimbată",
            "mediana crește cu 5",
            "coeficientul de variație cv crește obligatoriu cu 5 puncte",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă înmulțești toate valorile cu 2, care transformări sunt corecte?"
        ),
        "options": [
            "media se înmulțește cu 2",
            "abaterea standard s se înmulțește cu 2",
            "media rămâne aceeași, doar unitatea se schimbă",
            "dispersia s² rămâne identică",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La calculul dispersiei eșantionului s², împărțitorul uzual este:"
        ),
        "options": [
            "N − 1",
            "N",
            "N + 1",
            "N − 2",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Un coeficient de variație cv ≈ 25% indică, în interpretarea din curs, o "
            "dispersie:"
        ),
        "options": [
            "medie (moderată)",
            "foarte mică (sub 15%)",
            "foarte mare (peste 30%)",
            "nulă, echivalentă cu s = 0",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Într-o distribuție simetrică, modul, mediana și media verifică relația "
            "Mo = Me = M."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În asimetrie pozitivă (înclinată spre dreapta), ordinea uzuală a celor "
            "trei indicatori este:"
        ),
        "options": [
            "Mo < Me < M",
            "M < Me < Mo",
            "Me < Mo < M",
            "Mo = Me = M",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "După transformarea în scoruri z, care proprietăți sunt corecte?"
        ),
        "options": [
            "media distribuției z este 0",
            "abaterea standard a lui z este 1",
            "forma relativă a distribuției se păstrează",
            "media devine 1, iar abaterea standard devine 0",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "În distribuția normală, aproximativ 68% din cazuri se află între:"
        ),
        "options": [
            "±1σ față de medie",
            "±2σ față de medie",
            "±3σ față de medie",
            "mediana și modul exclusiv",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "În distribuția de eșantionare a mediilor, care afirmații sunt corecte?"
        ),
        "options": [
            "centrul teoretic μₘ este egal cu μ",
            "un singur eșantion poate avea m ≠ μ fără a contrazice TLC",
            "μₘ este mereu egal cu m din ultimul eșantion observat",
            "μₘ = σ / √N",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Când mărimea eșantionului N crește (σ populație constantă), eroarea "
            "standard a mediei sm:"
        ),
        "options": [
            "scade (sm = σ / √N)",
            "crește proporțional cu N",
            "rămâne egală cu σ",
            "devine σ × √N",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Regula practică din curs pentru „eșantion mare” în contextul TLC este, "
            "de obicei, N ≥ 30."
        ),
        "tf": True,
        "correct_tf": True,
    },
    {
        "stem": (
            "În care situații respingi H₀ la un test z (conform regulilor din curs)?"
        ),
        "options": [
            "când p ≤ α",
            "când zcalculat atinge sau depășește zcritic (în testul unilateral potrivit)",
            "când m = μ exact în eșantion",
            "când α = 0,05 indiferent de p",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "La α = 0,05 pentru un test unilateral, valoarea critică uzuală din tabel "
            "este zcritic ="
        ),
        "options": [
            "1,65",
            "1,96",
            "2,58",
            "0,05",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care distincții între histogramă și diagramă cu bare sunt corecte?"
        ),
        "options": [
            "histograma: variabile continue (intervale pe axă)",
            "diagrama cu bare: categorii discrete separate",
            "histograma: categorii nominale fără ordine pe axă",
            "diagrama cu bare: intervale contigue fără spații",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care indicatori sunt, de regulă, mai robusti la valori extreme "
            "(outliers)?"
        ),
        "options": [
            "mediana",
            "intervalul interquartilic (RQ = Q₃ − Q₁)",
            "media aritmetică neponderată",
            "suma pătratelor abaterilor",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Indicatorul statistic permis în mod fundamental pe scară nominală este:"
        ),
        "options": [
            "modul (frecvența maximă)",
            "media aritmetică",
            "mediana",
            "abaterea standard",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care formule pentru medie sunt corecte?"
        ),
        "options": [
            "m = ΣX / N",
            "m = Σ(X·f) / Σf (date grupate)",
            "m = Σ(Xᵢ − m) / N",
            "m = √s²",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care formule și convenții pentru dispersie sunt corecte?"
        ),
        "options": [
            "s² = Σ(Xᵢ − m)² / (N − 1)",
            "s = √s²",
            "s² = Σ(Xᵢ − m)² / N pentru eșantionul standard din curs",
            "s = Σ(Xᵢ − m) / (N − 1)",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Despre coeficientul de variație (cv), care afirmații sunt corecte?"
        ),
        "options": [
            "cv = (s / m) × 100",
            "cv < 15% sugerează dispersie mică",
            "cv > 30% sugerează dispersie mare",
            "cv = s + m, indiferent de unitate",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Formula scorului z standardizat este:"
        ),
        "options": [
            "z = (X − m) / s",
            "z = (m − X) / s",
            "z = X / m + s",
            "z = (X − μ) / sm",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care relații între scor z, transformare inversă și test pe eșantion sunt "
            "corecte?"
        ),
        "options": [
            "X = m + z·s (revenire la scor brut)",
            "sm = σ / √N",
            "z eșantion = (m − μ) / sm",
            "z eșantion = (X − m) / s pentru fiecare participant",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care formule pentru amplitudine și interval interquartilic sunt corecte?"
        ),
        "options": [
            "R = Xₘₐₓ − Xₘᵢₙ",
            "RQ = Q₃ − Q₁",
            "R = Q₃ + Q₁",
            "RQ = Xₘₐₓ − Xₘᵢₙ",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Care dintre următoarele sinteze despre scale și tipuri de teste sunt "
            "corecte?"
        ),
        "options": [
            "nominală < ordinală < interval < raport (ierarhie Stevens)",
            "gen → nominală; timp reacție → raport",
            "note școlare → uzual ordinal",
            "alegerea testului parametric/neparametric ține cont de scară și distribuție",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care distincții între variabile independente, dependente, observate și "
            "latente sunt corecte?"
        ),
        "options": [
            "VI: manipulată sau folosită pentru predicție; VD: rezultat măsurat",
            "observate: măsurate direct; latente: constructe inferate (ex. anxietate)",
            "latenta = mereu sinonimă cu variabila dependentă",
            "o variabilă observată nu poate fi măsurată niciodată direct în teste",
        ],
        "correct": "ab",
    },
    {
        "stem": (
            "Când este preferabil modul, mediana sau media?"
        ),
        "options": [
            "modul: date nominale",
            "mediana: asimetrie sau outliers",
            "media: date simetrice, interval/raport, fără extreme puternice",
            "media: obligatoriu pe orice scară nominală",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Dacă p ≤ α (ex. p = 0,03 la α = 0,05), decizia uzuală este:"
        ),
        "options": [
            "respingi H₀ — rezultat semnificativ statistic",
            "accepți H₁ ca demonstrație certă în populație",
            "respingi H₀ indiferent de zcalculat, chiar dacă p > α",
            "demonstrezi automat un efect clinic mare",
        ],
        "correct": "a",
    },
    {
        "stem": (
            "Care proprietăți la transformări liniare sunt corecte?"
        ),
        "options": [
            "adaugi +k → media crește cu k, s rămâne neschimbată",
            "înmulțești cu k → media și s se înmulțesc cu |k|",
            "adaugi +k → mediana crește cu k",
            "înmulțești cu k → dispersia s² se înmulțește cu k²",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care idei despre sm, TLC și testul z pe eșantion sunt corecte?"
        ),
        "options": [
            "sm = σ / √N; N mare → sm mic",
            "μₘ = μ (centrul distribuției mediilor)",
            "TLC: la N mare, distribuția mediilor → aproximativ normală",
            "TLC garantează m = μ în orice eșantion mic",
        ],
        "correct": "abc",
    },
    {
        "stem": (
            "Care perechi despre H₀, H₁ și decizia statistică sunt corecte?"
        ),
        "options": [
            "H₀: fără diferență/efect; H₁: există diferență sau efect",
            "respingi H₀ când p ≤ α sau zcalculat ≥ zcritic (unilateral dreapta)",
            "p > α înseamnă că H₀ e demonstrată cu certitudine în populație",
            "α = 0,05 unilateral → zcritic ≈ 1,65",
        ],
        "correct": "abd",
    },
    {
        "stem": (
            "Care dintre următoarele formule „de reținut” sunt corecte?"
        ),
        "options": [
            "m = ΣX/N; s² = Σ(Xᵢ−m)²/(N−1); s = √s²",
            "cv = (s/m)×100; z = (X−m)/s; X = m + z·s",
            "sm = σ/√N; z = (m−μ)/sm; R = Xₘₐₓ−Xₘᵢₙ; RQ = Q₃−Q₁",
            "Σ(Xᵢ−m) = 0; medie grupată m = Σ(X·f)/Σf",
        ],
        "correct": "abcd",
    },
    {
        "stem": (
            "Care teme din „ultima zi” de recapitulare Statistică II sunt formulate "
            "corect?"
        ),
        "options": [
            "cele 4 scale + parametric vs neparametric",
            "erori aleatorii vs sistematice; mod/medie/mediana",
            "asimetrie pozitivă Mo < Me < M; proprietăți ± și × la medie și s",
            "sm, TLC, H₀/H₁ și testul z pe eșantion",
        ],
        "correct": "abcd",
    },
]

assert len(RECAP_RAPID_ITEMS) == 40
