Note type: #litnote
Source: [[📖 Effective Python]] item 65

---
# `else` blocks after `try/except`
When used as part of a `try/except` clause, the `else` block will run if no exceptions were raised during the `try` block. In short, if the `try` fails then the `except` block runs, otherwise the `else` block will run.
```python
try:
	division = 10 / 2		# no errors raised
except:							# doesn't run
	print("error detected")
else:							   # runs
	print('success!')
	
>>>
success!
```