import sqlite3 as sq

# SELECT COUNT(DISTINCT sg.Goods)  DISTINCT для унікальних значень
# FROM Seller s, SellerGoods sg
# WHERE s.INNSeller = sg.INNSeller AND s.Status = 'Agent'

# (Альтернатива)
# SELECT COUNT(sg.Goods)
# FROM SellerGoods sg
# WHERE sg.INNSeller IN (
#     SELECT DISTINCT s.INNSeller
#     FROM Seller s
#     WHERE s.Status = 'Agent'
# );

# SELECT COUNT(DISTINCT sg.Goods)
# FROM SellerGoods sg
# WHERE sg.Goods LIKE '%Sugar%'


# SELECT AVG((sg.CostUnit*sg.Count)-(cg.CostUnit*cg.Count))
# FROM SellerGoods sg, ClientGoods cg
# WhERE sg.Goods LIKE '%Sweet%' AND sg.ID=cg.ID;


"""GROUP BY"""

data1 = [
    (2001, 'Hoffman', 'London', 1001, 100),
    (2002, 'Giovanni', 'Rome', 1003, 200),
    (2003, "Liu", "San Jose", 1002, 200),
    (2004, "Grass", "Berlin", 1002, 300),
    (2006, "Clements", "London", 1001, 100),
    (2007, "Pereira", "Rome", 1004, 100),
    (2008, "Cisneros", "San Jose", 1007, 300),
    (2009, "Karl", "Rome", 1000, 400)
]

with sq.connect('db6.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
    cnum INTEGER PRIMARY KEY,
    cname nvarchar(100),
    city nvarchar(100),
    snum INTEGER,
    rating INTEGER,
    FOREIGN KEY (snum) REFERENCES salespeople (snum)
    )
    """)

    # cur.executemany("""
    # INSERT INTO customers (cnum,cname,city,snum,rating) VALUES(?,?,?,?,?)
    # """, data1)

data2 = [
    (3001, 1007, 2008, 18.69, '1990-03-10 00:00:00'),
    (3002, 1004, 2007, 767.19, '1990-03-10 00:00:00'),
    (3003, 1001, 2001, 1900.1, '1990-03-10 00:00:00'),
    (3005, 1002, 2003, 5160.45, '1990-03-10 00:00:00'),
    (3006, 1007, 2008, 1098.16, '1990-03-10 00:00:00'),
    (3007, 1002, 2004, 1713.23, '1990-04-10 00:00:00'),
    (3008, 1001, 2006, 75.75, '1990-04-10 00:00:00'),
    (3009, 1003, 2002, 47.23, '1990-05-10 00:00:00'),
    (3010, 1002, 2004, 1309.95, '1990-06-10 00:00:00'),
    (3011, 1001, 2006, 9891.88, '1990-06-10 00:00:00'),
    (3012, 1000, 2009, 421.3, '1990-06-10 00:00:00')
]

with sq.connect('db6.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    onum INTEGER PRIMARY KEY,
    snum INTEGER,
    cnum INTEGER,
    amt FLOAT,
    odate DATETIME,
    Foreign Key (cnum) REFERENCES customers (cnum),
    Foreign Key (snum) REFERENCES salespeople(snum)
    )
    """)

    # cur.executemany("""
    # INSERT INTO orders (onum,snum,cnum,amt,odate) VALUES (?,?,?,?,?)
    # """, data2)

data3 = [
    (1000, 'Rikki', 0.89999997615814, 'Rome'),
    (1001, 'Peel', 0.11999999731779, 'London'),
    (1002, 'Serres', 0.1299999923163, 'San Jose'),
    (1003, 'Axelrod', 0.1000000149012, 'New York'),
    (1004, 'Motika', 0.10999999940395, 'London'),
    (1007, 'Rifkin', 0.15000000596046, 'Barcelona')
]

with sq.connect('db6.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS salespeople (
    snum INTEGER PRIMARY KEY,
    sname NVARCHAR(100),
    com REAL,
    city NVARCHAR (100)
    )
    """)

    # cur.executemany(
    #     """INSERT INTO salespeople(snum,sname,com,city) VALUES(?,?,?,?)""", data3
    # )

# SELECT c.cname
# FROM customers c, orders o
# WHERE c.cnum = o.cnum
# GROUP BY c.cname

# SELECT c.cname
# FROM customers c, salespeople s
# WHERE c.snum = s.snum AND c.city not LIKE s.city
# GROUP BY c.cname

# SELECT MAX(c.rating), city
# FROM customers c
# GROUP BY c.city

# SELECT SUM(o.amt), city
# FROM customers c, orders o
# WHERE c.cnum=o.cnum
# GROUP BY c.city

# SELECT COUNT (s.sname)
# FROM salespeople s
# GROUP BY s.city

# SELECT MAX (c.rating),s.sname
# FROM salespeople s, customers c
# WHERE s.snum=c.snum
# GROUP BY s.sname


# SELECT MAX(o.amt)
# FROM orders o, customers c
# WHERE o.cnum=c.cnum
# GROuP BY c.cname
# HAVING o.amt>3000

# (Альтернатива)
# SELECT MAX(o.amt)
# FROM orders o, customers c
# WHERE o.cnum=c.cnum AND o.amt>3000
# GROuP BY c.cname

# SELECT s.sname, o.amt
# FROM salespeople s, orders o
# WHERE s.snum=o.snum AND s.sname = 'Rifkin'


# SELECT s.com
# FROM Salespeople s, Customers c
# WHERE s.snum = c.snum AND c.city LIKE 'Rome';
#
# SELECT com FROM salespeople
# WHERE snum in (SELECT snum FROM customers WHERE city = 'Rome')

# SELECT sname
# FROM salespeople
# WHERE snum IN (
#     SELECT snum
#     FROM customers
#     GROUP BY snum
#     HAVING AVG(rating) > (SELECT AVG(rating) FROM customers)
# );


# SELECT MIN(com), s.sname
# FROM salespeople s
# GROUP By s.sname
# HavING MIN(s.com) IN (SELECT MIN(com)FROM salespeople)

# SELECT *
# FROM orders
# WHERE snum = (SELECT snum FROM customers WHERE cname = 'Liu')

# (Альтернатива)
# SELECT *
# FROM orders o, customers c
# WHERE o.snum=c.snum AND cname = 'Liu'

# SELECT MAX(com) FROM salespeople
# WHERE snum = (SELECT snum from customers WHERE city = 'Rome')
#
# SELECT cname
# FROM customers
# WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Motika')
#
# SELECT MAX(rating)
# FROM customers
# WHERE snum in (SELECT snum FROM salespeople WHERE com > 0.11)

datas1 = [
    (1, 'Differential equals', '2008-01-03 00:00:00', 4),
    (1, 'Foreign language',None, None),
    (1, 'Mathematics analise', '2008-01-09 00:00:00', 3),
    (2, 'Mathematics analise', '2008-01-09 00:00:00', 5),
    (2, 'Sociology', '2008-01-06 00:00:00', 4),
    (2, 'Theory of information', '2008-01-03 00:00:00', 4),
    (3, 'Politology', '2008-01-06 00:00:00', 5),
    (3, 'Philosophy', '2008-01-09 00:00:00', 5),
    (4, 'Analitic Geometry', '2008-01-09 00:00:00', 5),
    (4, 'Foreign language', '2008-01-06 00:00:00', 5),
    (4, 'Quantum mechanic', '2008-01-03 00:00:00', 4),
    (5, 'Differential equels', '2008-01-03 00:00:00', 5),
    (5, 'Maintanence OS', '2008-01-06 00:00:00', 5),
    (5, 'Ukrainian language', '2008-01-09 00:00:00', 4),
    (6, 'Politology', '2008-01-06 00:00:00', 4),
    (6, 'Philosophy', '2008-01-09 00:00:00', 3),
    (7, 'Analitic Geometry', '2008-01-09 00:00:00', 3),
    (7, 'Foreign language',None,None),
    (7, 'Quantum mechanic', '2008-01-03 00:00:00', 5)
]

with sq.connect("db7.db") as con:
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS exam (
        ID_st SMALLINT,
        Predmet NVARCHAR(50),
        Data DATETIME,
        Ball SMALLINT,
        PRIMARY KEY (ID_st,Predmet),
        FOREIGN KEY (ID_st) REFERENCES Student (ID_st),
        FOREIGN KEY (ID_st) REFERENCES Student (ID_Students)
        )"""
    )

    # cur.executemany(
    #     """INSERT INTO exam (ID_st,Predmet,Data,Ball) VALUES (?,?,?,?)""", datas1
    # )

datas2 = [
    ('FM151', 'Informatic room'),
    ('FM153', 'Mathematic room'),
    ('FT151', 'Technological room'),
    ('FT152', 'Technological room'),
    ('FT252', 'Phisics room')
]

with sq.connect("db7.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS G (
    Groups NVARCHAR (50) PRIMARY KEY,
    Kafedra NVARCHAR (50),
    FOREIGN KEY (Kafedra) REFERENCES Kafedra (Kafedra)
    )
    """)

    # cur.executemany("""
    # INSERT INTO G(Groups,Kafedra) VALUES (?,?)
    # """, datas2)

datas3 = [
    ('Informatic room', 'Phisics-mathematics'),
    ('Mathematic room', 'Phisics-mathematics'),
    ('Technological room', 'Phisics Technique'),
    ("Phisics", 'Phisics Technique')
]

with sq.connect('db7.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Kafedra (
    Kafedra NVARCHAR (50) PRIMARY KEY,
    DECANAT NVARCHAR (50)
    )
    """)
    # cur.executemany("INSERT INTO Kafedra("
    #                 "Kafedra, Decanat) VALUES (?,?)",datas3)


datas4 = [
    (1, 'Alex VAS', 'FM151', 'Mathematic and OS'),
    (2, ' OGA Stens', 'FM151', 'Mathematic and OS'),
    (3, 'Sergio Mikel', 'FT151', 'Technology of cars'),
    (4, 'Anto Antony', 'FT252', 'Building'),
    (5, 'Anjelika Edvardo', 'FM153', 'IT'),
    (6, 'Andy Serjio', 'FT152', 'Building'),
    (7, 'Stenly Ann', 'FT152', 'Buildings')
]

with sq.connect("db7.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Student(
    ID_st SMALLINT PRIMARY KEY,
    NSM NVARCHAR (50),
    GROUPS NVARCHAR(50),
    SPECIAL NVARCHAR(50),
    FOREIGN KEY (GROUPs) REFERENCES G(GROUPs)
    )
    """)
    # cur.executemany("""
    # INSERT INTO Student (ID_st, NSM,Groups, Special) VALUES(?,?,?,?)
    # """, datas4)




datas5 = [
    (1, 345852),
    (2, 345851),
    (3, 124589),
    (4, 144456),
    (5, 345853),
    (6, 124653),
    (7, 144450)
]

with sq.connect('db7.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Zalik (
    Id_Students SMALLINT PRIMARY KEY,
    N_Z INTEGER
    )
    """)

    # cur.executemany("INSERT INTO Zalik (Id_Students,N_Z)VALUES (?,?)",datas5)


# SELECT NSM FROM student s
# WHERE s.NSM in (SELECT NSM FROM Student WHERE GROUPS in (SELECT GROUPS FROM G WHERE Kafedra in (SELECT Kafedra FROM Kafedra WHERE Decanat = 'Phisics-mathematics')));

# (Альтернатива)
# SELECT NSM
# FROM student
# WHERE Groups in (
#         SELECT Groups FROM G
#         WHERE kafedra in (
#         SELECT Kafedra FROM Kafedra
#         WHERE decanat LIKE 'Phisics-mathematics'))




# SELECT Kafedra FROM G
# WHERE Groups in (SELECT GROUPS FROM Student WHERE ID_St in (SELECT ID_st
# FROM exam WHERE Predmet LIKE "Sociology" ))



# SELECT  s.NSM,g.Kafedra
# FROM G g, Student s
# WHERE s.GROUPS=g.Groups
# ORDER BY s.NSM

# (Альтернатива)
# SELECT s.NSM,
# (SELECT Kafedra FROM G g WHERE s.GROUPS = g.Groups )
# FROM Student s
# ORDER BY NSM

# SELECT N_Z FROM Zalik z
# WHERE ID_Students in (SELECT ID_st FROM Student WHERE GROUPS IN(
# SELECT GROUPS FROM G WHERE Kafedra in (SELECT KAFEDRA FROM KAFEDRA WHERE DECANAT =
# "Phisics-mathematics")) )

# SELECT Z.N_Z, S.NSM
# FROM Zalik Z
# JOIN Student S ON Z.Id_Students = S.ID_st
# WHERE S.GROUPS IN (
#     SELECT G.Groups
#     FROM G
#     WHERE G.Kafedra IN (
#         SELECT K.Kafedra
#         FROM Kafedra K
#         WHERE K.DECANAT = 'Phisics-mathematics'
#     )
# );

# SELECT s.NSM
# FROM Student s
# WHERE ID_st in (SELECT ID_st FROM exam WHERE BALL = 5 AND Predmet LIKE 'Foreign Language')

# SELECT COUNT(DISTINCT Predmet)
# FROM exam

# SELECT AVG(Ball)
# FROM exam
# WHERE ID_st  = (SELECT ID_st FROM Student WHERE NSM LIKE '%OGA%')

# SELECT COUNT(NSM) , special
# FROM Student
# GROUP BY Special


# SELECT GROUPS
# FROM  G
# WHERE Kafedra  in (SELECT Kafedra FROM Kafedra WHERE Decanat = 'Phisics Technique')





