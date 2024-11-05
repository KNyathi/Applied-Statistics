import numpy as np
from scipy.stats import norm, t, chi2
import matplotlib.pyplot as plt
import math

# Given sequences
a1 = [9.577, 12.628, 11.003, 12.512]
a2 = [12.718, 6.167, 9.919, 12.095, 5.811, 5.706]
a3 = [12.016323622186091, 9.259246505609095, 17.345717938437094, 5.900356369978998, 13.68768256707768, 6.507839378250566, 13.61900518222573, 5.948196429498942, 12.475855480039662, 7.66352639971797]
a4 = [11.896107580638313, 12.354328210962015, 5.35925979227144, 13.891229335546084, 10.170697806598511, 9.255832053277832, 16.561279953259266, 10.498005569850374, 9.716219531175344, 14.094420948209105, 9.558324283707853, 18.491552980442233]

# Function to calculate mean of a sample
def mean_sample(data):
    return sum(data) / len(data)

# Function to calculate mean of squares of sample
def mean_of_squares_sample(data):
    return sum(x**2 for x in data) / len(data)

# Function to calculate unbiased sample variance
def unbiased_sample_variance(data, mean_sample, mean_of_squares_sample):
    N = len(data)
    if N < 2:
        return None
    return (N / (N - 1)) * (mean_of_squares_sample - mean_sample**2)

# Function to calculate standard deviation
def standard_deviation(variance_value):
    if variance_value is None or variance_value == 0:
        return None
    return math.sqrt(variance_value)

# Function to calculate statistics and confidence intervals for standard deviation
def calculate_statistics_and_intervals(sequence, p):
    mean = mean_sample(sequence)
    mean_square = mean_of_squares_sample(sequence)
    variance = unbiased_sample_variance(sequence, mean, mean_square) 
    std_dev = standard_deviation(variance)
    n = len(sequence)

    # Chi-squared critical values
    chi2_upper = chi2.ppf(1 - p / 2, df=n - 1)
    chi2_lower = chi2.ppf(p / 2, df=n - 1)
    
    # Confidence interval for standard deviation
    s_min_2 = ((std_dev**2) * (n - 1)) / chi2_upper
    s_max_2 = ((std_dev**2) * (n - 1)) / chi2_lower
    s_min = math.sqrt(s_min_2)
    s_max = math.sqrt(s_max_2)

    return std_dev, s_min, s_max

# Calculate the standard deviation and intervals for each sequence at p = 0.1
p = 0.1


n_values = [len(a1), len(a2), len(a3), len(a4)]
std_devs = []
std_min_intervals = []
std_max_intervals = []

for seq in [a1, a2, a3, a4]:
    std_dev, s_min, s_max = calculate_statistics_and_intervals(seq, p)
    std_devs.append(std_dev)
    std_min_intervals.append(s_min)
    std_max_intervals.append(s_max)


# Calculate M_s (mean of all means)
std_avg = math.sqrt((3*(std_devs[0]**2) + 5*(std_devs[1]**2) + 9*(std_devs[2]**2) + 11*(std_devs[3]**2))/(4+6+10+12-4))
Std_values = [std_avg] * len(n_values)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, std_devs, marker='o', label='Std_i (Calculated Standard Deviation)')
plt.plot(n_values, Std_values, marker='o', linestyle='dashdot', label="Ms (Mean of Means)", color="blue")
plt.plot(n_values, std_min_intervals, marker='x', linestyle='--', label='Std Min_i (Lower Bound)')
plt.plot(n_values, std_max_intervals, marker='x', linestyle='--', label='Std Max_i (Upper Bound)')
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Sample Size (n)')
plt.ylabel('Standard Deviation')
plt.title('Confidence Intervals for Standard Deviation')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.show()
