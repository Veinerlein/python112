"""inheritance   Nasliduvannia"""
"""Cтворення класу на основі уже існуючого класу"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, new_age):
        if new_age in range(1, 101):
            self.__age = new_age
        else:
            print("Wrong age")


p1 = Person("Kate", 30)
p1.print_info()
print(p1.__dict__)

print(p1.name)
print(p1._Person__age)


class Employee(Person):
    company = "Google"

    def more_info(self):
        print(f"Name: {self.name} works in {self.company}")


emp1 = Employee("Nick", 30)
emp1.print_info()
emp1.more_info()
print(issubclass(Employee, Person))  # True  працює тільки із класами
print(isinstance(emp1, Person))  # True  працює також із обєктами (знайшовся обєкт)
print(isinstance(emp1, Employee))  # True  працює також із обєктами (знайшовся обєкт)
print(issubclass(int, object))  # True
print("=" * 70)  # ==================================================


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


class Prop:
    __name = "Prop"

    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 4):
        print(f"Initializator for {self.__class__}")
        self.sp = sp
        self.ep = ep
        self.color = color
        self.__width = width
        self._name = self.__name

    def get_width(self):
        return self.__width


class Line(Prop):

    def __init__(self, *args):
        super().__init__(*args)
        # self.draw()

    def draw(self):
        print("Painting the line")


class Rect(Prop):  # потрібно викликати ініціалізатор базового класу через функ super()

    def __init__(self, *args):
        # Prop.__init__(self,*args) - нижче наведена краща версія коду, функціональність та сама,
        # але захищений (код) від зміни назви базового класу
        super().__init__(*args)  # через super() іде виклик обєкту ініціалізатора базового класу Prop.(ДЕЛЕГУВАННЯ)
        print("Initializator Rect")
        self.__width = 5

    def draw_line(self):
        print(f"DRoWING THE LINE: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")

    def draw_rect(self):
        print(f"we drowing : {self.sp}, {self.ep}, {self.color},")


line = Line(0, 0, 10)
r = Rect(1, 2, 3)
print(line.__dict__)
print(r.__dict__)
r.draw_rect()

"""Приватні атрибути не використовуються дочірніми класами. Тільки протектні"""

print(r._Prop__name)  # звернутись до загального атрибуту базового класу можна   Prop
print(r.__dict__)  # {'_sp': 1, '_ep': 2, '_color': 3, '_name': 'Prop', '_Rect__width': 4}

line1 = Line(Point(1, 2), Point(10, 20))
line1.draw()
p1 = Point(3, 5)
print(p1)  # без def __str__(self): виведе об'єкт <__main__.Point object at 0x000002A61ECD78B0>
# із def __str__(self):  виведе  3, 5

print("=" * 70)  # =======================================================


class Figure:
    def __init__(self, color):  # створений клас має загальний атрибут колір, шо є обов'язково присутнім у всіх
        # фігур, незалежно якої комплектації
        self.__color = color

    @property
    def color(self):  # геттер для зміни закритої змінної
        return self.__color

    @color.setter
    def color(self, new_color):  # сеттер для зміни закритої змінної
        self.__color = new_color


class Rectangle(Figure):  # клас прямокутник, як дитя від класу фігура
    def __init__(self, width, height, color, border):  # має свої параметри, а також
        # усі параметри батьківського класу і може переоприділяти їх, як от "color"
        super().__init__(color)  # конкретно цей параметр буде з аргументів відсилатись на ініціалізатор батьківського
        # класу
        self.__width = width
        self.__height = height
        self.border = border

    def chack_vallue(self, x, method_name):  # метод перевірки із 2 агрументами, де 1 - це змінюваний параметр,
        # а інший 2гий просто для самогенерації помилки у разі неправильного введення
        if x > 0:
            return x
        else:
            raise ValueError(f"Fool, a? {method_name} has to be more then 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = self.chack_vallue(new_width, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = self.chack_vallue(new_height, "height")

    def border_new(self):
        return self.border

    def area(self):
        # return self.color # ім'я геттера
        return self.width * self.height  # геттери і сеттери є службовими методами, тут назва геттера і сеттера вказана
        # return self.border_new()
    # Звертаючись до геттера чи сеттера можна не використовувати круглі дужки при виклику


re1 = Rectangle(3, 5, "red", "1px solid gray")
print(re1.__dict__)
re1.width = 1

re2 = Rectangle(10, 20, "green", "1px solid gray")
print(re2.area())
print(re2.width)  # отримую дані через геттер
print(re2.height)
print(re2.color)  # отримую, навіть з батьківського класу
print(re2.border)
re2.height = 3


class Time:
    """Class for work with time in format Hour:minute:Second"""
    number = 0
    time_zone: str = f"UTC{number}"
    import time

    def __init__(self, hour: str, minut: str, seconds: str):
        self.hour = hour
        self.minut = minut
        self.seconds = seconds
        self.print_info()

    def __del__(self):
        print("Момент часу видалений Delete Exempl " + self.__class__.__name__)

    def print_info(self):
        print(f"{Time.time_zone}\n{self.hour}\n{self.minut}\n{self.seconds}")

    @classmethod
    def time_zon(cls, znak: str, n: str):
        if znak == "+" or "-":
            cls.number = int(f"{znak}{n}")
        else:
            raise ValueError(f"{znak} has to be '+' or '-' in string format\n{n} has to be string format")

    @staticmethod
    def chack_v():
        pass

    @staticmethod
    def change_format():
        pass


class Liquid:  # створений клас рідина

    def __init__(self, name, density):
        self._name = name
        self._density = density  # густина

    def change_density(self, new_gust): # метод зміни густини
        self._density = new_gust

    def v_liquid(self, m):  # визначення об'єму від заданої маси
        ret = self._density/m
        print(f"Oб'єм {m} kg {self._name} становить {ret} m^3")
        return ret

    def m_liquid(self, v):  # визначення маси від заданого об'єму
        res = v* self._density
        print(f"Маса {v} m^3 {self._name} становить {res} kg")
        return res

    def print_info(self):
        print(f" рідина {self._name} густина = {self._density} kg/m^3")


class Alcohol(Liquid):

    def __init__(self, name, density, promile):
        super().__init__(name, density)
        self.promile = promile

    def change_promile(self, new_promile):
        self.promile = new_promile


liq1 = Liquid("Wine", 1064.2)
liq2 = Liquid("Wine", 1000)
n = Liquid("name", 18)
print(n._name)
liq1.print_info()
liq2.print_info()
liq1.change_density(1000)
liq1.m_liquid(0.5)
liq1.v_liquid(300)

a1 = Alcohol("Wine", 1064.2, 14)
print(a1.promile)
a1.change_promile(20)
print(a1.promile)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def is_digit(self):
        if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
            return True
        else:
            return False

    def is_int(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            return True
        else:
            return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Coordinates have to be numbers")


class Line(Prop):
    def drow_line(self):
        print(f"Малювання лінії: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def set_coords(self, sp: Point, ep: Point):  # якщо закоментувати чи видалити, то знайде аналогічний у
        # батьківському класі і буде працювати по ньому
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep
        else:
            print("Coordinates have to be numbers")


line = Line(Point(1, 2), Point(10, 20))
line.drow_line()
line.set_coords(Point(30.6, 40), Point(100, 200))
line.drow_line()


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_rect(self):
        print(f"Rectangle:\nWidth: {self.width}\nHeight: {self.height}")


class RectFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()  # додасть прінт із show_rect() методу із батьківського класу
        print(f"Ramka: {self.fon}")


class RectBorder(Rect):
    def __init__(self, width, height, border):
        super().__init__(width, height)
        self.border = border

    def show_rect(self):
        super().show_rect()  # додасть прінт із show_rect() методу із батьківського класу
        print(f"Bort: {self.border}")


shape1 = RectFon(400, 200, "yellow")
shape1.show_rect()
shape2 = RectBorder(600, 300, "1px solid red")
shape2.show_rect()


class Liquid:  # створений клас рідина

    def __init__(self, name, density):
        self.__name = name
        self.__density = density  # густина

    def change_density(self, new_gust):
        self.__density = new_gust

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def density(self):
        return self.__name

    @density.setter
    def density(self, density):
        self.__density = density

    def v_liquid(self, m):  # визначення об'єму від заданої маси
        ret = m / self.__density
        print(f"Oб'єм {m} kg {self.name} становить {ret} m^3")
        # f"Об'ємне відношення спирту {}")
        return ret

    def m_liquid(self, v):  # визначення маси від заданого об'єму
        res = v * self.__density
        print(f"Маса {v} m^3 {self.name} становить {res} kg")
        # f"Масовий вміст спирту: {}")
        return res

    def print_info(self):
        print(f" рідина {self.__name} густина = {self.__density} kg/m^3\n", end=" ")


class Alcohol(Liquid):

    def __init__(self, name, density, promile):
        super().__init__(name, density)
        self.promile = promile

    def change_promile(self, new_promile):
        self.promile = new_promile

    def m_liquid(self, v):  # визначення маси від заданого об'єму
        m = super().m_liquid(v)
        m_alc = v * self.promile
        print(f"Маса {v} m^3 {self.name} становить {m_alc} kg")
        return m, m_alc

    def v_liquid(self, m):  # ПЕРЕвизначення об'єму від заданої маси
        # ret = m / self._density
        # print(f"Oб'єм {m} kg {self._name} становить {ret} m^3\n"
        #       f"Об'ємне відношення спирту {}")
        # return ret
        v = super().v_liquid(m)
        v_alc = v * self.promile
        print(f"Об'єм алкоголю в {m}kg {self.name} становить {v_alc} m^3")
        return v, v_alc

    def print_info(self):
        # print(f" рідина {self._name} густина = {self._density} kg/m^3")
        super().print_info()
        print(f"міцність =  {self.promile}:.0%")


liq1 = Liquid("Wine", 1064.2)
liq2 = Liquid("Wine", 1000)
n = Liquid("name", 18)
print(n.name)
liq1.print_info()
liq2.print_info()
liq1.change_density(1000)
liq1.m_liquid(0.5)
liq1.v_liquid(300)
print("3" * 67)
a1 = Alcohol("Wine", 1064.2, 14)
a1.change_density(1000)
a1.v_liquid(300)
a1.m_liquid(0.5)
print(a1.promile)
a1.change_promile(20)
print(a1.promile)
a1.print_info()

"""Усі типи даних це класи"""


class Vector(list):  # провів наслідування від базового класу list
    def __str__(self):
        return " ".join(map(str, self))  # метод буде конвертувати через селф кожен об'єкт, який буде створений через
        # клас Vector у строку із пробілами між даними. Ну а вхідні дані будуть завжди списком.


v = Vector([1, 23, 45])  # 1 23 45
v1 = Vector(["1", "23", 45])  # 1 23 45
# v2 = Vector(12345) # TypeError: 'int' object is not iterable
print(v)
print(v1)
# print(v2)
print(type(v))  # <class '__main__.Vector'>
