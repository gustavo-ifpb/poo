# import p1_remedio as rm
from p1_remedio import Remedio, tipos_remedios

class Cachorro:

    def __init__(self, nome, cor, peso, altura, raca='Vira-lata'):
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.altura = altura
        self.raca = raca

    def porte(self):
        if self.peso <= 6 and self.altura <= 0.33:
            return 0, 'mini'
        elif self.peso <= 15 and self.altura <= 0.43:
            return 1, 'p'
        elif self.peso <= 25 and self.altura <= 0.60:
            return 2, 'm'
        elif self.peso <= 45 and self.altura <= 0.70:
            return 3, 'g'
        else:
            return 4, 'xg'

if __name__ == '__main__':
    c1 = Cachorro('tripa', 'branco', 2.3, 0.38)
    c2 = Cachorro('pipoca', 'branco', 6.3, 0.7, 'beagle')
    print(c1.porte())

    if c1.porte()[0] > c2.porte()[0]:
        print(f'{c1.nome}({c1.porte()[1]}) tem um porte maior do que {c2.nome}({c2.porte()[1]})')
    elif c1.porte()[0] < c2.porte()[0]:
        print(f'{c2.nome}({c2.porte()[1]}) tem um porte maior do que {c1.nome}({c1.porte()[1]})')
    else:
        print(f'{c1.nome} e {c2.nome} possuem o mesmo porte ({c1.porte()[1]})')

    r1 = Remedio('tylenol', 20, 'comprimido', 'Bom para dor de cabeça')
    print(f'{r1.dosagem(c1)} de {r1.tipo}')
    print(tipos_remedios())
