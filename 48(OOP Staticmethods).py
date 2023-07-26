# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property
#     def coords_x(self):
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Wrong format data")
#
#     @coords_x.deleter
#     def coords_x(self):
#         print(f"Видалення {self.__x}")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
#
# print(p1.__dict__)
# p1.coords_x = 23
# print(p1.__dict__)
#
#
# class kgtpounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, kg):
#         if isinstance(kg, (int, float)):
#             self.__kg = kg
#         else:
#             print("Kg has been provided by numbers only")
#
#     @kg.deleter
#     def kg(self):
#         del self.__kg
#
#     def change(self):
#         return self.__kg * 2.205
#
# w = kgtpounds(12)
# print(w.kg)
# print(w.change())
# w.kg = "Nine"


class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    @staticmethod  # метод який не знає до якого класу відноситься, ті які є просто функціями які не заважають
    # архітектурі класу. СТатік методи не змінюють нічого у ініт
    def get_count():
        return Point.__count

    # get_count = staticmethod(get_count) #  - Аналог декоратору @staticmethod


p1 = Point()
p2 = Point()
p3 = Point()

print(Point.get_count())
print(p1.get_count())
print(p2.get_count())
print(p1.__dict__)


class Change:
    @staticmethod
    def inc(x):
        return x + 1

    @staticmethod
    def dec(x):
        return x - 1


print(Change.inc(10), Change.dec(10))
q = Change()
print(q.dec(5), q.inc(5))


# працюють статичні методи не тільки із статичними змінними


class Count:

    @staticmethod
    def maks(*args):
        t = args
        return max(t)

    @staticmethod
    def min(*args):
        t = args
        return min(t)

    @staticmethod
    def serar(*args):
        t = sum(args) / len(args)
        return t

    @staticmethod
    def factotial(arg):
        l = list(range(1, arg + 1))
        res = 1
        for i in l:
            res *= i
        return res


# k = 3, 5, 7, 9
res1 = Count
print(res1.maks(3, 5, 7, 9))
print(res1.min(3, 5, 7, 9))
print(res1.serar(3, 5, 7, 9))
print(res1.factotial(5))


class Numbers:
    @staticmethod
    def makxs(a, b, c, d):
        if a > b and a > c and a > d:
            return a
        elif b > a and b > c and b > d:
            return b
        elif c > a and c > b and c > d:
            return c
        else:
            return d

    @staticmethod
    def minis(a, b, c, d):
        if a < b and a < c and a < d:
            return a
        elif b < a and b < c and b < d:
            return b
        elif c < a and c < b and c < d:
            return c
        else:
            return d

    @staticmethod
    def avarage(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def fact():
        pass


print(Numbers.makxs(3, 5, 7, 9))
print(Numbers.minis(3, 5, 7, 9))
print(Numbers.avarage(3, 5, 7, 9))

"""Методи Классу"""


# @classmethod

class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data_as_str):
        day, month, year = map(int, data_as_str.split("."))
        date1 = cls(day, month, year)

        return date1

    def string_to_db(self):
        return f"{self.year}-{self.month}-{self.day}"

    @staticmethod
    def is_valid(date_as_string):
        if date_as_string.count(".") == 2:
            day, month, year = map(int, date_as_string.split("."))
            return day <= 31 and month <= 12 and year <= 3999


dates = [
    "30.12.2021",
    "30-12-2020",
    "01.31.2021",
    "12.31.2020"
]

for d in dates:
    if Date.is_valid(d):
        date = Date.from_string(d)
        db = date.string_to_db()
        print(db)
    else:
        print("Wrong format or date string")
da = "16.12.2021"
# day, month, year = map(int, d.split("."))
# print(day, month, year)
d = Date()
date = d.from_string(da)
print(date.string_to_db())

d1 = Date()
date1 = d1.from_string("02.12.2020")
print(date1.string_to_db()) # 2020-12-2

date2 = Date.from_string("15.10.2021")  # date2 не є екземпляром класу, це просто змінна, не є екземпляром класу тому,
# що не було виклику Date()
print(date2)
print(date2.string_to_db()) # 2021-10-15

"""self - відноситься до екземпляру класу а 
 cls - просто до класу
"""

"""де корисно приміняти cls методи пайтон замість звичайних self методів класу?
ChatGPT
Методи, що використовують cls замість звичайних self методів, називаються методами класу (class methods) в Python.
 Вони використовуються для взаємодії з класом, а не з окремими екземплярами класу.
Ось кілька ситуацій, коли варто розглянути використання методів класу замість звичайних методів:
Фабричні методи: Методи класу можуть використовуватися для створення нових екземплярів класу.
 Вони можуть бути корисними, якщо потрібно створити об'єкт зі складними параметрами або за допомогою певної логіки.
Методи, які працюють зі змінними класу: Якщо потрібно отримати доступ до змінних класу або змінювати їх,
 методи класу є зручним інструментом. Вони можуть використовуватися для ініціалізації статичних змінних,
  виконання операцій над цими змінними або забезпечення спільного доступу до них з інших методів.
Альтернативний конструктор: Методи класу можуть слугувати альтернативними конструкторами, які дозволяють створювати
 екземпляри класу з іншими параметрами або виконувати додаткову логіку при створенні.
Поліморфізм: Методи класу можуть бути перевизначеними в похідних класах, що дозволяє досягати поліморфізму. Це означає,
 що однаково названі методи можуть мати різну реалізацію в різних класах.
Цікавою особливістю методів класу є те, що вони мають доступ до самого класу через аргумент cls. Це може бути корисно,
 якщо потрібно виконати операції з класом, які не стосуються конкретного екземпляра.
Враховуйте, що методи класу можуть бути викликані безпосередньо з класу, а не через екземпляр класу.
 У методі класу немає доступу до змінних екземпляра, так як він не прив'язаний до конкретного екземпляра.
 Замість цього, він має доступ до змінних класу через cls.
Загалом, використання методів класу залежить від контексту і вимог вашої програми.
 Вони є корисним інструментом для взаємодії з класом в цілому і можуть бути використані в різних ситуаціях відповідно до вашої потреби."""


class Geometric:
    @staticmethod
    def area_square(a):
        return f"Площа квадрата {a ** 2}"

    @staticmethod
    def area_triangle_g(a, b, c):
        P = a+b+c
        s = P/2
        return f"За формулою герона {(s * (s - a) * (s - b) * (s - c)) ** (1 / 2)}"

    @staticmethod
    def area_rectangle(a, b):
        return f"Площя прямокутника {a * b}"

    @staticmethod
    def triangle_area_(width, high):
        return f"ПЛоща трикутника за висотою та стороною {(1/2)*width*high}"

print(Geometric.area_triangle_g(3,4,5)) # 6.0
print(Geometric.area_rectangle(2,6))
print(Geometric.triangle_area_(6,7))
print(Geometric.area_square(7))


