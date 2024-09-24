# secant_method.py

from sympy import symbols, lambdify, sympify

# Define symbolic variables
x = symbols('x')

def secant_method(x0, x1, tolerance, max_iterations, expr):
    x0 = float(x0)
    x1 = float(x1)
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)
    expr = sympify(expr)

    f = lambdify(x, expr, 'numpy')

    for _ in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero in the Secant method.")

        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        if abs(x2 - x1) < tolerance:
            return x2

        x0, x1 = x1, x2

    return x2
