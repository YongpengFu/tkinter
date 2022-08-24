from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")


#from where and to where
vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

def slide(var):
    #change the label text whenever you click this button
    my_label['text'] = horizontal.get()
    #we can change the geometry of the root window
    root.geometry(str(horizontal.get())+"x400")

#in case you want to the window dynamic change when you move the slide, you can use command = slide,
#but in the slide funciton, you have to have (var[or whatever]) to make it work
horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL, command = slide)
horizontal.pack()

#we can get a number to represent where the slide is
my_label = Label(root, text = horizontal.get())
my_label.pack()
#every time we press the button we will update the label

my_btn = Button(root, text = "click me!", command = slide).pack()

root.mainloop()

