# false_position_method.py

from sympy import symbols, lambdify, sympify

# Define symbolic variables
x = symbols('x')

def false_position_method(a, b, tolerance, max_iterations, expr):
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
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)

        if abs(fc) < tolerance or abs(b - a) < tolerance:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c
