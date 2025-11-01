import sqlite3

def crear_tabla():
    conn = sqlite3.connect("registro_users.db")
    cursor = conn.cursor()
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
