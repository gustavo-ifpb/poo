class Duck:

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.angle = 0
        self.bulletRange = 10
        self.bullets = 40

    def fire(self, angle, bulletRange = None):
        print('Mãe: atirando!')
    
class DuckVitor(Duck):

    def fire(self, angle, bulletRange = None):
        print(f'{self.name}: Atirando')

class DuckGlicia(Duck):
    
    def __init__(self):
        super().__init__('purple', 'Glicia')

class DuckVitoria(Duck):
    
    def __init__(self, color):
        super().__init__(color, 'Vitoria')
        super().fire(10, 4)
        self.fire()
        self.size = 1
    
    def fire(self):
        print(f'{self.name}: Atirando')

if __name__ == "__main__":
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    duckVitor = DuckVitor('yellow', 'Vitor')
    duckVitor.fire(10, 30)
    
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    duckGlicia = DuckGlicia()
    print(duckGlicia.name)
    duckGlicia.fire(10, 30)
    
    print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
    duckVitoria = DuckVitoria('blue')
    print(duckVitoria.name)
    duckVitoria.fire()