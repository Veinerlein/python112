"""BIN SEARCH AND SORTING"""
"""бінарний та послідовний(лінійний)"""


def seq_search(listt, item):
    pos = 0  # position
    found = False
    stop = False
    while pos < len(listt) and not found and not stop:
        if listt[pos] == item:
            found = True
        else:
            if listt[pos] > item:
                stop = True
            else:
                pos += 1
    return found


lst = [1, 2, 32, 8, 45, 6, 7, 8, 232, 21]
print(seq_search(lst, 3))
print(seq_search(lst, 32))


def binary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        midlpoint = (first + last) // 2
        if s[midlpoint] == item:
            found = True
        else:
            if item < s[midlpoint]:
                last = midlpoint - 1
            else:
                first = midlpoint + 1
    return found


lst1 = [1, 2, 3, 4, 5, 7, 8, 9]

print(binary_search(lst1, 7))
print(binary_search(lst1, 6))


def binsearch(l, x):
    l = sorted(l)
    first = 0
    last = len(l) - 1
    found = False
    stop = False
    while first <= last and not found and not stop:
        midlpoint = (first + last) // 2
        if l[midlpoint] == x:
            return f"Число:{x} у списку присутнє"
        else:
            if x > l[midlpoint]:
                first = midlpoint + 1
            else:
                last = midlpoint - 1


lst2 = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]


# print(binsearch(lst2, int(input("ввести число"))))


def binser(lst, e):
    lst = sorted(lst)
    Found = False
    Stop = False
    firstpoint = 0
    lastpoint = len(lst) - 1
    while firstpoint <= lastpoint and not Found and not Stop:
        midllpoint = (firstpoint + lastpoint) // 2
        if lst[midllpoint] == e:
            Found = True
            return Found
        else:
            if lst[midllpoint] > e:
                lastpoint = midllpoint - 1
            else:
                firstpoint = midllpoint + 1


print(binser(lst2, 34))

"""""""""""""""""""""""""""""""""""""""""""""SORTING"""
# бульбашкова - Порівнює попарно, найпростіша. Якщо лівий ел більший ніж правий , міняються місцями

import random as r
import time as t


def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(a)
        # print("-" * 40)


a = [r.randint(1, 99) for i in range(10)]
start = t.monotonic()
print(bubble(a))
res = t.monotonic() - start
print(round(res, 3), "sec")
"++++++++++++++++++++++++++++"
"4 списки додати в пятий, відсортувати по порядку вперед чи назад, відносно бажанню користувача," \
" знайти значення яке введе користувач."

l1 = [5, 9, 6, 7]
l2 = [3, 11, 8]
l3 = [2, 4]
l4 = [10, 1, 12]

# def decision(*args, sort_usual=True, item=int(input("enter the number"))):
#     lst = []
#     for l in args:
#         for i in l:
#             lst.append(i)
#     if sort_usual:
#         for e in range(len(lst) - 1):
#             for e2 in range(len(lst) - e - 1):
#                 if lst[e2] > lst[e2 + 1]:
#                     lst[e2], lst[e2 + 1] = lst[e2 + 1], lst[e2]
#                 print(lst)
#     else:
#         for e in range(len(lst) - 1):
#             for e2 in range(len(lst) - e - 1):
#                 if lst[e2] < lst[e2 + 1]:
#                     lst[e2], lst[e2 + 1] = lst[e2 + 1], lst[e2]
#     found = False
#     pos = 0
#     while pos < len(lst) and not found:
#         if lst[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return lst, f"{item} found is {found}"


# print(decision(l1, l2, l3, l4, sort_usual=False))

"Рішення судді"


def decision_junge(*args, sort_usual=True, item):
    lst = []
    for l in args:
        for i in l:
            lst.append(i)
    if sort_usual:
        for e in range(len(lst) - 1):
            for e2 in range(len(lst) - e - 1):
                if lst[e2] > lst[e2 + 1]:
                    lst[e2], lst[e2 + 1] = lst[e2 + 1], lst[e2]
    else:
        for e in range(len(lst) - 1):
            for e2 in range(len(lst) - e - 1):
                if lst[e2] < lst[e2 + 1]:
                    lst[e2], lst[e2 + 1] = lst[e2 + 1], lst[e2]

    found = False
    pos = 0
    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos += 1

    return lst, f"{item} found is {found}"


# item = int(input("enter the number"))
# print(decision_junge(l1, l2, l3, l4, sort_usual=False, item=item))


def decision_tech():
    pass


# print(decision_tech())

"Сортування злиттям"  # присутня рекурсія

arr = [r.randrange(50) for i in range(10)]
print(arr)


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    left = merge_sort(a[:n // 2])
    right = merge_sort(a[n // 2:])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


# array = [8, 2, 6, 4, 5]

array = merge_sort(arr)


# print(array)


# print(arr)


def sort(array):
    length = len(array)
    if length < 2:
        return array

    l = sort(array[:length // 2])
    r = sort(array[length // 2:])

    res = []
    i, j = 0, 0
    while i < len(l) or j < len(r):
        if i >= len(l):
            res.append(r[j])
            j += 1
        elif j >= len(r):
            res.append(l[i])
            i += 1
        elif l[i] > r[j]:
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1
    return res


start = t.monotonic()
sort = sort(arr)
end = t.monotonic()
print(round(end - start, 3), "sec")

start = t.monotonic()
sort2 = merge_sort(arr)
end = t.monotonic()
print(round(end - start, 3), "sec")

"""Сортування Шелла"""


# def shell_sort(array):
#     if len(array) < 2:
#         return array
#     lng = len(array)
#     res1 = []
#     res2 = []
#     inc = 2
#     l = array[:lng // inc]
#     r = array[lng // inc:]
#     i = j = 0
#     for e in range(lng // inc):
#         if l[e] > r[e]:
#             res1.append(r[e])
#             res2.append(l[e])
#         else:
#             res1.append(l[e])
#             res2.append(r[e])
#     res = res1 + res2
#     inc *= 2
#
#     # l = shell_sort(array[:lng//2])
#     # r = shell_sort(array[lng//2:])
#
#     return res
#
# print(shell_sort(arr))

def shelSort_tech(arrey):
    gap = len(arrey)
    while gap > 0:
        for val in range(gap,len(arrey)):
            cur_val = arrey[val]
            pos = val

            while pos >= gap and arrey[pos-gap]>cur_val:
                arrey[pos] = arrey[pos - gap]
                pos -= gap
                arrey[pos] = cur_val

        gap //= 2
        print(gap, "List:", arrey)
    return arrey

print(shelSort_tech(arr))


arr.sort()



