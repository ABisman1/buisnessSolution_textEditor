from tkinter import *
#need to install on all machines
from tkmacosx import Button

def writeF():
	text = text_box.get('1.0',END)
	with open("Notes/"name+".txt", "w") as f:
		f.write(text)
		print("You entered: ")
		print(text)

def readF():
	with open("Notes/"name+".txt", "r") as f:
		content = f.read()
		print(content)
		text_box.insert('1.0', content)


root = Tk()
root.title("Reading & Writing Files")

text_box = Text(root)

write = Button(root, text='Write To File', command=writeF)
readB = Button(root, text='Read From File', command=readF)

text_box.pack()
write.pack()
readB.pack()

root.mainloop()