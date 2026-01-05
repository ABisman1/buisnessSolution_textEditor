from tkinter import *
#need to install on all machines
from tkmacosx import Button

def new():
	open('unit1PT.py')

def view():
	pass

# Create the main window
root = Tk()
root.title("Home")

#Set size of window
root.geometry("2000x1000")

# Create buttons
new_button = Button(root, text="Open New File", font=("Arial", 20, "bold"),height=40,width=175,command=new)
view_button = Button(root, text="View Files",font=("Arial", 20, "bold"),height=40,width=175,command=view)

#Add a label
label = Label(root, text="Welcome to Note Taker",font=("Arial", 20, "bold"))
label_1 = Label(root, text="Select to Continue",font=("Arial", 20, "bold"))

# Place widgets in window (with pack function!)
new_button.grid(row=2,column=0,padx=200)
label.grid(row=0,column=1,padx=47,pady=50)
view_button.grid(row=2,column=2,padx=200,pady=150)
label_1.grid(row=1,column=1,pady=25)

# Start the GUI event loop
root.mainloop()
