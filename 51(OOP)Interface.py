from abc import ABC, abstractmethod


class Currency(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def change(self, x: str, x_currency: float = 37.7):
        raise NotImplementedError("'str' object has no attribute 'change'")


class Dollar(Currency):

    def __init__(self, value):
        super().__init__(value)

    def print_info(self):
        print(self.value)

    def change(self, x: str = "USD", x_currency: float = 37.7):
        res = self.value * x_currency
        print(f"{self.value} {x} = {res:.2f} UAH")
        return res


class Euro(Currency):

    def __init__(self, value):
        super().__init__(value)

    def print_info(self):
        print(self.value)

    def change(self, x: str = "EUR", x_currency: float = 39.7):
        res = self.value * x_currency
        print(f"{self.value} {x} = {res:.2f} UAH")
        return res


curr1 = Dollar(5)
curr2 = Dollar(10)
curr3 = Dollar(50)
curr4 = Dollar(100)

curr5 = Euro(5)
curr6 = Euro(10)
curr7 = Euro(50)
curr8 = Euro(100)

currency = list()
[currency.append(x) for x in [curr1, curr2, curr3, curr4, f'{"*" * 78}', curr5, curr6, curr7, curr8]]

for cur in currency:
    try:
        cur.change()
    except:
        print(f'{"*" * 78}')


# """Tech Decision"""

class CurrEncy(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def convert_uah(self):
        pass

    def print_value(self):
        print(self.value, end="")


class Dollars(CurrEncy):
    rate_to_uah = 37.7
    suffix = "USD"

    def convert_uah(self):
        uah = self.value * Dollars.rate_to_uah
        return uah

    def print_value(self):
        super().print_value()
        print(Dollars.suffix, end=" ")


class EUR(CurrEncy):
    rate_to_uah = 39.7
    suffix = "EUR"

    def convert_uah(self):
        uah = self.value * EUR.rate_to_uah
        return uah

    def print_value(self):
        super().print_value()
        print(EUR.suffix, end=" ")


d = [Dollars(5), Dollars(10), Dollars(50), Dollars(100)]
e = [EUR(5), EUR(10), EUR(50), EUR(100)]
print("*" * 50)
for elem in d:
    elem.print_value()
    print(f"= {elem.convert_uah():.2f} UAH")
print("*" * 50)
for elem in e:
    elem.print_value()
    print(f"= {elem.convert_uah():.2f} UAH")

print("*" * 78)  # **************************************************

""" INTERFACE - абстрактний клас, у якого жоден метод не реалізований, шаблон, де всі дочірні класи матимуть 
абстрактні методи"""

from abc import ABC, abstractmethod


class IFather(ABC):
    @abstractmethod
    def display1(self):
        pass

    @abstractmethod
    def display2(self):
        pass


class Child(IFather):
    def display1(self):
        print("Child class")
        print("Display 1 Abstract Method")


class GrandChild(Child):
    def display2(self):
        print("Child class")
        print("Display 2 Abstract Method")


gc = GrandChild()
gc.display2()
gc.display1()

print("=" * 67)  # =====================================================


class MyOuter:
    age = 18

    def __init__(self, name):
        self.name = name

    @classmethod
    def outer_class_method(cls):
        print("Out class Method")

    def outer_obj_method(self):
        print("Connection method with outer class object")

    class MyInner:
        def __init__(self, inner_name, obj):
            self.inner_name = inner_name
            self.obj = obj

        def inner_method(self):
            print("Inside class method")
            MyOuter.outer_class_method()
            self.obj.outer_obj_method()
            print(self.obj.name)


out = MyOuter("OUTER")
inner = out.MyInner("INNER", out)
# print(inner.inner_name) # INNER

""" ДО ВКЛАДЕНОГО КЛАСУ ЗВЕРТАЄМОСЬ ЧЕРЕЗ ЕКЗЕМПЛЯР БАТЬКІВСЬКОГО КЛАСУ """

inner.inner_method()

print("=" * 87)  # =============================================


class Employee:
    def __init__(self):
        self.name = "Employee"
        self.intern = self.Intern()  # цілий клас є екземпляром, у атрибут класу Employee попадає
        # цілий ініт класу Intern
        self.head = self.Head()  # а тут екземпляр класу Head
        # Можна використовувати методи відповідних класів

    def show(self):
        print("Employee list")
        print("Name:", self.name)

    class Intern:
        def __init__(self):
            self.name = "Smith"
            self.id = "657"

        def display(self):
            print("name:", self.name)
            print("Degree:", self.id)

    class Head:

        def __init__(self):
            self.name = "Alan"
            self.id = "570"

        def display(self):
            print("name:", self.name)
            print("Degree:", self.id)


outer = Employee()
outer.show()

d1 = outer.intern
d2 = outer.head
d1.display()
d2.display()

print("+" * 87)  # =============================================================


class Geeksforgeeks:
    def __init__(self):
        self.inner = self.Inner()  # inner1 = outer.Inner() замість цієї буде ця outer.inner

    def show(self):
        print("This is OuTER class")

    class Inner:

        def __init__(self):
            self.inner_inner = self.InnerClass()

        def show(self):
            print("inside class")

        class InnerClass:
            def show(self):
                print("This is an inner class of inner class")


outer = Geeksforgeeks()
outer.show()

inner1 = outer.inner
inner1.show()

inner_inner1 = inner1.inner_inner
inner_inner1.show()
print("new:", end=" ")
sample = Geeksforgeeks().inner.inner_inner
sample.show()


class Computer:
    def __init__(self):
        self.name = "PC001"
        self.os = self.OS()
        self.cpu = self.CPU()

    class OS:
        def system(self):
            return "Windows 10"

    class CPU:
        def make(self):
            return "Intel"

        def model(self):
            return "Core-i7"


computer = Computer()
my_os = computer.os  # також можна через computer.OS()
my_cpu = computer.cpu

print(computer.name)  # PC001
print(my_os.system())  # Windows 10
print(my_cpu.make())  # Intel
print(my_cpu.model())  # Core-i7

print("*" * 10, "внизу такі самі дані", "*" * 10, sep="\n")

print(Computer().name)  # PC001
print(Computer().OS().system())  # Windows 10
print(Computer().CPU().make())  # Intel
print(Computer().CPU().model())  # Core-i7

print("=" * 60)  # =============================================================


class Base:
    def __init__(self):
        self.db = self.Inner1()

    def display(self):
        print("In Base class")

    class Inner1:
        def display1(self):
            print("Inner_of_Base class")


class SubClass(Base):
    def __init__(self):
        print("In SubClass")
        super().__init__()  # отримав доступ до ініт в батьківському класі     def __init__(self):
        # self.db = self.Inner()

    class Inner2(Base.Inner1):
        def display2(self):
            print("Inner  of SubClass")


a = SubClass()  # In SubClass
a.display()  # In Base class

b = a.db
b.display1()  # Inner_of_Base class
# b.display2() # Якби Inner1 та Inner2 називались одинаково, то метод display2 можна
# було б викликати через атрибут db
c = SubClass.Inner2()  # у цьому варіанті обидва методи працюватимуть
c.display1()
c.display2()


class Student:
    def __init__(self, name="Rembrandt", n=None):
        if n is None:
            n = self.Laptop()
        self.name = name
        self.db = n
        # self.print_name()

    def print_name(self):
        print(self.name, "=>", end=" ")
        self.db.print_info()

    class Laptop:
        def __init__(self, model="MSI Game turbo BRAVO 17 Black", cpu="Ryzen 7 3600x", ram="8 GB "):
            self.model = model
            self.cpu = cpu
            self.memory = ram

        def print_info(self):
            print(self.model, self.memory, self.cpu)


s1 = Student()
s1.Laptop().print_info()  # MSI Game turbo BRAVO 17 Black 8 GB  Ryzen 7 3600x
s1.print_name()

s2 = Student()
s2.print_name()
s2 = s2.db
s2.print_info()  # MSI Game turbo BRAVO 17 Black 8 GB  Ryzen 7 3600x
s1.db.print_info()  # MSI Game turbo BRAVO 17 Black 8 GB  Ryzen 7 3600x

s3 = Student.Laptop("Brand", "i7", "16")
s3 = Student("Vlad", s3)
s4 = Student("Ann", Student.Laptop("HP", "i9", "32"))


class Creature:
    def __init__(self, name):
        self.name = name


class Animal(Creature):
    def sleep(self):
        print(self.name + " is sleeping")


class Pet(Creature):
    def play(self):
        print(self.name + " is playing")


class Dog(Animal, Pet):
    def bark(self):
        print(self.name + " is barking")


d = Dog("Buddy")
d.bark()
d.play()
d.sleep()
print(Dog.mro())

print("=" * 89)  # =========================================================


class A(object):
    # def __init__(self):
    #     print("Initializator class A")
    # def hi(self):
    #     print("A")
    pass


class AA(object):
    # def __init__(self):
    #     print("Initializator class A")
    # def hi(self):
    #     print("A")
    pass


class B(A):
    # def __init__(self):
    #     print("Initializator class B")
    # def hi(self):
    #     print("B")
    pass


class C(AA):
    # def __init__(self):
    #     print("Initializator class C")
    pass
    # def hi(self):
    #     print("C")


class D(B, C):
    # def __init__(self):
    #     print("Initializator class D")

    pass


d = D()
# d.hi()
print(D.mro())  # метод .mro() покаже порядок пошуку методів чи ініціалізаторів


# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):  # дозволяє вивести дані а не main.object
        # Painting the line: <__main__.Point object at 0x0000023C12B36C50>, <__main__.Point object at 0x0000023C12B360E0>,
        # green, 5

        return f"({self.x}, {self.y})"  # Painting the line: (10, 10), (100, 100), green, 5


class Styles:
    def __init__(self, color="red", width=1):
        print("Initializator Styles")
        self._color = color
        self._width = width


class Position:
    def __init__(self, sp: Point, ep: Point, *args):
        print("Initializator Position")
        self._sp = sp
        self._ep = ep
        # Styles.__init__(self,*args)
        super().__init__(*args)


class Line(Position, Styles):
    def draw(self):
        print(f"Painting the line: {self._sp}, {self._ep}, {self._color}, {self._width}")


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)

l1.draw()


class StudenT:
    def __init__(self, name):
        self.name = name
        self.note = self.Laptop()

    def show(self):
        print(self.name)
        self.note.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print(f"{self.brand},{self.cpu},{self.ram}")


st1 = StudenT("Roman")
st2 = StudenT("Vladislav")

st1.show()
st2.show()

