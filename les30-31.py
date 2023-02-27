import numpy

"""
l = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in l:
    if l.count(i) > 1:
        pass
    else:
        print(i, end=" ")
print()
print('*' * 7)

if __name__ == '__main__':
    pass

lis = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# my_array = numpy.asarray(lis)
# print(my_array)
result = []
for i in lis:
    if i in result:
        result.remove(i)
    else:
        result.append(i)

result.reverse()
print(result)
s = []
for j in range(len(l)):
    for i in range(len(l)):
        if l[j] == l[i] and j != i:
            break
    else:
        s.append(lis[j])
# print(s)
# print('*' * 10)
# print(l[1:3])
# l[1:3] = [20, 2]
# print(l)
# l[4] = 30
# print(dir(list))
# l.append(99)
# print(l)
# l.extend([11, 77, 66])
# print(l)
l = [1, 3, 5, 2, 6, 2, 4, 6, 1, 2, 7]
b = []
for i in range(len(l)):
    if l[i] not in b:
        b.append(l[i])
print(b)

print([x ** 2 for x in list(range(1, 11))])
"*****"
spisok = list(range(1, 11))
resl = []
for i in spisok:
    t = i ** 2
    resl.extend([t])  # або resl.append(t) одинаково
print(resl)
"****"
b = list(range(1, 11))  # якщо додати len отак:  list(range(len(spisok))), то потрібно [el] брати в квадрат
c = []
for el in b:
    d = el * el  # b[el] * b[el] отак
    c.extend([d])  # можна видалити рядок з d як непотріб і прописати просто c.extend[el**2].
print(c)
l.insert(2, 100)
print(l)

# lst = []
# n = int(input('Кількість чисел: '))
# for num in range(n):
#     while len(lst) < n:
#         x = int(input('ВВести число яке кратні 3: '))
#         if x % 3 == 0:
#             lst.append(x)
#         else:
#             print("Число", x, 'не ділиться на 3 без остачі')
# print(lst)

a = [5, 9, 2, 1, 4, 3]
b = [4, 2, 1, 3, 7]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)
c = [] # обнулив список, щоб було видно що це одинакові рішення, лише синтаксис інший
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c.append(a[i])
print(c)
"""


# l1 = [1, 2, 3]
# l2 = [11, 22, 33]
#
# l3 = []
# res = []
# for i in l1:
#     for j in l2:
#         l3.append(i)
#         l3.append(j)
# for i in l3:
#     if i in res:
#         res.remove(i)
#     else:
#         res.append(i)
# print(res)
# print(l1.index(1))
#
def func1(l1, l2):
    l3 = []
    for i in l1:
        l3.append(i)
        for j in l2:
            if l1.index(i) == l2.index(j):
                l3.append(j)
    return l3


# print(func([1,2,3],l2))

def func2(l1, l2):
    for i in range(len(l1)):
        l3 = []
        l3.append(l1[i])
        for j in range(len(l2)):
            if i == j:
                l3.append(l2[j])
    return l3


# for i in l1:
#     for j in l2:
#         if i in l3:
#             continue # не дає переходити нижче і повертає на початок ВНУТРІШНЬОГО for якщо умова виконується
#         l3.append(i)
#         l3.append(j)
# print(l3)
#
# for i in l1:
#     for j in l2:
#         if i in l3:
#             break # не дає переходити нижче і повертає на початок ЗОВНІШНЬОГО for якщо умова виконується,
#         l3.append(i)  # тільки один і той самий елемент внітрішного циклу запишеться [1, 11, 2, 11, 3, 11]
#         l3.append(j)
# print(l3)
def func3(l1, l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3


# l = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # l[2:7] = []
# last = l.pop(3)
# print(l, last)
#
# del l[:]
# print(l)
# list1 = []
# n = int(input("ВВести кількість чисел: "))
# for number in range(0,n):
#     x = int(input("ВВести число: "))
#     list1.append(x)
# k = int(input("Ввести індекс"))
# list1.pop(k)
# print(list1)


# a = [int(input("ВВести число: ")) for num in range(int(input("n = ")))]
# k = int(input("k="))
# del a[k] #-(видалив номер елемента) по індексу  # a.pop(k)   a[k:k + 1] = [] # del a[a.index(k)]#- не по індексу!!!
# print(a)
# l.reverse()
# print(l)
# l.sort(reverse=True)
# print(l)
#
# s2 = ["Віталік", "Сергій", "Сашка", "Анна"]
# s2.sort(key=len)
# print(s2)
#
# st = sorted(l, reverse=True)
# print(st)

# numbers = [int(input("Ввести число ")) for n in range(int(input("num: ")))]
# k = int(input("Елемент який буде видалений: "))
# numbers.remove(k)
# numbers.sort(reverse=True)
# print(numbers)

# numbers = [int(input("Ввести число ")) for n in range(int(input("num: ")))]
# k = int(input("Enter del numner "))
# del numbers[numbers.index(k)]
# numbers.sort(reverse=True)
# print(numbers)
import random
from random import randint, randrange

# print(random.random())
# print(randint(0,9)) # 9 включно
# print(randrange(0,9, 2)) # 9 не включно, а двійка буде давати крок і будуть генеруватись тільки парні числa
# city_list = ["Kiiv","Lviv", "Rivne","Dubno", "Lutsk"]
# print(random.choice(city_list))
# print(random.choice([43,23,12,564,6,76,5,3]))
#
# s3= [45,34,2,7,987,76,4,12,13,54,7,9,0,45,32,83,18,90]
# print(random.choices(s3))
# print(random.choices(s3, k=9))
#
# print(random.shuffle(s3))
# random.shuffle(s3)
# print(s3)
#
# print(round(random.uniform(10.4, 25),2))
#
# lrandom =[ randrange(10) for i in range(randrange(10))]
# print(lrandom)
#
# lst = [4,5,6,7,1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# sm = [5,3,2,4,1]
# print(sum(sm))

# spisok = [randrange(100) for i in range(10)]
# print(spisok)
# maxim = max(spisok)
# m = spisok.pop(spisok.index(maxim))
# spisok.insert(0,m)
# print("Spisok: ",spisok, "MAX: ", maxim)


# spisok2 = [randrange(100) for i in range(10)]
# m2 = spisok2.pop(spisok2.index(max(spisok2)))
# spisok2.insert(0,m2)
# print("Spisok: ",spisok2, "MAX: ", m2)


# list1 = [randrange(-10,10) for each in range(10)]
# print(list1)
# minn = min(list1)
# ind = list1.index(minn)
# list1 = list1[ind:] # del list1[0:ind]
# print(list1, minn, ind, sep='\n')

# x = list('1a2b3')
# print(x)
# print("a" in x)
# print("a" not in x)
# print("e" in x)
# print("e" not in x)
#
# lst = []
# if len(lst)== 0:
#     print("empty")
#
# if not lst:
#     print("empty")

# list1 = [randrange(10) for i in range(int(input("Величина першого")))]
# list2 = [randrange(10) for e in range(int(input("Величина другого")))]
# list3 = list1+list2
# list3_unique = []
# list_common = []
# for i in list1:
#     if i in list2 and i not in list_common: # можна також через list.count(значення) - кількість значень у списку, але мій вар із "in" кращий
#         list_common.append(i)
# if list_common == []:
#     list_common.append(0)
#
# for i in list3:
#     if i not in list3_unique:
#         list3_unique.append(i)
# list_minmax = [min(list1),min(list2),min(list3),min(list_common),min(list3_unique),max(list1),max(list2),max(list3),max(list_common),max(list3_unique)]
# print("list1: ",list1,"list2:", list2,"list3: ", list3, "Uniq:", list3_unique,"common_numbers_list: ",
#       list_common, "list_minmax: ", list_minmax,   sep="\n")

# m = [
#     [1,2,3,4,9],
#     [5,6,7,8,2],
#     [9,10,11,12]
# ]
# # print(m[1][2])
# for row in range(len(m)):
#     for collspan in range(len(m[row])):
#         print(m[row][collspan], end="\t\t")
#     print()
# print()
# for row in m:
#     for collspan in row:
#         print(collspan**2, end="\t\t")
#     print()
#
# for x,y  in [[1,2],[3,4],[5,6],[7,8]]:
#     print(x,"+", y, "=", x+y)
#
#
#
# matrix = [[randint(0,10) for i in range(3)] for r in range(5)]  # список списків (матриця)
# print(matrix)
# for r in range(len(matrix)): # для ІНДЕКСА кожного рядка в діапазоні матриці
#     if r % 2 ==0 or r == 0:  #   якщо рядок має парний індекс ЧИ  рядок має нульовий індекс
#         matrix[r].sort(reverse=True) #   значення  у списку списка matrix по індексу r , ми посортуємо в зворотній послідовності
#     else:
#         matrix[r].sort()  #  так само рядок по індексу r ми посортуємо від більшого до меншого
# for n,m,z in matrix:   # для кожного із трьох значень у кожному рядку
#     print(n,m,z, sep="\t\t")   #  зробимо вивід


# l = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# lm = []
# for y in l[0]:  # щоб ітерація пройшла по одному колу і кількість була 4
#     lm.append([])  #  4 пустих списка як результат ітерації
#     for x in l:   #   для кожного списку із l ми витя
#         lm[y-1].append(x[y-1])  # ми ставимо значення по індексу від 0 до того що дає у
#         # ( -1  щоб той "у" був похожий на індекс, бо росте він від 1 а не від 0, а в нас
#         # всюди інше росте від 0)
# print(lm)

"""
for y in range(len(l[0])):       # щоб ітерація пройшла по одному колу і кількість була 4
    lm.append([])                #  4 пустих списка як результат ітерації
    for x in l:                  #   для кожного списку із l ми витя
        lm[y].append(x[y])       # ми ставимо значення по індексу від 0 до того що дає у
print(lm)
"""
# for i in lm:
#     for t in i:
#         print(t, end="\t\t")
#     print()
# print()
# i=0
# z=[1,2,3,4]
# for y in z:
#     for z in l:
#         print(z[i], end="\t\t")
#     i+=1
#     print()

# b= int(input("Ввести розмір списку__:"))
# a=[]
# while len(a) !=b:
#     w = randint(0,b-1)
#     if w not in a:
#         a.append(w)
# print(a)
# height = 3
# width = 4
# amounnt = 20
# lst = [[randrange(amounnt) for x in range(width)] for el in range(height)]
# print(lst)

# w, h = 5, 4
# matrix = list()
# for i in range(h):
#     m = list()
#     for x in range(w):
#         m.append(randint(1, 30))
#     matrix.extend([m])
#
# print(matrix)
#
# programa = [[randint(-20, 11) for itr in range(3)] for itr2 in range(4)]
# cnt = 0
# for x in programa:
#     for l in x:
#         if l < 0:
#             cnt += 1
#         print(l, end="\t\t")
#     print()
# print(cnt)
#
# mat = []
# for x in range(4):
#     li = []
#     for y in range(5):
#         li.append(randrange(30))
#     mat.append(li)
# print(mat)
#
# matag = [[randrange(5) for yix in range(3)] for yx in range(4)]
# print(matag)
# res_sum = 1
# for iter in matag:
#     for reti in iter:
#         if reti != 0:
#             res_sum *= reti
# print(res_sum)

# reslist=[]
# dlist = [[randrange(11) for x in range(6)]for y in range(6)]
# for x in dlist:
#     if dlist.index(x)%2==0 or dlist.index(x)==0:
#         xres=dlist.index(x)+1
#         reslist.append(dlist[xres])
#     else:
#         xres=dlist.index(x)-1
#         reslist.append(dlist[xres])
# print(dlist)
# print(reslist)
#
# dvalist = [[randrange(11) for x in range(6)]for y in range(6)]
# print(dvalist)
# for row in range(len(dvalist)):
#     if row%2 != 0:
#         row=dvalist[row-1]
#     else:
#         row=dvalist[row+1]
#     for col in row:
#         print(col, end="\t\t")
#     print()
#
# print()
#
# for h in range(len(dvalist)): # різниця в відсутності else
#     if h%2==0:
#         for w in range(len(dvalist)):
#             print(dvalist[h+1][w], end="\t\t")
#         print()
#         for w in range(len(dvalist)):
#             print(dvalist[h][w], end="\t\t") # та обовязково без додавання одиниці
#         print()

"""
1  2  3  4  5
8  9  10 11 12
15 16 17 18 19
22 23 24 25 26
29 30 31
"""
# days = [d for d in range(1,32)]
# print(len(days))
# weeks1 = [[d for d in range(0,7)]for x in range((31//7)+1)]
# print(31//7)

# weeks = [days[i:i+7] for i in range(0,len(days),7)]
# for week in weeks:
#     for d in week:
#         if week.index(d) >4:
#             week.remove(d)
#             week.remove(d+1)
#
#
# print(weeks, sep="\n")

# weeks = [days[i:i+5] for i in range(0,len(days),7)] # крок в 7, але берем тільки 5 днів.
# for week in weeks:
#     for d in week:
#         print(d,end="\t\t")
#     print()
#
#
# print(weeks, sep="\n")

# from math import sqrt, floor, ceil, pi, fsum, degrees, radians, cos, sin
#
# print(sqrt(2))
# print(floor(3.8))
# print(ceil(3.2))
# print(pi)

# radius = int(input("Radius_:_"))
# C = 2 * radius * pi
# print(C.__round__(2))
# print(round(C, 2))

# lst = [1, 5, 3, 8.4]
# print(sum(lst))
# print(fsum(lst))
#
# print(degrees(3.14159)) # із радіян в градуси
# print(radians(180)) # із градусів у радіяни
#
# print(cos(radians(60)))
# print(sin(radians(60)))
#
# Katet1 = 8
# katet2 = 6
# print("gipotenuza=",sqrt(8**2+6**2))

import time

# seconds = time.time()
# print(seconds)
# local_time = time.ctime(seconds)
# print(local_time)
# res = time.localtime(32536799999)
# print(res)
# print(res.tm_hour)
#
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))#, time.localtime())) вказую тільки якщо хочу кількість секунд
#
# pause = 5
# print("prjgram started")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Назва нагадування")
# t = float(input("Через скільки хвилин"))
# t*= 60
# time.sleep(t)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)

import locale

locale.setlocale(locale.LC_ALL,"uk_UA")
print(time.strftime("Сьогодні: %B/%d/%Y, %H:%M:%S", time.localtime()))# вказую тільки якщо хочу кількість секунд





















