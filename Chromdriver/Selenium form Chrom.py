import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
from fake_useragent import UserAgent
from Auth_data import login
from Auth_data import password
from selenium.webdriver.common.keys import Keys


def test_eight_components(url):
    useragent = UserAgent()

    options = Options()
    options.add_argument("start-maximized")

    options.add_argument(f"user-agent={useragent.random}")
    chromedriver = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chromedriver, options=options)

    driver.get(url)

    # вставка логіна
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys(login)
    # вставка пароля
    password_input = driver.find_element(By.ID, "pass")
    password_input.clear()
    password_input.send_keys(password)
    # Авторизація
    driver.implicitly_wait(0.5)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    driver.implicitly_wait(0.5)
    time.sleep(15)
    driver.close()
    driver.quit()


test_eight_components("https://uk-ua.facebook.com/")
