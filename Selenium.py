import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pyperclip
import nltk  # імпорт бібліотеки Natural Language Tool Kit
from nltk.corpus import words  # імпорт слів
import random  # імпорт рандому
from langdetect import detect  # детектор на лише слова англійською
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# # Отримати список всіх слів англійської мови
# nltk.download("words")
# english_words = words.words()
#
# # Вибрати випадкове англійське слово
# # Вибрати випадкове слово
# res = ""
#
# while len(res.split(" ")) < 13:
#     random_word = random.choice(english_words)
#     # Перевірити, що слово англійське і не є іменем або власною назвою
#     if detect(random_word) == 'en' and random_word.islower():
#         res += random_word
#         res += " "
# print(res)


# Ваші дані для копіювання
# data_to_copy = res

# Копіювання даних в буфер обміну
# pyperclip.copy(data_to_copy)
# print("\nскопійовано у буфер обміну")
url1 = "https://www.coingecko.com/uk"
options = Options()  # об'єкт опцій
useragent = UserAgent()  # об'єкт юзерагента із бібліотеки
options.add_argument("start-maximized")  #  завжди великий екран
options.add_argument(f"user-agent={useragent.random}")
chrom_driver = ChromeDriverManager().install()  # інсталяція драйвера замість його скачування

driver = webdriver.Chrome(service=Service(chrom_driver), options=options)  # - ПРАВИЛЬНИЙ КОД
# ВКЛЮЧАЄ В СЕБЕ СЕРВІС


try:
    driver.get(url=url1)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
