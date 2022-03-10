Note type: #litnote
Source: [[📖 Effective Python]] item 14

---
# Sorting by multiple criteria
We can take advantage of the fact that [[Tuples are sorted left to right]] if we want to sort by multiple criteria. All we have to do is create tuples from our objects that contain the criteria by which we want to sort, in the order we want to use them for sorting. This can be done with a `lambda` function passed to the `sort` method's `key` parameter.
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
	Person('ana', 1991),
	Person('david', 2007),
	]
	
sorted = people.sort(key=lambda x: (x.birth_year, x.name)

print(people)

>>>
['ana 1991', 'pupi 1991', 'juan 1995', 'david 2007']
```

---
#### See also:
- [[Lists can be sorted by a specific attribute]]
- [[Tuples are sorted left to right]]