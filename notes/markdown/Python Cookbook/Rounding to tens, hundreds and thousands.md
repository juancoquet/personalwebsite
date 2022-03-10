Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.1 p83

---
# Rounding to tens, hundreds and thousands
The built in `round()` function can be supplied with two arguments—the number being rounded and the number of digits to round to. If supplied with a negative number for the second argument, the function will round the the respective number of spaces to the *left* of the decimal point, allowing you to round to tens, hundreds, thousands, and so on.
```python

num = 123789
round(num, -1)	# 123790
round(num, -2)	# 123800
round(num, -3)	# 124000
```