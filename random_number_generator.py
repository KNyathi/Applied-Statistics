import math

# Linear Congruential Generator
def linear_congruential_generator(a, b, M, seed, n):
    random_numbers = []
    x = seed  # starting value (seed)
    random_numbers.append(x / M)

    for _ in range(n):
        # Apply the LCM formula: x_{i+1} = (a * x_i + b) % M
        x = (a * x + b) % M
        # Generate the random number between 0 and 1 by dividing by M
        random_numbers.append(x / M)
    
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

# Parameters
a = 17      # multiplier
b = 1       # increment
M = 1000    # modulus
seed = 1    # starting value (x_0)
n = 9      # number of random numbers to generate
runs = 1000 # number of simulation runs

# Lists to store simulation results
mean_list = []
variance_list = []
std_dev_list = []

for run in range(runs):
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
    
    # Store the results
    mean_list.append(mean_value)
    variance_list.append(variance_value)
    std_dev_list.append(std_dev)
    
    # Update seed for next run (optional, depending on desired behavior)
    # For LCM, typically you continue the sequence, but here we reset to seed
    # To continue the sequence, uncomment the following line:
    # seed = (a * seed + b) % M

# Calculate aggregate statistics
overall_mean = mean(mean_list)
overall_variance = mean(variance_list)
overall_std_dev = mean(std_dev_list)

# Display aggregate results
print(f"After {runs} simulation runs with {n} random numbers each:")
print(f"Average Mean: {overall_mean}")
print(f"Average Unbiased Sample Variance: {overall_variance}")
print(f"Average Standard Deviation: {overall_std_dev}")
print(f"Random numbers: {random_numbers}")