Note type: #litnote
Source: [[📖 Effective Python]] item 12

---
# Striding syntax explained
The term striding refers to the size of the jump taken when going through a list. This allows you to make a copy of a list that only contains every nth term. The syntax is `my_list[start:end:stridesize]`.
```python
my_list = [1, 2, 3, 4, 5, 6]
stride_list = my_list[::2]	# copy every 2nd term

print(stride_list)

>>>
[1, 3, 5]
```

Here the stride value of 2 means every second item in the original list is copied, starting from the first item and finishing with the last as indicated by the `[:]` `[start:end]` syntax.

---
#### See also:
- [[Slicing a copy of a list]]