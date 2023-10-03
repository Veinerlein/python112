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
# def permutations(s):
#     result = []
#     r = []
#     st = ""
#     l = len(s)
#     d = 1
#     for i in s:
#         st += i
#         # if s.count(i) > 1:
#             # s=s[:s.index(i)]+s[s.index(i)+1:]
#     l = len(s)
#     while l != 1:
#         d *= l
#         l -= 1
#     # while len(result) < d:
#     for i in range(d+10):
#         r = (list(st))
#         shuffle(r)
#         r = "".join(r)  # змінена склеєна строка
#         for i in range(d):
#             if not r in result:
#                 result.append(r)  # Додати строку у список
#
#     return result
"""
def permutations(s):
    length = len(s)
    diapazone = length
    res = []
    while length > 1:
        diapazone *= (length - 1)
        length -= 1
    l = list(s)
    for x in range(100000):
        shuffle(l)
        st = "".join(l)
        if not st in res:
            res.append(st)
    return res
"""


def permutations(s):
    length = len(s)
    l = list(s)
    res = []
    cnt = 0
    while cnt != length + 1:
        for i in range(length):
            val = l.pop(i)
            l.insert(i + 1, val)
            r = l.copy()
            if not r in res:
                res.append(r)
            cnt2 = 0
            while cnt2 != length + 1:
                for i in range(-1, -length - 1, -1):
                    val = l.pop(i)
                    l.insert(i - 1, val)
                    r = l.copy()
                    if not r in res:
                        res.append(r)
                    cnt3 = 0
                    while cnt3 != length + 1:
                        for i in range(-1, -length - 1, -1):
                            val = l.pop(i)
                            l.insert(i - 1, val)
                            r = l.copy()
                            if not r in res:
                                res.append(r)
                        cnt3 += 1
                cnt2 += 1
        cnt += 1

    if length == 1:
        return list(s)
    return list(map(lambda x: "".join(x), res))


def permutation(s):
    length = len(s)
    l = list(s)
    res = []
    cnt = 0
    while cnt != length + 1:
        for i in range(length):
            val = l.pop(i)
            l.insert(i + 1, val)
            r = l.copy()
            p = 1
            for e in range(length):
                v = r.pop(e)
                r.insert(e + p, v)
                p += 1
                t = r.copy()
                if not t in res:
                    res.append(t)
            if not r in res:
                res.append(r)
            # cnt2 = 0
            # while cnt2 != length + 1:
            #     for i in range(-1, -length - 1, -1):
            #         val = l.pop(i)
            #         l.insert(i - 1, val)
            #         r = l.copy()
            #         for e in range(-1, -length - 1, -1):
            #             v = r.pop(e)
            #             r.insert(e - 1, v)
            #             t = r.copy()
            #             if not t in res:
            #                 res.append(t)
            #         if not r in res:
            #             res.append(r)
            #     cnt2 += 1
        cnt += 1

    if length == 1:
        return list(s)
    return list(map(lambda x: "".join(x), res))

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


# def perm(s):
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
# print(perm("1234"))

def permutations(s):
    if len(s) <= 1:
        return [s]
    per = permutations(s[1:])
    ch = s[0]
    res = []

    for p in per:
        for i in range(len(p) + 1):
            exm = p[:i] + ch + p[i:]
            if not exm in res:
                res.append(exm)
    return res


# def permutation(s):
#     if len(s) <= 1:
#         return [s]
#
#     perms = permutation(s[1:])
#     char = s[0]
#     result = []
#
# # Для кожної перестановки решти символів
#     for i in range(2):
#         # Вставляємо перший символ на різні позиції
#         result.append(perms[0] + char + perms[1])
#
#     return result

# print(permutations('aabb'))


# print(permutations('1234'))
# print(permutation('1234'))


def recurs(s):
    if len(s) > 1:
        return recurs(s[:-1])
    # l = list()
    # l.append(recurs(s[1]))


# print(recurs("abcd"))

import itertools


def custom_permutations(s):
    per = itertools.permutations(s)
    res = list({''.join(p) for p in per})
    return res


# Example usage:
# s = "abc"
# result = custom_permutations(s)
# print(result)

print(custom_permutations("abcd"))
print(custom_permutations("ab"))
print(custom_permutations("a"))
print(custom_permutations("aabb"))

"""
An integer partition of n is a weakly decreasing list of positive integers which sum to n.
For example, there are 7 integer partitions of 5:
[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
Write a function which returns the number of integer partitions of n.
The function should be able to find the number of integer partitions of n for n
    at least as large as 100.
"""


