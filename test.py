import numpy as np
import math
import matplotlib.pyplot as plt

# Example data and histogram
data = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7]
counts, edges = np.histogram(data, bins=7, density=True)

print(counts)