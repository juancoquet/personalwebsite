Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.1 p243

---
# Setting the `__repr__` method
The `__repr__` method of a class is used to output a representation of the object, and it is called when the `repr()` function is called with an object as its argument. By convention, `__repr__` is set to output to the console the code that would have created the object in question.
```python

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f'Point({self.x}, {self.y})'
```

In the above example, when `repr()` is called on a `Point` instance, the instance's `__repr__` method will be called which outputs the code required to create that particular object.
```python
# within shell

>>> p = Point(2, 3)
>>> p
Point(2, 3)
```
```python

p = Point(2, 3)
repr(point)		# outputs 'Point(2, 3)' to the console
```