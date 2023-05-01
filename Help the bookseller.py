"""
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a
 code c of 3, 4, 5 or more characters.
 The 1st character of a code is a capital letter which defines the book category.
In the bookseller's stocklist each code c is followed by a space and by a positive integer n
(int n >= 0) which indicates the quantity of books of this code in stock.
For example an extract of a stocklist could be:
L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
M = {"A", "B", "C", "W"}
or
M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum
 their quantity according to each category.
For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket/Prolog
a list of pairs):
(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A,
114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category
'W' since there are no code beginning with W.
If L or M are empty return string is "" (Clojure/Racket/Prolog should return an empty array/list
 instead).

Notes:
In the result codes and their values are in the same order as in M.
See "Samples Tests" for the return.

"""


def stock_list(list_of_art, list_of_cat):
    r = []
    s = ""
    result = {}
    for i in list_of_art:
        for el in list_of_cat:
            if el == i[0]:
                ind = i.find(" ")
                r += [f"{el}:{i[ind:]}"]
            elif el != i[0]:
                r += [el + ":" + '0']
    for i in r:
        k, v = i.split(":")
        if k in result:
            result[k].append(int(v))
        else:
            result[k] = [int(v)]
    for r in result:
        if len(result[r]) > 0:
            result[r] = sum(result[r])
    for r in result:
        s += f' ({r} : {result[r]}) -'
    return s[1:-2]


# b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]

b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]

print(stock_list(b, c))

"""

'(A : 0) - (B : 1290) - (C : 515) - (D : 600)'

"""


# def stock_list1(list_of_art, list_of_cat):
#     r = []
#     s = ""
#     result = {}
#     for el in list_of_cat:
#         for i in list_of_art:
#             if el == i[0]:
#                 ind = i.find(" ")
#                 print("ind",ind)
#             else:
#                 print(f"{el}:0")
#
#
#
# L = ["BKWRK 150", "BTSQZ 515", "DRTY 600"]
# M = ["A", "B", "C", "D"]
#
# stock_list1(L,M)

def stock_list1(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result


# print(stock_list1(b,c))


from collections import Counter


def stock_list2(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)


# print(stock_list2(b,c))

def stock_list3(stocklist, categories):
    if not stocklist or not categories:
        return ""
    return " - ".join(
        "({} : {})".format(
            category,
            sum(int(item.split()[1]) for item in stocklist if item[0] == category))
        for category in categories)


# print(stock_list3(b,c))

def stock_list4(listOfArt, listOfCat):
    if listOfArt and listOfCat:
        return " - ".join(
            ['(%s : %d)' % (c, sum([int(i.split(" ")[1]) for i in listOfArt if c == i[0]])) for c in listOfCat])
    else:
        return ""


def stock_list5(listOfArt, listOfCat):
    """Return a the number of books by category in a formatted way

    Args:
        listOfArt (tuple or list): list of book codes
        listOfCat (tuple or list): list of categories

    Returns:
        str: number of books by category in the format '<category> : <number of books> - ...'
    """
    if len(listOfArt) == 0 or listOfCat == 0:
        return ''

    books = {}
    for code in listOfArt:
        book = code.split()
        if book[0][0] in books:
            books[book[0][0]] += int(book[1])
        else:
            books[book[0][0]] = int(book[1])
    result = []
    for cat in listOfCat:
        num = books[cat] if cat in books else 0
        result.append('({} : {})'.format(cat, num))
    return ' - '.join(result)


print(stock_list5(b, c))


def stock_list6(a, b):
    a = [(q, sum(int(x.split()[1]) for x in a if x[0] == q)) for q in b]
    return ''.join(['({} : {}) - '.format(x[0], x[1]) for x in a]).strip(' - ') if sum(x[1] for x in a) != 0 else ''


def stock_list7(a, c):
    final = []
    for i in c:
        d = 0
        for j in a:
            if j[0] == i:
                d += int(j.split()[1])
        final += ['({} : {})'.format(i, d)]
    return '' if not a else ' - '.join(final)


def stock_list8(list_of_art: list[str], list_of_cat: list[str]) -> str:
    if not list_of_art: return ''
    res = dict.fromkeys(list_of_cat, 0)
    for art in list_of_art:
        code, amount = art.split()
        if code[0] in res: res[code[0]] += int(amount)
    return ' - '.join(f'({k} : {v})' for k, v in res.items())
