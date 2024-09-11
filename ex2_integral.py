
import random

xmin = 0
xmax = 2
ymin = 1
ymax = 9


def f(x):
    return x ** 3 + 1

def estimate_integral(n):
    m = 0
    for _ in range(n):
        xp = (xmax-xmin) * random.random() + xmin
        yp = (ymax-ymin) * random.random() + ymin

        if f(x) > y:
            m += 1

    integral_estimate = 4 * (m / n)
    return integral_estimate

def relative_error(integral_estimate):
    return ((abs(integral_estimate - 6)) / 6) * 100  # Calculate positive relative error




n_values = [10**4, 10**5, 10**6, 10**7]

# Function to run experiments and store results
def run_experiment(series):
    # Loop through the n_values, estimate Pi, and print the results
    for n in n_values:
        integral_estimate = estimate_integral(n)
        rel_error = relative_error(integral_estimate)
        series.append(integral_estimate)

        print(f"Estimated value of pi for n={n} is {integral_estimate}")
        print(f"Relative error for n={n} is {rel_error}%\n")