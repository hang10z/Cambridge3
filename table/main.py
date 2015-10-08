__author__ = 'demi'

# noinspection PyUnresolvedReferences

import table
from tkinter import *

# Create an instance of a window from tkinter Class
window = Tk()
window.title("MyPong")

#create an instance of the Table from the Table Class
my_table = table.Table(window, net_colour="green", vertical_net=True)
window.mainloop()


