Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.5 p250

---
# Using `_internal` attributes and methods
Attributes and functions names with a single leasing underscore are considered *internal* or *protected*. This means that they serve some internal purpose for the class in which they belong, and should not be accessed by users of the code.

Python does not prevent a user from accessing these private names, but it is considered impolite to do so and can lead to fragile code—these names were made private by the author of the code for a reason.
```python

class A:
	def __init__(self):
		self._internal_ = 0
		self.public = 1
		
	def public_method(self):
		'''
		For users of the class to call
		'''
	
	def _internal_method(self):
		'''
		For internal use
		'''
	
```

---
### See also:
- [[Pythonic naming conventions]]