Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.16 p292

---
# Defining more than one constructor in a class
There are some scenarios where you may need multiple ways of instantiating a class. To do this, use the `@classmethod` decorator.
```python
import time


class Date:
	# Primary constructor
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
		
	# Alternate constructor
	@classmethod
	def today(cls):		# Receives the class as the first argument
		now = time.localtime()
		return cls(now.tm_year, now.tm_mon, now.tm_mday)
```

The `today` method receives the class itself as the first argument, and uses it to create and return an instance.
```python
birthday = Date(1995, 12, 01)
now = Date.today()
```

It may be tempting to implement such behaviour using conditional logic inside the main `__init__()` constructor, but that can be difficult to read and implementations may not explicitly show what's going on.
```python


class Date:
	def __init__(self, *args):
		if len(args) == 0:
			now = time.localtime()
			args = (now.tm_year, now.tm_mon, now.tm_mday)
		self.year, self.month, self.day = args


birthday = Date(1995, 12, 01)		# Explicit, clear
now = Date()		# What's going on? Hard to tell.
```

As shown above, the use of the `@classmethod` to define `Date.today()` makes it far more clear what the code is actually doing behind the scenes.