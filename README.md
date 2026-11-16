# Sporta Kluba Vadības Sistēma

Šī ir programma ar grafisko interfeisu (GUI), kas paredzēta sporta kluba datu bāzes pārvaldīšanai, izmantojot Python un Tkinter.

## Faili

- `main.py` – izveido datu bāzi un tabulas (palaist vienu reizi)
- `functions.py` – datu bāzes funkcijas un vaicājumi (CRUD operācijas)
- `app.py` – galvenā programma ar grafisko interfeisu un cilnēm (palaist šo failu)
- `sport_club.db` – SQLite datu bāze (parādās pēc `main.py` palaišanas)

Visiem failiem ir jāatrodas vienā mapē.

## Kas nepieciešams

- Python 3.14 (vai jaunāka versija)
- Tkinter (parasti iekļauts Python instalācijā)

## Instalēšana (Windows)

Dodies uz [python.org/downloads](https://www.python.org/downloads/) un lejupielādē Python instalācijas failu Windows.

Atver instalētāju. Svarīgi: pirmajā logā atzīmē izvēles rūtiņu **"Add python.exe to PATH"**, pēc tam noklikšķini uz **Install Now**.

Atver projekta mapi File Explorer, noklikšķini uz adreses joslas augšpusē, ieraksti `cmd` un nospied Enter. Atvērsies Command Prompt logs vajadzīgajā mapē.

Izveido virtuālo vidi un aktivizē to:

```bat
python -m venv .venv
.venv\Scripts\activate
```

Ja izmanto PowerShell un parādās paziņojums, ka skriptu izpilde ir atspējota, izmanto Command Prompt (`cmd`) vai izpildi šo komandu:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Pārbaudi, vai Tkinter strādā:

```bat
python -m tkinter
```

## Instalēšana (Mac / Linux)

### 1. variants – bez Homebrew (vienkāršākais)

Dodies uz [python.org/downloads](https://www.python.org/downloads/) un lejupielādē Python instalētāju macOS/Linux.

Atver failu un turpini instalēšanu (Continue), līdz tā ir pabeigta.

Atver Terminal, dodies uz projekta mapi un izveido virtuālo vidi:

```bash
cd /tava_mape
python3 -m venv .venv
source .venv/bin/activate
```

### 2. variants – ar Homebrew

Ja tev nav Homebrew, instalē to no [brew.sh](https://brew.sh/) vai izvēlies 1. variantu.

```bash
brew install python-tk@3.14
cd /tava_mape
/opt/homebrew/bin/python3.14 -m venv .venv
source .venv/bin/activate
```

Pārbaudi, vai Tkinter strādā:

```bash
python -m tkinter
```

Ja atveras neliels logs, viss ir kārtībā.

## Kā sākt

Pirmoreiz izveido datu bāzi (jāpalaiž tikai vienu reizi):

```bash
python main.py
```

Pēc tam palaid programmu:

```bash
python app.py
```

Nākamajās reizēs darbam nepieciešamas tikai šīs 3 rindas terminālī:

```bash
cd /tava_mape
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python app.py
```

## Kā tas strādā

Augšpusē atrodas cilnes: Klienti, Treneri, Nodarbības, Abonementi, Grafiks, Rezervācijas, Maksājumi, Inventārs. Noklikšķini uz cilnes, lai redzētu atbilstošo tabulu.

Apakšā atrodas pogas ierakstu pievienošanai, rediģēšanai un dzēšanai. Izvēlies ierakstu tabulā, lai tas automātiski parādītos ievades laukos, kur to var mainīt un saglabāt. Tabulas atjaunojas automātiski.

## Pogas un ievades dati

| Cilne / Tabula | Lauki (secībā) | Piezīmes |
|---|---|---|
| Klienti | vards, uzvārds, tālrunis, epasts, registracijas_datums | Datuma formāts: YYYY-MM-DD |
| Treneri | vards, uzvārds, tālrunis, specializacija, pieņemšanas_datums | Datuma formāts: YYYY-MM-DD |
| Nodarbības | nosaukums, apraksts, ilgums_minūtēs | Ilgums minūtēs (skaitlis) |
| Abonementi | klienta_id, abonementa_veids, sakuma_datums, beigu_datums | ID jābūt esošam |
| Grafiks | nodarbibas_id, trenera_id, datums_laiks, telpa | Laika formāts: YYYY-MM-DD HH:MM:SS |
| Rezervācijas | klienta_id, grafika_id, rezervacijas_datums | Datuma formāts: YYYY-MM-DD |
| Maksājumi | klienta_id, summa, maksajuma_datums, maksajuma_veids | Summa (piem., 25.50) |
| Inventārs | nosaukums, daudzums, stāvoklis, iegades_datums | Daudzums (skaitlis) |

Piezīme: ID numurus vari redzēt attiecīgo tabulu pirmajās kolonnās. Esiet uzmanīgi ar ierakstu dzēšanu – datu bāzē ir iespējota ON DELETE CASCADE dzēšana noteiktām saitēm (piem., dzēšot klientu, var tikt dzēsti arī tā abonementi).
