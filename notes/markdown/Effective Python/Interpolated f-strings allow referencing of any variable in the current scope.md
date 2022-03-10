Note type: #litnote
Source: [[📖 Effective Python]] item 4

---
# Interpolated f-strings allow referencing of any variable in the current scope
With interpolated f-strings you can reference any variable within the current python scope by using it within the formatting expression:
```python
first = 'Juan'
last = 'Coquet'

formatted = f"My name is {first} {last}."

print(formatted)

>>>
My name is Juan Coquet
```