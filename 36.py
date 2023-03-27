# FROZENSET

s = frozenset([1, 2, 3, 4, 5])
# print(s)
a = frozenset({"hello", "world"})
# print(a)
b = frozenset({i ** 2 % 4 for i in range(10)})
# print(len(b))
d = list(b)

# DICT Словник

ls = ["ONE", "TWO"]
# print(ls[0])
di = {"one": 1, "two": 2, 1: "one", 2: "two"}
# print(di["one"])
# print(type(di), ls, di)
# print(id(di["one"]))
# print(id(di["two"]))
# print((di[1]))
d2 = dict(one="1", two="2")
# print(d2)

d3 = dict.fromkeys("a", "b")
# print(d3["a"])  # b
d3 = dict.fromkeys(["a", "b"])
# print(d3["a"])  # NONE
# print(d3)  # {'a': None, 'b': None}

d3 = dict.fromkeys(["a", "b"], 100)
# print(d3)

# users = (
# ("igor@gmail.com","igor"),
#  ("ira@gmail.com","ira"),
#   ("anna@gmail.com","anna")
#   )
#
# # print(users)
# d_users = dict(users)
# print(d_users)

d4 = {i: i + 1 ** 2 for i in range(7)}
# print(d4)

# print(d4[5])  # По ключу не індексу.
# хоча з індексами так само якщо ключі від 0 до якогось числа
d4[5] = "x500"
# print(d4)
d5 = {0: "text1", "one": 45, (1, 2, 3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# Ключами можуть бути любі незмінні типи данних
# print(d5[42][1])  # 3
# print(d5[1, 2, 3])  # кортеж
# del d5[1, 2, 3]
# print("one" in d5)  # True

# if "one" in d5:
#     print(True)
key = "four"
if key in d5:
    del d5[key]
# print(d5)

# try:
#     del d5[key]
# except KeyError:
# print("ПОмилка виключись, повідомлення запишись: Елемента із таким"
#       " ключем просто немає", key)

d6 = {"one": 1, "two": 2, "three": 3}
# for key in d6:
# print(key, d6[key])  # НА ВІДМІНУ ВІД СПИСКУ ІТЕРАЦІЯ В СЛОВНИКУ ІТИМЕ ТАК,
# НІБИ МИ РПОХОДИМОСЬ ПО ІНДЕКСАМ (ЯК У ВИПАДКУ ІЗ range() у списках),
# і тільки коди ми звертатимемось поключу буде виводитись значення d6[key]

dictionary = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(dictionary)
dictionary_multy = [dictionary[i] for i in dictionary]
dictionary_mult = 1
dictionary_mult = [dictionary_mult * i for i in dictionary_multy]
res = 1
for i in dictionary_multy:
    res *= i
# print(res)
# print(dictionary_mult)

# from functools import reduce
# dictionary_multy = [val for key, val in dictionary.items()]
# res = reduce(lambda x, y: x*y, dictionary_multy)
# print(res)

multy = 1
for i in dictionary:
    multy *= dictionary[i]
# print("HERE",multy)

# vved = dict.fromkeys([1,2,3,4], "ovoc")
# for i in vved:
#     vved[i] = input("Ввести назву овоча")
# del_element = int(input("Який елемент видалити"))
# del vved[del_element]
# print(vved)

# d = dict()
# d1 = {i: input("->") for i in range(1,5)}
# print(d1)
# dislike = int(input("What to delete"))
# del d1[dislike]
# print(d1)

# capitals = dict()
# capitals["Ukraine"] = "Kiiv"
# capitals["USA"] = "Vashington"
# capitals["ENGland"] = "London"
#
# countries = ["Ukraine", "USA", "France", "ENGland"]
# for country in countries:
#     if country in capitals:
#         print("The capital of country " + country + ": " + capitals[country])
#     else:
#         print("there is no in database " + country)


dict8 = [
    {1: 'Core-i3-4330', "9": " по 450"},
    {2: 'Core i5 - 4670k', "3": "по 850"},
    {3: 'AMD fx-6300', "6": "по 370"},
    {4: 'Pentium G3220', "8": "по 210"},
    {5: 'Core i5-3450', "5": "по 640"}
]
# print(dict8)

# d8 = {
#     {1: 'Core-i3-4330'}: {"9": 450},
#     {2: 'Core i5 - 4670k'}: {"3": 850},
#     {3: 'AMD fx-6300'}: {"6": 370},
#     {4: 'Pentium G3220'}: {"8": 210},
#     {5: 'Core i5-3450'}: {"5": 640}
# }


# goods = {
#     1: ['Core-i3-4330', 9, 450],
#     2: ['Core i5 -4670k', 3, 850],
#     3: ['AMD fx-6300', 6, 370],
#     4: ['Pentium G3220', 8, 210],
#     5: ['Core i5-3450', 5, 640]
# }
# while True:
#     try:
#         vvid = int(input("Ввести номер товару: "))
#         if vvid != 0:
#             new_quantity = int(input("Ввести кількість: "))
#             goods[vvid][1] = new_quantity
#         else:
#             break
#     except:
#         print("Товару з таким номером не існує")
#         # print(goods)
# for element in goods:
#     print(element, ")", goods[element][0]," - ",
#           goods[element][1], "шт по ціні в долларах " ,goods[element][2], sep="")
#

d9 = {"A": 1, "B": 2, "C": 3}

x = iter(d9)  # Виражає ітерацію
# print(x)  # <dict_keyiterator object at 0x00000292A85D1710>
# print(list(x))  # ['A', 'B', 'C']
# print(list(iter(d9)))  # ['A', 'B', 'C']
it = list(iter(dict8))
# print(it)

value = d9.get("B", "FF")
# print(value)  # d9["B"]

d_copy = d9.copy()  # створить новий обєкт на відміну від оператора присвоїти
d_copy["B"] = 5
d9["E"] = 7
# print("D9 = ", d9)  # {'A': 1, 'B': 2, 'C': 3, 'E': 7}
# print("D_copy = ", d_copy)  # {'A': 1, 'B': 5, 'C': 3}

new = d9.items()
# print(new)  # dict_items          ([('A', 1), ('B', 2), ('C', 3), ('E', 7)])
new1 = dict.items(d9)  # dict_items ([('A', 1), ('B', 2), ('C', 3), ('E', 7)])
# print(new1)

a = d9.keys()  # ('E', 7)
# print(a)

item = d9.popitem()  # те саме що pop() у списків видалить і збереже в собі пару
# в даному випадку останню. видаляє та повертає.
# print(item)

defoult = d9.setdefault("К", 5)  # додаються тількти нові ключі якщо подібних не було
# print(defoult)

pop = d9.pop("e", 10)  # видаляє та повертає лише ключ. 10 прописано щоб не було
# помилки коли такого ключа не буде
# print(pop)

# d9.clear() # зачистка
# print(d9)

d9.update([("R", 7), ("Q", 9)])  # додав нові унікальні ключі-значення або перезапише існуючі
# print(d9)

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = x.copy()
z.update(y)
# print(z)
# x.update([("b", 3),("c",4)])

zy = x | y  # обєднання двух словників в третій

# print(zy)
# print(x)

v = d9.values()  # повертає список значень
# print(list(v))  # [1, 2, 3, 5, 7, 9]
# print(v)  # dict_values([1, 2, 3, 5, 7, 9])

slovnyk = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New-York"}

a = {"name": slovnyk.pop("name"), "salary": slovnyk.pop("salary")}
d = dict()
d["name"] = a.pop("name")
d["salary"] = a.pop("salary")
# print(a)
# print(slovnyk)

# slovnyk_new = list(slovnyk.items())
# for i in slovnyk_new:
#     x = slovnyk_new[0],slovnyk_new[2]
#     x = list(x)
#     x = dict(x)
#
# print(x)
# slovnyk_new = list(slovnyk.items())
# for i in slovnyk_new:
#     x = slovnyk_new[0],slovnyk_new[2]
#     x = list(x)
#     x = dict(x)
# del slovnyk_new[0],slovnyk_new[1]
#
#     # del slovnyk_new[0],slovnyk_new[2]
# print(x)
#
# print(slovnyk_new)
slovnyk = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New-York"}
a = dict()
a["name"]=slovnyk.pop("name")
a["salary"]=slovnyk.pop("salary")
# er = slovnyk.pop("city")
# slovnyk.update([("Location", er)])
# print(slovnyk)

# slovnyk["location"] = slovnyk.pop("city")


slovnykys = [("name", "Kelly"), ("age", 25), ("salary", 8000), ("city", "New-York")]
new_slovnik = {}
for i in slovnykys:
    new_slovnik.update([i])
# print(new_slovnik)

a = {
    "first": {1: "one", 2: "two", 3: "three"},

    "second": {4: "four", 5: "five"}
}
# print(a)
# for x in a:
#     print(x, [i for i in a[x]], [a[x][i] for i in a[x]])
"""
for x in a:
    print(x)
    for y in a[x]:
        print("\t",y,": ",a[x][y], sep="")
"""

sps = {
    "john": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}

# name = input("Name: ")
# region = input("Region: ")
#
# for x in sps:
#     print(x)
#     for y in sps[x]:
#         if name == x and region == y:
#             print(sps[x][y])
#             sps[x][y] = int(input("New value: "))
#
#         print(y, ":", sps[x][y])

# ass = {"one": 1,"two": 2,"three": 3,"four": 4,}
# bass = {val:key for key,val in ass.items()} # items() приймає ключ і значення!!!
# print(bass) #{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#
# for i in ass.values():
#     print(i, end=" ") #1 2 3 4

example1 = {"one": 1, "two": 2, "three": 3, "four": 4}
cnt = 0
res = {}
for key, val in example1.items():
    if cnt == 2:
        break
    else:
        res.update({key: val})
        cnt += 1
# print(res)
"*****"
example2 = {"one": 1, "two": 2, "three": 3, "four": 4}
res2 = {key: val for key, val in example2.items() if val <= 2}
# print(res2)

# s = [10, 20, 30, 40]
# a = {
#     i: int(input("->")) for i in s
# }
# print(a)
"""TRANFORM INTO LIST/DIct"""

slovnykys = [("name", "Kelly"), ("age", 25), ("salary", 8000), ("city", "New-York")]
new_slovnik = {}
for i in slovnykys:
    new_slovnik.update([i])
# print(new_slovnik)
# figure = {i:input() for i in range(1,4)}

figure = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# print(list(figure.values()))
# print(list(figure.items()))

example3 = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
d = {}
for e in example3:
    # values = []
    if type(e) == str:
        d[e] = []
        s = d[e]
        # ind = example3.index(e)
        # key = example3[ind] = [e]
        # second = key.append([])

    else:
        s.append(e)
    #     ind_int = example3.index(e)
    #     example3[ind]=
    #     example3[ind][1] = e
    #     print(example3)
    #     print(d)
print(d)

dic = zip([1, 2, 3], ["one", "two", "three"])  # формує конкретний тип даних з двох послідовностей однієї довжини
print(dic)  # <zip object at 0x000002360D790D40>
"""
ОБВЕСТИ ДУЖКАМИ СФОРМОВАНУ КОМБІНАЦІЮ "ZIP" ТА ВКАЗАТИ ПЕРЕД НЕЮ ТИП ДАНИХ
"""
# print(dict(dic))  # {1: 'one', 2: 'two', 3: 'three'}
# a = {"Dec", "Jan", "Feb"}
# b = [12, 1, 2, 3]  # якщо множина (set()) то буде постійно змінюватись значення
# c = [4.0, 5.0, 6.0]
# f = {k: v for k, v in zip(b, a)}
# z = zip(a, b, c)
# print(f)
# print(z)
# print(type(z))
# print(list(z))

print(list(zip(range(2, 15), range(5, 100))))
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

b = {"a": 11, "b": 22, "c": 33, "d": 44, "e": 55}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
# print(k1, "->", v1)  # a -> 1
# print(k2, "->", v2)  # a -> 11

pairs = [(1, 'a'), (2, "b"), (3, "c"), (4, "d")]
a, b = zip(*pairs)  # ЗІРОЧКА ОЗНАЧАТИМЕ РОЗПАКУВАННЯ ПОСЛІДОВНОСТІ
# print(a)  # (1, 2, 3, 4)
# print(b)  # ('a', 'b', 'c', 'd')

a = [3, 1, 4, 2]
b = ['d', 'b', 'a', 'c']
data = list(zip(a, b))
# print(data)  # [(3, 'd'), (1, 'b'), (4, 'a'), (2, 'c')]
data.sort()
# print(data)  # [(1, 'b'), (2, 'c'), (3, 'd'), (4, 'a')]

data1 = list(zip(b, a))
# print(data1)  # [('d', 3), ('b', 1), ('a', 4), ('c', 2)]
data1.sort()
# print(data1)  # [('a', 4), ('b', 1), ('c', 2), ('d', 3)]

data2 = sorted(zip(b, a))  # Сортед сам переобразує у список по замовчуванню, хоча ми і не вказували це
# print(data2)

ts = {'January': 52000, 'Fabruary': 51000, 'March': 48000}
pc = {'January': 46800, 'Fabruary': 45900, 'March': 43200}
true_profit = None
for (k1, v1), (k2, v2) in zip(ts.items(), pc.items()):
    true_profit = v1 - v2
    print(true_profit)

month = ["January", 'February', "March"]
total_sales = [52000.00, 51000.00, 48000.00]
production_cost = [46800.00, 45900.00, 43200.00]
for sales, cost, mon in zip(total_sales, production_cost, month):
    res = sales - cost
    print("Загальний прибуток в ", mon, "=", res)

one = {"apple": 0.04, "orange": 0.35, "pepper": 0.53}
two = {"pepper": 0.20, "onion": 0.55}
print({**two, **one})  # {'pepper': 0.2, 'onion': 0.55, 'apple': 0.04, 'orange': 0.35}
for k, v in {**two, **one}.items():
    print(k, "->", v)
    # pepper -> 0.2
    # onion -> 0.55
    # apple -> 0.04
    # orange -> 0.35

colors = ["red", "green", "blue"]

ind = 1
for color in colors:
    print(str(ind) + ")" + color)  # 1)red
    ind += 1  # 2)green
    # 3)blue

print()
for i, color in enumerate(colors, 100):  # 100)red
    print(str(i) + ")" + color)  # 101)green
    # 102)blue

d = {"a": 1, "b": 2, "c": 3, "d": 4}
for i, (j, q) in enumerate(d.items(), 1):  # 1:a1
    print(i, ":", j, q, sep="")  # 2:b2
    # 3:c3
    # 4:d4
d = {
    1: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
    2: {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
}

for i, k in enumerate(d, 1):
    print(i, ") key=", k, ", value=", d[k], sep="")

num = [1, 2, 3, 4, 5]
itr = iter(num)
print(itr)
print(next(itr, "STOP"))
print(next(itr, "STOP"))
print(next(itr, "STOP"))
print(next(itr, "STOP"))
print(next(itr, "STOP"))
print(next(itr, "STOP"))
print(next(itr, "STOP"))

a = [6, 7, 3, 4, 1, 5]
b = enumerate(a)
print(b)  # <enumerate object at 0x000001B4FED71EC0>

c = next(b)
c1= next(b)
print(c)  #  (0, 6)
print(c1)  # (1, 7)
print(type(c))
