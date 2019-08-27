class Robot:

    def __init__(self, name, life = 100):
        self.name = name
        self.life = life
        self.attackValue = 10
        self.defenseValue = 10

    def attack(self, opponent):
        opponent.life -= self.attackValue + opponent.defenseValue * 0.5
    
    def __str__(self):
        return f'{self.name} ({self.life})'

class RobotAlpha(Robot):

    def __init__(self, name):
        super().__init__(name, 100)
        self.attackValue = 15
        self.defenseValue = 7

class RobotBeta(Robot):

    def __init__(self, name):
        super().__init__(name, 100)
        self.defenseValue = 12

if __name__ == '__main__':
    robotAlpha = RobotAlpha('Alph4')
    robotBeta = RobotBeta('B3t4')

    print(robotAlpha, robotBeta)
    robotAlpha.attack(robotBeta)
    print(robotAlpha, robotBeta)