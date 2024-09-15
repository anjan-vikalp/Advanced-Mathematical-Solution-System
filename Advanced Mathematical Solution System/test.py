import customtkinter
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# --- Calculation Methods --- #
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


# --- Input Parsing --- #
def parse_expression(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr), 'numpy')


# --- Plot Results --- #
def plot_results(x, y, title):
    plt.figure()
    plt.plot(x, y, 'o-', label=title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


# --- GUI Implementation --- #
def calculate_method(selected_method):
    # Fetch user inputs
    expr = entry_func.get()
    a = entry1.get()
    b = entry2.get()

    try:
        # Parse the function expression
        f = parse_expression(expr)

        # Handle different methods
        if selected_method == "Bisection Method":
            a = float(a)
            b = float(b)
            root = bisection_method(f, a, b)
            messagebox.showinfo("Result", f"Bisection Method Root: {root}")

        elif selected_method == "Newton-Raphson Method":
            x0 = float(a)
            f_prime = parse_expression(entry_prime.get())
            root = newton_raphson_method(f, f_prime, x0)
            messagebox.showinfo("Result", f"Newton-Raphson Method Root: {root}")

        elif selected_method == "Runge-Kutta Method":
            y0 = float(entry_y0.get())
            x0 = float(entry_x0.get())
            x_end = float(entry_x_end.get())
            h = float(entry_h.get())
            x, y = runge_kutta_4(f, y0, x0, x_end, h)
            plot_results(x, y, "Runge-Kutta Method")

        elif selected_method == "Simpson's Rule":
            a = float(a)
            b = float(b)
            n = int(entry_n.get())
            integral = simpsons_rule(f, a, b, n)
            messagebox.showinfo("Result", f"Simpson's Rule Integral: {integral}")

        elif selected_method == "Euler Method":
            y0 = float(entry_y0.get())
            x0 = float(entry_x0.get())
            x_end = float(entry_x_end.get())
            h = float(entry_h.get())
            x, y = euler_method(f, y0, x0, x_end, h)
            plot_results(x, y, "Euler Method")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# --- Create GUI --- #
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x600")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Select Calculation Method", font=("Roboto", 18))
label.pack(pady=12, padx=10)

# Entry for the function expression
entry_func = customtkinter.CTkEntry(master=frame, placeholder_text="Enter function f(x)")
entry_func.pack(pady=12, padx=10)

# Entry for the first and second input (a and b or x0)
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Input First Number (a or x0)")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Input Second Number (b)")
entry2.pack(pady=12, padx=10)

# Option menu to select the method
method_options = ["Bisection Method", "Newton-Raphson Method", "Runge-Kutta Method", "Simpson's Rule", "Euler Method"]
optionmenu = customtkinter.CTkOptionMenu(master=frame, values=method_options)
optionmenu.pack(pady=12, padx=10)
optionmenu.set("Select Method")

# Entries for additional input like derivative (Newton), y0, step size, etc.
entry_prime = customtkinter.CTkEntry(master=frame, placeholder_text="Enter f'(x) (for Newton-Raphson)")
entry_prime.pack(pady=12, padx=10)

entry_y0 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter y0 (for Euler/Runge-Kutta)")
entry_y0.pack(pady=12, padx=10)

entry_x0 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter x0 (for Euler/Runge-Kutta)")
entry_x0.pack(pady=12, padx=10)

entry_x_end = customtkinter.CTkEntry(master=frame, placeholder_text="Enter x_end (for Euler/Runge-Kutta)")
entry_x_end.pack(pady=12, padx=10)

entry_h = customtkinter.CTkEntry(master=frame, placeholder_text="Enter step size (h)")
entry_h.pack(pady=12, padx=10)

entry_n = customtkinter.CTkEntry(master=frame, placeholder_text="Enter number of intervals (n) (for Simpson)")
entry_n.pack(pady=12, padx=10)

# Button to trigger the calculation
button = customtkinter.CTkButton(master=frame, text="Calculate", command=lambda: calculate_method(optionmenu.get()))
button.pack(pady=12, padx=10)

root.mainloop()
