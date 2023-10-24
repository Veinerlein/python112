from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")
        # print(req)
        return req

    def parsing(self):
        news = self.html.find_all("div", class_="caption")
        # print(news)
        for item in news:
            title = item.find("h3").text
            href = item.find("a").get("href")
            author = item.find("footer").find("li", class_="topic-info-author").text.strip()
            # print(title)
            self.res.append({
                "Title": title,
                "Href": href,
                "Author": author
            })
        print(self.res)


    def safe(self):
        with open(self.path, "w") as f:
            i = 1
            for  item in self.res:
                f.write(f"News № {i}\n\nTitle: {item['Title']}\nlink: {item['Href']}\nAuthor: {item['Author']}\n\n"
                        f"{'*'*21}\n")
                i+=1


    def run(self):
        self.get_html()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.parsing()
        self.safe()


"""_____________________________MVC________________________"""
