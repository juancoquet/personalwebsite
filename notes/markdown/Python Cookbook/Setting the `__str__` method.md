Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.1 p244

---
# Setting the `__str__` method
The `__str__` method indicates what should be printed to the console when `print()` is called on an object.
```python

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		return f'x is {self.x}, y is {self.y}'
		
p = Point(2, 3)

print(p)	# x is 2, y is 3
```

---
### See also:
- [[Setting the `__repr__` method]]