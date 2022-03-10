Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.9 p98

---
# Prefer numpy universal native functions over looping
The Numpy module comes with built-in 'universal functions', which are a set of standard mathematical functions commonly applied to arrays. Always prefer using these functions to affect the elements of an array over looping, as they can be hundreds of times faster.

Some of these universal functions are:
- np.sqrt(arr)
- np.cos(arr)

---
### See also:
- [[Lists vs Numpy arrays]]