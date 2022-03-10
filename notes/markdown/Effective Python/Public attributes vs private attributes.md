Note type: #litnote
Source: [[📖 Effective Python]] item 42

---
# Public attributes vs private attributes
Public attributes are class attributes that can be accessed by anyone by using the dot operator on an object. Private attributes are created by naming an attribute with two leading underscores and can only be accessed by inherent class methods that return the attribute. Attempts to access the attribute from the outside using the dot operator will raise an error.
```python
class MyObject:
	def __init__(self):
		self.public_attr = 'public'
		self.__private_attr = 'private'
		
	def get_private_attr(self):
		return self.__private_attr

foo = MyObject()

private_attr = foo.get_private_attr()

print(foo.public_attr)

>>>
public
private
```
```python
print(foo.__private_attr)

>>>
Traceback ...
AtrributeError: 'MyObject' object has no attribute '__private_attr'
```

---
#### See also:
- [[Pythonic naming conventions]]