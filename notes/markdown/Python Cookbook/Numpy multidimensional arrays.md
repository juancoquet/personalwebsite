Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.9 p99

---
# Numpy multidimensional arrays
Multidimensional numpy arrays can be index-accessed in a similar way to standard lists.
```python

import numpy as np

arr = np.array([
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
])

arr[1]		# Row 1, [1, 2, 3, 4]
arr[:,1]		# Colummn 1, [2, 6, 10]
arr[1:3, 1:3]	# Sub-region, [ [6, 7], [10, 11] ]

arr[1:3, 1:3] + 10	# modifying the sub-region
# [ [1, 2, 3, 4],
#	[5, 16, 17, 8],
#	[9, 20, 21, 12] ]
	
arr + [100, 101, 102, 103]	# broadcast a row vector on all rows
# [ [101, 103, 105, 107],
#	[105, 117, 119, 111],
#	[109, 121, 123, 115] ]

np.where(arr < 10, arr, 10)
# replace all values greater than 10 with 10
```