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


class StudentsList(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ''' Listbox '''
        self.students = ['Filipe', 'Gabriel', 'Vitórias', 'Ester']

        self.studentListbox = tk.Listbox(self)
        self.studentListbox.pack(fill=tk.X)
        self.studentListbox.bind('<Double-Button-1>', self.itemClicked)

        for student in self.students:
            self.studentListbox.insert(tk.END, student)
    
    def itemClicked(self, selection):
        # print(f'{self.studentListbox.curselection()} foi selecionado') # (index, )
        print(f'{self.students[self.studentListbox.curselection()[0]]} foi selecionado')