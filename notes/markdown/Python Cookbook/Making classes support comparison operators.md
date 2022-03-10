Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.24 p321

---
# Making classes support comparison operators
Classes can be made to support comparison operators (>, >=, <, <=, != etc). To do this, the methods `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__` must be defined. Thankfully, the `total_orddering` decorator from `functools` automates the creation of most of these methods if you only define `__eq__` and one other.
```python
from functools import total_ordering


@total_ordering
class Square:
	__init__(self, side_length):
		self.side_length = side_length
		self.perimeter = side_length * 4
		self.area = self.side_length ** 2
		
	def __eq__(self, other):
		return self.area == other.area		# Comare areas
	
	def __lt__(self, other):
		return self.area < other.area
		
small_sq = Square(4)
big_sq = Square(5)

print(big_sq > small_sq)		# True
```

It is not difficult to define each comparison method individually, but using this decorator is quicker and easier.