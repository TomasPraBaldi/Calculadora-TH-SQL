def button_clicked(button_value, value1='', value2='', value3=''):
    if button_value == '=':
       bottomdisplay.config(state="normal")
       value2 = bottomdisplay.get('1.0','end')
       print(value1,value2)
       bottomdisplay.delete("1.0", "end")
       bottomdisplay.insert("end", value1+value2)
       bottomdisplay.config(state="disabled")
    if button_value == '+':
       if value1 != '' and value2 != '':
          bottomdisplay.config(state="normal")
          value3 = value1 #value1+value2
          value1 = bottomdisplay.get('1.0','end')
          value2 = ''
          #operator = '+'
          bottomdisplay.delete("1.0", "end")
          bottomdisplay.config(state="disabled")
       if value1 != '' and value2 == '': # pode ser aqui o erro -- cade o insert?
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
    else: # qualquer número cai aqui
       bottomdisplay.config(state="normal")
       bottomdisplay.insert('end', button_value)
       bottomdisplay.config(state="disabled")

       
