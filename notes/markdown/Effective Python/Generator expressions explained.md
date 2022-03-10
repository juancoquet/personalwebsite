Note type: #litnote
Source: [[📖 Effective Python]] item 32

---
# Generator expressions explained
Generator expressions are much like comprehensions, except that instead of creating a container they create an iterator. The syntax used is the same but the expression must me wrapped in `()` instead of `[]`.
```python
my_nums = [1, 2, 3, 4, 5, 6]
square_container = [x**2 for x in my_nums]		# comprehension
square_it = (x**2 for x in my_nums)				# generator expression
```

Generator expressions can be used in nested combinations—that is, use an iterator already created by a generator expression inside a subsequent generator expression.
```python
square_pairs = ((i, square) for i, square in enumerate(square_it))
```

The above code utilises the `square_it` iterator that was created in the first example, and combines it with `enumerate` to create another iterator that returns a tuple with the `enumerate` index value and the squared number at that index.

Each time the `square_pairs` iterator is advanced using `next`, the interior `square_it`  iterator is also advanced creating a cascading effect. This is very memory-efficient as it only ever generates and evaluates the values being used for the current call, rather than generating all values and storing them in memory. The only thing to be wary of is the fact that these iterators can become exhausted once fully iterated, so they cannot be reused for further iteration unlike iterable containers.

---
#### See also:
- [[Using generators]]
- [[Iterables are not the same as iterators]]