Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.7 p257

---
# Using `super()` to call parent methods
The `super()` function allows you to call the methods of a parent class (or *superclass*) from inside a child class.
```python

class Base:
	def __init__(self):
		print('Base.__init__')
		
class A(Base):
	def __init__(self):
		super().__init__()	# Calls Base.__init__()
		print('A.__init__')
		
a = A()

# Base.__init__
# A.__init__

```