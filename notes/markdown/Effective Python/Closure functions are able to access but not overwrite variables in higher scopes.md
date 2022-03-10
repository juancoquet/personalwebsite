Note type: #litnote
Source: [[📖 Effective Python]] item 21

---
# Closure functions are able to access but not overwrite variables in higher scopes
A closure function is a function inside another functions. These closure functions are able to access and read higher-order variables, such as arguments passed into the enclosing function, but they can not be redefined by default. This causes the creation of a new variable within the local function scope that is not ported out to the higher-order scope of the enclosing function. To override this, you can 'import' the higher order variable into the closure function by using the `nonlocal` statement.
```python
def my_function():
	flag = True
	def change_flag:
		flag = False	# new flag variable in current scope
	return flag

print(my_function())

>>>
False	# original flag variable unchanged
```

Using `nonlocal`:
```python
def my_function():
	flag = True
	def change_flag:
		nonlocal flag	# 'importing' flag variable into scope
		flag = False	# original flag variable being used
	return flag

print(my_function())

>>>
True	# original flag variable updated
```

Be very careful when using this functionality as it can make the code difficult to follow.