Note type: #litnote
Source: [[📖 Effective Python]] item 17

---
# `defaultdict` automatically sets a default value to missing keys
The `defaultdict` type can be imported from the `collections` module in the standard library. Upon defining the `__init__` method, you must provide a valid callable or `None` as the first argument in the method. It will then be called automatically when you try to access a key that doesn't exist, creating an instance of that callable as the default value for the new (ex-missing) key.
```python
from collections import defaultdict

my_dict = defaultdict(list)	# list callable passed as default value

my_dict['name'] = 'juan'	# adding key/value pair
dob = my_dict['dob']	# try to access missing key

print(my_dict['name'])
print(dob)

>>>
juan
[]	# list was called as the default value for key 'dob'
```

---
#### See also:
- [[Using `get` to check for existence of a `key` in a `dict` type]]