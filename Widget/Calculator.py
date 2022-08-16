from tkinter import *

root = Tk()
#Change the title of the window
root.title("Simple Calculator")
#create the entry widget
e = Entry(root, width = 35, borderwidth = 3)
    # underneath of this column will have 3 columns
e.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
#define arry to hold the input value`````````````
input_array = []

#show the number when you click a button
def button_click(number):
    #end populate the number (Insert STRING at INDEX.)
    #we need to insert the number plus whatever's already in there
    current = e.get()
    #after you get the current value, you can delete it
    e.delete(0, END)
    #make sure you are concatenate two strings to display
    e.insert(0, str(current) + str(number))
#clear out the entry widget when you click clear button
def button_clear():
    e.delete(0,END)


#define what button add will do
#what it will do is to remember the number its shown now and then delete it in the display when you click this button
def button_add():
    first_number = e.get()
    #the reason you define this as a global so that you can use this vaiable outside of this function
    global f_num
    global input_array
    #give an indicator
    global math
    math = 'addition'
    f_num = int(first_number)
    input_array.append(f_num)
    e.delete(0, END)
#define button_substrate
def button_substrate_real():
    first_number = e.get()
    #the reason you define this as a global so that you can use this vaiable outside of this function
    global f_num
    #give an indicator
    global math
    math = 'substration'
    f_num = int(first_number)
    e.delete(0, END)
#define button_substrate
def button_multiply():
    first_number = e.get()
    #the reason you define this as a global so that you can use this vaiable outside of this function
    global f_num
    #give an indicator
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)
#define button_substrate
def button_divide():
    first_number = e.get()
    #the reason you define this as a global so that you can use this vaiable outside of this function
    global f_num
    #give an indicator
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0, END)

#define what equal button will do
def button_equal():
    #get the current number
    second_number = e.get()
    print(second_number == '')
    input_array.append(int(second_number))
    #just to make sure everything is cleared out
    e.delete(0, END)
    if math == 'addition':
        if len(input_array) == 2:
            e.insert(0, input_array[0] + input_array[1])
        else:
            e.insert(0, input_array[1] + input_array[-1])
    if math == 'substration':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / float(second_number))


#we will create button for each number
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
button_equal = Button(root, text = "=", padx = 100, pady = 20, command = button_equal)
button_clear = Button(root, text = "Clear", padx = 89, pady = 20, command = button_clear)
#add a few more operator
button_substrate = Button(root, text = "-", padx = 40, pady = 20, command = button_substrate_real)
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = button_multiply)
button_divide = Button(root, text = "÷", padx = 40, pady = 20, command = button_divide)




#put the button on the screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
button0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)
#put the extra operator in the window
button_substrate.grid(row=6, column = 0)
button_multiply.grid(row=6, column = 1)
button_divide.grid(row=6, column = 2)


root.mainloop()

