Note type: #litnote
Source: [[📖 Effective Python]] item 65

---
# `finally` Blocks
`finally` blocks will always run after `try` blocks, whether an exception was raised in the process or not. In the absence of an `except` block to handle exceptions, any code within the `finally` block will run before the exception is propagated up to the calling code.
```python
try:
	division = 10 / 5
	print(division)
finally:
	print("this runs")
	
>>>
2
this runs
```

```python
try:
	causes_error = 10 / 0
	print(causes_error)
finally:
	print("this still runs")
	
>>>
this still runs
Traceback ...
```