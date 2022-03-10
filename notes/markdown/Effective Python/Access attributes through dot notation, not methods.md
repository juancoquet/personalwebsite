Note type: #litnote
Source: [[📖 Effective Python]] item 44

---
# Access attributes through dot notation, not methods
It is much more straight forward to access class attributes using the dot operator than by defining attribute set and get methods. It makes your code terser and clearer.
```python
class MyClass:
	def __init__(self):
		self.attr_1 = 1
		self.attr_2 = 2
		self.attr_3 = 3
	
#	def get_attr_1(self):		# Don't do this
#		...

my_object = MyClass()

print(my_object.attr_1)

my_object.attr_2 = 'two'
print(my_object.attr_2)

>>>
1
two
```