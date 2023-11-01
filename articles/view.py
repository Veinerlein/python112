# decorator
def add_title(text):  # перетворити у статік метод декорирувану функцію
    def wrap(func):
        def wrapper(articles):
            print("The list of articles: ".center(50, '='))
            func(articles)
            print("=" * 50)

            print(text)

        return wrapper

    return wrap


# decorator2
def add_title(title):
    def wrapper(func):
        def wrap(*arg, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*arg, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    def wait_user_answer(self):
        print(" Enter customer data:".center(50, "="))
        print('Business with documents')
        print("1- creating the document"
              "\n2- watching the articles"
              "\nq - Exit")
        user_answer = input("Choose your destiny:")
        print("=" * 60)
        return user_answer  # поверне лише інпут але додатково усі прінти

    def add_user_articles(self):
        dict_article = {
            "Name": None,
            "Author": None,
            "Amount of pages": None,
            "Description": None
        }
        print(" creating the Document".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Input the {key} of article: ")  # я ввоже не key, а по key назву кожної статті
        print(50 * "=")
        return dict_article

    # @staticmethod
    # def add_title(func):
    #     def wrapper(articles):
    #         print("The list of articles: ".center(50, '='))
    #         func(articles)
    #         print("=" * 50)
    #
    #     return wrapper
    # @staticmethod
    @add_title("Entering the customer data")
    def show_all_articles(self, articles):

        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
