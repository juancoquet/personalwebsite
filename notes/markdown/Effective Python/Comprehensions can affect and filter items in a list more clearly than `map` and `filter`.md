Note type: #litnote
Source: [[📖 Effective Python]] item 27

---
# Comprehensions can affect and filter items in a list more clearly than `map` and `filter`
Using comprehensions to create a derivative data structure allows you to affect and filter the original data with far more clarity than by using `map` and `filter` for the same effect.
```python
original_data = [1, 2, 3, 4, 5, 6]

# list comprehension
even_squares = [num**2 for num in original_data if num % 2 == 0]

# dict comprehension
even_squares = {num: num**2 for num in original_data if num % 2 == 0}

# set comprehension
even_squares = {num**2 for num in original_data if num % 2 == 0}
```

In each of the above examples, the `original_data` list object is filtered to only process even numbers, then each of these even numbers are squared and added to the `even_squares` data set. Each time it is implemented using a different data structure, as comprehensions work for lists as well as dictionaries and sets.