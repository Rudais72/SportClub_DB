import sqlite3
from datetime import datetime


def connect():
    database = sqlite3.connect("sport_club.db")
    database.execute("PRAGMA foreign_keys = ON")
    return database


# ---------------------------------- PIEVIENOT KLIENTU ----------------------------------
def add_client(first_name, last_name, phone, email, registration_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Klienti (vards, uzvards, talrunis, epasts, registracijas_datums) VALUES (?,?,?,?,?)",
        (first_name, last_name, phone, email, registration_date)
    )
    database.commit()
    client_id = cursor.lastrowid
    database.close()
    return client_id


# ---------------------------------- IZSAUKT KLIENTU SARAKSTU ----------------------------------
def get_clients():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT klienta_id, vards, uzvards, talrunis, epasts, registracijas_datums FROM Klienti")
    clients = cursor.fetchall()
    database.close()
    return clients


# ---------------------------------- MAINIT KLIENTU ----------------------------------
def update_client(client_id, first_name, last_name, phone, email, registration_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Klienti SET vards = ?, uzvards = ?, talrunis = ?, epasts = ?, registracijas_datums = ? WHERE klienta_id = ?",
        (first_name, last_name, phone, email, registration_date, client_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST KLIENTU ----------------------------------
def delete_client(client_id):
    database = connect()
    cursor = database.cursor()
    # Foreign keys are ON, so memberships, bookings and payments are removed too (ON DELETE CASCADE)
    cursor.execute("DELETE FROM Klienti WHERE klienta_id = ?", (client_id,))
    database.commit()
    deleted = cursor.rowcount  # 1 if the client existed, 0 if not
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT TRENERI ----------------------------------
def add_trainer(first_name, last_name, phone, specialization, hire_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Treneri (vards, uzvards, talrunis, specializacija, pienemsanas_datums) VALUES (?,?,?,?,?)",
        (first_name, last_name, phone, specialization, hire_date)
    )
    database.commit()
    trainer_id = cursor.lastrowid
    database.close()
    return trainer_id


# ---------------------------------- IZSAUKT TRENERU SARAKSTU ----------------------------------
def get_trainers():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT trenera_id, vards, uzvards, talrunis, specializacija, pienemsanas_datums FROM Treneri")
    trainers = cursor.fetchall()
    database.close()
    return trainers


# ---------------------------------- MAINIT TRENERI ----------------------------------
def update_trainer(trainer_id, first_name, last_name, phone, specialization, hire_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Treneri SET vards = ?, uzvards = ?, talrunis = ?, specializacija = ?, pienemsanas_datums = ? WHERE trenera_id = ?",
        (first_name, last_name, phone, specialization, hire_date, trainer_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST TRENERI ----------------------------------
def delete_trainer(trainer_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Treneri WHERE trenera_id = ?", (trainer_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT NODARBIBU ----------------------------------
def add_group_class(name, description, duration_minutes):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Grupu_Nodarbibas (nosaukums, apraksts, ilgums_minutes) VALUES (?,?,?)",
        (name, description, duration_minutes)
    )
    database.commit()
    class_id = cursor.lastrowid
    database.close()
    return class_id


# ---------------------------------- IZSAUKT NODARBIBU SARAKSTU ----------------------------------
def get_group_classes():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT nodarbibas_id, nosaukums, apraksts, ilgums_minutes FROM Grupu_Nodarbibas")
    classes = cursor.fetchall()
    database.close()
    return classes


# ---------------------------------- MAINIT NODARBIBU ----------------------------------
def update_group_class(class_id, name, description, duration_minutes):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Grupu_Nodarbibas SET nosaukums = ?, apraksts = ?, ilgums_minutes = ? WHERE nodarbibas_id = ?",
        (name, description, duration_minutes, class_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST NODARBIBU ----------------------------------
def delete_group_class(class_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Grupu_Nodarbibas WHERE nodarbibas_id = ?", (class_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT ABONEMENTU ----------------------------------
def add_membership(client_id, membership_type, start_date, end_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Abonementi (klienta_id, abonementa_veids, sakuma_datums, beigu_datums) VALUES (?,?,?,?)",
        (client_id, membership_type, start_date, end_date)
    )
    database.commit()
    membership_id = cursor.lastrowid
    database.close()
    return membership_id


# ---------------------------------- IZSAUKT ABONEMENTU SARAKSTU ----------------------------------
def get_memberships():
    database = connect()
    cursor = database.cursor()
    cursor.execute("""
                   SELECT a.abonementa_id,
                          a.klienta_id,
                          k.vards,
                          k.uzvards,
                          a.abonementa_veids,
                          a.sakuma_datums,
                          a.beigu_datums
                   FROM Abonementi a
                            JOIN Klienti k
                                 ON a.klienta_id = k.klienta_id
                   ORDER BY a.abonementa_id
                   """)
    memberships = cursor.fetchall()
    database.close()
    return memberships


# ---------------------------------- MAINIT ABONEMENTU ----------------------------------
def update_membership(membership_id, client_id, membership_type, start_date, end_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Abonementi SET klienta_id = ?, abonementa_veids = ?, sakuma_datums = ?, beigu_datums = ? WHERE abonementa_id = ?",
        (client_id, membership_type, start_date, end_date, membership_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST ABONEMENTU ----------------------------------
def delete_membership(membership_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Abonementi WHERE abonementa_id = ?", (membership_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT GRAFIKU ----------------------------------
def add_schedule(class_id, trainer_id, date_time, room):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Grafiks (nodarbibas_id, trenera_id, datums_laiks, telpa) VALUES (?,?,?,?)",
        (class_id, trainer_id, date_time, room)
    )
    database.commit()
    schedule_id = cursor.lastrowid
    database.close()
    return schedule_id


# ---------------------------------- IZSAUKT GRAFIKA SARAKSTU ----------------------------------
def get_schedules():
    database = connect()
    cursor = database.cursor()
    cursor.execute("""
                   SELECT g.grafika_id,
                          n.nosaukums,
                          t.vards,
                          t.uzvards,
                          g.datums_laiks,
                          g.telpa
                   FROM Grafiks g
                            JOIN Grupu_Nodarbibas n
                                 ON g.nodarbibas_id = n.nodarbibas_id
                            JOIN Treneri t
                                 ON g.trenera_id = t.trenera_id
                   ORDER BY g.grafika_id
                   """)
    schedules = cursor.fetchall()
    database.close()
    return schedules


# ---------------------------------- MAINIT GRAFIKU ----------------------------------
def update_schedule(schedule_id, class_id, trainer_id, date_time, room):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Grafiks SET nodarbibas_id = ?, trenera_id = ?, datums_laiks = ?, telpa = ? WHERE grafika_id = ?",
        (class_id, trainer_id, date_time, room, schedule_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST GRAFIKU ----------------------------------
def delete_schedule(schedule_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Grafiks WHERE grafika_id = ?", (schedule_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT REZERVACIJU ----------------------------------
def add_booking(client_id, schedule_id, booking_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Rezervacijas (klienta_id, grafika_id, rezervacijas_datums) VALUES (?,?,?)",
        (client_id, schedule_id, booking_date)
    )
    database.commit()
    booking_id = cursor.lastrowid
    database.close()
    return booking_id


# ---------------------------------- IZSAUKT REZERVACIJU SARAKSTU ----------------------------------
def get_bookings():
    database = connect()
    cursor = database.cursor()
    cursor.execute("""
                   SELECT r.rezervacijas_id,
                          r.klienta_id,
                          k.vards,
                          k.uzvards,
                          n.nosaukums,
                          r.rezervacijas_datums
                   FROM Rezervacijas r
                            JOIN Klienti k
                                 ON r.klienta_id = k.klienta_id
                            JOIN Grafiks g
                                 ON r.grafika_id = g.grafika_id
                            JOIN Grupu_Nodarbibas n
                                 ON g.nodarbibas_id = n.nodarbibas_id
                   ORDER BY r.rezervacijas_id
                   """)
    bookings = cursor.fetchall()
    database.close()
    return bookings


# ---------------------------------- MAINIT REZERVACIJU ----------------------------------
def update_booking(booking_id, client_id, schedule_id, booking_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Rezervacijas SET klienta_id = ?, grafika_id = ?, rezervacijas_datums = ? WHERE rezervacijas_id = ?",
        (client_id, schedule_id, booking_date, booking_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST REZERVACIJU ----------------------------------
def delete_booking(booking_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Rezervacijas WHERE rezervacijas_id = ?", (booking_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT MAKSAJUMU ----------------------------------
def add_payment(client_id, amount, payment_date, payment_method):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Maksajumi (klienta_id, summa, maksajuma_datums, maksajuma_veids) VALUES (?,?,?,?)",
        (client_id, amount, payment_date, payment_method)
    )
    database.commit()
    payment_id = cursor.lastrowid
    database.close()
    return payment_id


# ---------------------------------- IZSAUKT MAKSAJUMU SARAKSTU ----------------------------------
def get_payments():
    database = connect()
    cursor = database.cursor()
    cursor.execute("""
                   SELECT m.maksajuma_id,
                          m.klienta_id,
                          k.vards,
                          k.uzvards,
                          m.summa,
                          m.maksajuma_datums,
                          m.maksajuma_veids
                   FROM Maksajumi m
                            JOIN Klienti k
                                 ON m.klienta_id = k.klienta_id
                   ORDER BY m.maksajuma_id
                   """)
    payments = cursor.fetchall()
    database.close()
    return payments


# ---------------------------------- MAINIT MAKSAJUMU ----------------------------------
def update_payment(payment_id, client_id, amount, payment_date, payment_method):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Maksajumi SET klienta_id = ?, summa = ?, maksajuma_datums = ?, maksajuma_veids = ? WHERE maksajuma_id = ?",
        (client_id, amount, payment_date, payment_method, payment_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST MAKSAJUMU ----------------------------------
def delete_payment(payment_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Maksajumi WHERE maksajuma_id = ?", (payment_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted


# ---------------------------------- PIEVIENOT INVENTARU ----------------------------------
def add_equipment(name, quantity, condition, purchase_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "INSERT INTO Inventars (nosaukums, daudzums, stavoklis, iegades_datums) VALUES (?,?,?,?)",
        (name, quantity, condition, purchase_date)
    )
    database.commit()
    equipment_id = cursor.lastrowid
    database.close()
    return equipment_id


# ---------------------------------- IZSAUKT INVENTARA SARAKSTU ----------------------------------
def get_equipment():
    database = connect()
    cursor = database.cursor()
    cursor.execute("SELECT inventara_id, nosaukums, daudzums, stavoklis, iegades_datums FROM Inventars")
    equipment = cursor.fetchall()
    database.close()
    return equipment


# ---------------------------------- MAINIT INVENTARU ----------------------------------
def update_equipment(equipment_id, name, quantity, condition, purchase_date):
    database = connect()
    cursor = database.cursor()
    cursor.execute(
        "UPDATE Inventars SET nosaukums = ?, daudzums = ?, stavoklis = ?, iegades_datums = ? WHERE inventara_id = ?",
        (name, quantity, condition, purchase_date, equipment_id)
    )
    database.commit()
    updated = cursor.rowcount
    database.close()
    return updated


# ---------------------------------- IZDZEST INVENTARU ----------------------------------
def delete_equipment(equipment_id):
    database = connect()
    cursor = database.cursor()
    cursor.execute("DELETE FROM Inventars WHERE inventara_id = ?", (equipment_id,))
    database.commit()
    deleted = cursor.rowcount
    database.close()
    return deleted
