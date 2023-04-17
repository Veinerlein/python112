def create_phone_number(n):
    ret = ""
    for element in n:
        ret += str(element)
    res = "(" + f"{ret[0:3]}" + ")" + " " + f"{ret[3:6]}" + "-" + f"{ret[6:]}"

    return res


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def create_phone_number(n):
    ret = "".join(map(str, n))
    res = "(" + f"{ret[0:3]}" + ")" + " " + f"{ret[3:6]}" + "-" + f"{ret[6:]}"

    return res


print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


# help(format)

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

"Преобразувати список у словник таким чином, щоб строкові значення були ключами, а числові - значеннями"
l = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
b = []
d = {}
for i in l:
    if type(i) == str:
        d[i] = []
        s = d[i]
    else:
        s.append(i)

print(b)

print(d)
l2 = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d2 = {}
# for i in range(0, len(l2), 4):
#     if isinstance(l2[i], str):
#         d2[l2[i]] = l[i+1:i+4] if i+4 <= len(l) else []
#
# print(d2)# код GPT зі сраки

