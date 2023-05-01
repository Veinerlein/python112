s = 'I am learning Python. hello, World!'
sdel1 = s.find('h')  # 17
sdel2 = s.rfind("h")  # 22
print(sdel1, sdel2)

res = s[:sdel1] + s[sdel1 + 1:sdel2] + s[sdel2 + 1:]
print(res)
res2 = s[:sdel1] + s[sdel2 + 1:]
print(res2)

print(s.endswith("ld!"))  # True
print(s.endswith("ld!", 0, 5))  # False
print(s.endswith("m ", 0, 5))  # True
#      Можна шукати кінець строки в заданому діапазоні

print(s.startswith("I am"))  # True
#     .startswith() - те саме що і .endswith() але наваки

print('abc123'.isalnum())  # True якщо строка не пуста і має букви або цифри.
print('abc№123'.isalnum())  # False
print('abc'.isalnum())  # True
print('123'.isalnum())  # True

print("ABCabc".isalpha())  # True  тому що строка складається із букв тільки.
print("ABCabc11111".isalpha())  # False

print("123".isdigit())  # True  тільки із цифр
print("abc".isidentifier())  # валідний ідентифікатор (чи можна назвати таким іменем як строка змінну в пайтон)
print("123abc".isidentifier())  # False

print("abc".islower())  # True (нижній регістр)

print(' \t \n'.isspace())  # True бо символів немає
print(' a '.isspace())  # False бо символи окрім пробілу теж присутні

print('The Apple'.istitle())  # True якщо кожне слово після спейс у верхньому регістрі

print("ABC".isupper())  # False

print('py'.center(10))  # в діапазоні 10 поставить "py" в середину
print('py'.center(10, '!'))  # '!!!!py!!!!'

print('    py'.lstrip())  # py   видалить пробіли зліва
print('py     '.rstrip())  # py                   зправа

print("https://www.python.org".lstrip("/:pths"))  # видалятиме дані символи
# доти, доки не зустріне симол якого немає у переліку в дужеках методу
# і починає це робити з ліва на право.

print('py.$$$;'.rstrip(";$."))  # py    таке саме видалення але із правої сторони

print("https://www.python.org".lstrip("/:pths").rstrip("org"))  # www.python.

print('     py     '.strip())  # py    видалення пробілів зліва та права

print("https://www.python.org".strip('/org.w:pths'))  # ython залишиться після
# видалення з правої та лівої частини

s = "I am learning Nuthon. I like Nuthon." \
    " Nuthon is very interesting programming lenguage."
print(s.replace("Nuthon", 'Python'))  # заміна підстрок у строці

print(s.replace("Nuthon", 'Python', 2))  # 2 це каунт (МЕТОД ЧАСТИЙ)

"""
              ПЕРЕТВОРЕННЯ СТРОКИ В СПИСОК       """

s = "-"
seq = ("a", "b", "c")
print(s.join(seq))  # a-b-c

print("..".join(["1", "2"]))  # 1..2   розділили список приєднавши елемент до списку,
# помістили елемент між елементами списку, вивели строку.
# працює тільки із строковими елементами списку

print(":".join("Hello"))  # H:e:l:l:o  помістили у строку і вивели строку

print("Строка розділена пробілами".split())  # поверне список
# ['Строка', 'розділена', 'пробілами']


print('www.python.org'.split('.'))  # ['www', 'python', 'org']
# розділили по крапці '.'

print('www.python.org'.split('.', 1))  # задав кількість розділень по крапці
# ['www', 'python.org']

# a = input("=> ").split()
# print(a)  # => Hello world
# ['Hello', 'world']


'''Користувач вводить прізвище, імя та по-батькові. Прогама виводить прізвище
та ініціали.'''

# vvid = input("прізвище, імя та по-батькові=>")
vvid = "Modern Teirry Henry"
r = ""
for i in vvid:
    if i.istitle():  # в придуману змінну ввів усі великі букви
        r += i
print(vvid[:vvid.index(" ")], r[1] + '.', r[2] + '.')  # сформував зріз таким чином,
# щоб перше слово виводилось від початку до кінця, де кінець це символ " " з індексом.
# А далі зріз змінної r для першої літери імені та для першої літери по-батькові

rezult = ""  # створив змінну для другої частини
res3 = vvid.split(" ", 1)  # розділив на список
for r in res3:  # пройшовся по циклу
    if r.find(" ") != -1:  # відкинув Прізвище
        rezult = r[0] + '.' + r[r.index(" ") + 1] + '.'  # зробив зріз
    else:
        F = r  # тут у мене прізвище
print(F, rezult)  # прізвище + зріз

a = vvid.split()  # роблю список елементів не придумуючи багато чого
print(a[0], a[1][0] + '.', a[2][0] + '.')  # відразу зрізаю елементи

print('www.python.org'.rsplit('.', 1))  # ['www.python', 'org'] те саме що і split але із правої сторони

stroka = 'Замінити пробіли в строці на символ'

print(stroka.replace(" ", '*'))  # Замінити*пробіли*в*строці*на*символ

print("*".join(stroka.split(" ")))  # Замінити*пробіли*в*строці*на*символ

"""               Регулярні вирази                   
                                            """
import re

# regular express
res = "Я шукаю співпадіння в 2020 році. І я їх обов'язково знайду."
reg = 'я'
print(res.find(reg))  # 18 Індекс
print(reg in res)  # True

print(re.findall(reg, res))  # ['я', 'я', 'я'] список усіх знайдених

print(re.search(reg, res))  # <re.Match object; span=(18, 19), match='я'>  обєкт знайдених співпадінь
# Метод .search() знайде перші попавші елементи
print(re.search(reg, res).span())  # індекс зрізу  span=(18, 19)
print(re.search(reg, res).start())  # 18
print(re.search(reg, res).end())  # 19
print(re.search(reg, res).group())  # я

print(re.match('Я шукаю', res))  # <re.Match object; span=(0, 7), match='Я шукаю'>

print(re.split("я", res))  # ['Я шукаю співпадінн', ' в 2020 році. І ', " їх обов'", 'зково знайду.']
# розбиває строку по шаблону, на виході список.
print(res.split(reg))  # ['Я шукаю співпадінн', ' в 2020 році. І ', " їх обов'", 'зково знайду.']
# те саме але буде розбивати по крапці нормально

# І МЕТОД re.split() ІЗ РЕГУЛЯРНИХ ВИРАЗІВ ДАЄ МОЖЛИВВІСТЬ ДОДАВАТИ КІЛЬКІСТЬ ІТЕРАЦІЇ

print(re.sub(reg, "!", res))  # Я шукаю співпадінн! в 2020 році. І ! їх обов'!зково знайду.
# Типовий реплейс метод

print(re.sub(reg, "!", res, 1))  # Я шукаю співпадінн! в 2020 році. І я їх обов'язково знайду.
# лишень 1 раз заміна

print(re.findall(r'[2020]', res))  # ['2', '0', '2', '0']

# ЧОМУ ІСНУЄ АНАЛОГ МЕТОДІВ ІЗ ЗВИЧАЙНИМ ПАЙТОНОМ.
# СПРАВА У ТОМУ, ЩО В ПАРАМЕТРАХ МЕТОДІВ МОДУЛЯ RE МОЖЕ БУТИ РЕГУЛЯРНИЙ ВИРАЗ АБО ШАБЛОН ІЗ
# ПРАПОРЦЯМИ, ЯКИХ НЕ ЗРОЗУМІЮТЬ ЗВИЧАЙНІ МЕТОДИ СТРОК У ПАЙТОН,
#  АЛЕ І ВАЖИТИ ВОНИ В ПАМЯТІ БУДУТЬ ПО ІНШОМУ І ШВИДКІСТЬ КОДУ ЗМІНЮВАТИМЕТЬСЯ ТЕЖ.

print(re.findall(r'[2520]', "Я шукаю співпадіння в 2125 році. І я їх обов'язково знайду."))  # ['2', '2', '5']
# Тому тут все працює
# із квадратними дужками
# це означає що має символ для пошуку входжень і повертає любий із знайдених символів

print(re.findall(r'[0-9]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# ['2', '1', '2', '5', '1', '2', '4', '7', '8', '6', '8']

# 1900 - 2999
print(re.findall(r'[12][0-9]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# ['21', '25', '12'] Перша цифра кожного числа == 1 або 2, а наступна люба, від 0 до 9,
# тому знайшо 21, а не 78, бо 78 - перша цифра починається не на 1 або 2.

print(re.findall(r'[12][0-9][0-9][0-9]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# У даному випадку шукаємо число із 4 цифр, де обовязково перша цифра це 1 або 2

print(re.findall(r'[А-ЯІа-яі]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# ['Я', 'ш', 'у', 'к', 'а', 'ю', 'с', 'п', 'і', 'в', 'п', 'а', 'д', 'і', 'н', 'н', 'я', 'в', 'р', 'о', 'ц',
#  'і', 'І', 'я', 'х', 'о', 'б', 'о', 'в', 'я', 'з', 'к', 'о', 'в', 'о', 'з', 'н', 'а', 'й', 'д', 'у']

print("Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124".find(r'[а-я]'))  # -1

s = 'Їжа, їжак, їдак'
reg = "[Її][жд]а"  # або "[Її][жд][ак]"  буде те саме
print(re.findall(reg, s))  # ['Їжа', 'їжа', 'їда']

print(re.findall(r'[А-ЯІа-яі.]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# ['Я', 'ш', 'у', 'к', 'а', 'ю', 'с', 'п', 'і', 'в', 'п', 'а', 'д', 'і', 'н', 'н', 'я', 'в',
#  'р', 'о', 'ц', 'і', '.', 'І', 'я', 'х', 'о', 'б', 'о', 'в', 'я', 'з', 'к', 'о', 'в', 'о',
#  'з', 'н', 'а', 'й', 'д', 'у', '.'] є крапка

s = 'Ледь-на-ледь[-ледь-ледь].'
reg = r"[А-ЯІа-яі.\[\]-]"
print(re.findall(reg, s))  # ['Л', 'е', 'д', 'ь', '-', 'н', 'а', '-',
# 'л', 'е', 'д', 'ь', '[', '-', 'л', 'е', 'д', 'ь', '-', 'л', 'е', 'д', 'ь', ']', '.']
# Дефіс завжди в кінці щоб не розумілось як діапазон

print(re.findall(r'[^0-9]', "Я шукаю7868 співпадіння в 2125 році. І я їх обов'язково знайду.124"))
# ['Я', ' ', 'ш', 'у', 'к', 'а', 'ю', ' ', 'с', 'п', 'і', 'в', 'п', 'а', 'д', 'і', 'н', 'н', 'я',
#  ' ', 'в', ' ', ' ', 'р', 'о', 'ц', 'і', '.', ' ', 'І', ' ', 'я', ' ', 'ї', 'х', ' ', 'о', 'б',
#  'о', 'в', "'", 'я', 'з', 'к', 'о', 'в', 'о', ' ', 'з', 'н', 'а', 'й', 'д', 'у', '.']
# Все що завгодно тільки не цифра - завдяки циркумфлекс ^

"""знайти час в форматі : [16:25]
тест: 
  Час в 24 годинному форматі від 00 до 23. 2021-06-15Т21:45.
   Хвилини в діапазоні від 00 до 59. 2021-06-15Т01:09.
 ['21:45', '01:09']
  """

test1 = '2021-06-15Т21:45'
test2 = '2021-06-15Т01:09'
print(re.findall(r'[0-2][0-3][:][0-5][0-9]', test1))  # ['21:45']  тут точніший варіант
print(re.findall(r'[0-9][0-9][:][0-9][0-9]', test2))  # ['01:09']  тут гірший варіант
test3 = (re.findall(r'[0-2][0-3][:][0-5][0-9]', test1)) + (re.findall(r'[0-9][0-9][:][0-9][0-9]', test2))
print(test3)

"""
r'.' - Це абсолютно любий символ
"""

"""
r'\.' - Із бекслешом ця комбінація поверне усі крапки які знайде ('\\.' - можна так)
"""

"""
r'\d' - Це цифра
"""

"""
r'w' - цифра буква символ 'підкреслення'
"""

"""
r'\s' - Space
"""
"""
r'\S' - все окрім Space. 
"""
# у бек слеш + великому регістрі ми вказуємо, що НЕ потрібно повертати!

"""
r'\b' - шукає на початку або в кінці слова
"""

"""
r'\Z' - Шукає символи в кінці строки і повинне бути в кінці нашого шаблону
"""

"""
r'\A' - Шукає символи в початку строки
"""

strok = "11 23 44 55 23 22"
zam_pid_strok = '23'
zamina = '!!!'
all_task = [zam_pid_strok, zamina, strok]
# p = []
# for i in range(0,3):
#     i = input("ввести під строку, строку на якеу замінити, і строку в якій замінити, через ентер")
#     p.append(i)
# print(re.sub(p[0], p[1], p[2]))

print(strok.replace('23', '!!!'))


def zaminnuk(zam_pid_strok, zamina, strok, kilk=0):
    return re.sub(zam_pid_strok, zamina, strok, kilk)


print(zaminnuk('23', '!!!', "11 23 44 55 23 22", kilk=1))

s = 'I am learning python. hello WORLD!'
s1 = s[s.find('h') + 1:s.rfind("h")]
s2 = (re.split("", s1))

s3 = list(reversed(s2))  # s2[::-1]
s3 = "".join(s3)  # "".join(s2[::-1])

print(s1, s2, s3)
s4 = s.replace(s[(s.find('h') + 1):(s.rfind("h"))], s3)
print(s4)

print(s2[::-1])

s1 = s[:s.find('h') + 1] + s1[::-1] + s[s.rfind("h"):]
print(s1)

# Розпишу простими словами
firstH = s.find("h")  # індекс першого 'h'
lastH = s.rfind('h')  # індекс останнього 'h'

pidstroka = s[firstH + 1:lastH]  # on. це у нас шуканий підрядок у строці
reversed_pidstrok = "".join(reversed(pidstroka))  # .no # знайшов реверс підстроки

result = s[0:firstH + 1] + reversed_pidstrok + s[lastH:]
# звичайною канкатенацією у місце де повинна ставитись підстрока,
# ставлю перекручену підстроку
print(result)

my_string = "Мені 13 минало"
reversed_string = my_string[::-1]
# ЩОБ СПРАЦЮВАВ ДАНИЙ РЕВЕРС НЕОБХІДНО ЗАДАВАТИ ТІЛЬКИ ЦИФРУ КРОКУ З МІНУСОМ
print(reversed_string)

mY_string = "Замінити в цьому рядку усі наявні букви 'о' на букву 'О', окрім першого та останнього входження."
st_first = mY_string.find("о")  # Перше входження
st_last = mY_string.rfind("о")  # Друге входження
my_result = mY_string[:st_first + 1] + mY_string[st_first + 1:st_last].replace("о", "О") + mY_string[st_last:]
# Канкатенація
print(my_result)
