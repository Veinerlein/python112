def add_text(text):
    def wrap(func):
        def wrapper(*args, **kwargs):
            print(text.center(50, "="))
            f = func(*args, **kwargs)
            print(50 * "*")
            return f  # повернути результат функції, інакше не працюватиме user_choice належним чином

        return wrapper

    return wrap


class UserInterface:
    @add_text(" List of articles ")
    def user_choice(self):
        print('Options: '
              '\n1 - to create'
              '\n2 - to watch'
              '\n3 - to find'
              '\n4 - to delete')
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

    def title_to_find(self):
        title_to_find = input("Enter the searching data")
        return title_to_find


    #Bonus from the chat
    def find_article(self, articles):
        title_to_find = input("Enter the title of the article you want to find: ")
        found_articles = [article for article in articles if article.title == title_to_find]

        if found_articles:
            print("Found articles:")
            for ind, article in enumerate(found_articles, 1):
                print(f"{ind} {article}")
        else:
            print(f"No articles found with the title '{title_to_find}'.")

    # bonus
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