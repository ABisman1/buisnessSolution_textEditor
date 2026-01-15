from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title( '<title>' )

frame = Frame( window )

listbox = Listbox( frame )
listbox.insert( 1, '<filename>' )
listbox.insert( 2, '<filename>' )
listbox.insert( 3, '<filename>' )

def dialog() :
    box.showinfo( 'Selection' , 'Your Choice: ' + \
    listbox.get( listbox.curselection() ) )

btn = Button( frame, text = 'View Info', command=dialog )

btn.pack( side = RIGHT , padx = 5 )
listbox.pack( side = LEFT )
frame.pack( padx = 30, pady = 30 )

window.mainloop()