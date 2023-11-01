def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])


print(palindrom('ШалаШ'))


def count_items(array):
    cnt = 0
    for item in array:
        if isinstance(item, list):
            cnt += count_items(item)
        else:
            cnt += 1
    return cnt


# names = ["Adam", ["Bob", ["Chet", 'Cat'], 'Bart', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
# print(count_items(names))

"""
Isinstance. взяла дані із найглибшого масиву. із середини піднімається назовні перезапускаючи функцію
рекурсивно. При цьому є зміна та АнуЛяцІя CNT показника, але тільки у наступній функції. 
RETURN виділив область памяті,куди складає усі виконання функції, і тому усі 
returns канкатенуються.
"""


def perevirka_na_kankatenacio(array):
    stroka_danuh = ""
    for i in array:
        if isinstance(i, list):
            stroka_danuh += perevirka_na_kankatenacio(i)
        else:
            stroka_danuh += i
    return stroka_danuh  # Канкатенація ретурнс


# print(perevirka_na_kankatenacio(names))  # AdamBobChetCatBartBertAlexBeaBillAnn


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def fibo(length):
    sp = []
    chislo = 1
    for n in range(length):
        if n < 2:
            sp.append(chislo)
        else:
            chislo = (sp[n - 2] + sp[n - 1])
            sp.append(chislo)
    return sp


# print(fibo(8))

def union(s):
    if not s:  # s == []:
        return s  # - результат виконання функції в кінці буде тут
    if isinstance(s[0], list):  # перевірить чи s[0] є списком, так - це список ["First"] і дана строка коду основна у
        # фуункції, а ретурн запустить її ще раз уже до аргументу ["First"][0] ,
        return union(s[0]) + union(s[1:])  # ось тут запускає ще раз, (знову відпрацьовує
        # строка основна if isinstance(s[0], list).
        # тоді чи є "First"[0] списком,  (ні бо це строка 'F') і ми не до того іфа і не заходимо в нього, а одразу в
        # тупіку, тому переходимо до наступної лінійки коду і повертаємо
    peturn = s[:1] + union(s[1:])  # у стеку памяті збережеться s[:1] а це s[0] у першому випадку, це власне наш # аргумент s
    return peturn


# print("Скореговано:", union(names))
test = [["First"], ["Second", ["Third", ["Fourth", ["Fifth"]]]]]


def recur(length, n=1, sp=None, ):
    if not sp:
        sp = []
        n = 1
    if len(sp) < 2:
        sp.append(n)
        return recur(length, n, sp)
    if len(sp) == length:
        return sp
    else:
        n = (sp[sp.index(n)]) + (sp[sp.index(n) - 1])  # n_value_ind = sp[sp.index(n)]
        # n = sp[-1]+sp[-2] - the same
        sp.append(n)
        return recur(length, n, sp)


def fibonacci_list_recursive(index):
    if index <= 0:
        return [0]
    elif index == 1:
        return [0, 1]
    else:
        fib_list = fibonacci_list_recursive(index - 1)
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)
        return fib_list


print(recur(8))
print(fibonacci_list_recursive(8))
"""
Delete пробіл в строці через рекурсо
"""


def remove(text):
    if not text:
        return text  # можна і це ""
    if text[0] == "\t" or text[0] == " ":
        return remove(text[1:])
    else:
        return text[0] + remove(text[1:])


print(remove("1 2 3 Hello\tWorld"))


def sp_fibo_generation(length):
    if length <= 0:
        return [1]
    if length == 1:
        return [1, 1]
    else:
        sp = sp_fibo_generation(length - 1)
        n = (sp[-1] + sp[-2])
        sp.append(n)
        return sp


print(sp_fibo_generation(8))


def fibonacci_list_recursive(index):
    if index <= 0:
        return [0]
    if index == 1:
        return [0, 1]
    fib_list = fibonacci_list_recursive(index - 1)
    next_number = fib_list[-1] + fib_list[-2]
    fib_list.append(next_number)
    return fib_list


print(fibonacci_list_recursive(8))

print(union(test))

"Кількість негативних чисел у списку через рекурсію"

l = [-2, 3, 8, -11, -4, 6]  # 3


def quannegativs_num(n):

    if not n:
        return n
    if n[0] >= 0:
        return  quannegativs_num(n[1:])
    else:

        return quannegativs_num(n[1:])


print(quannegativs_num(l))

def negativs_num(n):
    if not n:
        return 0
    else:
        if n[0] < 0:
            return 1 + negativs_num(n[1:])
        else:
            return negativs_num(n[1:])

l = [-2, 3, 8, -11, -4, 6]
print(negativs_num(l))