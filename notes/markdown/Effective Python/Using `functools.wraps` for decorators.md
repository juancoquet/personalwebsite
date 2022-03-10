Note type: #litnote
Source: [[📖 Effective Python]] item 26

---
# Using `functools.wraps` for decorators
The `wraps` helper function form the `functools` built-in module is a decorator that helps you write decorators. When applied to a wrapper function, it copies all relevant metadata from the innermost function to the outermost function.
```python
from functools import wraps

def my_decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result
	return wrapper

@my_decorator
def my_function(first, last):
	...
```