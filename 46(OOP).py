# class Point3D:
#     pass

class Point:
    """ПРедставлення координат точок на площині"""
    x = 1
    y = 1

    def set_curts(self, x, y):
        self.x = x
        self.y = y


print(Point.__doc__)  # ПРедставлення координат точок на площині
print(Point.__name__)  # Point
print(
    dir(Point))  # # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']

p1 = Point()
p1.x = 100
print(p1.x, p1.y)  # 100 1
print(p1.__dict__)  # {'x': 100} - показує тільки ті значення, які були змінені
print(getattr(p1, "x"))  # 100 - у екземпляра p1 значення х буде дорівнювати 100
print(getattr(p1, "z", None))  # AttributeError: 'Point' object has no attribute 'z' (None по замовчуванню виведе якщо
# буде
# помилка,
# 3 тій параметр як значення по замовчуванню)
print(hasattr(p1, "z"))  # False
print(setattr(p1, "z", 7))
print(p1.__dict__)  # {'x': 100, 'z': 7}
print(hasattr(p1, "z"))  # True - тому що setattr встановить значення
print(type(p1))  # <class '__main__.Point'>
print(isinstance(p1, Point))  # True

p1.set_curts("admin", 13)  # Hello
Point.set_curts(p1, "Arts", "tik")

p2 = Point()

p2.set_curts("Ihor", 29)  # Hello Ihor
Point.set_curts(p2, "Ihor", 72)  # Hello Ihor
# рівнозначно


p2.y = 200
print(p2.x, p2.y)  # 1 200
print(p2.__dict__)  # {'y': 200}

"""
getattr (об'єкт, ім'я [, по замовчуванню]) - для доступу до атрибуту об'єкту.
hasattr (об'єкт, ім'я) - перевірити чи атрибут дійсно існує чи ні.
setattr (об'єкт, ім'я, значення) - встановити атрибут. Якщо атрибут не існує, він буде створений.
delattr (об'єкт, ім'я) - для видалення атрибуту.
"""

p3 = Point()
p3.set_curts(5, 10)
p4 = Point()
p4.set_curts(3, 8)

print(p3.__dict__)  # {'x': 5, 'y': 10}
print(p4.__dict__)  # {'x': 3, 'y': 8}


class Human:
    name = "Name"
    date_of_birth = "Date"
    phone = "00-00-00"
    country = ""
    city = ""
    address = ""
    age = 10

    def print_info(self):
        print(" Personal Data ".center(41, "*"))
        print(f"Name: {self.name}\nBirthday: {self.date_of_birth}\nPhone Number: {self.phone}\nCountry: "
              f"{self.country}\nCity: {self.city}\nAddress: {self.address}\nAge:{self.age}\n{'=' * 40}")

    def input_info(self, first_name, birtday, phone, country, city, address):
        self.name = first_name
        self.date_of_birth = birtday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):
        self.name = name

    def set_phone(self, ph):
        self.phone = ph

    def get_phone(self):
        return self.phone

    def get_name(self):
        return self.name


h1 = Human()
h1.print_info()

h1.input_info("Juels", "23.05.1992", "45-46-67", "USA", "Seattle", "15.1 a, Bruck Avenu street")

h1.print_info()

h1.set_name("Legolas")
h1.print_info()

print(h1.get_name())


class Person:
    name = "1"
    last_name = "2"
    grade = "10"

    def set_name(self, first, last):
        self.name = first
        self.last_name = last
        return first, last

    def get_info(self):
        print(f"{'=' * 40}\nData of employee: {self.name} {self.last_name}\nQualification of employee: {self.grade}"
              f"\n{'=' * 40}")

    def improove_qualification(self, grade):
        current_grade = self.grade
        new_grade = int(current_grade) + grade
        self.grade = new_grade
        print("Qualification of employee increase to", grade)


emp1 = Person()
emp2 = Person()

emp1.set_name("Robert", "Lionheart")

emp1.get_info()
emp1.improove_qualification(12)
emp1.get_info()


# l = []
# for empl in range(1,10):
#     pers = f"pers{empl}"
#     l.append(pers)
#     print(empl)
#
# print(l)
# for pers in l:
#     pers = Person()
#
# Тут хотів зрозуміти як побудувати велику кількість екземплярів класу використовуючи генератор циклу for
#
# pers.get_info()

# instances = [Person() for parameter in range(100)] - цей шлях

class Car:
    model = "Model of Car"
    year = "Year of model"
    brand = "Brand"
    power = "power"
    colour = "color"
    price = "price"

    def print_info(self):
        print(f"Information about the car: {self.model}\nYear {self.year}\nBrand {self.brand}"
              f"\nPower {self.power}\nColour {self.colour}\nPrice {self.price}")

    def set_info(self, model, year, brand, power, colour, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.power = power
        self.colour = colour
        self.price = price

    def power_auto(self, power):
        self.power = power

    def show_power(self):
        print(self.power)


car1 = Car()
car1.set_info("Audi A7", 2009, "Wolksfagen Motors", 2000, "Black", "7000 dollars")
car1.print_info()

car1.power_auto(3500)
car1.show_power()


class Book:
    name_of_the_book = "01"
    year = "02"
    publisher = "03"
    genre = "04"
    autor = "05"
    price = "06"

    def print_info(self):
        print(f"Вивід даних: {self.name_of_the_book}\n{self.year}\n{self.publisher}\n{self.genre}\n{self.autor}\n"
              f"{self.price}")

    def set_info(self, name, year, publisher, genre, autor, price):
        self.name_of_the_book = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def get_name(self):
        print(self.name_of_the_book)

    def get_year(self):
        print(self.year)

    def get_publisher(self):
        print(self.publisher)

    def get_genre(self):
        print(self.genre)

    def get_autor(self):
        print(self.autor)

    def get_price(self):
        print(self.price)


class P:
    skill = 10

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_info(self):
        print("Data of employee:", self.name, self.surname)

    def add_skill_point(self, k):
        self.skill += k
        print("Qualification of employee:", self.skill, "\n")


p1 = P("Vsevolod", "Nestaiko")
p1.print_info()
p1.add_skill_point(3)

p2 = P("Anna", "Ahmatova")
p2.print_info()
p2.add_skill_point(2)


class Pointer:
    count = 0  # статична властивість

    def __new__(cls, *args, **kwargs):  # прописується програмістами тільки для створення метакласів,
        print("Constructor")  # А взагальному, то виконується сам по собі по замовчуванні
        return super().__new__(cls)

    def __init__(self, x=0, y=0):  # динамічні властивості
        self.x = x
        self.y = y
        Pointer.count += 1  # (не прив'язується до екземпляру класу) звертаючтсь до імені класу, кожного разу,
        # ( не тільки при створенні
        # екземпляру),
        # у статичну властивість count буде збільшуватись на одиницю
        # self.count+=1 # збільшитться тільки 1 раз тільки для екземпляра
        print("Initializator")

    def __del__(self):  # працює автоматично, можна прописати щоб запрограмувати розрив зв'зку із екземпляром раніше
        # по спеціально заданому сценарію
        print("Delete Exempl" + self.__class__.__name__)

    def set_coords(self, x, y):
        self.x = x
        self.y = y


p1 = Pointer(5, 10)

print(p1.__dict__)  # {'x': 5, 'y': 10} виведе значення які присвоєні через ініціалізатор

# del p1
print(p1.x)
p2 = Pointer()
print(p2.__dict__)  # {'x': 0, 'y': 0} оскільки не змінювали значення, то попали ті, що по замовчуванню

p2 = Pointer(10, 20)

print(Pointer.count)
print(p1.count)
print(p2.count)

# print(Pointer.x)
print(p1.x)


class Robots:
    count_of_robots = 0

    def __init__(self, name):
        self.name = name
        Robots.count_of_robots += 1

    def print_info(self):
        print(f"Initialization of robot {self.name}\nHello, my name is {self.name}\nQuantity of robots "
              f"{self.count_of_robots}\n{'=' * 40}")

    def end_of_work(self):
        print(f"Robots have finished their work. Let us off them")
        Robots.count_of_robots -= 1
        print(f"{self.name} is Turning off\nWorking robots left {self.count_of_robots}")
        if self.count_of_robots == 0:
            print(f"{self.name} was the last")
        print("=" * 40)
        del self


r1 = Robots("R2-D2")
r1.print_info()
r2 = Robots("C-3PO")
r2.print_info()

r1.end_of_work()
r2.end_of_work()


class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print(f"Initialization of robots: {self.name}")
        print(f"Hello, my name is {self.name}")
        Robot.k += 1

    def __del__(self):
        print(self.name, "is off!")
        Robot.k -= 1

        if Robot.k == 0:
            print(self.name, "was the last one")
        else:
            print(f"Working robots left", Robot.k)


droid1 = Robot("R2_D2")
print("Quantity of robots:", Robot.k)

droid2 = Robot("C3_PO")
print("Quantity of robots:", Robot.k)

print("*" * 30)
del droid1
del droid2

print("Quantity of robots:", Robot.k)

b1 = Book()

b1.print_info()
