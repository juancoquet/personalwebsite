Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.12 p104

---
# Converting `timedelta` objects to total seconds
Accessing a `timedelta` object's `.seconds` attribute will return the remaining number of seconds after ignoring higher order time units, like days. To convert the entire `timedleta` duration into seconds, use `timedelta.total_seconds()`.
```python

from datetime import timedelta

delta = timedelta(days=2, hours=10.5)

delta.seconds			# 37800 (10.5 hours in seconds)
delta.total_seconds()	# 124200 (2 days and 10.5 hours in seconds)
```
