# functions.py
import sqlite3

DATABASE_NAME = "sport_club.db"

def connect():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn

# --- KLIENTI ---
def add_client(first_name, last_name, phone, email, registration_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Klienti (vards, uzvards, tālrunis, epasts, registracijas_datums) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, phone, email, registration_date)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_clients():
    conn = connect()
    res = conn.execute("SELECT * FROM Klienti").fetchall()
    conn.close()
    return res

def update_client(client_id, first_name, last_name, phone, email, registration_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Klienti SET vards = ?, uzvards = ?, tālrunis = ?, epasts = ?, registracijas_datums = ? WHERE klienta_id = ?",
        (first_name, last_name, phone, email, registration_date, client_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_client(client_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Klienti WHERE klienta_id = ?", (client_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- TRENERI ---
def add_trainer(first_name, last_name, phone, specialization, hire_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Treneri (vards, uzvards, tālrunis, specializacija, pieņemšanas_datums) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, phone, specialization, hire_date)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_trainers():
    conn = connect()
    res = conn.execute("SELECT * FROM Treneri").fetchall()
    conn.close()
    return res

def update_trainer(trainer_id, first_name, last_name, phone, specialization, hire_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Treneri SET vards = ?, uzvards = ?, tālrunis = ?, specializacija = ?, pieņemšanas_datums = ? WHERE trenera_id = ?",
        (first_name, last_name, phone, specialization, hire_date, trainer_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_trainer(trainer_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Treneri WHERE trenera_id = ?", (trainer_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- GRUPU NODARBĪBAS ---
def add_group_class(name, description, duration_minutes):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Grupu_Nodarbibas (nosaukums, apraksts, ilgums_minutēs) VALUES (?, ?, ?)",
        (name, description, duration_minutes)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_group_classes():
    conn = connect()
    res = conn.execute("SELECT * FROM Grupu_Nodarbibas").fetchall()
    conn.close()
    return res

def update_group_class(class_id, name, description, duration_minutes):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Grupu_Nodarbibas SET nosaukums = ?, apraksts = ?, ilgums_minutēs = ? WHERE nodarbibas_id = ?",
        (name, description, duration_minutes, class_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_group_class(class_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Grupu_Nodarbibas WHERE nodarbibas_id = ?", (class_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- ABONEMENTI ---
def add_membership(client_id, membership_type, start_date, end_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Abonementi (klienta_id, abonementa_veids, sakuma_datums, beigu_datums) VALUES (?, ?, ?, ?)",
        (client_id, membership_type, start_date, end_date)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_memberships():
    conn = connect()
    res = conn.execute("SELECT * FROM Abonementi").fetchall()
    conn.close()
    return res

def update_membership(membership_id, client_id, membership_type, start_date, end_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Abonementi SET klienta_id = ?, abonementa_veids = ?, sakuma_datums = ?, beigu_datums = ? WHERE abonementa_id = ?",
        (client_id, membership_type, start_date, end_date, membership_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_membership(membership_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Abonementi WHERE abonementa_id = ?", (membership_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- GRAFIKS ---
def add_schedule(class_id, trainer_id, date_time, room):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Grafiks (nodarbibas_id, trenera_id, datums_laiks, telpa) VALUES (?, ?, ?, ?)",
        (class_id, trainer_id, date_time, room)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_schedules():
    conn = connect()
    res = conn.execute("SELECT * FROM Grafiks").fetchall()
    conn.close()
    return res

def update_schedule(schedule_id, class_id, trainer_id, date_time, room):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Grafiks SET nodarbibas_id = ?, trenera_id = ?, datums_laiks = ?, telpa = ? WHERE grafika_id = ?",
        (class_id, trainer_id, date_time, room, schedule_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_schedule(schedule_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Grafiks WHERE grafika_id = ?", (schedule_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- REZERVĀCIJAS ---
def add_booking(client_id, schedule_id, booking_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Rezervacijas (klienta_id, grafika_id, rezervacijas_datums) VALUES (?, ?, ?)",
        (client_id, schedule_id, booking_date)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_bookings():
    conn = connect()
    res = conn.execute("SELECT * FROM Rezervacijas").fetchall()
    conn.close()
    return res

def update_booking(booking_id, client_id, schedule_id, booking_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Rezervacijas SET klienta_id = ?, grafika_id = ?, rezervacijas_datums = ? WHERE rezervacijas_id = ?",
        (client_id, schedule_id, booking_date, booking_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_booking(booking_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Rezervacijas WHERE rezervacijas_id = ?", (booking_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- MAKSĀJUMI ---
def add_payment(client_id, amount, payment_date, payment_method):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Maksajumi (klienta_id, summa, maksajuma_datums, maksajuma_veids) VALUES (?, ?, ?, ?)",
        (client_id, amount, payment_date, payment_method)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_payments():
    conn = connect()
    res = conn.execute("SELECT * FROM Maksajumi").fetchall()
    conn.close()
    return res

def update_payment(payment_id, client_id, amount, payment_date, payment_method):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Maksajumi SET klienta_id = ?, summa = ?, maksajuma_datums = ?, maksajuma_veids = ? WHERE maksajuma_id = ?",
        (client_id, amount, payment_date, payment_method, payment_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_payment(payment_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Maksajumi WHERE maksajuma_id = ?", (payment_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


# --- INVENTĀRS ---
def add_equipment(name, quantity, condition, purchase_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Inventars (nosaukums, daudzums, stāvoklis, iegades_datums) VALUES (?, ?, ?, ?)",
        (name, quantity, condition, purchase_date)
    )
    conn.commit()
    idx = cursor.lastrowid
    conn.close()
    return idx

def get_equipment():
    conn = connect()
    res = conn.execute("SELECT * FROM Inventars").fetchall()
    conn.close()
    return res

def update_equipment(equipment_id, name, quantity, condition, purchase_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Inventars SET nosaukums = ?, daudzums = ?, stāvoklis = ?, iegades_datums = ? WHERE inventara_id = ?",
        (name, quantity, condition, purchase_date, equipment_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected

def delete_equipment(equipment_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Inventars WHERE inventara_id = ?", (equipment_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected