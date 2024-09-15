from sympy import lambdify

def runge_kutta_4(f, x0, y0, x_end, h):
    f_numeric = lambdify((x, y), f)  # Convert symbolic function to numerical function
    # Initialize variables...
    for i in range(1, num_steps):
        k1 = h * f_numeric(x[i - 1], y[i - 1])
        # Compute other k values and update y...
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
