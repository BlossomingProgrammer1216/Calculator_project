# import statements
from tkinter import *

# App Setup
root = Tk()
root.title("Your Calculator")
root.geometry("750x500")
l = Label(root, text="Your Calculator")
l.grid(row=1, column=0, columnspan=10)
e = Entry(root, borderwidth=5, width=64)
e.grid(row=2, column=0, columnspan=10, padx=171, pady=10)


# Command Functions

def onclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global math
    math = "subtraction"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global math
    math = "multiplication"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def divide():
    first_number = e.get()
    global math
    math = "division"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def square():
    first_number = e.get()
    global math
    math = "square"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, f_num ** 2)

def cube():
    first_number = e.get()
    global math
    math = "cube"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, f_num ** 3)

def raise_power():
    first_number = e.get()
    global math
    math = "raise power"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "raise power":
        e.insert(0, f_num ** int(second_number))

# Declaring button one-zero
one = Button(root, text="1", command=lambda: onclick(1), bg="#909090")
two = Button(root, text="2", command=lambda: onclick(2), bg="#909090")
three = Button(root, text="3", command=lambda: onclick(3), bg="#909090")
four = Button(root, text="4", command=lambda: onclick(4), bg="#909090")
five = Button(root, text="5", command=lambda: onclick(5), bg="#909090")
six = Button(root, text="6", command=lambda: onclick(6), bg="#909090")
seven = Button(root, text="7", command=lambda: onclick(7), bg="#909090")
eight = Button(root, text="8", command=lambda: onclick(8), bg="#909090")
nine = Button(root, text="9", command=lambda: onclick(9), bg="#909090")
zero = Button(root, text="0", command=lambda: onclick(0), bg="#909090")

# Necessary Functions
equal = Button(root, text="=", command=equal, bg="#909090")
clear = Button(root, text="Clear", command=clear, bg="#ffb347")
multiply = Button(root, text="*", command=multiply, bg="#909090")
divide = Button(root, text="/", command=divide, bg="#ffb347")
add = Button(root, text="+", command=add, bg="#909090")
subtract = Button(root, text="-", command=subtract, bg="#ffb347")

# Special Functions
sqr = Button(root, text="Square", command=square, bg="#ffb347")
cub = Button(root, text="Cube", command=cube, bg="#ffb347")
power = Button(root, text="Raise Power", command=raise_power, bg="#ffb347")
# Initiate all the buttons
one.grid(columnspan=1, column=5, rowspan=1, row=40, ipadx=40, ipady=40)
two.grid(column=6, columnspan=1, rowspan=1, row=40, ipadx=40, ipady=40, padx=4)
three.grid(column=7, columnspan=1, rowspan=1, row=40, ipadx=40, ipady=40)
four.grid(column=5, columnspan=1, rowspan=1, row=50, ipadx=40, ipady=40, pady=4)
five.grid(column=6, columnspan=1, rowspan=1, row=50, ipadx=40, ipady=40)
six.grid(column=7, columnspan=1, rowspan=1, row=50, ipadx=40, ipady=40, padx=4)
seven.grid(column=6, columnspan=1, rowspan=1, row=60, ipadx=40, ipady=40, padx=4)
eight.grid(column=5, columnspan=1, rowspan=1, row=60, ipadx=40, ipady=40, padx=4)
nine.grid(column=7, columnspan=1, rowspan=1, row=60, ipadx=40, ipady=40, padx=4)
zero.grid(column=5, columnspan=3, rowspan=1, row=70, ipadx=100, ipady=40, padx=1)
equal.grid(column=8, columnspan=1, rowspan=54, row=60, ipadx=50, ipady=100, padx=10)
add.grid(column=8, columnspan=1, rowspan=54, row=10, ipadx=50, ipady=20, padx=10)
subtract.grid(column=8, columnspan=1, rowspan=54, row=22, ipadx=50, ipady=20, padx=10)
multiply.grid(column=8, columnspan=1, rowspan=30, row=17, ipadx=50, ipady=20, padx=10)
divide.grid(column=8, columnspan=1, rowspan=40, row=17, ipadx=50, ipady=20, padx=10)
sqr.grid(column=5, columnspan=1, rowspan=1, row=70, ipadx=21, ipady=40)
cub.grid(column=7, columnspan=1, rowspan=1, row=70, ipadx=30, ipady=40)
clear.grid(column=1, columnspan=1, rowspan=1, row=60, ipadx=40, ipady=50, padx=1)
power.grid(column=1, columnspan=1, rowspan=1, row=40, ipadx=40, ipady=50, padx=1)

# run the app
root.mainloop()