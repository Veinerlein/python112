site = 'https://disk.yandex.ru/dMoyZgh5AIGaZ3g'

import sqlite3 as sq

"""
con = sq.connect("profile.db")  # створення об'єкта
cur = con.cursor()  # елемент для працездатності цієї конструкції бази даних
cur.execute("""
"DROP TABLE 'users'"
""")  # призначений для введення запитів
con.close()
"""
#
#
#

with sq.connect("profile_main.db") as con:  # створення об'єкта
    cur = con.cursor()  # елемент для працездатності цієї конструкції бази даних
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, summa REAL, 
        data TEXT)
            """)  # призначений для введення запитів

clases_SQlite = ['NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB']

# Primary kay : суррогатний чи логічний


# SELECT [ALL | DISTINCT ]
# FROM tablename


# SELECT DISTINCT position FROM players - усі позиції, унікальні виведе

# BETWEEN - діапузон
# LIKE - шаблон
# % - люба кількість символів
# _  - любий символ

# GLOB - чи відповідає строка певному регуляр вираженню (тільки у sqlite3)
# * - любий символ
# ? - один символ
# . - один символ
# [abc] - любий одиничний символ
# [a-z] - заданий діапазон
# [^0-9] - що не входить у список
# SELECT * FROM players WHERE full_name GLOB "[AO]*"
# IS BULL - всі строки, стовпці яких мають значенн NULL


with  sq.connect("American_prez.db") as con:
    con.cursor().execute("CREATE TABLE IF NOT EXISTS americans(CNUM INT PRIMARY KEY,    Name TEXT,    City TEXT,"
                         "Rating INT,    Meng_cod INT,    Sum REAL,    City2 TEXT,    Prod TEXT,Rem TEXT)")

    # con.cursor().executemany("""INSERT INTO americans (CNUM, Name, City, Rating, Meng_cod, Sum, City2,
    # Prod,
    # Rem) VALUES(?,?,?,?,?,?,?,?,?)""", [
    #     (1, 'Joe Biden', 'Scranton', 5, 101, 600, 'Washington, D.C.', 'Books', 'Description 1'),
    #     (2, 'Donald Trump', 'New York', 4, 102, 550, 'Los Angeles', 'Electronics', 'Description 2'),
    #     (3, 'Barack Obama', 'Honolulu', 3, 103, 700, 'Chicago', 'Clothing', 'Description 3'),
    #     (4, 'George W. Bush', 'New Haven', 4, 104, 600, 'Houston', 'Furniture', 'Description 4'),
    #     (5, 'Bill Clinton', 'Hope', 5, 105, 800, 'Little Rock', 'Appliances', 'Description 5'),
    #     (6, 'George H. W. Bush', 'Milton', 3, 106, 550, 'Houston', 'Sports Equipment', 'Description 6'),
    #     (7, 'Ronald Reagan', 'Tampico', 4, 107, 750, 'Los Angeles', 'Home Decor', 'Description 7'),
    #     (8, 'Jimmy Carter', 'Plains', 5, 108, 620, 'Atlanta', 'Outdoor Gear', 'Description 8'),
    #     (9, 'Gerald Ford', 'Omaha', 3, 109, 580, 'Detroit', 'Tools', 'Description 9'),
    #     (10, 'Richard Nixon', 'Yorba Linda', 4, 110, 700, 'San Francisco', 'Garden Supplies', 'Description 10'),
    #     (11, 'Lyndon B. Johnson', 'Stonewall', 5, 111, 540, 'Austin', 'Toys', 'Description 11'),
    #     (12, 'John F. Kennedy', 'Brookline', 4, 112, 680, 'Boston', 'Electronics', 'Description 12'),
    #     (13, 'Dwight D. Eisenhower', 'Denison', 5, 113, 720, 'Gettysburg', 'Clothing', 'Description 13'),
    #     (14, 'Harry S. Truman', 'Lamar', 3, 114, 590, 'Independence', 'Furniture', 'Description 14'),
    #     (15, 'Franklin D. Roosevelt', 'Hyde Park', 4, 115, 780, 'Albany', 'Appliances', 'Description 15'),
    #     (16, 'Herbert Hoover', 'West Branch', 5, 116, 600, 'Stanford', 'Sports Equipment', 'Description 16'),
    #     (17, 'Calvin Coolidge', 'Plymouth', 4, 117, 650, 'Northampton', 'Home Decor', 'Description 17'),
    #     (18, 'Warren G. Harding', 'Blooming Grove', 5, 118, 670, 'Marion', 'Outdoor Gear', 'Description 18'),
    #     (19, 'Woodrow Wilson', 'Staunton', 3, 119, 620, 'Washington, D.C.', 'Tools', 'Description 19'),
    #     (20, 'William Howard Taft', 'Cincinnati', 4, 120, 730, 'Washington, D.C.', 'Garden Supplies', 'Description 20'),
    #     (21, 'Theodore Roosevelt', 'New York City', 5, 121, 560, 'Oyster Bay', 'Toys', 'Description 21'),
    #     (22, 'William McKinley', 'Niles', 4, 122, 690, 'Canton', 'Electronics', 'Description 22'),
    #     (23, 'Grover Cleveland', 'Caldwell', 5, 123, 640, 'Princeton', 'Clothing', 'Description 23'),
    #     (24, 'Benjamin Harrison', 'North Bend', 3, 124, 610, 'Indianapolis', 'Furniture', 'Description 24'),
    #     (25, 'Chester A. Arthur', 'Fairfield', 4, 125, 720, 'Albany', 'Appliances', 'Description 25'),
    #     (26, 'James A. Garfield', 'Moreland Hills', 5, 126, 550, 'Cleveland', 'Sports Equipment', 'Description 26'),
    #     (27, 'Rutherford B. Hayes', 'Delaware', 4, 127, 600, 'Columbus', 'Home Decor', 'Description 27'),
    #     (28, 'Ulysses S. Grant', 'Point Pleasant', 5, 128, 670, 'Galena', 'Outdoor Gear', 'Description 28'),
    #     (29, 'Andrew Johnson', 'Raleigh', 3, 129, 580, 'Greenville', 'Tools', 'Description 29'),
    #     (30, 'Abraham Lincoln', 'Hardin County', 4, 130, 750, 'Springfield', 'Garden Supplies', 'Description 30'),
    #     (31, 'James Buchanan', 'Cove Gap', 5, 131, 620, 'Lancaster', 'Clothing', 'Description 31'),
    #     (32, 'Franklin Pierce', 'Hillsborough', 4, 132, 700, 'Concord', 'Electronics', 'Description 32'),
    #     (33, 'Millard Fillmore', 'Summerhill', 5, 133, 590, 'Buffalo', 'Toys', 'Description 33'),
    #     (34, 'Zachary Taylor', 'Barboursville', 3, 134, 680, 'Louisville', 'Furniture', 'Description 34'),
    #     (35, 'James K. Polk', 'Pineville', 4, 135, 600, 'Nashville', 'Appliances', 'Description 35'),
    #     (36, 'John Tyler', 'Charles City County', 5, 136, 780, 'Richmond', 'Sports Equipment', 'Description 36'),
    #     (37, 'William Henry Harrison', 'Charles City County', 4, 137, 540, 'Indianapolis', 'Home Decor',
    #      'Description 37'),
    #     (38, 'Martin Van Buren', 'Kinderhook', 5, 138, 750, 'Albany', 'Clothing', 'Description 38'),
    #     (39, 'Andrew Jackson', 'Waxhaws', 3, 139, 620, 'Nashville', 'Outdoor Gear', 'Description 39'),
    #     (40, 'John Quincy Adams', 'Braintree', 4, 140, 670, 'Boston', 'Tools', 'Description 40'),
    #     (41, 'James Monroe', 'Monroe Hall', 5, 141, 600, 'Richmond', 'Garden Supplies', 'Description 41'),
    #     (42, 'James Madison', 'Port Conway', 4, 142, 720, 'Orange', 'Furniture', 'Description 42'),
    #     (43, 'Thomas Jefferson', 'Shadwell', 5, 143, 550, 'Charlottesville', 'Electronics', 'Description 43'),
    #     (44, 'John Adams', 'Braintree', 3, 144, 600, 'Quincy', 'Toys', 'Description 44'),
    #     (45, 'George Washington', 'Westmoreland County', 4, 145, 670, 'Mount Vernon', 'Colonial Goods',
    #      'Description 45')
    # ])

    all = con.cursor().execute("SELECT Name from americans").fetchall()
    print(all)
    for each in enumerate(all, 1):
        print(f"{each[0]} {each[1][0]}")

    all2 = con.cursor().execute("SELECT City2 from americans")
    for a in all2:
        print(a[0])

    all3 = con.cursor().execute("SELECT City from americans")
    for a in all3:
        print(f"Living in {a[0]}")

    all4 = con.cursor().execute("SELECT * from americans WHERE Cnum is '45'")
    for a in all4:
        print(f"45 president is not {a}")

    all5 = con.cursor().execute("SELECT * FROM americans WHERE Rating = 3")
    for a in all5:
        print(a)

    all6 = con.cursor().execute("SELECT City2 FROM americans Where Prod is 'Furniture'")
    for a in all6:
        print(a)

    all7 = con.cursor().execute("SELECT * FROM americans WHERE Sum > 700")
    for a in all7:
        print(a)

    all8 = con.cursor().execute("SELECT * FROM americans WHERE Sum>700 and City <> 'Port Conway'")
    for a in all8:
        print("JC", a)

    all9 = con.cursor().execute("SELECT Name FROM americans WHERE City <> City2")
    for a in all9:
        print('City1-2', a)

    all11 = con.cursor().execute("SELECT CNUM FROM americans WHERE Rating < '4' or Rating > '4'")
    for a in all11:
        print('Rating', a[0])

    all12 = con.cursor().execute("SELECT Name FROM americans WHERE Prod is 'Furniture'")
    for a in all12:
        print("Furniture", a)

    all13 = con.cursor().execute("SELECT Name FROM americans WHERE Name LIKE '%a%a%'")
    for a in all13:
        print('LIKE', a)

    all14 = con.cursor().execute("SELECT CNUM,Name FROM americans WHERE Name LIKE 'W%'")
    for a in all14:
        print('CNUM', a[0], a[1])

    all15 = con.cursor().execute("SELECT CNUM, City FROM americans WHERE Prod is 'Furniture' AND City is 'Lamar'")
    for a in all15:
        print("Furn", a)

    all16 = con.cursor().execute("SELECT Name FROM americans WHERE Sum > 700")
    for a in all16:
        print("SUM", a)

import sqlite3
import random

# З'єднання з базою даних (створення або підключення)
with sqlite3.connect("db3.db") as con:
    # Створення таблиці "employees"
    # con.cursor().execute("""
    # DROP TABLE employees""")
    con.cursor().execute("""
        CREATE TABLE IF NOT EXISTS employees (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Position TEXT,
            Experience INTEGER,
            Salary REAL
        )
    """)
    #
    # Заповнення таблиці даними (рандомні дані)
    names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", 'john',
             'Monica', 'Ivy', 'Paolo', 'Zuck']
    positions = ["Manager", "Engineer", "Technician", "Analyst", "Operator"]

    for i in range(1, 32):  # Додамо 10 працівників
        name = random.choice(names)
        position = random.choice(positions)
        experience = random.randint(1, 10)
        salary = round(random.uniform(30000, 80000),
                       2)  # Рандомне значення від 30000 до 80000 з двома знаками після коми

        con.cursor().execute("INSERT INTO employees (ID,Name, Position, Experience, Salary) VALUES (?,?, ?, ?, ?)",
                             (i,name, position, experience, salary))
