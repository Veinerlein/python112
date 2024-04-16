import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('eroor of the readings of DATABASE')
        return []

    def add_post(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM posts WHERE url like ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('The note already exists')
                return False
            base = url_for('static', filename='images')
            newtext = re.sub(r'(?P<tag><img\s+[^>]*src=)(?P<quote>[\'"])(?P<url>.+?)(?P=quote)>', r'\g<tag>' + base +
                             r'/\g<url>>',
                             text)
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL,?,?,?,?)', (title, newtext, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error of adding the note' + str(e))
        return True

    def del_post(self, title):
        try:
            self.__cur.execute(f'DELETE FROM posts WHERE title==?', (title,))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error of the deleting" + " " + str(e))
        return True

    def get_post(self, alias):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url LIKE "{alias}" LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Error' + str(e))
            return False, False

    def get_all_posts(self):
        sql = 'SELECT * FROM posts ORDER BY time DESC'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('eroor of the readings of DATABASE')
        return []

    def add_user(self, name, email, hash):
        sql = 'INSERT INTO users VALUES(NULL,?,?,?,NULL,?)'
        tm = math.floor(time.time())
        try:
            self.__cur.execute(f'SELECT COUNT() as count FROM users WHERE email LIKE "{email}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('This email already registered')
                return False
            self.__cur.execute(sql, (name, email, hash, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('error' + str(e))
            return False
        return True

    def get_user(self, user_id):
        try:
            self.__cur.execute(f'SELECT * FROM users WHERE id = {user_id} LIMIT 1')
            res = self.__cur.fetchone()
            if not res:
                print('User does not exist')
                return False
            return res
        except sqlite3.Error as e:
            print('Error from Database' + str(e))
        return False

    def get_user_by_email(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Current user does not exists')
                return False
            return res
        except sqlite3.Error as e:
            print('Error to catch the data from Database' + str(e))
        return False

