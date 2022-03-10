Note type: #litnote
Source: [[📖 Effective Python]] item 90

---
# How to use `typing`
You can add a `type` to any name in python with the syntax `name: type` for variables and `-> type` for return values.
```python
def my_func(value: int, value2: int) -> int:
	return value + value2

def concat(a: str, b: str) -> str:
	return a + b
```

Typing can be used to avoid common bugs before runtime, particularly with callers of your API.