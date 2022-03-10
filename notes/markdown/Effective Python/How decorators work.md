---
aliases: [decorators, decorator]
---
Note type: #litnote
Source: [[📖 Effective Python]] item 26

---
# How decorators work
A decorator has the ability to run additional code before and after each call to a function that it wraps. This means that decorators can access and modify input arguments, return values and raised exceptions. Decorators are useful for enforcing semantics, debugging and more.

A decorator is essentially a function that takes another function as an argument and then runs this function inside a tertiary wrapper function inside the initial decorator.
```python
def my_decorator(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result
	return wrapper
```

Decorators are applied most commonly by using the @ symbol. When a decorator is placed with the @ symbol above a function definition, it is the same as passing the function below into the decorator as an argument.
```python
@my_decorator
def my_function(first, last):
	print(f'{first} {last}')
```

The only problem with this is that it doesn't carry all metadata from the innermost function to the outermost function.

---
#### See also:
- [[Using `star-args` to accept a variable number of positional arguments]]
- [[Using `doublestar-kwargs` as a catch-all parameter]]