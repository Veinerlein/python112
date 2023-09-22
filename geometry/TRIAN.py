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
            spaces = " " * (self.__a - (k + i))
            k += int(i / self.__a) + i
            stars = "*" * (self.__a)  # (int(self.__a/i))
            # stars2 = "*"*(i-1)
            print(spaces + stars)


class Trian:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


t= Triangle(11,6,6)
t.print_figure()