import tkinter
from tkinter import *
from tkinter import messagebox

Calc = Tk()
Calc.title("Calculatrice")
Calc.geometry("600x600") 
Calc.resizable(False, False)
Calc.configure(bg="#051923")

equation = ""
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
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
                    
                                  

label_result = Label(Calc, width=25, height=2, text="", font=("Arial", 30),bg="#DBD2E0")
label_result.pack()

Button(Calc, text="⌦", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: clear()).place(x=20, y=110)
Button(Calc, text="÷", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: show('/')).place(x=160, y=110)
Button(Calc, text="%", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: show('%')).place(x=300, y=110)
Button(Calc, text="× ", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: show('*')).place(x=440, y=110)


Button(Calc, text="7", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('7')).place(x=20, y=210)
Button(Calc, text="8", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('8')).place(x=160, y=210)
Button(Calc, text="9", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('9')).place(x=300, y=210)
Button(Calc, text="-", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: show('-')).place(x=440, y=210)

Button(Calc, text="4", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('4')).place(x=20, y=300)
Button(Calc, text="5", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('5')).place(x=160, y=300)
Button(Calc, text="6", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('6')).place(x=300, y=300)
Button(Calc, text="+", width=5, height=1, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#463F3A",command=lambda: show('+')).place(x=440, y=300)


Button(Calc, text="1", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('1')).place(x=20, y=390)
Button(Calc, text="2", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('2')).place(x=160, y=390)
Button(Calc, text="3", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('3')).place(x=300, y=390)

Button(Calc, text="0", width=11, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('0')).place(x=20, y=480)
Button(Calc, text=".", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#273E47",command=lambda: show('.')).place(x=300, y=480)
Button(Calc, text="=", width=5, height=3, font=("Arial", 30, "bold"), bd=3, fg="#fff", bg="#D8973C",command=lambda: calculate()).place(x=440, y=390)




Calc.mainloop()
