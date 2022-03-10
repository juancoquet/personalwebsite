Note type: #litnote
Source: [[📖 Effective Python]] item 30

---
# Using generators
A generator is produced by a function that utilises the `yield` expression. When a generator function is called, it doesn't actually run—instead it returns an iterator. The `next` function can then be used on this new iterator, causing the generator to advance to the next `yield` expression. Each value passed to the `yield` expression is then returned by the generator function to the caller. This means that generators have better memory management than returning a full list, as returning a full list requires the full list to be created before it can be returned. This can use up a system's available memory when working with large list outputs. By contrast, a generator only deals with one value at a time, keeping memory consumption at safe levels.
```python
def fib_generator():
	a = 0
	b = 1
	c = 0
	n = 1
	if n == 1:
		n += 1
		c = b + a
		a = b
		b = c
		yield 0
	elif n == 2:
		n += 1
		c = b + a
		a = b
		b = c
		yield 1
	else:
		n += 1
		c = b + a
		a = b
		b = c
		yield c

fib_iterator = fib_generator()

for _ in range(8):
	print(next(fib_iterator))

>>>
0
1
1
2
3
5
8
13
```

The above generator can be used to retrieve one Fibonacci number at a time each time the `next` function is called on `fib_iterator`. 