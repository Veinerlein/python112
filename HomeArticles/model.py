import os.path
import pickle


class Article:
    def __init__(self, title, author, pages, descr):
        self.title = title
        self.author = author
        self.pages = pages
        self.descr = descr

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticlesList():
    def __init__(self):
        self.saved_DB = "DB.txt"
        self.articles_dict = self.load_saved()
        self.articles_list = []

    def add_article(self, dict_article):
        article = Article(*dict_article.values())  # article = Article("arturs", "snihurs", 34, "about himself")
        self.articles_dict[article] = article  # варіант словника
        self.articles_list.append(article)  # мій варіант списку

    def get_all(self):
        return self.articles_dict.values()  # варіант із словником зберігає дані лише на час дії першої опції і
        # закінчує після відпрацювання другої
        return self.articles_list  # - варіант із списком постійно має збережені дані

    def find_article(self, inputed_title):
        articles = {}

        for article in self.get_all():
            articles.update({"Title": article.title,
                             "Author": article.author,
                             "Pages": article.pages,
                             "Descr": article.descr})
            if inputed_title in articles["Title"]:
                for k, v in articles.items():
                    print(f"{k}:{v}")
                return articles

    def remove_article(self, title_to_del):
        for art in self.articles_dict:
            if art.title == title_to_del:
                del self.articles_dict[art]
                return self.articles_dict

    def save_to_txt(self):
        with open(self.saved_DB, "wb") as f:
            pickle.dump(self.articles_dict, f)

    def load_saved(self):
        articles = {}
        if os.path.exists(self.saved_DB):
            with open(self.saved_DB, "rb") as f:
                data = pickle.load(f)
            articles.update(data)
            return articles
        else:
            return {}