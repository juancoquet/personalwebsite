Note type: #litnote
Source: [[📖 Effective Python]] item 87

---
# Using an exception base-class
By defining a base-class which inherits from the built in `Exception` class, you can make it easy for callers of the code to handle deliberate exceptions by writing a 'catch' for this new base error class. The way this works is that a base-class is created which inherits from `Exception`, and then all custom exceptions created for your code will inherit from this new base class.
```python
class BaseError(Exception):
	"""Base-class for all exceptions in this module."""
	
class CustomError1(BaseError):
	"""Error raised when..."""

class CustomError2(BaseError):
	"""Error raised when..."""

def my_function(value):
	if value < 0:
		raise CustomError1('Value must be greater than 0')
	...
	
```

---
#### See also:
- [[Inheriting from `Exception`]]