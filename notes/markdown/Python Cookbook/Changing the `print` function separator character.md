Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.3 p144

---
# Changing the `print` function separator character
By default, the `print` function will separate each call with a new line. To change this behaviour, a `sep` and `end` argument can be defined.
```python

print('AAPL', 50, 613.25, sep=',')
# AAPL,50,613.25

my_list = ['AAPL', 50, 613.25]

for item in my_list:
	print(item, end=' ')
# AAPL 50 613.25
```