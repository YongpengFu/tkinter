from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')

def popup():
    # messagebox.showinfo(title = 'This is my Popup.', message = 'Hello word')
    # messagebox.showwarning(title = 'This is my Popup.', message = 'Hello word')
    # messagebox.showerror(title = 'This is my Popup.', message = 'Hello word')
    # messagebox.askquestion(title = 'This is my Popup.', message = 'Hello word')
    response = messagebox.askyesno(title = 'This is my Popup.', message = 'Hello word')
    print(response) #True when you click yes
    if response:
        Label(root, text = 'You Clicked Yes!').pack()
    else:
        Label(root, text = 'You Clicked No!').pack()
#use a button to call the function
Button(root, text = 'popup', command = popup).pack()


root.mainloop()