from db.database import connect

def add_stock(stock, lots, price):
    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO portfolio VALUES (?, ?, ?)", (stock, lots, price))

    conn.commit()
    conn.close()

def get_portfolio():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM portfolio")
    data = cur.fetchall()

    conn.close()
    return data