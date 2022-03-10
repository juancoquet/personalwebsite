Note type: #litnote
Source: [[📖 Effective Python]] item 23

---
# Dictionaries can be used for providing keyword arguments in function calls
If you have a dictionary whose keys correspond to the arguments that a function expects, you can use this dictionary to provide the function with values by using the `**my_dict` syntax within the function call to pass in the dictionary's values.
```python
my_dict = {
	'first': 'juan',
	'last': 'coquet',
	}
	
def my_function(first, last):
	print(f'{first} {last}')

my_function(**my_dict)

>>>
juan coquet
```

This is equivalent to explicitly specifying each argument within the function call:
def my_function(first, last):
	print(f'{first} {last}')
```python
my_function(first='juan', last='coquet')

>>>
juan coquet
```