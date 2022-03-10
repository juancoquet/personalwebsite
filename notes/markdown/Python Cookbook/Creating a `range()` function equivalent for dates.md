Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.14 p109

---
# Creating a `range()` function equivalent for dates
```python

def date_range(start: datettime, stop: datetime, step: timedelta):
	while start < stop:
		yield start
		start += step
```
