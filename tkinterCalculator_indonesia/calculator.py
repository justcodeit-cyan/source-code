from tkinter import *

root = Tk()
root.iconbitmap("profile.png")
root.title("Kalkulator Sederhana")

operasi = 0
def insertnumber(number):
    num = views.get()
    views.delete(0, END)
    views.insert(0, str(num) + str(number))

def tambah():
    global operasi
    global f_num
    global status
    operasi += 1
    status = "pertambahan"
    if operasi > 1:
        l_num = views.get()
        f_num = str(int(f_num) + int(l_num))
    else:
        f_num = views.get()
    views.delete(0, END)

def kurang():
    global operasi
    global f_num
    global status
    status = "pengurangan"
    f_num = views.get()
    views.delete(0, END)
    operasi += 1

def perkalian():
    global f_num
    global status
    global operasi
    status = "perkalian"
    f_num = views.get()
    views.delete(0, END)
    operasi += 1

def pembagian():
    global f_num
    global status
    global operasi
    status = "pembagian"
    f_num = views.get()
    views.delete(0, END)
    operasi += 1

def equal():
    global operasi
    l_num = views.get()
    views.delete(0, END)
    if status == "pertambahan":
        views.insert(0, str(int(f_num) + int(l_num)))
    if status == "pengurangan":
        views.insert(0, str(int(f_num) - int(l_num)))
    if status == "perkalian":
        views.insert(0, str(int(f_num) * int(l_num)))
    if status == "pembagian":
        views.insert(0, str(int(f_num) / int(l_num)))
    operasi = 0

def clear():
    global f_num
    global status
    global operasi
    views.delete(0, END)
    f_num = ""
    status = ""
    operasi = 0

views = Entry(root, width = "30", borderwidth = "5")
button0 = Button(root, width = "10", text = "0", command = lambda:insertnumber(0))
button1 = Button(root, width = "10", text = "1", command = lambda:insertnumber(1))
button2 = Button(root, width = "10", text = "2", command = lambda:insertnumber(2))
button3 = Button(root, width = "10", text = "3", command = lambda:insertnumber(3))
button4 = Button(root, width = "10", text = "4", command = lambda:insertnumber(4))
button5 = Button(root, width = "10", text = "5", command = lambda:insertnumber(5))
button6 = Button(root, width = "10", text = "6", command = lambda:insertnumber(6))
button7 = Button(root, width = "10", text = "7", command = lambda:insertnumber(7))
button8 = Button(root, width = "10", text = "8", command = lambda:insertnumber(8))
button9 = Button(root, width = "10", text = "9", command = lambda:insertnumber(9))
out = Button(root, width = "6", text = "Quit", bg = "red", fg = "white", command = root.destroy)
tambah = Button(root, width = "6", text = "+",bg = "gray", fg = "white", command = tambah)
kurang = Button(root, width = "6", text = "-", bg = "gray", fg = "white", command = kurang)
kali = Button(root, width = "6", text = "x", bg = "gray", fg = "white", command = perkalian)
bagi = Button(root, width = "6", text = "/", bg = "gray", fg = "white",command = pembagian)
clear = Button(root, width = "10", text = "C", bg = "aqua", command = clear)
equal = Button(root, width = "10", text = "=", bg = "gray", fg = "white", command = equal)


views.grid(row = 0, column = 0, columnspan = 3)
out.grid(row = 0, column = 3)

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
tambah.grid(row = 1,column = 3)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
kurang.grid(row = 2, column = 3)

button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
kali.grid(row = 3, column = 3)

clear.grid(row = 4, column = 0)
button0.grid(row = 4, column = 1)
equal.grid(row = 4, column = 2)
bagi.grid(row = 4, column = 3)

root.mainloop()