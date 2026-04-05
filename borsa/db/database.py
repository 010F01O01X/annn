import sqlite3

DB_NAME = "db/app.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
        stock TEXT,
        lots INTEGER,
        avg_price REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        stock TEXT,
        action TEXT,
        price REAL,
        lots INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()