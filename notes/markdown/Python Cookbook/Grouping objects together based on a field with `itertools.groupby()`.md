Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.15 p25

---
# Grouping objects together based on a field with `itertools.groupby()`
If you have a sequence of objects that you would like to be grouped by a particular field or attribute, the `gorupby()` function from `itertools` is a great fit. There is a preliminary step before handing the objects over to `groupby()`—they must be sorted by the desired field or attribute, as `groupby()` works by iterating through the sequence and grouping together sequential runs that contain identical data in a desired field.
```python
from itertools import groupby


meals_list = [
	{'bfast': 'cereal', 'date': '2021-04-16'},
	{'lunch': 'sandwich', 'date': '2021-04-16'},
	{'dinner': 'soup', 'date': '2021-04-16'},
	{'bfast': 'bacon & eggs', 'date': '2021-04-15'},
	{'lunch': 'sandwich', 'date': '2021-04-15'},
	{'dinner': 'chicken & potatoes', 'date': '2021-04-15'},
]
# already sorted by date, no need to sort in this case.

for date, meals in groupby(meals_list, key=lambda x: x['date']):
	print(date)
	for meal in meals:
		print('    ', meal)

2021-04-16
	{'date': '2021-04-16', 'bfast': 'cereal'}
	{'date': '2021-04-16', 'luncht': 'sandwich'}
	{'date': '2021-04-16', 'dinner': 'soup'}
2021-04-15
	{'date': '2021-04-15', 'bfast': 'bacon & eggs'}
	{'date': '2021-04-15', 'bfast': 'sandwich'}
	{'date': '2021-04-15', 'bfast': 'chicken & potatoes'}
```

On each iteration, the `groupby()` function returns the value it grouped by along with an iterator containing all the contents that matched the grouping criteria.