import chuchu

class Animal:

    tipo = None
    olhos = 2
    boca = 1
    hp = 10

    def comer(self, comida):
        self.hp += comida // 5

if __name__ == '__main__': 
    print(__name__)