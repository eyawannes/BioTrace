import sqlite3

def init_db():
    conn = sqlite3.connect("access_system.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        time TEXT,
        status TEXT,
        watermark TEXT
    )
    """)

    conn.commit()
    conn.close()


# ✅ Fonction add_user manquante
def add_user(name):
    conn = sqlite3.connect("access_system.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name) VALUES(?)", (name,))
    conn.commit()
    conn.close()