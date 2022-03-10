Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.20 p305

---
# Calling methods with string names
If you have the name of a method stored as a string, this can be used to call the method itself with `getattr()`. First you lookup the method, then you pass arguments to it.
```python
class Nums:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def add(self, extra_num=0):
		return self.x + self.y + extra_num


a = Nums(2, 3)

result = getattr(a, 'add')(4)	# Calls `add` on `a`, with the argument `4` = 9
```

The `getattr()` function takes an object (`a`), an attribute to look for as a string (`'add'`) and returns the attribute found. Since the attribute found is a callable method, we can supply it with an argument inside brackets straight after (`(4)`).