Note type: #litnote
Source: [[📖 Effective Python]] item 18

---
# `__missing__` method explained
The `dict` type has a built-in `__missing__` method that is called when a key that doesn't exist is accessed. By default, this raises an error. With this knowledge, we can create a sub-class that inherits from the `dict` class and overwrite the `__missing__` method to handle missing keys using custom logic according to our needs.
```python
class MyCustomDict(dict):
	def __missing__(self, key):
		self[key] = "I created this custom default value!"

my_dict = MyCustomDict()

test = my_dict['test key']

print(test)

>>>
I created this custom default value!
```

The real power of overwriting the `__missing__` method is that it can be as complex as we need it to be—we can overwrite it to execute other function calls if we so wished.

---
#### See also:
- [[Using `get` to check for existence of a `key` in a `dict` type]]