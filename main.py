import sqlite3

# Connect to DB
database = sqlite3.connect("sport_club.db")
database.execute("PRAGMA foreign_keys = ON")
cursor = database.cursor()

# Create tables

# Clients
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Klienti" (
    "klienta_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "vards" TEXT NOT NULL,
    "uzvards" TEXT NOT NULL,
    "talrunis" TEXT UNIQUE,
    "epasts" TEXT UNIQUE,
    "registracijas_datums" TEXT NOT NULL
)
""")

# Trainers
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Treneri" (
    "trenera_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "vards" TEXT NOT NULL,
    "uzvards" TEXT NOT NULL,
    "talrunis" TEXT UNIQUE,
    "specializacija" TEXT NOT NULL,
    "pienemsanas_datums" TEXT NOT NULL
)
""")

# Group classes
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Grupu_Nodarbibas" (
    "nodarbibas_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nosaukums" TEXT NOT NULL UNIQUE,
    "apraksts" TEXT NOT NULL,
    "ilgums_minutes" INTEGER NOT NULL
)
""")

# Memberships
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Abonementi" (
    "abonementa_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "klienta_id" INTEGER NOT NULL,
    "abonementa_veids" TEXT NOT NULL,
    "sakuma_datums" TEXT NOT NULL,
    "beigu_datums" TEXT NOT NULL,
    FOREIGN KEY ("klienta_id") REFERENCES "Klienti"("klienta_id")
        ON UPDATE NO ACTION ON DELETE CASCADE
)
""")

# Schedule
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Grafiks" (
    "grafika_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nodarbibas_id" INTEGER NOT NULL,
    "trenera_id" INTEGER NOT NULL,
    "datums_laiks" TEXT NOT NULL,
    "telpa" TEXT NOT NULL,
    FOREIGN KEY ("nodarbibas_id") REFERENCES "Grupu_Nodarbibas"("nodarbibas_id")
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("trenera_id") REFERENCES "Treneri"("trenera_id")
        ON UPDATE NO ACTION ON DELETE NO ACTION
)
""")

# Bookings
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Rezervacijas" (
    "rezervacijas_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "klienta_id" INTEGER NOT NULL,
    "grafika_id" INTEGER NOT NULL,
    "rezervacijas_datums" TEXT NOT NULL,
    FOREIGN KEY ("klienta_id") REFERENCES "Klienti"("klienta_id")
        ON UPDATE NO ACTION ON DELETE CASCADE,
    FOREIGN KEY ("grafika_id") REFERENCES "Grafiks"("grafika_id")
        ON UPDATE NO ACTION ON DELETE CASCADE
)
""")

# Payments
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Maksajumi" (
    "maksajuma_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "klienta_id" INTEGER NOT NULL,
    "summa" REAL NOT NULL,
    "maksajuma_datums" TEXT NOT NULL,
    "maksajuma_veids" TEXT NOT NULL,
    FOREIGN KEY ("klienta_id") REFERENCES "Klienti"("klienta_id")
        ON UPDATE NO ACTION ON DELETE CASCADE
)
""")

# Equipment
cursor.execute("""
CREATE TABLE IF NOT EXISTS "Inventars" (
    "inventara_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nosaukums" TEXT NOT NULL,
    "daudzums" INTEGER NOT NULL,
    "stavoklis" TEXT NOT NULL,
    "iegades_datums" TEXT NOT NULL
)
""")

# Fill tables

# Clients
cursor.execute("""
INSERT OR IGNORE INTO Klienti (klienta_id, vards, uzvards, talrunis, epasts, registracijas_datums)
VALUES (1, 'Anna', 'Berzina', '+371 20000001', 'anna.berzina@mail.com', '2026-01-10')
""")
cursor.execute("""
INSERT OR IGNORE INTO Klienti (klienta_id, vards, uzvards, talrunis, epasts, registracijas_datums)
VALUES (2, 'Janis', 'Ozols', '+371 20000002', 'janis.ozols@mail.com', '2026-02-15')
""")
cursor.execute("""
INSERT OR IGNORE INTO Klienti (klienta_id, vards, uzvards, talrunis, epasts, registracijas_datums)
VALUES (3, 'Liga', 'Kalnina', '+371 20000003', 'liga.kalnina@mail.com', '2026-03-20')
""")

# Trainers
cursor.execute("""
INSERT OR IGNORE INTO Treneri (trenera_id, vards, uzvards, talrunis, specializacija, pienemsanas_datums)
VALUES (1, 'Peteris', 'Liepa', '+371 30000001', 'Fitness', '2025-09-01')
""")
cursor.execute("""
INSERT OR IGNORE INTO Treneri (trenera_id, vards, uzvards, talrunis, specializacija, pienemsanas_datums)
VALUES (2, 'Mara', 'Ziedina', '+371 30000002', 'Joga', '2025-10-15')
""")

# Group classes
cursor.execute("""
INSERT OR IGNORE INTO Grupu_Nodarbibas (nodarbibas_id, nosaukums, apraksts, ilgums_minutes)
VALUES (1, 'Trenazieru zale', 'Grupu trenins trenažieru zālē', 60)
""")
cursor.execute("""
INSERT OR IGNORE INTO Grupu_Nodarbibas (nodarbibas_id, nosaukums, apraksts, ilgums_minutes)
VALUES (2, 'Rita joga', 'Mierīga rīta jogas nodarbība', 45)
""")
cursor.execute("""
INSERT OR IGNORE INTO Grupu_Nodarbibas (nodarbibas_id, nosaukums, apraksts, ilgums_minutes)
VALUES (3, 'Aerobika', 'Enerģiska aerobikas nodarbība', 50)
""")

# Memberships
cursor.execute("""
INSERT OR IGNORE INTO Abonementi (abonementa_id, klienta_id, abonementa_veids, sakuma_datums, beigu_datums)
VALUES (1, 1, 'Menesa', '2026-01-11', '2026-02-11')
""")
cursor.execute("""
INSERT OR IGNORE INTO Abonementi (abonementa_id, klienta_id, abonementa_veids, sakuma_datums, beigu_datums)
VALUES (2, 2, 'Gada', '2026-02-16', '2027-02-16')
""")
cursor.execute("""
INSERT OR IGNORE INTO Abonementi (abonementa_id, klienta_id, abonementa_veids, sakuma_datums, beigu_datums)
VALUES (3, 3, 'Menesa', '2026-03-21', '2026-04-21')
""")

# Schedule
cursor.execute("""
INSERT OR IGNORE INTO Grafiks (grafika_id, nodarbibas_id, trenera_id, datums_laiks, telpa)
VALUES (1, 1, 1, '2026-11-18 18:00:00', 'Zale 1')
""")
cursor.execute("""
INSERT OR IGNORE INTO Grafiks (grafika_id, nodarbibas_id, trenera_id, datums_laiks, telpa)
VALUES (2, 2, 2, '2026-11-19 08:00:00', 'Zale 2')
""")
cursor.execute("""
INSERT OR IGNORE INTO Grafiks (grafika_id, nodarbibas_id, trenera_id, datums_laiks, telpa)
VALUES (3, 3, 1, '2026-11-19 19:00:00', 'Zale 1')
""")

# Bookings
cursor.execute("""
INSERT OR IGNORE INTO Rezervacijas (rezervacijas_id, klienta_id, grafika_id, rezervacijas_datums)
VALUES (1, 1, 1, '2026-11-17')
""")
cursor.execute("""
INSERT OR IGNORE INTO Rezervacijas (rezervacijas_id, klienta_id, grafika_id, rezervacijas_datums)
VALUES (2, 2, 2, '2026-11-17')
""")
cursor.execute("""
INSERT OR IGNORE INTO Rezervacijas (rezervacijas_id, klienta_id, grafika_id, rezervacijas_datums)
VALUES (3, 3, 3, '2026-11-16')
""")

# Payments
cursor.execute("""
INSERT OR IGNORE INTO Maksajumi (maksajuma_id, klienta_id, summa, maksajuma_datums, maksajuma_veids)
VALUES (1, 1, 25.50, '2026-01-11', 'Karte')
""")
cursor.execute("""
INSERT OR IGNORE INTO Maksajumi (maksajuma_id, klienta_id, summa, maksajuma_datums, maksajuma_veids)
VALUES (2, 2, 250.00, '2026-02-16', 'Nauda')
""")
cursor.execute("""
INSERT OR IGNORE INTO Maksajumi (maksajuma_id, klienta_id, summa, maksajuma_datums, maksajuma_veids)
VALUES (3, 3, 25.50, '2026-03-21', 'Karte')
""")

# Equipment
cursor.execute("""
INSERT OR IGNORE INTO Inventars (inventara_id, nosaukums, daudzums, stavoklis, iegades_datums)
VALUES (1, 'Skrienis', 10, 'Laba', '2025-08-01')
""")
cursor.execute("""
INSERT OR IGNORE INTO Inventars (inventara_id, nosaukums, daudzums, stavoklis, iegades_datums)
VALUES (2, 'Jogas mats', 15, 'Laba', '2025-08-15')
""")
cursor.execute("""
INSERT OR IGNORE INTO Inventars (inventara_id, nosaukums, daudzums, stavoklis, iegades_datums)
VALUES (3, 'Hanteles 5kg', 8, 'Vidēja', '2025-09-10')
""")

database.commit()

# Get data from tables

print("--- Clients ---")
cursor.execute("SELECT klienta_id, vards, uzvards, talrunis, epasts, registracijas_datums FROM Klienti")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | {row[1]} {row[2]} | Phone: {row[3]} | Email: {row[4]} | Registered: {row[5]}")

print("\n--- Trainers ---")
cursor.execute("SELECT trenera_id, vards, uzvards, specializacija, pienemsanas_datums FROM Treneri")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | {row[1]} {row[2]} | Specialization: {row[3]} | Hired: {row[4]}")

print("\n--- Memberships ---")
cursor.execute("""
SELECT a.abonementa_id, k.vards, k.uzvards, a.abonementa_veids, a.sakuma_datums, a.beigu_datums
FROM Abonementi a
         JOIN Klienti k ON a.klienta_id = k.klienta_id
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Client: {row[1]} {row[2]} | Type: {row[3]} | {row[4]} -> {row[5]}")

print("\n--- Schedule ---")
cursor.execute("""
SELECT g.grafika_id, n.nosaukums, t.vards, t.uzvards, g.datums_laiks, g.telpa
FROM Grafiks g
         JOIN Grupu_Nodarbibas n ON g.nodarbibas_id = n.nodarbibas_id
         JOIN Treneri t ON g.trenera_id = t.trenera_id
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Class: {row[1]} | Trainer: {row[2]} {row[3]} | Time: {row[4]} | Room: {row[5]}")

print("\n--- Bookings ---")
cursor.execute("""
SELECT r.rezervacijas_id, k.vards, k.uzvards, n.nosaukums, r.rezervacijas_datums
FROM Rezervacijas r
         JOIN Klienti k ON r.klienta_id = k.klienta_id
         JOIN Grafiks g ON r.grafika_id = g.grafika_id
         JOIN Grupu_Nodarbibas n ON g.nodarbibas_id = n.nodarbibas_id
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Client: {row[1]} {row[2]} | Class: {row[3]} | Booked: {row[4]}")

print("\n--- Payments ---")
cursor.execute("""
SELECT m.maksajuma_id, k.vards, k.uzvards, m.summa, m.maksajuma_datums, m.maksajuma_veids
FROM Maksajumi m
         JOIN Klienti k ON m.klienta_id = k.klienta_id
""")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Client: {row[1]} {row[2]} | Amount: {row[3]} | Date: {row[4]} | Method: {row[5]}")

print("\n--- Equipment ---")
cursor.execute("SELECT inventara_id, nosaukums, daudzums, stavoklis, iegades_datums FROM Inventars")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | {row[1]} | Quantity: {row[2]} | Condition: {row[3]} | Bought: {row[4]}")

database.close()
