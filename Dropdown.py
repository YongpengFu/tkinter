from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("400x400")

#values in the dropdown list

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#Clicked is the one selected
clicked = StringVar() #tkinter variable
clicked.set(options[0]) #set the default value
drop = OptionMenu(root, clicked, *options)
drop.pack()

#you can access to the value of the dropdown value
def show():
    my_label = Label(root, text = clicked.get()).pack()
my_button = Button(root, text = "Show Selection", command = show).pack()


root.mainloop()