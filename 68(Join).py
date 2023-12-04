# Where EXISTS (SELECT c.cnum FROM Customers c WHERE c.cnum=o.cnum AND c.cname = 'Cisneros')

# SELECT c.cname
# FROM customers c, salespeople s
# WHERE c.city <> s.city AND c.snum=s.snum

# (Альтернатива)
# SELECT c.cname
# FROM customers c
# WHERE c.snum in (SELECT snum FROM salespeople WHERE c.city<>city)

# SELECT MAX(c.rating), c.city
# FROM customers c
# GROUP BY c.city

# SELECT SUM(o.amt), c.city
# FROM orders o, customers c
# WHERE c.snum=o.snum
# GROUP BY c.city

# SELECT COUNT(s.sname), s.city
# FROM salespeople s
# GROUP BY s.city

# SELECT MAX(c.rating),s.city
# FROM customers c, salespeople s
# WHERE c.snum=s.snum
# GROUP BY s.sname

# SELECT MAX(o.amt), c.cname
# FROM orders o, customers c
# WHERE o.snum=c.snum AND o.amt > 3000
# GROUP BY c.cname

# SELECT MIN(o.amt), o.odate
# FROM orders o
# GROUP BY o.odate
# ORDER BY o.odate DESC

# SELECT MAX(o.amt), o.snum
# FROM orders o
# WHERE  o.amt>3000
# GROUP BY o.snum

# (Альтернатива)
# SELECT snum, MAX(amt)
# FROM orders
# GROUP BY snum
# HAVING MAX (amt) > 3000


# SELECT  'For the city ' || s.city as City,'Max reting is ' || MAX(c.rating) as Rating
# FROM customers c, salespeople s
# WHERE s.snum = c.snum
# GROUP BY s.city;

# SELECT  SUM (o.amt), o.odate
# FROM orders o
# GROUP BY o.odate

# SELECT SUM(o.amt), c.snum
# FROM orders o, customers c
# WHERE o.snum = c.snum
# GROUP BY c.snum
# HAVING SUM(o.amt) > 10000

# SELECT SUM(o.amt)
# FROM orders o, customers c
# WHERE o.cnum=c.cnum
# GROUP BY c.snum
# HAVING SUM(o.amt) > 10000

# SELECT s.sname, SUM(o.amt)
# FROM salespeople s, orders o
# WHERE s.snum = o.snum
# GROUP BY s.sname

# SELECT c.cname, SUM(o.amt)
# FROM orders o, customers c
# WHERE o.cnum = c.cnum
# GROUP BY c.cname

"""49"""
# SELECT * FROM orders
# WHERE snum in (SELECT snum FROM Customers WHERE cname='Cisneros')

# (Альтернатива) - вибрати все що існує для значення в дужках для екзіст
# SELECT * FROM orders o

# SELECT s.sname
# FROM salespeople s, customers c
# WHERE c.snum=s.snum AND c.rating  = 300

# (Альтернатива)
# SELECT s.sname
# FROM salespeople s
# WHERE s.snum in (SELECT snum FROM customers WHERE rating = 300)

# SELECT sname, snum
# FROM salespeople s
# WHERE EXISTS (SELECT c.snum FROM customers c WHERE c.snum <> s.snum AND c.city = s.city)

"""UNION"""
# SELECT s.sname
# FROM salespeople s
# WHERE s.city = 'London'
# UNION - обєднання всього (Поля повинні бути одного типу)
# SELECT c.cname
# FROM customers c
# WHERE c.city = 'London'

# SELECT s.snum,s.city
# FROM salespeople s
# UNION ALL - Включно із повтореннями
# SELECT c.snum,c.city
# FROM customers c

# SELECT c.cname || ' Low rating',c.city, c.rating
# FROM customers c
# WHERE c.rating<200
# UNION
# SELECT c.cname || ' High rating',c.city, c.rating
# FROM customers c
# WHERE c.rating>=200


# (Альтернатива  )
# SELECT cnum,city,rating, 'High rating'
# FROM customers
# WHERE rating >=200
# UNION
# SELECT cnum,city,rating, 'Low rating'
# FROM customers
# WHERE rating <200

# SELECT c.cname, s.sname
# FROM customers c INNER JOIN salespeople s
# where c.snum = s.snum

# SELECT c.cname, o.*
# FROM customers c, orders o
# WHERE c.snum=o.snum
# ORDER BY c.cname

# SELECT c.cname, o.*
# FROM customers c RIGHT JOIN orders o ON o.cnum = c.cnum
# ORDER BY c.cname


import sqlite3 as sq

cars = [
    ('BMW', 54000),
    ('Lincoln', 46000),
    ('ZAZ', 6000),
    ('FIAT', 16000),
    ('Hyundai', 36000),
]

with sq.connect('cars.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER
    )
    """)

    # cur.execute("INSERT INTO cars  Values(1,'Renault',22000)")
    # cur.execute("INSERT INTO cars  Values(2,'Volvo',29000)")
    # cur.execute("INSERT INTO cars  Values(3,'Marcedes',62000)")
    # cur.execute("INSERT INTO cars  Values(4,'Bentley',222000)")
    # cur.execute("INSERT INTO cars  Values(5,'AUDI',42000)")

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES (NULL,?,?)",car)

    # cur.executemany('INSERT INTO cars VALUES(NULL,?,?)', cars)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0}) # другий параметр довомагає
    # визначити параметр PRICE

    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE "B%";
    # UPDATE cars SET Price =  price + 100;
    # """) # знаки недопустимі (?)

# con.commit() - save changes to db (no need in with..as..)
# con.close() - close db

# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES (NULL, 'Renault', 22000);
#     UPDATE cars SET price = price+100;
#     """) # rollback поверне до begin у разі помилки, BEGIN у своїй силі точка збереження
#     con.commit()
# except sq.Error as e:
#     if con :
#         con.rollback() # при виникненні помилки відкотить зміни до бази даних
#     print('Error of request')
# finally:
#     if con:
#         con.close()
#

# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost (
#     name TEXT, tr_in INTEGER, buy INTEGER
#     );
#
#     """) # тільки в executescript можна писати більше 1 запиту
#
#     cur.execute('INSERT INTO cars VALUES (NULL, "VAZ", 1000)')
#     last_row_id = cur.lastrowid # id останнього запису самої таблиці
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES ('Elon',?,?)", (last_row_id,buy_car_id))

# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row # данні в стані ключ-значення
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#     cur.execute("SELECT model,price FROM cars")
#
#     # rows1 = cur.fetchall() # показати рядки усі
#     # print(rows1)
#
#     # rows2 = cur.fetchone() # показати тільки 1 рядок
#     # print(rows2)
#
#     # rows3 = cur.fetchmany(5) # показати певну кількість рядків
#     # print(rows3)
#
#     for res in cur:
#         print(res['model'], res ['price'])

def read_avatar(n):
    try:
        with open(f"{n}.jpg", 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sq.connect("cars.db") as con:
    con.row_factory = sq.Row # данні в стані ключ-значення
    cur = con.cursor()
    cur.executescript("CREATE TABLE IF NOT EXISTS users("
                "name TEXT,"
                "ava BLOB,"
                "score INTEGER"
                ")")

    img = read_avatar('avatars')
    if img:
        binary = sq.Binary(img) # картинка для бази даних
        cur.execute("INSERT INTO users VALUES ('Elon',?,1000)", (binary,))# вставляю зображення у базу даних

