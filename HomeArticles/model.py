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
        self.articles_dict = {}
        self.articles_list = []

    def add_article(self, dict_article):
        article = Article(*dict_article.values())  # article = Article("arturs", "snihurs", 34, "about himself")
        self.articles_dict[article] = article # варіант словника
        self.articles_list.append(article) # мій варіант списку

    def get_all(self):
        return self.articles_dict.values() # варіант із словником зберігає дані лише на час дії першої опції і
        # закінчує після відпрацювання другої
        return self.articles_list # - варіант із списком постійно має збережені дані
