def non_mutually_exclusive_probability(*args):
    """
    Calculate the probability of non-mutually exclusive events using the inclusion-exclusion principle.
    """
    total_prob = 0
    event_sums = args[0]  # Event probabilities
    intersections = args[1]  # Intersections of two or more events
    
    # Add individual event probabilities
    for event in event_sums:
        total_prob += event
    
    # Subtract pairwise intersections
    for intersection in intersections:
        total_prob -= intersection

    # Add back intersections of all events
    if len(args) == 3:
        all_intersection = args[2]  # Intersection of all events
        total_prob += all_intersection
    
    if 0 <= total_prob <= 1:
        return total_prob
    
    print("Error: Probability must be between 0 and 1. Try to think and input meaningful values.")
    return None

def result_non_mutual(event_probs, pair_intersections, all_intersection=None):
    """
    Display the result of non-mutually exclusive probability calculation.
    """
    prob = non_mutually_exclusive_probability(event_probs, pair_intersections, all_intersection)
    if prob is not None:
        print(f"The probability of non-mutually exclusive events is: {prob:.4f}")

# Example for three non-mutually exclusive events
P_A = 0.3
P_B = 0.6
P_C = 0.5

# Pairwise intersections
P_AnB = 0.2
P_AnC = 0.1
P_BnC = 0.15

# Intersection of all three events
P_AnBnC = 0.05

# Calculate the union of three events
event_probs = [P_A, P_B, P_C]
pair_intersections = [P_AnB, P_AnC, P_BnC]
all_intersection = P_AnBnC

result_non_mutual(event_probs, pair_intersections, all_intersection)

# Example for two non-mutually exclusive events
P_A = 0.3
P_B = 0.6
P_AnB = 0.2

# Calculate the union of two events
result_non_mutual([P_A, P_B], [P_AnB])
