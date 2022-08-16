from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
#the padding here is the inside the frame
frame = LabelFrame(root, text = 'This is my frame...', padx = 50, pady = 50)
#this padding here is the outside of the frame
frame.pack(padx = 10, pady = 10)
#put the button 
b = Button(frame, text = "don't click here")
b2 = Button(frame, text = "or here")
b.grid(row = 0, column = 0)
b2.grid(row=1, column = 1)



root.mainloop()