"""
OS
OS.PATH
"""

import os

print("Current directory", os.getcwd()) # E:\pythonProject1\les
print(os.listdir()) # Список назв усіх файлів у поточній директорії або по вказаному шляху
print(os.listdir("..")) # Список назв усіх файлів, тих що на рівень вище
# os.mkdir("folder1") # створює  папку із вказаним ім'ям якщо такої неіснує. повторно не запуститься
if not os.path.exists("folder1"):
    os.mkdir("folder1")
if not os.path.exists("folder1/folder2/folder3"):
    os.makedirs("folder1/folder2/folder3") # створює кінцеву директорію та проміжні папки якщо таких не було

# os.remove("test.txt") # видаляє файл, але не папку.
os.rename("folder1/folder2/ts.txt", "ts1.txt") # перейменовує файл або директорію (папку), а також
# перенести файл по новій адресі



