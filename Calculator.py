import tkinter 
from tkinter import*


root = Tk()
root.title("Calculator")
root.geometry("600x600") 
root.resizable(True, True)
root.configure(bg="#17161b")

label_result = Label(root, width=25, height=2, text="", font=("Arial", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=20, y=100)
Button(root, text="⌦", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=160, y=100)
Button(root, text="%", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=300, y=100)
Button(root, text="÷", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=440, y=100)

root.mainloop()
