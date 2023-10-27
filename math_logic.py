import gui
import functools

value1 = ''
value2 = ''

def button_clicked(button_value):
    global value0, value1, value2, value3
    if button_value == '=':
       if value2 == '':
         bottomdisplay.config(state="normal")
         topdisplay.config(state="normal")
         bottomdisplay.delete("1.0", "end")
         topdisplay.delete("1.0", "end")
         value3 = int(value0)+int(value1)
         bottomdisplay.insert('end', f'{value3}')
         bottomdisplay.config(state="disabled")
         topdisplay.config(state="disabled")
         return
       if value2 != '':
         bottomdisplay.config(state="normal")
         topdisplay.config(state="normal")
         bottomdisplay.delete("1.0", "end")
         topdisplay.delete("1.0", "end")
         value3 = int(value0)+int(value2)
         bottomdisplay.insert('end', f'{value3}')
         bottomdisplay.config(state="disabled")
         topdisplay.config(state="disabled")
         return  
    if button_value == '+':
       if value1 == '':
          bottomdisplay.config(state="normal")
          topdisplay.config(state="normal")
          value1 = value0
          value0 = ''
          topdisplay.insert('end', f'{value1.strip()} + ')
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")
          topdisplay.config(state="disabled")
       elif value2 != '':
          bottomdisplay.config(state="normal")
          topdisplay.config(state="normal")
          value2 = (int(value0) + (int(value2)))
          value1 = bottomdisplay.get('1.0','end')
          topdisplay.insert('end', f'{value1.strip()} + ')
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")   
          topdisplay.config(state="disabled")
       elif value1 != '':
          bottomdisplay.config(state="normal")
          topdisplay.config(state="normal")
          value2 = (int(value0) + (int(value1)))
          value1 = bottomdisplay.get('1.0','end')
          topdisplay.insert('end', f'{value1.strip()} + ')
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")          
          topdisplay.config(state="disabled")
    else: # qualquer número cai aqui
       bottomdisplay.config(state="normal")
       topdisplay.config(state="normal")
       bottomdisplay.insert('end', button_value)
       value0 = bottomdisplay.get('1.0','end') 
       bottomdisplay.config(state="disabled")
       topdisplay.config(state="disabled")

       
button1 = gui.tk.Button(gui.window, text=gui.b1, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b1))
button1.grid(row=3, column=0, padx=0, pady=0)
button2 = gui.tk.Button(gui.window, text=gui.b2, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b2))
button2.grid(row=3, column=1, padx=1, pady=1)
button3 = gui.tk.Button(gui.window, text=gui.b3, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b3))
button3.grid(row=3, column=2, padx=0, pady=0)
button4 = gui.tk.Button(gui.window, text=gui.b4, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b4))
button4.grid(row=2, column=0, padx=0, pady=0)
button5 = gui.tk.Button(gui.window, text=gui.b5, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b5))
button5.grid(row=2, column=1, padx=0, pady=0)
button6 = gui.tk.Button(gui.window, text=gui.b6, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b6))
button6.grid(row=2, column=2, padx=0, pady=0)
button7 = gui.tk.Button(gui.window, text=gui.b7, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b7))
button7.grid(row=1, column=0, padx=0, pady=1)
button8 = gui.tk.Button(gui.window, text=gui.b8, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b8))
button8.grid(row=1, column=1, padx=0, pady=0)
button9 = gui.tk.Button(gui.window, text=gui.b9, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b9))
button9.grid(row=1, column=2, padx=0, pady=0)
button0 = gui.tk.Button(gui.window, text=gui.b0, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.b0))
button0.grid(row=4, column=0, padx=0, pady=0)
buttoncomma = gui.tk.Button(gui.window, text=gui.bc, background = gui.buttoncolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.bc))
buttoncomma.grid(row=4, column=1, padx=0, pady=0)

buttonplus = gui.tk.Button(gui.window, text=gui.bplus, background = gui.buttonoperationcolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.bplus))
buttonplus.grid(row=1, column=3, padx=1, pady=0)
buttonminus = gui.tk.Button(gui.window, text=gui.bpminus, background = gui.buttonoperationcolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.bpminus))
buttonminus.grid(row=2, column=3, padx=0, pady=0)
buttonequals = gui.tk.Button(gui.window, text=gui.bequals, background = gui.buttonoperationcolor, borderwidth=0, width = gui.buttonw, height = gui.buttonh, fg = gui.buttonfontcolor , font = gui.buttonfont, command=functools.partial(button_clicked, gui.bequals))
buttonequals.grid(row=3, column=3, padx=0, pady=0)

bottomdisplay = gui.bottomdisplay
topdisplay = gui.topdisplay