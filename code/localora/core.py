class User:

    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
        self.movies = []

    def addMovie(self, movie):
        self.movies.append(movie)

    def remMovie(self, movie):
        for m in self.movies:
            if m.id == movie.id:
                self.movies.remove(movie)
                return True
        return False