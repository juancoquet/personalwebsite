Note type: #litnote
Source: [[📖 Effective Python]] Item 87

---
# Inheriting from `Exception`
An error/exception class can be created by inheriting from the built-in `Exception` class. This new class can then be used in your own code to create custom exceptions to deliberately raise. This helps callers fix bugs, as there is a clear distinction between deliberately raised exceptions and the rest.
```python
class Error(Exception):
	"""Custom error class."""
```