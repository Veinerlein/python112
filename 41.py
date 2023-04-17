"""

         Strings """


def ser_ariph(fn):
    def wrapper(*args):
        return fn(*args) / len(args)

    return wrapper


@ser_ariph
def function(*args):
    sum = 0
    for a in args:
        sum += a
    return sum


print(function(2, 3, 3, 4))

str1 = "I am learning Nuthon. I like Nuthon." \
       " Nuthon is very interesting programming lenguage."


def letter_in_string_chenger(str, old, new):
    res_str = ""
    for s in range(len(str)):
        if str[s] == old and s % 2 != 0:
            res_str += new
        else:
            res_str += str[s]
    return res_str


print(letter_in_string_chenger(str1, "N", "P"))


def udal(slovo, n):
    res_s = ""
    for s in slovo:
        if slovo.index(s) == n:
            res_s += ""
        else:
            res_s += s
    return res_s


print(udal("Словосполучення", 5))
print(udal("0123456789", 4))

print("+++++++++++++++++++++++++")

print(u"Hello")  # do not use
print(r"I\'m")  # roll string

print(r"C:\file.txt\\"[:-1])  # C:\file.txt\
print(r"C:\file.txt" + "\\")  # C:\file.txt\
print("C:\\file.txt\\")  # C:\file.txt\

print(b"")
print(f"{3}")

name = "David"
age = 20
print("My name is ", name, ". I am ", age, " years old. ", sep="")
print("My name is " + name + ". I am " + f"{age}" + " years old. ")
print("My name is " + name + ". I am " + str(age) + " years old. ")
print(f"My name is {name}. I am {age} years old.")

import math as m

print(f"number pi: {m.pi:.2f}")  # number pi: 3.14
print(f"13/3= {round(13 / 3, 2)}")  # 13/3= 4.33

x = 13
y = 3

print(f"{x}/{y} = {round(x / y, 2)}")  # 13/3 = 4.33

a = [1, 2, 3, 4, 5, 6]
print(f"Third element {a[2] * 2}")  # Third element 6

name = "Friend"
prof = "Programmer"
lang = "Python"

message = (
    f"Hello {name}. "
    f"You are {prof}. "
    f"On language {lang}."
)

print(message)

a = 74

print(f"{{{a}}}")  # {74}
d = "my_doc"
f = "data.txt"
print(fr"home\{d}\{f}")  # home\my_doc\data.txt
print(f"home\\{d}\\{f}")  # home\my_doc\data.txt
print("home\\" + d + "\\" + f)  # home\my_doc\data.txt

s = """
<div>
    <a href='#'>content</a>
</div>
"""

print(s)
print(br"3452")

"""
             DOCUMENTATION
                               """


def square(n):
    """take number n and returns square of n"""
    a = n ** 2

    return a


print(square(5))

print(square.__doc__)  # take number n and returns square of n

import math


def cylinder(r, h):
    """
    Calculate square of cylinder.

    Calculate square of cylinder basis on height and basic radius
    :param r: positive number, radius of cylinder
    :param h: positive number, height of cylinder
    :return: positive number, square of cylinder
    """
    return 2 * math.pi * r * (r + h)


print(cylinder(2, 4))
print(cylinder.__doc__)

print("+++++++++++++++++++++++")

a = "Hello"
print(len(a))
print(ord("a"))  # 97 - код символу в ASCII

print(ord("#"))  # 35
print("++++++++++++++++++++++++++++++++")
# while True:
#     n = input("->")
#     if n !="-1":
#         print(ord(n))  # задане число в коді ASCII
#     else:
#         break

print("+++++++++++++++++++++++++++++++++++++++")

str2 = "Test string for me"
l_ASCII = []
summ = 0
for s in str2:
    l_ASCII.append(ord(s))
    summ += ord(s)
serarph = summ / len(l_ASCII)
l_ASCII.insert(0, round(serarph))
print(summ)
print(l_ASCII)
print(f"{serarph:.0f}")
print(round(serarph))
cnt = 0
symbols = ""
# while cnt<3:
#     enter = input("Ввести символ: ")
#     symbols +=f" {enter} "
#     if ord(enter) in l_ASCII:
#         pass
#     else:
#         l_ASCII.append(ord(enter))
#     cnt+=1
# print(symbols)
# print(l_ASCII)

el_equal_last = 0
for i in l_ASCII[:-1]:
    if i == l_ASCII[-1]:
        el_equal_last += 1
print(el_equal_last)
sort_list = sorted(l_ASCII, reverse=True)
print(sort_list)

print("++++++++++++++++++++++++++++++++++++++++++++")

my_str = "Test string for me"

arr = [ord(x) for x in my_str]
print(arr)

arr.insert(0, int(sum(arr) / len(arr)))  # 95 appeared in our list on 0 position
print(arr)
# arr = [int(sum(arr) / len(arr))]+arr # The some result
print("ASCII codes", arr)
print("middle arithmetic: ", int(sum(arr) / len(arr)))

# arr += [x for x in [ord(x) for x in (input("->")[:3])] if x not in arr]
print(arr)
if arr[-1] in arr[:-1]:
    print(arr.count(arr[-1]) - 1)
arr.sort(reverse=True)
print(arr)

print(chr(97))  # Обернена операція до ord()
"ord()->chr()"
"chr()->ord()"
print(chr(540))

print("++++++++++++++++++++++++++++++++")

a = 22
b = 97
print(chr(a))  # z
print(chr(b))  # a
print([chr(x) for x in list(range(b, a))][1:])
print(print(chr(x)) for x in list(range(b, a))[1:])
if a > b:
    for x in list(range(b, a))[1:]:
        print(chr(x), end=" ")
else:
    for x in list(range(a, b))[1:]:
        print(chr(x), end=" ")

print("+++++++++++++++++++++++++++++")

print("apple" > "Apple")

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126


def random_password():
    random_length = randint(SHORTEST, LONGEST)  # генерація випадкової довжини
    res = ""
    for i in range(random_length):
        random_char = chr(randint(MIN_ASCII, MAX_ASCII))
        res += random_char
    return res


print(random_password())

s = "hello, WORLD! I am learning Python."
print(s)  # hello, WORLD! I am learning Python.
print(s.capitalize())  # Hello, world! i am learning python.
print(s.lower())  # hello, world! i am learning python.
print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
print(s.title())  # Hello, World! I Am Learning Python.

print(s.count("h", 1, -4))  # 0 - з першого символа підрахунок і до -4того
print(s.find("Python"))  # 28 перший індекс входження підстроки

stroc = "one two"
stroc1 = "one"
stroc2 = "two"
print(stroc[stroc.find(stroc2):] + " " + stroc[:stroc.find(stroc2)])
print(stroc[4:] + " " + stroc[:4])

print("++++++++++++++++++++++++++++++")

# s = "ab12c59p7dq"
# resl = [int(e) for e in s if ord(e) < 97]
# print(resl)
# digits = []
# for i in s:
#     if "0123456789".find(i) != -1:
#         digits.append(int(i))
#     else:
#         pass
#
# print(digits)
#
# s = "hello, WORLD! I am learning Python."
# print(s.index("Python"))  # так само як і s.find("Python"), але при не знаходженні
# # поверне помилку, а не =1
#
# stroka = "asfd(jkd;)ngf"
# for s in stroka:
#     ind1 = stroka.index("(")
#     ind2 = stroka.index(")")
#     r = stroka[ind1+1:ind2]
# print(r)

s = "hello, WORLD! I am learning Python."
print(s.rfind("l"))  # 19 індекс останнього входження підстроки в строку
# якщо ітерація ішла вправо(СТАНДАРТНО), ТобтО останній раз підстрока з'явилась на 19 індексі
print(s.rfind("al"))  # -1

print(s.rfind('l', 3, 19))  # 3  - пошук підстроки триває з 3 по 19 індекс і тоді індекс по якому
# останній раз зустрічали 'l' буде 3
print(s.rindex("l"))  # 19

vs = 'Send unlimited free texts and make WiFi calls from a free phone number. Download the free app' \
     'or sign app online to pick your free phone number.'

"""15 125"""
if vs.count('f') == 1:
    print(vs.find('f'))
elif vs.count('f') >= 2:
    print(vs.find('f'), vs.rfind('f')) # print(vs.index('f'), vs.rindex('f'))



