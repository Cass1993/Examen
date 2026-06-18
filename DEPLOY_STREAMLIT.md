# Deploy pe telefon — Streamlit Community Cloud

Quiz-ul rulează în browser (și pe telefon) la un link de tip  
`https://nume-app.streamlit.app` — fără să ții PC-ul pornit.

## Ce trebuie în GitHub

| Include în repo | De ce |
|-----------------|--------|
| `app.py` | aplicația |
| `requirements.txt` | dependențe |
| `.streamlit/config.toml` | setări UI |
| `scripts/` | loturi examen + sincronizare |
| `data/questions.json` | **toate întrebările** (generat local) |

| **Nu** urca (sunt în `.gitignore`) | De ce |
|-------------------------------------|--------|
| `.venv/` | prea mare, se instalează pe Cloud |
| `1400 x3/`, `2000 itemi raw/` | surse locale; pe Cloud folosim `questions.json` |
| `data/scores_history.json` | istoric local |

## Pas 1 — Pregătește `questions.json` (o dată, pe PC)

```powershell
cd C:\Users\casia\psihologie-quiz
.\.venv\Scripts\python.exe scripts\prepare_streamlit_deploy.py
```

Verifică că există `data\questions.json` (câțiva MB, mii de întrebări).

## Pas 2 — Repository GitHub

Repo-ul tău: **[github.com/Cass1993/Examen](https://github.com/Cass1993/Examen)** (public).

Dacă nu ai git configurat pe PC: [github.com](https://github.com) → login → Settings → Developer settings → Personal access token (pentru push).

## Pas 3 — Push cod pe GitHub

**Variantă rapidă (dublu-click):** `Push pe GitHub Examen.bat`

Sau manual în PowerShell:

```powershell
cd C:\Users\casia\psihologie-quiz
.\.venv\Scripts\python.exe scripts\prepare_streamlit_deploy.py
git init
git remote add origin https://github.com/Cass1993/Examen.git
git add app.py requirements.txt .gitignore .streamlit DEPLOY_STREAMLIT.md README.md scripts data/questions.json
git status
git commit -m "Streamlit Cloud: quiz complet cu data/questions.json"
git branch -M main
git pull origin main --allow-unrelated-histories --no-edit
git push -u origin main
```

La primul push, GitHub poate cere login (browser sau token).

Dacă `git pull` dă conflicte la `app.py` sau `README.md`, păstrează versiunea locală (cea din `psihologie-quiz`), apoi `git add` și `git commit` înainte de push.

**Dacă `data/questions.json` e foarte mare (>50 MB):** push-ul poate dura; sub 100 MB e OK pe GitHub.

## Pas 4 — Streamlit Community Cloud

1. [share.streamlit.io](https://share.streamlit.io) → **Sign in with GitHub**.
2. **Create app**.
3. **Repository:** `Cass1993/Examen`
4. **Branch:** `main`
5. **Main file path:** `app.py`
6. **Deploy**.

Prima pornire durează 2–5 minute (instalare pachete + încărcare bancă).

## Pas 5 — Pe telefon

1. Deschide linkul `https://....streamlit.app` în **Chrome** sau **Safari**.
2. (Opțional) **Adaugă pe ecranul principal** — se comportă ca o iconiță de app.
3. Salvează linkul la favorite.

## Actualizări ulterioare

După ce modifici itemi în cod:

```powershell
.\.venv\Scripts\python.exe scripts\prepare_streamlit_deploy.py
git add data/questions.json scripts app.py
git commit -m "Actualizare itemi"
git push
```

Streamlit Cloud **redeployează automat** în ~1–2 minute.

## Limitări

- **Istoric scoruri** pe Cloud se poate reseta la redeploy (nu e bază de date permanentă).
- **Prima încărcare** poate fi lentă (mii de întrebări).
- UI-ul e făcut pentru desktop; pe telefon e utilizabil, dar mai înghesuit.

## Depanare

| Problemă | Soluție |
|----------|---------|
| `ModuleNotFoundError: scripts` | Rulează `Push pe GitHub Examen.bat` — trebuie `scripts/` + `data/questions.json` în repo |
| Lot nou lipsește | Rulează `prepare_streamlit_deploy.py`, commit + push |
| `FileNotFoundError` questions | Nu ai inclus `data/questions.json` în repo |
