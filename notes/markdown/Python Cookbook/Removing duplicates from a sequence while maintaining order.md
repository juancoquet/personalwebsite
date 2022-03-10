Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.10 p17

---
# Removing duplicates from a sequence while maintaining order
Duplicates can be easily removed from a sequence, such as a `list` type, by converting it into a set (`set(my_list)`). However, this will scramble the order of the items.

To maintain the original order after removing duplicates, a simple function can be defined as follows:
```python
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)
```

The above function works well if the items contained in the sequence are hashable. For non-hashable types such as dictionaries, a `key` argument can be defined to take a function to be used to convert the items into a hashable type. This method can also be used to eliminate duplicates by a specific attribute of a larger data structure.
```python
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)
```

The first line of the `for` loop above says that `val` is the `item` itself if `key` was not provided, but if `key` was provided, use this `key` function to detect duplicates.
```python
a = [
	{'x': 1, 'y': 2},
	{'x': 1, 'y': 3},
	{'x': 1, 'y': 2},	# dupe
	{'x': 2, 'y': 4},
]

print list(dedupe(a, key=lambda d: (d['x'], d['y'])))
# [{'x':1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
```

The above block of code uses the `key` argument in the `dedupe` function to index into the `x` and `y` values of each item in the list, and then creates a tuple of these items for the purpose of comparing. If a created tuple already exists in the `seen` variable, the `item` to which that tuple belongs will not be yielded.