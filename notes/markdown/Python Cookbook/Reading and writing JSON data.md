Note type: #litnote
Source: [[📖 Python Cookbook]] ch6.2 p179

---
# Reading and writing JSON data
The `json` module is used for working with JSON data. It's operation mirrors that of `pickle`.
```python

import json

data = {
	'name': 'ACME'
	'shares': 100,
	'price': 542.23
}

with open('stocks.json', 'w') as f:
	json.dump(data, f)
	
with open('stocks.json', 'r') as f:
	data = json.load(f)
```