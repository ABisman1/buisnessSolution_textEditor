from tkinter import *
#need to install on all machines
from tkmacosx import Button
import random

def change1():
	label1.config(text='Updated 1!')

def change2():
	label2.config(text='Updated 2!')

def change3():
	label3.config(text='Updated 3!')

def randomB():
	random.choice(things).config(text='RANDOMLY PICKED!')



# Create the main window
root = Tk()
root.title("Command & Callback Functions")

button1 = Button(root, text='Button 1!', command=change1)
button2 = Button(root, text='Button 2!', command=change2)
button3 = Button(root, text='Button 3!', command=change3)
randomButton = Button(root, text='Random Button!', command=randomB)

label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')

things = [button1, button2, button3, label1, label2, label3]

button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)
randomButton.grid(row=3,column=1)
label1.grid(row=0,column=2)
label2.grid(row=1,column=2)
label3.grid(row=2,column=2)


root.mainloop()