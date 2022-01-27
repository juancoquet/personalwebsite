Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch5 p73

---
# Creating a new database entry without calling `save()`
Normally, to create a new object from a model you'd instantiate it like a regular class and then call the `save()` method on the created object:
```python
from myapp.models import SomeModel

def home_view(request):
	new_entry = SomeModel(data=123)
	new_entry.save()
```

This can also be achieved with `.objects.create()`.
```python
def home_view(request):
	SomeModel.objects.create(data=123)
```