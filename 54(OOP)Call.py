from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color=None):
        self.color = color

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_figure(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    def __str__(self):
        return self


class Square(Shape):

    def __init__(self, a, color=None):
        super().__init__(color)
        self.a = a

    def perimetr(self):
        return self.a * 4

    def area(self):
        return self.a ** 2

    def print_figure(self):
        self.print_info()
        [print("*" * self.a) for _ in range(self.a)]

    def print_info(self):
        print(f"Сторона квадрату а == {self.a}")

    def __str__(self):
        return f'сторона а = {self.a}, сторона b = {self.b}'


class Rectangle(Shape):
    def __init__(self, a, b, color=None):
        super().__init__(color)
        self.a = a
        self.b = b

    def perimetr(self):
        return self.a + self.b

    def area(self):
        return self.a * self.b

    def print_figure(self):
        self.print_info()
        [print("*" * self.a) for _ in range(self.b)]

    def print_info(self):
        print(f"Сторони прямокутника а == {self.a}, b == {self.b}")

    def __str__(self):
        return f'сторона а = {self.a}, сторона b = {self.b}'


class Triangle(Shape):
    def __init__(self, a, b, c, color=None):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimetr() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def print_figure(self):
        self.print_info()
        for i in range(self.b):
            print(" " * (self.a // 2 - 1) + "*" * i + "*" + "*" * i + "\n", end="")
        # for i in range(self.b):
        #     print(" " * (self.a // 2 - i) + "\n", end="")
        #     for k in range(1, self.a):
        #         print('*' * k)

    def print_info(self):
        print(f"Сторони трикутника: a == {self.a}, b == {self.b}, c == {self.c}")

    def __str__(self):
        return f'сторона а = {self.a}, сторона b = {self.b}'


f1 = Square(4, "red")
f1.print_figure()

f2 = Rectangle(4, 5)
f2.print_figure()
print(f2)
f3 = Triangle(11, 6, 6)
f3.print_figure()

for e in (f1, f2, f3):
    e.print_info()

print("*" * 89)  # ******************************************************************************


class Human:
    def __init__(self, last_name, first_name, age):
        self.lastname = last_name
        self.firstname = first_name
        self.age = age

    def info(self):
        print(f'{self.lastname} {self.firstname} {self.age}!', end=" ")


class Student(Human):
    def __init__(self, last_name, first_name, age, spec, group, rating=None):
        super().__init__(last_name, first_name, age)
        self.speciality = spec
        self.group = group
        self.rating = rating

    def info(self):
        super().info()
        print(f'{self.speciality} {self.group} ,', end=" ")
        if self.rating is not None:
            print(self.rating)


class Teacher(Human):
    def __init__(self, last_name, first_name, age, spec, exp):
        super().__init__(last_name, first_name, age)
        self.speciality = spec
        self.experience = exp

    def info(self):
        super().info()
        print(f'{self.speciality} {self.experience}.')


class Graduate(Student):
    def __init__(self, last_name, first_name, age, spec, group, topic):
        super().__init__(last_name, first_name, age, spec, group)
        self.topic = topic

    def info(self):
        super().info()
        print(f'{self.topic}.')


p1 = Student("Button", "Benjamin", 16, "GK", "Web_011", 50)
p2 = Teacher("Cruze", "Penelope", 21, "Algebra", 20)
p3 = Graduate("Shnaider", "Zack", 15, "PGO", "PD_011", "Protection")
#
group = [
    p1,
    p2,
    p3
]

for i in group:
    i.info()

print(p1.lastname)  # "Button"
print(p1.age)  # 16
print(p3.topic)  # 'Protection'
print(p3.speciality)  # 'PGO'
print(p3.rating)

print("=" * 89)  # ==================================================================

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __str__(self):
#         return f"{self.__coords}"
#
#     def __len__(self):  # довжина кортежу
#         return len(self.__coords)
#
#     def __abs__(self):  # список модулів
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, 2, 3)
# print(len(p))
# print(p)
# print(abs(p))
# print(p.__dict__)
#
# print("=" * 87)  # ======================================================
#
# import math


# class Point:
#     __slots__ = ("x", "y", "__length")  # прибирає метод __dict__ і обмежує цим використання усіх змінних окрім
#
#     # зазначених
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
#
# print(p.x)
# print(p.y)
# print(p.length)


# class Point2D:
#
#     # зазначених
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)


# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print(f"pt= {pt.__sizeof__()}")
# print(f"pt2= {pt2.__sizeof__()}" + f"{pt2.__dict__.__sizeof__()}")


# ПРИ НАСЛІДУВАННІ СЛОТС НЕ ПЕРЕДАЄТЬСЯ по замовчуванню
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ("z",)
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
#
# print(pt3.x)
# print(pt3.y)
# print(pt3.z)
#
# print("=" * 89)  # =============================================

""""""""""""""""""""""""""""""""""""""""""'FUNCTORS'""""""""""""""""""""""""""""""""""""""""""""


#  ключовий метод call() для створення функтору
# дозволяють працювати із об'єктами класу як із функціями

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self):  # Перегрузка круглих дужок виклику функуії
        self.__counter += 1
        print(self.__counter)
        return self.__counter


c1 = Counter()

c1()
c1()
c2 = Counter()  # тут іде збереження рахівника
c2()
c2()
Counter()()  # рахує тільки раз , бо  не зберігається в ніяку область пямяті
Counter()()


class StripsChars:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args):
        if not isinstance(args[0], str):
            raise ValueError("This argument must be string")
        return args[0].strip(self.chars)


s1 = StripsChars("?:!.,$ ")
print(s1(" ?Hello World! "))

print("  ?Hello, World!.  ".strip("?:!.,$ "))


def strip_string(chars):
    def wrap(string):
        if not isinstance(string, str):
            raise ValueError("This argument must be string")
        return string.strip(chars)

    return wrap


s2 = strip_string("?:!., ")
print(s2("  ?Hello World!.  "))

"""Class Decorators"""

print("=" * 78)  # =================================================================


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before calling a function")
        self.func()
        print("After calling the function")


@MyDecorator  # функція нижче попаде в атрибут класу
def funct():
    print("func")


#  Декоратори використовуються для передачі функції у аргументи

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print("Before calling a function")
        res = self.func(a, b)
        print("After calling the function")
        return res


@MyDecorator
def funct(a, b):
    print("func")
    print(a * b)
    return a * b


funct(2, 56)


class Power:
    def __init__(self, func):  # попадає функція
        self.f = func

    def __call__(self, a, b):
        res = self.f(a, b) ** 2
        return res


@Power
def functs(a, b):
    print(a * b)
    return a * b


print(functs(2, 3))


class Power:
    def __init__(self, sdf):  # попадає аргумент декоратора
        self.sdf = sdf

    def __call__(self, func):  # попадає функція без виклику та без аргументів
        def wrap(a, b):  # аргументи для func передаються
            res = func(a, b) ** 2
            print(self.sdf)
            return res

        return wrap


@Power("sdf")
def functs(a, b):
    print(a * b)
    return a * b


print(functs(2, 3))
print("=" * 78)  # ===========================================================================

"""
СТворити функтор для визначення порядку сортування списку р, який складається із обєктів класу
Person : [('Joan', 'Gorge',28),('Potter', 'Sten', 21),('Sider','Antuan',25),
('Peter', 'Ted',11),('Joana','Janett',28)]. Викликати функтор SortKey, із назвою поля
SortKey("surname"), і сортування буде відбуватись по цій властивості.
Якщо вказати відразу 2 значення: Sortkey("surname","firstname"), то сортування буде відбуватись
по прізвищу, а при рівності - по імені
"""


# class Person:
#     def __init__(self, surname, firstname, age):
#         self.firstname = firstname
#         self.surname = surname
#         self.age = age
#
#     def __str__(self):
#         return f"{self.surname}, {self.firstname}, {self.age}"
#
#
# class SortKey:
#     def __init__(self, *args):
#         self.arg = args
#
#     def __call__(self, a: list, **kwargs):
#         return sorted(a, key=lambda k: [k.__dict__[v] for v in self.arg])  # цей варіант не змінює список,
#         # тільки дані
#         # return a.sort(key=lambda j: [j.__dict__[v] for v in self.arg]) # цей варіант замінює сам список
#
#
# #  [k.__dict__[v] - буде попадати значення від ключа v.] в даному випадку дані, які видаються в кінці списку for v in
# #  self.arg
# p = [Person('Joan', 'Gorge', 28), Person('Potter', 'Sten', 21), Person('Sider', 'Antuan', 25),
#      Person('Peter', 'Ted', 11), Person('Joana', 'Janett', 28)]
#
# #
# s = SortKey("surname", "firstname")
# s(p)
# for pers in s(p):
#     print(pers)
# print(s.__dict__.items())
# res = lambda x, y: [x ** 2, y]
# print(res(5, 4))

# d = {"one": 1, "two": 2, "three": 3}

# class Person:
#     def __init__(self, surname, firstname, age):
#         self.surname = surname
#         self.firstname = firstname
#         self.age = age
#
#     def __str__(self):
#         return f"{self.surname}, {self.firstname}, {self.age}"
#
#     @property
#     def data(self):
#         return self.surname, self.firstname, self.age
#
#
# class Sortkey:
#     def __init__(self, *args):
#         self.p = args
#
#     def __call__(self, pe):
#         pe.sort(key=lambda j: [j.__dict__[key] for key in self.p])
#
#
#
# p = [('Joan', 'Gorge', 28), ('Potter', 'Sten', 21), ('Sider', 'Antuan', 25),
#      ('Peter', 'Ted', 11), ('Joana', 'Janett', 28)]
#
# s = Sortkey("surname", "firstname", "age")
# s(p)
#
# for i in p:
#     print(i.__str__())
#
#
# for i in p:
#     print(i.data)


class Person:
    def __init__(self, surname, firstname, age):
        self.surname = surname
        self.firstname = firstname
        self.age = age

    def __str__(self):
        return f"{self.surname}, {self.firstname}, {self.age}"

    @property
    def data(self):
        return self.surname, self.firstname, self.age


class Sortkey:
    def __init__(self, *args):
        self.p = args

    def __call__(self, pe):
        pe.sort(key=lambda j: [j.__dict__[k] for k in self.p])
        return pe


people = [Person('Joan', 'Gorge', 28), Person('Potter', 'Sten', 21), Person('Sider', 'Antuan', 25),
          Person('Peter', 'Ted', 11), Person('Joana', 'Janett', 28)]

s = Sortkey("surname")
s(people)

for person in people:
    print(person)

for person in people:
    print(person.data)

print("..new.." * 10)  # ===============================================================================

# class Sort:
#     p = [('Joan', 'Gorge', 28), ('Potter', 'Sten', 21), ('Sider', 'Antuan', 25),
#          ('Peter', 'Ted', 11), ('Joana', 'Janett', 28)]
#
#     def __init__(self, *keyargs):
#         self.sort_keys = keyargs
#
#     # def __str__(self):
#     #     return f"{self.surname} {self.name} {self.age}"
#
#     def __call__(self):
#         arg = self.p
#         return sorted(arg, key=lambda x: tuple(x[atr] for atr in self.sort_keys))
#
#
# #
#
#
# exempl = Sort(0)
# sortlist = exempl()
# for pe in sortlist:
#     print(pe)

# class Sort:
#     p = [('Joan', 'Gorge', 28), ('Potter', 'Sten', 21), ('Sider', 'Antuan', 25),
#          ('Peter', 'Ted', 11), ('Joana', 'Janett', 28)]
#
#     def __init__(self, *keyargs):
#         self.sort_keys = keyargs
#
#     def __str__(self):
#         return f"{self.surname} {self.name} {self.age}"
#
#     def __call__(self):
#         arg = self.p
#         arg.sort(key=lambda x: tuple(x[i] for i in self.sort_keys))
#         return arg
#
# exempl = Sort(0)  # Вказуємо індекс сортування (0 - за іменем, 1 - за прізвищем, 2 - за віком)
# sorted_people = exempl()  # Отримуємо відсортований список кортежів
# for person in sorted_people:
#     print(person)
