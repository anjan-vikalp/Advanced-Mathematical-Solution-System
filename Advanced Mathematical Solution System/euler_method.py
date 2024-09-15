from sympy import lambdify

def euler_method(f, x0, y0, x_end, h):
    f_numeric = lambdify((x, y), f)  # Convert symbolic function to numerical function
    # Initialize variables...
    for i in range(1, num_steps):
        y[i] = y[i - 1] + h * f_numeric(x[i - 1], y[i - 1])
    return x, y

def euler_method(f, y0, x0, x_end, h):
    if x_end <= x0:
        raise ValueError("End of interval must be greater than start.")
    if h <= 0:
        raise ValueError("Step size must be positive.")

    # Adjust the end value to ensure it's included in the range
    x = np.arange(x0, x_end + h, h)

    # Handle cases where the interval might be too small
    if len(x) == 0:
        raise ValueError("The interval with the given step size results in no points.")

    y = np.zeros(len(x))
    y[0] = y0

    for i in range(1, len(x)):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])

    return x, y
