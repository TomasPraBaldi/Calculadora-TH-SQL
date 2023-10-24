import tkinter as tk
import customtkinter as ctk
from gui import *
from math import *

class mainApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title = ''
        self.gui = Cgui(self.window)
        self.math = mathLogic()

if __name__ == "__main__":
    app = mainApp()