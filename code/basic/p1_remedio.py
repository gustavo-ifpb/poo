class Remedio:

    def __init__(self, nome, quantidade, tipo, bula):
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        self.bula = bula
    
    def dosagem(self, cachorro):
        return (cachorro.porte()[0] + 1) / 5
        # if cachorro.porte()[0] == 0:
        #     return 1/5
        # elif cachorro.porte()[0] == 1:
        #     return 2/5
        # elif cachorro.porte()[0] == 2:
        #     return 3/5
        # elif cachorro.porte()[0] == 3:
        #     return 4/5
        # else:
        #     return 1

def tipos_remedios():
    return ('comprimido', 'gotas', 'injetável')