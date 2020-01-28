import tkinter as tk
import psycopg2

from screens.blog.views import PeopleForm

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Modifica o tamanho da janela
        self.geometry('270x200+10+100')

        # Atualizar o título da janela
        self.title('Blog')

        # Conectar ao banco de dados
        self.db = psycopg2.connect('dbname=blog user=guga password=gugasv host=127.0.0.1')

        # Hello world
        hello = PeopleForm(self)
        hello.pack(fill=tk.BOTH)
    
    def switchScreen(self, screen):
        screen.pack()
        screen.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()