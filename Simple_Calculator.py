from tkinter import *

def button_click(value):
    screen_var.set(screen_var.get() + str(value))

def clear():
    current = screen_var.get()
    screen_var.set(current[:-1])

def calculate():
    try:
        expression = screen_var.get().replace("x", "*").replace("÷", "/")
        result = eval(expression)
        screen2_var.set(result)
    except:
        screen2_var.set("Error")

mainWindow = Tk()
mainWindow.title("Simple Calculator")
mainWindow.geometry("314x415")  
mainWindow.configure(bg="grey")

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
Button(mainWindow, text="⌫", font=("Arial", 20), command=lambda: clear).place(x=220, y=105)
Button(mainWindow, text="9",width=3, font=("Arial", 20), command=lambda: button_click("9")).place(x=160, y=105)
Button(mainWindow, text="8",width=3, font=("Arial", 20), command=lambda: button_click("8")).place(x=100, y=105)
Button(mainWindow, text="7",width=3, font=("Arial", 20), command=lambda: button_click("7")).place(x=40, y=105)

# Second Goup
Button(mainWindow, text="÷", width=3, font=("Arial", 20), command=lambda: button_click("÷")).place(x=220, y=163)
Button(mainWindow, text="6", width=3, font=("Arial", 20), command=lambda: button_click("6")).place(x=160, y=163)
Button(mainWindow, text="5",width=3, font=("Arial", 20), command=lambda: button_click("5")).place(x=100, y=163)
Button(mainWindow, text="4",width=3, font=("Arial", 20), command=lambda: button_click("4")).place(x=40, y=163)

# Third Group
Button(mainWindow, text="x", width=3, font=("Arial", 20), command=lambda: button_click("x")).place(x=220, y=221)
Button(mainWindow, text="3", width=3, font=("Arial", 20), command=lambda: button_click("3")).place(x=160, y=221)
Button(mainWindow, text="2", width=3, font=("Arial", 20), command=lambda: button_click("2")).place(x=100, y=221)
Button(mainWindow, text="1", width=3, font=("Arial", 20), command=lambda: button_click("1")).place(x=40, y=221)

# Fourth Group
Button(mainWindow, text="+", width=3, font=("Arial", 20), command=lambda: button_click("+")).place(x=220, y=279)
Button(mainWindow, text="-", width=3, font=("Arial", 20), command=lambda: button_click("-")).place(x=160, y=279)
Button(mainWindow, text="0", width=3, font=("Arial", 20), command=lambda: button_click("0")).place(x=100, y=279)
Button(mainWindow, text=".", width=3, font=("Arial", 20), command=lambda: button_click(".")).place(x=40, y=279)

# Fifth
Button(mainWindow, text="=", width=12, font=("Arial", 20), command= calculate).place(x=58, y=337)



mainWindow.mainloop()