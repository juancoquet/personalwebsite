Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.14 p23

---
# Sorting objects by a particular attribute
When wanting to sort a sequence of objects by a particular attribute, or when wanting to sort a sequence of objects without native comparison, a `key` argument can be provided to the `sorted` or `sort` functions.
```python

class User:
	def __init__(self, fname, lname, dob):
		self.fname = fname
		self.lname = lname
		self.dob = dob
		


juan = User('Juan', 'Coquet', '1995-12-01')
claudio = User('Claudio', 'Coquet', '1953-09-13')
hristo = User('Hristo', 'Zaykov', '1996-04-07')

users = [juan, claudio, hristo]

by_full_name = sorted(users, key=lambda u: (u.lname, u.fname))
#	[claudio, juan, hristo]
```

In the above block of code, a `lambda` which returns a tuple containing the user's last name and the user's first name to use as the sorting criteria.

---
### See also:
- [[Sorting by multiple criteria]]