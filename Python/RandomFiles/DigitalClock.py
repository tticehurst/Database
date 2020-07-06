import tkinter
import time

root = Tk()
root.title('Clock')

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')

lbl.pack(anchor = 'center')
time()
mainloop()
