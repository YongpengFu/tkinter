from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')

#when you click a button what will happen
def open():
    #you need to define my_img as a global variable, otherwise the img wont show
    #this only has to be done when you are openning a second window
    #on the root window you dont need to define global
    global my_img
    #open a new window
    top = Toplevel(root)
    top.title("A new window")
    #create a label inside this new window
    lbl = Label(top, text = "Hello World!").pack()
    #put an image in there
    my_img = ImageTk.PhotoImage(Image.open('./Image/Lexi Bath.jpeg'))
    my_label = Label(top, image = my_img).pack()
    #create a button to close the second window
    btn2 = Button(top, text = 'close window',command = top.destroy).pack()
    #disable the underlying window when a second window pops up
    top.wait_visibility()
    top.grab_set_global()

#create a button to control when to open a second window
btn = Button(root, text = 'Open Second Window', command = open).pack()

root.mainloop()