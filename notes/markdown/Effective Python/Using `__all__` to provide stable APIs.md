Note type: #litnote
Source: [[📖 Effective Python]] item 85

---
# Using `__all__` to provide stable APIs
When writing an API for broad consumption, such as an open source python package, it is important to ensure that it is stable across releases and that functionality remains the same. To ensure that happens, internal code should be hidden from external users—only code that can be called by them should be accessible to them. By following this approach, the package can be improved and refactored without affecting the code of anyone already using the API.

This can be achieved by using the `__all__` special attribute. Any name inside the `list` `__all__` is exported from the module as part of a public API. When consuming code executes `from mypackage import *`, only names within the `__all__` attribute of the `mypackage` module will be imported, rendering all internal code uncallable. If `__all__` has not been declared in `mypackage`, then only public attributes (those without leading underscores, see [[Pythonic naming conventions]]) will be imported.
```python
__all__ = ['MyClass', 'my_function']

class MyClass:
	def __init__(self):
		...

class _NotIncluded:
	def __init__(self):
		...

def my_function():
	...
```

---
#### See also:
- [[Importing python packages]]