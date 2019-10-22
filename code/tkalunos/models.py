'''
Gender:
- 0: homem
- 1: mulher
- 2: não binário
'''
class Student:

    def __init__(self, name = None, id = None, email = None, age = 0, gender = None):
        self.name = name
        self.id = id
        self.email = email
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.email} ({self.age} - {self.gender})"