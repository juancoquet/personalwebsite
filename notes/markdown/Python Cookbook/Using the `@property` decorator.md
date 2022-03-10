Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.6 p252

---
# Using the `@property` decorator
The `@property` decorator is used for implementing additional processing (such as type-checking) when accessing an object's attributes—you can run *getter* and *setter* methods when an attribute is accessed with regular dot notation.
```python

class Person:
	def __init__(self, first_name):
		self.first_name = first_name
		
	# Getter function
	@property
	def first_name(self):
		return self._first_name
		
	# Setter function
	@first_name.setter
	def first_name(self, value):
		if not isinstance(calue, str):
			raise TypeError('Expected a string')
		self._first_name = value
	
	# Deleter function (optional)
	@fist_name.deleter
	def first_name(self):
		raise AttributeError("Can't delete attribute")

```

The above code shows how the `@property` decorator should be utilised. Each method must have the same name as the attribute to which they pertain, and should be preceded by the appropriate `@property` tag. The `setter` and `deleter` decorators won't be defined unless `first_name` was already established as a property.

Once the decorator has been implemented, the defined methods will automatically be run with each access to the attribute via dot notation.
```python

me = Person('Juan')

me.first_name	# Calls the getter

me.first_name = 42		# Calls the setter, raises TypeError

del a.first_name	# Call deleter, raises AttributeError

```

Property decorators should only be used when additional processing actually needs to be run. Implementing them without any need for additional processing upon attribute access only causes bloated, untidy code.