from sympy import lambdify

def bisection_method(f, a, b, tol=1e-5):
    f_numeric = lambdify(x, f)  # Convert symbolic function to numerical function
    if f_numeric(a) * f_numeric(b) >= 0:
        raise ValueError("Function values at the interval endpoints must be of opposite signs.")
    # Continue with bisection method...

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    # Ensure function is evaluated as a number
    fa, fb = f(a), f(b)

    if fa * fb >= 0:
        raise ValueError("Function has the same signs at the endpoints.")

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise ValueError("Maximum iterations exceeded.")
