from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
editer = Tk()
editer.title("Enter Title Here")

#Set size of window
editer.geometry("500x500")

#Creates label
label = Label(editer, text='Enter Text Here', anchor=N,font=("Arial", 20, "bold"))

# Create buttons
save_button = Button(editer, text="Save",font=("Arial", 20, "bold"))

# Creates textbox
text_box = Text(editer,)

# # Specify Grid
# # Grid.rowconfigure(editer,0,weight=1,)
# # Grid.columnconfigure(editer,0,weight=1)

# # Grid.rowconfigure(editer,1,weight=1)

# # Place widgets in window (with pack function!)

sizeY=editer.winfo_width()

label.pack(fill='both',expand=True)
text_box.pack(fill='both',expand=True)
save_button.pack(fill='both',expand=True,padx=(0,sizeY*4))


# Start the GUI event loop
editer.mainloop()
