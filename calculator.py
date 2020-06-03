#NOTES:
#because this is a very simple calculator so there are some issue 
#if you do more than one operation before hitting equal button, the result wont match

from tkinter import *

#Displaying main display
root = Tk()
root.iconbitmap("favicon.ico")
root.title("Calculator")

#Function
def insert_number(number):
    num = views.get()
    views.delete(0, END)
    views.insert(0, str(num) + str(number))
def addition():
    global operator
    global f_num
    operator = "addition"
    f_num = views.get()
    views.delete(0, END)
def substraction():
    global operator
    global f_num
    operator = "substraction"
    f_num = views.get()
    views.delete(0, END)
def multiplication():
    global operator
    global f_num
    operator = "multiplication"
    f_num = views.get()
    views.delete(0, END)
def division():
    global operator
    global f_num
    operator = "division"
    f_num = views.get()
    views.delete(0, END)
def equal():
    global l_num
    if operator == "addition":
        l_num = views.get()
        views.delete(0, END)
        views.insert(0, str(int(f_num) + int(l_num)))
    if operator == "substraction":
        l_num = views.get()
        views.delete(0, END)
        views.insert(0, str(int(f_num) - int(l_num)))
    if operator == "multiplication":
        l_num = views.get()
        views.delete(0, END)
        views.insert(0, str(int(f_num) * int(l_num)))
    if operator == "division":
        l_num = views.get()
        views.delete(0, END)
        views.insert(0, str(int(f_num) / int(l_num)))
def clear():
    views.delete(0, END)
    f_num = ""
    l_num = ""

#Declaring Widget
views = Entry(root, width = "30", borderwidth = "5")
button0 = Button(root, width = "10", text = "0", command = lambda:insert_number(0))
button1 = Button(root, width = "10", text = "1", command = lambda:insert_number(1))
button2 = Button(root, width = "10", text = "2", command = lambda:insert_number(2))
button3 = Button(root, width = "10", text = "3", command = lambda:insert_number(3))
button4 = Button(root, width = "10", text = "4", command = lambda:insert_number(4))
button5 = Button(root, width = "10", text = "5", command = lambda:insert_number(5))
button6 = Button(root, width = "10", text = "6", command = lambda:insert_number(6))
button7 = Button(root, width = "10", text = "7", command = lambda:insert_number(7))
button8 = Button(root, width = "10", text = "8", command = lambda:insert_number(8))
button9 = Button(root, width = "10", text = "9", command = lambda:insert_number(9))
out = Button(root, width = "6", text = "Quit", bg = "red", fg = "white",command = root.destroy)
plus = Button(root, width = "6", text = "+", command = addition)
substract = Button(root, width = "6", text = "-", command = substraction)
multiply = Button(root, width = "6", text = "x", command = multiplication)
divide = Button(root, width = "6", text = "/", command = division)
equal = Button(root, width = "10", text = "=", command = equal)
clear = Button(root, width = "10", text = "Clear", bg = "aqua", command = clear)

#Widget Positioning
views.grid(row = 0, column = 0, columnspan = 3)
out.grid(row = 0, column = 3)

clear.grid(row = 4, column = 0)
button0.grid(row = 4, column = 1)
equal.grid(row = 4, column = 2)
divide.grid(row = 4, column = 3)

button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
multiply.grid(row = 3, column = 3)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
substract.grid(row = 2, column = 3)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
plus.grid(row = 1, column = 3)

#Essensial Feature
root.mainloop()