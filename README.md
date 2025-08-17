# Team Task Scheduler

Een Python-tool om eerlijk en overzichtelijk **teamtaken** te verdelen voor sportteams, met export naar Excel.  
Speciaal gemaakt voor het HMHC Saxenburg Heren 1 hockeyteam, maar bruikbaar voor elk team dat werkt met uit/thuis-wedstrijden en vaste taken.

## ✨ Features

- Ondersteunt **altijd**, **uit** en **thuis** gebonden taken.
- Houdt rekening met:
  - Geen dubbele taken per week.
  - Vermijden van opeenvolgende indelingen waar mogelijk.
  - Eerlijke verdeling van **taken** en **kilometers**.
- Kleuren per speler in het schema voor snelle herkenning.
- Automatische statistiek-tabblad in Excel.
- Configuratie via CSV-bestanden:
  - `taken.csv` → takenlijst, scope, aantal personen.
  - `wedstrijden.csv` → wedstrijdschema.
  - `spelers.csv` → spelersnamen en weergavenamen.
  - `afstanden.csv` → enkele reis kilometers naar clubs.

## 📂 Projectstructuur

```txt
.../Team-Task-Scheduler$
├── .gitignore
├── pyproject.toml
├── README.md
├── task_planner
│   ├── config.py
│   ├── data_loader.py
│   ├── exporter.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── models.py
│   ├── scheduler.py
│   └── utils.py
└── templates
    ├── afstanden.csv
    ├── spelers.csv
    ├── taken.csv
    └── wedstrijden.csv
```

## 🚀 Installatie

We gebruiken **Conda** + **pipx** + **Poetry** voor een schone omgeving.

```bash
# 1. Maak en activeer Conda omgeving
conda create -n team-tasks python=3.13
conda activate team-tasks

# 2. Installeer pipx en poetry
conda install conda-forge::pipx
pipx install poetry

# 3. Installeer dependencies via poetry
poetry install
```

## 📊 Gebruik

Vul eerst de CSV-bestanden in `templates/` met jouw teamdata.

```bash
poetry run task_planner \
  --taken templates/taken.csv \
  --wedstrijden templates/wedstrijden.csv \
  --spelers templates/spelers.csv \
  --afstanden templates/afstanden.csv \
  --uitvoer templates/schema.xlsx
```

Het resultaat is een **Excelbestand** met:

- Een schema-tabblad met alle wedstrijden en toegewezen taken.
- Een statistiek-tabblad met tellingen en kilometerverdeling.

## 📜 Licentie

Dit project valt onder de MIT-licentie. Zie het bestand [LICENSE](LICENSE) voor details.

## 🛠 Development

Format, lint en type-check uitvoeren:

```bash
poetry run black .
poetry run ruff check .
poetry run mypy .
```

## 📌 TODO

- [ ] Unit tests toevoegen.
- [ ] Mogelijkheid om afstandsdata via API op te halen.
- [ ] PDF-export naast Excel.
