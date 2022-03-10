Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.12 p21

---
# `collections.Counter` features
Under the hood, counter objects are dictionaries that map the items to the respective number of occurrences.
```python
from collections import Counter


my_list = ['one', 'two', 'two', 'two', 'three', 'three']
item_counts = Counter(my_list)

print(item_counts['one'])		# 1
print(item_counts['two'])		# 3
print(item_counts['three'])		# 2
```

This means that individual counts can be manipulated by indexing into them directly.
```python

item_counts['one'] += 1
print(item_counts['one'])		# 2

print(item_counts)	# {'one': 2, 'two': 3, 'three': 2}
```

Another feature of `Counter` objects is that they can be added to, and subtracted from each other.
```python

other_list = ['one', 'one', 'two', 'three']
other_counts = Counter(other_list)

aggregate = item_counts + other_counts

print(aggregate)	# {'one': 4, 'two': 4, 'three': 3}
```