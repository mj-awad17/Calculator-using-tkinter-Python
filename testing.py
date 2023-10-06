# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
root = Tk()
root.geometry("500x200")
root.title("Testing screen")
def hello(event):
    print("Single Click, Button-l")
def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

widget = Button(None, text='Mouse Clicks' ,padx=28, pady=18, font="lucida 40 bold")
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()