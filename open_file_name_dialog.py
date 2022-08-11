from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
#button
def my_button():
    #•	When you create an Image object using ImageTk inside a function, 
    # #you need to define my_img as a global variable, otherwise the img wont show 
    global my_image
    #show what types file you want to who
    root.filename = filedialog.askopenfilename(initialdir = "./Image", title = "select a file", filetypes = (("jpg file", "*jpeg"),("all file", "*.*")))
    #show the returned filename
    my_label = Label(root, text = root.filename).pack()
    #show the image from this directory
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()

my_btn = Button(root, text = "Open File", command = my_button).pack()

root.mainloop()