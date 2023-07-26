import re


class UserDate:
    def __init__(self, pib, age, ps, weight):
        self.verify(pib)
        self.verify_age(age)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__pib = pib.split()
        self.__age = age
        self.__password = ps
        self.__weight = weight

    @classmethod
    def verify(cls, pib):
        if not isinstance(pib, str):  # якщо не строка то зайдем в цей блок і закінчимо помилкою
            raise TypeError("ПІБ має бути строкою")
        f = pib.split()  # поверне масив з трьох елементів ПІБ
        print(f)
        if len(f) != 3:  # перевірка масиву
            raise TypeError("Невірний формат")

        letters = "".join(re.findall(r"[a-zа-я-]", pib, flags=re.IGNORECASE))  # ПрізвищеІм'яПобатькові
        print(letters)
        for s in f:
            if len(s.strip(letters)) != 0:  # стріп видалить усі букви, які вказані в круглих дужках, за наявністю
                # 1 цифри  довжина стане 1, і тоді ми зайдемо у цей блок де буде ловитись помилка
                raise TypeError("В ПІБ можна використовувати тільки букви або дефіси")

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age < 14 or age > 100:
            raise TypeError('Тип даних віку повинен бути числом в діапазоні від 14 до 100')

    @classmethod
    def verify_weight(cls, w):
        if not isinstance(w, (int, float) or w < 40):
            raise TypeError("Вага повинна бути числом та від 40 кг")

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспортні дані повинні бути строковим значенням")
        s = ps.split()
        print(s)
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Не вірний формат паспортних даних')  # райз закриє виконання так само як ретурн

    @property
    def get_pib(self):
        return self.__pib

    @get_pib.setter
    def get_pib(self, x):
        self.verify(x)
        self.__pib = x

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, x):
        self.verify_age(x)
        self.__age = x

    @property
    def get_weight(self):
        return self.__weight

    @get_weight.setter
    def get_weight(self, x):
        self.verify_weight(x)
        self.__weight = x

    @property
    def get_ps(self):
        return self.__password

    @get_ps.setter
    def get_ps(self, x):
        self.verify_ps(x)
        self.__password = x


p1 = UserDate("Заплет Денис Миколайович", 26, "1234 567890", 80.8)
p1.get_pib = "Баран Тарас Брозович"
print(p1.get_pib)
p1.get_ps = "2390 123097"
print(p1.get_ps)
p1.get_age = 35
print(p1.__dict__)

# {'_UserDate__pib': 'Баран Тарас Брозович', 'age': 26,
#               'password': '1234 567890', 'weight': 80.8, '_UserDate__password': '2390 123097',
#                                                                           '_UserDate__age': 35}

"""геттери і сеттери переписують змінні які є публічними на свій лад, але тільки у випадку 
конфронтації імен. Це коли ми називаємо геттер і сеттер ім'ям змінної. Якщо назвати різними іме-
нами так, як це зробив я, то ніякої конфронтації не виникає і метод __dict__ покаже утворення
нових закритих змінних, які утворить сеттер і геттер. Це буде на додачу до старих змінних які 
публічні. Тому у мене і утворились нові змінні в запутку програми (коли було закоментовано
веріфікацію та змінено приватні атрибути в ініціалізаторі на публічні. )(Зараз усе відредаговано до 
первісного вигляду)"""
