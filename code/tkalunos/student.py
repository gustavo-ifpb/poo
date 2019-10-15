import tkinter as tk
from models import Student

class StudentForm(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        ''' Name '''
        nameLabel = tk.Label(self, text="Título", bg="gray", fg="white")
        nameLabel["text"] = "Nome do aluno"
        # title.place(x=50, y=50)
        # title.grid(row=0, column=0)
        nameLabel.pack(fill=tk.X, ipady=5)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack(fill=tk.X, pady=5)

        ''' ID '''
        idLabel = tk.Label(self, text="Matrícula", bg="gray", fg="white")
        idLabel.pack(fill=tk.X, ipady=5)

        self.idEntry = tk.Entry(self)
        self.idEntry.pack(fill=tk.X, pady=5)

        ''' Email '''
        emailLabel = tk.Label(self, text="Email", bg="gray", fg="white")
        emailLabel.pack(fill=tk.X, ipady=5)

        self.emailEntry = tk.Entry(self)
        self.emailEntry.pack(fill=tk.X, pady=5)

        ''' Age '''
        emailLabel = tk.Label(self, text="Email", bg="gray", fg="white")
        emailLabel.pack(fill=tk.X, ipady=5)

        ''' Save '''
        saveButton = tk.Button(self, text="Salvar", command=self.save)
        saveButton.pack(fill=tk.X)

    def save(self):
        # print("Botão 'Salvar' clicado")
        student = Student()
        student.name = self.nameEntry.get()
        student.id = self.idEntry.get()
        student.email = self.emailEntry.get()
        print(student)