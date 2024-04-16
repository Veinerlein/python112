class Point:
    WIDTH = 5
    __slots__ = ["__x", "__y"]   # Вказую властивості які можуть використовуватись у даному класі.
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
        return f"In the class {__class__.__name__} відсутній атрибут: {item}"  # Відтворив

    def __getattribute__(self, item):  # метод getattribute закрив доступ до змінних через конструкцію _Point__x
        if item == "_Point__x":
            return "Закрита змінна"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # захист константи і створення свого користувацького виключення
        if key == "WIDTH":
            raise AttributeError("Do not alowed to change WIDTH")
        else:
            self.__dict__[key] = value


p1 = Point(5, 10)  # свого роду p1 має тип данних Point, данних, які я програмую сам.
# print(p1.x, p1.y)  # 5 10          p1 це self |  . це .  |  x це x  (p1.x  ==  self.x)
# print(p1.__x, p1.__y)
# p1.x = 100
# print(p1.x, p1.y)  # 100 10

# p1.y = "abc"
print(p1.x, p1.y)  # 100 abc


