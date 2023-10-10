
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry("500x300")


def button_clicked():
    messagebox.showinfo("Button clicked!", "The button was clicked!")
button_value = tk.StringVar()


button = tk.Button( window, text="1", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button2 = tk.Button(window, text="2", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button3 = tk.Button(window, text="3", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button4 = tk.Button(window, text="4", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button5 = tk.Button(window, text="5", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button6 = tk.Button(window, text="6", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button7 = tk.Button(window, text="7", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button8 = tk.Button(window, text="8", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button9 = tk.Button(window, text="9", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button0 = tk.Button(window, text="0", command=button_clicked, width=7, height=4, bg="grey",fg="black")
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button0.pack()


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