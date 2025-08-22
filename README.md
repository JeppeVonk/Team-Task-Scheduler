# 🏑 Team Task Scheduler

Een handige tool om **teamtaken eerlijk en overzichtelijk te verdelen** voor sportteams.  
De uitkomsten worden automatisch in **Excel** gezet: een schema + statistieken.

➡️ Oorspronkelijk gemaakt voor **HMHC Saxenburg Heren 1**, maar bruikbaar voor elk team met thuis- en uitwedstrijden en vaste taken.

---

## 📚 Inhoudsopgave

1. [✅ Wat kan dit programma?](#-wat-kan-dit-programma)
2. [📂 Mappen & Bestanden](#-mappen--bestanden)
3. [⚙️ Installatie (eenmalig instellen)](#️-installatie-eenmalig-instellen)
4. [🏃 Gebruik (het schema maken)](#-gebruik-het-schema-maken)
5. [📝 Hoe vul je de bestanden in?](#-hoe-vul-je-de-bestanden-in)
   - [taken.csv – Takenlijst](#takencsv--takenlijst)
   - [spelers.csv – Spelers en voorkeuren](#spelerscsv--spelers-en-voorkeuren)
   - [wedstrijden.csv – Wedstrijdschema](#wedstrijdencsv--wedstrijdschema)
   - [afstanden.csv – Afstanden naar clubs](#afstandencsv--afstanden-naar-clubs)
6. [📊 Voorbeeld resultaat](#-voorbeeld-resultaat)
7. [👩‍💻 Voor ontwikkelaars (optioneel)](#-voor-ontwikkelaars-optioneel)
8. [📜 Licentie](#-licentie)
9. [🤝 Bijdragen](#-bijdragen)
10. [📌 Toekomstige uitbreidingen](#-toekomstige-uitbreidingen)

---

## ✅ Wat kan dit programma?

- Taken kunnen gekoppeld worden aan:
  - **Altijd** (bij elke wedstrijd)
  - **Uitwedstrijden**
  - **Thuiswedstrijden**
- Houdt rekening met:
  - Geen dubbele taken voor 1 persoon in dezelfde week
  - Zo min mogelijk opeenvolgende taken
  - Eerlijke verdeling van **taken** én **kilometers rijden**
- Kleurtjes per speler voor snel overzicht
- Extra **statistiek-tabblad** in Excel (per speler en per taak)
- Werkt met eenvoudige **CSV-bestanden** (Excel-bestanden die je opslaat als `CSV`):
  - `taken.csv` → lijst met taken
  - `wedstrijden.csv` → wedstrijdschema
  - `spelers.csv` → spelersnamen en voorkeuren
  - `afstanden.csv` → afstanden naar clubs

---

## 📂 Mappen & Bestanden

Wanneer je het project downloadt, ziet de structuur er zo uit:

```txt
Team-Task-Scheduler/
├── README.md
├── task_planner/        ← de code
├── templates/           ← voorbeeldbestanden (csv)
└── tests/               ← automatische controles (niet nodig voor gebruik)
```

De map **`templates/`** bevat voorbeelden die je kunt kopiëren en invullen met je eigen teaminformatie.

---

## ⚙️ Installatie (eenmalig instellen)

Voor het gebruik heb je **Python** nodig.  
Wij raden **Conda** aan, omdat dat het eenvoudigst is en overal werkt.

1. **Installeer Conda**

   - Download: [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda)  
   - Volg de installatiehandleiding voor jouw computer.

2. **Haal het project binnen**

   - Als je het project als `.zip` hebt gedownload:
     - Pak het bestand uit (rechtermuisknop → "Alles uitpakken").
     - Je krijgt een map zoals `Team-Task-Scheduler/`.

   - Als je **Git** hebt geïnstalleerd:

     ```bash
     git clone https://github.com/jouw-gebruikersnaam/Team-Task-Scheduler.git
     ```

     Ook dan krijg je een map `Team-Task-Scheduler/`.

   👉 Onthoud waar deze map staat, want je moet er in de volgende stappen naartoe gaan.

3. **Maak een nieuwe omgeving voor dit project**  
   Open een terminal/Anaconda Prompt en voer uit:

   ```bash
   conda create -n team-tasks python=3.13
   ```

   ```bash
   conda activate team-tasks
   ```

4. **Installeer de benodigde hulpmiddelen**

   ```bash
   conda install conda-forge::pipx
   ```

   ```bash
   pipx install poetry
   ```

   <!-- TODO: Figure out why poetry is not always added to the PATH, thus causing a fail during `poetry install` -->

5. **Installeer het project zelf**  
   Ga in de terminal eerst naar de projectmap:

   ```bash
   cd pad/naar/Team-Task-Scheduler
   ```

   🔎 **Tip:** twijfel je of je in de juiste map zit?  
   Typ in de terminal:

   - macOS/Linux:

     ```bash
     ls
     ```

   - Windows:

     ```bash
     dir
     ```

   Je zou o.a. `README.md`, `task_planner/` en `templates/` moeten zien, net als in het voorbeeld hierboven.

   Voer daarna uit:

   ```bash
   poetry install
   ```

👉 Klaar! Je hoeft dit maar één keer te doen. Daarna kun je steeds direct naar **Gebruik** springen.

---

## 🏃 Gebruik (het schema maken)

1. Kopieer de map **`templates/`** naar een eigen werkmap, bijvoorbeeld:

   ```txt
   mijn-team/
   ├── taken.csv
   ├── spelers.csv
   ├── wedstrijden.csv
   └── afstanden.csv
   ```

2. Vul de bestanden in met jullie teaminformatie (zie hieronder voor uitleg).

3. **Ga naar je werkmap en activeer Conda**  
   - Open **Anaconda Prompt** (Windows) of een terminal (Mac/Linux).
   - Navigeer naar de map waar je de bestanden hebt gezet, bijvoorbeeld:

     ```bash
     cd pad/naar/mijn-team/
     ```

   - Controleer of je in de juiste map zit:

     ```bash
     ls   # macOS/Linux
     dir  # Windows
     ```

     Je zou hier de bestanden `taken.csv`, `spelers.csv`, `wedstrijden.csv`, `afstanden.csv` moeten zien.

   - Activeer de Conda-omgeving:

     ```bash
     conda activate team-tasks
     ```

4. **Draai het programma**  

   ```bash
   poetry run task_planner \
     --taken taken.csv \
     --wedstrijden wedstrijden.csv \
     --spelers spelers.csv \
     --afstanden afstanden.csv \
     --uitvoer schema.xlsx
   ```

5. Open **`schema.xlsx`** in Excel → daarin staan:
   - **Schema-tabblad** → alle wedstrijden en wie welke taak doet
   - **Statistiek-tabblad** → overzicht per speler en kilometerverdeling

---

## 📝 Hoe vul je de bestanden in?

### `taken.csv` – Takenlijst

| taak       | scope  | aantal |
| ---------- | ------ | ------ |
| Materialen | altijd | 2      |
| Hesjes     | altijd | 1      |
| Rijden     | uit    | 4      |
| Fluiten    | thuis  | 2      |
| Bar        | thuis  | 2      |

- **scope** = `altijd`, `uit`, `thuis`
- **aantal** = hoeveel personen tegelijk nodig zijn

---

### `spelers.csv` – Spelers en voorkeuren

| naam           | displaynaam | Materialen | Hesjes | Rijden | Fluiten | Bar |
| -------------- | ----------- | ---------- | ------ | ------ | ------- | --- |
| Jan Jansen     | Jan         | 2          | 3      | 0      | 1       | 0   |
| Piet Pietersen | Piet        | 1          | 0      | 3      | 1       | 2   |

- **naam** = volledige naam
- **displaynaam** = korte naam (komt in het schema, moet uniek zijn)
- Cijfers geven voorkeur:
  - `0 = kan niet`
  - `1 = liever niet`
  - `2 = neutraal`
  - `3 = doet graag`

---

### `wedstrijden.csv` – Wedstrijdschema

| jaar | maand | dag | club    | team    | isUit |
| ---- | ----- | --- | ------- | ------- | ----- |
| 2025 | 09    | 07  | Myra    | Heren 1 | nee   |
| 2025 | 09    | 14  | Overbos | Heren 1 | ja    |

- **isUit** = `ja` (uitwedstrijd) of `nee` (thuiswedstrijd)

---

### `afstanden.csv` – Afstanden naar clubs

| club      | afstand_km |
| --------- | ---------- |
| Nieuwkoop | 45         |
| Soest     | 80         |

- Afstand = **enkele reis in kilometers**

---

## 📊 Voorbeeld resultaat

**Schema-tabblad (Excel):**

| Datum      | Tegenstander | Uit/Thuis | Materialen 1 | Materialen 2 | Hesjes 1 | Rijden 1 | Rijden 2 | Rijden 3 | Rijden 4 | Fluiten 1 | Fluiten 2 | Bar 1 | Bar 2 |
| ---------- | ------------ | --------- | ------------ | ------------ | -------- | -------- | -------- | -------- | -------- | --------- | --------- | ----- | ----- |
| 2025-09-07 | Myra         | Thuis     | Rick         | Martijn      | Jan      |          |          |          |          | Bram      | Koen      | Dirk  | Piet  |
| 2025-09-14 | Overbos      | Uit       | Jasper       | Thomas       | Niels    | Luuk     | Bas      | Henk     | Arjan    |           |           |       |       |

👉 Daarnaast is er een **Statistiek-tabblad** met per speler hoeveel taken en kilometers ze hebben gedaan.

---

## 👩‍💻 Voor ontwikkelaars (optioneel)

Wil je zelf aan de code werken of testen draaien?

- Extra tools installeren:

  ```bash
  poetry install --with dev,test
  ```

- Automatische checks activeren:

  ```bash
  poetry run pre-commit install
  ```

- Tests draaien:

  ```bash
  poetry run pytest -v
  ```

---

## 📜 Licentie

Dit project gebruikt de **MIT-licentie**.  
Zie [LICENSE](LICENSE) voor de volledige tekst.

---

## 🤝 Bijdragen

Verbeteringen en ideeën zijn altijd welkom!  
We gebruiken [Conventional Commits](https://www.conventionalcommits.org/) en pre-commit checks voor consistente code.

---

## 📌 Toekomstige uitbreidingen

- [ ] Afstanden automatisch ophalen via een API
- [ ] Export naar extra formaten (bijv. PDF naast Excel)
