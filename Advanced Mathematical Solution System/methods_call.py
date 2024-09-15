import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
import sympy as sp


# Define Methods
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


# Parse expression into a function
def parse_expression(expr, symbol='x'):
    x = sp.Symbol(symbol)
    parsed_expr = sp.sympify(expr)
    f = sp.lambdify(x, parsed_expr, 'numpy')
    f_prime = sp.lambdify(x, sp.diff(parsed_expr, x), 'numpy')
    return f, f_prime


# User Input Functions
def get_user_input():
    # Get user input for bisection method
    print("Bisection Method:")
    expr = input("Enter the function expression (e.g., x**3 - x - 2): ")
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))

    # Get user input for Newton-Raphson method
    print("\nNewton-Raphson Method:")
    x0 = float(input("Enter the initial guess (x0): "))

    # Get user input for Simpson's Rule
    print("\nSimpson's Rule:")
    a_simpson = float(input("Enter the lower bound (a): "))
    b_simpson = float(input("Enter the upper bound (b): "))
    n = int(input("Enter the number of intervals (n): "))

    # Get user input for Euler and Runge-Kutta methods
    print("\nEuler and Runge-Kutta Methods:")
    y0 = float(input("Enter the initial value (y0): "))
    x0_euler_rk = float(input("Enter the start of the interval (x0): "))
    x_end = float(input("Enter the end of the interval (x_end): "))
    h = float(input("Enter the step size (h): "))

    return expr, a, b, x0, a_simpson, b_simpson, n, y0, x0_euler_rk, x_end, h


# Get User Inputs
(expr, a, b, x0, a_simpson, b_simpson, n, y0, x0_euler_rk, x_end, h) = get_user_input()

# Parse the expression for Newton-Raphson method
f, f_prime = parse_expression(expr)

# Perform Calculations
try:
    root_bisection = bisection_method(f, a, b)
    print(f"\nRoot found using Bisection Method: {root_bisection}")
except ValueError as e:
    print(e)

try:
    root_newton = newton_raphson_method(f, f_prime, x0=x0)
    print(f"Root found using Newton-Raphson Method: {root_newton}")
except ValueError as e:
    print(e)

try:
    integral_simpsons = simpsons_rule(f, a_simpson, b_simpson, n=n)
    print(f"Integral computed using Simpson's Rule: {integral_simpsons}")
except ValueError as e:
    print(e)

x_euler, y_euler = euler_method(lambda x, y: x + y, y0=y0, x0=x0_euler_rk, x_end=x_end, h=h)
print(f"Euler Method Results: x={x_euler}, y={y_euler}")

x_rk, y_rk = runge_kutta_4(lambda x, y: x + y, y0=y0, x0=x0_euler_rk, x_end=x_end, h=h)
print(f"Runge-Kutta Method Results: x={x_rk}, y={y_rk}")


# Plot Results
def plot_results(x, y, title):
    plt.figure()
    plt.plot(x, y, 'o-', label=title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


# Plot Euler Method Results
plot_results(x_euler, y_euler, "Euler Method")

# Plot Runge-Kutta Method Results
plot_results(x_rk, y_rk, "Runge-Kutta Method")
