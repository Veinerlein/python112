"""_____________________________MVC________________________"""
"""
Model
View
Controller
Separation of logic to some parts
"""

import requests
from bs4 import BeautifulSoup
import re


class Pars:
    html = ""

    def __init__(self, url):
        self.url = url

    def get_html(self):
        r = requests.get(self.url).text
        self.html = BeautifulSoup(r, "lxml")

    def parsing(self):
        res = self.html.find_all("div", class_="model-price-range")
        prices = []
        for i in res:
            pr1 = i.find_all("span")[0].text
            price1 = re.sub(r"\D", "", pr1)
            pr2 = i.find("span").parent
            # print(pr1)
            # print(pr2)
            if price1.isnumeric():  # чи є тільки числа у строці
                prices.append((int(price1)))
            else:
                prices.append(int(price1))

    def run(self):
        self.get_html()
        self.parsing()


pars = Pars(f"https://ek.ua/ua/list/206/")

pars.run()
