Note type: #litnote
Source: [[📖 Effective Python]] item 4

---
# F-strings allow a full expression to be placed within specifier braces
As well as referencing any variable within the current scope, you can also combine these variables with expressions within f-string specifier braces {}.
```python
first_last = ['Juan', 'Coquet']

formatted = "My name is {' '.join(first_last)}."

print(formatted)

>>>
My name is Juan Coquet.
```

---
See also:
- [[Advanced .format specifier uses]]
- [[Interpolated f-strings allow referencing of any variable in the current scope]]