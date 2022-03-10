Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.8 p13

---
# Calculating and sorting with dictionary data
Numeric dictionary data can be manipulated quite handily with the by inverting key-value pairs using the `zip()` function.
```python
prices = {
	'ACME': 45.23
	'AAPL': 612.78
	'IBM': 205.55
	'HPQ': 37.50
	'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))	# (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))	# (612.78, 'AAPL')
```

Other comparative functions can also be used, such as `sorted()`.