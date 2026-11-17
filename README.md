# Sporta kluba vadības sistēma

Projekts, kas izveidots, lai pārvaldītu sporta kluba ikdienas datus — klientus, trenerus, nodarbības, abonementus, nodarbību grafiku, rezervācijas, maksājumus un inventāru. Dati tiek glabāti SQLite datu bāzē, bet darbs ar tiem notiek, izmantojot grafisko saskarni (Tkinter) vai termināla izvēlni.

## Funkcionalitāte

- Pilns CRUD (pievienot / apskatīt / rediģēt / dzēst) visām 8 tabulām
- Grafiskā saskarnē tabulas var pārslēgt ar nolaižamo izvēlni, ierakstu formās var pārslēgties ar Enter, aizvērt ar Esc
- Saistes starp tabulām ir aizsargātas ar foreign key ierobežojumiem
- Termināla režīms ar izvēlni pa numuriem (piemērotāks ātrai pārbaudei bez loga)

## Faili

| Fails | Nozīme |
|---|---|
| `main.py` | Izveido datu bāzi, tabulas un testa ierakstus (palaist vienu reizi) |
| `functions.py` | Visas datu bāzes funkcijas (SQL vaicājumi) |
| `app.py` | Galvenā programma ar logu |
| `terminal.py` | Tas pats, bet termināla izvēlnē |
| `sport_club.db` | Datu bāzes fails (parādās pēc `main.py` palaišanas) |

## Prasības

- Python 3.10 vai jaunāka versija (pārbaudīts ar 3.14)
- Tkinter (iekļauts standarta Python instalācijā; macOS ar Homebrew Python: `brew install python-tk@3.14`)

## Palaišana

Pirms pirmās palaišanas ieteicams izveidot virtuālo vidi:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

Pēc tam:

```bash
python main.py    # izveido datu bāzi ar testa datiem (tikai vienu reizi)
python app.py     # grafiskā versija
```

## Lietošana

Logā augšā izvēlies tabulu no saraksta, apakšā izvēlies darbību (Add / Update / Delete). Aizpildi laukus un nospied Submit. ID skaitļus paņem no attiecīgās tabulas pirmās kolonnas.

Datuma formāts: `YYYY-MM-DD` (piemēram, `2026-11-17`). Grafikam datums ar laiku: `YYYY-MM-DD HH:MM:SS`.

## Datu bāzes tabulas

| Tabula | Saturs |
|---|---|
| `Klienti` | Kluba klienti un to kontakti |
| `Treneri` | Treneri un specializācijas |
| `Grupu_Nodarbibas` | Nodarbību veidi un ilgums |
| `Abonementi` | Klientu abonementi (saiste uz Klienti) |
| `Grafiks` | Kad un kur notiek nodarbības (saistes uz nodarbībām un treneriem) |
| `Rezervacijas` | Klientu rezervācijas uz grafika ierakstiem |
| `Maksajumi` | Klientu maksājumi |
| `Inventars` | Kluba inventārs |

Dzēšot klientu, automātiski tiek dzēsti arī viņa abonementi, rezervācijas un maksājumi (`ON DELETE CASCADE`) — šo darbību nevar atsaukt.
