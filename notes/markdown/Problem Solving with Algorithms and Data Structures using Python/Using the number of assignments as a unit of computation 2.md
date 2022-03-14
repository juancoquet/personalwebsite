Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 3.3
Date: 2021-10-27

---
# Using the number of assignments as a unit of computation
When analysing the runtime of a function, we need to use a basic unit of computation. Deciding what that unit of computation should be will depend on the type of function, but a good one to use is often the number of assignments made. Other candidates might be the number of operations executed, or the number of comparisons made.

Assume we have the following code:
```python

def my_func(n):
	a = n[0]
	b = n[0] * 2
	n_list = []
	for n in range(n):
		for n2 in range(n):
			new_num = n * n2
			n_list.append(new_num)
	for n3 in range(n):
		m = n3 ** 2
		o = m/2
	x = a + b + n_list2[-1]

```

Here we have 3 assignments before the first loop, then **n^2** assignments of `new_num` inside the nested loop, then **2n** assignments of the `m` and `o` variables combined, and finally one assignment of the `x` variable before the function finishes running. We can notate this as **3 + n^2 + 2n + 1**, or **n^2 + 2n + 4**.

This describes the *absolute* runtime of the function. However, as `n` grows larger, the constants and coefficients are dwarfed by the quadratic part of the equation. In every absolute runtime analysis there is a part that accounts for most of the function's growth rate. Because of this, when analysing the runtime of a function we ignore all constants and coefficients, and instead focus on the order of magnitude the function – the part that accounts for most of the function's growth rate. We call this **Big-O**, where O stands for the **order of the function**.

The Big-O runtime of the above function is **O(n^2)**.