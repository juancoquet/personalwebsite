Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.8 p578

---
# Creating custom exceptions
Custom exceptions can be easily created by defining a class that inherits from `Exception`, or any other standard exception as follows:
```python
class MyCustomError(Exception):
	pass
```

This custom exception can now be raised in the usual way. The reason to define custom exceptions is that it can provide a more detailed account of what is going wrong in your program to help users debug. For example, you could define `PassedAsStringError` to inherit from the standard `ValueError` which tells the detail more clearly what has gone wrong.

You can also create inheritance hierarchies to help users handle custom errors with more malleability:
```python
class MyCustomBaseError(Exception):
	pass

class MyError1(MyCustomBaseError):
	pass

class MyError2(MyCustomBaseError):
	pass
```

In the above example, `MyError1` and `MyError2` can both be caught with an except clause that catches `MyCustomBaseError`. Use this to intuitively group together related custom exceptions.