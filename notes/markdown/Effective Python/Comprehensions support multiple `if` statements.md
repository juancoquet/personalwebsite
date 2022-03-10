Note type: #litnote
Source: [[📖 Effective Python]] item 28

---
# Comprehensions support multiple `if` statements
You can use multiple `if` conditions within comprehensions for filtering results. When doing so, these if statements have an implicit `and` expression between them.
```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [x for x in original if x > 4 if x % 2 == 0]		# equivalent
c = [x for x in original if x > 4 and if x % 2 == 0]	# equivalent
```

In the example above, the original list is filtered out with comprehensions into `b` and `c` to include only elements that are greater than 4 and even numbers. It makes no difference whether or not the explicit `and` is included in the expression.

---
#### See also:
- [[Multiple looping in comprehensions]]
- [[Comprehensions can affect and filter items in a list more clearly than `map` and `filter`]]