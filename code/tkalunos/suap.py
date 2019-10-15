import tkinter as tk
from student import StudentForm, StudentsList

class Suap(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # self.screen = StudentForm(self)
        self.screen = StudentsList(self)
        self.screen.pack(fill=tk.BOTH, padx=10, pady=5)

if __name__ == '__main__':
    app = Suap()
    # app.geometry("200x200+100+300")
    app.mainloop()