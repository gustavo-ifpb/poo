import tkinter as tk
from users import UserForm

class Suap(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.form = UserForm(self)
        self.form.pack()

if __name__ == '__main__':
    app = Suap()
    app.geometry("200x200+0+0")
    app.mainloop()