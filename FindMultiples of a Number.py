"""
In this simple exercise, you will build a program that takes a value, integer ,
 and returns a list of its multiples up to another value, limit . If limit is a
 multiple of integer, it should be included as well.
 There will only ever be positive integers passed into the function, not consisting of 0.
 The limit will always be higher than the base.

For example, if the parameters passed are (2, 6), the function should return
 [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
"""


def multiples(x, y):
    l = range(x, y + 1)
    limit = []
    for number in l:
        if number % x == 0:
            limit.append(number)
    return limit


def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))

print(find_multiples(9,100))

print(multiples(2, 6))
print(10 % 4)

"""
Кратність (термін) — це властивість числа, яка перевіряється діленням без 
остачі деякого натурального числа на задане.
Наприклад, розглянемо число 3.
Націло (без остачі) на число 3 будуть ділитися: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33 і т. д
Тому, говорять, що кожне з названих вище чисел є кратним числу 3,
 оскільки діляться на нього без остачі.
Будь-яке натуральне число має нескінченно багато кратних.
Найменшим із кратних натурального числа є саме це число, а найбільшого немає.
"""
