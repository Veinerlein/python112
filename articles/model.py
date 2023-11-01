"""Data base"""


class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article): # метод додачі у базу даних
        article = Article(*dict_article.values())# сюди попадуть значення із аргумента, який буде словником
        self.articles[article.title] = article # Метод values() повертає спеціальний вид об'єкта,
        # відомий як "dict_values," який є подібним до списку, але є видом ітерабельного об'єкта

    def get_all_articles(self):
        return self.articles.values()
