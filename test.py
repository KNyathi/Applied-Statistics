import random

def sum_of_random_frequencies_from_random_numbers(num_frequencies):
    """
    Generates random numbers and normalizes them to create random frequencies that sum to 1.
    
    Parameters:
    num_frequencies (int): Number of random frequencies to generate.
    
    Returns:
    list: A list of random frequencies that sum to 1.
    """
    # Step 1: Generate random numbers
    random_numbers = [random.random() for _ in range(num_frequencies)]
    
    # Step 2: Normalize the numbers to create frequencies
    total_sum = sum(random_numbers)
    frequencies = [num / total_sum for num in random_numbers]
    
    return frequencies

# Example usage
random_frequencies = sum_of_random_frequencies_from_random_numbers(4)
print("Random frequencies:", random_frequencies)
print("Sum of frequencies:", sum(random_frequencies))  # This should be very close to 1
