from datetime import datetime
# import bomba
from bomba import *

class Posto:

    __bombas = None

    def __init__(self):
        self.__bombas = []
    
    def addBomba(self, bomba):
        if datetime.now().day == 8:
            bomba.desconto(0.1)
        self.__bombas.append(bomba)

    def abastecer(self, tipo, litros):
        bomba = None
        for bomba in self.__bombas:
            if bomba._tipo == tipo:
                break
        bomba.quantidade -= litros
    
if __name__ == "__main__":
    p = Posto()
    b = Bomba('G', 4.5, 100)
    p.addBomba(b)

    b2 = Bomba('A', 3.5, 200)
    p2.addBomba(b)

    p.abastecer('G', 10)