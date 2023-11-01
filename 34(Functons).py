# functions
# def hello(name, word):  # arguments
#     print("Hello,", name, ". Say ", word, sep="")
#
#
# hello("John", "hi")  # parammetres
# hello("Junior", "hello")  # parammetres
#
#
# def get_sum(a, b):
#     print(a + b)
#
#
# n = 2
# m = 5
# get_sum(n, m)
# x = 1
# y = 8
# get_sum("abc", "ABC")
#
# get_sum(2.5, float("4.5"))


# def mon(a, b, c):
#     string = ""
#     cnt = 1
#     while cnt <= c:
#         string += a
#         cnt += 1
#         if cnt<c:
#             string += b
#             cnt += 1
#     print(string)
#
# mon('+', '-', 9)
# mon("X", "0", 7)
#
# def symbol(x,y,z):
#     s = ""
#     for i in range(z):
#         if i%2==0:
#             s+=x
#         else:
#             s+=y
#     print(s)
#
# symbol('*', '#', 9)
# symbol("A", "8", 7)


def get_sum(a, b):
    # print("Сума: ")
    return a + b


n = 2
m = 5
res = get_sum(n, m)


# print(res)


def maximum():
    a = int(input('Put a: '))
    b = int(input('Put b: '))
    if a > b:
        return a - b
    elif a < b:
        return a + b
    else:
        return "Equal"


# m = maximum()
# print(m)

def cub(a):
    for x in range(1, 11):
        print(f"{x} in cube = {x ** 3}")


# (cub(3))

# def cube(a):
#     return a*a*a
#
# for i in range(1,11):
#     print(i,"в кубі = ", cube(i))


# Фібоначі - послідовність де кожне наступне рівно сумі попередніх двох
# 0 1 1 2 3 5 8 13 21

def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        x = a  # x=a+b
        a = b  # a=b
        b = x + a  # b = x  або просто a,b = b,a+b замість іншого коду


# fibo(25)


def change(lst):
    resl = []
    for i in lst:
        ind = lst.index(i)
        if ind == 0:
            resl.append(lst.pop(0))
            resl.append(lst.pop())
            lst.insert(0, resl[-1])
            lst.append(resl[0])
    return lst


# print(change([9,12,33,54,105]))

def list_changer(lst):
    l = lst
    result = [l[-1], l[1:-1], l[0]]
    final = []
    for i in result:
        for x in i:
            final.append(x)
    return final


print(list_changer("fgss"))


def ch(s):
    a = s[0]
    b = s[-1]
    for i in range(len(s)):
        if i == 0:
            s[i] = b
        elif i == len(s) - 1:
            s[i] = a
        print(s[i], end=" ")


ch([1, 2, 3, 5, 6, 7])


def changer2(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(changer2([9, 12, 33, 54, 105]))


def start(lst):
    start = lst.pop()  # 105
    end = lst.pop(0)  # 9
    lst.append(end)
    lst.insert(0, start)
    return lst


print(start([9, 12, 33, 54, 105]))


def squere():
    a = int(input("1 side: "))
    b = int(input("2 Side: "))
    return print("Squere is", a * b)


def triangle():
    a = int(input("1 side: "))
    h = int(input("high is: "))
    return a * h / 2


def cirle():
    pi = 3.14
    choice = input("if you have radius press r, if diametr - press d: ")
    if choice == "r":
        radius = int(input("radius is: "))
        return 2 * pi * radius
    if choice == "d":
        diametr = int(input("diametr is: "))
        return pi * diametr
    else:
        print("Your enter was not correct, please press r or d, "
              "(no big letters and English only")
        return cirle()


def enter_func():
    enter = int(input("1 - Square,2 - Triangle, 3 - Circle: "))
    if enter == 1:
        squere()
    elif enter == 2:
        triangle()
    elif enter == 3:
        cirle()
    else:
        print("you did not press the correct number")
        return enter_func()


# enter_func()

def numbers(numbers):
    list_usual = []
    list_simple = []
    for n in numbers:
        if n==1:
            numbers.remove(n)
        elif n % 2 == 0 or n % 3 == 0 and n!=2 and n!=3:
            list_usual.append(numbers.pop(numbers.index(n)))
    return max(list_usual), min(numbers)


print(numbers([6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]))






