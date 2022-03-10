Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.9 p15

---
# Set operations can be used on dictionary `.keys()` and `.items()` calls
[Set operations](https://miro.medium.com/max/3200/0*a02OPI3-TnbKXyub.png) such as unions, intersections and differences can be used on the return values of `.keys()` and `.items()`.

This is useful for identifying commonalities and differences between two dictionaries.
```python
a = {
	'x': 1,
	'y': 2,
	'z': 3,
}

b = {
	'w': 10,
	'x': 11,
	'y': 2,
}


# Find keys in common
a.keys() & b.keys()		# {'x', 'y'}

# Find keys in a that are not in b
a.keys() - b.keys()		# {'z'}

# Find (key, value) pairs in common
a.items() & b.items()	# {('y', 2)}
```

This is handy for filtering and altering dictionary contents, e.g. within a dict comprehension.
```python
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
```

The return of the `.values()` call does not support the same operation as the items contained in a dictionary's values are not guaranteed to be unique. If this kind of functionality is required for the values, a `set` of the values can be created first.