def add_text(text):
    def wrap(func):
        def wrapper(*args, **kwargs):
            print(text.center(50, "="))
            f = func(*args, **kwargs)
            print(50 * "*")
            return f # повернути результат функції, інакше не працюватиме user_choice належним чином
        return wrapper

    return wrap


class UserInterface:
    @add_text(" List of articles ")
    def user_choice(self):
        print('Options: '
              '\n1 - to create'
              '\n2 - to watch')
        print("q - Quit")
        user_answer = input("Make your choice: ")

        return user_answer

    @add_text(" Creating the article ")
    def create_article(self):
        article = {
            "Title": None,
            "Author": None,
            "Pages": None,
            "Descr": None
        }
        for key in article:
            article[key] = input(f"Enter that the {key} is: ")
        return article

    @add_text(" Articles list ")
    def show_articles(self, list_articles):
        for ind, article in enumerate(list_articles, 1):
            print(f"{ind} {article}")
