# BIBLIOTECAS ---------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
#import functools
#import math_logic

# GUI - DEFINIÇÕES ----------------------------------------------------------------------------
#def math_logic.button_clicked(): 
#    math_logic.math_logic.button_clicked2()


window = ctk.CTk()
ctk.set_appearance_mode('dark')
window.corner_radius = 10
totalw = 300
totalh = 481
bgcolor = '#000'
displaycolor = '#000'
window.geometry(f'{totalw}x{totalh}')
window.title('')
window.iconbitmap(r"th_ico.ico")
window.config(bg = bgcolor)
window.resizable(False,False)
window.wm_attributes('-topmost', True)

grid = tk.Frame(window)
grid.grid(pady=70)

buttoncolor = '#333'
buttonfontcolor = '#eeeffe'
buttonoperationcolor = '#65b595'
buttonfont = ("Arial", 20, 'bold')

buttonw = 4
buttonh = 2

topdisplay = tk.Text(window)
topdisplay.place(x=0, y=40, width=totalw, height=40)
#topdisplay.config(state="disabled")
topdisplay.configure(bg=displaycolor)
topdisplay.config(borderwidth=0)
topdisplay.config(fg='#ccc')
topdisplay.config(font=("Calibri", 20))

bottomdisplay = tk.Text(window)
bottomdisplay.place(x=0, y=80, width=totalw, height=60)
bottomdisplay.config(state="disabled")
bottomdisplay.configure(bg=displaycolor)
bottomdisplay.config(borderwidth=0)
bottomdisplay.config(fg='#eee')
bottomdisplay.config(font=("Calibri", 32, "bold"))

# VARIÁVEIS DOS BOTÕES ----------------------------------------------------------------------------------
b1 = 1
b2 = 2
b3 = 3
b4 = 4
b5 = 5
b6 = 6
b7 = 7
b8 = 8
b9 = 9
b0 = 0
bplus = '+'
bequals = '='
bpminus = '-'
bc = '.'

