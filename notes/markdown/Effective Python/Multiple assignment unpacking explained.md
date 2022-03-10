Note type: #litnote
Source: [[📖 Effective Python]] item 6

---
# Multiple assignment unpacking explained
In python you can unpack the items of an iterable into variables in a single line, reducing visual noise which helps readability.
```python
name_iter = ('Juan', 'Coquet')
first, last = name_iter

print(first)
print(last)

>>>
Juan
Coquet
```

In the example above, we first define an iterable containing two items. In the following line, we unpack these items into two separate variables using the `=` assignment operator.