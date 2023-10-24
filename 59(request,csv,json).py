import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.text
# print(data)

todos = json.loads(data)  # збереження даних у оперативну память

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)

max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

print(users)

max_users = " and ".join(users)
s = "s" if len(users) > 1 else ""
print(f"user {max_users} complited {max_complete} TODOs")
print()


def keep(todo):
    is_completed = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_completed and has_max_count


with open("data.json", "w") as f:
    td = list(filter(keep, todos))  # filter працює як і map, але окрім проходження по списку перевіряє певну умову
    json.dump(td, f, indent=4)

with open("data.json", "r") as f:
    print(json.load(f))

"""CSV (Comma Separated Value)
csv.reader
csv.writer
csv.DictReader
csv.DictWriter
"""

print("import csv")

# with open("data.csv") as f:  # звернення до елементів через індекси списку
#     reader = csv.reader(f, delimiter=",")
#     cnt = 0
#     for row in reader:
#         if cnt == 0:
#             print(f"File contains rows:\n\t{', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Was born in {row[2]}")
#         cnt += 1
#     print(f"All data in the file {cnt} string.")


with open("data.csv") as f:  # DictReader працює у стилі ключ : значення
    fields_name = ["Name", "Profession", 'Year_birth']
    reader = csv.DictReader(f, fieldnames=fields_name, delimiter=",")  # у фіелдс нейм додав поля
    cnt = 0
    for row in reader:
        if cnt == 0:
            print(f"File contains rows:\n\t{', '.join(row)}")
        print(f"{row['Name']}-{row['Profession']}.", end="")
        print(f"Was born in {row['Year_birth']}")
        cnt += 1
    print(f"All data in the file {cnt + 1} string.")

with open("student.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\r")
    writer.writerow(["Name", "Class", "Age"])
    writer.writerow(["Nick", "9", "14"])
    writer.writerow(["Nina", "5", "10"])
    writer.writerow(["Alex", "6", "11"])

data = [["hostname", "vendor", "model", 'location'],
        ['sw1', 'Cisco', '3750', 'London; Best str.'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str.'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str.'],
        ['sw4', 'Cisco', '3650', 'London, Best str.'],
        ]

with open("sw_data.csv", 'w') as f:
    writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)  # по замовчуванню lineterminator="\r\n"
    # quoting = csv.QUOTE_NONNUMERIC робить усе строковим, додає лапки
    for row in data:
        writer.writerow(row)

with open("sw_data.csv") as f:
    print(f.read())

with open("student1.csv", mode="w") as f:
    names = ['Name', 'Age']  # будуть ключами для запису, і назвами стовпців відповідно
    writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
    writer.writeheader()
    writer.writerow({"Name": "Alex", "Age": '6'})
    writer.writerow({"Name": "Helos", "Age": '9'})
    writer.writerow({"Name": "Mark", "Age": '8'})

lst_datas = []
datas = {}
cnt = 0
for d in data[1:]:
    datas["hostname"] = d[0]
    datas["location"] = d[1]
    datas["model"] = d[2]
    datas["vendor"] = d[3]
    c = datas.copy()
    lst_datas.append(c)

print(lst_datas)

# [{'hostname': 'sw1', 'location': 'Cisco', 'model': '3750', 'vendor': 'London; Best str.'},
#  {'hostname': 'sw2', 'location': 'Cisco', 'model': '3850', 'vendor': 'Liverpool, Better str.'},
#  {'hostname': 'sw3', 'location': 'Cisco', 'model': '3650', 'vendor': 'Liverpool, Better str.'},
#  {'hostname': 'sw4', 'location': 'Cisco', 'model': '3650', 'vendor': 'London, Best str.'}]

with open("dict.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(lst_datas[0].keys()), quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()  # оприділить ключі 0-вого індекса списку словників, тобто першого словника. запише ключі
    # одноразово
    for d in lst_datas:
        writer.writerow(d)

print("Homework" * 10)  # HomeworkHomeworkHomeworkHomeworkHomeworkHomeworkHomeworkHomeworkHomeworkHomework

with open("Dict_home.csv", "r") as f:
    r = csv.reader(f, delimiter=";")
    for row in r:
        print(row)


def recurs(s):
    if len(s) <= 1:  # в даному випадку умова виходу із рекурсії
        return s
    res = ""
    r = recurs(s[1:])
    first_letter = s[0]

    res +=first_letter

    return res


print(recurs("abc"))


