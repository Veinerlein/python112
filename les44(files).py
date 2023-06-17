"""
FILES
"""
import os

# txt and bin files
f = open(r"E:\pythonProject1\les\text.txt", "r")
# print(*f)  -  забере акцент на себе якщо є метод read()
print(f.closed)
print(f.mode)  # показує даний мод, який зазвичай заданий у функції open
print(f.name)  # показує ім'я файлу
print(f.encoding)  # демонструє кодування тексту файлу

print(f.read(3))  # - працює якщо немає команди print(*f)   -   Sla
print(f.read())  # - при повторному виклику продовжить зчитувати   -   va Ukraini

f.close()  # закриття поточного файлу

# try:
#     print((f.read()))
# finally:
#     f.close()

f2 = open("test.txt", "r")
print(f2.readline())  # this is line1
print(f2.readline(8))  # this is
print(f2.readline())  # читає лінію або дочитує її, відносно заданого курсору
print(f2.readline())

f.close()

f = open("test.txt", "r")
# print(f.readlines(13))  #  захоплення символів у строці, і навіть якщо у лінії захопиться тільки 1 символ,
# строка виведеться

cnt = 0
for line in f:
    print(line)
    cnt += 1

print(cnt)

f.close()

file = open("test.txt", "r")
print(len(file.readlines()))  # прочитує увесь текст, але відносно заданого курсору як початок відчитування
file.close()


# FILE = open("XYZ.txt","w") # перепише файл якщо такий існує, або створить, якщо такого не існує
# FILE = open("XYZ.txt", "a")  # - режим а, якщо дані існують то файл дозапишеться в кінець.
# FILE.write("It was written by Python!!!")  # Запише у файл, який створиться

# print(FILE.write("New text.")) # print покаже скільки символів додасться до файлу в даній команді
# lines = ["This is line 1", "This is line 2"]
# FILE.writelines(lines)  # усі елементи пропишуться в стр
#
# FILE.close()  # закриття файлу

# fil = open("XYZ.txt", "w")
# lst = [i for i in range(1, 20)]
# print(lst)
# for i in lst:
#     fil.write(str(i)+"\t\t")
# fil.close()
def chenger(str_text, way_tofile, line_number):
    f = open(way_tofile, "r")
    lines = f.readlines()
    print(lines)
    f.close()
    f2 = open(way_tofile, "w")
    lines[line_number] = str_text
    print(lines)
    f2.writelines(lines)
    f2.close()
    return lines


print(chenger("Змінена строка ось так\n", "XYZ.txt", 0))
# "Змінена строка\n"


"""
# f = open("text2.txt","w")
# f.write("заміна строки в текстовому форматі\n")
# f.close()
f = open("text2.txt","r")
r = f.readlines()
# print(r)
for i in range(len(r)):
    if r[i] == "Змінена строка 2,\n":
        r[i] = "Hello world\n"
# print(r)
f.close()
f = open("text2.txt","w")
for i in range(len(r)):
    if r[i] == "Змінена строка 2,\n":
        r[i] = "Hello world\n"
f.writelines(r)
print(r)
f.close()
"""

# f = open("text.txt", "r")
# l = f.readlines()
# ind = int(input("Enter index"))
# if 0 <= ind < len(l):
#     l.remove(l[ind])
# else:
#     print("Index was wrong")
#
# print(l)
# f.close()
# f = open("text.txt", "w")
# f.writelines(l)
# f.close()

"""
f = open("text.txt", "r")
print(f.read(3))
print(f.tell()) # вказує у якій позиції знаходиться курсор
print(f.seek(1)) # Переведе курсор у іншу позицію
print(f.read()) # дочитає з індекса, який вказаний у методі seek
"""

# f = open("text.txt", "r+")
# print(f.write("I am Python developer"))
# # print(f.seek(3))
# print(f.write("-new string_"))
# print(f.tell())
# f.close()


# with open("text.txt", "w+") as f:
#     print(f.write("0123456789"))

# with open("text.txt", "r") as f:
#     for line in f:
#         print(line[:6])
#
file_name = "res_1.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.77]


# def get_line(elt):
#     elt = list(map(str, elt))
#     return " ".join(elt)
#
#
#
#
# with open(file_name,"w") as f:
#     f.write(get_line(lst))
# print("Done")


with open(file_name, "r") as f:
    s = f.read()


def Get_list_from_line(s):
    ls = s.split(" ")
    ls = list(map(float, ls))
    return ls


# print(len(Get_list_from_line(s)))

# with open(file_name, "r") as f:
#     for i in f:
#         print(i)

with open(file_name, 'r') as f:
    # f.write("Food in Divinity: \n"
    #         "Original Sin 2 can be crafted or found\n"
    #         "by the player and consumed for immediate benefits.\n"
    #         "Below is a list of Recipes for Food and what Materials\n"
    #         "are required in order to craft them.\n")
    print(f.read())


def slovo(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        l = text.split()
        res = max(map(len, l))
        result = []
        for e in l:
            if len(e) == res:
                result.append(e)
        if len(result) == 1:
            return result[0]
    return result


# print(slovo(file_name))


def longest_word(file_name):
    with open(file_name, "r") as text:
        w = text.read().split()
        print(w)
        max_length = len(max(w, key=len))
        print(max_length)
        res = [word for word in w if len(word) == max_length]
        # print(res)
        if len(res) == 1:
            return res[0]
        else:
            return res


# print(longest_word(file_name))
"""
with open(file_name, "r") as text:
    lst = text.read().split()
    m = max(len(word) for word in lst)
    print([i for i in lst if len(i) == m])
"""

"""Реверс строк файлу"""


def revers_text(file_name):
    with open(file_name, "r+") as f:
        rev_text = "".join(f.readlines())[::-1]
        f.seek(0)
        res = f.write(rev_text)
        f.truncate()
        return res


# print(revers_text(file_name))

def chance_lines(file_name):
    line1 = int(input("Enter line 1 number that should be changed"))
    line2 = int(input("Enter line 2 number that should be changed"))
    with open(file_name, "r+") as f:
        list_text = f.readlines()
        list_text[line1], list_text[line2] = list_text[line2], list_text[line1]
        f.seek(0)
        f.writelines(list_text)
        return list_text


# print(chance_lines(file_name))

# f = open("text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# f.write("-new string-")
# print(f.tell())
# # print(f.read(3))
# # print(f.tell()) # скаже де є курсор
# # print(f.seek(1)) # задає позицію курсору
# # print(f.read())
#
# f.close()

# with open("text.txt","w+") as f:
#     print(f.seek(2))
#     print(f.write("Hello Arsenal!\nfddflaghfad"))
#     print(f.tell())

"""
r+ - не витирає вміст файлу, який існує,
w+ - повністю витирає попередній вміст файлу який існує
(w+ додатково робить truncate() )
"""

# with open("text.txt","r+") as f:
#     for line in f:
#         print(line[:6])

file_numbers = "res_2.txt"

lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]

# def getline(lt):
#     lt = list(map(str, lt))
#     return "-".join(lt)
#
# with open(file_numbers,'w+') as f:
#     f.write(getline(lst))
# print("!")

with open(file_numbers, "r+") as f:
    res = (f.read().split("-"))
res = list(map(float, res))
print(len(res))
""" ''.join() взаємо оберненні .split() """


def sl(file):
    with open(file, "r") as f:
        r = f.read()
        rlist = r.split()
        # res = max(map(len, rlist)) - Любий варіант підійде
        res = len(max(rlist, key=len))
        res = [i for i in rlist if len(i) == res]
    if len(res) > 1:
        return res
    else:
        return res[0]


# print(sl(file_name))
def func(file_name):
    with open(file_name, "r") as f:
        lstk = f.read().split(" ")
        m = max(len(i) for i in lstk)
        print([i for i in lstk if len(i) == m])

# func(file_name)


text = "String 1\n String 2\n String 3\n String 4\n String 5\n String 6\n " \
       "String 7\n String 8\n String 9\n "

# with open("one.txt","w") as f:
#     f.write(text)

fil =  "one.txt"
write_fil = "two.txt"
with open(fil,"r") as fr, open(write_fil, "w") as fw:
    for line in fr:
        line = line.replace("String", "Line->")
        fw.write(line)

with open(write_fil,"r") as f:
    for line in f:
        print(line, end="")


