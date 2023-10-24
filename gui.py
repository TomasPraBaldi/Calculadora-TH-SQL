import tkinter as tk

class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.display = tk.Entry(self.root)
        self.display.pack()

        self.buttons = {}
        for i in range(10):
            self.buttons[str(i)] = tk.Button(self.root, text=str(i), command=lambda i=i: self.display.insert(tk.END, str(i)))
            self.buttons[str(i)].pack()

        self.buttons["+"] = tk.Button(self.root, text="+", command=self.add)
        self.buttons["+"].pack()

        self.buttons["-"] = tk.Button(self.root, text="-", command=self.subtract)
        self.buttons["-"].pack()

        self.buttons["*"] = tk.Button(self.root, text="*", command=self.multiply)
        self.buttons["*"].pack()

        self.buttons["/"] = tk.Button(self.root, text="/", command=self.divide)
        self.buttons["/"].pack()

        self.buttons["="] = tk.Button(self.root, text="=", command=self.evaluate)
        self.buttons["="].pack()

        self.root.mainloop()

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass

    def evaluate(self):
        pass

if __name__ == "__main__":
    calculator = CalculatorGUI()
