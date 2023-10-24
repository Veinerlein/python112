"""Parsing"""
import csv
import re

import requests
from bs4 import BeautifulSoup


# f = open("index.html", encoding="utf-8").read()  # encoding чисто для унеможливлення помилки кодування
# soup = BeautifulSoup(f, "html.parser")  # parser встроєний в інтерпретатор пайтон. дає можливість витягувати дані
#
# """ пошук по тегу та пошук по тегам """
# row = soup.find("p", class_="link-read-post")  # перший аргумент це тег, другий це або id або class
# # підкреслення оскільки class це зарезервоване слово
# print(row)  # <p class="link-read-post"><a href="{{ p.get_absolute_url }}">Read about</a></p>
# """ soup.find - повертає перший знайдений елемент """
#
# row2 = soup.find_all("p")[1]  # повертає усписок із знайдених співпадінь
# print(row2)
# row3 = soup.find_all("p")[0].find("p")
# print(f"ROW3:\n\t\t{row3}")
#
# row4 = soup.find("div", {'class': "clear"})  # словник як аналог, але якщо є дефіс у елементі пошуку, то словник
# # МАСТХЕВ (наприклад, data-set = "salary" == {"data-set": "salary"})
# print(row4)
#
# # row_rext = soup.find("p", string=" All actors ")
# # print("row-text", row_rext)
# #
# # row_rext2 = soup.find("p", string=" All actors ").parent # знайде той тег,який оточує текст
# # print("row-text2", row_rext2)
# #
# #
# # row_rext3 = soup.find("p", string=" All actors ").parent.parent # знайде цілий блок
# # print("row-text3", row_rext3)
# print()
# print("=========" * 10)
# print()
#
# f2 = open("Solidity — Вікіпедія.html", encoding="utf-8").read()
# s = BeautifulSoup(f2, "html.parser")
#
# result = s.find("div", id="wlm_2023_ua")
# print(result)
#
# print()
# print("=========" * 10)
# print()
#
# print(result.find_next_sibling())  # знайти наступного
#
# print()
# print("=========" * 10)
# print()
#
# print(result.find_previous_sibling())  # знайти попереднього
#
# print()
# print("=========" * 10)
# print()
#
#
# # для пошуку копірайтерів створена функція
#
# def get_element(tag):
#     what = tag.find("span")
#     if what and "Посилання сюди" in what.text:  # потрібно провірити чи What не є NONE а також What.text обовязково у
#         # новій версії парсера
#         return tag
#     return None
#
#
# list_of_elements = []
#
# LOE = s.find_all("div", class_="vector-menu-content")
#
# for i in LOE:
#     cw = get_element(i)
#     if cw:
#         list_of_elements.append(cw.text)  # додасть тільки текст, без тегів.
#
# print()
# print("=========" * 10)
# print()
#
# print(f"RESULT{list_of_elements}")
#
# print()
# print("=========" * 10)
# print()
#
# for i in row:
#     print(i.text)  # виведе тільки текст (в даному випадку Read about)
#
# for i in result:  # Змагайтеся за призи у «Вікі любить пам’ятки» — подавайте фото/відео для Вікіпедії!
#     print(i.text)  # Дізнайтеся більше
#
#
# # у парсері для опрацювання тексту використовують регулярні вирази
#
# def get_str(s):
#     pattern = r"\d+"  # -  пошук любої цифри від однієї до безкінечності
#     res = re.findall(pattern, s)  # паттерн, я також місце де саме шукатимуться дані
#     res2 = re.search(pattern, s)  # паттерн, я також місце де саме шукатимуться дані
#     print(res2)
#     if len(res) > 1:
#         print(res)
#     if res2 is not None:
#         print(res2.group())  # поверне перший знайений результат. тобто 2014
#
#
# for i in s:
#     get_str(i.text)
#
# r = requests.get("https://wordpress.org/")
# print(r.status_code)  # 200
# print(r.headers)  # {'Server': 'nginx', 'Date': 'Wed, 18 Oct 2023 13:01:50 GMT',
# # 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked',
# # 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Strict-Transport-Security': 'max-age=3600',
# # 'X-Olaf': 'â\x9b\x84', 'Link': '<https://wordpress.org/wp-json/>; rel="https://api.w.org/",
# # <https://wordpress.org/wp-json/wp/v2/pages/457>; rel="alternate"; type="application/json",
# # <https://w.org/>; rel=shortlink',
# # 'X-Frame-Options': 'SAMEORIGIN', 'Content-Encoding': 'gzip', 'X-nc': 'HIT ord 2'}
#
# # print(r.text)# дуже багато тексту
# print()
# print(r.headers["content-type"])  # text/html; charset=UTF-8
#
# print()


# print(r.content) # зміст в байтах


def get_html(url):
    r = requests.get(url)
    return r.text


# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("h1", class_="wp-block-wporg-random-heading has-heading-cta-font-size").text
#     return p1

def refined(s):
    res = re.sub(r"\D+", "", s)  # 1 = що шукаєм, 2 = на що міняєм, 3 = у якому місці(строці)
    return res


def get_data(html):
    data = {}
    soup = BeautifulSoup(html, "lxml")
    p2 = soup.find_all("section", class_="plugin-section")[1]
    plugins = p2.find_all('article')
    for plugin in plugins:
        name = plugin.find("h3").text
        url = plugin.find('h3').find("a").get("href")  # з find замість get не працюватиме
        # метод get() дає можливість отримати дані атрибуту.
        # Цей метод використовується, коли потрібно отримати значення атрибута 'href' із тегу HTML
        # (зазвичай тегу a) і зберегти його в змінній.
        print(name)
        print(url)
        rating = plugin.find("span", class_="rating-count").text
        r = refined(rating)
        data.update({f"{name}": f"{url}, rate: {r}"})
        data_ex = {"name": name, "URL": url, "Rating": r}
        # write_to_csv(data_ex)
    write_to_csv(data)
    return data


def write_to_csv(d):
    with open("plugins2.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=',')
        # writer.writerow((d["name"], d["URL"], d["Rating"]))
        writer.writerow(["Name", "URL", "Rating"])
        for k, v in d.items():
            url, rate = v.split(", rate: ")
            writer.writerow([k, url, rate])


def main():
    url = "https://wordpress.org/plugins/"
    print(get_data(get_html(url)))


if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup
import lxml
import csv


class Parser:

    def __init__(self, url, filename="parser_home.csv"):
        self.file_name = filename
        self.url = url

    def get_data(self):
        data = requests.get(self.url)
        soup = BeautifulSoup(data.text, "lxml")
        return soup

    def find_elem(self):
        r = self.get_data().find("main", class_="site-main").find_all("article")
        l = list()
        for i in r:
            l.append(i.find("h3", class_="entry-title").text)

        return l

    def dump_elem(self):
        data = self.find_elem()
        with open(self.file_name, "a") as f:
            writer = csv.writer(f, lineterminator="\r", delimiter=",")
            for i in data:
                writer.writerow([i])

    # def clean_file(self):
    #     with open(self.file_name, "w") as f:
    #         writer = csv.writer(f)
    #         writer.writerow("")

    def clean_file2(self):
        with open(self.file_name, "w") as f:
            f.truncate(0)  # Метод truncate(0) використовується для обрізання
            # файлу до заданої довжини, в цьому випадку, до довжини 0 байтів.
            # У контексті роботи з файлами це означає повне очищення
            # вмісту файлу, зробивши його порожнім.


p = Parser("https://wordpress.org/plugins/browse/popular/")

# print(p.clean_file2())
# print(p.dump_elem())
print()
print('+' * 89)  # ====================================================================
print()

f = requests.get("https://rozetka.com.ua/ua/mobile-phones/c80003/page=2;producer=poco;sort=expensive/").text
soup = BeautifulSoup(f, "lxml")
dani = soup.find_all("span", class_='goods-tile__title')
money = soup.find_all('span', {"class": "goods-tile__price-value"})
# res = list(zip(dani,money))
# res = list(map(lambda x, y: f"{x}-{y}", dani, money)) # поверне строку що запорить подальше використання
dani = [i.text for i in dani]
money = [i.text for i in money]
money2 = []

for element in money:
    money2.append(element.replace("\xa0", "").replace('₴', ""))

res = [f'{x}-{y}' for x, y in zip(dani, money2)]

l = []
for i in res:
    print(i)

[print(l) for l in l]
