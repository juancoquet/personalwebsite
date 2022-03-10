Note type: #litnote
Source: [[📖 Python Cookbook]] ch4.14 p135

---
# Flattening a nested sequence
You can iterate through a nested sequence by defining a flattening function as follows.
```python

from collections.abc import Iterable

def flatten(items, ignore_types=(str, bytes)):
	for item in items:
		if isinstance(item, Iterable) and not isinstance(item, ignore_types):
			yield from flatten(item)
		else:
			yield item


nested = [1, 2, 3, ['juan', 5, 6]]

for x in flatten(nested):
	print(x)		# 1, 2, 3, 'juan', 5, 6
```

This recursive function works by checking if the current item of the sequence being considered is an Iterable type, while not being one of the `ignore_types` to prevent iterating through every character in a string, for example. If the item is iterable and not an ignore type, it uses `yield from` to run a generator sub-routine. This means that a generator runs in the recursion layer below and passes the generated item up to the top-level generator to yield to the main function.