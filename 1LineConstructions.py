from functools import reduce

"""
x, y, z = input("ввести значення через пробіл: ").strip().split()
print(f"{x},{y},{z}")  # 10,20,30
print(f"{x=},{y=},{z=}")  # x='10',y='20',z='30'

x, y, z = map(int, (x, y, z))
V = z * y * z
# print(V)

volume = reduce(lambda x, y: x * y, map(int,input().strip().split()))
# функція reduce() задіюється до двох елементів послідовності
# Крім того можна передати як 1 число так і більще за 3
print(volume)
print(reduce(lambda a,b:a+b,(10,10,10,10,10))) # 50

"""

"""
names = ["Epicur", 'Aristotel', 'Piphagor', 'Demokrit', 'Mark Avrelii']
name_has_a = [name for name in names if "a" in name]
[name_has_a.append(name) for name in names if name.__contains__("A") and not name in name_has_a]
print(name_has_a)

name_starts_a = list(filter(lambda name: name.startswith('A'), names))
print(name_starts_a)

"""
"""
numbers = [1, 2, 3]
an_num = numbers
an_num.append(100)
print(an_num)  # [1, 2, 3, 100]
print(numbers)  # [1, 2, 3, 100]

an_num = numbers[:] #  хороша альтернатива методу copy
an_num.append(23)
print(numbers)  # [1, 2, 3, 100]
print(an_num)  # [1, 2, 3, 100, 23]

revers_num = numbers[::-1]
print(revers_num)


"""

'''
name = 'Seidorf'
if name == "hfiolh" or name == "hfdjla" or name == "Bon":
    print(name)

if name in ("fdffda", "dfsaf", "fdafd"):
    print(name)
'''

'''
A = B = C = D = E = True
y = u = i = o = p = None
if all((A, B, C, D, E)):  # функція all перевірить чи всі елементи у послідовності є True
    print("gjlk")
if (y, u, i, o, p):  # вони всі None але це список None-ів і тому він існує тому він тру
    print("Не мало б бути прінта")

if any((True,True,None,None)):
    print('Щонайменше 1 елемент із True знайшовся')
    
'''


class User:
    def __init__(self, group: str):
        self.group = group

    def __str__(self):
        return f'{self.group}'


def process_admin_request(a, b):
    print(a, b)


def process_manager_request(a, b):
    print(a, b)


def process_client_request(a, b):
    print(a, b)


user = User(group="admin")

# if user.group == "admin":
#     process_admin_request(user, 'request')
# elif user.group == "manager":
#     process_manager_request(user, 'request')
# elif user.group == "client":
#     process_client_request(user, 'request')

# декларативність коду:

group_to_process_method = {
    "admin": process_admin_request,
    "manager": process_manager_request,
    "client": process_client_request
}

group_to_process_method[user.group](user, 'request')  # поверне process_admin_request так, як user.group == адмін,
# а адмін це ключ до process_admin_request, а далі уже виклик функції із необхідними аргументами
