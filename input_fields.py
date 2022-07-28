from tkinter import *

root = Tk()

input_info = Entry(root, width = 50, bg = 'black', fg = 'white', borderwidth = 10)
input_info.pack()
#give some default text in the entry widget already
input_info.insert(0, "Enter your name here.")


#define a function to use inside a button
def myClick():
    hello = "Hello " + input_info.get()
    myLabel = Label(root, text = hello, fg = 'red', bg = 'yellow')
    myLabel.pack()

# myButton = Button(root, text = 'Click me!', state = DISABLED)
# myButton.pack()
myButton1 = Button(root, text = 'Hello Button', padx = 5, pady = 5, command = myClick, fg = 'blue')
myButton1.pack()


root.mainloop()

