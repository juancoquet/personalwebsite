Note type: #litnote
Source: [[📖 Effective Python]] item 72

---
# Using `bisect`
Using the `bisect` module can dramatically increase the speed of searching through an ordered list or other containers. `bisect` is a binary search algorithm, meaning that runtime increases logarithmically (O(log N)) as the size of the data set increases. Compared to a linear search algorithm (iterating through every list item using a `for` loop) whose runtime increases linearly, the `bisect` module can significantly improve performance.
```python
from bisect import bisect_left

data = list(range(10**5))		# list of 100k items

index = bisect_left(data, 91234)		# find the index position of the number 91234
print(index)

>>>
91234			# returns the correct index
```