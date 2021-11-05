import numpy as np
import pandas as pd

# Create matrix with the input
matrix_input = np.array(pd.read_csv("./inputs.csv")).transpose()
# Calculate the output
output = np.sum(np.floor(matrix_input / 3) - 2)

# Print the output
print(output)


## part 2

matrix_input = matrix_input.tolist()[0]

total_fuel = 0
for f in matrix_input:
    new_fuel = f
    while True:
        new_fuel = np.floor(new_fuel/3) - 2
        if new_fuel > 0:
            total_fuel += new_fuel
        else:
            break
print(total_fuel)
