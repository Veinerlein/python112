# def change(lst):
#     start = lst.pop()  # видаляю і зберігаю за змінною останній елемент
#     end = lst.pop(0)  # видаляю і зберігаю перший елемент
#     lst.append(end)  # в поточному списку (Список змінний тип даних) вставлю вкінець елемент змінної end
#     lst.insert(0, start)  # в поточному списку вставлю елемент змінної start у початковий індекс списку
#     return lst
#
#
# print(change(['цибуля', 23, 'морква', 42]))
#
#
# def is_grater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_grater(10, 5))
#
# # def chech_password(password):
# #     has_upper = False
# #     has_lower = False
# #     has_num = False
# #     for ch in password:
# #         if 'A' <= ch <= 'Z':
# #             has_upper = True
# #         elif 'a' <= ch <= 'z':
# #             has_lower = True
# #         elif "0" <= ch <= '9':
# #             has_num = True
# #     if len(password) >= 8 and has_upper and has_lower and has_num:
# #         return True
# #     return False
# #
# #
# # p = input("Password=>")  # 1234567890
# # if chech_password(p):
# #     print("good")
# # else:
# #     print("not good")
#
# import re
#
#
# def c_h(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for c in password:
#         if re.match(r'[A-Z]', c):
#             has_upper = True
#         elif re.match(r"[a-z]",c):
#             has_lower = True
#         elif re.match(r"[0-9]", c):
#             has_num = True
#     if has_upper and has_lower  and has_num:
#         return True
#     return False
#
# #ОБОВ'ЯЗКОВО ПЕРЕВІРЯТИ КОЖЕН ШАБЛОН ОКРЕМО, ЩОБ НЕ ПУТАТИ УСЕ РАЗОМ
#
# password = input("Passw:_")
# if c_h(password):
#     print("GOOD")
# else:
#     print("Not GOOD")
import timeit


# def check(user_name,password,min_length = 8, chack_user = True):
#     if len(password) < min_length:
#         print("TOO SHort")
#         # return False
#     elif chack_user and user_name in password:
#         print("Consisting username")
#         # return False
#     else:
#         print("GOOD")
#         # return True
#
# print(check("BOB","BOB"))

def sum_even(a, odd=False):
    summ = 0  # 'Перемінна для підсумування'
    while a != 0:  # цикл вайл з умовою виходу коли зникне останнє число
        b = a % 10  # беру останню цифру із числа у змінну b
        if b % 2 == 0 and odd == False:  # перевірка на парність
            summ += b  # додавання кожної парної b
        if b % 2 == 1 and odd == True:  # перевірка на непарність
            summ += b  # додаванна кожної непарної b
        a = a // 10  # обрізання останньої цифри із числа і зберігаю обріз числа у перемінну a

    return summ


def wrapper(b, odd, summ):
    if b % 2 == 0 and odd == False:  # перевірка на парність
        summ += b  # додавання кожної парної b
    if b % 2 == 1 and odd == True:  # перевірка на непарність
        summ += b  # додаванна кожної непарної b
    return summ, b


print(sum_even(9874023))


def sum_evenTEST_WITH_DECORATOR(a, odd=False):
    summ = 0  # 'Перемінна для підсумування'
    while a != 0:  # цикл вайл з умовою виходу коли зникне останнє число
        b = a % 10  # беру останню цифру із числа у змінну b
        wrapper(b, odd, summ)

        a = a // 10  # обрізання останньої цифри із числа і зберігаю обріз числа у перемінну a
    return summ


print(sum_evenTEST_WITH_DECORATOR(9874023))

a = [1, 2, 3]
b = [*a]
print(b)


def func(*args):
    return args


print(func(1))
print(1, 3, 5, "abc")
print(func())


def summa(*params):
    res = 0
    for n in params:
        res += n

    return res


a = summa(1, 2, 3, 4, 5, 6, 7, 8, 9)
b = summa(1, 2, 3)
print(a)
print(b)


def funcikc(*args):
    dictionary = {i: i for i in args}
    return dictionary


print(funcikc('gray', (2, 17), 3.11, -4))


def less_then_avarage(*args):
    summa_usih = 0
    kilk = 0
    l = []
    for element in args:
        summa_usih += element
        kilk += 1
    average = summa_usih / kilk
    print(average)
    for i in args:
        if i < average:
            l.append(i)
    return l


print(less_then_avarage(1, 2, 3, 4, 5, 6, 7, 8, 9))


def cg(*args):
    r = sum(args) / len(args)
    d = []
    for i in args:
        if i < r:
            d.append(i)
    return d


def ff(stud, *scores):
    a = "stud_name:" + stud
    s = []
    for score in scores:
        s.append(score)
    print(a, end="- ")
    print(*s)


(ff("man", 111, 98, 86, 75, 788, 75, ))
(ff('WOM', 1, 2, 3))


def reverinio(*args, even=True):
    sps = []
    for a in args:
        a = str(a)
        if even == True:
            sps.append(int(a[::-1]))
        elif even == False and int(a) % 2 == 1:
            sps.append(int(a[::-1]))
    return sps


# print(reverinio(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(reverinio(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, even=False))


def revero(*args, only_odd=False):
    l = list(map(lambda a: int(str(a)[::-1]), args))
    if only_odd == True:
        l = list(filter(lambda a: a % 2 == 1, args))
        l = list(map(lambda a: int(str(a)[::-1]), l))
    return l


# print(revero(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(revero(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


def rev(*args, only_odd=False):
    l = list(map(lambda a: int(str(a)[::-1]), args))
    if only_odd == True:
        l = list(map(lambda a: int(str(a)[::-1]) if a % 2 == 1 else 0, args))
    return l


# print(rev(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(rev(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

def rasvert(*args, only_odd=False):
    li = []
    for a in args:
        if only_odd == False:
            b = str(a % 10)
            c = str(a // 10)
            li.append(int(b + c))
        elif only_odd == True and a % 2 == 1:
            b = str(a % 10)
            c = str(a // 10)
            li.append(int(b + c))
    return li


# print(rasvert(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(rasvert(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# Define some test data
data = list(range(1000000))


# Time the rev function
# print("Time taken by rasvert function:", timeit.timeit(lambda: rasvert(*data, only_odd=True), number=10))

# Time the reverinio function
# print("Time taken by reverinio function:", timeit.timeit(lambda: reverinio(*data, even=False), number=10))

# f1_function = timeit.timeit(lambda: rasvert(*data, only_odd=True), number=10)
# f2_function = timeit.timeit(lambda: reverinio(*data, even=False), number=10)


def SPEED_CHECKING264(f1_function, f2_function):
    f1function = timeit.timeit(lambda: f1_function(*data, only_odd=True), number=10)
    f2function = timeit.timeit(lambda: f2_function(*data, only_odd=True), number=10)
    print(f1function, f2function, sep="\n")
    if f1function > f2function:
        a = {f2_function: f2function}
    else:
        a = {f1_function: f1function}
    print("Faster is:", a)


def reverse_num(n):
    return int(str(n)[::-1])


def functt(*args, only_odd=False):
    res = []
    for i in args:
        if not only_odd or (only_odd and i % 2 != 0):
            res.append(reverse_num(i))  # якщо не виносити в окрему функцію, код виконується швидше
    return res


def functt2(*args, only_odd=False):
    res = []
    for i in args:
        if not only_odd or (only_odd and i % 2 != 0):
            res.append(int(str(i)[::-1]))  # якщо не виносити в окрему функцію, код виконується швидше
    return res


# print(functt(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(functt(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


my_dict = {"one": "first"}


def fff(**kwargs):
    for key, val in kwargs.items():
        my_dict.update({key: val})
    return my_dict


print(fff(firstname="Somebody", lastname="Anybody", middlename="bobosindra"))
print(fff(BOB="KLAUSTRAFOB"))

my_dict1 = {"one": "first"}

"""
def fff(**kwargs):
    my_dict1.update(**kwargs)
    return my_dict1
"""

result = 10 // 3 + (10 % 3 > 0)  # В цьому випадку ми хочемо, щоб результат ділення
# був округленим до більшого цілого числа, якщо ділення не є точним. Наприклад,
# коли ми ділимо 10 на 3, результатом є 3 з залишком 1. Якщо ми застосуємо лише
# оператор цілочисельного ділення //,
# то ми отримаємо 3. Щоб отримати округлений результат до більшого цілого числа,
# нам потрібно додати 1 до результату, якщо залишок від ділення більше за нуль.
# Тому, додавши (10 % 3 > 0) до цілочисельного ділення 10 // 3,
# ми отримуємо результат,  який буде округленим до
# більшого цілого числа, якщо ділення не є точним. Якщо ж ділення є точним,
# тобто залишок від ділення дорівнює 0, то додання (10 % 3 > 0) не змінить результату,
# оскільки вираз (10 % 3 > 0) буде дорівнювати False.
print(result)

# SPEED_CHECKING264(functt, functt2)

# 2.5107066000000486
# 2.249957400000085
# Faster is: {<function functt2 at 0x000002060D074E50>: 2.249957400000085}
kilk = 3
l = [["PPPPP", 4], ["PPP", 6], ['PPPP', 4], ["PPPPP", 7]]
for element1, element2 in l:
    # print(element1 + " " + f'{element2}')
    # print(min(max(element2 - len(element1), 0), kilk))
    pass


def outer(a1, b1, a2, b2):
    a = 0
    b = 0

    def inner():
        nonlocal a, b
        a = a1 + a2
        b = b1 + b2

    inner()
    return a, b


# print(outer(2,3,-1,4))

# local
def square(a, b, c):
    # S = 2*(a*b+a*c+b*c)
    def square2(i, j):
        S1 = i * j
        return S1

    S = 2 * (square2(a, b) + square2(a, c) + square2(b, c))

    return S


print(square(2, 4, 6))

# global
S = 0


def square(a, b, c):
    # S = 2*(a*b+a*c+b*c)
    def square2(i, j):
        S1 = i * j
        return S1

    global S
    S = 2 * (square2(a, b) + square2(a, c) + square2(b, c))

    return S


print(square(5, 8, 2))


# nonlocal
def square(a, b, c):
    # S = 2*(a*b+a*c+b*c)
    S = 0

    def square2(i, j):
        nonlocal S
        S += i * j

    square2(a, b)
    square2(a, c)
    square2(b, c)
    return S * 2


print(square(1, 6, 8))


# Замкнення - це не виклик вкладеної функції, а виклик результату вкладеної функції
def outeri(n):
    def inner(x):
        return n + x

    return inner


add = outeri(5)
print(add(10))
print(outeri(5)(10))


def func1():
    a = 1
    b = "line"
    c = [1, 2, 3]

    def func2():
        nonlocal a, b  # для незмінного типу даних використовую нон локал
        c.append(4)  # тому що списки можна змінювати
        a = a + 1
        b = b + "2"
        return a, b, c

    return func2


func = func1()
print(func())


def Kiiv(k):
    cnt = 0

    def Zhitomir():
        nonlocal cnt
        cnt += 1
        return k, cnt

    return Zhitomir


res = Kiiv('Kiiv')
print(res())
print(res())  # буде збільшуватись cnt оскільки функція як і її результат буде зберігатись у змінній res
# без реєстрації у змінній, область у памяті так і залишиться областю памяті, і не реагуватиметься.
print(Kiiv('Kiiv'))  # <function Kiiv.<locals>.Zhitomir at 0x000002D83C571360>
# print(Kiiv('Kiiv')) тому що без круглих дужок викликаємо функцію
print(Kiiv('Zhitomir'))  # <function Kiiv.<locals>.Zhitomir at 0x000002D83C571360>
print(Kiiv("Kiiv")())
print(Kiiv("Kiiv")())
stingi = "proba"

print(stingi.strip("b"))

students = {
    "Alice": 98,
    "Bob": 67,
    "David": 85,
    "Chris": 75,
    "Ella": 54,
    "Fiona": 35,
    "Grace": 69,
}


def outers(lower, upper):
    def inner(exam):
        return {k: v for k, v in exam.items() if lower <= v <= upper}

    return inner


a = outers(80, 100)
b = outers(70, 80)
c = outers(50, 700)
d = outers(0, 50)
print(a(students))
print(b(students))
print(c(students))
print(d(students))


def funcobj(a, b):
    def add():
        return a + b

    def mul():
        return a * b

    def sub():
        return a - b

    def replace():  # ця функція по суті повязує, це як ланцюг для задіяння методів прописаних вище через .(назва функції)
        pass  # і виклик

    replace.add = add  # це код передбачення для імовірного виклику методу функції  print(obj1.add())
    replace.sub = sub  # тобто це МеТоД запиту функції у середині функції, а виклик буде уже коли даю дужки print(obj1.add())
    replace.mul = mul
    return replace  # У replace попадає функція funcobj   #   print(funcobj(5, 2).add())  == 7


obj1 = funcobj(5, 2)  # Записали сюди результат виведення функції funcobj, а саме replace.
obj2 = funcobj(5, 2)
obj3 = funcobj(5, 2)
# print(obj1.add())
print(obj1.add())  # 7 в обох випадках
print(funcobj(5, 2).add())  # 7 відпрацював одинаково

print((lambda x, y: x + y)(3, 5))
print((lambda x, y: x ** 2 + y ** 2)(2, 5))
summ = lambda a=1, b=2, c=3: a + b + c
print(summ(30, c=10))
print((lambda *args: args)(1, 2, "fgdd", 4))

c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
for i in c:
    print(i("10"))


def inc(n):
    return lambda x: x + n


f = inc(42)
print(f(2))

print(inc(30)(3))


def incognito(n):
    return lambda x: x + n


inc2 = (lambda n: (lambda x: x + n))

print(inc2(10)(20))  # 10 впаде в n, а 20 у x

print((lambda a: (lambda b: (lambda c: c + a + b)))(2)(4)(6))

d = {"e": 10, "b": 15, "c": 4}
list_d = list(d.items())
print(list_d)
list_d.sort(key=lambda i: i[1])
print(list_d)

a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
b = a[2](12, 6)  # спрацює конкретно тільки множення
print(b)

print(type(lambda x, y: x + y))

players = [{'name': 'Andron', 'last name': 'Buterin', 'rating': 9},
           {'name': "Alexandr", 'last name': "Macedonian", 'rating': 10},
           {'name': "Phrodo", 'last name': "Beggins", 'rating': 4},
           {'name': "Michel", 'last name': 'Jexon', 'rating': 6}]

# for d in players:
#     print(d['last name'])
# for person in d.items():
#     print(person)
print(players)
print(players.sort(key=lambda x: x['rating'], reverse=True))  # None По суті,
# це говорить, що будь-які мутації в списку можуть призвести до помилок сегментів,
# і оскільки функція key може виконувати довільний код, список спорожняється.

print(sorted(players, key=lambda x: x["rating"], reverse=True))  # has result
# sortedлише обходить цю проблему, оскільки він негайно копіює список,
# і таким чином «копія»
# сортується. Це означає, що
# оригінал players залишається цілим і його можна використовувати.

a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
b = [-3, 10, 0, 1]
for i in b:
    if i < 0:
        print(a['two'](i))
    elif i > 0:
        print(a["one"](i))
    else:
        print(a["three"](i))

a1 = [lambda x: x - 1, lambda x: abs(x) - 1000, lambda x: x]
b1 = [-3, 10, 0, 1]
for i in b1:
    if i < 0:
        print(a1[1](i))
    elif i > 0:
        print(a1[0](i))
    else:
        print(a1[2](i))

d = {
    1: lambda: print("Monday"),
    2: lambda: print("Tuesday"),
    3: lambda: print("Wednesday"),
    4: lambda: print("Thursday"),
    5: lambda: print("Friday"),
    6: lambda: print("Saturday"),
    7: lambda: print("Sanday"),
}
f = (d[2])
f()
print(type(f))
print(type(d))
print((lambda a, b: a if a > b else b)(12, 13))

print((lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))(6, 2, 18))


def mul(t):
    return t * 2


s = [2, 3, 132, -5, -8]
ls = map(mul, s)  # пройдеться по послідовності і виконає функцію
print(ls)
print(set(ls))  # set() видалить дублікати, якщо такі існують

# замість mul функції, ви користаємо lambda.
print(list(map(lambda t: t * 2, s)))
# можна кожен елемент любої послідовності обробити функцією map(), пізніше тільки вказати тип вихідних даних.

areas = [3.46773, 5.67334, 4.543654, 56.1263442, 9.2345232, 32.6346546]
res = list(
    map(round, areas, range(1, len(areas) + 1)))  # третій аргумент у map() це аргумент функції, яка є аргументом у
# map(), але аргумент повинен змінюватись як range() (взяли по довжині списку)
# якщо діапазон поставити менший, то цикл пройде меншу кількість ітерацій
print(res)

rounded_areas = list(map(lambda x: round(x, 2), areas))
print(rounded_areas)
print(list(map(lambda x, y: x + y, [1, 5, 6], [2, 8, 4])))

print(list(map(lambda x, y: x + y, ([1, 5, 6]), ([2, 8, 4]))))
# filter працює як і map(), але не виконує опцій із даними, а просто повертає дані по конкретній умові.


# print(r"C:\file.txt\") - Raw strings не дозволяють ставити слеш в кінці
print(r"C:\file.txt\\"[:-1])  # C:\file.txt\
print(r"C:\file.txt" + "\\")  # C:\file.txt\
print("C:\\file.txt\\")  # C:\file.txt\

name = 'Damian'
print(f"my name is {name}")

import math as m

print(f"PI number is:{m.pi:.2f}")

a = 75

print(f"a char is {{{a}}}")  # a char is {75}


def doc(a, b):
    """
    simple calculating
    :param a: first parametr
    :param b: second parametr
    :return: result, sum of parameters
    """
    return a + b


print(doc.__doc__)  # поверне усі задокументовані дані


# print(ord.__doc__)  # Return the Unicode code point for a one-character string.


#  СПИСКИ КАНКАТЕНУЮТЬСЯ

def symbols(a=122, b=97):
    return "-".join([chr(x) for x in range(b, a + 1)]) if a > b else " ".join([chr(x) for x in range(a, b + 1)])


# JOIN РОБИТЬ з любого списку строку, і не треба ніякого map із print

# simple code here
"""
def symbols_loop(a=122,b=97):
    if a>b:
        for x in range(b, a+1):
            print(chr(x),end="..")
    else:
        for s in range(a, b+1):
            print(chr(s),end="..")
    print()
symbols_loop()
"""

# вивід усіх символів між а і b
print(symbols())


def obmin(a="one two"):
    res = "".join(a[a.find(" ") + 1:] + " " + a[:a.find(" ")])
    return res


def obmin2(a="one two"):
    res = a.split(" ")
    res = res[1] + " " + res[0]
    return res


a = "one two"
print(a[a.find(" ") + 1:] + " " + a[:a.find(" ")])
print(obmin2())
print(obmin())


def exvert(s="ab12c59p7bq"):
    digits = []
    for el in s:
        try:
            s = int(el)
            digits.append(s)
        except ValueError:
            pass
    return digits


print(exvert())


def exvert2(s="ab12c59p7bq"):
    digits = []
    for el in s:
        if el.isdigit():
            digits.append(int(el))
        else:
            pass
    return digits


def extract(s="ab12c59p7bq"):
    digits = []
    for ii in s:
        if ii in "0123456789":  # could be method "0123456789".find(ii)
            digits.append(int(ii))
    return digits


print(exvert2())
print(extract())

print("MArteta MikelM".strip("M"))
string = "MArteta MikelM"
rez = ""
for s in string:
    if s.isspace():
        pass
    else:
        rez += s
print(rez.strip("M"))

print("=" * 56)  # ==================================================
"""Mixins"""


class Student:
    def __init__(self, name="fdsaf"):  # ініціалізатор для студента
        self.name = name
        self.note = self.Laptop()  # для того щоб могти використовувати метод вкладеного класу, створюю
        # його об'єкт і зберігаю і змінну

    def show(self):
        print(self.name, end="")  # реалізація методу
        self.note.show()  # запуск методу із вкладеного класу

    def change_parameters(self, model, processor, memory):  # додаткова функція для можливості змінювати
        self.note = self.Laptop(model, processor, memory)  # змінювати параметри об'єкту вкладеного класу

    class Laptop:
        def __init__(self, model="HP", processor='I7', memory='16'):  # немає функції передачі параметрів,
            # є лише метод їх зміни
            self.model = model
            self.processor = processor
            self.memory = memory

        def show(self):
            print(f" => {self.model}, {self.processor}, {self.memory}")


p = Student("Roman")
p2 = Student("Vovan")

p.show()
p2.show()
p2.change_parameters("Dell", "Ryzen7", "16")
p2.show()

print(Student.__doc__)
print(Student.__dir__)
print(dir(Student))

p1 = Student()
print(p1.name)
# p1.name = "fhdsjlfhdasl"
print(p1.name)
print(p1.__dict__)


class Poin:
    x = 3
    y = 4  # print(Poin.y)

    def __new__(cls, *args, **kwargs):
        print("ВИклик __new__ для " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):  # print(getattr(obt, "y"))
        print("ВИклик __init__ для " + str(self))
        self.x = x  # print(pt.x)
        self.y = y  # print(pt.y)
        self.z = __class__.__name__


pt = Poin(1, 2)
obt = Poin()
print(obt.__dict__)
print(Poin.y)
print(pt.__class__.__name__)
print(pt.x)
print(pt.y)
print(getattr(obt, "y"))

"""SINGLETON"""


class DataBase:
    __instance = None  # посилання на екземпляр класу (патерн Sangleton)

    def __new__(cls, *args, **kwargs):  # надає адресу області памяті
        if cls.__instance is None:  # якщо він нан, то
            cls.__instance = super().__new__(cls)  # тут буде адреса нового об'єкту, якщо нан
        # якщо не нан, то поверне адресу раніше створеного об'єкту
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None  # якщо мусор видалить екземпляр, то знову буде прийматись нан,
        # а, отже, знову буде виконуватись рядок коду із умовою "if cls.__instance is None"
        # і буде мати можливість створюватись 1 екземпляр

    def __init__(self, x, y, z):  # надає значення змінним
        self.user = x
        self.psw = y
        self.port = z

    def connect(self):
        print(f"Connection with database: {self.user},{self.psw},{self.port}")

    def close(self):
        print('Closing connection with database')

    def read(self):
        return "database data"

    def write(self, data):
        print(f"Loading to DB {data}")


db = DataBase("root", "1234", 80)
db2 = DataBase("root2", "4321", 17)
print(id(db), id(db2))
# 1938657974144 1938657974144 - рівність айді означає, що об'єкт посилається на один і той
# же район пам'яті
print(db.__dict__)  # {'user': 'root2', 'psw': '4321', 'port': 17}
print(db2.__dict__)  # {'user': 'root2', 'psw': '4321', 'port': 17}

print("=" * 98)  # =================================================


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # метод класу працює лише із атрибутами цього класу
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def validate2(self, x):
        return Vector.MIN_COORD <= x <= Vector.MAX_COORD  # працює АЛЕ погана практика
        # адже часто у великих проектах змінюється нізви класів

    @staticmethod
    def validate3(x, y):
        return __class__(x, y).MIN_COORD <= y + x <= __class__(x, y).MAX_COORD  # те саме що і з
        # класvетодом, тільки тут я вдався до передачі лишніх аргументів, які унеможливлюють
        # помилку. (Хоча лишній х ніяк не задіяний)(задіяв)

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x,y):
        return x*x+y*y


v = Vector(1, 2)
res = v.get_coord()
print(Vector.validate(6))
ress = Vector.get_coord(v)
print(res, '==', ress)
print(Vector)
print(Vector.get_coord(v))
print(Vector.MIN_COORD)
print(Vector.MAX_COORD)

# print(Vector.validate2(5)) - не працює так
print(v.validate2(6))
print(v.validate3(7, 1118))
print(v.norm2(5,6))


