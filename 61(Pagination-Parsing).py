import requests
import csv
from bs4 import BeautifulSoup


def get_elem(soup):
    elements = soup.find_all("article", class_="plugin-card")
    print(len(elements))
    for el in elements:
        try:
            name = el.find("h3").text
        except ValueError:
            name = ""
        print(name)
        try:
            url = el.find("h3").find("a").get("href")
        except ValueError:
            url = ""
        print(url)
        try:
            snippet = el.find("div", class_="entry-excerpt").text.strip()
        except ValueError:
            snippet = ""
        print(snippet)
        try:
            active = el.find("span", class_="active-installs").text.strip()
        except ValueError:
            active = ""
        print(active)
        try:
            c = el.find("span", class_="tested-with").text.strip()
            cy = refind(c)  # взяв лише цифри
        except ValueError:
            cy = ""
        print(cy)
        print("-" * 35)
        data = {
            "name": name,
            "url": url,
            "snippet": snippet,
            "active": active,
            "cy": cy
        }
        write_csv(data)


def write_csv(data):
    with open("plugin.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\r")
        writer.writerow((data["name"],
                         data["url"],
                         data["snippet"],
                         data["active"],
                         data["cy"]))


def refind(s):
    s = s.split(" ")  # відкинув усе крім цифр
    return s[-1]


def main():
    for i in range(1, 46):
        url = f"https://wordpress.org/plugins/browse/popular/page/{1}/"
        request = requests.get(url).text
        soup = BeautifulSoup(request, "lxml")
        get_elem(soup)


# if __name__ == "__main__":
#     main()
import pytunneling
from pars import Parser


def mains():
    pars = Parser("https://www.ixbt.com/live/", "news.txt")
    pars.run()


# if __name__ == "__main__":
#     mains()

import random
import time


class ParsTech:
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    Referer = "https://hotline.ua/"
    data = {}

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def pagination(self):
        res = int(BeautifulSoup(requests.get('https://ek.ua/list/61/').text, "lxml")
                  .find("div", class_="ib page-num").find_all("a", {"class": "ib"})[-1].text)
        return res  # кількість сторінок

    def get_html(self, page=0):
        r = requests.get(f"{self.url}{page}/").text
        soup = BeautifulSoup(r, "lxml")
        return soup

    def get_element(self):
        for page in range(self.pagination()):
            element = self.get_html(page=page)
            res = element.find_all("table", class_='model-short-block')
            data = []
            for product in res:
                title = product.find("span", class_="u").text.strip()
                # self.data["Title"]=title
                try:
                    description = product.find("div", class_='m-s-f2').text.strip()
                except AttributeError:
                    description = "Not taked"
                # self.data["Description"] = description
                # time.sleep(1)
                try:
                    price = product.find("div", class_="model-price-range").find("a").text
                except AttributeError:
                    price = "Not took"
                # self.data['Price']=price
                self.data = {
                    "Title": title,
                    "Description": description,
                    "Price": price
                }
                data.append(self.data)
                # print(product.find("div", {'class id': "hj6olx8qyf2"}))
                # print(title)
                self.dump_info(data)

    def dump_info(self, data):
        with open(self.filename, "a") as f:
            w = csv.writer(f, lineterminator="\r")
            w.writerow(["Product Name", "Description of the product", "Price range of the product"])
            for i in data:
                w.writerow((i["Title"],
                            i["Description"],
                            i['Price']))


e_katalog = ParsTech("https://ek.ua/list/61/", "EKATALOG_SSD.csv")

# print(hotline_ua.pagination())
# print(e_katalog.get_element())
print(e_katalog.get_html().find("div", class_="model-price-range")) # price
print()
print(e_katalog.get_html().find("span", class_="u")) # title
print()
print(e_katalog.get_html().find_all("div", class_="model-short-div list-item--goods")[0].text)
print()
print(e_katalog.get_html().find_all("div", class_="model-short-div list-item--goods")[1].text)
print()
print(e_katalog.get_html().find("td", class_="model-hot-prices-td").text)


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


# pars = Pars(f"https://ek.ua/ua/list/206/")
# pars.run()

