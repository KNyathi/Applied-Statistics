import random
import math
import matplotlib.pyplot as plt

r = 5  # Radius of the circle
x0, y0 = 1, 2  # Centre coordinate

# Using input data to find the max and min values of x and y
xmax = x0 + r
xmin = x0 - r
ymax = y0 + r
ymin = y0 - r


def estimate_pi(n):
    m = 0
    for _ in range(n):
        xp = random.uniform(xmin, xmax)
        yp = random.uniform(ymin, ymax)

        if (xp - x0)**2 + (yp - y0)**2 <= r**2:
            m += 1

    pi_estimate = 4 * (m / n)
    return pi_estimate


def relative_error(pi_estimate):
    return ((abs(pi_estimate - math.pi)) / math.pi) * 100  # Calculate positive relative error


# List of n values
n_values = [10**3, 10**4, 10**5, 10**6]

# Lists to store results
pi_estimates = []
errors = []

# Loop through the n_values, estimate Pi, and store the results
for n in n_values:
    pi_estimated = estimate_pi(n)
    rel_error = relative_error(pi_estimated)

    pi_estimates.append(pi_estimated)
    errors.append(rel_error)

    print(f"Estimated value of pi for n={n} is {pi_estimated}")
    print(f"Relative error for n={n} is {rel_error}%\n")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Experiments (n)')
plt.ylabel('Relative Error (%)')
plt.title('Relative Error vs. Number of Experiments')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
