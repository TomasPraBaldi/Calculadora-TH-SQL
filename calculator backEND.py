# BIBLIOTECAS ---------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import functools

# GUI - DEFINIÇÕES ----------------------------------------------------------------------------
window = tk.Tk()
totalw = 315
totalh = 455
bgcolor = '#000'
displaycolor = '#000'
window.geometry(f'{totalw}x{totalh}')
window.title('')
window.iconbitmap(r"C:\Users\Hiurytg.000\Desktop\TH_SQL\Calculadora-TH-SQL\images\th_ico.ico")
window.config(bg = bgcolor)
window.resizable(False,False)
window.wm_attributes('-topmost', True)
window.after(50,None)

grid = tk.Frame(window)
grid.grid(pady=70)

buttoncolor = '#333'
buttonfontcolor = '#eeeffe'
buttonoperationcolor = '#65b595'
buttonfont = ("Arial", 30, 'bold')

buttonw = 3
buttonh = 1

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


##############################################################################################
##############################################################################################


# FUNÇÃO PRINCIPAL - BOTÕES & OPERAÇÕES ------------------------------------------------------
def button_clicked(button_value, value1='', value2='', value3=''):
    if button_value == '=':
       bottomdisplay.config(state="normal")
       value2 = bottomdisplay.get('1.0','end')
       #print(value1,value2)
       bottomdisplay.delete("1.0", "end")
       bottomdisplay.insert("end", value1+value2)
       bottomdisplay.config(state="disabled")
    if button_value == '+':
       if value1 != '' and value2 != '':
          bottomdisplay.config(state="normal")
          value3 = value1+value2
          value1 = value3
          value2 = ''
          #operator = '+'
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")
       if value1 != '' and value2 == '':
          bottomdisplay.config(state="normal")
          value2 = bottomdisplay.get('1.0','end')
          #operator = '+'
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")
       else:
          bottomdisplay.config(state="normal")
          value1 = bottomdisplay.get('1.0','end')
          topdisplay.insert('end', f'{value1.strip()} + ')
          #operator = '+'
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")
    else:
       bottomdisplay.config(state="normal")
       bottomdisplay.insert('end', button_value)
       bottomdisplay.config(state="disabled")

# BOTÕES --------------------------------------------------------------------------------------------
button1 = tk.Button(window, text=b1, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b1))
button1.grid(row=3, column=0, padx=0, pady=0)
button2 = tk.Button(window, text=b2, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b2))
button2.grid(row=3, column=1, padx=1, pady=1)
button3 = tk.Button(window, text=b3, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b3))
button3.grid(row=3, column=2, padx=0, pady=0)
button4 = tk.Button(window, text=b4, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b4))
button4.grid(row=2, column=0, padx=0, pady=0)
button5 = tk.Button(window, text=b5, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b5))
button5.grid(row=2, column=1, padx=0, pady=0)
button6 = tk.Button(window, text=b6, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b6))
button6.grid(row=2, column=2, padx=0, pady=0)
button7 = tk.Button(window, text=b7, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b7))
button7.grid(row=1, column=0, padx=0, pady=1)
button8 = tk.Button(window, text=b8, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b8))
button8.grid(row=1, column=1, padx=0, pady=0)
button9 = tk.Button(window, text=b9, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b9))
button9.grid(row=1, column=2, padx=0, pady=0)
button0 = tk.Button(window, text=b0, background = buttoncolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, b0))
button0.grid(row=4, column=0, padx=0, pady=0)
buttoncomma = tk.Button(window, text=bc, background = buttoncolor, borderwidth=0, width = 3, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, bc))
buttoncomma.grid(row=4, column=1, padx=0, pady=0)

buttonplus = tk.Button(window, text=bplus, background = buttonoperationcolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, bplus))
buttonplus.grid(row=1, column=3, padx=1, pady=0)
buttonminus = tk.Button(window, text=bpminus, background = buttonoperationcolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, bpminus))
buttonminus.grid(row=2, column=3, padx=0, pady=0)
buttonequals = tk.Button(window, text=bequals, background = buttonoperationcolor, borderwidth=0, width = buttonw, height = buttonh, fg = buttonfontcolor , font = buttonfont, command=functools.partial(button_clicked, bequals))
buttonequals.grid(row=3, column=3, padx=0, pady=0)


# INICIA A GUI -----------------------------------------------------------------------------------------
window.mainloop()