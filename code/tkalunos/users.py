import tkinter as tk

class UserForm(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        title = tk.Label(self, text="IFPB")
        # title.place(x=50, y=50)
        # title.grid(row=0, column=0)
        title.pack()

        subtitle = tk.Entry(self, text="Cajazeiras")
        # subtitle.place(x=50, y=50)
        # subtitle.grid(row=1, column=0)
        subtitle.pack()

        button = tk.Button(self, text="Eita!")
        button.pack()