from tkinter import *

root = Tk()
#create a label and put this in to the root window
myLabel1 = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = 'My name is Yong')
myLabel3 = Label(root, text = '             ')



#put the label in the grid
myLabel1.grid(row =0, column = 0)
#the number here is relative, so 5 is essentially the same as 2
#tkinter ignores 3,4 basically
myLabel2.grid(row =1, column = 5)
myLabel3.grid(row =1, column = 1)



#eventloop: so that the application is aware where your mouse is
#this loop ends when you close the program
root.mainloop()

