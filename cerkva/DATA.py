import sqlite3
import time, math
import re
from flask import url_for


class DATA:

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError as e:
            print("Не можу зчитати дані із бази даних" + str(e))

    def get_user(self, user_id):
        sql = f"SELECT * FROM users WHERE id={user_id} LIMIT 1"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                return res
            else:
                print("Користувача не знайдено")
                return False
        except sqlite3.Error as e:
            print("Помилка читання із бази даних" + str(e))
        return False

    def add_user(self, name, nickname, email, hash):
        sql = "INSERT INTO users VALUES(NULL,?,?,?,?,NULL,?) "
        tm = math.floor(time.time())
        self.__cur.execute(
            f'SELECT COUNT() as count FROM users WHERE email LIKE "{email}"'
        )
        res = self.__cur.fetchone()
        if res["count"] > 0:
            print("Цей емейл уже існує")
            return False
        try:
            self.__cur.execute(sql, (name, nickname, email, hash, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Помилка запису у базу даних" + str(e))
            return False
        return True

    def get_user(self, user_id):
        try:
            sql = f"SELECT * FROM users WHERE id = {user_id} LIMIT 1"
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if not res:
                print("Користувача не знайдено")
                return False
            return res
        except sqlite3.Error as e:
            print("Помилка читання із бази даних" + str(e))
        return False
