import numpy as np
import matplotlib.pyplot as plt


def linear_line_of_best_fit(x, y):
    # m is the gradient | c is the intercept
    m, c = np.polyfit(x, y, deg=1)

    return m, c


def linear_line_of_best_fit_new(x, y):
    """
    There is a newer method that is supposed to be more feature-ful
    It's just got some small differences
    """
    p_fitted = np.polynomial.Polynomial.fit(x, y, deg=1)
    c, m = p_fitted.convert().coef

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

    gradient_new, intercept_new = linear_line_of_best_fit_new(x, y)

    print(f"Gradient is {gradient} | Intercept is {intercept}")
    print(
        f"Using the new method: Gradient is {gradient_new} | Intercept is {intercept_new}"
    )

    # Create a scatter plot of the original data
    plt.scatter(x, y)

    # Plot the line of best fit
    y_fit = gradient * x + intercept
    plt.plot(x, y_fit, "r")

    plt.show()
