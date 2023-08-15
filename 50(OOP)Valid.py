import re

"""Валідація можлива через закриття атрибутів і сеттери"""


class UserDate:
    def __init__(self, pib, age, ps, weight):
        self.verify_pib(pib)
        self.verify_age(age)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__pib = pib.split()
        self.__age = age
        self.__password = ps
        self.__weight = weight

    @classmethod
    def verify_pib(cls, pib):
        if not isinstance(pib, str):  # якщо не строка то зайдем в цей блок і закінчимо помилкою
            raise TypeError("ПІБ має бути строкою")
        f = pib.split()  # поверне масив з трьох елементів ПІБ
        print(f)
        if len(f) != 3:  # перевірка масиву
            raise TypeError("Невірний формат")
        letters = "".join(re.findall(r"[a-zа-я-]", pib, flags=re.IGNORECASE))  # ПрізвищеІм'яПобатькові
        print(letters)
        for s in f:
            if len(s.strip(letters)) != 0:  # стріп видалить усі букви, які вказані в круглих дужках, за наявністю
                # 1 цифри  довжина стане 1, і тоді ми зайдемо у цей блок де буде ловитись помилка
                raise TypeError("В ПІБ можна використовувати тільки букви або дефіси")

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age < 14 or age > 100:
            raise TypeError('Тип даних віку повинен бути числом в діапазоні від 14 до 100')

    @classmethod
    def verify_weight(cls, w):
        if not isinstance(w, (int, float) or w < 40):
            raise TypeError("Вага повинна бути числом та від 40 кг")

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспортні дані повинні бути строковим значенням")
        s = ps.split()
        print(s)
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Не вірний формат паспортних даних')  # райз закриє виконання так само як ретурн

    @property
    def get_pib(self):
        return self.__pib

    @get_pib.setter
    def get_pib(self, x):
        self.verify_pib(x)
        self.__pib = x

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, x):
        self.verify_age(x)
        self.__age = x

    @property
    def get_weight(self):
        return self.__weight

    @get_weight.setter
    def get_weight(self, x):
        self.verify_weight(x)
        self.__weight = x

    @property
    def get_ps(self):
        return self.__password

    @get_ps.setter
    def get_ps(self, x):
        self.verify_ps(x)
        self.__password = x


p1 = UserDate("Заплет Денис Миколайович", 26, "1234 567890", 80.8)
p1.get_pib = "Баран Тарас Брозович"
print(p1.get_pib)
p1.get_ps = "2390 123097"
print(p1.get_ps)
p1.get_age = 35
print(p1.__dict__)

# {'_UserDate__pib': 'Баран Тарас Брозович', 'age': 26,
#               'password': '1234 567890', 'weight': 80.8, '_UserDate__password': '2390 123097',
#                                                                           '_UserDate__age': 35}

"""геттери і сеттери переписують атрибути які є публічними на свій лад, але тільки у випадку 
конфронтації імен. Це коли ми називаємо геттер і сеттер ім'ям змінної. Якщо назвати різними іме-
нами так, як це зробив я, то ніякої конфронтації не виникає і метод __dict__ покаже утворення
нових закритих змінних, які утворить сеттер і геттер. Це буде на додачу до старих змінних які 
публічні. Тому у мене і утворились нові атрибути в запуску програми (коли було закоментовано
веріфікацію та змінено приватні атрибути в ініціалізаторі на публічні. )(Зараз усе відредаговано до 
первісного вигляду)"""

"""Перегрузка методів"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def is_digit(self):
        if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
            return True
        else:
            return False

    def is_int(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            return True
        else:
            return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Coordinates have to be numbers")


class Line(Prop):
    def drow_line(self):
        print(f"Малювання лінії: {self._sp}, {self._ep}, {self._color}, {self._width}")

    # def set_coords(self, sp: Point, ep: Point = None):  # якщо закоментувати чи видалити, то знайде аналогічний у
    #     # батьківському класі і буде працювати по ньому
    #     if ep is None:
    #         if sp.is_int():
    #             self._sp = sp
    #         else:
    #             print("Coordinates have to be numbers")
    #     else:
    #         if sp.is_int() and ep.is_int():
    #             self._sp = sp
    #             self._ep = ep
    #         else:
    #             print("Coordinates have to be numbers")

    def __set_one_coords(self, sp):  # два закритих методи для того, щоб використовувати їх у коді нижче
        if sp.is_int():
            self._sp = sp
        else:
            print("Coordinates have to be numbers")

    def __set_to_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep
        else:
            print("Coordinates have to be numbers")

    def set_coords(self, sp: Point, ep: Point = None):  # якщо закоментувати чи видалити, то знайде аналогічний у
        # батьківському класі і буде працювати по ньому
        if ep is None:
            self.__set_one_coords(sp)  # готовий метод для однієї координати
        else:
            self.__set_to_coords(sp, ep)  # Готовий метод для вводу двох координат


line = Line(Point(1, 2), Point(10, 20))
line.drow_line()
line.set_coords(Point(30.6, 40), Point(100, 200))
line.drow_line()

line.set_coords(Point(-12, -20))
line.drow_line()

print("=" * 89)  # ==================================================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         else:
#             return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         else:
#             return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coordinates have to be numbers")
#
#     def drow(self):  # Абстрактний метод, викликається тільки тоді, коли є помилка і метод із таким самим іменем
#         # не прописаний у дочірньому класі, а у коді викликається
#         raise NotImplementedError("В дочірньому класі повинен бути ВИЗНАЧЕНИЙ метод draw()")
#
#
# class Line(Prop):
#     def drow(self):
#         print(f"Малювання лінії: {self._sp}, {self._ep}, {self._color}, {self._width}")
# #
# #
# class Rect(Prop):
#     def drow(self):
#         print(f"Малювання прямокутника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def drow(self):
#         print(f"Малювання еліпсу: {self._sp}, {self._ep}, {self._color}, {self._width}")
# #
# #
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
# print(figs) # [<__main__.Line object at 0x000001BDFCF2ECE0>, <__main__.Line object at 0x000001BDFCF2EBC0>, <__main__.Rect object at 0x000001BDFCF2EAA0>, <__main__.Ellipse object at 0x000001BDFCF2E980>]
# for f in figs:
#     f.drow()

print("=" * 89)  # ==================================================================
"""АБСТРАКТНІ КЛАСИ"""

from abc import ABC, abstractmethod


class Chess(ABC):  # Став абстрактний класом, не може мати об'єкти, але має методи, які виконуються якщо одноіменні
    # методи із наслідних (дочірніх) класів не прописані.
    def draw(self):
        print("Намалював шахову фігуру")

    @abstractmethod
    def move(self):
        print('Метод move() в базовому класі')


class Queen(Chess):
    def move(self):
        super().move()
        print("Королева змінила положення на шаховому полі")


q = Queen()

q.draw()

q.move()

"""Абстрактний метод повинен бути переоприділений у дочірньому класі"""

from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def set_radius(self, radius):
        self._radius = radius

    def set_sides(self, width=None, length=None):
        if length is None:
            self._width = self._length = width
        else:
            self._width = width
            self._length = length

    def calc_area(self):
        raise NotImplementedError("В дочірньому класі повинен бути визнячений метод calc_area()")


class Sq_table(Table):
    def calc_area(self):
        return self._width * self._length


class Round_table(Table):

    def calc_area(self):
        return self._radius ** 2 * pi


t = Sq_table(20, 10)
print(t.__dict__)
t.set_sides(2)
print(t.calc_area())

t1 = Round_table(radius=10)
print(t1.__dict__)
print(t1.calc_area())

t2 = Round_table(radius=20)
t2.set_radius(60)
print(t2.__dict__)
print(t2.calc_area())

print("=" * 78)  # ==============================================================


class Table(ABC):
    def __init__(self, width=None, length=None, radius=None, ):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    @abstractmethod
    def area(self):
        raise NotImplementedError("Повинен бути прописаний у дочірньому класі")


class RectTable(Table):
    def area(self):
        # super().area()
        return self._width * self._length


class CirleTable(Table):

    def area(self):
        # super().area()
        return pi * self._radius ** 2


f1 = RectTable(20, 10)
f2 = CirleTable(radius=10)
f3 = CirleTable(radius=20)

f = list()
# f.append(f1)
# f.append(f2)
# f.append(f3)
#
[f.append(x) for x in [f1, f2, f3]]
for table in f:
    print("ПОкуажись",table.area())


class Root(ABC):

    def __init__(self, equation: str):
        self.equation = equation

    @abstractmethod
    def line_equation(self):
        pass

    @abstractmethod
    def sq_equation(self):
        pass

    @abstractmethod
    def valid(self):
        pass


class LineEquation(Root):
    def __init__(self, equation):
        super().__init__(equation)

    def line_equation(self):
        leftside = self.equation.split("=")[0]
        rightside = self.equation.split("=")[1]
        if "+" in leftside:
            r = leftside.replace("+", "+-")
            c = r.split("+")[1]
            b = r.split("x")[0]
            x = (-int(c[1:]) + int(rightside)) / int(b)

            return round(x, 2)
        if "-" in leftside:
            r = leftside.replace("-", "-+")
            c = r.split("-")[1]
            b = r.split("x")[0]
            x = (int(c[1:]) + int(rightside)) / int(b)
            return round(x, 2)

    @staticmethod
    def Discriminant(a, b, c):
        return b ** 2 - 4 * a * c

    @staticmethod
    def results(a, b, D):
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2

    def sq_equation(self):
        leftside = self.equation.split("=")[0]
        rightside = self.equation.split("=")[1]
        a = int(leftside.split("x")[0])
        r = leftside.replace("-", "+-")
        b = int(r.split("+")[1].removesuffix("x"))
        c = int(r.split("+")[2]) + (-1 * int(rightside))
        D = b ** 2 - 4 * a * c
        if D < 0:
            x1 = None
            x2 = None
        elif D == 0:
            x1 = x2 = (-b + D ** 0.5) / (2 * a)
        else:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)

    def valid(self):
        if "**2" in self.equation:
            print("Square equation")
            self.sq_equation()
        else:
            print("line equation")
            self.line_equation()


class SqEquation(Root):
    pass


l = LineEquation("1x**2-2x-3=0")
print(l.sq_equation())
