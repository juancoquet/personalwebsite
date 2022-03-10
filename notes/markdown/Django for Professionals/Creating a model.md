Note Type: #litnote
Source: [[📖 Django for Professionals]] ch10 p143

---
# Creating a model
To create a new model, inherit from the built in `Model` class and then define any attributes with a field type. For example, here is a book model:
```python
# models.py

from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	price - models.DecimalField(max_digits=6, decimal_places=2)
	
	def __str__(self):
		return self.title
		
```

A model represents a table in a database. The above model represents a `Book` table, with the columns `title`, `author` and `price`, as well as some implicit columns such as `id`.

The `__str__` method decides what will be shown on the console when `print` is used on an instance of the model, as well as what shows in the Django admin.