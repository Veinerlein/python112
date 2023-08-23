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
