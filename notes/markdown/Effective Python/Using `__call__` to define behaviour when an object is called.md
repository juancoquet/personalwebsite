Note type: #litnote
Source: [[📖 Effective Python]] item 38

---
# Using `__call__` to define behaviour when an object is called
The built-in method `__call__` can be defined within a class to make instances of that class callable, executing specified behaviour each time a call to the object is made.
```python
Class MyObject:
	def __init__(self):
		self.times_called = 0
	
	def __call__(self):
		self.times_called += 1
		print("Called object!")
```

The above class can be used to create objects which can be called within function hooks, for example. Each time this object is called it will print "Called object!" and increment the `self.times_called` counter by 1 to keep track of the number of times this object has been called.