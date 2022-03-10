Note type: #litnote
Source: [[📖 Effective Python]] item 10

---
# Assignment expressions can be combined with comparison and logical operators as part of logical expressions
The walrus operator can be used within a broader logical expression to make more complex evaluations.
```python
budget = 50
price = 75
discount = 35

if (reduced_price := price - discount) <= budget:
	print("I can afford it!")
else:
	print("It's out of my budget")
```

Above, `reduced_price` is assigned the value of `price - discount`, and then compared to `budget`. When the walrus operator is used in this manner, the assignment expression should be wrapped in parentheses as it is a sub-expression of a larger expression.

---
#### See also:
- [[Assignment expressions explained]]