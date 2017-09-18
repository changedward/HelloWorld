#TKINTER GUI PYTHON PROGRAMMING: https://www.youtube.com/watch?v=-tbWoZSi3LU
''' TK is a cross-platform GUI toolkit providing widgets. TKINTER specifically deals with python interface. '''

#test if tkinter works
#####import tkinter
#####tkinter._test()

#modules
''' A module is a file containing Python definitions and statements.
The file name is the module name with the suffix .py appended.
Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
Using the module name you can access the functions.
If you intend to use a function often you can assign it to a local name:
>>> fib = fibo.fib '''
#thus, we have access to a Python file name called ttk which we will use to access some GUI functions that are
#already defined in there.
from tkinter import *
from tkinter import ttk

#it is common that the variable is called root when making the actual window for the GUI in Python.
root = Tk()
#create title
root.title("GUI")
#create a button in root with text "Hello World!" and grid() is for simple layout manager
#####ttk.Button(root, text="Hello World!").grid()
#keep GUI running constantly
root.mainloop()

''' SOME OF THE DIFFERENT WIDGETS: Button, Label, Canvas, Menu, Text, Scale, OptionMenu, Frame, CheckButton,
LabelFrame, MenuButton, PanedWindow, Entry, ListBox, Message, RadioButton, ScrollBar, Bitmap, SpinBox, Image'''

#frame is a widget that surround other widgets
frame = Frame(root)

#using TKINTERVARIABLE to change text on our label
labelText = StringVar()

#create label and button
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click me!")

#set lable text to something else
labelText.set("My label!")

#aligning widgets automatically
label.pack()
button.pack()
frame.pack()

#LAST CALLING, ERROR ON CODE AND 6:10 IN VIDEO