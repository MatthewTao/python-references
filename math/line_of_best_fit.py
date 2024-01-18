import numpy as np
import matplotlib.pyplot as plt


def linear_line_of_best_fit(x, y):
    # m is the gradient | c is the intercept
    m, c = np.polyfit(x, y, deg=1)

    return m, c


def generate_random_linear_data():
    np.random.seed(0)

    # Generate data
    x = np.linspace(0, 10, 100)
    y = 3 * x + 2 + np.random.randn(100)
    return x, y


if __name__ == "__main__":
    x, y = generate_random_linear_data()
    gradient, intercept = linear_line_of_best_fit(x, y)

    print(f"Gradient is {gradient} | Intercept is {intercept}")

    # Create a scatter plot of the original data
    plt.scatter(x, y)

    # Plot the line of best fit
    y_fit = gradient * x + intercept
    plt.plot(x, y_fit, "r")

    plt.show()
