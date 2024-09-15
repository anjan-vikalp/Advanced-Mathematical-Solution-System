import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton


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


# Define Input Parsing
def parse_expression(expr):
    x = sp.Symbol('x')
    return sp.lambdify(x, sp.sympify(expr), 'numpy')


def get_user_input():
    print("Select a method:")
    print("1. Bisection Method")
    print("2. Newton-Raphson Method")
    print("3. Simpson's Rule")
    print("4. Euler Method")
    print("5. Runge-Kutta Method")
    choice = input("Enter the number of the method you want to use: ")

    # Default return values
    f_bisection = f_newton = f_newton_prime = f_simpson = f_euler_rk = None
    a = b = a_simpson = b_simpson = x0 = n = x0_euler_rk = x_end = y0 = h = None

    if choice == "1":
        expr = input("Enter the function expression (e.g., x**3 - x - 2): ")
        a = float(input("Enter the lower bound (a): "))
        b = float(input("Enter the upper bound (b): "))
        f_bisection = parse_expression(expr)

    elif choice == "2":
        expr = input("Enter the function expression (e.g., x**3 - x - 2): ")
        expr_prime = input("Enter the derivative expression (e.g., 3*x**2 - 1): ")
        x0 = float(input("Enter the initial guess (x0): "))
        f_newton = parse_expression(expr)
        f_newton_prime = parse_expression(expr_prime)

    elif choice == "3":
        expr = input("Enter the function expression (e.g., x**2): ")
        a_simpson = float(input("Enter the lower bound (a): "))
        b_simpson = float(input("Enter the upper bound (b): "))
        n = int(input("Enter the number of intervals (n): "))
        f_simpson = parse_expression(expr)

    elif choice == "4":
        expr = input("Enter the function expression (e.g., x + y): ")
        y0 = float(input("Enter the initial value (y0): "))
        x0_euler_rk = float(input("Enter the start of the interval (x0): "))
        x_end = float(input("Enter the end of the interval (x_end): "))
        h = float(input("Enter the step size (h): "))
        f_euler_rk = parse_expression(expr)

    elif choice == "5":
        expr = input("Enter the function expression (e.g., x + y): ")
        y0 = float(input("Enter the initial value (y0): "))
        x0_euler_rk = float(input("Enter the start of the interval (x0): "))
        x_end = float(input("Enter the end of the interval (x_end): "))
        h = float(input("Enter the step size (h): "))
        f_euler_rk = parse_expression(expr)

    else:
        print("Invalid choice.")

    return (f_bisection, a, b, f_newton, f_newton_prime, x0, f_simpson, a_simpson, b_simpson, n,
            f_euler_rk, y0, x0_euler_rk, x_end, h)


def plot_results(x, y, title):
    plt.figure()
    plt.plot(x, y, 'o-', label=title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        (f_bisection, a, b, f_newton, f_newton_prime, x0, f_simpson, a_simpson, b_simpson, n,
         f_euler_rk, y0, x0_euler_rk, x_end, h) = get_user_input()

        if f_bisection is not None and a is not None and b is not None:
            try:
                root_bisection = bisection_method(f_bisection, a, b)
                print(f"Root found using Bisection Method: {root_bisection}")
            except ValueError as e:
                print(f"Bisection Method Error: {e}")

        if f_newton is not None and f_newton_prime is not None and x0 is not None:
            try:
                root_newton = newton_raphson_method(f_newton, f_newton_prime, x0)
                print(f"Root found using Newton-Raphson Method: {root_newton}")
            except ValueError as e:
                print(f"Newton-Raphson Method Error: {e}")

        if f_simpson is not None and a_simpson is not None and b_simpson is not None and n is not None:
            try:
                integral_simpsons = simpsons_rule(f_simpson, a_simpson, b_simpson, n)
                print(f"Integral computed using Simpson's Rule: {integral_simpsons}")
            except ValueError as e:
                print(f"Simpson's Rule Error: {e}")

        if f_euler_rk is not None and y0 is not None and x0_euler_rk is not None and x_end is not None and h is not None:
            try:
                x_euler, y_euler = euler_method(f_euler_rk, y0, x0_euler_rk, x_end, h)
                print(f"Euler Method Results: x={x_euler}, y={y_euler}")
                plot_results(x_euler, y_euler, "Euler Method")
            except ValueError as e:
                print(f"Euler Method Error: {e}")

        if f_euler_rk is not None and y0 is not None and x0_euler_rk is not None and x_end is not None and h is not None:
            try:
                x_rk, y_rk = runge_kutta_4(f_euler_rk, y0, x0_euler_rk, x_end, h)
                print(f"Runge-Kutta Results: x={x_rk}, y={y_rk}")
                plot_results(x_rk, y_rk, "Runge-Kutta Method")
            except ValueError as e:
                print(f"Runge-Kutta Method Error: {e}")

        # Prompt the user to continue or exit
        cont = input("Do you want to run another method? (yes/no): ").strip().lower()
        if cont != "yes":
            break


if __name__ == "__main__":
    main()
