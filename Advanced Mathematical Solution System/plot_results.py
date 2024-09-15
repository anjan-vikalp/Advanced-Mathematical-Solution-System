from methods_call import x_euler, y_euler, x_rk, y_rk
import matplotlib.pyplot as plt

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
