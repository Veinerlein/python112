# decorator
# def add_title(text):  # перетворити у статік метод декорирувану функцію
#     def wrap(func):
#         def wrapper(articles):
#             print("The list of articles: ".center(50, '='))
#             func(articles)
#             print("=" * 50)
#
#             print(text)
#
#         return wrapper
#
#     return wrap


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
    @add_title(' Business with documents ')
    def wait_user_answer(self):
        print("1- creating the document"
              "\n2- watching the articles"
              "\n3- find the article"
              "\n4- delete the article"
              "\nq - Exit")
        user_answer = input("Choose your destiny:")
        print("=" * 60)
        return user_answer  # поверне лише інпут але додатково усі прінти

    add_title(" Creating the Document ")

    def add_user_articles(self):
        dict_article = {
            "Name": None,
            "Author": None,
            "Amount of pages": None,
            "Description": None
        }

        for key in dict_article:
            dict_article[key] = input(f"Input the {key} of article: ")  # я ввоже не key, а по key назву кожної статті

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
    @add_title(" The list with articles ")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")

    @add_title(" Find article ")
    def get_user_article(self):  # 3
        user_article = input("Enter the article you want to find")
        return user_article
        # res = [a for a in article if  article_from_user in a.title]  # title атрибут оскільки така змінна у об  єеті
        # # Article
        # if res:
        #     print("found article(s)")
        #     for ind, art in enumerate(res,1):
        #         print(f"{ind} {art}")
        # else:
        #     print(f"No aricle like {article_from_user}")

    @add_title(" Here is founded article")
    def show_single_article(self, article):  # 3
        for key in article:
            print(f"{key} of the article - {article[key]}")

    def show_incorrect_title_error(self, user_title):
        print(f"Article {user_title} is not found")

    @add_title(" Deleting the article ")
    def remove_single_article(self, article):
        print(f"Article {article} was removed")

    @add_title(" Article error message ")
    def show_incorrect_answer_error(self, answer):
        print(f"The answer {answer} doesn't exist")
