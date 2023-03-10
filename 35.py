# numbers = []
# while True:
#     try:
#         num = input("Enter a number (or press Enter to exit): ")
#         if num == '':
#             break
#         num = int(num)
#         numbers.append(num)
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#
# total = sum(numbers)
# print("The sum of the numbers entered is:", total)

def inputs():
    numbers = []
    n = input(":")
    if "0" <= n <= "9":
        numbers.append(n)
        print(numbers)
        return inputs()
    else:
        return numbers


def realization():
    numbers = []
    numbers.append(inputs())
    return numbers


# print(inputs())

# print(realization())

def summy_and_average():
    # enter = False
    # numbers = []
    # n = input("input: ")
    # if n == "":
    #     enter = True
    # numbers.append(n)
    pass


# print(summy_and_average())

# while True:
#     user_input = input("Enter a number (or press Enter to exit): ")
#     if user_input == "":
#         break
#     else:
#         # do something with the user_input
#         print("You entered:", user_input)


# summy_and_average()

def is_greater(x, y):
    if x > y:
        return True
    else:
        return False


# print(is_greater(10, 5))
# print(is_greater(5, 10))


def check_password(password):  # Декілька ретьорнів
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) >= 8 and has_upper and has_num and has_lower:
        return True
    return False


# p = input("Password: ")  # 125An456
# if check_password(p):
#     print("The password is good")
# else:
#     print("The password isn't good")

def get_sum(a=5, b=3, c=0, d=1):
    return a + b + c + d


# print(get_sum(1, 5, d=2))


def set_param(n=20, s="-"):
    print(n * s)


# set_param(10,"+")
#
# set_param(5,"*")
#
# set_param(15,"#")
#
# set_param(7)
#
# set_param()

def check_password2(username, password, min_length=8, check_user=True):
    if len(password) < min_length:
        print("Password is too short")
        return False
    elif check_user and username in password:
        print("Password had the username inside")
        return False
    else:
        print("The password passed all tests")
        return True


# check_password2("John", "12345")
# check_password2("John", "12345John", )
# check_password2("John", "12345name",10)


def sum_numbers(number, odd_numbers=False):
    numbers = [int(n) for n in str(number)]  # список із чисел
    even_sum = 0
    odd_sum = 0
    if odd_numbers == True:
        for n in numbers:
            if n % 2 != 0:
                odd_sum += n
        print("The summ of odd numbers is: ")
        return odd_sum
    else:
        for n in numbers:
            if n % 2 == 0:
                even_sum += n
        return even_sum


def sumNumber(number, even=True):
    s = 0
    while number > 0:
        cur_digit = number % 10
        if even and cur_digit % 2 == 0:
            s += cur_digit
        elif cur_digit % 2 != 0:
            s += cur_digit
        number = number // 10
    return s


# print(sumNumber(9874023, even=False))
# print(sum_numbers(38271))
# print(sum_numbers(123456789))

def display_info(name, age):
    print("Name: ", name, "\nAge: ", age)


# display_info("Anna", 23)
# display_info(age=23,name= "Anna")

def func(a, ln=[]):
    if ln is None:
        ln = []
    ln.append(a)
    return ln

#
# print(func(1, ln=[2, 3]))
# print(func(2))
# print(func(3))
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # порівнює значення
# print(lt1 is lt2)  # порівнює адреси в памяті
# lt1.append(4)
# print(id(lt1))  # айді такий же як і був, хоча додали ще один елемент у список,
# Так працює видозміняємий тип данних .

"**********"

# lt1[1] = "Hello"
# print(id(lt1))
#
# s = "Hello"
# print(id(s))
# s += "word"
# print(s)
# print(id(s))  # Незмінний тип данних
#
# s = "Hello"
# s1 = "Hello"
# # print(id(s))
# # s=s[1:-1] # - новий адрес ячейки памяті.
# print(id(s))
# print(id(s1))
# print(s == s1)
# print(s is s1)


def add_number(n):
    print("Inside the function", n, "=", id(n))
    n += [1]
    print("After appropriation", n, "=", id(n))
    n = n + [4]  # змінить айді так як переприсвоїмо у нову перемінну по новій адресі
    print("After second appropriation", n, "=", id(n))


# x = [1, 2, 3]
# print(x, "=", id(x))
# # add_number(x)
# print(x, "=", id(x))

"""
для незмінних типів даних таких, як строка або число,
 люба зміна буде прописуватись у новій адресі айді
"""

# lst = [10, 20, 30]#  ----  зміннтй тип даних
# tp = (10, 20, 30)# -----  незмінний тип даних (кортеж)
#
#
# a=(1,2,3,4,5,6,7,8)
# print(a)
# print(type(a))
# b= 1,2,3
# print(tuple((1,2,3)))
# print(type(b))
# a = tuple(a)
# t = tuple("hello") # Якщо одне значення, то повинна бути кома
# print(type(t))
# print(t,a)
# a=tuple((1,2,3,4,5))
# print(a)
# s1=tuple(int(input("=> ")) for i in range(1,3))
# print(s1)

import random
s1=tuple(random.randint(0,100) for i in range(10))

print(s1)

k = tuple(2**i for i in range(1,13))
print(k)
t1=tuple("hello")
t2=tuple(" World")
t3 = t1 + t2
print(t3)
print(t3.count("l"))
print(t3.index("l"))






