"""
def outer(a1, b1, a2, b2):
    a = 0
    b = 0

    def inner():
        nonlocal a, b
        a = a1 + a2
        b = b1 + b2

    inner()
    return [a, b]
"""

# print(outer(2,3,-1,4))

# def square(a, b, c):
#     global s_par
#     s_par = 2 * (a * b + b * c + a * c)
#
#     def square_rectangle(a, b):
#         s_rect = a * b
#
#     square_rectangle(a, b)
#     return s_par
#
#
# def square1(a, b, c):
#     s_par = 0
#
#     def square_rectangle(a, b, c):
#         s_rect = a * b
#         nonlocal s_par
#         s_par = 2 * (a * b + b * c + a * c)
#
#     square_rectangle(a, b, c)
#     return s_par


""""""

"""
def rect_paral_square(a, b, c):
    def rect_square(i, j):
        return i * j  # площа прямокутника

    s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
    return s # площа паралелепіпеда


print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))
"""


# Глобальна змінна s
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j  # площа прямокутника
#
#     global s
#     s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
#     return s  # площа паралелепіпеда
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


def rect_paral_square(a, b, c):
    s = 0

    def rect_square(i, j):
        nonlocal s
        s += i * j

    rect_square(a, b)
    rect_square(a, c)
    rect_square(c, b)
    return 2 * s  # площа паралелепіпеда


# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

""""""
# Замикання
""""""


def outer(n):
    def inner(x):
        return n + x

    return inner  # Замкнення це ретюрн функції, без виклику функції


"""
add5 = outer(5)  # (outer(5)(10))
print(add5(10))  # 15
print((outer(5)(10)))  # 15

add6 = outer(6)
print(add6(10)) # 16
"""


def func1():
    a = 1
    b = "line"
    c = [1, 2, 3]

    def func2():
        c.append(4)  # в даному випадку зміниться (список змінний тип данних)
        # a+=1 - НЕ ПРАЦЮВАТИМЕ (незмінний тип)
        nonlocal a
        a += 1  # ТЕПЕР ПРАЦЮЄ після NONLOCAL
        # b = b + "2" НЕ ПРАЦЮВАТИМЕ (незмінний тип)
        nonlocal b
        b = b + "2"  # ТЕПЕР ПРАЦЮЄ після NONLOCAL
        return a, b, c

    return func2


func = func1()
# print(func())

""""""


def aparture(x):
    cnt = 0

    def calc():
        nonlocal cnt
        cnt += 1
        return x, cnt

    # print(x, "було відвідано") якщо замість вищого ретюрн це,
    return calc  # то виклик без print  і буде не кортеж


aparture1 = aparture("Kiiv")
# print(aparture1())
# print(aparture1())

aparture2 = aparture("Ternopil")
# print(aparture2())
# print(aparture2())
# print(aparture1())
""""""

"""
def appart(city):
    cnt = 0

    def calcul():
        nonlocal cnt
        cnt += 1
        print(city, cnt)
    return calcul

res = appart("Kiiv")
res()
res()
res2 = appart("Ternopil")
res2()
res2()
res()
"""

students = {
    'Alice': 98,
    'Bob': 67,
    'David': 85,
    'Chris': 75,
    'Ella': 54,
    "Fiona": 35,
    "Grace": 69
}


def outer(lower, upper):
    def inner(exam):
        return {k: v for (k, v) in exam.items() if lower <= v <= upper}

    return inner


a = outer(80, 100)
b = outer(70, 80)
c = outer(50, 70)
d = outer(0, 50)

print(a(students))
print(b(students))
print(c(students))
print(d(students))

"""students = dict(zip(["Alice","Bob", "David", "Chris", "Ella"],[98,67,85,75,54]))
print(students)"""  # {'Alice': 98, 'Bob': 67, 'David': 85, 'Chris': 75, 'Ella': 54}

# stu = {input("Key: "): i for i in range(5)}
"""print(stu) # {'Alice': 0, 'Bob': 1, 'David': 2, 'Chris': 3, 'Ella': 4}"""


def func_object(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def replace():
        pass  # обовязково чимось заткнути функцію

    replace.add = add  # тут функція add
    replace.sub = sub  # тут функція sub
    replace.mul = mul  # тут функція mul
    return replace  # сюди попаде або add, або sub, або mul,


# в залежності що буде викликано після крапки

obj1 = func_object(5, 2)  # сюди попадає replace
print(obj1.add())

obj2 = func_object(5, 2)
print(obj1.sub())

obj3 = func_object(5, 2)
print(obj1.mul())

print(type(func_object))

"""  LAMBDA  """


def func(x1, y1):
    return x1 + y1


# те саме що і це:
print((lambda x, y: x + y))

print(func(1, 2))
print((lambda x, y: x + y)(1, 2))

func1 = lambda x, y: x + y
print(func1(1, 2))
print(func1("a", 'b'))

print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2,c=3:a+b+c
#
# print(summ(10,20,30))

# func = lambda *args: print(args)
# (func(1, 2, 3, 4))

c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
for t in c:
    print(t("abc"))
""""""


def inc1(n):
    def inner(x):
        return x + n

    return inner


# те саме що наступне

def inc2(n):
    return lambda x: x + n


# те саме що наступне

inc = (lambda n: (lambda x: x + n))

#

F = inc(42)
print(F(2))

f = inc2(42)
print(f(2))
""""""
print((lambda n: (lambda x: x + n))(42)(2))

# print((lambda summ: (lambda a, b, c: a + b + c)(2)(4)(6)))
# sum3 = lambda a, b, c: a + b + c
# print(sum3(2,4,6))

sum3 = lambda a: (lambda b: (lambda c: a + b + c))
print(sum3(2)(4)(6))
""""""

d = {"r": 10, "b": 15, "c": 4}
list_d = list(d.items())
print(list_d)
list_d.sort(key=lambda i: i[0])
print(list_d)

""""""

listok = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
res = listok[3](12, 6)
print(res)

print(type(lambda x, y: x + y))

def outer(x):
    def inner(y):
        def inner_inner(z):
            return x+y+z

        return inner_inner