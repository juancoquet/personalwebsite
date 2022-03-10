Note type: #litnote
Source: [[📖 Python Cookbook]] ch6.1 p175

---
# Reading CSV data
Use the `csv` module. For simple csv data, you can read and write using `csv.reader` and `csv.writer`. We'll be working with the following csv data:
```
 Symbol,Price,Date,Time,Change,Volume "AA",39.48,"6/11/2007","9:36am",-0.18,181800 "AIG",71.38,"6/11/2007","9:36am",-0.15,195500 "AXP",62.58,"6/11/2007","9:36am",-0.46,935000 "BA",98.31,"6/11/2007","9:36am",+0.12,104800 "C",53.08,"6/11/2007","9:36am",-0.25,360900 "CAT",78.29,"6/11/2007","9:36am",-0.23,225400
```
```python

import csv


with open('stocks.csv') as f:
	f_csv = csv.reader(f)	# create reader
	headers = next(f_csv)
	for row in f_csv:
		...	# process row
```

To avoid confusing indexing, such as `row[0]` for symbol or `row[5]` for volume, `csv.DictReader` can be used which allows us to access the data in each row using the header name of each column as a key.
```python

with open('stocks.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		...	# process row
```

Using `DictReader` assumes that there is a header column, which it will automatically consume so `next()` does not have to be called on `f_csv` to extract the headers. The data can now be accessed for each row by using header names as dictionary keys, such as `row['Symbol']` or `row['Volume']`.