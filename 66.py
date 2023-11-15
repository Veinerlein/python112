import sqlite3 as sq



with sq.connect('db4.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOR EXISTS Ware (
    ID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    Name,
    )
    """)

    # SELECT * FROM orders
    # ORDER    BY    Price    DESC    LIMIT 5 - кількість 5

    # SELECT * FROM orders
    # ORDER BY Price    DESC    LIMIT 5    OFFSET 2; - зіщення на 2 строки