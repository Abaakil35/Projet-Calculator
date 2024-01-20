import tkinter
from tkinter import *
from tkinter import messagebox

Calc = Tk()
Calc.title("Calculatrice")
Calc.geometry("600x600") 
Calc.resizable(False, False)
Calc.configure(bg="#051923")

equation = ""
def voir(value):
    global equation
    equation += value
    label_result.config(text=equation)
    
def suppr():
    global equation
    equation = ""
    label_result.config(text=equation)

    
def calcul():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
            messagebox.showerror("Error",  "Please enter a Number.")
    label_result.config(text=result)
                    
                                  

label_result = Label(Calc, width=25, height=2, text="", font=("inherit", 30),bg="#E2FCEF")
label_result.pack()

Button(Calc, text="⌦", width=7, height=1, font=("inherit", 30), bd=4,  fg="#fff", bg="#FC7753",command=lambda: suppr() ).place(x=20, y=110)
Button(Calc, text="÷", width=8, height=1, font=("inherit", 30), bd=4,   fg="#fff", bg="#463F3A",command=lambda: voir('/')).place(x=200, y=110)
Button(Calc, text="× ", width=7, height=1, font=("inherit", 30), bd=4,   fg="#fff", bg="#463F3A",command=lambda: voir('*')).place(x=400, y=110)


Button(Calc, text="7", width=5, height=1, font=("inherit", 30), bd=1,   fg="#fff", bg="#273E47",command=lambda: voir('7')).place(x=20, y=210)
Button(Calc, text="8", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('8')).place(x=160, y=210)
Button(Calc, text="9", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('9')).place(x=300, y=210)
Button(Calc, text="-", width=5, height=1, font=("inherit", 30), bd=4,  fg="#fff", bg="#463F3A",command=lambda: voir('-')).place(x=440, y=210)

Button(Calc, text="4", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('4')).place(x=20, y=300)
Button(Calc, text="5", width=5, height=1, font=("inherit", 30), bd=1,   fg="#fff", bg="#273E47",command=lambda: voir('5')).place(x=160, y=300)
Button(Calc, text="6", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('6')).place(x=300, y=300)
Button(Calc, text="+", width=5, height=1, font=("inherit", 30), bd=4,  fg="#fff", bg="#463F3A",command=lambda: voir('+')).place(x=440, y=300)


Button(Calc, text="1", width=5, height=1, font=("inherit", 30), bd=1, fg="#fff", bg="#273E47",command=lambda: voir('1')).place(x=20, y=390)
Button(Calc, text="2", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('2')).place(x=160, y=390)
Button(Calc, text="3", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('3')).place(x=300, y=390)

Button(Calc, text="+/-", width=5, height=1, font=("inherit", 30 ), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('-')).place(x=20, y=480)
Button(Calc, text="0", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('0')).place(x=160, y=480)
Button(Calc, text=".", width=5, height=1, font=("inherit", 30), bd=1,  fg="#fff", bg="#273E47",command=lambda: voir('.')).place(x=300, y=480)
Button(Calc, text="=", width=5, height=3, font=("inherit", 30), bd=4,  fg="#fff", bg="#FC7753",command=lambda: calcul()).place(x=440, y=390)




Calc.mainloop()
