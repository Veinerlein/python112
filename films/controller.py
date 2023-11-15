from view import User_interface
from model import Films


class Controller:
    def __init__(self):
        self.view = User_interface()
        self.model = Films()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.view.user_business()
            self.business_with_answer(answer)

    def business_with_answer(self, answer):
        if answer == "1":
            created = self.view.create_film()
            self.model.add_film(created)
        elif answer == "2":
            films = self.model.get_all()
            self.view.show_catalogue(films)
        elif answer == "3":
            title_to_find = self.view.title_to_find()
            self.model.find_film(title_to_find)
        elif answer == "4":
            title = self.view.remove_movie_title()
            self.model.remove_movie(title)
        elif answer == "q":
            self.model.dump_DB()
        else:
            print('Enter the correct option')
