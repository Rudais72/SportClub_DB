# Sport Club Manager
This is a program with a window where you can see and change the database of a sport club (clients, trainers, classes, memberships, schedule, bookings, payments, equipment).

## Files

- `main.py` - makes the database and adds some test data (run it one time)
- `functions.py` - all functions for the database
- `app.py` - the program with the window (run this one)
- `terminal.py` - the same program but in the terminal (menu with numbers)
- `sport_club.db` - the database (it appears after you run the first file)

All files must be in the same folder.

## What you need

- Python 3.14
- Tk 

## How to install (Windows)
 
1. Go to https://www.python.org/downloads/ and download the Python installer for Windows.
2. Open the installer. **Important:** at the first screen turn on the checkbox **"Add python.exe to PATH"**, then click Install Now. Tk is already inside.
3. Open the project folder in File Explorer, click on the address bar, type `cmd` and press Enter. A black window (Command Prompt) opens in the right folder.
4. Make a virtual environment and turn it on:
```
python -m venv .venv
.venv\Scripts\activate
```
 
 
If you use PowerShell and it says that running scripts is disabled, use Command Prompt (cmd) instead, or run this first:
 
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
 
### Check that Tk works:
```
python -m tkinter
```

## How to install (for Mac/Linux)

You need Python with Tk. There are two ways how to install it.

### Way 1 - without Homebrew (easier)

1. Go to https://www.python.org/downloads/ and download the Python installer for macOS.
2. Open the file and click Continue until it is installed. Tk is already inside, you don't need anything more.
3. Open Terminal, go to the project folder and make a virtual environment:

```
cd /your_map
python3 -m venv .venv
source .venv/bin/activate
```



### Way 2 - with Homebrew

If you don't have Homebrew, install it first from https://brew.sh. Or choose Way 1.

Then:

```
brew install python-tk@3.14
cd /your_map
/opt/homebrew/bin/python3.14 -m venv .venv
source .venv/bin/activate
```

### Check that Tk works (both ways)

```
python -m tkinter
```

A small window should open. If it opens, everything is ok.

## How to start

First, make the database (only one time):

```
python main.py
```

Then start the program:

```
python app.py
```

Next time you only need these 3 lines:

```
cd /your_map
source .venv/bin/activate
python app.py
```

## How it works

At the top there is one dropdown with all tables: Clients, Trainers, Group classes, Memberships, Schedule, Bookings, Payments, Equipment. Pick a table to see it. Columns share the whole width and long text wraps onto several lines.

At the bottom there are buttons. Click a button, fill in the fields and press Submit. Press Cancel (or Esc) if you changed your mind. The tables update by themselves.

## Buttons

| Button | What to write |
|--------|---------------|
| Add client | first name, last name, phone, email, registration date |
| Update client | client ID, first name, last name, phone, email, registration date |
| Delete client | client ID |
| Add trainer | first name, last name, phone, specialization, hire date |
| Update trainer | trainer ID, first name, last name, phone, specialization, hire date |
| Delete trainer | trainer ID |
| Add class | name, description, duration in minutes |
| Update class | class ID, name, description, duration in minutes |
| Delete class | class ID |
| Add membership | client ID, type, start date, end date |
| Update membership | membership ID, client ID, type, start date, end date |
| Delete membership | membership ID |
| Add schedule | class ID, trainer ID, date & time, room |
| Update schedule | schedule ID, class ID, trainer ID, date & time, room |
| Delete schedule | schedule ID |
| Add booking | client ID, schedule ID, booking date |
| Update booking | booking ID, client ID, schedule ID, booking date |
| Delete booking | booking ID |
| Add payment | client ID, amount (for example 25.50), date, method |
| Update payment | payment ID, client ID, amount, date, method |
| Delete payment | payment ID |
| Add equipment | name, quantity, condition, purchase date |
| Update equipment | equipment ID, name, quantity, condition, purchase date |
| Delete equipment | equipment ID |

Dates must look like this: `2026-11-17`. Date & time must look like this: `2026-11-18 18:00:00`.

IDs are in the first column of the tables, so look there first.

Be careful with Delete client. It deletes the client and everything about him (memberships, bookings, payments...). You can't undo it.

<h1 align="center">
Thanks and GL!
</h1>
