#convert a png file to ico file
# from PIL import ImageTk, Image
# filen = r'/Users/yongpengfu/Desktop/icon.png'
# img = Image.open(filen)
# img.save('/Users/yongpengfu/Desktop/icon.ico',format = 'ICO', sizes=[(32,32)])

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code.')
# root.geometry('505x700')

#all the image I have
lexi1 = ImageTk.PhotoImage(Image.open('./Image/Lexi in ride.jpeg'))
lexi2 = ImageTk.PhotoImage(Image.open('./Image/Yarrning Lexi.jpeg'))
lexi3 = ImageTk.PhotoImage(Image.open('./Image/Lexi Bath.jpeg'))
# xavier = ImageTk.PhotoImage(Image.open('./Image/three month xavier.jpeg'))

image_list = [lexi1, lexi2, lexi3]

#create a status https://www.tutorialspoint.com/python/tk_label.htm
status = Label(root, text = f'Image 1 of {len(image_list)}', bd = 1, relief = SUNKEN,anchor = E, justify = LEFT)

def forward(image_num):
    global my_label
    global button_forward
    global button_back
    #when this function is called, lets get rid of the last image
    my_label.grid_forget()
    #put a new image here
    my_label = Label(image = image_list[image_num-1])
    #then I will need to update the button all over again to next image number
    button_forward = Button(root, text = '>>', command = lambda: forward(image_num+1))
    button_back = Button(root, text = '<<', command = lambda:back(image_num-1))

    #if that is the final image, disable the forward button
    if image_num == len(image_list):
        button_forward.config(state = 'disabled')
        # button_forward = Button(root, text">>", state=DISABLED)

    #put them in there, although the button is changed, their position is not changed
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    #update the status bar
    status = Label(root, text = f'Image {image_num} of {len(image_list)}', bd = 1, relief = SUNKEN,anchor = E, justify = LEFT)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = EW)

    
def back(image_num):
    global my_label
    global button_forward
    global button_back

    #when this function is called, lets get rid of the last image
    my_label.grid_forget()
    #put a new image here
    my_label = Label(image = image_list[image_num-1])
    #then I will need to update the button all over again to next image number
    button_forward = Button(root, text = '>>', command = lambda: forward(image_num+1))
    button_back = Button(root, text = '<<', command = lambda:back(image_num-1))

    #if that is the final image, disable the forward button
    #if you dont stop here, then the list will grab things from -1, -2,...
    if image_num == 1:
        button_back.config(state = 'disabled')
        # button_back = Button(root, text">>", state=DISABLED)

    #put them in there, although the button is changed, their position is not changed
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    #update the status bar
    status = Label(root, text = f'Image {image_num} of {len(image_list)}', bd = 1, relief = SUNKEN,anchor = E, justify = LEFT)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = EW)

#show image
my_label = Label(image = lexi1)
my_label.grid(row = 0, column = 0, columnspan = 3)

#create buttons
#the reason you dont need to provide a parameter for back funciton although we have image_num parameter
#because when this button is created but not clicked, the back function is not got called
button_back = Button(root, text = '<<', command = back, state = DISABLED)
button_exit = Button(root, text = 'EXIT PROGRAM', command = root.quit)
button_forward = Button(root, text = '>>', command = lambda: forward(2))
#put them in the window
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)
#put the label in the window
status.grid(row = 2, column = 0, columnspan = 3, sticky = EW)


root.mainloop()


