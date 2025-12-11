from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
editer = Tk()
editer.title("Enter Title Here")

#Set size of window
editer.geometry("300x150")

#Creates label
label = Label(editer, text='Enter Text Here')

# Create buttons
save_button = Button(editer, text="Save")

# Creates textbox
text_box = Text(editer,)

# Specify Grid
Grid.rowconfigure(editer,0,weight=1)
Grid.columnconfigure(editer,0,weight=1)

Grid.rowconfigure(editer,1,weight=1)

# Place widgets in window (with pack function!)

save_button.grid(row=2,column=0,sticky='SW')
text_box.grid(row=1,column=0, columnspan=3,sticky='NSEW')
label.grid(row=0,column=1,sticky='N')

# Start the GUI event loop
editer.mainloop()