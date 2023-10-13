import json


class Student:

    def __init__(self, surname, firstname, marks: list):
        self.check_list(marks)
        self.surname = surname
        self.firstname = firstname
        self.__marks = marks

    def __str__(self):
        return f"{self.firstname} {self.surname}: {self.__marks}"

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, m: list):
        self.__marks = m

    def add_mark(self, m):
        self.marks.append(m)

    def del_mark(self, ind):
        del self.__marks[ind - 1]

    def change_mark(self, value, ind):
        self.del_mark(ind + 1)
        self.marks.insert(ind, value)

    def check_list(self, x):
        if isinstance(x, list):
            return x
        else:
            raise TypeError

    def average_mark(self):
        return sum(map(int, self.__marks)) / len(self.__marks)

    def read(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data

    def write(self, filename):
        try:
            memory = self.read(filename)
        except (FileNotFoundError, json.JSONDecodeError):
            memory = []
        d = [{'Name': f'{self.surname} {self.firstname}', "Marks": self.marks}]
        memory.extend(d)
        with open(filename, "w") as f:
            json.dump(memory, f, indent=4)


student1 = Student("John", "Malkovich", [91, 82, "78", 75])
student2 = Student("Milos", "Ninkovich", [71, 62, "98", 73])
student3 = Student("Marius", "Levandovski", [81, 81, "88", 78])

student2.write("Srudent.json")
student3.add_mark(45)

print(student3)
student3.change_mark(100, 0)
print(student3)
print(student1.average_mark())

l = [student1, student2, student3]


class Group(Student):

    def __init__(self, lst, surname=None, firstname=None, marks: list = None, group=None):
        if group is None:
            group = []
        if marks is None:
            marks = []
        super().__init__(surname, firstname, marks)
        self.check_type(lst)
        self.lst = lst
        # self.tempgroup=[]
        if surname and firstname and marks is not None:
            self.tempgroup = [Student(surname, firstname, marks)]
        self.group = group

    def __str__(self):
        res = [str(student) for student in self.lst]
        return ", ".join(res)

    def add_student(self):
        r = self.lst.append(self.tempgroup[0])
        return r

    def tempgroup(self):
        if self.surname and self.firstname and self.marks is not None:
            return self.tempgroup
        return []

    def check_type(self, l):
        for i in l:
            if not isinstance(i, Student):
                raise TypeError

    def trnsfer_student(self, student, grope_out):
        if student in grope_out.group:
            self.lst.append(student)
            grope_out.group.remove(student)
        return self.lst

    def read_group(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data

    def write_data(self, filename):
        # try:
        memory = self.read_group(filename)  # зчитає пустий список так, як я організщував виключення у методі читання
        # except (FileNotFoundError, json.JSONDecodeError):
        #     memory = [] - не потрібно, так як все зроблено у методі прочитанні
        templist = {}  # готовий пустий словник

        for i in self.lst:  # ітерація по списку об'єктів, по кожному self
            templist.update({"Student": f"{i.surname} {i.firstname}", "Marks": i.marks})  # У кожен елемент попаде
            # відповідне значення із назви змінних у класі Студент, а у i. == self. у класі студент
            tmp = templist.copy()  # копія списку для того, щоб не змінювались дані під останній об'єкт
            memory.append(tmp)  # додав до списку клон із оновленого словника по об'єету
        with open(filename, "w") as f:
            json.dump(memory, f, indent=4)  # запис


studing1 = Group(l, "Kolia", "Zigryi", [54, 67, 56, 44, 78])
studing2 = Group([])
studing1.trnsfer_student(student1, studing2)
print(studing2)
print(studing1)
# print(studing1.tempgroup)
studing1.add_student()
print(studing1)
# print(studing1.read_group("Group.json"))
# studing1.write_data("Group.json")
print("=" * 56)  # ========================================================


class Stud:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_tojson(cls, student, filename):
        try:
            data = json.load(open(filename))
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append({'Name': student.name, "Marks": student.marks})
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as f:
            return json.load(f)


class Grupe:
    def __init__(self, students, name_groupe):
        self.grupe = name_groupe
        self.std = students

    def __str__(self):
        res = ", ".join([str(i) for i in self.std])  # Bodnuya: 55, 66, 80, 90, 53, Yupiwo: 75, 56, 87, 78, 78
        return f"{self.grupe}:\n {res}"

    # def __str__(self):  #  Bodnuya: 55, 66, 80, 90, 53
    # Yupiwo: 75, 56, 87, 78, 78
    #     a = ''
    #     for i in self.std:
    #         a+=str(i)+"\n"
    #     return f"{a}"

    def add_student(self, student):
        self.std.append(student)

    def del_student(self, index):
        if index > len(self.std):
            index = len(self.std) - 1
        del self.std[index]

    def remove_student(self, index):
        return self.std.pop(index)

    def trnsfer_student(self, student, grope_out):
        if student in grope_out:
            self.std.append(student)
            grope_out.remove(student)
        return self.std

    # Альтернатива
    @classmethod
    def change_grup(cls, grup1, grup2, index):
        grup2.std.append(grup1.std[index])
        del grup1.std[index]

    @classmethod
    def change_grupe(cls, grup1, grup2, index):
        return grup2.add_student(grup1.remove_student(index))  # for this method => # def remove_student(self, index):
        # ____________________________________________________________________________     return self.std.pop(index)

    @classmethod
    def dump_grup(cls, file, group):
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
            with open(file, "w") as f:
                stud_list = []
                for i in group.std:
                    stud_list.append([i.name, i.marks])
                tmp = {"Students": stud_list}
                data.append(tmp["Students"])
                json.dump(data, f, indent=4)

    @classmethod
    def upload_journal(cls, file):
        with open(file, 'r') as f:
            print(json.load(f))


st1 = Stud('Bodnuya', [55, 66, 77, 88, 90])
st2 = Stud('Yupiwo', [75, 56, 87, 78, 78])
st3 = Stud('Krimans', [78, 68, 97, 68, 81])

sts = [st1, st2]
my_group = Grupe(sts, "Python")
print(my_group)
group22 = [st3]
my_group2 = Grupe(group22, "WEB")
# Grupe.change_grup(my_group2, my_group, 0)
Grupe.change_grupe(my_group2, my_group, 0)
print(my_group)
print(my_group2)

# my_group.add_student(st3)
# print(my_group)
# my_group.del_student(2)
# print(my_group)

# my_group.trnsfer_student(st3, group22)
print("після трансферу", my_group)
print("після трансферу", group22)
print(st1)

st1.add_mark(53)  # + ,90
st1.delete_mark(3)  # - 88,
# print(st1)
st1.edit_mark(2, 80)
print(st1)  # 77 =>80
print(st1.average_mark())
Stud.dump_tojson(st1, "Students.json")
Stud.load_from_file("Students.json")

my_group.dump_grup("Grupe.json", my_group)
Grupe.upload_journal("Grupe.json")

print("=" * 56)  # =======================================================================

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(response.text)

print(data[:10])
print(type(data))  # <class 'list'>
print("=" * 56)  # =======================================================================


class Europe:

    def __init__(self):
        self.dict_cntrs = {}

    def add_data(self, country_capital):
        country = country_capital.split(", ")[0]
        capital = country_capital.split(", ")[1]
        self.dict_cntrs.update({f"{country}": f"{capital}"})

    def del_data(self, country, capital=None):
        del self.dict_cntrs[country]

    def __str__(self):
        return f"{self.dict_cntrs}"

    def data_search(self, word):
        d = None
        for i in self.dict_cntrs.items():
            if word in i:
                print(i)
                return i
                # return {i[0]: i[1]}

        # results = {}
        # for country, capital in self.dict_cntrs.items():
        #     if word in capital:
        #         results[country] = capital
        # print(results)
        # return results

    def edit_data(self, data_to_change, change_to):
        self.dict_cntrs[change_to[0]] = change_to[1]
        del self.dict_cntrs[data_to_change]
        return self.dict_cntrs

    def dumping(self, filename):
        data = self.dict_cntrs
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def chose(self):
        context = ["Input what you wont to add", "Input what you need to delete", "Input what you need to find",
                   ("Input what you want to edit", "Now add plaese a list with data what you want "
                                                   "to get instead"),
                   "input the name of file in a format  (name of file).json  "]
        lst_functions = [
            self.add_data,
            self.del_data,
            self.data_search,
            self.edit_data,
            self.dumping,
            self
        ]
        num = int(input("Chose the business")) - 1
        for i in lst_functions:
            if num == lst_functions.index(i) and num != 3 and num != 5:
                i(input(context[lst_functions.index(i)]))
            elif num == lst_functions.index(i) and num == 3:
                i(input(), input())
            else:
                return print(self)

    def choise(self, n):
        d = {1: ("Input what you wont to add", self.add_data),
             2: ("Input what you need to delete", self.del_data),
             3: ("Input what you need to find", self.data_search),
             4: ("Input what you want to edit, Now add plaese a list with data what you want to get instead",
                 self.edit_data),
             5: ("input the name of file in a format  (name of file).json", self.dumping),
             6: ("information view", print(self))
             }
        # ['Input what you need to find', '<bound method Europe.data_search of <__main__.Europe
        # object at 0x000002F3156CFF10>>']

        if n in d:
            action = d[n][1]
            if callable(action):
                return action(input(d[n][0]))
            elif not callable(action):
                return d[n][1]  # d[n][1] # виклик функції, яка є елементом 1 у кортежі під номером n
            else:
                print(d[n][0])
        else:
            print("Invalid choice")


c = Europe()
# print(c)
c.add_data("Ukraine, Kiiv")
# print(c)
c.add_data("USA, Washington")
c.add_data("Grate Britain, London")
c.add_data("Italy, Roma")
# print(c)
c.del_data("USA", "Washington")
# print(c)
print(c.data_search("Kiiv"))
print(c.edit_data("Grate Britain", ["Arsenal", "Zinchenko"]))
# print(c)
c.dumping("Europe.json")
# c.chose()
# c.chose()
c.choise(3)
# c.choise(6)
