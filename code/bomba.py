from datetime import datetime

class Bomba:

    _tipo = None
    __valor = 0
    __quantidade = 0

    def __init__(self, tipo, valor, quantidade):
        self._tipo = tipo
        self.__valor = valor
        self.__quantidade = quantidade
    
    def desconto(self, desconto):
        self.__valor -= self.__valor * desconto
    
    @property
    def vitoria(self):
        if 8 == datetime.now().day:
            return self.__valor - (self.__valor * 0.1)
        return self.__valor

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

class Frentista:

    nome = None
    __cpf = None

    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

if __name__ == "__main__":
    bg = Bomba('G', 4.5, 100)
    print(f'Tipo: {bg._tipo}\nValor: {bg.vitoria}')
    bg.quantidade = 150
    # # bg.setQuantidade(150)
    # bg.addQuantidade(150)
    print('->>>>>>>>>', bg.quantidade)
    
    ba = Bomba('A', 3.5, 100)
    print(f'Tipo: {ba._tipo}\nValor: {ba.vitoria}')