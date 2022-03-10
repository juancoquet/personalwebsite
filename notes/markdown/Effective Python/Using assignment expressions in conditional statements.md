Note type: #litnote
Source: [[📖 Effective Python]] item 29

---
# Using assignment expressions in conditional statements
In order to needless repetition, assignment expressions can be used within comprehensions. They can be used in any portion of the comprehension, but it's best to only use them within the conditional portion as using them anywhere else will result in the created variable to leak into the containing scope which can lead to obscure bugs.
```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [square for x in original if (square := x**2) > 16]
print(a)

>>>
[25, 36, 49, 64, 81]
```

The above example uses an assignment expression to create the `square` variable, eliminating the need to run the `**2` operation twice:
```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [x**2 for x in original if x**2 > 16]
print(a)

>>>
[25, 36, 49, 64, 81]
```

This is not the greatest example, but in more complex comprehensions and expressions this can reduce the length of your code and improve readability.

---
#### See also:
- [[Assignment expressions explained]]
- [[Assignment expressions can be combined with comparison and logical operators as part of logical expressions]]
- [[Comprehensions can affect and filter items in a list more clearly than `map` and `filter`]]