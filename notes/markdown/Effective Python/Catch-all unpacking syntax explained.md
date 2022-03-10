Note type: #litnote
Source: [[📖 Effective Python]] item 13

---
# Catch-all unpacking syntax explained
Catch-all unpacking is a more advanced application of multiple assignment unpacking. A shortcoming of multiple assignment unpacking is that the left and right side of the `=` assignment operator must contain the same amount of items, as each item on the right goes into one variable on the left. This applies whether the items on the right are discreet values or the contents of a list.
```python
my_list = [1, 2, 3, 4, 5, 6]
one, two = my_list	# Raises ValueError

>>>
Traceback ...
ValueError: too many values to unpack (expected 2)
```

By using a starred variable with the syntax `*varaible_name`, all excess values can be unpacked into this container—this is catch-all unpacking. Starred expressions are always turned into a `list` object.
```python
my_list = [1, 2, 3, 4, 5, 6]
one, two, *others = my_list

print(one)
print(two)
print(others)

>>>
1
2
[3, 4, 5, 6]
```

A starred variable can appear in any position, not just at the end:
```python
my_list = [1, 2, 3, 4, 5, 6]
first, *others, last = my_list

print(first)
print(others)
print(last)
>>>
1
[2, 3, 4, 5]
6
```
```python
my_list = [1, 2, 3, 4, 5, 6]
*others, second_last, last = my_list

print(others)
print(second_last)
print(last)
>>>
[1, 2, 3, 4]
5
6
```

The only caveats are that starred expressions must be used in combination with at least one other discreet expressions when unpacking, and multiple catch-all expressions cant be used together.

---
#### See also:
- [[Multiple assignment unpacking explained]]