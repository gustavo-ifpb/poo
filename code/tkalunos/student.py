import sys
import tkinter as tk
import tkinter.ttk as ttk
from models import Student

class StudentForm(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.imageFile = tk.PhotoImage(file='bode.gif')
        image = tk.Label(self, image=self.imageFile, height=50)
        image.pack(fill=tk.X)

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
        ageLabel = tk.Label(self, text="Idade", bg="gray", fg="white")
        ageLabel.pack(fill=tk.X, ipady=5)

        self.ageSpin = tk.Spinbox(self, from_=0, to=10, increment=.2)
        self.ageSpin.pack(pady=5)

        ''' Gender '''
        genderLabel = tk.Label(self, text="Gênero", bg="gray", fg="white")
        genderLabel.pack(fill=tk.X, ipady=5)

        self.genderSpin = tk.Spinbox(self, values=('Feminino', 'Masculino', 'Não binário'), state='readonly')
        self.genderSpin.pack(pady=5)

        ''' Gender '''
        genderLabel = tk.Label(self, text="Gênero #2", bg="gray", fg="white")
        genderLabel.pack(fill=tk.X, ipady=5)

        self.genderCombo = ttk.Combobox(self, values=('Feminino', 'Masculino', 'Não binário'), state='readonly', postcommand=self.itemSelected)
        self.genderCombo.pack(pady=5)
        self.genderCombo['values'] = ('Test',)

        ''' Save '''
        saveButton = tk.Button(self, text="Salvar", command=self.save)
        saveButton.pack(fill=tk.X)

    def save(self):
        # print("Botão 'Salvar' clicado")
        student = Student()
        student.name = self.nameEntry.get()
        student.id = self.idEntry.get()
        student.email = self.emailEntry.get()
        student.age = self.ageSpin.get()
        student.gender = self.genderSpin.get()
        print(self.genderCombo.get())
        print(student)

    def itemSelected(self):
        print('Algum item foi selecionado')

class StudentView(tk.Frame):

    def __init__(self, master, student):
        tk.Frame.__init__(self, master)

        self.controller = master

        # Back button
        backButton = tk.Button(self, text='Voltar', width=20, command=self.back)
        backButton.pack(fill=tk.X, ipady=5)

        # Matrícula
        idLabel = tk.Label(self, text="Matrícula", bg="gray", fg="white")
        idLabel.pack(fill=tk.X, ipady=5)

        idLabel = tk.Label(self, text=student.id)
        idLabel.pack(fill=tk.X, ipady=5)

        # Matrícula
        idLabel = tk.Label(self, text="Nome", bg="gray", fg="white")
        idLabel.pack(fill=tk.X, ipady=5)

        idLabel = tk.Label(self, text=student.name)
        idLabel.pack(fill=tk.X, ipady=5)

        # Matrícula
        idLabel = tk.Label(self, text="Email", bg="gray", fg="white")
        idLabel.pack(fill=tk.X, ipady=5)

        idLabel = tk.Label(self, text=student.email)
        idLabel.pack(fill=tk.X, ipady=5)

        # Matrícula
        idLabel = tk.Label(self, text="Gênero", bg="gray", fg="white")
        idLabel.pack(fill=tk.X, ipady=5)

        idLabel = tk.Label(self, text=student.gender)
        idLabel.pack(fill=tk.X, ipady=5)

        if student.gender == 0:
            idLabel['text'] = 'Masculino'
        elif student.gender == 1:
            idLabel['text'] = 'Feminino'
        else:
            idLabel['text'] = 'Não binário'

    def back(self):
        self.controller.changeScreen(StudentsList(self.controller))
        self.destroy()


class StudentsList(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Referência para SUAP
        self.controller = master

        ''' Listbox '''
        self.studentListbox = tk.Listbox(self)
        self.studentListbox.pack(fill=tk.X)
        self.studentListbox.bind('<Double-Button-1>', self.itemClicked)

        for student in self.controller.students:
            self.studentListbox.insert(tk.END, student.name)
    
    def itemClicked(self, selection):
        student = self.controller.students[self.studentListbox.curselection()[0]]
        self.controller.changeScreen(StudentView(self.controller, student))
        self.destroy()

        # self.controller.wait_window(StudentView(self.controller, student))