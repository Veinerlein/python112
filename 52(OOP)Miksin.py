"""    MIXINS    """
""" Змішування """


class Displayer:
    @staticmethod
    def display(message):
        print(message)


class LoggerMixin:
    def log(self, message, filename=None):
        if filename is None:
            filename = "Logfile.txt"
        with open(filename, "a") as fh:
            fh.write(message)

    def display(self, message, filename=""):
        Displayer.display(message)  # метод із попереднього класу для виводу рядка на екран
        self.log(message, filename)  # виклик метода із (НЕ) цього класу, але в селф попадає
        # екземпляр класу MySubClass бо я його
        # створив отак sub = MySubClass(). Якби екземпляр був sub1 = LoggerMixin, то селф був би екземпляр цього
        # класу і метод log() викликався б із цього класу (той що вище).
        # А так маємо бути уважні який екземпляр як створюється
        # У СЕЛФ ПОПАДАЄ ЕКЗЕМПЛЯР КЛАСУ, який ми створили  sub = MySubClass() і там є log
        # А тоді вже функція super().log(message) відпрацює на метод log, що вище, і запише рядок у файл


class MySubClass(LoggerMixin, Displayer):
    def log(self, message, filename=None):  # попаде повідомлення
        super().log(message, filename)  # в супер попадає батьківський клас  LoggerMixin,
        # месендж залишається таким є, а от ім'я файлу перезапишеться
        pass


sub = MySubClass()
sub.display("It is string with writing in to a file", filename="shos_nowe.txt")

print("+" * 78)  # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# тут 1 веріант
class MyGoods:
    def __init__(self, name, weight, price):
        print("Init of MyGoods class")
        self.name = name
        self.weight = weight
        self.price = price

    def myprint_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MyMixinLog:
    ID = 0

    def __init__(self):
        print("Init of MixinLog class")
        self.ID += 1
        self.id = self.ID

    def mysave_sell_log(self):
        # MyMixinLog.__init__(self)
        super().__init__()
        print(f'{self.ID}: the good was sold in 00:00 o`clock')


class MyLaptop(MyGoods, MyMixinLog):
    pass


myn = MyLaptop('HP', 1.5, 35000)
myn.myprint_info()
myn.mysave_sell_log()

print('=' * 67)  # ==========================================================


# тут 2-гий варіант
class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # код викличе спочатку ініт класу MixinLog, і тільки тоді вже відпрацюють методи цього
        # класу. по ієрархії цій [<class '__main__.Laptop'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>,
        # <class 'object'>]. Після Goods іде MixinLog
        print("Init of Goods class")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("Init of MixinLog class")
        MixinLog.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: the good was sold in 00:00 o`clock')


class Laptop(Goods, MixinLog):
    pass


n = Laptop('HP', 1.5, 35000)
n.print_info()
n.save_sell_log()
print(Laptop.mro())
n2 = Laptop('HP', 1.5, 35000)
n2.save_sell_log()

print('=' * 67)  # =========================================================================
print("""Перегрузка операторів""")

"""Перегрузка операторів"""


# ДОДАТИ ОПЕРАТОР ДО КЛАСУ
class Clock:
    __DAY = 86400  # число секунд в 1 день 24*60*60

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Sec has to be integer")

        self.__sec = sec

    def get_format_time(self):
        s = self.__sec % 60  # secunds
        m = (self.__sec // 60) % 60  # minuts
        h = (self.__sec // 3600) % 24  # hours
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):  # тепер клас має можливість додавати екземпляри
        if not isinstance(other, Clock):
            raise ArithmeticError("The right operand must be Clock type")
        return Clock(self.__sec + other.__sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(f"Wrong type in '{other}'")
        return Clock(self.__sec - other.__sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(f"Wrong type in '{other}'")
        return Clock(self.__sec * other.__sec)

    def __truediv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(f"Wrong type in '{other}'")
        return Clock(int(self.__sec / other.__sec))

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(f"Wrong type in '{other}'")
        return Clock(self.__sec // other.__sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError(f"Wrong type in '{other}'")
        return Clock(self.__sec % other.__sec)

    # перегрузити оператори рівності
    def __eq__(self, other):
        if self.__sec == other.__sec:
            return Clock(self.__sec == other.__sec)

    # def __ne__(self, other):
    #     if self.__sec != other.__sec:
    #         return Clock(self.__sec != self.__sec)

    # def __ne__(self, other):
    #     return not self.__eq__(other)
    def __ne__(self, other):
        return self.__sec != other.__sec

    def __lt__(self, other):
        return self.__sec < other.__sec

    def __le__(self, other):
        return self.__sec <= other.__sec

    def __gt__(self, other):
        return self.__sec > other.__sec

    def __ge__(self, other):
        return self.__sec >= other.__sec


c1 = Clock(200)
print(c1.get_format_time())
c2 = Clock(600)
print(c2.get_format_time())
c3 = c2 + c1  # тип даних немає оператора '+'
print(c3.get_format_time())
c4 = Clock(300)
c5 = c4 + c3 + c2 + c1
print(c5.get_format_time())

if c1 == c2:
    print("the time is equal")
if c1 != c2:
    print("the time is different")
if c2 < c4:
    print("c2<c4")
if c2 > c4:
    print('c2>c4')
print((c1 - c2).get_format_time())
print((c1 * c2).get_format_time())
print((c1 // c2).get_format_time())
print((c1 % c2).get_format_time())
print(((c1 - c2) * c2).get_format_time())
c1 += c2
print(c1.get_format_time())
print(dir(Clock))
