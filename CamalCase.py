text = "an empty string was provided but not returned"

s = text.title()
for i in s:
    if i == " " or i == "-" or i == "_":
        not_i = ""
        s = s.replace(i, not_i)
        if text[0].islower():
            s = s.replace( s[0],s[0].lower())
print(s)



# print(i,end="")
# s.index(i) чомусь постійно = 2, чи означає це, що пайтон у строку постійно кладе значення
# індекса 2 тоді коли потрібно викласти пробіл? тобто індекс любого пробілу буде = 2(ТАК І Є).
# Також пайтон економить на памяті і букви які уже були згадані раніше, матимуть інші індекси.
# Ось так буде виглядати строка s по індексам
# 01(2)34567(2)96111(2)114(2)16179(2)51122231225325229306212262113630111325
"""
Список наших індексів строки s [0, 1, 2, 3, 4, 5, 6, 7, 2, 9, 6, 11, 12, 1, 
 14, 2, 16, 17, 9, 2, 5, 11, 22, 23, 12, 25, 3, 25, 2, 29, 30, 6, 2, 1, 22, 6,
 2, 11, 3, 6, 30, 11, 1, 3, 25]
"""


# s1 = s.title()
# for i in s1:
#     if i != "":
#         # I=(s1.index(i))
#         not_i = ""
#         s1=s1.replace(i,not_i)
# print("Second",s1)
#     # print(i,end="")


"""
Other decisions
"""
# if __name__ == "__main__":  #це дозволяє вам виконувати код,
#     # коли файл працює як сценарій,
#     # але не коли його імпортовано як модуль
#     pass

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
'*******'
def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])
'*******'
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
'*******'


import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)
'*******'
def to_camel_case(text):
    cap = False
    newText = ''
    for t in text:
        if t == '_' or t == '-':
            cap = True
            continue
        else:
            if cap == True:
                t = t.upper()
            newText = newText + t
            cap = False
    return newText
'*******'

from re import compile as reCompile

PATTERN = reCompile(r'(?i)[-_]([a-z])')

def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)

def to_camel_case(text):
    return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])

















































