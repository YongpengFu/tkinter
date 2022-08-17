from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("500x400")

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
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row =0, column = 0)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 30)
l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row =1, column = 0)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 30)
address_label = Label(root, text = "Address")
address_label.grid(row =2, column = 0)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 30)
city_label = Label(root, text = "City")
city_label.grid(row =3, column = 0)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 30)
state_label = Label(root, text = "State")
state_label.grid(row =4, column = 0)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 30)
zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row =5, column = 0)

#Create submit button
def submit():
        #insert the value into database
        #create a database or connect to one 
        # (you have to create a new connection inside this function, otherwise it wont work
        conn = sqlite3.connect('Addredd_book.db')
        #create a cursor
        cursor = conn.cursor()
        #insert values to the table
        cursor.execute("insert into addresses values (:f_name, :l_name, :address, :city, :state, :zipcode)",
                        {
                               'f_name':f_name.get(),
                               'l_name':l_name.get(),
                               'address':address.get(),
                               'city':city.get(),
                               'state':state.get(),
                               'zipcode':zipcode.get()
                        })
        #commit changes when you need to change the database
        conn.commit()
        #good practise to close the connection
        conn.close()

        #clear the text boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)
        
submit_btn = Button(root, text = "Add Record to Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#create a query button
def query():
        conn = sqlite3.connect('Addredd_book.db')
        #create a cursor
        cursor = conn.cursor()
        #query the database
        #oid (original ID) is primary key automatically created by sqlite3
        cursor.execute("select *, oid from addresses")
        #return all the records
        records = cursor.fetchall()
        #show the records in a label
        print_records = ''
        for record in records:
                print_records += str(record) + "\n"
        query_label = Label(root, text = print_records)
        query_label.grid(row = 8, column = 0, columnspan = 2)
        #commit changes when you need to change the database
        conn.commit()
        #good practise to close the connection
        conn.close()
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 131)



#commit changes when you need to change the database
conn.commit()

#good practise to close the connection
conn.close()

root.mainloop()