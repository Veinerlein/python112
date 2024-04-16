import sqlite3

def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
data_base = sqlite3.connect("simple_prepared_db.sqlite")  # підключив базу даних через змінну. (назва як шлях до
# програми бази даних яку я використовую)(із mySQL це буде "simple_prepared_db.mysql" )(запуск скрипту)
# в програмі sqlite додав файл, який зявиться після запуску скрипту

data_base.row_factory = dict_factory

# із MySQL потрібно вказати також логін, пароль, хост окрім назви самої бд в connect()

c = data_base.cursor()  # cursor method спеціальний об'єкт, з допомогою якого можна працювати із бд (створювати
# запроси і тд.)

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")  # Check if the table exists
table_exists = c.fetchone()
if not table_exists:  # Check if the table exists  хоча можна було прописати  CREATE TABLE IF NOT EXISTS users
    # замість 3 рядків коду вище, але не усі субд підтримують цю опцію
    c.execute("""CREATE TABLE users ( 
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
       )
        """)  # створений запрос до бази даних із SQL
# тобто банальна команда із мови структурних запитів

# Drop the old table
# c.execute("DROP TABLE users")

# Тоді створюю заново структуру (метод не підходить якщо є дані)

"""
 FOR MYSQL буде
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, AUTOINCREMENT)")
# CREATE TABLE Persons (
#     ID int NOT NULL AUTO_INCREMENT,
#     LastName varchar(255) NOT NULL,
#     FirstName varchar(255),
#     Age int,
#     PRIMARY KEY (ID)
# );
"""

# c.execute("INSERT INTO users (name, email) VALUES ('msr. Smith', 'Smith2@gmail.com') ")
# тільки готує дані до відправки

# коментую щоб повторно не відправляти запит, виникне помилка унікальності

# c.executescript("""
# INSERT INTO users (name, email) VALUES ('John Smith', 'John@gmail.com');
# INSERT INTO users (name, email) VALUES ('Nick Smith', 'Nick@gmail.com');
# """)  # метод для масового заповнення без постійного виклику c.execute() (також повторно не відправиться)

# spisok_kortejiv = [
#     ("user 1", "user1@gmail.com"),
#     ("user 2", "user2@gmail.com"),
#     ("user 3", "user3@gmail.com"),
# ]
# c.executemany(
#     "INSERT INTO users (name, email) VALUES (?, ?)", spisok_kortejiv)  # вставляє в запит цілу колекцію даних із списка кортежів

email_to_find = "user1@gmail.com"

'''c.execute(f"SELECT * FROM users WHERE email == '{email_to_find}'")''' # Ніколи не робити так, оскільки через такого типу

# c.execute("SELECT * FROM users WHERE email == ?", (email_to_find,))

# запит можна провести sql ін'єкцію
# щоб отримати дані із бд fetchone або fetchall
# fetchone повертає набір результатів запиту наступного рядка як tuple.

c.execute("SELECT * FROM users WHERE email == :email or name == :name", {'email':email_to_find,'name':'msr. Smith'})

our_select = c.fetchone() # 1 запис
our_select2= c.fetchall() # уся колекція (вказаний один користувач, можливо тому виводить останній збіг, тобто 5тий)

print(our_select) # (2, 'msr. Smith', 'Smith2@gmail.com')
print(our_select2) # [(5, 'user 1', 'user1@gmail.com')]  поверне у випадку
# якби не було використано # our_select = c.fetchone() # 1 запис
print("++++++++++++++")

c.execute("SELECT * FROM users")
print(c.fetchall())  # КОмбінація викликала і вивела усі записи
# zminna_dla_fetchall = c.fetchall()
# for zapis in c.fetchall():
#     print(zapis[1],"-",zapis[2])

"""Після того як команда fetchall() викликалась повторно її викликати не вийде, як і більшість команд робити із 
запитами СКЛ команду потрібно видаляти або закоментовувати"""

data_base.commit()  # для фіксації усіх змін
data_base.close()

print(type(email_to_find,))
print(type((email_to_find,)))
