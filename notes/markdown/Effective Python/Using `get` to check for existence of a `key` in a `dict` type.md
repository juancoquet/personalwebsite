Note type: #litnote
Source: [[📖 Effective Python]] item 16

---
# Using `get` to check for existence of a `key` in a `dict` type
The `get` method implicitly searches for the existence of a key within the `dict` it is called on. If the key can be found, it returns the associated value; if the key can't be found, it returns `None`.
```python
my_dict = {'name': 'juan', 'dob': '01/12/1995'}

name = my_dict.get('name')
gender = my_dict.get('gender')

print(name, gender)

>>>
juan None
```

An optional default return value can also be passed to `get`—note that this simply returns the given value; it *does not* create a new `key` in the `dict`.
```python
truncated ...

name = my_dict.get('name')
gender = my_dict.get('gender', 'not specified')

print(name, gender)
print(my_dict.keys())

>>>
juan not specified
dict_keys(['name', 'dob'])	# no new key created
```

Using `get` combined with `:=` assignment expressions instead of testing if a key is `in` a `dict` and then using `if`/`else` control flow statements can make for cleaner, terser code.

```python
truncated ...

if not (gender := my_dict.get('gender')):
	gender = 'male'
	my_dict['gender'] = gender
```

---
#### See also:
- [[Assignment expressions explained]]