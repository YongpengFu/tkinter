from tkinter import *

root = Tk()

#define a function to use inside a button
def myClick():
    myLabel = Label(root, text = "Look! I clicked a button!", fg = 'red', bg = 'yellow')
    myLabel.pack()

# myButton = Button(root, text = 'Click me!', state = DISABLED)
# myButton.pack()
myButton1 = Button(root, text = 'Click me!', padx = 50, pady = 50, command = myClick, fg = 'blue')
myButton1.pack()


root.mainloop()

