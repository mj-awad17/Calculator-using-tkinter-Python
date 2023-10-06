# **Calculator-using-tkinter-Python**

GUI-tkinter-Python 🧮 🐍



# **Things You Must Know**

Python provide different tools for developing GUI (Graphical User Interface). In python GUI tool-kit, tkinter is the most common used. Python with tkinter is the easiest and fastast way for creating the GUI(Graphical 

User Interface) applications. Creating a GUI using tkinter is an easy to dealing with home and busniss task.

# **Methods**

There are two main methods used:

1. Tk(screenName=None, baseName=None, className=’Tk’, useTk=1)

2. mainloop()

**Note:** User needs to remember while creating the (every project of) Python application with GUI.

**1.** To create **a main window**, tkinter offers a method: ‘Tk(screenName=None, baseName=None, className=’Tk’, useTk=1)’. 

You can change the window name according to your desired one. Basic code used for creating the main window

    tk = tkinter.tk()

Windows are the containers in which all other GUI elements live. **Widgets** are contained inside of windows such as text boxes, labels, and buttons, are known as **widgets**.

widgets have access to the specific geometry management methods

  -  pack() method:It organizes the widgets in blocks before placing in the parent widget.
  
  -  Button:To add a button in your application, this widget is used.The general syntax is:
     
          Button(master, option=value)  # master represernt the parent windoow

**2.** The name **mainloop()** is used when your application is ready to run. You have to use mainloop() due to every event to occur before the window closed. Becuse that mainloop is an infinite loop in your 

application.

# **To create a tkinter app:**

**1.**	Importing the module(tkinter)

        from tkinter import *

**note:** This module name in python 2.x ‘Tkinter’ and in Python 3.x it is ‘tkinter’

**2.**	Create the main window (container)

        # create top level window
        root = Tk()
        
      # set window title
      root.title("Calculator By mj_awad")
      
      # set window size
      root.geometry("570x590+100+200")
      
      # non-resize the calculator
      root.resizable(False,False)
      
      # background-confirmed
      root.configure(bg="#17161b")

**3.**	Add any number of widgets to the main window
      
      # buttons [0-9, + - * /]
      Button(root, text="#", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)

**4.**	Apply the event Trigger on the widgets.
      
      # display window and wait for any events
      root.mainloop()
      m.mainloop() #m is the main window object.
