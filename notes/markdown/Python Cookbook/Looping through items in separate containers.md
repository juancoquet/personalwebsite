Note type: #litnote
Source: [[📖 Python Cookbook]] ch4.12 p131

---
# Looping through items in separate containers
The `chain()` function from `itertools` allows you to chain together multiple iterables in order to loop through them in succession. This is a more elegant solution than setting up two `for` loops, one for each iterable, each of which executes the same process on every item.
```python

from itertools import chain

nums = [1, 2, 3]
letters = ['a', 'b', 'c']

for item in chain(nums, letters):
	print(item)					# 1, 2, 3, a, b, c
```
