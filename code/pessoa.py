class Pessoa:

    __nome = None
    __idade = 0
    peso = 0
    altura = 0

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.__idade += 1
        if self.__idade < 21:
            self.crescer(0.05)

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, cm):
        self.altura += cm

    def getNome(self):
        return self.__nome

if __name__ == '__main__':
    p = Pessoa('Gustavo', 32, 80, 1.73)
    p.emagrecer(1.2)
    # print(f'Nome: {p.getNome()} - Peso: {p.peso}')