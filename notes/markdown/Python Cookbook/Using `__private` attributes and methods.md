Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.5 p250

---
# Using `__private` attributes and methods
The use of double-underscore, or *dunder*, names signifies a private attribute or method. Names that are stated with two leading underscores belong only to the class in which they are declared—they are not inherited by sub-classes. The reason is that python renames these attributes behind the scenes. Take the following example:
```python

class B:
	def __init__(self):
		self.__private = 0
		
	def __private_method(self):
		...
		
	def public_method(self):
		...

```

Here, python will rename `__private` as `_B__private` and `__private_method` as `_B__private_method`. The reason for this is so that these attributes cannot be overridden via inheritance—they belong only to the class in which they are declared. Consider the following:
```python

class C(B):
	def __init__(self):
		super().__init__()
		self.__private = 1	# Does not override `B.__private`
		
	def __private_method(self):
		'''
		Does not override `B.__private_method()`
		'''
		...
		
```

In this case, the private names are renamed to `_C__private` and `_C__private_method` behind the scenes, differentiating them from the names of the methods in the `B` base class.

---
### See also:
- [[Using `_internal` attributes and methods]]
- [[Pythonic naming conventions]]