# SELECT Name, Prod FROM americans
# WHERE Name GLOB '[C-L]*'
# ORDER BY Name DESC

# SELECT Name, Prod FROM americans
# WHERE Name GLOB '[C-L]*'
# ORDER BY 1 DESC


# SELECT Name, SUM ,CNUM FROM americans
# WHERE Sum > 600 AND CNUM IN (2,7,15)

# SELECT Name, SUM ,CNUM FROM americans
# WHERE Sum > 600 AND (CNUM LIKE 45 or CNUM LIKE 13 or CNUM LikE 2)


# SELECT Name,Sum,CNUM FROM americans
# WHERE Sum > 600 AND (CNUM = 2 OR CNUM = 6)


# SELECT Name FROM americans
# WHERE Name BETWEEN 'A%' and 'J%' AND Prod is NOT 'Furniture'

# SELECT Name, cnum, Sum FROM americans
# WHERE Sum >700 AND CNUM not in (1,11,22,33,44,42,38);


# SELECT Name, Prod FROM americans
# WHERE Name BETWEEN 'A' AND 'J' AND Prod NOT LIKE 'Furniture'
# Order by Name DESC

# SELECT CNUM, City FROM Americans
# WHERE City in ('Omaha','New York')

# SELECT CNUM, City FROM Americans
# ORDER BY 1 DESC


# SELECT CNUM, name, City, city2 FROM Americans
# Where City LIKE 'New York' AND City2 NOT LIKE 'New York'


# SELECT Name, Meng_cod, CNUM FROM americans
# WHERE Meng_cod IN (112,113,114,115,116)
# ORDER BY 3 DESC
# (Name = 1
#  Meng_cod = 2
#  CNUM = 3)

import sqlite3 as sq

with sq.connect("users.db") as con:
    cur = con.cursor()
    # cur.execute("""
    # INSERT INTO person
    # VALUES (10, 'Bobly', '380674562345', 24, "sobaka@gmail.com")
    # """)
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT +380600000000,
    # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )
    # """)

    # ALTER TABLE person RENAME TO person_table
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT str

    # ALTER TABLE person_table RENAME COLUMN address to home

    # ALTER TABLE person_table
    #     DROP COLUMN home
    # DROP TABLE person_table

    # INSERT INTO імя_таблиці [(Вставляємий список стовпців)]
    # SELECT список_стовпців
    # FROM список_таблиць
    # WHERE умова

    # INSERT INTO employees2
    # SELECT ID, Name, Position, Experience, Salary
    # FROM employees
    # WHERE ID < 23 AND ID > 19

    # INSERT    INTO    employees2(ID, Name, Position, Experience)
    # SELECT    ID, Name, Position, Experience
    # FROM    employees
    # WHERE    ID > 29 AND ID < 32

    # INSERT    INTO employees4(ID, Name, Position, Experience, salary)
    # SELECT    ID, Name, position, experience, salary + 10000
    # FROM employees2
    # WHERE    salary < 50000

    # UPDATE імя_таблиці
    # SET стовпець1=слово, стовпець2=слово2
    # WHERE умова

    # UPDATE    employees2
    # SET    Salary = salary - 5000
    # WHERE    salary = 60000 AND    experience < 5

    # DELETE FROM шмя_таблиці
    # WHERE умова

    # DELETE from employees
    # WHERE    CAST(salary as TEXT) NOT LIKE  '%._'  - чомусь видалить саме по цьому шаблону

with sq.connect("Home_Shop.db") as con:
    curs = con.cursor()
    curs.execute("""
    CREATE TABLE IF NOT EXISTS orders(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRODUCE TEXT NOT NULL,
    MATERIAL TEXT NOT NULL,
    COLOR TEXT NOT NULL,
    SIZE TEXT,
    COUNTRY TEXT,
    ID_SALESPEOPLE TEXT,
    PRICE INTEGER,
    COUNT INTEGER NOT NULL,
    REMARKS TEXT
    )
    """)  # створення таблиці

    data = [
        (1026, 'F8E157eaLRG', 'Polyester / Neylon', 'Black', '38,1x28x70', 'Germany', 2014, 126, 0,
         'StoneStreet Case (15)'),
        (1049, 'KCB-03BKP', 'Leather', 'Black', '40x30x8,5', 'Germany', 2001, 325, 14, 'System Case (15)'),
        (1050, 'ABC123', 'Cotton', 'Blue', '36x24x60', 'France', 2005, 150, 8, 'Travel Bag (12)'),
        (1051, 'XYZ789', 'Canvas', 'Green', '45x32x75', 'Italy', 2008, 200, 10, 'Backpack (20)'),
        (1052, 'PQR456', 'Leather', 'Brown', '42x30x10', 'Spain', 2012, 280, 12, 'Executive Briefcase (18)'),
        (1053, 'JKL789', 'Nylon', 'Red', '32x20x50', 'Portugal', 2015, 180, 15, 'Weekender Bag (14)'),
        (1054, 'MNO123', 'Polyester / Cotton', 'Gray', '39x28x65', 'Germany', 2010, 240, 10, 'Rolling Duffel Bag (16)'),
        (1055, 'STU456', 'Leather', 'Blue', '34x22x55', 'France', 2018, 190, 8, 'Business Backpack (18)'),
        (1056, 'VWX789', 'Nylon', 'Red', '36x26x60', 'Italy', 2015, 200, 12, 'Weekender Bag (14)'),
        (1057, 'YZA123', 'Canvas', 'Black', '38x30x70', 'Spain', 2013, 260, 15, 'Travel Tote (22)'),
        (1058, 'BCD456', 'Polyester', 'Green', '42x32x75', 'Portugal', 2016, 180, 10, 'Backpack (20)'),
        (1059, 'EFG789', 'Leather', 'Brown', '40x28x65', 'Germany', 2017, 300, 18, 'Executive Briefcase (18)'),
        (1060, 'HIJ123', 'Nylon', 'Gray', '36x24x60', 'France', 2012, 210, 14, 'Rolling Duffel Bag (16)'),
        (1061, 'KLM456', 'Polyester', 'Blue', '34x22x55', 'Italy', 2014, 170, 8, 'Business Backpack (18)'),
        (1062, 'NOP789', 'Leather', 'Red', '38x30x70', 'Spain', 2019, 240, 12, 'Weekender Bag (14)'),
        (1063, 'QRS123', 'Canvas', 'Black', '42x32x75', 'Portugal', 2018, 260, 15, 'Travel Tote (22)'),
        (1064, 'TUV456', 'Nylon', 'Green', '40x28x65', 'Germany', 2015, 190, 10, 'Backpack (20)'),
        (1065, 'WXY789', 'Polyester / Cotton', 'Brown', '36x24x60', 'France', 2013, 220, 14, 'Rolling Duffel Bag (16)'),
        (1066, 'ZAB123', 'Canvas', 'Blue', '34x22x55', 'Italy', 2016, 180, 8, 'Business Backpack (18)'),
        (1067, 'CDE456', 'Leather', 'Red', '38x30x70', 'Spain', 2017, 280, 15, 'Weekender Bag (14)'),
        (1068, 'FGH789', 'Nylon', 'Black', '42x32x75', 'Portugal', 2014, 250, 12, 'Travel Tote (22)'),
        (1069, 'IJK123', 'Polyester', 'Green', '40x28x65', 'Germany', 2012, 200, 10, 'Backpack (20)'),
        (1070, 'LMN456', 'Leather', 'Brown', '36x24x60', 'France', 2018, 240, 14, 'Executive Briefcase (18)'),
        (1071, 'OPQ789', 'Canvas', 'Blue', '34x22x55', 'Italy', 2015, 170, 8, 'Business Backpack (18)'),
        (1072, 'RST123', 'Polyester', 'Red', '38x30x70', 'Spain', 2016, 260, 15, 'Weekender Bag (14)'),
        (1073, 'UVW456', 'Leather', 'Black', '42x32x75', 'Portugal', 2019, 280, 12, 'Travel Tote (22)'),
        (1074, 'WXY789', 'Nylon', 'Green', '40x28x65', 'Germany', 2017, 210, 10, 'Backpack (20)'),
        (1075, 'ZAB123', 'Polyester / Cotton', 'Brown', '36x24x60', 'France', 2015, 220, 14, 'Rolling Duffel Bag (16)'),
        (1076, 'CDE456', 'Canvas', 'Blue', '34x22x55', 'Italy', 2018, 180, 8, 'Business Backpack (18)'),
        (1077, 'FGH789', 'Leather', 'Red', '38x30x70', 'Spain', 2013, 280, 15, 'Weekender Bag (14)'),
        (1078, 'IJK123', 'Polyester', 'Black', '42x32x75', 'Portugal', 2012, 250, 12, 'Travel Tote (22)'),
        (1079, 'LMN456', 'Nylon', 'Green', '40x28x65', 'Germany', 2014, 200, 10, 'Backpack (20)'),
        (
            1080, 'OPQ789', 'Polyester / Cotton', 'Brown', '36x24x60', 'France', 2015, 240, 14,
            'Executive Briefcase (18)'),
        (1081, 'RST123', 'Leather', 'Blue', '34x22x55', 'Italy', 2017, 170, 8, 'Business Backpack (18)'),
        (1082, 'UVW456', 'Canvas', 'Red', '38x30x70', 'Spain', 2019, 260, 15, 'Weekender Bag (14)'),
        (1083, 'XYZ789', 'Nylon', 'Black', '42x32x75', 'Portugal', 2016, 280, 12, 'Travel Tote (22)'),
        (1084, 'ABC123', 'Polyester', 'Green', '40x28x65', 'Germany', 2014, 210, 10, 'Backpack (20)'),
        (1085, 'DEF456', 'Leather', 'Brown', '36x24x60', 'France', 2018, 240, 14, 'Rolling Duffel Bag (16)')
    ]  # дані для заповнення

    # curs.executemany(
    #     "INSERT INTO orders (ID,PRODUCE,MATERIAL,COLOR,SIZE,COUNTRY,ID_SALESPEOPLE,PRICE,COUNT,REMARKS) VALUES (?,?,"
    #     "?,?,?,?,?,?,?,?)", data)  # заповнення таблиці

    # INSERT INTO order2 (ID,PRODUCE,MATERIAL,COLOR,SIZE,COUNTRY,ID_SALESPEOPLE,PRICE,COUNT,REMARKS)
    # SELECT * FROM orders

    # UPDATE orders
    # SET country = 'Germany'
    # WHERE country = 'Portugal'

    # Insert into orders (ID,produce,material,color,size,country,id_salespeople,price,count,remarks)
    # Select * from order2
    # Where country = 'Portugale'

    # Select * FROM orders
    # Where    color is not 'Black'

    # INSERT    INTO orders(produce, material, color, size, country, id_salespeople, price, count, remarks)
    # VALUES ('NTC-117BK Micro Camera Case','Nylon','Black','13,3x8,3x5,7','Ukraine',2016, 150,0,1046)

    # SELECT    PRODUCE
    # FROM    ORDERS
    # WHERE    ID_SALESPEOPLE = 2014

    # SELECT    PRODUCE, PRIcE, MATERIAL
    # FROM    orders
    # WHERE    PRIcE between 200 and 345

    # SELECT    ID, Remarks, id_salespeople
    # from orders    where remarks    LIKE '% bag %'

    # SELECT    ID_salespeople, remarks, price, count
    # from orders    where
    # remarks    LIKE    '% bag %'    AND    count * price < 3000

    # SELECT *    from orders
    # WHERE    material = 'Leather' AND    count < 10    AND    count * price < 4000

    # SELECT *    from orders
    # where    material = 'Nylon' AND    price < 250

    # Update    orders
    # set    material = 'Canvas'
    # WHERE    material = 'Nylon' and price < 200

    # SELECT *    from orders
    # WHERE    material is 'Leather'    AND    remarks    LIKE    '%bad'    AND    color is 'Black'    AND country is 'France'

    # SELECT * from orders
    # where    remarks    like    '%bag%' and SIZE > 15

    # SELECT *    from orders where
    # remarks    like '%bag%' and color <> 'black'

    # Update    orders    set material = 'Polyester'
    # WHERE    ID in (1015, 1041, 1032, 1010) AND    Country = 'China'
