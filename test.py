import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given sequences
a1 = [9.577, 12.628, 11.003, 12.512]
a2 = [12.718, 6.167, 9.919, 12.095, 5.811, 5.706]
a3 = [12.016323622186091, 9.259246505609095, 17.345717938437094, 5.900356369978998, 13.68768256707768, 6.507839378250566, 13.61900518222573, 5.948196429498942, 12.475855480039662, 7.66352639971797]
a4 = [11.896107580638313, 12.354328210962015, 5.35925979227144, 13.891229335546084, 10.170697806598511, 9.255832053277832, 16.561279953259266, 10.498005569850374, 9.716219531175344, 14.094420948209105, 9.558324283707853, 18.491552980442233]

# List of sequences
sequences = [a1, a2, a3, a4]

# Function to calculate mean of a sample
def mean_sample(data):
    return sum(data) / len(data)

# Function to calculate unbiased sample variance
def unbiased_sample_variance(data):
    N = len(data)
    mean = mean_sample(data)
    mean_square = sum(x**2 for x in data) / N
    return (N / (N - 1)) * (mean_square - mean**2)

# Calculate statistics and confidence intervals for each sequence
mean_values = []
lower_bounds = []
upper_bounds = []
individual_means = []

# Confidence level
p = 0.1
for seq in sequences:
    n = len(seq)
    mean = mean_sample(seq)
    variance = unbiased_sample_variance(seq)
    std_dev = math.sqrt(variance)
    
    # Store individual means
    individual_means.append(mean)
    
    # Calculate confidence interval for the mean
    normal_quantile = norm.ppf(1 - p / 2)
    margin_error = normal_quantile * (std_dev / math.sqrt(n))
    lower_bounds.append(mean - margin_error)
    upper_bounds.append(mean + margin_error)
    mean_values.append(mean)

# Calculate M_s (mean of all means)
mean_of_means = sum(mean_values) / len(mean_values)
M_s_values = [mean_of_means] * len(sequences)

# Plotting the results
n_values = [4, 6, 10, 12]

plt.figure(figsize=(10, 6))
plt.plot(n_values, M_s_values, marker='o', linestyle='dashdot', label="Ms (Mean of Means)", color="blue")
plt.plot(n_values, lower_bounds, marker='o', linestyle='--',  label="M_min_i (Lower Bound)", color="red")
plt.plot(n_values, upper_bounds, marker='o', linestyle='--', label="M_max_i (Upper Bound)", color="green")
plt.plot(n_values, individual_means, marker='o', label="Mi (Individual Means)", color="purple")

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Ni (Sample Size)')
plt.ylabel('Mean Value')
plt.title('Confidence Intervals for Mean')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
