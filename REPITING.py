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
print(res())
print(Kiiv('Kiiv'))
print(Kiiv('Kiiv'))
print(Kiiv('Zhitomir'))
print(Kiiv("Kiiv")())
print(Kiiv("Kiiv")())
stingi = "proba"

print(stingi.strip("b"))
