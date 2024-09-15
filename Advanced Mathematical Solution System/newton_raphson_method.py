def newton_raphson_method(f, f_prime, x0, tol=1e-8, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Maximum iterations exceeded.")
