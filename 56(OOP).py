"""            MODULES                 """

import rect
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return f"Perimetr of {__class__.__name__} is {2 * (self.w + self.h)}"
#
#     def __repr__(self):  # Функція __repr__ повинна повертати рядок,
#         # який представляє об'єкт в текстовому вигляді, а не виводити щось на екран
#         return f"Rectangle({self.h},{self.w})"
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return f"Perimetr of {__class__.__name__} is {4 * self.a}"
#
#     def __repr__(self):
#         return "fd"
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return f"Perimetr of {__class__.__name__} is {self.a + self.b + self.c}"
#
#     def __repr__(self):
#         return 'dfs'


R1 = rect.Rectangle(1, 2)
R2 = rect.Rectangle(3, 4)
S1 = rect.Square(10)
S2 = rect.Square(20)
t1 = rect.Triangle(1, 2, 3)
t2 = rect.Triangle(4, 5, 6)

shape = [R1, R2, S2, S1, t2, t1]
for s in shape:
    print(repr(s))


"""
Можна імпортувати любий документ, любий пакет документів.
"""