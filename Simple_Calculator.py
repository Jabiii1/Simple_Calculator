from tkinter import *

def inClick(value):
    screen_var.set(screen_var.get() + str(value))

def clearLatest():
    current = screen_var.get()
    screen_var.set(current[:-1])
    
def clearAll():
    screen_var.set("")
    screen2_var.set("")

def calculate():
    try:
        expression = screen_var.get().replace("×", "*").replace("÷", "/").replace("%", "/100")
        result = eval(expression)
        screen2_var.set(result)
    except:
        screen2_var.set("Error")

mainWindow = Tk()
mainWindow.title("Simple Calculator")
mainWindow.geometry("314x415")  
mainWindow.configure(bg="grey")
mainWindow.resizable(False, False)

# Screen variables
screen_var = StringVar()
screen2_var = StringVar()

# Screens for calcu
screen = Entry(mainWindow, textvariable=screen_var, font=("Arial", 35),width=12, relief="ridge", justify="right")
screen.grid(column=1,row=1, sticky="nsew")
screen2 = Entry(mainWindow, textvariable=screen2_var, font=("Arial", 15),width=12, relief="ridge", justify="right")
screen2.grid(column=1,row=2, sticky="nsew")

icon = PhotoImage(file= "calc.png")    
mainWindow.iconphoto(False, icon)

# Buttons for calcu

#First Group
Button(mainWindow, text="÷",width=3, font=("Arial", 20), command=lambda: inClick("÷")).place(x=220, y=105)
Button(mainWindow, text="%",width=3, font=("Arial", 20), command=lambda: inClick("%")).place(x=160, y=105)
Button(mainWindow, text="⌦",width=3, font=("Arial", 20), command=lambda: clearLatest()).place(x=100, y=105)
Button(mainWindow, text="C", width=3, font=("Arial", 20), command=lambda: clearAll()).place(x=40, y=105)

# Second Goup
Button(mainWindow, text="×",width=3, font=("Arial", 20), command=lambda: inClick("×")).place(x=220, y=163)
Button(mainWindow, text="9",width=3, font=("Arial", 20), command=lambda: inClick("9")).place(x=160, y=163)
Button(mainWindow, text="8",width=3, font=("Arial", 20), command=lambda: inClick("8")).place(x=100, y=163)
Button(mainWindow, text="7",width=3, font=("Arial", 20), command=lambda: inClick("7")).place(x=40, y=163)

# Third Group
Button(mainWindow, text="-", width=3, font=("Arial", 20), command=lambda: inClick("-")).place(x=220, y=221)
Button(mainWindow, text="6", width=3, font=("Arial", 20), command=lambda: inClick("6")).place(x=160, y=221)
Button(mainWindow, text="5",width=3, font=("Arial", 20), command=lambda: inClick("5")).place(x=100, y=221)
Button(mainWindow, text="4",width=3, font=("Arial", 20), command=lambda: inClick("4")).place(x=40, y=221)

# Fourth Group
Button(mainWindow, text="+", width=3, font=("Arial", 20), command=lambda: inClick("+")).place(x=220, y=279)
Button(mainWindow, text="3", width=3, font=("Arial", 20), command=lambda: inClick("3")).place(x=160, y=279)
Button(mainWindow, text="2", width=3, font=("Arial", 20), command=lambda: inClick("2")).place(x=100, y=279)
Button(mainWindow, text="1", width=3, font=("Arial", 20), command=lambda: inClick("1")).place(x=40, y=279)

# Fourth Group
Button(mainWindow, text="=", width=3, font=("Arial", 20), command= calculate).place(x=220, y=337)
Button(mainWindow, text=".", width=3, font=("Arial", 20), command=lambda: inClick(".")).place(x=160, y=337)
Button(mainWindow, text="0", width=3, font=("Arial", 20), command=lambda: inClick("0")).place(x=100, y=337)
Button(mainWindow, text="00", width=3, font=("Arial", 20), command=lambda: inClick("00")).place(x=40, y=337)

mainWindow.mainloop()