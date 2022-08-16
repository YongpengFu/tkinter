from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("400x400")

# OptionMenu()

#this is tkinter variable to keep track what value it is corresponding to which radiobutton you clicked
var = StringVar()
#create the function whenever you click a button which is used to track Checkbutton
def show():
    #uncheck is 0, check is 1
    my_label.forget()
    my_label.configure(text = var.get())
    my_label.pack()
#create a check button
c = Checkbutton(root, text = "Check this box, I dare you!", variable = var, onvalue = "On", offvalue = "Off")
c.deselect() #deselect the button first
c.pack()

#a button to track Checkbutton
ny_button = Button(root, text = "Show Selection", command = show).pack()
my_label = Label(root, text = var.get())
root.mainloop()