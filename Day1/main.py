
import numpy as np
import pandas as pd

# Create matrix with the input
matrix_input = np.array(pd.read_csv("./inputs.csv")).transpose()
# Calculate the output
output = np.sum(np.floor(matrix_input / 3) - 2)

# Print the output
print(output)