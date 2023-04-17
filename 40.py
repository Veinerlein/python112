# p = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda x: p.index(x) ** 3 * x, p)))
#
# p2 = [3, -4, -6, 7, -8, 3, -12, 4, 7]
# res = (list(filter((lambda y: y if y == False else True), list(map(lambda x: x if x < 0 else not x, p2)))))
# print(res)
# print(abs(sum(res)))
#
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(list(map(lambda x:x**2,nums)))
# print((list(x**3 for x in nums )))
#
#
# def func_compute(a):
#     def wrapp(b):
#         return a*b
#
#     return wrapp
# res = func_compute(2)
#
# print(res(15))
# print(res(20))


def args_decorator(arg1, arg2):  # "Mrs", "Smitt" параметри попадуть у вигляді аргументів
    print("Arguments: ", arg1, arg2)  # Arguments:  Mrs Smitt

    def wrapper1(func1):  # func("Jack", "Nicklson") попадає сюди
        print("''''''''''")

        def wrapper2(func_arg1, func_arg2):  # "Jack", "Nicklson" параметри попадуть у вигляді аргументів
            print("Аргументи:_", func_arg1, func_arg2)  # Аргументи:_ Jack Nicklson
            func1(func_arg1, func_arg2)  # my name is: Jack Nicklson
            return func1(arg1, arg2)  # my name is: Mrs Smitt (return не обовязковий)

        return wrapper2

    return wrapper1


@args_decorator("Mrs", "Smitt")
def func(first, last):
    print("my name is:", first, last)


func("Jack", "Nicklson")

print("+++++++++++++++++")


def dec(decorator_text):  # "Hello, "
    def wrapper(func2):  # hello_world("world!")
        def wrap(*args):  # ("world!")
            print(decorator_text, end="")  # "Hello, " + {end=""} + {наступний рядок коду=("world!")}
            func2(*args)  # ("world!")

        return wrap

    return wrapper  # буде  Hello, world!


@dec(decorator_text="Hello, ")
def hello_world(text):
    print(text)


hello_world("world!")

print("+++++++++++++++++")


@dec(decorator_text="Hi, I am ")
def hello(text1, text2):
    print(text1, text2)


hello("Martin", "Scorcese")

if __name__ == "__main__":
    print("THis code will be showed only if this modele is`nt imported")

print("++++++++++++++++++++++")


def chislo(number1):
    def wrapper(funct):
        def wrap(number2):
            return number1 * funct(number2)

        print(funct(number1))
        return wrap

    return wrapper


@chislo(3)
def res(number):
    return number


print(res(5))

print("++++++++++++++++")


def typed(*args, **kwargs):  # 3, 4, 5
    print(args)
    print(kwargs)

    def wrapper(fn):
        def wrap(*f_args, **f_kwargs):
            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    print("incorrect type")
                    raise TypeError("incorrect type")
            for k in kwargs:
                if type(f_kwargs[k]) != kwargs[k]:
                    print("incorrect type")
                    raise TypeError("incorrect type")
            return fn(*f_args, **f_kwargs)

        return wrap

    return wrapper


@typed(int, int, int)
def typed_fn(x, y, z):
    return x * y * z


print(typed_fn(3, 4, 5))


# print(typed_fn(3, 4, "Hello"))

@typed(str, str, str)
def typed_fn2(x, y, z):
    return (x + y) + z


@typed(str, str, z=int)
def typed_fn3(x, y, z="Hello!"):
    return (x + y) * z


print(typed_fn2("Some, ", "man is saying ", "'Hello'"))
print(typed_fn3("Some, ", "man is saying ", z=2))

print("+++++++++++++++++++++++")


def dec(tx=None, dec_text=""):
    def wrapper(func):
        def wrap(*args):
            print(dec_text, end="")
            func(*args)

        return wrap

    if tx is None:
        return wrapper
    else:
        return wrapper(tx)


@dec
def hello_world(text):
    print(text)


@dec(dec_text="Hello, ")
def hello_world2(text):
    print(text)


hello_world("HI!")
hello_world2("world!")
print("+++++++++++++++++++++++++")

"""         STRING       """
# print(int("19"))
# print(int(float("19.5")))

print(int("100", 2))  # 2 У даному випадку вказує,
# що int потрібно перетворити строку 100 як двоїчний код в число і буде 4
# тому що 421

print(int("100", 8))  # 64
print(int("100", 10))  # 100  - - - ПО замоувчуванню
print(int("100", 16))  # 256

# "++++++++++++++++++++++++"

print(bin(18))  # 0b10010 а конкретно  10010
print(oct(18))  # 0o22
print(hex(18))  # 0x12

print(0o22)  # 18
print(0b10010)  # 18
print(0x12)  # 18

print("+++++++++++++++++++++++++++")

q = "Pyt"
w = "hon"
e = q + w
print(e)
print(3 * e)
print(e in "I am learning Python")  # True
print(e in "I am learning Java")  # False

s = "Hello"
# print(s[1])#e
# print(s[-5])#H
#
# print(s[1:4])#ell
# print(s[:4])#Hell
# print(s[2:])#llo
#
# print(s[0:5:2])#Hlo
# print(s[4:0:-2]) #ol
print("++++++++++++++++++++++++")

s1 = "abcdefgh"
print(s1[slice(2, 5)])  # cde
print(s1[slice(2, )])  # ab
print(s1[slice(2, None)])  # cdefgh
print(s1[slice(5, None, -1)])  # fedcba
print(s1[slice(5, None, None)])  # fgh
print(s1[slice(None, None, -1)])  # hgfedcba

s = "python"
# s[3] = "t" # TypeError: 'str' object does not support item assignment
print(s)  # TypeError: 'str' object does not support item assignment
print(id(s))
s = s[:3] + "t" + s[4:]  # - По факту змінна s уже інша
print(s)  # pytton
print(id(s))

str1 = "I am studying Nuthon. I like Nuthon." \
       " Nuthon is very interesting programming lenguage."
str2 = str1[:14] + "P" + str1[15:29] + "P" + str1[30:37] + "P" + str1[38:]
print(str2)  # I am studying Puthon. I like Puthon. Puthon is very interesting programming lenguage.


def string(str1):
    stri = ""
    for x in range(len(str1)):
        if str1[x] == "N":  # old
            # pos = str1.index(x) # position of index
            stri += 'P'  # new
        else:
            stri += str1[x]
    return stri


print(string(str1))


# наступна функція така ж але універсальніша
def change_char_to_str(string, old, new):
    new_string = ""
    for s in string:
        if s == old:
            new_string += new
        else:
            new_string += s
    return new_string


# одинакові 2 варіанти (верхній через for нижній через while)

def ch_ch_to_str(s, old, new):
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == old:
            s2 += new
        else:
            s2 += s[i]
        i += 1
    return s2


str1 = "I am studying Nuthon. I like Nuthon." \
       " Nuthon is very interesting programming lenguage."
str2 = change_char_to_str(str1, "N", "P")
print("str1 = ", str1)
print("str2 = ", str2)

str3 = ch_ch_to_str(str1, "N", "P")
print("str3 = ", str3)


def ser_ariph(fn):
    def wrapper(*args):
        return fn(*args)/len(args)
    return wrapper

@ser_ariph
def function(*args):
    sum = 0
    for a in args:
        sum += a
    return sum


print(function(2, 3, 3, 4))
