# Create a 2D array using lists of lists
rows, cols = 3, 3
two_d_array = [[0 for _ in range(cols)] for _ in range(rows)]

# Print the 2D array
for row in two_d_array:
    print(row)

import array

# Create a 2D array using the array module
rows, cols = 3, 3
two_d_array = [array.array('i', [0] * cols) for _ in range(rows)]

# Print the 2D array
for row in two_d_array:
    print(row)
print(two_d_array)

import numpy as np

# Create a 2D array using numpy
rows, cols = 3, 3
two_d_array = np.zeros((rows, cols), dtype=int)

# Print the 2D array
print(two_d_array)
