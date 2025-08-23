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
11. [🚑 Problemen oplossen met Poetry](#-problemen-oplossen-met-poetry)

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
  - [`taken.csv`](templates/taken.csv) → lijst met taken
  - [`wedstrijden.csv`](templates/wedstrijden.csv) → wedstrijdschema
  - [`spelers.csv`](templates/spelers.csv) → spelersnamen en voorkeuren
  - [`afstanden.csv`](templates/afstanden.csv) → afstanden naar clubs

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

> [!TIP]
> De map [**`templates/`**](templates/) bevat voorbeelden die je kunt kopiëren en invullen met je eigen teaminformatie.

---

## ⚙️ Installatie (eenmalig instellen)

Voor het gebruik heb je **Python** nodig.  
Wij raden **Conda** aan, omdat dat het eenvoudigst is en overal werkt.

### 1. Installeer Conda

- Download: [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda)  
- Volg de installatiehandleiding voor jouw computer.

### 2. Haal het project binnen

- Als je het project als `.zip` hebt gedownload:

  - Pak het bestand uit (rechtermuisknop → "Alles uitpakken").
  - Je krijgt een map zoals `Team-Task-Scheduler/` of `Team-Task-Scheduler-main/`.

- Als je **Git** hebt geïnstalleerd:

  ```bash
  git clone https://github.com/jouw-gebruikersnaam/Team-Task-Scheduler.git
  ```

> [!TIP]
> Onthoud waar deze map staat, want je moet er in de volgende stappen naartoe gaan.

### 3. Maak een nieuwe omgeving voor dit project  

Open een terminal/Anaconda Prompt en voer uit:

```bash
conda create -n team-tasks python=3.13
```

```bash
conda activate team-tasks
```

### 4. Installeer de benodigde hulpmiddelen

```bash
conda install conda-forge::pipx
```

```bash
pipx ensurepath
```

```bash
pipx install poetry
```

> [!WARNING]
> Soms wordt `pipx` of `poetry` niet meteen herkend.  
> Zie de sectie [🚑 Problemen oplossen met Poetry](#-problemen-oplossen-met-poetry) als je een foutmelding krijgt zoals *“poetry not found”*.

### 5. Installeer het project zelf  

Ga in de terminal naar de projectmap:

```bash
cd pad/naar/Team-Task-Scheduler
```

```bash
poetry install
```

> [!TIP]
> Twijfel je of je in de juiste map zit?  
> Typ `ls` (macOS/Linux) of `dir` (Windows) en controleer dat `README.md`, `task_planner/` en `templates/` zichtbaar zijn.

👉 Klaar! Je hoeft dit maar één keer te doen. Daarna kun je steeds direct naar [**Gebruik**](#-gebruik-het-schema-maken) springen.

---

## 🏃 Gebruik (het schema maken)

1. Kopieer de map [**`templates/`**](templates/) naar een eigen werkmap, bijvoorbeeld:

   ```txt
   mijn-team/
   ├── taken.csv
   ├── spelers.csv
   ├── wedstrijden.csv
   └── afstanden.csv
   ```

   <!-- TODO: Misschien een `cp` uitleg of een verkenner uitleg over kopieren -->

2. Vul de bestanden in met jullie teaminformatie (zie [📝 Hoe vul je de bestanden in?](#-hoe-vul-je-de-bestanden-in)).

3. Activeer de Conda-omgeving in je werkmap:

   ```bash
   cd pad/naar/mijn-team/
   ```

   ```bash
   conda activate team-tasks
   ```

   Controleer dat je bestanden `taken.csv`, `spelers.csv`, `wedstrijden.csv`, `afstanden.csv` in de map staan:

   ```bash
   ls   # macOS/Linux
   dir  # Windows
   ```

4. Draai het programma:

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

### [`taken.csv`](templates/taken.csv) – Takenlijst

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

### [`spelers.csv`](templates/spelers.csv) – Spelers en voorkeuren

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

### [`wedstrijden.csv`](templates/wedstrijden.csv) – Wedstrijdschema

| jaar | maand | dag | club    | team    | isUit |
| ---- | ----- | --- | ------- | ------- | ----- |
| 2025 | 09    | 07  | Myra    | Heren 1 | nee   |
| 2025 | 09    | 14  | Overbos | Heren 1 | ja    |

- **isUit** = `ja` (uitwedstrijd) of `nee` (thuiswedstrijd)

---

### [`afstanden.csv`](templates/afstanden.csv) – Afstanden naar clubs

| club      | afstand\_km |
| --------- | ----------- |
| Nieuwkoop | 45          |
| Soest     | 80          |

- Afstand = **enkele reis in kilometers**

---

## 📊 Voorbeeld resultaat

**Schema-tabblad (Excel):**

![Schema-tabblad (Excel)](.github/schema-tabblad-vb.png)

**Schema-tabblad (Markdown):**

| Datum      | Tegenstander | Uit/Thuis | Materialen 1 | Materialen 2 | Hesjes 1 | Rijden 1 | Rijden 2 | Rijden 3 | Rijden 4 | Fluiten 1 | Fluiten 2 | Bar 1 | Bar 2 |
| ---------- | ------------ | --------- | ------------ | ------------ | -------- | -------- | -------- | -------- | -------- | --------- | --------- | ----- | ----- |
| 2025-09-07 | Myra         | Thuis     | Rick         | Martijn      | Jan      |          |          |          |          | Bram      | Koen      | Dirk  | Piet  |
| 2025-09-14 | Overbos      | Uit       | Jasper       | Thomas       | Niels    | Luuk     | Bas      | Henk     | Arjan    |           |           |       |       |

> [!NOTE]
> Daarnaast is er een **Statistiek-tabblad** met per speler hoeveel taken en kilometers ze hebben gedaan.

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

---

## 🚑 Problemen oplossen met Poetry

Soms werkt `poetry` niet meteen nadat je het hebt geïnstalleerd met `pipx`.  
Je krijgt dan een melding zoals:

```bash
poetry: command not found
# of in Windows:
'poetry' is not recognized as an internal or external command
```

Dat komt doordat de map waar `pipx` programma’s neerzet nog niet aan je **PATH** is toegevoegd.  
Geen paniek: dit is eenvoudig op te lossen.

### 👣 Snelle oplossing

1. Sluit terminal/computer volledig af en open opnieuw.  
   ❗ **Let op:** Iedere keer dat je de terminal opnieuw opstart, moet je de Conda-omgeving ook opnieuw activeren, d.m.v. `conda activate team-tasks`.
2. Voer uit:

   ```bash
   pipx ensurepath
   ```

3. Sluit terminal/computer volledig af en open opnieuw.
4. Test:

   ```bash
   poetry --version
   ```

Ga nu verder met de volgende stap in [⚙️ Installatie (eenmalig instellen)](#️-installatie-eenmalig-instellen).

> [!TIP]
> Zie onderstaande secties voor platform-specifieke instructies als het nog niet werkt.

---

### 🪟 Windows

1. Controleer waar pipx programma’s heeft neergezet:

   ```bash
   pipx list
   ```

   Zoek de regel: `apps are exposed on your PATH at C:\Users\JOUWNAAM\.local\bin`

2. Voeg dit pad toe aan je PATH via **Instellingen → Systeem → Info → Geavanceerde systeeminstellingen → Geavanceerd → Omgevingsvariabelen → Gebruikersvariabelen → Path → Bewerken → Nieuw**.
3. Sluit terminal/computer volledig af en open opnieuw, test met:

   ```bash
   poetry --version
   ```

---

###  macOS

1. Voer uit:

   ```bash
   pipx ensurepath
   ```

2. Voeg eventueel toe aan je shell-profiel:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. Sluit terminal/computer volledig af en open opnieuw, test met:

   ```bash
   poetry --version
   ```

---

### 🐧 Linux

Zelfde als macOS, maar voeg toe aan `~/.bashrc` of `~/.zshrc`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### 🆘 Noodoplossingen

- Herstart computer en terminal.
- Controleer dat de juiste Conda-omgeving actief is:

  ```bash
  conda activate team-tasks
  ```

- Tijdelijk via pipx run:

  ```bash
  pipx run --spec poetry poetry install
  ```
