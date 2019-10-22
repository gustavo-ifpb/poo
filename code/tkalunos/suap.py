import tkinter as tk
from models import Student
from student import StudentForm, StudentsList, StudentView

class Suap(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Alunos
        self.students = []
        self.students.append( Student(name = 'Davi Sesion', id = '00001', email = 'davi@kung.fu', age = 17, gender = 0) )
        self.students.append( Student(name = 'Vitória Pires', id = '00002', email = 'vitoria@kung.fu', age = 19, gender = 1) )

        # self.screen = StudentForm(self)
        self.screen = StudentsList(self)
        # self.screen = StudentView(self, self.students[0])
        self.screen.pack(fill=tk.BOTH, padx=10, pady=5)

    def changeScreen(self, screen):
        self.screen = screen
        self.screen.pack(fill=tk.BOTH, padx=10, pady=5)

if __name__ == '__main__':
    app = Suap()
    app.title('SUAP')
    app.geometry("200x200+50+50")
    app.mainloop()