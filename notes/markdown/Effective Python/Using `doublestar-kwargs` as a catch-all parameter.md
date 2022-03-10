Note type: #litnote
Source: [[📖 Effective Python]] item 23

---
# Using `doublestar-kwargs` as a catch-all parameter
You can define a function that takes the parameter `**kwargs` to create a function that accepts any number of arguments providing they are specified. This function takes these arguments and puts them into a dictionary which can then be processed within the function by referencing the `kwargs` variable.
```python
def my_function(**kwargs):
	for key, value in kwargs.items():
		print(f'{key} = {value})

my_function(first='juan', last='coquet', dob='01/12/1995')

>>>
first = juan
last = coquet
dob = 01/12/1995
```

---
#### See also:
- [[Dictionaries can be used for providing keyword arguments in function calls]]