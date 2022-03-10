Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.11 p19

---
# Using `slice` objects to name slices and avoid hardcoding
To avoid unreadable code caused by repeated hardcoding of slices and indexes, a `slice` object can be used and assigned to a variable with a friendly, easy to understand name.

Suppose you are reading in lines from a flat text file and you have to parse numbers from it based on their position. In this scenario, we are reading in information about a stock portfolio which includes share numbers and purchase price.
```python
record = 'AAPL....................100 .......513.25 ..........'
cost = int(record[20:32] * float(record[40:48])
```

Doing this repeatedly can cause a lot of confusion when reading back the code, as it's not obvious at all what the slices are indexing. Instead, you can name a slice by turning it into an object:
```python
SHARES = slice(20, 32)	# same as [20:32]
PRICE = slice(40, 48)	# same as [40:48]

cost = int(record[SHARES]) * float(record[PRICE])
```

Using the above code repeatedly makes it clear what each slice is accessing, and it's also much easier to edit if the format of the source file changes as you don't have to update many instances of hardcoded slices and indexes.

Attributes of the `slice` object can be accessed with `slice.start`, `slice.stop` and `slice.step`.