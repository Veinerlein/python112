import sqlite3
import random

# Підключення до бази даних (якщо не існує, то вона створиться)
with sqlite3.connect('ukraine_national_team.db') as sq:


    # Створення курсора для виконання SQL-запитів
    cursor = sq.cursor()

# Створення таблиці
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    ''')

    # Імена та позиції гравців
    players_data = [

        ('Andriy Yarmolenko', 'Forward', random.randint(500000, 1000000)),
        ('Oleksandr Zinchenko', 'Midfielder', random.randint(600000, 1200000)),
        ('Roman Yaremchuk', 'Forward', random.randint(700000, 1500000)),
        ('Mykola Matviyenko', 'Defender', random.randint(550000, 1100000)),
        ('Andriy Pyatov', 'Goalkeeper', random.randint(800000, 1600000)),
        ('Taras Stepanenko', 'Midfielder', random.randint(550000, 1100000)),
        ('Oleksandr Karavaev', 'Defender', random.randint(600000, 1200000)),
        ('Viktor Tsyhankov', 'Midfielder', random.randint(700000, 1500000)),
        ('Oleksandr Zubkov', 'Forward', random.randint(500000, 1000000)),
        ('Mykola Shaparenko', 'Midfielder', random.randint(600000, 1200000)),
        ('Denys Boyko', 'Goalkeeper', random.randint(750000, 1400000)),
        ('Serhiy Kryvtsov', 'Defender', random.randint(650000, 1300000)),
        ('Marlos', 'Midfielder', random.randint(700000, 1400000)),
        ('Yevhen Konoplyanka', 'Forward', random.randint(600000, 1200000)),
        ('Vitaliy Mykolenko', 'Defender', random.randint(600000, 1200000)),
        ('Oleksandr Syrota', 'Defender', random.randint(550000, 1100000)),
        ('Andriy Taran', 'Forward', random.randint(500000, 1000000)),
        ('Vasyl Kobin', 'Midfielder', random.randint(600000, 1200000)),
        ('Andriy Voronin', 'Forward', random.randint(700000, 1500000)),
        ('Yevhen Khacheridi', 'Defender', random.randint(750000, 1400000)),
        # Додайте інших гравців за необхідністю
    ]

    # Вставка даних в таблицю
    cursor.executemany('INSERT INTO players (full_name, position, salary) VALUES (?, ?, ?)', players_data)

# Збереження змін та закриття з'єднання
    sq.commit()


    print("Базу даних успішно створено та заповнено даними.")