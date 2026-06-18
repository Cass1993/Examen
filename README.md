# Simulare Examen Licență Psihologie (Streamlit)

Aplicație web locală pentru test grilă la psihologie: cronometru, amestecare întrebări, mod examen / verificare, review greșeli și istoric scoruri.

## Structura proiectului

| Fișier | Rol |
|--------|-----|
| `app.py` | Aplicația Streamlit (UI + logică) |
| `scripts/bank_parser.py` | Importă banca din JSON / MD / TXT |
| `data/questions.json` | Întrebări generate automat la pornire |
| `data/scores_history.json` | Istoric scoruri |
| `requirements.txt` | Dependențe Python |

Banca activă (implicit): **3400 itemi** = 1400 (`1400 x3/`) + 2000 (`2000 itemi raw/`), validate și combinate în `questions_3400_merged.json`.

## Instalare (Windows)

```powershell
cd C:\Users\casia\psihologie-quiz
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Dacă activarea venv e blocată de PowerShell, rulează direct cu Python din venv (fără activate):

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless true --browser.gatherUsageStats false
```

## Rulare

```powershell
cd C:\Users\casia\psihologie-quiz
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Deschide `http://localhost:8501` în browser.

## Cum o folosești

În sidebar:

- **Alege loturile** — filtrează pe domeniu (Statistică, Psihoterapie, etc.)
- **Mod**
  - *Examen* — fără feedback până la final
  - *Verificare* — feedback imediat după fiecare răspuns
- **Amestecă întrebările** — shuffle la start
- **Număr întrebări** — 0 = toate
- **Limită timp** — cronometru cu auto-submit
- **Start / Restart**

### Mod Verificare

După „Confirmă răspunsul” vezi: Corect/Greșit, răspunsul tău vs. corect, variantele marcate ✓/✗.

### La final

- Scor total și procent
- Secțiune **Răspunsuri corecte**
- Secțiune **Răspunsuri greșite** — compară ce ai ales vs. corect
- **Istoric scoruri**

## Formate bancă acceptate

- **JSON** (recomandat): `intrebare`, `variante`, `raspuns_corect`, `domeniu`, `tip`
- **Markdown** cu loturi și barem: `# Lotul 1` + `## Barem — Lotul 1`
- **TXT** (`Itemi.txt`): enunț + variante a/b/c/d

La prima pornire (sau când banca sursă e mai nouă), aplicația generează automat `data/questions.json`.

Pentru regenerare manuală (validare + merge + `data/questions.json`):

```powershell
.\.venv\Scripts\python.exe scripts\generate_bank.py
```

Rapoarte generate:
- `2000 itemi raw/raport_validare_merge_3400.txt` — merge + avertismente
- `2000 itemi raw/raport_cercetare_metodologica_2000.txt` — analiză metodologică banca 2000

Exemplu format: vezi `data/questions_demo.json`.

## Pe telefon (Streamlit Cloud)

Ghid complet: **[DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md)** — publicare gratuită pe `*.streamlit.app`, link deschis în browser pe telefon.

Pe scurt:

```powershell
.\.venv\Scripts\python.exe scripts\prepare_streamlit_deploy.py
# apoi push pe GitHub + Create app pe https://share.streamlit.io
```

## Schimbarea băncii

Pune noul fișier în proiect și actualizează calea în sidebar (sau modifică `BANK_MD_DEFAULT` în `app.py`), apoi apasă **Start / Restart**.
