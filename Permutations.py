"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""

st = "Hello World!"

from random import shuffle

#
#
# def p(s):
#     result = []
#     l = len(s)
#     d = 1
#     l = len(s)
#     while l != 1:
#         d *= l
#         l -= 1
#     while len(result)<d:
#         r = (list(s))
#         shuffle(r)
#         r = "".join(r)  # змінена склеєна строка
#         for i in range(d):
#             if not r in result:
#                 result.append(r)  # Додати строку у список
#
#     return result
#
# print(p("1234"))

# def p2(s):
#     length = len(s)
#     diapazone = length
#     res = []
#     while length > 1:
#         diapazone *= (length - 1)
#         length -= 1
#     l = list(s)
#     while len(res) < diapazone:
#         shuffle(l)
#         st = "".join(l)
#         if not st in res:
#             res.append(st)
#     return res
#
#
# print(p2("abcd"))


# def p3(s): # проходить успішно перші тести
#     length = len(s)
#     l = list(s)
#     res = []
#     cnt = 0
#     while cnt != length + 1:
#         for i in range(length):
#             val = l.pop(i)
#             l.insert(i + 1, val)
#             r = l.copy()
#             if not r in res:
#                 res.append(r)
#             cnt2 = 0
#             while cnt2 != length + 1:
#                 for i in range(-1, -length - 1, -1):
#                     val = l.pop(i)
#                     l.insert(i - 1, val)
#                     r = l.copy()
#                     if not r in res:
#                         res.append(r)
#                     cnt3 = 0
#                     while cnt3 != length + 1:
#                         for i in range(-1, -length - 1, -1):
#                             val = l.pop(i)
#                             l.insert(i - 1, val)
#                             r = l.copy()
#                             if not r in res:
#                                 res.append(r)
#                         cnt3 += 1
#                 cnt2 += 1
#         cnt += 1
#
#     if length == 1:
#         return list(s)
#     return list(map(lambda x: "".join(x), res))
#
# print(p3("abcd"))

# def p4(s): # проходить успішно перші тести
#     length = len(s)
#     l = list(s)
#     res = []
#     cnt = 0
#     while cnt != length + 1:
#         for i in range(length):
#             val = l.pop(i)
#             l.insert(i + 1, val)
#             r = l.copy()
#             p = 1
#             for e in range(length):
#                 v = r.pop(e)
#                 r.insert(e + p, v)
#                 p += 1
#                 t = r.copy()
#                 if not t in res:
#                     res.append(t)
#             if not r in res:
#                 res.append(r)
#         cnt += 1
#
#     if length == 1:
#         return list(s)
#     return list(map(lambda x: "".join(x), res))
#
# print(p4("abcd"))

# string_list = [None for _ in range(len(s))]
# i = 0
# for e in range(len(s)):
#     if not s[e] in string_list:
#         string_list.append([s[e]])

#     string_list.insert(i, elem)
#     print(string_list)


# print(permutations("ba"))
#
# print(permutations('a'))
# print(permutations('ab'))
# print(permutations('abc'))
# print(permutations('aabb'))
# print(permutations('12345678'))
# print(permutation('1234'))
# print(('1234'[-2]))


# def p5(s):  #  модуль random збільшує час виконання суттєво
#     res = []
#     l = list(s)
#     length = len(l)
#     d=len(l)
#     while length>1:
#         d*=length-1
#         length-=1
#     while len(res) < d:
#         shuffle(l)
#         r=l.copy()
#         if r in res:
#             pass
#         else:
#             res.append(r)
#     return list(map(lambda x: "".join(x), res))
#
#
# print(p5("1234"))

# def p6(s):  # працює
#     if len(s) <= 1:
#         return [s]
#     per = p6(s[1:])
#     ch = s[0]
#     res = []
#
#     for p in per:
#         for i in range(len(p) + 1):
#             exm = p[:i] + ch + p[i:]
#             if not exm in res:
#                 res.append(exm)
#     return res
#
#
# print(p6("abcd"))
#
#
# def recurs(s):
#     if len(s) > 1:
#         return recurs(s[:-1])
#     # l = list()
#     # l.append(recurs(s[1]))
#
#
# # print(recurs("abcd"))
#
# import itertools
#
#
# def custom_permutations(s):
#     per = itertools.permutations(s)
#     res = list({''.join(p) for p in per})
#     return res
#
#
# # Example usage:
# # s = "abc"
# # result = custom_permutations(s)
# # print(result)
#
# print(custom_permutations("abcd"))
# print(custom_permutations("ab"))
# print(custom_permutations("a"))
# print(custom_permutations("aabb"))

"""
An integer partition of n is a weakly decreasing list of positive integers which sum to n.
For example, there are 7 integer partitions of 5:
[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
Write a function which returns the number of integer partitions of n.
The function should be able to find the number of integer partitions of n for n
    at least as large as 100.
"""

print("=" * 45)  # =========================================


def ally_permutations(string):
    if len(string) == 1: return set(string)
    first = string[0]
    rest = ally_permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result


print(ally_permutations("abcd"))
#
# print("=" * 45)  # =========================================
#
#
# def ally_permutations2(s):
#     if len(s) == 0:
#         return []
#     elif len(s) == 1:
#         return [s]
#     else:
#         return set(s[i] + p for i in range(len(s)) for p in ally_permutations2(s[:i] + s[i + 1:]))
#
#
# print("=" * 45)  # =========================================
#
#
# def ally_permutations3(s):
#     def genInOrder(lst, p=[]):
#         if not lst:
#             yield ''.join(p)
#         else:
#             seen = set()
#             for i, c in enumerate(lst):
#                 if c in seen: continue
#                 p.append(c)
#                 seen.add(c)
#                 yield from genInOrder(lst[:i] + lst[i + 1:], p)
#                 p.pop()
#
#     return list(genInOrder(sorted(s)))
#
#
# print("=" * 45)  # =========================================
#
#
# def perm(s=''):
#     if len(s) <= 1:
#         return [s]
#     sl = []
#     for i in range(len(s)):
#         for j in perm(s[0:i] + s[i + 1:]):
#             sl.append(s[i] + j)
#     return sl
#
#
# def ally_permutations4(s):
#     return list(set(perm(s)))
#
#
# print("=" * 45)  # =========================================
#
#
# def ally_permutations5(string):
#     ps = set() #ps to hold all permutations of s
#     ps.add(string[0])
#     l = len(string)
#     i = 1
#     while i < l:
#         tmp_ps = set()
#         for p in ps:
#             ll = len(p)
#             ii = 0
#             while ii <= ll:
#                 tmp_ps.add(p[:ii]+string[i]+p[ii:])
#                 ii += 1
#         ps = tmp_ps
#         i += 1
#     return ps
#
# print(ally_permutations5("abcd"))

# def ally_permutations6(string):
#     ps = set()  # ps - це множина, в якій будуть зберігатися всі перестановки рядка s
#     ps.add(string[0])  # Додаємо перший символ рядка s до множини ps
#     l = len(string)  # Знаходимо довжину вхідного рядка
#     i = 1
#
#     while i < l:
#         tmp_ps = set()  # tmp_ps - тимч. множ., в якій будуть зберігатися перестановки на поточному етапі
#         for p in ps:
#             ll = len(p)
#             ii = 0
#             while ii <= ll:
#                 # Додаємо всі можливі вставки символу з рядка s на різні позиції в поточній перестановці p
#                 tmp_ps.add(p[:ii] + string[i] + p[ii:])
#                 ii += 1
#         ps = tmp_ps  # Оновлюємо множину ps на поточну множину tmp_ps для наступного етапу
#         i += 1
#
#     return ps  # Повертаємо множину ps, яка містить всі можливі перестановки вхідного рядка
#
# print(ally_permutations6("abcd"))  # Викликаємо функцію з рядком "abcd" і виводимо результат


def permutation(s):
    l = len(s)
    p = set()
    lst = list(s)
    res = []
    y = 1
    for i in range(len(lst)):
        for e in range(len(lst)):
            k = lst.pop(i)
            lst.insert(e,k)
            lst_final = lst.copy()
            string = "".join(lst_final)
            p.add(string)

    return p


print(permutation("abcd"))


def permut(s):
    l = len(s)
    p = set()
    lst = list(s)
    res = []
    for i in range(len(lst)):
        for e in range(len(lst)):
            k = lst.pop(i)
            lst.insert(e, k)
            lst_final = lst.copy()
            string = "".join(lst_final)
            p.add(string)

print(permut("abcd"))