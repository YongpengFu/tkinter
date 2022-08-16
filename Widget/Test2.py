# # Import the required libraries
# from tkinter import *

# # Create an instance of tkinter frame or window
# root=Tk()

# # Set the size of the window
# root.geometry("700x350")

# #when you click a button what will happen
# def open():
#     #open a new window
#     top = Toplevel(root)
#     top.title("Credential Window")
#     top.geometry("350x250")
#     #username label
#     user_label = Label(top, text = "USERNAME:", pady = 50, padx = 5)
#     user_label.grid(row = 0, column = 0)
#     user_entry = Entry(top, bd = 3, width = 20)
#     user_entry.grid(row = 0, column = 1)
#     #password label
#     pass_label = Label(top, text = "PASSWORD:", pady = 20, padx = 5)
#     pass_label.grid(row = 1, column = 0)
#     pass_entry = Entry(top, bd = 3,width = 20, show = "*")
#     pass_entry.grid(row = 1, column = 1)
#     #

#     #disable the underlying window when a second window pops up
#     top.wait_visibility()
#     top.grab_set_global()

# #create a button to control when to open a second window
# btn = Button(root, text = 'Open Second Window', command = open).pack()


# root.mainloop()

# class Count(object):
    
#     def __init__(self,mymin,mymax):
#         self.mymin=mymin
#         self.mymax=mymax
#         self.current=None

#     def __getattr__(self, item):
#             self.__dict__[item]=1
#             return 0

#     def __getattribute__(self, item):
#         if item.startswith('cur'):
#             raise AttributeError
#         return object.__getattribute__(self,item)
#         # or you can use ---return super().__getattribute__(item)
#         # note this class subclass object

# obj1 = Count(1,10)
# print(obj1.mymin)
# print(obj1.mymax)
# print(obj1.current)
# print(obj1.item)

import threading

class Example(threading.Thread):

    def run(self):
        print ('%s from %s' % (self._Thread__kwargs['example'],
                              self.name))

example = Example(kwargs={'example': 'Hello World'})
example.start()
example.join()