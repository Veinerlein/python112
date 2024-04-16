import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
from fake_useragent import UserAgent


def test_eight_components(url):
    user_agent_list = ["hello world", "best_of_the_best", "Python_seeker"]
    useragent = UserAgent()

    url = url
    options = Options()
    options.add_argument("start-maximized")
    # options.add_argument(f"user-agent={random.choice(user_agent_list)}]")
    options.add_argument(f"user-agent={useragent.random}]")
    chromedriver = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chromedriver, options=options)

    driver.get(url)

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(4.5)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    #
    # text_box.send_keys("Selenium")
    # submit_button.click()
    #
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"
    time.sleep(25)
    driver.close()
    driver.quit()


test_eight_components("https://www.youtube.com/watch?v=r4OY7hp4yd8")
