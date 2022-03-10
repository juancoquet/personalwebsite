Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.9 p97

---
# Lists vs Numpy arrays
Mathematical functions behave differently on `list` types than on `np.array()` types. The main difference is that numpy applies the mathematical function on a per-element basis, as though looping through each element (but it is much faster than looping).
```python

import numpy as np

my_list = [1, 2, 3, 4]
my_arr = np.array([1, 2, 3, 4])

print(my_list * 2)	# [1, 2, 3, 4, 1, 2, 3, 4]
print(my_arr * 2)	# [2, 4, 6, 8]

print(my_list + 10)	# Traceback error
print(my_arr + 10)	# [11, 12, 13, 14]

other_list = [5, 6, 7, 8]
other_arr = np.array([5, 6, 7, 8])

print(my_list + other_list)	# [1, 2, 3, 4, 5, 6, 7, 8]
print(my_arr + other_arr)	# [6, 8, 10, 12]

print(my_arr * other_arr)	# [5, 12, 21, 32]
```