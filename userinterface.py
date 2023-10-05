from tkinter import *
from tkinter import ttk

class userinterface:

    def __init__(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.startInterface()
    def startInterface(self):
        self.root.geometry("700x350")
        self.frame.grid()
        ttk.Label(self.frame, text="Hello World!").grid(column=0, row=0)
        ttk.Button(self.frame, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        self.root.mainloop()
        print("start")

userinterface()