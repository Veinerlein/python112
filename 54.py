class Human:
    def __init__(self, last_name, first_name, age):
        self.lastname = last_name
        self.firstname = first_name
        self.age = age

    def info(self):
        # print("Тут працює Human")
        print(f'{self.lastname} {self.firstname} {self.age}!', end=" ")


class Student(Human):
    def __init__(self, last_name, first_name, age, spec, group, rating=None):
        super().__init__(last_name, first_name, age)
        self.spec = spec
        self.group = group
        self.rating = rating

    def info(self):
        super().info()
        # print("Тут працює Student")
        print(f"Speciality: {self.spec}, Group: {self.group}",end=" ")
        if self.rating != None:
            print(f"{self.rating}")

class Teacher(Human):
    def __init__(self,last_name, first_name, age, spec, exp):
        super().__init__(last_name, first_name, age)
        self.spec=spec
        self.exp = exp


    def info(self):
        super().info()
        print(f"Speciality: {self.spec}, Experience: {self.exp}")

class Graduate(Student):
    def __init__(self, last_name, first_name, age, spec, group,  course, topic):
        super().__init__(last_name, first_name, age, spec, group)
        # self.speciality = spec
        # self.group = group
        self.course = course
        self.topic = topic


    def info(self):
        super().info()
        # print("Тут працює Graduate")
        print(f"Course: {self.course}, Topic: {self.topic}")


p1 = Student("Button", "Benjamin", 16, "GK", "Web_011", 50)
p2 = Teacher("Cruze", "Penelope", 21, "Developing app's", "20 years exp")
p3 = Graduate("Shnaider", "Zack", 15, "PGO", "PD_011", 4, "Protection")

group = [
    p1,
    p2,
    p3
]

for i in group:
    i.info()

print(p1.lastname)  # "Button"
print(p1.age)  # 16
print(p3.topic)  # 'Protection'
print(p3.spec)  # 'PGO'
print(p2.exp)  # 20 years exp
print(p3.course)
print(p1.rating)