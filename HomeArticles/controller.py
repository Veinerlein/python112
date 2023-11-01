from model import ArticlesList
from views import UserInterface


class Controller:
    def __init__(self):
        self.article_DB = ArticlesList()
        self.user_int = UserInterface()

    def run(self):
        answer = None
        while answer !="q":
            answer = self.user_int.user_choice()
            self.options(answer)

    # метод із опціями
    def options(self, answer_from_user):
        if answer_from_user == '1':
            created = self.user_int.create_article() # у змінну ставлю створену статтю
            # to save into database
            self.article_DB.add_article(created) # в метод додавання до бази даних ставлю створену статтю,
            # тим самим доповнюю створення статті до кінця
        if answer_from_user == "2":
            articles = self.article_DB.get_all() # для того, щоб показати статті, витягую їх із бази даних
            self.user_int.show_articles(articles) # витягнуті статті із оперативної памяті кладу у метод демонстрації
            # статтей
