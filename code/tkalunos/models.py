class Student:

    def __init__(self, name = None, id = None, email = None):
        self.name = name
        self.id = id
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.email}"