Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.13 p589

---
# Timing a function with a decorator
If you want to time a function every time it is called, you can create a timing decorator.
```python
import time
from functools import wraps

def timethis(func)
	@wraps
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		print(f'{func.__module__}, {func.__name__}, end - start)
		return result


@timethis
def add(a, b):		# Calling module, function name and runtime will print with every call
	return a + b
```