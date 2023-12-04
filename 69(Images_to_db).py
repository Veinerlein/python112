import sqlite3 as sq

# def read_avatar(n): # зчитування файлу із пам'яті
#     try:
#         with open(f"{n}.jpg", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):  # запис даних у вигляді графічних даних
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e) # що таке е
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row  # дані в стані ключ-значення
#     cur = con.cursor()
#     cur.executescript("CREATE TABLE IF NOT EXISTS users("
#                       "name TEXT,"
#                       "ava BLOB,"
#                       "score INTEGER"
#                       ")")
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava'] # зчитані дані із бази даних
#
#     # img = read_avatar('avatars') # прочитати та зберегти прочитане у змінну
#     # if img:
#     #     binary = sq.Binary(img)  # картинка для бази даних # зробити бінарний тип даних
#     #     cur.execute("INSERT INTO users VALUES ('Elon',?,1000)", (binary,))  # вставляю бінарне зображення у базу даних
#
#     write_ava('out.png', img) # дістав із бази даних файл і зберіг у графічний формат
"""
with sq.connect('cars.db') as con:
    cur = con.cursor()

    # with open('sql_dump.sql', 'w') as f: # створений бек ап
    #     for sql in con.iterdump():
    #         f.write(sql)

    with open('sql_dump.sql', 'r') as f:  # відновлення бази даних по збереженому бекапу
        sql = f.read()
        cur.executescript(sql)

    # for sql in con.iterdump(): # метод курсора, який повертає ітерацію всіх даних, що корисно для створення бекапу
    #     print(sql)

"""
data = [("car","Авто"),("house","дім"),("tree","дерево"),("color","колір")]
with sq.connect(':memory:') as con:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS dict
        (eng TEXT,
        ua TEXT
        )
        """)
        cur.executemany("INSERT INTO dict VALUES (?,?)", data)

        cur.execute("SELECT ua FROM dict WHERE eng LIKE 'c%'")
        print(cur.fetchall()) # [('Авто',), ('колір',)]


"""WSGI (WEB SERVER GATEWAY INTERFACE)"""



