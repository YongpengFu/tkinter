from tkinter import *

root = Tk()
#create a label and put this in to the root window
myLabel = Label(root, text = 'Hello World!')
#put this label on the window
#packing is like shoving it in there at the first available spot
myLabel.pack()
#eventloop: so that the application is aware where your mouse is
#this loop ends when you close the program
root.mainloop()



