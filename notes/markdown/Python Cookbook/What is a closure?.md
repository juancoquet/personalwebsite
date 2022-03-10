Note type: #litnote
Source: [[📖 Python Cookbook]] ch7.9 p231

---
# What is a closure?
A closure is a function that lives (is defined) inside of another function. The reason closures are used is because they remember the environment in which they are defined—that is, a closure remembers any values that exist within the function within which it is defined.
```python

def func(my_arg):
	def closure(other_arg):
		return my_arg + other_arg
	return closure		# returns callable `closure` function
```

In the above example, the `closure` function is defined inside the `func` function. This means that each time `func` is called, `closure` is defined and it will remember any arguments which the enclosing `func` was passed for `my_arg`. `func` then returns the callable `closure`, which expects `other_arg`. This returned callable can be assigned to any variable name and then used as its own function, with the key feature that this variable contains within it (contained within the `closure` function) whatever value was originally passed to `func`.
```python

testing = func(5)
# testing now holds the `closure` function, inside which is `my_arg=5`

result = testing(2)		# result is `my_arg=5` + `other_arg=2`, so 7

other_result = testing(10)	# 15

using_str = func('Hello')

restult_str = using_str('World!')	# 'HelloWorld!'
```

Because of this 'remembering' behaviour, closures can be used instead of simple single-method classes for cleaner code. You may want to use a single-method class when you need a simple function that remembers one or more values—for such cases, using a closure may be a more elegant option.