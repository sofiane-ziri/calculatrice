import tkinter
from tkinter import *

root=Tk()
root.title("calculette")
root.geometry("1100x600+100+200")
root.resizable(False,False)

input_string = ""
def add_number(number):
    global input_string
    input_string += str(number)
    echo.config(text=input_string)

def add_point(point):
    global input_string
    input_string += point
    echo.config(text=input_string)

def dele():
    global input_string
    input_string = ""
    echo.config(text=input_string)

def add():
    global input_string
    input_string += "+"
    echo.config(text=input_string)

def subtract():
    global input_string
    input_string += "-"
    echo.config(text=input_string)

def multi():
    global input_string
    input_string += "*"
    echo.config(text=input_string)

def divi():
    global input_string
    input_string += "/"
    echo.config(text=input_string)

def carre():
    global input_string
    input_string += "** 0.5"
    echo.config(text=input_string)

def calculate():
    global input_string
    result = eval(input_string)
    fichier = open("data.txt", "a")
    fichier.write("\n" + input_string + " = " + str(result))
    fichier.close
    input_string = str(result)
    echo.config(text=input_string)

def hs():
    history.config(text=open("data.txt").read())

def clear():
    fichier = open("data.txt", "w")
    history.config(text=open("data.txt").read())

echo= Label(root, text="",width=24, height=2, font=('arial', 30,))#la ou les calcule et les resultats font s'afficher
echo.grid(row=0, column=0)

history = Label(root, text="",width=24, height=5, font=('arial', 30,))
history.grid(row=1, column=1)

Button(root, text="clear", width=10, height=1, font=('arial', 30, 'bold'), command=clear).grid(row=2, column=1)

Button(root, text="1", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(1)).place(x=10, y=200)
Button(root, text="2", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(2)).place(x=150, y=200)
Button(root, text="3", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(3)).place(x=290, y=200)
Button(root, text="C", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=dele).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(4)).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(5)).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(6)).place(x=290, y=300)
Button(root, text="+", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'),command=add).place(x=430, y=300)

Button(root, text="7", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(7)).place(x=10, y=400)
Button(root, text="8", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(8)).place(x=150, y=400)
Button(root, text="9", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(9)).place(x=290, y=400)
Button(root, text="-", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=subtract).place(x=430, y=400)

Button(root, text="0", width=11, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(0)).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_point(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=calculate).place(x=430, y=500)

Button(root, text="*", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=multi).place(x=10, y=100)
Button(root, text="/", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=divi).place(x=150, y=100)
Button(root, text="HS", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=hs).place(x=290, y=100)
Button(root, text="√", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=carre).place(x=430, y=100)


root.mainloop()