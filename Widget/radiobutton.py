from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')

#this is tkinter variable to keep track what value it is corresponding to which radiobutton you clicked
r = StringVar() #because i know I am using integer, I am using IntVar
r.set("2")
Radiobutton(root, text = "Option 1", variable = r, value = "11", command = lambda: clicked(r.get())).pack()
Radiobutton(root, text = "Option 2", variable = r, value = "21", command = lambda: clicked(r.get())).pack()
#test when you click a button, my label get changed
def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text = r.get())
    myLabel.pack()
#show the value of a radio in a label
myLabel = Label(root, text = r.get())
myLabel.pack()

root.mainloop()