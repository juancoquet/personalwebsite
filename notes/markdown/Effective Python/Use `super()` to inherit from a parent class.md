Note type: #litnote
Source: [[📖 Effective Python]] item 40

---
# Use `super()` to inherit from a parent class
When creating a new class that should inherit some functionality from a parent class, the way to do this is by using `super()`. This can be done within any class method, not just the `__init__` method.
```python
class Parent:
	def __init__(self):
		print("class created")
		
class Child(Parent):
	def __init__(self):
		super().__init__()
```