from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calc")

        # Creating screen widget
        self.screen = Text(master, state='disabled', width=30 ,height=3 ,background="black", foreground="white")
        # Position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')
        # Initialize screen value as empty
        self.equation = ''

        # Create buttons using method createButton
        b1 = self.createButton(7)
        b2 = self.


root = Tk()
my_calc = Calculator(root)
root.mainloop()
