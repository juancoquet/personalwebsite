Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.19 p33

---
# Using generator expressions as arguments for reduction functions
Reduction functions (e.g. `min()`, `max()`, `sum()`) can be passed a generator expression as an argument, thereby eliminating the need to create a temporary sequence for processing.
```python

nums = [1, 2, 3, 4, 5]

smallest_square = min(n**2 for n in nums)	# 1
evens_sum = sum(n for n in nums if n % 2 == 0)	# 6
```

Notice that the generator expression does not need to be wrapped in its own set of brackets to be passed into the reduction function.

The generator expression can be passed in as a list, but in cases where `nums` is a large data set this is not as memory-efficient as passing it as a generator.
```python

squares_sum = sum([n**2 for n in nums])
# Full list is created and stored in memory. Can be a problem as nums grows

squares_sum = sum(n**2 for n in nums)
# Only one data point handled at a time.
```

Note that reduction functions can also accept a `key` argument, which may be a better object if you want to return the object that contains the data point being considered.
```python

stocks = [
	{'name': 'AAPL', 'price': 615.23},
	{'name': 'TSLA', 'price': 420.69},
]

min_price = min(stocks, key=lambda stock: stock['price'])
# {'name': 'TSLA', 'price': 420.69}
```