from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator Using Tkinter")

root = Tk()
my_calc = Calculator(root)
root.mainloop()
