from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Home")

#Set size of window
root.geometry("2000x1000")

# Create buttons
new_button = Button(root, text="Open New File", font=("Arial", 20, "bold"))
view_button = Button(root, text="View Files",font=("Arial", 20, "bold"))

#Add a label
label = Label(root, text="Welcome to Note Taker")
label_1 = Label(root, text="Select to Continue")

# Place widgets in window (with pack function!)
new_button.grid(row=2,column=0)
label.grid(row=0,column=1)
view_button.grid(row=2,column=2,sticky=)
label_1.grid(row=1,column=1)

# Start the GUI event loop
root.mainloop()
