Note type: #litnote
Source: [[📖 Effective Python]] item 4

---
# Advanced .format specifier uses
Specifiers (the placeholders between {} symbols) within format strings can be very powerful in some advanced use cases. They can be combined with dictionary and list indexing in the following way:
```python
my_dict = {
	'first_name': 'Juan',
	'surname': 'Coquet',
	}
	
formatted = "My name is {dict['first_name']}. Initals are \
	{dict['fist_name'][0]}{dict['surname'[0]]}.".format(dict=my_dict)

print(formatted)

>>>
My name is Juan. Initials are JC.
```

---
See also:
- [[What is string formatting]]