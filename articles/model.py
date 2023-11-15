"""Data base"""
import os.path
import pickle


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
        self.db_name = "db.txt"
        self.articles = self.load_data()  # буде пустий список якщо документа не існує, якщо існує, ито отримаємо ті дані

    def add_article(self, dict_article):  # метод додачі у базу даних
        article = Article(*dict_article.values())  # сюди попадуть значення із аргумента, який буде словником
        self.articles[article.title] = article  # Метод values() повертає спеціальний вид об'єкта,
        # відомий як "dict_values," який є подібним до списку, але є видом ітерабельного об'єкта

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):  # 3
        article = self.articles[user_title]
        dict_article = {
            "Name": article.title,
            "Author": article.author,
            "Amount of pages": article.pages,
            "Description": article.description
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
