import math

# Linear Congruential Generator to generate random numbers between 2 and 4
def linear_congruential_generator(a, b, M, seed, n):
    random_numbers = []
    x = seed  # starting value (seed)
    
    for _ in range(n):
        # Apply the LCM formula: x_{i+1} = (a * x_i + b) % M
        x = (a * x + b) % M
        # Scale random numbers between 2 and 4
        random_numbers.append(2 + 2 * (x / M))
    
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

# Function to normalize data between 0 and 1
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Parameters
a = 17      # multiplier
b = 1       # increment
M = 1000    # modulus
seed = 1    # starting value (x_0)
n = 10      # number of random numbers to generate

# Generate random numbers using LCM between 2 and 4
random_numbers = linear_congruential_generator(a, b, M, seed, n)

# Normalize the random numbers between 0 and 1
normalized_random_numbers = normalize(random_numbers)

# Calculate statistics for the original data
mean_value = mean(random_numbers)
mean_sq_value = mean_of_squares(random_numbers)
variance_value = unbiased_sample_variance(random_numbers, mean_value, mean_sq_value)
std_dev = standard_deviation(variance_value)

# Calculate statistics for the normalized data
mean_normalized = mean(normalized_random_numbers)
mean_sq_normalized = mean_of_squares(normalized_random_numbers)
variance_normalized = unbiased_sample_variance(normalized_random_numbers, mean_normalized, mean_sq_normalized)
std_dev_normalized = standard_deviation(variance_normalized)

# Display results
print(f"Generated Random Numbers (Original): {random_numbers}")
print(f"Mean (Original): {mean_value}")
print(f"Variance (Original): {variance_value}")
print(f"Standard Deviation (Original): {std_dev}")

print("\nNormalized Random Numbers (0 to 1):", normalized_random_numbers)
print(f"Mean (Normalized): {mean_normalized}")
print(f"Variance (Normalized): {variance_normalized}")
print(f"Standard Deviation (Normalized): {std_dev_normalized}")
