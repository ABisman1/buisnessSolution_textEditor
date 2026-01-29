from tkinter import *
#need to install on all machines
from tkmacosx import Button
import os
import tkinter.messagebox as box

global name 
name = ""
newfile=True

def edit():

	def save():
			text = text_box.get('1.0',END)
			with open("Notes/"+name+".txt", "w") as f:
				f.write(text)
			editer.destroy()

	editer = Toplevel(root)
	editer.geometry("2000x1000")
	editer.title(name)
	enter.delete(0,END)

	#Creates label
	label = Label(editer, text='Enter Text Here',font=("Arial", 20, "bold"))

	# Create buttons
	save_button = Button(editer, text="Save",font=("Arial", 20, "bold"), command=save)

	# Creates textbox
	text_box = Text(editer,width=200,height=55)

	if newfile==False:
		with open(selected, "r") as f:
			content = f.read()
			text_box.insert('1.0', content)

	label.grid(row=0,column=1,sticky='w',padx=325,pady=10)
	text_box.grid(row=1,column=0,columnspan=3,padx=30)
	save_button.grid(row=2,column=0,sticky='sw',padx=30)


	# Start the GUI event loop
	editer.mainloop()

def new():
	newfile=True
	name = enter.get()
	print(name)
	#if name != "":
	edit()
	

def view():
	newfile=False
	edit()

# Create the main window
root = Tk()
root.title("Home")

#Set size of window
root.geometry("2000x1000")

# Create buttons
new_button = Button(root, text="Open New File", font=("Arial", 20, "bold"),height=40,width=175,command=new)
view_button = Button(root, text="View Files",font=("Arial", 20, "bold"),height=40,width=175,command=view)

enter=Entry(root)
listOfFiles = [os.listdir("Notes")]
frame = Frame(root)
opener=Listbox(frame)
for i in range(0, len(listOfFiles)):
	opener.insert(i,listOfFiles[i])
selected=opener.curselection()
#opener.insert(1,"one")
#opener.insert(2,"two")


#Add a label
label = Label(root, text="Welcome to Note Taker",font=("Arial", 20, "bold"))
label_1 = Label(root, text="Select to Continue",font=("Arial", 20, "bold"))
label_2 = Label(root, text="Enter Name of Notes Here")
label_3 = Label(root, text="Selet File you Want to Open")

# Place widgets in window (with pack function!)
new_button.grid(row=4,column=0,padx=200)
label.grid(row=0,column=1,padx=47,pady=50)
view_button.grid(row=4,column=2,padx=200,pady=150)
label_1.grid(row=1,column=1,pady=25)
label_2.grid(row=2,column=0)
label_3.grid(row=2,column=2)
enter.grid(row=3, column=0)
frame.grid(row=3,column=2)
opener.pack()

# Start the GUI event loop
root.mainloop()
