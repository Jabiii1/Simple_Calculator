from tkinter import *

mainWindow = Tk()
mainWindow.title("Simple Calculator")
mainWindow.geometry("314x415")  
mainWindow.resizable(False, False) 
mainWindow.configure(bg="black")  #Backgorund color (i choose this because its more darker than the hex colors)

# Whthis function is when you click the buttons it will show in the Entry
def Inclick(value):
    calcuScreen_var.set(calcuScreen_var.get() + str(value))

# This function is when you click the ⌦ it will clear the latest text (need to study it more)
def clear_latest():
    currentString = calcuScreen_var.get()
    calcuScreen_var.set(currentString[:-1])
    answerScreen_var.set("")

# This function is when you click the C it will clear the all text that shows in the entry 
def clear_all():
    calcuScreen_var.set("")
    answerScreen_var.set("")

# This function will convert the text into operational and will compute it to show the answer (need to study it more)
def calculate():
    try:
        expression = calcuScreen_var.get().replace("×", "*").replace("÷", "/").replace("%", "/100")
        result = eval(expression)
        answerScreen_var.set(result)
    except:
        answerScreen_var.set("Error")

# Screen variables that i declared it into String
calcuScreen_var = StringVar()
answerScreen_var = StringVar()

# Screens for Calculator (I used some hex colors to change just a plain black/white color to something more lighter/darker)
calcuScreen = Entry(mainWindow,bg="#1E1E1E", fg="white", textvariable=calcuScreen_var,font=("Arial", 35),width=12, relief="ridge", justify="right")
calcuScreen.grid(column=1,row=1, sticky="nsew")
answerScreen = Entry(mainWindow,bg="#1E1E1E", fg="white", textvariable=answerScreen_var, font=("Arial", 15),width=12, relief="ridge", justify="right")
answerScreen.grid(column=1,row=2, sticky="nsew")

# Icon For Window
icon = PhotoImage(file= "calc.png")    
mainWindow.iconphoto(False, icon)

# Buttons for Calculator with lambda("Currently learning and trying it to practical codes")

# First Group
Button(mainWindow, text="÷",width=3,bg="#9575CD", foreground="#FFFFFF", relief="flat", font=("Arial", 20), command=lambda: Inclick("÷")).place(x=220, y=105)
Button(mainWindow, text="%",width=3, relief="flat",bg="#1E1E1E" ,foreground="#9575CD",font=("Arial", 20), command=lambda: Inclick("%")).place(x=160, y=105)
Button(mainWindow, text="⌦",width=3, relief="flat",bg="#1E1E1E" ,foreground="#9575CD", font=("Arial", 20), command=lambda: clear_latest()).place(x=100, y=105)
Button(mainWindow, text="C", width=3, relief="flat", bg="#1E1E1E" ,foreground="#9575CD", font=("Arial", 20), command=lambda: clear_all()).place(x=40, y=105)

# Second Goup
Button(mainWindow, text="×",width=3, bg="#9575CD", foreground="#FFFFFF", relief="flat",  font=("Arial", 20), command=lambda: Inclick("×")).place(x=220, y=163)
Button(mainWindow, text="9",width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("9")).place(x=160, y=163)
Button(mainWindow, text="8",width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("8")).place(x=100, y=163)
Button(mainWindow, text="7",width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("7")).place(x=40, y=163)

# Third Group
Button(mainWindow, text="-", width=3,bg="#9575CD", foreground="#FFFFFF", relief="flat",  font=("Arial", 20), command=lambda: Inclick("-")).place(x=220, y=221)
Button(mainWindow, text="6", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("6")).place(x=160, y=221)
Button(mainWindow, text="5",width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("5")).place(x=100, y=221)
Button(mainWindow, text="4",width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("4")).place(x=40, y=221)

# Fourth Group
Button(mainWindow, text="+", width=3,bg="#9575CD", foreground="#FFFFFF", relief="flat",  font=("Arial", 20), command=lambda: Inclick("+")).place(x=220, y=279)
Button(mainWindow, text="3", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("3")).place(x=160, y=279)
Button(mainWindow, text="2", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("2")).place(x=100, y=279)
Button(mainWindow, text="1", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("1")).place(x=40, y=279)

# Fourth Group
Button(mainWindow, text="=", width=3,bg="#9575CD", foreground="#FFFFFF", relief="flat",  font=("Arial", 20), command= calculate).place(x=220, y=337)
Button(mainWindow, text=".", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick(".")).place(x=160, y=337)
Button(mainWindow, text="0", width=3, relief="flat", bg="#1E1E1E" ,foreground="#FFFFFF", font=("Arial", 20), command=lambda: Inclick("0")).place(x=100, y=337)
Button(mainWindow, text="00", width=3, relief="flat",bg="#1E1E1E" ,foreground="#FFFFFF",  font=("Arial", 20), command=lambda: Inclick("00")).place(x=40, y=337)

# To show the window
mainWindow.mainloop()