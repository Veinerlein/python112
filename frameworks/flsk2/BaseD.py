import sqlite3, time, os


class Base:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM menu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            return res
        except IOError:
            print('Some error in reading from database')
            return []

    def add_menu(self, name, url):
        try:
            self.__cur.execute("INSERT INTO menu VALUES(NULL,?,?)", (name, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error of adding the menu point')
        return True

    def del_menu(self, name):
        try:
            self.__cur.execute('DELETE FROM menu WHERE menu_name==?', (name,))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error of deleting the menu point')
        return True
