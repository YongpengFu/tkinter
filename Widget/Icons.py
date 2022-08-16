#convert a png file to ico file
# from PIL import ImageTk, Image
# filen = r'/Users/yongpengfu/Desktop/icon.png'
# img = Image.open(filen)
# img.save('/Users/yongpengfu/Desktop/icon.ico',format = 'ICO', sizes=[(32,32)])

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code.')
root.geometry('600x400')
#icon
root.iconbitmap('./icon.ico')
#button quit
button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()
#show image
my_img = ImageTk.PhotoImage(Image.open('image.png'))
my_label = Label(root, image = my_img)
my_label.pack()

root.mainloop()


