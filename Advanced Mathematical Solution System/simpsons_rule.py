def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Number of intervals must be even.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral
