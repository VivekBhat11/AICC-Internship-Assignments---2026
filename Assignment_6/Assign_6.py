"""

Assignment (20/02/2026)
Assignment Name : NumPy Speed Test
Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.

This program compares the performance of Python lists and NumPy arrays using 1 million numbers. It measures execution time for performing the same operation (multiplication). The results show how NumPy is faster due to optimized operations and vectorization. This helps in understanding why NumPy is widely used in data science and AI.

"""

import time
import numpy as np

# Create 1 million numbers
size = 1000000

# Python list
start = time.time()
py_list = [i for i in range(size)]
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python List Time:", end - start)

# NumPy array
start = time.time()
np_array = np.arange(size)
np_result = np_array * 2
end = time.time()
print("NumPy Array Time:", end - start)


"""
3 Observations
NumPy arrays execute operations much faster than Python lists.
NumPy uses vectorized operations, which reduces the need for loops.
Python lists are slower because they process elements one by one.

"""