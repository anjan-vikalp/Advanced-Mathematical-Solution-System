import customtkinter
from tkinter import messagebox
import numpy as np
import sympy as sp
import numpy as np
import sympy as sp

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Function has the same signs at the endpoints.")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded.")

def newton_raphson_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Maximum iterations exceeded.")

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Number of intervals must be even.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

def euler_method(f, y0, x0, x_end, h):
    x = np.arange(x0, x_end, h)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(1, len(x)):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
    return x, y

def runge_kutta_4(f, y0, x0, x_end, h):
    x = np.arange(x0, x_end, h)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(1, len(x)):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y

# Import your previously written calculation methods (from earlier code)
# from your_project import bisection_method, newton_raphson_method, simpsons_rule, euler_method, runge_kutta_4

# Set up the GUI appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the root window
root = customtkinter.CTk()
root.geometry("500x500")  # Adjust window size

# Define the method for parsing the function
def parse_expression(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr), 'numpy')

# Define the frame for the GUI
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Advanced Mathematical Solution System", font=("Roboto", 18))
label.pack(pady=12, padx=10)

# Create text entry for the function and inputs
entry_function = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Function (e.g., x**3 - x - 2)")
entry_function.pack(pady=12, padx=10)

entry_a = customtkinter.CTkEntry(master=frame, placeholder_text="Lower Bound / Initial Guess")
entry_a.pack(pady=12, padx=10)

entry_b = customtkinter.CTkEntry(master=frame, placeholder_text="Upper Bound / Initial Value")
entry_b.pack(pady=12, padx=10)

# Create the dropdown menu for method selection
def on_method_select(selected_method):
    messagebox.showinfo("Selected Method", f"You selected {selected_method}")

option_menu = customtkinter.CTkOptionMenu(
    frame,
    values=["Bisection Method", "Newton-Raphson Method", "Simpson's Rule", "Euler Method", "Runge-Kutta Method"],
    command=on_method_select
)
option_menu.pack(pady=12, padx=10)
option_menu.set("Select a Method")

# Create a button to perform the calculation
def calculate():
    selected_method = option_menu.get()
    func_expression = entry_function.get()  # Get the function from user input
    a = entry_a.get()  # Get lower bound / initial guess
    b = entry_b.get()  # Get upper bound / second input

    # Parse the function expression
    try:
        f = parse_expression(func_expression)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to parse function: {e}")
        return

    if selected_method == "Bisection Method":
        try:
            root = bisection_method(f, float(a), float(b))
            messagebox.showinfo("Result", f"Root found: {root}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    elif selected_method == "Newton-Raphson Method":
        try:
            f_prime = parse_expression(sp.diff(sp.sympify(func_expression)))  # Derivative for Newton-Raphson
            root = newton_raphson_method(f, f_prime, float(a))
            messagebox.showinfo("Result", f"Root found: {root}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    elif selected_method == "Simpson's Rule":
        try:
            integral = simpsons_rule(f, float(a), float(b), 10)  # Using n=10 intervals for simplicity
            messagebox.showinfo("Result", f"Integral: {integral}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    elif selected_method == "Euler Method":
        try:
            x, y = euler_method(f, float(a), 0, float(b), 0.1)  # Euler with initial value a and x_end=b
            messagebox.showinfo("Result", f"Euler results: {list(zip(x, y))}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    elif selected_method == "Runge-Kutta Method":
        try:
            x, y = runge_kutta_4(f, float(a), 0, float(b), 0.1)  # Runge-Kutta with step size 0.1
            messagebox.showinfo("Result", f"Runge-Kutta results: {list(zip(x, y))}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Create the calculate button
button_calculate = customtkinter.CTkButton(master=frame, text="Calculate", command=calculate)
button_calculate.pack(pady=12, padx=10)

# Run the application
root.mainloop()
