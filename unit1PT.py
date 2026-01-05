from tkinter import *
#need to install on all machines
from tkmacosx import Button

def save():
	pass

# Create the main window
editer = Tk()
editer.title("Enter Title Here")

#Set size of window
editer.geometry("2000x1000")

#Creates label
label = Label(editer, text='Enter Text Here',font=("Arial", 20, "bold"))

# Create buttons
save_button = Button(editer, text="Save",font=("Arial", 20, "bold"), command=save)



# Creates textbox
text_box = Text(editer,width=200,height=55)

sizeH=editer.winfo_height()
sizeW=editer.winfo_width()

label.grid(row=0,column=1,sticky='w',padx=325,pady=10)
text_box.grid(row=1,column=0,columnspan=3,padx=30)
save_button.grid(row=2,column=0,sticky='sw',padx=30)


# Start the GUI event loop
editer.mainloop()
