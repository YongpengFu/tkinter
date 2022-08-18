from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learn to code.")
root.iconbitmap('./icon.ico')
root.geometry("500x600")

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
f_name.grid(row = 0, column = 1, padx = 30, pady = (10,0))
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

#what to delete
delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)
delete_box_label = Label(root, text = 'Select ID')
delete_box_label.grid(row = 9, column = 0, pady = 5)


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
        query_label.grid(row = 12, column = 0, columnspan = 2)
        #commit changes when you need to change the database
        conn.commit()
        #good practise to close the connection
        conn.close()
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 131)

#Create function to delete a record
def delete(oid):
        #connect to the database
        conn = sqlite3.connect('Addredd_book.db')
        #create a cursor
        cursor = conn.cursor()
        #delete a record
        cursor.execute("delete from addresses where oid = :placeholder", {"placeholder": oid})
        #commit changes when you need to change the database
        conn.commit()
        #good practise to close the connection
        conn.close()
        #show records right away
        query()
delete_btn = Button(root, text = "Delete Record", command = lambda: delete(delete_box.get()))
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 131)

#create an updated button
def edit():
        editor = Tk()
        editor.title("Update A Record")
        editor.iconbitmap('./icon.ico')
        editor.geometry("400x400") 
        #crete entry widget to get data for the database
        f_name_editor = Entry(editor, width = 30)
        f_name_editor.grid(row = 0, column = 1, padx = 30, pady = (10,0))
        f_name_label_editor = Label(editor, text = "First Name")
        f_name_label_editor.grid(row =0, column = 0)

        l_name_editor = Entry(editor, width = 30)
        l_name_editor.grid(row = 1, column = 1, padx = 30)
        l_name_label_editor = Label(editor, text = "Last Name")
        l_name_label_editor.grid(row =1, column = 0)

        address_editor = Entry(editor, width = 30)
        address_editor.grid(row = 2, column = 1, padx = 30)
        address_label_editor = Label(editor, text = "Address")
        address_label_editor.grid(row =2, column = 0)

        city_editor = Entry(editor, width = 30)
        city_editor.grid(row = 3, column = 1, padx = 30)
        city_label_editor = Label(editor, text = "City")
        city_label_editor.grid(row =3, column = 0)

        state_editor = Entry(editor, width = 30)
        state_editor.grid(row = 4, column = 1, padx = 30)
        state_label_editor = Label(editor, text = "State")
        state_label_editor.grid(row =4, column = 0)

        zipcode_editor = Entry(editor, width = 30)
        zipcode_editor.grid(row = 5, column = 1, padx = 30)
        zipcode_label_editor = Label(editor, text = "Zipcode")
        zipcode_label_editor.grid(row =5, column = 0)

        #populate the contents from the ID to this new window
        conn = sqlite3.connect('Addredd_book.db')
        #create a cursor
        cursor = conn.cursor()
        #only get the record from the particular ID
        record_id = delete_box.get()
        #query the database
        #oid (original ID) is primary key automatically created by sqlite3
        cursor.execute("select * from addresses where oid = :record_id", {"record_id":record_id})
        #return all the records
        records = cursor.fetchall()
        #put the results in the entry eidget
        f_name_editor.insert(0, records[0][0])
        l_name_editor.insert(0, records[0][1])
        address_editor.insert(0, records[0][2])
        city_editor.insert(0, records[0][3])
        state_editor.insert(0, records[0][4])
        zipcode_editor.insert(0, records[0][5])

        #define save funciton
        def save():
                cursor.execute('''
                update addresses set 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                where oid = :oid
                ''', {"first":f_name_editor.get(), "last":l_name_editor.get(),
                 "address":address_editor.get(), "city": city_editor.get(), 
                 "state":state_editor.get(), "zipcode":zipcode_editor.get(),
                 "oid":record_id})
                #commit changes when you need to change the database
                conn.commit()
                #good practise to close the connection
                conn.close()
                #close the window
                editor.destroy()


        #create a save button

        edit_btn = Button(editor, text = "Save Record", command = save)
        edit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 139)

edit_btn = Button(root, text = "Edit Record", command = edit)
edit_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 139)

#commit changes when you need to change the database
conn.commit()

#good practise to close the connection
conn.close()

root.mainloop()