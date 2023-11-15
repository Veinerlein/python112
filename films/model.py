import csv


class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title}({self.duration}) by {self.director} in {self.studio} with {self.actors}. {self.year}"


class Films:
    def __init__(self):
        self.DB = "films_DB.csv"
        self.films = self.load_DB()

    def add_film(self, created_film):
        film = Film(*created_film.values())
        res = self.films.append(film)
        return res

    def get_all(self):
        return self.films

    def find_film(self, title_to_find):
        for film in self.films:
            movie = {
                "Title": film.title,
                "Genre": film.genre,
                "Director": film.director,
                "Year": film.year,
                "Duration": film.duration,
                "Studio": film.studio,
                "Actors": film.actors}
            if title_to_find in movie.values():
                [print(f'{k} : {v}') for k, v in movie.items()]
                return movie

    def remove_movie(self, title):
        for film in self.films:
            if title in [
                film.title,
                film.genre,
                film.director,
                film.year,
                film.duration,
                film.studio,
                film.actors]:
                self.films.remove(film)
                print(f"The {film.title} was removed")

    def dump_DB(self):
        fields = ["title",
                  "genre",
                  "director",
                  "year",
                  "duration",
                  "studio",
                  "actors"]
        with open(self.DB, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for film in self.films:
                writer.writerow(film.__dict__)

    def load_DB(self):
        with open(self.DB, "r") as f:
            films = []
            data = csv.DictReader(f)  # <csv.DictReader object at 0x0000017D369A3D90>
            for d in data:
                print(d.values())
                obj = Film(*d.values())
                films.append(obj)
            return films
