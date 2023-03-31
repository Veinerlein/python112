team = [
    {'name': 'Antuan', 'lastname': 'Grizman', 'raiting': 9},
    {'name': 'Alexis', 'lastname': 'Sanches', 'raiting': 10},
    {'name': 'Taras', 'lastname': 'Stepanenko', 'raiting': 4},
    {'name': 'Mihael', 'lastname': 'Mudryk', 'raiting': 6}
]

res = sorted(team, key=lambda t: t["lastname"])
print(res)

# res2 = sorted(team, key=lambda t: t["raiting"],reverse=True)
# print(res2)
# res3 = sorted(team, key=lambda t: t["name"])
# print(res3)
# for t in team:
#     for (k,v) in t.items():
#         print({k:v})


# def outer(lower, upper):
#     def inner(raiting):
#         return {k: v for (k, v) in raiting.values() if lower <= v <= upper}
#
#     return inner
#
# vuklyk = outer(5,10)
# print(vuklyk(team[0][2]))

""" ВИКЛИК ЛЯМБДИ ЯК ФУНКЦІЇ ІЗ ЗНАЧЕННЯ СПИСКУ """
a = {"one": lambda x: x - 1, "two": lambda x: abs(x) - 1, "three": lambda x: x}
b = [-3, 10, 0, 1]
for i in b:
    if i < 0:
        print(a["two"](i))  # i == -3;  lambda x: abs(-3) - 1 == 3-1

    elif i > 0:
        print(a["one"](i))  # 9 and 0
    else:
        print(a["three"](i))  # 0

# a["three"](i)  -    a["three"]  == це типу назва змінної
# в якій буде функція,
# (i) це буде виклик функції із параметром - і

d = {
    1: lambda: print("Monday"),
    2: lambda: print("Tuesday"),
    3: lambda: print("Wednesday"),
    4: lambda: print("Thursday"),
    5: lambda: print("Friday"),
    6: lambda: print("Saturday"),
    7: lambda: print("Sunday")
}

d[7]()
from math import pi

radius = lambda x: 2 * pi * x
rectangle = lambda x, y: x * y
trapeze = lambda a=7, b=5, h=3: 0.5 * (a + b) * h

print(radius(2))  # 12.566370614359172
print(rectangle(10, 13))  # 130
print(trapeze())  # 18.0

radius = lambda x: print(round((2 * pi * x), 4))  # 12.5664
rectangle = lambda x, y: print(x * y)  # 130
trapeze = lambda a=7, b=5, h=3: print(0.5 * (a + b) * h)  # 18.0

radius(2)
rectangle(10, 13)
trapeze()

area = {
    "radius": lambda x: print(round((2 * pi * x), 4)),
    "rectangle": lambda x, y: print(x * y),
    "trapeze": lambda a=7, b=5, h=3: print(0.5 * (a + b) * h)
}

area["radius"](12)  # 75.3982

print((lambda a, b: a if a > b else b)(15, 13))  # 15 Перевірка на максимальне
# print((lambda x, y, z: z if z < (lambda x,y:x if x < y and z else y))(9, 8, 5))
print((lambda x, y, z: x if (x < y) and (y < z) else (y if (y < x) and (y < z) else z))(9, 8, 5))

"""  MAP()  """

# map(func,iterable)
# MAP() приймає функцію та ітеруємий обєкт
"""
def mul(t):
    return t * 2


s = [2, 8, 12, -5, -8]
stro = "Heelloo"
ls = dict(map(mul, stro))  # {'H': 'H', 'e': 'e', 'l': 'l', 'o': 'o'}
print(ls)
"""
s = [2, 8, 12, -5, -8]
ls = list(map(lambda t: t * 2, s))
print(ls)  # [4, 16, 24, -10, -16]

strok_list = ["1", "2", "3", "4", "5"]
s1 = list(map(int, strok_list))  # стане integer
print(type(s1[0]))  # <class 'int'>

areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
res = list(map(round, areas, range(1, len(areas) + 1)))
print(res)
print(round((5.233562654), 4))
""""""
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]
summ = list(map(sum, (l1, l2)))  # [6, 15]
print(summ)  # [6, 15]

# Тепер поелементно
l3 = []
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
print(l3)  # [5, 7, 9]

# Тепер із Mеп
res = list(map(lambda x, y: x + y, l1, l2))
print(res)  # [5, 7, 9]
""""""

"""    FILTER    """
# filter(func, iterable) Працює якщо фанк повертає True

t = ("abcd", "abc", "cdefg", "def", "ghi",)
print(tuple(filter(lambda s: len(s) == 3, t)))

b = [66, 90, 68, 59, 76, 88, 74, 81, 65]
res = filter(lambda s: s > 75, b)
print(res)  # <filter object at 0x000001BE06F37FD0>
res = list(filter(lambda s: s > 75, b))
print(res)  # [90, 76, 88, 81]

import random as ar

lst = [ar.randint(0, 50) for i in range(0, 10)]
print(lst)
f = list(filter(lambda x: 10 <= x <= 20, lst))
print(f)

liss = [45, 55, 60, 37, 100, 105, 220]
rez = list(filter(lambda x: x % 15 == 0, liss))  # [45, 60, 105]
print(rez)

lisst = [45, 55, 60, 37, 100, 105, 220]
rezult = list(filter(lambda i: not i % 15, lisst))  # [45, 60, 105]
print(rezult)

l = [i for i in range(1, 11)]
squirt = list(map(lambda x: x ** 2, list(filter(lambda i: i % 2 == 1, l))))  # [1, 9, 25, 49, 81]
print(squirt)

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10)))))  # [1, 9, 25, 49, 81]

print([x ** 2 for x in range(10) if x % 2 != 0])  # [1, 9, 25, 49, 81]

t = ("madam", "fire", "tomato", "book", "kiosk", "mom")

print(list(filter(lambda x: x[0::] == x[::-1], t)))  # ['madam', 'mom']

words = ("madam", "fire", "tomato", "book", "kiosk", "mom")
print(list(filter(lambda x: x == x[::-1], words)))  # ['madam', 'mom']

"""   DECORATORS   """


def hello():
    return "Hello I am func 'Hello'"


def super_func(func):
    print("Hello I am Super_func 'Hello'")  # Hello I am Super_func 'Hello'
    print(func())  # Hello I am func 'Hello'


super_func(hello)
# Hello I am Super_func 'Hello'
# Hello I am func 'Hello'
# _________________________________________________________

test = hello
print(test())  # Hello I am func 'Hello'


# def my_decorator(func):
#     def func_wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return func_wrapper
#
# def func_test():
#     print("Somethinf inside is happening")
#
#
# general = my_decorator(func_test)
# general()


def my_secorator(func):
    def func_wrapper():
        print("Code before")
        func()
        print("Code after")

    return func_wrapper


@my_secorator
def func_test():
    print("Somethinf inside is happening")


@my_secorator
def hello():
    print("Hello I am func 'Hello'")


hello()
func_test()


# general = my_secorator(func_test)
# general()

def bold(fn):
    def wrap():
        return "<b>" + fn() + "</b>"

    return wrap


def italic(fn):
    def wrap():
        return "<i>" + fn() + '</i>'

    return wrap


@bold
@italic
def hello():
    return "text"


print(hello())


def quantity(fn):
    cnt = 0

    def func():
        nonlocal cnt
        cnt += 1
        fn()
        print('Виклик', cnt)

    return func


@quantity
def test():
    print("Hello")


test()
test()
test()


def args_decorator(func):
    def personal_data(arg1, arg2):  # first, last
        print(func(arg1, arg2))  # first, last    None
        print("дані: ", arg1, arg2)  # дані:  Iren Mackenzy
        func(arg1, arg2)  # my name is Iren Mackenzy

    return personal_data


@args_decorator
def print_full_name(first, last):
    print("my name is", first, last)


print_full_name("Iren", "Mackenzy")


def args_decorator_TWO(fn):
    def wrap(*args, **kwargs):  # Зробить необхідну рорзпаковку
        print("args:", args)
        print("kwargs:", kwargs)
        fn(*args, **kwargs)

    return wrap


@args_decorator_TWO
def print_fullname_again(a, b, c, study="Python"):
    print(a, b, c, "Studying", study, "\n")


print_fullname_again("john", 'mackoley', "Jane", study="java")

print_fullname_again("Iraklii", 'Tesla', "Janett")
