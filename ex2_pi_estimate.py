##Exercise 1

import random
import math

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
        xp = (xmax-xmin)*random.random() + xmin
        yp = (ymax-ymin)*random.random() + ymin

        ''' xp = random.uniform(xmin, xmax)
            yp = random.uniform(ymin, ymax) 
            
            This also produces the same result as the given formulaes above
        '''
        if (xp - x0)**2 + (yp - y0)**2 <= r**2:
            m += 1

    pi_estimate = 4 * (m / n)
    return pi_estimate


def relative_error(pi_estimate):
    return ((abs(pi_estimate - math.pi)) / math.pi) * 100  # Calculate positive relative error


# List of n values
n_values = [10**4, 10**5, 10**6, 10**7, 10**8]

# Function to run experiments and store results
def run_experiment(series):
    # Loop through the n_values, estimate Pi, and print the results
    for n in n_values:
        pi_estimated = estimate_pi(n)
        rel_error = relative_error(pi_estimated)
        series.append(pi_estimated)

        print(f"Estimated value of pi for n={n} is {pi_estimated}")
        print(f"Relative error for n={n} is {rel_error}%\n")


##Exercise 2

# Initialize lists to store results for each series
Series1 = []
Series2 = []
Series3 = []
Series4 = []
Series5 = []


run_experiment(Series1)
run_experiment(Series2)
run_experiment(Series3)
run_experiment(Series4)
run_experiment(Series5)

# Output the results
print("Series1:", Series1)
print("Series2:", Series2)
print("Series3:", Series3)
print("Series4:", Series4)
print("Series5:", Series5)


##Exercise 3
Avg_Series1 = sum(Series1)/ len(Series1)
Avg_Series2 = sum(Series2)/ len(Series2)
Avg_Series3 = sum(Series3)/ len(Series3)
Avg_Series4 = sum(Series4)/ len(Series4)
Avg_Series5 = sum(Series5)/ len(Series5)

Avg_of_all_series = sum(Avg_Series1 + Avg_Series2 + Avg_Series3 + Avg_Series4 + Avg_Series5) / 5

rel_error_Avg_Series1 = relative_error(Avg_Series1)
rel_error_Avg_Series2 = relative_error(Avg_Series2)
rel_error_Avg_Series3 = relative_error(Avg_Series3)
rel_error_Avg_Series4 = relative_error(Avg_Series4)
rel_error_Avg_Series5 = relative_error(Avg_Series5)

rel_err_Avg_of_all_series = relative_error(Avg_of_all_series)