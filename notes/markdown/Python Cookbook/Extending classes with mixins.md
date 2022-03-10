Note type: #litnote
Source: [[📖 Python Cookbook]] ch8.18 p294

---
# Extending classes with mixins
[[What is a mixin?|Mixins]] can be used to add specific behaviour to many different classes. This is helpful when you have a fairly generic type of behaviour that you want to implement in several classes, but these classes don't necessarily have anything in common to allow them to share a base class. In such cases, a separate mixin class can be built and inherited from. Consider the following example, where a mixin class is created for only allowing a `key` to be set once.
```python
class SetOnceMixin:
	def __setitem__(self, key, value):
		if key in self:
			raise KeyError(str(key) + ' already set')
		return super().__setitem__(key, value)
```

This class is completely useless on its own—the lack of `__init__()` and the use of `super()` will raise errors if instantiated. However, when this mixin class is inherited from, the resulting class will not allow a `key` to be set more than once.
```python
class SetOnceDict(SetOnceMixin, dict):
	pass


d = SetOnceDict()
d['x'] = 1		# Creates a `x` key, sets value to 1
d['y'] = 2		# Creates a `y` key, sets value to 2
d['x'] = 3		# Raises KeyError, `x` is already set
```

An important thing to note is the use of `super()` within the mixin class. It seems like a strange implementation, since the mixin doesn't inherit from another class, yet without it the mixin wouldn't work. The `super()` call is responsible for delegating the `__setitem__()` call over to the `dict` class. If there was no multiple inheritance present, this would also cause the code to break. Mixins rely on the presence of other classes—they rely on multiple inheritance. They piggyback onto another class (in this case `dict`) and add functionality to it.

---
### See also:
- [[Using `super()` to call parent methods]]