from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Command & Callback Functions")

button1 = Button(root, text='Change Title', command=changeTitle)
T = Text(root, height = 5, width = 52)

def changeTitle():
	root.title(T.get('1.0',END))

