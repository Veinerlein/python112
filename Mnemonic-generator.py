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

# Отримати список всіх слів англійської мови
nltk.download("words")
english_words = words.words()

# Вибрати випадкове англійське слово
# Вибрати випадкове слово
res = ""

while len(res.split(" ")) < 13:
    random_word = random.choice(english_words)
    # Перевірити, що слово англійське і не є іменем або власною назвою
    if detect(random_word) == 'en' and random_word.islower():
        res += random_word
        res += " "
print(res)


# Ваші дані для копіювання
data_to_copy = res

# Копіювання даних в буфер обміну
pyperclip.copy(data_to_copy)
print("\nскопійовано у буфер обміну")
url1 = "https://www.coingecko.com/uk"
# url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/import-with-recovery-phrase"
# extension_path = 'C:\\Users\\veine\\AppData\\Local\\Google\\Chrome\\User ' \
#                  'Data\\Default\\Extensions\\nkbihfbeogaeaoehlefnkodbefgpgknn'
# dr = webdriver.Chrome(ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
# Створіть об'єкт опцій для налаштування розширень
chrome_options = Options()
# chrome_options.add_argument(f'--load-extension={extension_path}')
# service = webdriver.chrome.service.Service("\\Chromdriver\\chromedriver.exe")


# Створюю веб-драйвер з підтримкою розширення
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# try:
#     driver.get(extension_path)
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
