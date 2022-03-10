Note type: #litnote
Source: [[📖 Effective Python]] item 14

---
# Lists can be sorted by a specific attribute
Custom-made objects cannot normally be sorted as there is no obvious sorting criteria. However, a specific attribute can be designated as the sorting criteria through the use of the `sort` function's `key` parameter.

The `key` parameter expects a function. This function can be passed a single argument, which should be an item from the list that is being sorted. The return value of the function should be a comparable value for sorting purposes.
```python
class Person:
	def __init__(self, name, birth_year):
		self.name = name
		self.birth_year = birth_year
		
	def __repr__(self):
		return f'{self.name} {self.birth_year}'
		
people = [
	Person('juan', 1995),
	Person('pupi', 1991),
	Person('ana', 1993),
	Person('david', 2007),
	]
	
sorted = people.sort(key=lambda x: x.birth_year)

print(people)

>>>
['pupi 1991', 'ana 1991', 'juan 1995', 'david 2007']
```