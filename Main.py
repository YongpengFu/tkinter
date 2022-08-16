from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("400x400")

#create a database or connect to one
conn = sqlite3.connect('Addredd_book.db')
#create a cursor
cursor = conn.cursor()
#create table
cursor.execute('''create table if not exists addresses (first_name text,
                                        last_name text,
                                        address text,
                                        city text,
                                        state text,
                                        zipcode integer)
                                ''')

#crete entry widget to get data for the database
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 30)
f_name_label = Lable(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 30)
address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 30)
city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 30)
state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 30)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 30)


#commit changes when you need to change the database
conn.commit()

#good practise to close the connection
conn.close()

root.mainloop()