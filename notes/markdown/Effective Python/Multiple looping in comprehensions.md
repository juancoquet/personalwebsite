Note type: #litnote
Source: [[📖 Effective Python]] item 28

---
# Multiple looping in comprehensions
You can loop multiple times when using list comprehensions to access deeper nested elements. These sub expressions run in the order provided, from left to right.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for x in row for row in matrix]
print(flat)

>>>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Including more than two loops in a comprehension becomes too visually noisy and difficult to follow, and it isn't much shorter than fully fleshed out `for` loops anyway. In this case, it's best to use a full for loop nesting sequence, in which the indentations will make it far easier to read.

---
#### See also:
- [[Comprehensions can affect and filter items in a list more clearly than `map` and `filter`]]