"""Incapsulating"""
import math

"""ПРиховування якихось данних, щоб неможливо було отримати доступ ззовні без спец запитів
Об'єднує властивості та методи і приховує реалізацію від користувача"""


class Point:
    WIDTH = 5
    __slots__ = ["__x", "__y"]  # Вказую властивості які можуть використовуватись у даному класі.

    # Виділяє менше памяті

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Point.__check_type(x) and Point.__check_type(y):
            self.__x = x
            self.__y = y
        else:
            print("Coords should be integer or float")

    # def set_x(self, x):
    #     self.__x = x
    #
    # def get_x(self):
    #     return self.__x

    def __check_type(z):  # закритий метод
        if isinstance(z, int) or isinstance(z, float):
            return True
        else:
            return False

    def set_coords(self, x, y):
        if Point.__check_type(x) and Point.__check_type(y):  # Перенести в
            # окремий метод, щоб не дублювати постійно цей код перевірки
            self.__x = x
            self.__y = y
        else:
            print("Coords should be integer or float")

    """пропишу новий сет курдз зверху"""

    # def set_coords(self, x, y):
    #     if (isinstance(x, int)) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):  # Перенести в
    #         # окремий метод, щоб не дублювати постійно цей код перевірки
    #         self.__x = x
    #         self.__y = y
    #     else:
    #         print("Coords should be integer")

    def get_coords(self):
        return self.__x, self.__y

    def __getattr__(self, item):  # метод пошуку універсального атрибуту
        return f"In the class {__class__.__name__} відсутній атрибут: {item}"  # викликається,
        # коли код намагається отримати доступ до якогось неіснуючого атрибуту. Можна прописати виключення,
        # що і прописав

    def __getattribute__(self, item):  # метод getattribute закрив доступ до змінних через конструкцію _Point__x
        if item == "_Point__x":
            return "Закрита змінна"
        else:
            return object.__getattribute__(self, item)

    # def __setattr__(self, key, value):  # захист константи і створення свого користувацького виключення
    #     if key == "WIDTH":
    #         raise AttributeError("Not allowed to change WIDTH")
    #     else:
    #         self.__dict__[key] = value


p1 = Point(5, 10)  # свого роду p1 має тип данних Point, данних, які я програмую сам.
# print(p1.x, p1.y)  # 5 10          p1 це self |  . це .  |  x це x  (p1.x  ==  self.x)
# print(p1.__x, p1.__y)
# p1.x = 100
# print(p1.x, p1.y)  # 100 10
#
# p1.y = "abc"
print(p1.x, p1.y)  # 100 abc

"""код не працюватиме, якщо не закоментувати print(p1.x, p1.y) або print(p1.x, p1.y) або print(p1.__x, p1.__y)
 Але буде працювати після того, як я вручну зміню кожне значення для кожного атрибуту"""
print(p1.__dict__)  # {'_Point__x': 5, '_Point__y': 10, 'x': 100, 'y': 'abc'}
"""У дікт видно що я створив нові 'х' та 'у' після дії  p1.x = 100 та p1.y = 'abc' """
# p1.__x = 112  # так заплутуєшся, передавати дані треба через геттер чи сеттер
# p1.__y = "ZYX"
print(p1.__dict__)  # {'_Point__x': 5, '_Point__y': 10, 'x': 100, 'y': 'abc', '__x': 112, '__y': 'ZYX'}
"""абсолютно нові перемінні такі ж як х чи у: __x   __y  утворені через p1.__x = 112
p1.__y = "ZYX". АЛе до класу вони не моють відношення. Додалась за межами класу"""

"""геттер та сеттер для доступу до змінних"""

# p1.set_x(222)
# print(p1.get_x())
print(p1.__dict__)
"""Доступ отримав за рахунок того, що вказав геттер і сеттер, де через ретюрн вивів self.__x у Геттері, або
 через аргументи методу встановив у сеттері"""

p1.set_coords(50.50, 70.70)
print(p1.get_coords())  # (50, 70)
print(p1.__dict__)  # {'_Point__x': 50, '_Point__y': 70, 'x': 100, 'y': 'abc', '__x': 112, '__y': 'ZYX'}

p1.set_coords(32, "STR")  # Coords should be integer
"""За рахунок обмеження через умови у сеттері"""
print(p1.get_coords())

p1 = Point("5", 10)  # ХОЧА і ЗАБОРОНИВ МЕТОДОМ  __check_type(z) змінювати, заборона на введення відсутня
print(p1.__dict__)  # {'_Point__x': 0, '_Point__y': 0}

""" Це вирішується зміною в самому ініціалізаторі де я вставновлюю 0 для кожного значення по замовчуванню, 
а на початкове введення даних встановлюю перевірки типу"""

p1 = Point(5, 10)
print(p1.__dict__)  # {'_Point__x': 5, '_Point__y': 10}

"""Таким чином відбувається захист на введення данних"""

print(p1._Point__x)  # звернення напряму в пам'ять імені, яке знаходиться всередині класу
# p1._Point__x = 90000
print(p1.__dict__)

p2 = Point(5, 10)
print(p2.zzz)
print(p2.__dict__)  # {'_Point__x': 5, '_Point__y': 10}
print(p2._Point__x)  # через мігічний метод getattribute закрив доступ до змінних через конструкцію _Point__x
# при цьому можна встановити через сеттер, але переглянути через геттер чи сеттер не вийде
print(p2.get_coords())
print(p2.set_coords(45, 20))
print(p2.__dict__)  # {'_Point__x': 45, '_Point__y': 20}


# p2.WIDTH = 7 #   File "E:\pythonProject1\les\47(OOP incap).py", line 62, in __setattr__
#     raise AttributeError("Not allowed to change WIDTH")
# AttributeError: Do not alowed to change WIDTH


class Rectangle:

    def __init__(self, a, b):
        self.a = self.b = 2
        if Rectangle.__check_type(a) and Rectangle.__check_type(b):
            self.a = a
            self.b = b
        else:
            print("Should be integer or float.!\n(Using default data 2)")

    def set_side(self, a, b):
        if Rectangle.__check_type(a) and Rectangle.__check_type(b):
            self.a = a
            self.b = b
        else:
            print("Should be integer or float")

    def get_side(self):
        return self.a, self.b

    def __check_type(side):
        if isinstance(side, int) or isinstance(side, float):
            return True
        return False

    def square(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b) * 2
        # return self.square() * 2

    def gipotenuz(self):
        return round((self.a ** 2 + self.b ** 2) ** (1 / 2), 2)

    def info_rectangle(self):
        return (f"Довжина прямокутника:{self.a}\nШирина прямокутника:{self.b}\nПлоща прямокутника"
                f":{self.square()}\nПериметр "
                f"прямокутника"
                f":{self.perimetr()}\nГіпотенуза прямокутника:{self.gipotenuz()}")

    def print_rectangle(self):
        # for i in range(len("*"*self.b)):
        #     print('*'*self.a)
        [print('*' * self.a) for i in range(len("*" * self.b))]


rec1 = Rectangle(3, 9)

print(rec1.info_rectangle())
rec1.print_rectangle()


class RectAngle:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if RectAngle.__chack_value(x) and RectAngle.__chack_value(y):
            self.__x = x
            self.__y = y

    def __chack_value(z):
        if isinstance(z, (int, float)):
            return True
        return False

    def set_x(self, x):
        if RectAngle.__chack_value(x):
            self.__x = x

    def set_y(self, y):
        if RectAngle.__chack_value(y):
            self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_area(self):
        return self.__y * self.__x

    def get_perim(self):
        return 2 * (self.__x + self.__y)

    def gipot(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def print_area(self):
        # for i in range(self.__x):
        #     print("*"*self.__y)
        print(("*" * self.__y + "\n") * self.__x)


r1 = RectAngle(3, 9)
# a = int(input("Hight"))
# b = int(input("With"))
# r1.set_y(b)
# r1.set_x(a)
print(r1.get_x(), r1.get_y())
print(r1.get_area())
print(r1.get_perim())
print(round(r1.gipot(), 2))
r1.print_area()


class Pointer:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __set_x(self, x):
        print("Setter")
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("Wrong format of data")

    def __get_x(self):
        print("Getter")
        return self.__x

    def __del_x(self):
        print("ВИдалення властивості")
        del self.__x

    coordzX = property(__get_x, __set_x, __del_x)  # дозволить перезаписувати через закриті методи __set_x,
    # та __get_x автоматично
    # використовуючи coordzX


p1 = Pointer(5, 10)
p1.__set_x = 100
print(p1.__dict__)  # {'_Pointer__x': 5, '_Pointer__y': 10, '__set_x': 100}

p2 = Pointer(5, 10)
# p2.coordzX = "100" # ValueError: Wrong format of data
p2.coordzX = 100
print(p2.coordzX)
print(p2.__dict__)  # {'_Pointer__x': 100, '_Pointer__y': 10}

del p2.coordzX  # спрацює якщо викликати через дел і тільки, якщо у coordz передані параметри вірні


# Що стосується   property(__get_x, __set_x, __del_x)
# del спрацює тільки якщо викликати видалення через coordzX
# setter спрацює тільки, якщо встановлювати через coordzX
# getter спрацює тільки, якщо запрошувати через coordzX


class Ruta:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # наступна комбінація видозмінена по відношенню до попередньої
    # через додання @property, @coordzX.setter, @coordzX.deleter.
    # Ім'я всіх методів названо одинаково

    @property  # завжди біля геттера і завжди перший
    def x(self):
        print("Getter")
        return self.__x

    @x.setter
    def x(self, x):
        print("Setter")
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("Wrong format of data")

    @x.deleter
    def x(self):
        print("ВИдалення властивості")
        del self.__x

    # coordzX = property(__get_x, __set_x, __del_x)  # дозволить перезаписувати через закриті методи __set_x,
    # та __get_x автоматично
    # використовуючи coordzX


p1 = Ruta(5, 10)
p1.__set_x = 100
print(p1.__dict__)  # {'_Pointer__x': 5, '_Pointer__y': 10, '__set_x': 100}

p2 = Ruta(5, 10)
# p2.x = "100" # ValueError: Wrong format of data
p2.x = 100  # '_Ruta__x': 100  - ЗВЕРНЕННЯ ПІДЕ НЕ ДО ЗМІННОЇ (ЇЇ НЕМАЄ, А ДО СЕТТЕРА, ЩО ВИЩЕ ІЗ @ПРОПИСАНИЙ)
print(p2.x)
print(p2.__dict__)  # {'_Ruta__x': 100, '_Ruta__y': 10}


class Personal:

    def __init__(self, name, age, high):
        self.__name = name
        self.__age = age
        self.__high = high

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    # тепер для age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, high):
        self.__high = high

    @high.deleter
    def high(self):
        del self.__high


one = Personal('Iren', 25, 173)

print(one.name)
print(one.age)

one.name = "Hidalgo"
print(one.__dict__)  # {'_Personal__name': 'Hidalgo', '_Personal__age': 25}

print(one.name)  # Hidalgo

del one.name
print(one.__dict__)  # {'_Personal__age': 25}


class Convertation:

    def __init__(self, weight):
        try:
            weight = float(weight)
            if isinstance(weight, (int, float)):
                self.__weight = weight
            else:
                print("Weight value should be int or float1")
        except:
            print("Weight value should be int or float2")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        try:
            new_weight = float(new_weight)
            if isinstance(new_weight, (int, float)):
                self.__weight = new_weight
            else:
                print("Weight value should be int or float1!")
        except:
            print("Weight value should be int or float2!")

    @weight.deleter
    def weight(self):
        del self.__weight

    def to_pounts(self):
        print(self.weight, "KG =>", self.__weight * 2.205, "pounts")


box1 = Convertation(12)
print(box1.__dict__)
box1.weight = 41
print(box1.weight)
print(box1.__dict__)
box1.weight = "123"

box2 = Convertation("123.4")
print(box2.__dict__)
box2.weight = "34"
print(box2.weight)

box1.to_pounts()
box2.to_pounts()


class Cats:
    """This class represents a cat"""
    slts = ["name", "age", "type_of_cat", "high", "weight", 'color', 'claws', 'food', "ayes", "vaccination"]

    def __init__(self, name, age, type_of_cat, high, weight, color, claws, food, ayes, vaccination):
        self.__name = name
        self.__age = age
        self.__type_of_cat = type_of_cat
        self.__high = high
        self.__weight = weight
        self.__color = color
        self.__claws = claws
        self.__food = food
        self.__ayes = ayes
        self.__vaccination = vaccination

    # name________________________________________________________
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print(name, "Inserted")
        self.__name = name

    @name.deleter
    def name(self):
        print(self.__name, "Deleted")
        del self.__name

    # age________________________________________________________
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    # type   ________________________________________________________
    @property
    def type_of_cat(self):
        return self.__type_of_cat

    @type_of_cat.setter
    def type_of_cat(self, type_of_cat):
        self.__type_of_cat = type_of_cat

    @type_of_cat.deleter
    def type_of_cat(self):
        del self.__type_of_cat

    # high________________________________________________________
    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, high):
        self.__high = high

    @high.deleter
    def high(self):
        del self.__high

    # weight________________________________________________________
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @weight.deleter
    def weight(self):
        del self.__weight

    # color________________________________________________________
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @color.deleter
    def color(self):
        del self.__color

    # claws________________________________________________________
    @property
    def claws(self):
        return self.__claws

    @claws.setter
    def claws(self, claws):
        self.__claws = claws

    @claws.deleter
    def claws(self):
        del self.__claws

    # food________________________________________________________
    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    @food.deleter
    def food(self):
        del self.__food

    # ayes________________________________________________________
    @property
    def ayes(self):
        return self.__ayes

    @ayes.setter
    def ayes(self, ayes):
        self.__ayes = ayes

    @ayes.deleter
    def ayes(self):
        del self.__ayes

    # vaccination________________________________________________________
    @property
    def vaccination(self):
        return self.__vaccination

    @vaccination.setter
    def vaccination(self, vaccination):
        self.__vaccination = vaccination

    @vaccination.deleter
    def vaccination(self):
        del self.__vaccination

    def print_Information(self):
        # d = dict(zip(self.slts, [getattr(self, f"_{self.__class__.__name__}{attr}") for attr in self.slts])) #
        # Варіант якщо є __slots__
        d = dict(zip(self.slts, [getattr(self, f"_Cats__{attr}") for attr in self.slts])) # варіант із звичайним
        # списком (ІМЕНА ЗМІННИХ ПОВИННІ ЗБІГАТИСЬ ІЗ ІМЕНАМИ ВІДПОВІДНИХ SELF-ЗМІННИХ)
        [print(f"{k} : {v}") for k, v in d.items()]
        print('='*40)
        {print(k,":",v) for k,v in d.items()}
        print()
        [print(k,":",v) for k,v in self.__dict__.items()]



    def print_info(self):
        print(f"Hello my name is {self.__name}. I am {self.__age} years old.\n"
              f"My breed is {self.type_of_cat} and I don`t know what does it mean.\n"
              f"My high is {self.__high} centimetres, weight is {self.__weight} kg and colour is {self.__color}.\n"
              f"I have to take care about my {self.__claws} claws. It is usefull.\n"
              f"Especially when I hunt or get my {self.__food}.\n"
              f"I've got {self.__ayes} ayes color and it is the reason to be proud by me.\n"
              f"But I never forget my vaccination day, when I've got my {self.__vaccination} vaccination.\n"
              f"o-hhhhh......")


cat1 = Cats("Alita", 1, "'European shorthear'", 30, 4.5, "gray-white and black", "sharp", "Brit pet-food",
            'light green', "100%")

print(cat1.name)
cat1.print_info()
cat1.print_Information()
