Note type: #litnote
Source: [[📖 Python Cookbook]] ch4.2 p114

---
# Iterating through a custom object
Sometimes you'll create a custom object that contains an iterable attribute. You can define an `__iter__` method to be able to iterate through this attribute by calling a `for` loop directly on the object itself, which makes for cleaner code than accessing internal attributes each time.
```python

class MyObject:
	def __init__(self):
		self._internal_iterable = [1, 2, 3, 4]
	
	def __iter__(self)
		return iter(self._internal_iterable)
		
test = MyObject()

for num in test:
	print(num)

# 1
# 2
# 3
# 4
```

Each time a `for` loop is called, an iterator object is created by calling `.__iter__()` on the object in question. In the above example, we are simply instructing the `.__iter__()` method to return an iterator of the `_internal_iterable` attribute. So when a `for` loop is called on the overarching object, `iter()` is called on `_internal_iterable` and the resulting iterator object is returned, ready to be looped through.