from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_figure(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self.__a = a

    def __str__(self):
        return f"Square {self.__a},{self.__a},{self.__a},{self.__a}"

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    def perimetr(self):
        return self.__a * 4

    def area(self):
        return self.__a * self.__a

    def print_figure(self):
        [print("*" * self.__a) for _ in range(3)]


class Rectangle(Shape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f"Rectangle {self.__a},{self.__b},{self.__a},{self.__b}"

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def perimetr(self):
        return self.__a * 2 + self.__b * 2

    def area(self):
        return self.__a * self.__b

    def print_figure(self):
        [print("*" * self.__b) for _ in range(self.__a)]


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        return f"Triangle {self.__a},{self.__b},{self.__c}"

    @staticmethod
    def isosceles_triangle(a, b):
        res = (b / 2) * (((a + b / 2) * (a - b / 2)) ** 0.5)
        return res

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def perimetr(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimetr() / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def print_figure(self):
        k = 1
        for i in range(1, self.__b + 1):
            spaces = " " * (self.__a - k + i)
            k += int(i / self.__a) + i
            stars = "*" * (k - 1)  # (int(self.__a/i))
            # stars2 = "*"*(i-1)
            print(spaces + stars)


f1 = Square(3)
print(f1)
print(f1.area())
print(f1.perimetr())
f1.print_figure()

f2 = Rectangle(3, 7)
print(f2)
print(f2.area())
print(f2.perimetr())
f2.print_figure()

f3 = Triangle(11, 6, 6)
print(f3)
print(f3.area())
print(f3.perimetr())
f3.print_figure()

__author__ = "Arthur"
if __name__ == "__main__":
    print(f" Module {__name__}  author: {__author__}")



