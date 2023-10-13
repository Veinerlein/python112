"""            MODULES                 """

import rect
import geometry.RECT  # імпорт пакет.модуль
from les.shape import circle, rectangle, cylinder

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
"""
Створення пакету реалізується через стоврення папки, у якій буде пустий пітон файл __init__.py
"""

"""
import sys  -  задати в консоль, покаже усі варіанти де буде шукати інтерпретатор
конкретний модуль
sys.path
"""

from car import electrocar

e = electrocar.Electrocar("Tesla", "T", 2018, 99000)
e.show_car()
e.description_battery()

"""
пакет shape, в якому створеться ініт, в ініті клас ректангл.модуль сьоркл.модуль циліндер.модуль.
Клас циліндер наслідується від ректангла і Сьоркла. 

"""
#
# from shape.rectangle import Rectangle
# from shape.circle import Circle
# from shape.cylinder import Cylinder

from les.shape import rectangle
from shape import cylinder
from shape import circle

circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
circle_max_s = max(circles, key=lambda c: c.get_circle_square())
rect_min_p = min(rects, key=lambda r: r.get_rect_perimetr())
cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)
print("=" * 54)  # ================================================
print(circle_max_s)
print(rect_min_p.get_rect_perimetr())
print(cylinders_v)
print(cylinders_v_avg)
print(f"{cylinders_v_avg:.2f}")


