import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify, sympify, diff

# Define symbolic variables
x, y = symbols('x y')


def evaluate_expression(expr, value_x, value_y=None):
    """Evaluate the mathematical expression with given x and y values."""
    func = lambdify((x, y), expr, 'numpy')
    if value_y is None:
        return func(value_x)
    return func(value_x, value_y)


def bisection_method(a, b, tolerance, max_iterations, expr):
    """Bisection method to find the root of the function `expr`."""
    a = float(a)
    b = float(b)
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)
    expr = sympify(expr)

    f = lambdify(x, expr, 'numpy')
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("Function has the same sign at endpoints a and b")

    for _ in range(max_iterations):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c


def newton_raphson_method(x0, tolerance, max_iterations, expr):
    """Newton-Raphson method to find the root of the function `expr`."""
    x0 = float(x0)
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)
    expr = sympify(expr)

    f = lambdify(x, expr, 'numpy')
    f_prime = lambdify(x, diff(expr, x), 'numpy')

    for _ in range(max_iterations):
        f_x0 = f(x0)
        f_prime_x0 = f_prime(x0)

        if f_prime_x0 == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")

        x1 = x0 - f_x0 / f_prime_x0

        if abs(x1 - x0) < tolerance:
            return x1

        x0 = x1

    return x0


def euler_method(x0, y0, h, xn, expr):
    """Euler method to solve the differential equation `dy/dx = expr`."""
    expr = sympify(expr)  # Convert string to sympy expression
    f = lambdify((x, y), expr, 'numpy')

    x_vals = [x0]
    y_vals = [y0]

    while x0 < xn:
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_vals.append(x0)
        y_vals.append(y0)

    return x_vals, y_vals


def runge_kutta_method(x0, y0, h, xn, expr):
    """Runge-Kutta method to solve the differential equation `dy/dx = expr`."""
    expr = sympify(expr)  # Convert string to sympy expression
    f = lambdify((x, y), expr, 'numpy')

    x_vals = [x0]
    y_vals = [y0]

    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 = x0 + h

        x_vals.append(x0)
        y_vals.append(y0)

    return x_vals, y_vals


def run_method():
    method = method_var.get()
    expr = entry_expr.get()

    try:
        if method == 'Bisection':
            a = float(entry_a.get())
            b = float(entry_b.get())
            tolerance = float(entry_tolerance.get())
            max_iterations = int(entry_max_iterations.get())
            result = bisection_method(a, b, tolerance, max_iterations, expr)
            messagebox.showinfo("Result", f"Root: {result}")
        elif method == 'Newton-Raphson':
            x0 = float(entry_x0.get())
            tolerance = float(entry_tolerance.get())
            max_iterations = int(entry_max_iterations.get())
            result = newton_raphson_method(x0, tolerance, max_iterations, expr)
            messagebox.showinfo("Result", f"Root: {result}")
        elif method == 'Euler':
            x0 = float(entry_x0.get())
            y0 = float(entry_y0.get())
            h = float(entry_h.get())
            xn = float(entry_xn.get())
            x, y = euler_method(x0, y0, h, xn, expr)
            plot_graph(x, y, 'Euler\'s Method')
        elif method == 'Runge-Kutta':
            x0 = float(entry_x0.get())
            y0 = float(entry_y0.get())
            h = float(entry_h.get())
            xn = float(entry_xn.get())
            x, y = runge_kutta_method(x0, y0, h, xn, expr)
            plot_graph(x, y, 'Runge-Kutta Method')
        else:
            messagebox.showerror("Error", "Invalid method selected.")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {e}")


def plot_graph(x, y, title):
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


# Create the main window
root = tk.Tk()
root.title("Advanced Mathematical Solution System")

# Method selection
method_var = tk.StringVar(value='Bisection')
tk.Label(root, text="Select Method:").pack()
tk.Radiobutton(root, text="Bisection", variable=method_var, value='Bisection').pack()
tk.Radiobutton(root, text="Newton-Raphson", variable=method_var, value='Newton-Raphson').pack()
tk.Radiobutton(root, text="Euler", variable=method_var, value='Euler').pack()
tk.Radiobutton(root, text="Runge-Kutta", variable=method_var, value='Runge-Kutta').pack()

# Inputs for Bisection and Newton-Raphson methods
tk.Label(root, text="Expression:").pack()
entry_expr = tk.Entry(root)
entry_expr.pack()

tk.Label(root, text="Tolerance:").pack()
entry_tolerance = tk.Entry(root)
entry_tolerance.pack()

tk.Label(root, text="Max Iterations:").pack()
entry_max_iterations = tk.Entry(root)
entry_max_iterations.pack()

tk.Label(root, text="a (for Bisection):").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="b (for Bisection):").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="x0 (for Newton-Raphson and Euler and Runge-Kutta):").pack()
entry_x0 = tk.Entry(root)
entry_x0.pack()

tk.Label(root, text="y0 (for Euler and Runge-Kutta):").pack()
entry_y0 = tk.Entry(root)
entry_y0.pack()

tk.Label(root, text="h (Step Size for Euler and Runge-Kutta):").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Label(root, text="xn (End x for Euler and Runge-Kutta):").pack()
entry_xn = tk.Entry(root)
entry_xn.pack()

# Run button
tk.Button(root, text="Run", command=run_method).pack()

root.mainloop()
