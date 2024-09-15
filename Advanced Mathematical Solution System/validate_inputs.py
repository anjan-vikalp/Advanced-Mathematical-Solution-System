def validate_inputs(x0, x_end, h):
    if x_end < x0:
        raise ValueError("End value x_end must be greater than or equal to start value x0.")
    if h <= 0:
        raise ValueError("Step size h must be positive.")
    if (x_end - x0) / h < 1:
        raise ValueError("The range between x0 and x_end is too small for the given step size h.")
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

    # Validate inputs
    if x0_euler_rk >= x_end:
        raise ValueError("Start of interval (x0) must be less than end of interval (x_end).")
    if h <= 0:
        raise ValueError("Step size (h) must be positive.")

    return expr, a, b, x0, a_simpson, b_simpson, n, y0, x0_euler_rk, x_end, h
