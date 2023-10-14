import tkinter as tk
import datetime

def update_label():
    current_time = 'assd'
    label.config(text=current_time)
    root.after(1000, update_label)  # run itself again after 1000 ms

root = tk.Tk()
label = tk.Label(root)
label.pack()

update_label()  # run first time at once

root.mainloop()
