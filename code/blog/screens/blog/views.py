import tkinter as tk
import psycopg2.extras

class PeopleForm(tk.Frame):

    result = []

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        # Listbox
        self.listBox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listBox.bind('<<ListboxSelect>>', self.itemClicked)
        self.listBox.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)

        self.showAllUsers()

    def showAllUsers(self):
        cur = self.parent.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM "user"')
        
        self.result = cur.fetchall()
        
        cur.close()

        # Apagar lista de nomes
        self.listBox.delete(0, tk.END)

        for i, people in enumerate(self.result):
            self.listBox.insert(i, people['name'])

    def itemClicked(self, event):
        widget = event.widget
        self.parent.switchScreen(PeopleView(self.parent, self.result[self.listBox.curselection()[0]]))
        self.destroy()

class PeopleView(tk.Frame):

    def __init__(self, parent, people):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        # Entry
        self.nameEntry = tk.Label(self, text=f'Nome: {people["name"]}')
        self.nameEntry.grid(row=0, column=0)

        self.nameEntry = tk.Label(self, text=f'Senha: {people["password"]}')
        self.nameEntry.grid(row=1, column=0)

        # Button
        self.backButton = tk.Button(self, text='Voltar', command = self.back)
        self.backButton.grid(row=2, column=0)

    def back(self):
        self.parent.switchScreen(PeopleForm(self.parent))
        self.destroy()

        
