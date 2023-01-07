# Install the numpy package
import numpy as np

import pandas as pd

# Make a function that
a = 2
b = 3
print(a + b)

# A function that takes two inputs that are numbers and returns an array with the numbers being the first and the second dimension of the array
def make_array(x, y):
    return np.zeros((x, y))

make_array(2, 3)
