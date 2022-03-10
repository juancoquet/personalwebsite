Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.4 p8

---
# Using `heapq.nsmallest/largest` to find the smallest or largest N items
For cases where N is small relative to the total length of items you're searching through, `heapq` is a far better alternative than using `.sort()` and slicing due to runtime (`heapq` has O(logN) complexity).
```python
import heapq
nums = [1, 8 ,2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))	#[42, 37, 23]
print(heapq.nsmallest(3, nums))	# [-4, 1, 2]
```

A `key` argument can also be provided to sort by complex criteria (see [[Lists can be sorted by a specific attribute]]).