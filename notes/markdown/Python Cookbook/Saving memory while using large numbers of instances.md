Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.4 p249

---
# Saving memory while using large numbers of instances
When using large numbers of instances (in the millions), you may need to find a way to save memory. A good way of doing this is by adding `__slots__` to a class if it's a relatively simple data structure.
```python

class Date:
	__slots__ = ['year', 'month', 'day']
	
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
```
The function of `__slots__` is to change the way a class' attributes are internally stored—rather than being stored as key/value pairs inside a dictionary, they are stored as a fixed-size array. Attribute names listed in the `__slots__` specifier are internally mapped to specific indices within this array.

A side effect of using this method is that it will no longer be possible to add more attributes to this class.

Storing a `Date` object such as the one defined above would normally take 428 bytes of data, but after specifying `__slots__`, only 156 bytes is required.

Only use this method when absolutely necessary as there are many parts of internal Python code that rely on normal dictionary-based classes.