"""Пакування даних. (Серіалізація та Десеріалізація)"""
#  перекодували дані в певний формат та зберігли на диск.

# Серіалізація - запис даних на диск
# Десеріалізація - читання даних із диска

#  -  marshal - підтримка старих форматі в дланих (застарів)
#  - pickle - працює тільки із пітон,
#  - json

import pickle
import string

filename = "basket.txt"
shoplist = {
    "fruits": ["apples", "mango"],
    "vegetables": ["carrots"],
    "money": 1000
}

with open(filename, "wb") as fh:
    pickle.dump(shoplist, fh)  # серіліазіація даних у відкритий файл

with open(filename, "rb") as fh:
    print(pickle.load(fh))  # зчитування даних із оперативної


class Test:
    a_number = 35
    a_string = "Hello"
    a_list = [1, 2, 3]
    a_tuple = (22, 23)
    a_dict = {"first": "a", 'second': 2, 'third': [1, 2, 3]}

    def __str__(self):
        return f"Number {Test.a_number}\nString {Test.a_string}\nList {Test.a_list}\nTuple {Test.a_tuple}\nDictionary {Test.a_dict}"


obj = Test()

my_obj = pickle.dumps(obj)  # серіалізація(збереження даних у оперативну пам'ять)
print(f"Serealization in string:\n{my_obj}")

"""
Для файлу
pickle.dump()- запис
pickle.load() - зчитування 

Для оперативної памяті
pickle.dumps() - запис
pickle.loads() - зчитцування
"""

l_obj = pickle.loads(my_obj)
print(f"Deserealization in string:\n{l_obj}")


class Test2:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x

    def __str__(self):
        return f"{self.a},{self.b},{self.c(2)}"  # 2 goes to x in lambda

    def __getstate__(self):  # підхід дозволяє вам визначити, які дані об'єкта слід зберігати
        # і які можна виключити з серіалізації та відновлення за допомогою методу
        attr = self.__dict__.copy()  # зберігаємо копію даних
        print(attr)  # {'a': 35, 'b': 'test', 'c': <function Test2.__init__.<locals>.<lambda> at 0x00000157C350E290>}
        del attr["c"]  # Видалити lambda Яку неможливо сереалізувати
        print(attr)  # {'a': 35, 'b': 'test'}
        return attr

    #
    def __setstate__(self, state):  # state == {} # відновлює атрибут c під час відновлення об'єкта.
        self.__dict__ = state  # Повернули все те, що було раніше
        self.c = lambda x: x * x  # Повернули раніше видалену lambda


item = Test2()
item2 = pickle.dumps(item)
item3 = pickle.loads(item2)

print(item3.__dict__)  # {'a': 35, 'b': 'test'}
# print(item3)  # <__main__.Test2 object at 0x00000202AB08FD90>
print(item3)

print("=" * 45)  # ========================================================


class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)  # для даної функції теж потрібен __getstate__
        self.cnt = 0

    def read_line(self):
        self.cnt += 1
        line = self.file.readline()  # мутод readline зчитує до переносу один рядок
        if not line:
            return None
        if any(char.isalnum() or char in string.punctuation for char in line) and line.endswith("\n"):
            # повертає True, якщо принаймні один елемент у iterable обчислюється як True.
            # Метод any() є вбудованим в Python, і він використовується для перевірки, чи є хоча б один елемент
            # в ітерабельному об'єкті (такому як список, кортеж, множина, рядок тощо)
            # True (істинним) на підставі умови, заданої у вигляді функції або виразу.,
            #     line = line[:-1]
            # if line.endswith("\n"):  # якщо зчитування закінчується переносом на наступний рядок (закінчується там
            # де закінчується), то:
            line = line[:-1]  # візьме лайн до переносу (таким чином виключили небажані відступи)
        else:
            return "___EMPTY___"
        return f"{self.cnt}:{line}"

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)  # відновлення стан у раніше відкритого файлу
        file = open(self.filename)
        for i in range(self.cnt):
            file.readline()
        self.file = file


reader = TextReader("res_1.txt")

print(reader.read_line())  # - Цей виклик не повинен відбутись
print(reader.read_line())
print(reader.read_line())
print(reader.read_line())

new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.read_line())

import re


class NextReader:
    def __init__(self, filename):
        self.filename = filename
        self.cnt = 0
        self.file = open(self.filename)

    def __str__(self):
        return f"{self.filename}{self.file}{self.cnt}"

    def read(self):
        if re.match("", self.file.readline()) is True:
            pass
        else:
            self.cnt += 1
            text = self.file.readline()
            if text.endswith('\n'):
                text = text[:-1]
            return f"{self.cnt}: {text}"

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__ = state
        self.file = open(self.filename)
        for i in range(self.cnt):
            self.file.readline()


print("up")
nread = NextReader("res_1.txt")
print(nread.read())
print(nread.read())
dumping = pickle.dumps(nread)
print(nread.__dict__)
loading = pickle.loads(dumping)
print(loading.read())
print(loading.read())
print(loading.read())
print("down")
# class NextReader2:
#     def __init__(self, filename):
#         self.filename = filename
#         self.cnt = 0
#         self.file = open(self.filename)
#
#     def read(self):
#         self.cnt += 1
#         text = self.file.readline()
#         if text.endswith('\n'):
#             text = text[:-1]
#         return f"{self.cnt}: {text}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         # Закрити файл перед серіалізацією
#         state["file"].close()
#         del state["file"]
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         # Перевірка існування атрибуту "file" у стані
#
#         # Відновлення файлового об'єкта
#         self.file = open(self.filename)  # open(state["filename"])
#
#
# nread2 = NextReader2("res_1.txt")
# print(nread2.read())
# print(nread2.read())
# print(nread2.read())
# #
# # Серіалізація
# dumping2 = pickle.dumps(nread2)
#
# # Десеріалізація
# loading2 = pickle.loads(dumping2)
#
# # Перевірка, чи працює відновлений об'єкт
# print(loading2.read())
#
# class NextReader3:
#     def __init__(self, filename):
#         self.filename = filename
#         self.cnt = 0
#         self.file = open(self.filename)
#
#     def read(self):
#         self.cnt += 1
#         text = self.file.readline()
#         if text.endswith('\n'):
#             text = text[:-1]
#         return f"{self.cnt}: {text}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         # Закрити файл перед серіалізацією
#         state["file"].close()
#         del state["file"]
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         # Перевірка існування атрибуту "file" у стані
#         if "filename" in state:
#             # Відновлення файлового об'єкта
#             self.file = open(state["filename"])
#
# nread3 = NextReader3("res_1.txt")
# print(nread3.read())
# print(nread3.read())
# print(nread3.read())
#
# # Серіалізація
# dumping3 = pickle.dumps(nread3)
#
# # Десеріалізація
# loading3 = pickle.loads(dumping3)
#
# # Перевірка, чи працює відновлений об'єкт
# print(loading3.read())  # <= бонусні класи від чатбота

"""JSON"""

import json  # Словник має ключі в лапках тільки так

#   dict            == object
#   list,tuple      == array
#   str             == string
#   int,long,float  == number (int), number(real)
#   True            == true
#   False           == false
#   None            == null

data = {
    "firstname": "Janet",
    "lastname": 'Django',
    "hobbies": ("running", "wolking", "sky gazing"),  # все одно буде список
    "age": 5,
    '20': "one"  # все одно переформує у "20" ключ, але під час сортування викличе помилку
}

# with open("data_file.txt", "w") as fw:
#     json.dump(data, fw,indent=4) # indent - кількість символів для переформатування
# Означає що по (4 в даному випадку) табуляції кожен блок даних відсувається

# робота із функціями: в json функції не можна передавати

# with open("data_file.txt","r") as fr:
#     print(json.load(fr))

st = json.dumps(data, sort_keys=True)  # зберіг дані в оперативну пам

data = json.loads(st)
print(data)

x = {
    "name": "Vander", "ім'я": "Вандер"
}
y = {
    "name": "Vander", "ім'я": "Вандер"
}
print(json.dumps(x))
print(json.dumps(y, ensure_ascii=False))  # виправить кодування

print("=" * 45)  # ==================================================================

import json
from random import choice


def get_pers():
    name = ""
    names = set()
    tel = ""
    letters = ['a', "b", 'c', 'd', 'e', 'f', 'i']
    num = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 8:
        name += choice(letters)
        name += choice(num)
    if name not in names:
        names.add(name)
        print(names)


# get_pers()


def get_person():
    name = ""
    tel = "380"
    letters = ['a', "b", 'c', 'd', 'e', 'f', 'i']
    num = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 7:
        name += choice(letters)
    name = name[0].upper() + name[1:]
    while len(tel) != 10:
        tel += choice(num)
    person = {
        'name': name,
        "tel": tel
    }
    print(f"Name is '{name}' and telephone number is +{tel[:3] + ' ' + tel[3:6] + ' ' + tel[6:]}.\n{person}")
    return person


# Додати список, у який потім додасо дані із return get_person
persons_exempl = []
for i in range(7):
    persons_exempl.append(get_person())

# [{'name': 'Icccfcb', 'tel': '3806400184'},
# {'name': 'Ecbcfda', 'tel': '3804830950'},
# {'name': 'Dedbfie', 'tel': '3803260646'},
# {'name': 'Bdeiadd', 'tel': '3807263437'},
# {'name': 'Bdaiceb', 'tel': '3801169637'}]

with open("persons_exempl.json", "w") as f:
    json.dump(persons_exempl, f, indent=4,
              ensure_ascii=False)  # записали список у форматі json у файл f , тобто із такою назвою:
    # "persons.json"

# для того щоб у режимі дозапису даних не додавався новий список, я розширувався і доповнювався перший
# потрібно додатково прописати функцію, яка буде діяти в умові дозапису файлу.


persons = []


def rewrite_json(person_dict):
    try:
        data = json.load(open('persons.json'))  # якщо дані є, то зчитуємо дані
        print(f"data is {data}")
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # якщо даних немає то список буде пустим
    data.append(person_dict)  # в змінну до зчитаних даних додати нові дані, які прийшли
    with open("persons.json", "w") as f:  # записати замість старих даних дані зі змінної,
        # у якій є як старі дані так і нові.
        json.dump(data, f, indent=4)  # записано


rewrite_json(get_person())

print('+' * 45)  # =========================================================


def gen_person():
    vowel_letter = ['a', 'u', 'o', 'i', 'e', 'y']
    consonant_letter = ['b', 'f', 'h', 'p', 'r', 'w', 'c', 'q', 't', 'm', 'z', 'x', 'l', 'j', 's', 'g']
    numbers = [str(i) for i in range(10)]
    name = ""
    tel = "380"
    while len(name) < 9:
        name += choice(consonant_letter)
        name += choice(vowel_letter)
    name = name.title()
    while len(tel) < 10:
        tel += choice(numbers)
    pers = {"Name": name, 'TEL': tel}
    return pers


# print(gen_person())


def dumpload(func_generator, filename):  # попаде персон
    try:
        datas = json.load(open(filename))
        key = len(datas)  # визначиться ключ, в який буде вставлятись наступний об'єкт
    except (FileNotFoundError, json.JSONDecodeError):
        datas = {}
        key = 0  # тут ключ буде 0
    datas[key] = func_generator  # відповідно до умов або вставляється в пустий словник, або продовжується
    # поповнюватись до існуючих даних новими.
    with open(filename, "w") as f:
        json.dump(datas, f, indent=4)


# print(dumpload(gen_person(), "Person_DICT.json"))
# print(dumpload(gen_person(), "Person_DICT.json"))
# for data in dumpload(gen_person(),"Person_DICT.json"):
#     print(data)


import os  # Додатково імпортуємо модуль os


# def get_person():
#
#     name = ""
#     tel = "380"
#     letters = ['a', "b", 'c', 'd', 'e', 'f', 'i']
#     num = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#     name = name[0].upper() + name[1:]
#     while len(tel) != 10:
#         tel += choice(num)
#     person = {
#         'name': name,
#         "tel": tel
#     }
#     return person
# # ... Код для генерації даних про людину ...
#
# def rewrite_json(person_list):
#     with open("persons.json", "w") as f:
#         json.dump(person_list, f, indent=4)
#
# # Перевіряємо існування файлу "persons.json"
# if os.path.exists("persons.json"):
#     try:
#         # Спробуємо відкрити та зчитати дані з файлу
#         with open("persons.json", "r") as f:
#             persons = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         # Якщо файл порожній або містить неправильні дані, створимо пустий список
#         persons = []
# else:
#     # Якщо файл не існує, створимо пустий список
#     persons = []
#
# # Генеруємо та додаємо дані про людей до списку
# for i in range(5):
#     persons.append(get_person())
#
# # Записуємо весь список persons у файл "persons.json"
# rewrite_json(persons)

class Loader:
    def __init__(self, data, filename):
        self.data = data  # звичайна змінна для даних
        self.datacopy = self.data  # тимчасова змінна у випадку, якщо дані будуть функцією
        # або callable об'єктом
        self.file_name = filename  # ім'я файлу

    def __str__(self):
        return f"{self.data}{self.file_name}"

    def __getstate__(self):
        state = self.__dict__.copy()
        print(state)
        state["data"] = None

        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.data = self.datacopy

    def dumping(self):
        temporary_data = []
        try:
            temporary_data.extend(self.reading())
        except (FileNotFoundError, json.JSONDecodeError):
            temporary_data = []
        temporary_data.append(self.data) if not callable(self.data) else temporary_data.append(str(self.data))
        with open(self.file_name, "w") as f:
            json.dump(temporary_data, f, indent=4)

    def reading(self):
        with open(self.file_name, "r") as f:
            datas = json.load(f)
            print(datas)
            return datas


x1 = Loader(gen_person(), "LoaderDUMP.json")


x1.dumping()


x1.reading()


class LoaderPickle:
    def __init__(self, data, filename):
        self.data = data
        self.file_name = filename

    def dumping(self):
        temporary_data = []
        try:
            temporary_data.append(self.reading())
        except (FileNotFoundError, EOFError):
            temporary_data = []
        temporary_data.append(self.data)
        with open(self.file_name, "wb") as f:
            pickle.dump(temporary_data, f)

    def reading(self):
        with open(self.file_name, "rb") as f:
            datas = pickle.load(f)
            return datas


x2 = LoaderPickle(gen_person(), "LoaderDUMP2.pkl")
# x2.dumping()
