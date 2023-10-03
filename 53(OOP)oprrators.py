class Student:
    def __init__(self, name, marks: list):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # перегрузка отримання даних у квадратних дужках
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Wrong index")

    def __setitem__(self, key, value):  # Перегрузка оператора установлення даних через ключ-значення
        if 0 <= key <= len(self.marks) and isinstance(key, int):
            self.marks[key] = value
        elif key >= len(self.marks):  # Дозволяє вставити значення на вказаний довільний індекс
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
            self.marks[key] = value
        else:
            raise IndexError("Wrong index")

    def __delitem__(self, key):  # Можливість видалити значення по ключу
        if not isinstance(key, int):
            raise TypeError("Index has to be integer")
        del self.marks[key]


s1 = Student("Sergio]", [5, 5, 3, 7, 8])
print(s1[2])  # 3 - ДЛя цього прописаний __getitem__
s1[10] = 4
del s1[2]
print(s1.marks)  # 4


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coords = x + y + z

    @staticmethod
    def checj_val(x):
        return isinstance(x, (int, float))

    def get_form(self):
        return self.x, self.y, self.z

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("The right operand must be Point3D type")
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("The right operand must be Point3D type")
        # return self.x - other.x, self.y - other.y, self.z - other.z
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("The right operand must be Point3D type")
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("The right operand must be Point3D type")
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return Point3D(self.x == other.x, self.y == other.y, self.z == other.z)


c1 = Point3D(12, 15, 18)
c2 = Point3D(6, 3, 9)
# print(c1+c2)
c3 = c1 - c2
print((c3.get_form()))
print((c1 / c2).get_form())


class Point:
    CH = "Coordinate must be integer"
    RIGHT = "Right operand has to be type Point"

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @staticmethod
    def __check_value(v):
        return isinstance(v, (int, float))

    @staticmethod
    def __check0(exempl):
        if exempl.x == 0 or exempl.y == 0 or exempl.z == 0:
            raise ZeroDivisionError("Can not divide to zero")

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"  # Оскільки створив геттр-сеттери, то тут відобраєатиметься їх результат
        # дії

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__check_value(value):
            self.__x = value
        else:
            print(self.CH)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__check_value(value):
            self.__y = value
        else:
            print(self.CH)

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if self.__check_value(value):
            self.__z = value
        else:
            print(self.CH)

    def __add__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError(self.RIGHT)
        else:
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError(self.RIGHT)
        else:
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError(self.RIGHT)
        else:
            return Point(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError(self.RIGHT)
        self.__check0(other)
        return Point(self.__x / other.x, self.__y / other.y, self.__z / other.z)

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError(self.RIGHT)
        # if self.x == other.x and self.y == other.y and self.z == other.z:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Key has to be string")
        elif item == "x":
            return self.__x
        elif item == "y":
            return self.__y
        elif item == "z":
            return self.__z
        else:
            print("Wrong value")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Must be string")
        if self.__check_value(value):
            if key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value
            elif key == "z":
                self.__z = value
        else:
            print("Wrong value")


pt = Point(12, 15, 18)
pt2 = Point(6, 3, 9)

print(f"Coordinates 1st point : {pt}")  # Coordinates 1st point : 12,15,18
print(f"Coordinates 2st point : {pt2}")  # Coordinates 2st point : 6,3,9
pt3 = pt + pt2
print(f"Sum of coordinates {pt3}")  # Sum of coordinates 18,18,27
pt6 = pt / pt2
print(f"Devided of coordinates {pt6}")  # Sum of coordinates 2.0,5.0,2.0
print(f"Equity of coordinates : {pt == pt2}")  # Equity of coordinates : False

print("x = ", pt["x"], "x1 = ", pt2["x"])  # x =  12 x1 =  6
pt["x"] = 20
print("Loading value into coordinates x:", pt["x"])  # Loading value into coordinates x: 20
print(f"Coordinates 1st point : {pt}")  # Coordinates 1st point : 20,15,18

print("=" * 89)  # ==============================================================================

print("POLYMORPHIZM")
"""POLYMORPHIZM"""


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return f"Perimetr of {__class__.__name__} is {2 * (self.w + self.h)}"


class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return f"Perimetr of {__class__.__name__} is {4 * self.a}"


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
# print(r1.get_per_rect(), r2.get_per_rect())

s1 = Square(10)
s2 = Square(20)
# print(s1.get_per_sq(), s2.get_per_sq())

shape = [r1, r2, s1, s2]

# for i in shape:
#     if isinstance(i, Rectangle):
#         print(i.get_per_rect())
#     if isinstance(i, Square):
#         print(i.get_per_sq())
for g in shape:
    print(g.get_perimetr())


class Number:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        return self.value + int(a)


class Text:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        return len(self.value + str(a))


t1 = Number(10)
t2 = Text("Python")

print(t1.total(34))
print(t2.total(34))

print("=" * 89)  # =================================================================

from abc import ABC, abstractmethod


class Cat:
    SOUND = "meowing"

    def __init__(self, name="Pookh", age=2.5):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):  # відпрацює лише у тому випадку коли немає repr
        return f"{self.__class__}: {self.name}"

    def print_info(self):
        print(f"I am {self.__class__.__name__.lower()}. My name is {self.name}. My age is {self.age}")

    def make_sound(self):
        print(f"{self.name} is {self.SOUND}.")

    @property
    def catname(self):
        return self.name

    @catname.setter
    def catname(self, x):
        self.name = x

    @catname.deleter
    def catname(self):
        del self.name


class Dog:
    SOUND = "barking"

    def __init__(self, name="Muhtar", age=4):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"I am {self.__class__.__name__.lower()}. My name is {self.name}. My age is {self.age}")

    def make_sound(self):
        print(f"{self.name} is {self.SOUND}")


a = Cat()
a1 = Dog()

print(a1.__class__.__name__.lower())
a.print_info()
a.make_sound()
a1.print_info()
a1.make_sound()

animals = [a, a1]

for a in animals:
    a.print_info()
    a.make_sound()

cat = Cat("Murlo")
print(cat)

#
# class Shape(ABC):
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def print_figure(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, a):
#         self.__a = a
#
#     def __str__(self):
#         return f"Square {self.__a},{self.__a},{self.__a},{self.__a}"
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         self.__a = a
#
#     def perimetr(self):
#         return self.__a * 4
#
#     def area(self):
#         return self.__a * self.__a
#
#     def print_figure(self):
#         [print("*" * self.__a) for _ in range(3)]
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#
#     def __str__(self):
#         return f"Rectangle {self.__a},{self.__b},{self.__a},{self.__b}"
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         self.__b = b
#
#     def perimetr(self):
#         return self.__a * 2 + self.__b * 2
#
#     def area(self):
#         return self.__a * self.__b
#
#     def print_figure(self):
#         [print("*" * self.__b) for _ in range(self.__a)]
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     def __str__(self):
#         return f"Triangle {self.__a},{self.__b},{self.__c}"
#
#     @staticmethod
#     def isosceles_triangle(a, b):
#         res = (b / 2) * (((a + b / 2) * (a - b / 2)) ** 0.5)
#         return res
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         self.__b = b
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         self.__c = c
#
#     def perimetr(self):
#         return self.__a + self.__b + self.__c
#
#     def area(self):
#         s = self.perimetr() / 2
#         return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5
#
#     def print_figure(self):
#         k = 1
#         for i in range(1, self.__b + 1):
#             spaces = " " * (self.__a - k + i)
#             k += int(i / self.__a) + i
#             stars = "*" * (k - 1)  # (int(self.__a/i))
#             # stars2 = "*"*(i-1)
#             print(spaces + stars)

from geometry import RECT, TRIAN, SQ


# from geometry import *

def main():
    f1 = SQ.Square(3)
    print(f1)
    print(f1.area())
    print(f1.perimetr())
    f1.print_figure()

    f2 = RECT.Rectangle(3, 7)
    print(f2)
    print(f2.area())
    print(f2.perimetr())
    f2.print_figure()

    f3 = TRIAN.Triangle(11, 6, 6)
    print(f3)
    print(f3.area())
    print(f3.perimetr())
    f3.print_figure()


if __name__ == "__main__":
    main()


def main2():
    e = electrocar.Electrocar("Tesla", "T", 2018, 99000)
    e.show_car()
    e.description_battery()


from car import electrocar

if __name__ == '__main__':
    main2()


class Mouse:

    def __init__(self, name):
        self.name = name

    def __repr__(self):  # Також повертає строку, Використовується для КОНСОЛІ
        return f"{self.__class__}: {self.name}"

    def __str__(self):  #  Відпрацює стр, а __repr__ не працюватиме при наявності __str__
        return f"{self.name}"


mouse = Mouse('Gerry')

print(mouse)
