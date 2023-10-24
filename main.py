import customtkinter as ctk
import gui2
import math_logic

window = gui2.window

def main():
    calculator = window
    calculator.add = math_logic.button_clicked2
    calculator.mainloop()

if __name__ == "__main__":
    main()
