Note type: #litnote
Source: [[📖 Effective Python]] item 33

---
# Use `yield from` when looping through a generator to create another generator
Instead of looping through a generator using `for` and manually yielding results, the `yield from` expression is faster and improves readability.
```python
def my_gen(num):
	for i in range(num):
		yield i

def multiple_gen(multiple, num):
	for _ in range(multiple):
		for i in my_gen(num):
			yield i						# noisy, hard to follow
			
---

def multiple_gen(multiple, num):
	for _ in range(multiple):
		yield from my_gen(num)			# much clearer, and runs faster
```

This can be employed when using a sub-generator within an enclosing generator.

---
#### See also:
- [[Generator expressions explained]]
- [[Using generators]]