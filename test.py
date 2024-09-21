import math
import numpy as np
from scipy.stats import chi2

# Linear Congruential Generator
def linear_congruential_generator(a, b, M, seed, n):
    random_numbers = []
    x = seed  # starting value (seed)
    random_numbers.append(x / M)

    for _ in range(n):
        # Apply the LCM formula: x_{i+1} = (a * x_i + b) % M
        x = (a * x + b) % M 

        #Random number to be between A=0 and B=10
        random= (10-0)*(x/M) + 0 #(xmax-xmin)*random + xmin

        random_numbers.append(round(random, 8)) 
        #random_numbers.append(random)

    return random_numbers

# Function to calculate mean
def mean(data):
    return sum(data) / len(data)


# Function to calculate mean of squares
def mean_of_squares(data):
    return sum(x**2 for x in data) / len(data)


# Function to calculate unbiased sample variance
def unbiased_sample_variance(data, mean_value, mean_sq_value):
    N = len(data)
    if N < 2:
        raise ValueError("Variance requires at least two data points.")
    return (N / (N - 1)) * (mean_sq_value - mean_value**2)


# Function to calculate standard deviation
def standard_deviation(variance_value):
    return math.sqrt(variance_value)

def relative_error(expectation):
    #(max_x+min_x)/2 - theoretical mathematical expectation
    return ((abs(expectation - 5)) / 5) * 100  

def relative_err_var(variance):
    #((max_x-min_x)**2)/12 -  theoretical variance
    return ((abs(variance - (10**2/12))) / (10**2/12)) * 100 

def simulations():

    for _ in range(1):
        # Generate random numbers using LCM
        random_numbers = linear_congruential_generator(a, b, M, seed, n)
        
        # Calculate the mean
        mean_value = mean(random_numbers)
        
        # Calculate the mean of squares
        mean_sq_value = mean_of_squares(random_numbers)
        
        # Calculate the unbiased sample variance
        variance_value = unbiased_sample_variance(random_numbers, mean_value, mean_sq_value)
        
        # Calculate the standard deviation
        std_dev = standard_deviation(variance_value)
        
        relative_err = relative_error(mean_value)

        relative_err_variance = relative_err_var(variance_value)
    
    return random_numbers, mean_value, variance_value, std_dev, relative_err, relative_err_variance


def check_repeated_numbers(random_numbers):
    count_dict = {}  # Dictionary to store numbers and their counts
    
    # Loop through each number in random_numbers
    for num in random_numbers:
        # If the number already exists in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        else:
            # If the number doesn't exist, add it with a count of 1
            count_dict[num] = 1

    # Prepare the results
    unique_numbers = list(count_dict.keys())  # List of unique numbers
    repeat_counts = list(count_dict.values())  # List of counts for each unique number

    return unique_numbers, repeat_counts

def aggregate():

    # Display aggregate results
    print(f"After a simulation with {n + 1} random numbers each:")

    print(f"Random numbers: {random_numbers}")
    #print(f"Random numbers: {[f'{num:.2f}' for num in random_numbers]}")

    print(f"Max_Random is {max(random_numbers)}")
    print(f"Min_Random is {min(random_numbers)}")

    print(f"Mathematical Expectation: {mean_value}")

    print(f"Unbiased Sample Variance: {variance_value}")

    print(f"Standard Deviation: {std_dev}")

    print(f"Relative Error for Mathematical Expectation: {relative_err}%")

    print(f"Relative Error for Variance: {relative_err_variance}%")

    if any(n > 1 for n in repeat_counts):
        print("The set contains repeated numbers")
        print(f"Unique numbers: {unique_numbers}")
        print(f"Repeat counts: {repeat_counts}\n")
   

def relative_frequencies(random_sample, left_boundary, right_boundary, num_plots):
    # Determine the width of each interval (bin)
    interval_width = (right_boundary - left_boundary) / num_plots
    
    # Initialize a list to hold the frequency count for each interval
    frequency_counts = [0] * num_plots
    
    # Loop through the random sample and count which interval each number falls into
    for num in random_sample:
        # Check if the number is within the specified boundaries
        if left_boundary <= num <= right_boundary:
            # Determine which interval the number falls into
            index = int((num - left_boundary) // interval_width)
            
            # Edge case for the rightmost boundary
            if index == num_plots:
                index -= 1
            
            # Increment the count for that interval
            frequency_counts[index] += 1
    
    # Convert the frequency counts to relative frequencies
    total_numbers = len(random_sample)
    relative_frequencies = [count / total_numbers for count in frequency_counts]
    
    return relative_frequencies


import matplotlib.pyplot as plt

def relative_frequencies(random_sample, left_boundary, right_boundary, num_plots):
    # Determine the width of each interval (bin)
    interval_width = (right_boundary - left_boundary) / num_plots
    
    # Initialize a list to hold the frequency count for each interval
    frequency_counts = [0] * num_plots
    
    # Loop through the random sample and count which interval each number falls into
    for num in random_sample:
        # Check if the number is within the specified boundaries
        if left_boundary <= num <= right_boundary:
            # Determine which interval the number falls into
            index = int((num - left_boundary) // interval_width)
            
            # Edge case for the rightmost boundary
            if index == num_plots:
                index -= 1
            
            # Increment the count for that interval
            frequency_counts[index] += 1
    
    # Convert the frequency counts to relative frequencies
    total_numbers = len(random_sample)
    relative_frequencies = [count / total_numbers for count in frequency_counts]
    
    return relative_frequencies


def draw_histogram(random_sample, left_boundary, right_boundary, num_plots, relative_frequencies):
    # Calculate the bin edges
    bins = [left_boundary + (i * (right_boundary - left_boundary) / num_plots) for i in range(num_plots + 1)]
    
    # Create the histogram plot
    plt.figure(figsize=(8, 6))
    plt.bar(range(num_plots), relative_frequencies, width=1, align='center', edgecolor='black', tick_label=[f'{bins[i]:.1f}-{bins[i+1]:.1f}' for i in range(len(bins)-1)])
    
    # Labeling the axes
    plt.xlabel('Intervals')
    plt.ylabel('Relative Frequency')
    plt.title('Relative Frequency Histogram')
    
    # Show the plot
    plt.show()




# Function to calculate the Pearson Chi-Square criterion
def pearson_chi_square(relative_frequencies, num_plots):
    # Calculate observed relative frequencies
    observed_frequencies = relative_frequencies
    
    # Total number of samples
    total_samples = n
    
    # Convert observed frequencies to actual observed counts
    observed_counts = [freq * total_samples for freq in observed_frequencies]
    
    # Expected counts for a uniform distribution (evenly distributed across all bins)
    expected_count = total_samples / num_plots
    expected_counts = [expected_count] * num_plots
    
    # Calculate the Pearson Chi-Square statistic
    chi_square_statistic = sum(((o - e) ** 2) / e for o, e in zip(observed_counts, expected_counts))
    
    return chi_square_statistic





# Parameters
a = 22695477      # multiplier
b = 1       # increment
M = 2**32   # modulus
seed = 1    # starting value (x_0)


n_values = [10**2-1, 10**3-1, 10**4-1, 10**5-1]

for n in n_values:

    if M>=0:
        if a> 0 and a<M:
            if b>0 and b<M:
                if seed>0 and seed<M:
                    random_numbers, mean_value, variance_value, std_dev, relative_err, relative_err_variance = simulations()
                    unique_numbers, repeat_counts = check_repeated_numbers(random_numbers)
                    #aggregate()

                    left_boundary = 0  # Minimum boundary of the range
                    right_boundary = 10  # Maximum boundary of the range
                    num_plots = 10  # Number of intervals (bins)

                    frequencies = relative_frequencies(random_numbers, left_boundary, right_boundary, num_plots)
                    print(f"Relative Frequencies: {frequencies}")

                    draw_histogram(random_numbers, left_boundary, right_boundary, num_plots, frequencies)


                    # Calculate the Pearson Chi-Square statistic
                    chi_square_stat = pearson_chi_square(frequencies, num_plots)
                    print(f"Pearson Chi-Square statistic: {chi_square_stat}")


                    # Calculate the p-value
                    degrees_of_freedom = num_plots - 1
                    p_value = chi2.cdf(chi_square_stat, degrees_of_freedom)

                    print(f"Chi-Squared statistic: {chi_square_stat}")
                    print(f"P-value: {p_value}")
