a = [1, 2, 3]
b = [*a, 4, 5, 6]  # розпаковка a летить сюди [1, 2, 3, 4, 5, 6]


# print(b)

#
# def func(*args):
#     return args
#
#
# print(func())
#
#
# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res


# a = summa(1, 2, 3, 4, 5, 6, 7, 8)
# b = summa(1, 2, 3)
# print(a)
# print(b)
#
#
# def dict_back(*args):
#     d = {}
#     for i in args:
#         d[i] = i
#     return d
#
#
# print(dict_back(1, 2, 3, 4, "one"))
#
#
# def ser_ar(*args):
#     suma = 0   #  можна просто sum() і не використовувати наступний цикл
#     for i in args:
#         suma += i
#     ser_ar = suma / len(args)
#     l = []
#     for i in args:
#         if i < ser_ar:
#             l.append(i)
#     print(ser_ar)
#     return l
#
#
# print(ser_ar(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ser_ar(3, 6, 1, 9, 5))
#
#
# def func(student,*scores):
#     print("Student name: " + student, end=" ")
#     s = []
#     for score in scores:
#         s.append(score)
#     print(*s, sep=", ")
#     return "."
#
# print(func("John", 100,78, 95,89, 56, 99, 92, 88))
# print(func("Ddsopk",2,3,"adfbgf"))
#
#
# def reverso(*args, only_odd=False):
#     numbers = []
#     for n in args:
#         if only_odd==False:
#             number = str(n % 10) + str(n // 10)
#             numbers.append(int(number))
#         else:
#             if n%2!=0:
#                 number = str(n % 10) + str(n // 10)
#                 numbers.append(int(number))
#     return numbers
#
# print(reverso(12,2345,323,4456,5687,62,734,81,91))
# print(reverso(12,2345,323,4456,5687,62,734,81,91,only_odd=True))
#
# def revers_num(n):
#     s = str(n)
#     return int(n[::-1])
#
#
# def funct(*args, only_odd=False):
#     numbers = []
#     for n in args:
#         if not only_odd or (only_odd and n%2 !=0):
#             numbers.append(revers_num(n))
#     return numbers
#
# print(funct(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(funct(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def functs(**kwargs):
#     return kwargs
#
# # print(functs(a=1, b=2, c=3))
#
# def info(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
# info(firstname="Irina", lastname = "Saunal", age = 22, phone = 1124564789)
# info(firstname="Igor", lastname = "Wood",email='igor@gmail.com' ,age = 20, phone = 1124564789, country= "UK")
#
# my_dict = {"one":"first"}
# def refresh(**kwargs):
#     my_dict.update(kwargs)
#     return my_dict
#
# print(refresh(k1=22,k2=31,k3=11,k4=91))
# print(refresh(name="Bob",age=31,weight=61,eyes_color="grey"))
#
# def db(**kwargs):
#     my_dict1.update(kwargs)
#
# my_dict1 = {'one':"first"}
# db(k1=22,k2=31,k3=11,k4=91)
# db(name="Bob",age=31,weight=61,eyes_color="grey", k1=23)
# print('my_dict=', my_dict1)

def func(a, *args, b=False, **kwargs):
    return a, args, b, kwargs


print(func(1, 2, 3, 4, b=True, x=11, y=12, z=13))


def func(*args):
    print(args[0])


func(1, 2, 3, 4, 5, 6)


def func2(**kwargs):
    print(kwargs["one"])


func2(one=123, two=456)

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, "one": 1, 'two': 2, **y}
print(z)
"""

# SCOPE - область бачення

4 види
"""
name = "Tom"  # Global


def hi():
    global name  # Became global  перезаписали name як обєкт
    name = "Sam"  # Local but if "global name" mentioned above it is become global as new object
    print("Hello, ", name)


def bye():
    print("Good bye, ", name)


print(name, id(name))  # до виклику функцій нижче змінна name
# працює як Global із самого першого визначення
hi()
bye()
print(name, id(name))
i = 5  # інфа


def Opanas(arg=i):  # тут пішов в школу і вивчив що і = 5
    print(arg)


# А тут він школу закінчив і не знає далі що відбувалось

i = 6
Opanas()  # 5  звонимо до Опанаса і він не в курсі що
# що і помінялась, бо в школі вивчив що і = 5

Enclosing_Scope = "Ім'я в локальнцій області видимості любої об'ємної функції" \
                  "яка оголошена з інструкціями def і lambda зсередини назовні"

Built_in_Scope = "Встроєна область видимості на рівні мови Python." \
                 " Призначені імена в модулі встроєних імен: open, range, set, print"
# ____________________________________
# __'Built-in(B)'__________________ |
# |  __"Global(G)"_____________    | |
# |  |   __'Enclosed(E)'_____ |    | |
# |  |   |  ___"Local(L)"___| |    | |
# |________________________________| |
# ________________________________|_|

""""""


def add_two(a):
    x = 2

    def add_some():
        print("x = ", x)
        return a + x

    return add_some()


print(add_two(6))


# x=4
# def fun():
#     print(x+3)
#
# fun()

# import builtins
#
# names = dir(builtins)
# for t in names:
#     print(t)


def outer_f(who):
    def inner_f():
        print("Hello, ", who)

    inner_f()


outer_f('World!')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         # a = 4
#         print("Сума внітрішньої функції:", a + b)
#
#     print("Значення зовнішньої функції a:", a)
#
#     fun2(4)
#
#
# fun1()

x = 25


def fn():
    global t
    a = 30
    t = a
    print("global:", x)

    def inner():
        nonlocal a
        a = 35
        print(a)

    inner()
    print(a)
    t = 35


fn()
z = x + t
print(z)


def fn1():
    x1 = 25

    def fn2():
        x1 = 33

        def fn3():
            # nonlocal x1
            x1 = 55

        fn3()
        print("fn2.x1= ", x1)

    fn2()
    print("fn1.x1 = ", x1)


fn1()
