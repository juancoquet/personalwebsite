Note type: #litnote
Source: [[📖 Effective Python]] item 6

---
# Use multiple assignment unpacking to unpack iterables in loops
Indexing into the items within an iterable over a loop is very visually noisy.
```python
fam_info = [
	('Juan', 'Coquet', '01/12/1995'),
	('Mariela', 'Diaz', '26/10/1967'),
	]

for person in fam_info:
	first = person[0]
	last = person[1]
	dob = person[2]
	
	print(first, last, dob)

>>>
Juan Coquet 01/12/1995
Mariela Diaz 26/10/1967
```

Instead, items can be unpacked within the initial `for` expression:

```python
truncated...

for first, last, dob in fam_info:
	print(first, last, dob)
	
>>>
Juan Coquet 01/12/1995
Mariela Diaz 26/10/1967
```

This is the pythonic way of writing such code—it's terse, yet it improves readability.

---
See also:
- [[Multiple assignment unpacking explained]]