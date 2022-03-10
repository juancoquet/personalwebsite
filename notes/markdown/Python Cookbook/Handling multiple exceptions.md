Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.5 p574

---
# Handling multiple exceptions
- except can be handed a tuple of exceptions
- exceptions that require specific behaviour go in their own except clause
- exceptions that share a common base class can be caught by catching the base class
- view an exception's class hierarchy by calling exception.__mro__

Multiple exceptions can be caught by one except clause by providing each exception as part of a tuple:
```python
try:
	# Code that fails
	...
except (ZeroDivisionError, NotANumberError):		# Catches two errors
	...
```

Any exceptions that require specific behaviour can go into their own `except` clause:
```python
try:
	# Code that fails
	...
except (ZeroDivisionError, NotANumberError):
	...
except PassedAsStringError:
	...
```

Another way of handling multiple errors is by catching a common base class if the exceptions in question have a common inheritance hierarchy. For example, `FileNotFoundError` and `PermissionError` both inherit from `OSError`, so rather than passing both of these exceptions as a tuple, you can simply pass `OSError` to catch them both.
```pyhton
try:
	...
except OSError:				# Catches FileNotFoundError and PermissionError
	...
```

To view an exception's inheritance hierarchy, you can print a call to the exception's `__mro__` property:
```python
print(ZeroDivisionError.__mro__)

# Prints:
'''
(<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
'''
```

This means that `ZeroDivisionError` inherits from `ArithmeticError`, which inherits from `Exception`, etc...