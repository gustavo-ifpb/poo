from movie import Movie
from core import User

class Store:

    def __init__(self):
        self.movies = []
        self.users = []

    def addMovie(self, movie):
        self.movies.append(movie)

    def searchMovie(self, id):
        for movie in self.movies:
            if id == movie.id:
                return movie
        return None

    def addUser(self, user):
        self.users.append(user)

    def searchUser(self, id):
        for user in self.users:
            if id == user.id:
                return user
        return None
    
    def rent(self, user, movie):
        if not movie.available:
            return False
        movie.available = False
        user.addMovie(movie)


if __name__ == "__main__":
    store = Store()
    op = int(input('1. Cadastrar filme\n2. Cadastrar usuário\n3. Alugar um filme\n0. Sair'))
    while op != 0:
        # Add movie
        if op == 1:
            id = input('Digite o código do filme? ')
            name = input('Digite o nome do filme? ')
            year = int(input('Digite o ano do filme? '))
            movie = Movie(id, name, year)
            
            store.addMovie(movie)
        
        # Add user
        elif op == 2:
            id = input('Digite o código do usuário? ')
            name = input('Digite o nome do usuário? ')
            phone = input('Digite o telefone do usuário? ')
            user = User(id, name, phone)

            store.addUser(user)
        
        # Rent
        elif op == 3:
            user = None
            while user == None:
                userId = input('Digite o código do usuário: ')
                user = store.searchUser(userId)

                if user == None:
                    print('Usuário não econtrado!')
            
            movie = None
            while movie == None:
                movieId = input('Digite o código do filme: ')
                movie = store.searchMovie(movieId)

                if movie == None:
                    print('Filme não encontrado!')
            
            if movie.available:
                movie.available = False
                user.addMovie(movie)
            else:
                print('Filme indisponível!')