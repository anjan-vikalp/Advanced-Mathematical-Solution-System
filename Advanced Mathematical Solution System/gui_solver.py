import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define Methods (same as before)

# Define Example Functions (same as before)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Mathematical Solution System")

        self.create_widgets()

    def create_widgets(self):
        self.method_label = ttk.Label(self.root, text="Select a method:")
        self.method_label.pack(pady=10)

        self.method_combobox = ttk.Combobox(self.root,
                                            values=["Bisection Method", "Newton-Raphson Method", "Simpson's Rule",
                                                    "Euler Method", "Runge-Kutta Method"])
        self.method_combobox.pack(pady=10)
        self.method_combobox.bind("<<ComboboxSelected>>", self.on_method_selected)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=10)

    def on_method_selected(self, event):
        method = self.method_combobox.get()
        self.clear_inputs()

        if method == "Bisection Method":
            self.add_input("a", float)
            self.add_input("b", float)
            self.add_button("Compute", self.compute_bisection)

        elif method == "Newton-Raphson Method":
            self.add_input("x0", float)
            self.add_button("Compute", self.compute_newton_raphson)

        elif method == "Simpson's Rule":
            self.add_input("a", float)
            self.add_input("b", float)
            self.add_input("n", int)
            self.add_button("Compute", self.compute_simpsons)

        elif method == "Euler Method":
            self.add_input("y0", float)
            self.add_input("x0", float)
            self.add_input("x_end", float)
            self.add_input("h", float)
            self.add_button("Compute", self.compute_euler)

        elif method == "Runge-Kutta Method":
            self.add_input("y0", float)
            self.add_input("x0",)
