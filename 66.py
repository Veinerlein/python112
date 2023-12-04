import sqlite3 as sq

with sq.connect('Home_Shop.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM orders ORDER BY Price DESC LIMIT 2, 5
    """)

    # SELECT * FROM orders
    # ORDER    BY    Price    DESC    LIMIT 5 - кількість 5

    # SELECT * FROM orders
    # ORDER BY Price    DESC    LIMIT 5    OFFSET 2 - зіщення на 2 строки
    # SELECT * FROM orders
    # ORDER BY Price    DESC    LIMIT 2 ,5     - зіщення на 2 строки

    # SELECT    remarks from orders
    # WHERE    remarks    GLOB    '*1[5-9]*'    AND    remarks    LIKE "%case%"

    res = cur.fetchall()  # Виводить все, що запросили у списку кортежів
    print(res)

    for res in cur.execute("""SELECT * FROM orders ORDER BY Price DESC LIMIT 2, 5"""):
        print(res)

    res = cur.execute("""SELECT * FROM orders ORDER
    BY Price DESC LIMIT 2, 5""").fetchone()
    print(res)  # - вивів один  (перший) кортеж із даними.

    res = cur.execute("""SELECT * FROM orders ORDER 
    BY Price DESC LIMIT 2, 5""").fetchmany(2)
    print(res)  # кількість виведе в слід після попереднього виводу

with sq.connect('db5.db') as con:
    cur = con.cursor()
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS ClientGoods(
    # IDParty PRIMARY KEY,
    # ID INTEGER,
    # INNClient INTEGER,
    # CostUnit numeric,
    # Count integer,
    # Foreign KEY (INNClient) REFERENCES Client(INNClient),
    # Foreign Key (ID) REFERENCES SellerGoods (ID)
    # );
    # """)
    data = [
        (2016, "Cow", 'Shop'),
        (2017, "Dog", 'Home'),
        (2018, "Cat", 'Pet Store'),
        (2019, "Fish", 'Aquarium'),
        (2020, "Bird", 'Pet Shop'),
        (2021, "Hamster", 'Home'),
        (2022, "Rabbit", 'Pet Store'),
        (2023, "Turtle", 'Home'),
        (2024, "Snake", 'Pet Shop'),
        (2025, "Horse", 'Farm'),
        (2026, "Pig", 'Farm'),
        (2027, "Chicken", 'Farm'),
        (2028, "Sheep", 'Farm'),
        (2029, "Duck", 'Farm'),
        (2030, "Goat", 'Farm'),
        (2031, "Elephant", 'Zoo'),
        (2032, "Giraffe", 'Zoo'),
        (2033, "Lion", 'Zoo'),
        (2034, "Penguin", 'Zoo'),
        (2035, "Kangaroo", 'Zoo'),
        (2036, "Panda", 'Zoo'),
        (2037, "Monkey", 'Zoo'),
        (2038, "Squirrel", 'Park'),
        (2039, "Deer", 'Forest'),
        (2040, "Bear", 'Forest'),

    ]

    # cur.executemany("INSERT INTO Client(INN, Client,Status) VAlues(?,?,?)", data)
    data2 = [
        (105, 130, 2046, 23.1, 95),
        (107, 144, 2046, 7.25, 78),
        (111, 101, 2016, 8.9, 25),
        (113, 105, 2046, 12.5, 60),
        (115, 110, 2016, 9.75, 45),
        (117, 125, 2046, 15.3, 80),
        (120, 112, 2016, 10.2, 30),
        (123, 108, 2046, 18.7, 65),
        (128, 120, 2016, 11.8, 55),
        (130, 116, 2046, 14.6, 40),
        (135, 124, 2016, 9.0, 20),
        (138, 130, 2046, 17.2, 75),
        (142, 128, 2016, 12.3, 60),
        (145, 104, 2016, 13.5, 50),
        (150, 136, 2046, 11.2, 45),
        (155, 142, 2016, 16.8, 70),
        (160, 118, 2046, 9.7, 35)
    ]
    # cur.executemany("INSERT INTO ClientGoods (IDParty, ID, INNClient,CostUnit,Count) Values (?,?,?,?,?)", data2)

    data3 = [
        (1001, 'Animal brand', 'Agent'),
        (1007, 'Caramel', 'Manufacturer'),
        (1009, 'Sweets & Co.', 'Manufacturer'),
        (1015, 'Rainbow Inc.', 'Agent'),
        (1020, 'Delicious Treats', 'Manufacturer'),
        (1025, 'Tasty Treats Ltd.', 'Agent'),
        (1030, 'Sweet Delights', 'Manufacturer'),
        (1035, 'Candy Creations', 'Agent'),
        (1040, 'Sugar Rush Co.', 'Manufacturer'),
        (1045, 'Sweets Galore', 'Agent'),
        (1050, 'Flavors Unlimited', 'Manufacturer'),
        (1055, 'The Candy Shop', 'Agent'),
        (1060, 'Sweet Sensations', 'Manufacturer'),
        (1065, 'Joyful Confections', 'Agent'),
        (1070, 'Divine Desserts', 'Manufacturer'),
        (1075, 'Heavenly Sweets', 'Agent'),
        (1080, 'Sugar Bliss Co.', 'Manufacturer'),
        (1085, 'Yummy Goodies', 'Agent'),
        (1090, 'Delightful Treats', 'Manufacturer'),
        (1095, 'Sweet Symphony', 'Agent'),
        (1100, 'Candy Kingdom', 'Manufacturer'),
        (1105, 'Treats Haven', 'Agent'),
        (1110, 'Sugary Delights', 'Manufacturer'),
        (1115, 'Happy Sweets', 'Agent')
    ]
    # cur.executemany("INSERT INTO Seller (INNSeller,Seller,Status) VALUES (?,?,?)",data3)

    data4 = [
        (101, 145876876, 1007, '2007-11-10 00:00:00', "Candies", 1.8, 55),
        (102, 124587920, 1123, '2007-11-10 00:00:00', 'Artek waffles', 8.6, 65),
        (103, 136589723, 1050, '2007-11-11 00:00:00', 'Sweet Dreams', 5.4, 42),
        (104, 115487965, 1095, '2007-11-11 00:00:00', 'Delicious Bites', 6.2, 38),
        (105, 142369874, 1040, '2007-11-12 00:00:00', 'Heavenly Delights', 7.8, 50),
        (106, 128945612, 1105, '2007-11-12 00:00:00', 'Sugar Fantasy', 4.5, 30),
        (107, 137856924, 1065, '2007-11-13 00:00:00', 'Treats Paradise', 6.9, 48),
        (108, 121587490, 1110, '2007-11-13 00:00:00', 'Joyful Sweets', 5.7, 35),
        (109, 139874651, 1075, '2007-11-14 00:00:00', 'Divine Confections', 8.3, 60),
        (110, 118956387, 1085, '2007-11-14 00:00:00', 'Sugar Symphony', 7.1, 45),
        (111, 130478956, 1035, '2007-11-15 00:00:00', 'Delightful Treats', 6.5, 55),
        (112, 144856972, 1115, '2007-11-15 00:00:00', 'Happy Sweets', 4.9, 32),
        (113, 125689347, 1060, '2007-11-16 00:00:00', 'Sweet Symphony', 7.2, 40),
        (114, 141297856, 1080, '2007-11-16 00:00:00', 'Sugar Bliss', 6.4, 28),
        (115, 134852697, 1030, '2007-11-17 00:00:00', 'Delicious Dreams', 8.1, 50),
        (116, 120487965, 1055, '2007-11-17 00:00:00', 'Joyful Treats', 5.6, 36),
        (117, 128964731, 1120, '2007-11-18 00:00:00', 'Sweet Paradise', 6.8, 45),
        (118, 146587924, 1090, '2007-11-18 00:00:00', 'Candyland Delights', 4.3, 30),
        (119, 137856490, 1045, '2007-11-19 00:00:00', 'Sugar Fantasy', 7.7, 55),
        (120, 122369485, 1100, '2007-11-19 00:00:00', 'Divine Confections', 5.9, 42),
        (121, 139874650, 1070, '2007-11-20 00:00:00', 'Heavenly Sweets', 8.5, 60),
        (122, 118956384, 1083, '2007-11-20 00:00:00', 'Sweet Symphony', 6.1, 38),
        (123, 130478953, 1033, '2007-11-21 00:00:00', 'Treats Delight', 5.4, 48),
        (124, 144856979, 1117, '2007-11-21 00:00:00', 'Sugar Bliss', 7.3, 35),
        (125, 125689341, 1062, '2007-11-22 00:00:00', 'Sweet Delights', 6.5, 52),
        (126, 141297852, 1087, '2007-11-22 00:00:00', 'Candyland Symphony', 8.0, 44),
        (127, 134852693, 1037, '2007-11-23 00:00:00', 'Joyful Confections', 4.8, 30)
    ]

    # cur.executemany("INSERT INTO SellerGoods (ID,Code,INNSeller,DateStart,Goods,CostUnit,Count) Values (?,?,?,?,?,?,?)",
    #                 data4)

    # SELECT    Seller.Seller, SellerGoods.Goods
    # FROM    Seller, SellerGoods
    # WHERE    Seller.INNSeller = SellerGoods.INNSeller

    # SELECT    s.Seller, sg.Goods
    # FROM    Seller as s, SellerGoods as sg
    # WHERE    s.INNSeller = sg.INNSeller

    # SELECT    c.Client, s.Seller
    # FROM    SELLER    s, SellerGoods    sg, Client    c, ClientGoods cg
    # WHERE    s.INNSeller = sg.INNSeller    AND    sg.ID = cg.ID    AND    cg.INNClient = c.INNClient

    # SELECT    sg.CODE, sg.DateStart, sg.CostUnit, sg.Count, sg.Goods
    # FROM    SELLER    s, SellerGoods    sg, Client    c, ClientGoods    cg
    # WHERE    s.INNSeller = sg.INNSeller    AND    sg.ID = cg.ID    AND    cg.INNClient = c.INNClient
    # ORDER    BY    Goods    ASC

    # SELECT *
    # FROM    SELLER    s, SellerGoods    sg, Client    c, ClientGoods cg
    # WHERE    s.INNSeller = sg.INNSeller    AND    sg.ID = cg.ID    AND    cg.INNClient = c.INNClient    AND    s.Status = "Agent"    ORDER    BY    Goods    ASC

    # SELECT    s.INNSeller, sg.DateStart
    # FROM    SELLER    s, SellerGoods    sg, Client    c, ClientGoods cg
    # WHERE    s.INNSeller = sg.INNSeller    AND    sg.ID = cg.ID    AND    cg.INNClient = c.INNClient    AND    sg.DateStart    BETWEEN    '2007-11-10'    AND    '2007-11-11'

    # Дати по різному записуються у різних субд

"""AGREGATION FUNCTIONS"""
# - SUM - sum of data (only integer)
# - AVG  - avarage (only integer)
# - COUNT - quantity of wrotes (str and integer)
# - MIN - minimum (str and integer)
# - MAX -maximum (str and integer)

# SELECT COUNT (c.Client) as [amount quantyty]
# From Client c

# SELECT COUNT (s.Status) as Amount
# From Seller s
# Where Status = 'Agent'

# SELECT AVG (sg.Count*sg.CostUnit) as Amount
# From SellerGoods sg

# SELECT SUM (sg.Count*sg.CostUnit) as Amount
# From SellerGoods sg

# SELECT MAX (cg.Count), cg.ID,cg.INNClient,cg.IDParty
# From ClientGoods cg

# SELECT min(cg.Count * cg.CostUnit), cg.ID, cg.INNClient, cg.IDParty, c.Client
# From ClientGoodscg, Client c
# WHEREc.INNClient = cg.INNClient

# SELECT SUM (sg.Count*sg.CostUnit)
# From SellerGoods sg, Client c,Seller s, ClientGoods cg
# Where cg.INNClient=c.INNClient  AND c.STATUS LIKE '%Shop%' OR c.STATUS LIKE "%Store%"

# SELECT COUNT (sg.Goods)
# From SellerGoods sg
# WHERE Goods Like '%Waffles%'

# SELECT SUM (sg.Count)
# From SellerGoods sg, Client c, Seller s,ClientGoods cg
# WHERE sg.INNSeller = s.INNSeller AND cg.ID=sg.ID AND cg.INNClient=c.INNClient AND Goods Like '%Potato%' AND c.STATUS = 'Farm'

# SELECT COUNT (sg.Goods)
# FROM SellerGoods sg, Seller s
# WHERE sg.INNSeller=s.INNSeller AND s.Status = 'Agent'

# SELECT MIN (sg.CostUnit)
# FROM SellerGoods sg, Seller s

# SELECT MIN (cg.CostUnit*cg.Count)
# FROM SellerGoods sg, Seller s, ClientGoods cg

# SELECT MAX (sg.CostUnit*sg.Count)
# FROM SellerGoods sg, Seller s, ClientGoods cg, Client c
# WHERE sg.ID=cg.ID AND cg.INNClient=c.INNClient AND c.Client Like '%Shop%'

# SELECT Count (s.Status)
# FROM Seller s, Client c, SellerGoods sg, ClientGoods cg
# WHERE s.Status Like 'Manufacturer' AND s.INNSeller=sg.INNSeller AND sg.ID=cg.ID AND cg.INNClient=c.INNClient

# SELECT MIN (sg.Count*sg.CostUnit), sg.Goods
# FROM Seller s, SellerGoods sg
# WHERE s.Status Like 'Manufacturer' AND s.INNSeller=sg.INNSeller

# SELECT AVG (sg.CostUnit),sg.Goods
# FROM Seller s, SellerGoods sg
# WHERE sg.Goods LIKE "%Joyful%"

# SELECT MAX (sg.CostUnit*sg.Count), s.INNSeller
# FROM Seller s, SellerGoods sg
# WHERE s.STatus LIKE '%Agent%' AND s.INNSeller=sg.INNSeller

# SELECT MIN (sg.CostUnit*sg.Count)
# FROM Seller s, SellerGoods sg
# WHERE s.INNSeller=sg.INNSeller AND s.Status Like '%Agent%'

# SELECT continent, name, area FROM world x
#   WHERE area >= ALL
#     (SELECT area FROM world y
#         WHERE y.continent=x.continent
#           AND population>0)


# SELECT name
# FROM world
# WHERE GDP > ALL(SELECT GDP FROM world WHERE GDP > 0 AND continent = 'Europe')


# SELECT name,CONCAT(ROUND(population/(SELECT population from world WHERE name = 'Germany')*100),'%')
# FROM world
# WHERE continent = 'Europe'

# SELECT continent,MIN(name)
# FROM world
# GROUP BY continent ORDER BY name

# SELECT a.name, a.continent, a.population
# FROM world a
# WHERE a.population < ALL (
#     SELECT b.population
#     FROM world b
#     WHERE a.name <> b.name AND a.continent = b.continent
# );

# SELECT name,continent,population
# FROM world a
# WHERE  a.population < (SELECT MIN(b.population) FROM world b WHERE a.name<>b.name AND a.continent=b.continent)

# SELECT continent, SUM(population)
#   FROM world
#  GROUP BY continent
# HAVING SUM(population)>500000000
