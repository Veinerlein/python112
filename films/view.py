def add_text(text):
    def wrap(func):
        def wrapper(*args, **kwargs):
            print(f' {text} '.center(50, "="))
            f = func(*args, **kwargs)
            print(50 * "=")
            return f

        return wrapper

    return wrap


class User_interface:
    @add_text("Films")
    def user_business(self):
        print('Options:'
              '\n1 - new film'
              '\n2 - catalogue'
              '\n3 - find the movie'
              '\n4 - delete the movie'
              '\nq - Quit')
        user_answer = input("Enter your option: ")
        return user_answer

    @add_text("Creating the film notice")
    def create_film(self):
        new_film = {
            "Title": None,
            "Genre": None,
            "Director": None,
            "Year": None,
            "Duration": None,
            "Studio": None,
            "Actors": None
        }
        for key in new_film:
            new_film[key] = input(f"{key} is : ")
        return new_film

    @add_text("Catalogue")
    def show_catalogue(self, film_list):
        for ind, obj in enumerate(film_list, 1):
            print(ind, obj)

    def title_to_find(self):
        title = input("Enter the movie you need")
        return title

    @add_text('There is movie you were searched')
    def show_movie(self, movie):
        print(movie)


    def remove_movie_title(self):
        title_to_remove = input("Enter the movie to remove: ")
        return title_to_remove
