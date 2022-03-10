Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.12 p20

---
# Using `collections.Counter` to find most common items
The `Counter` object from the `collections` library is great for finding the most common item (or items) from a sequence. It has a built-in method—`most_common()` for just this purpose.
```python
from collections import Counter


my_list = ['one', 'two', 'two', 'two', 'three', 'three']
item_counts = Counter(my_list)
top_two = item_counts.most_common(2)	# [('two', 3), ('three', 2)]
```

---
### See also:
- [[`collections.Counter` features]]