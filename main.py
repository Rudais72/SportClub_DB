import sqlite3

def create_database():
    conn = sqlite3.connect("sport_club.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Klienti (
        klienta_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT,
        uzvards TEXT,
        tālrunis TEXT,
        epasts TEXT,
        registracijas_datums TEXT
    );

    CREATE TABLE IF NOT EXISTS Treneri (
        trenera_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT,
        uzvards TEXT,
        tālrunis TEXT,
        specializacija TEXT,
        pieņemšanas_datums TEXT
    );

    CREATE TABLE IF NOT EXISTS Grupu_Nodarbibas (
        nodarbibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT,
        apraksts TEXT,
        ilgums_minutēs INTEGER
    );

    CREATE TABLE IF NOT EXISTS Abonementi (
        abonementa_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klienta_id INTEGER,
        abonementa_veids TEXT,
        sakuma_datums TEXT,
        beigu_datums TEXT,
        FOREIGN KEY (klienta_id) REFERENCES Klienti(klienta_id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Grafiks (
        grafika_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nodarbibas_id INTEGER,
        trenera_id INTEGER,
        datums_laiks TEXT,
        telpa TEXT,
        FOREIGN KEY (nodarbibas_id) REFERENCES Grupu_Nodarbibas(nodarbibas_id),
        FOREIGN KEY (trenera_id) REFERENCES Treneri(trenera_id)
    );

    CREATE TABLE IF NOT EXISTS Rezervacijas (
        rezervacijas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klienta_id INTEGER,
        grafika_id INTEGER,
        rezervacijas_datums TEXT,
        FOREIGN KEY (klienta_id) REFERENCES Klienti(klienta_id),
        FOREIGN KEY (grafika_id) REFERENCES Grafiks(grafika_id)
    );

    CREATE TABLE IF NOT EXISTS Maksajumi (
        maksajuma_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klienta_id INTEGER,
        summa REAL,
        maksajuma_datums TEXT,
        maksajuma_veids TEXT,
        FOREIGN KEY (klienta_id) REFERENCES Klienti(klienta_id)
    );

    CREATE TABLE IF NOT EXISTS Inventars (
        inventara_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT,
        daudzums INTEGER,
        stāvoklis TEXT,
        iegades_datums TEXT
    );
    """)
    
    conn.commit()
    conn.close()