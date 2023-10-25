import gui
import math_logic


def main():
    calculator = gui.window
    bottomdisplay = gui.bottomdisplay
    calculator.add = math_logic.button_clicked
    calculator.mainloop()

if __name__ == "__main__":
    main()
