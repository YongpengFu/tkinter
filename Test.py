# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Add a new Frame
f1=Frame(win, background="bisque", width=10, height=100)
f2=Frame(win, background="blue", width=10, height=100)

# Add weight property to span the widget in remaining space
f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")

win.columnconfigure(0, weight=1)
win.rowconfigure(1, weight=0)

win.mainloop()

def test_finally(arg1, **kargs):
    import os
    try:
        print ("this is try block")
        if('name' in kargs):
            print(kargs['name'])
        else:
            print("no name" + arg1)
    except:
        print("this is except block")
    finally:
        print("this is finally block")
print(test_finally('namename'))