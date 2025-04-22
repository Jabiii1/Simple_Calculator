from tkinter import *

mainWindow = Tk()
mainWindow.title("Simple Calculator")
mainWindow.geometry("314x414")  
mainWindow.bg("lightblue")
# Screens for calcu
screen = Entry(mainWindow, font=("Arial", 35),width=12, relief="ridge", justify="right").grid(column=1,row=1, sticky="nsew")
screen2 = Entry(mainWindow, font=("Arial", 15),width=12, relief="ridge", justify="right").grid(column=1,row=2, sticky="nsew")


# Button for calcu
erase = Button(mainWindow, text="⌫", font=("Arial", 20))
erase.place(x=220, y=105)
nine = Button(mainWindow, text="9",width=3, font=("Arial", 20))
nine.place(x=160, y=105)
eight = Button(mainWindow, text="8",width=3, font=("Arial", 20))
eight.place(x=100, y=105)
seven = Button(mainWindow, text="7",width=3, font=("Arial", 20))
seven.place(x=40, y=105)

divide = Button(mainWindow, text="÷", width=3, font=("Arial", 20))
divide.place(x=220, y=163)
six = Button(mainWindow, text="6", width=3, font=("Arial", 20))
six.place(x=160, y=163)
five = Button(mainWindow, text="5",width=3, font=("Arial", 20))
five.place(x=100, y=163)
four = Button(mainWindow, text="4",width=3, font=("Arial", 20))
four.place(x=40, y=163)

multiply = Button(mainWindow, text="x", width=3, font=("Arial", 20))
multiply.place(x=220, y=221)
three = Button(mainWindow, text="3", width=3, font=("Arial", 20))
three.place(x=160, y=221)
two = Button(mainWindow, text="2", width=3, font=("Arial", 20))
two.place(x=100, y=221)
one = Button(mainWindow, text="1", width=3, font=("Arial", 20))
one.place(x=40, y=221)

plus = Button(mainWindow, text="+", width=3, font=("Arial", 20))
plus.place(x=220, y=279)
minus = Button(mainWindow, text="-", width=3, font=("Arial", 20))
minus.place(x=160, y=279)
zero = Button(mainWindow, text="0", width=3, font=("Arial", 20))
zero.place(x=100, y=279)
dot = Button(mainWindow, text=".", width=3, font=("Arial", 20))
dot.place(x=40, y=279)

equal = Button(mainWindow, text="=", width=12, font=("Arial", 20))
equal.place(x=58, y=337)

mainWindow.mainloop()