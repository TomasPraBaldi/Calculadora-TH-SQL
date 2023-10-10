import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x300')
button_value = tk.StringVar()

def button_clicked():
    button_value = button1.cget("text")
    messagebox.showinfo("Button clicked!", f"The button {button_value} was clicked!")

button1 = tk.Button(window, text="1", command=button_clicked)
button2 = tk.Button(window, text="2", command=button_clicked)

button1.pack()
button2.pack()

window.mainloop()


'''
def val1():
    global valor1
    #valor1 = float(int(input("First value: ")))
    valor1 = input("First value: ")
    if valor1.isdigit(): 
        print()
    else:
        print("This calculator can't use letters!")
        val1()
val1()

def op():
    global operador
    operador = input("Operator: + , - , / , or *: ")
    if operador !="+" and operador !="-" and operador !="*" and operador != "/":   
        print("Type an valid operator!")
        op()
op()

valor2 = input("Second value: ")
if valor2.isdigit():
    print()
else:
    print("This calculator can't use letters!")


if operador == "+":
    print(valor1+valor2)
elif operador == "-":
    print(valor1-valor2)
elif operador == "/":
    print(valor1/valor2)
elif operador == "*":
    print(valor1*valor2)
else:
    print("Digite um operador valido.")
'''