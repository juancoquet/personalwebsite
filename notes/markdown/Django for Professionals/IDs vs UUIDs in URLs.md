Note Type: #litnote
Source: [[📖 Django for Professionals]] ch10 p158

---
# IDs vs UUIDs in URLs
Using an object's `pk` field is a quick and dirty way of creating a unique URL that points to that object, but it's not ideal in production for security reasons. It can tell a hacker how many items exist in the database and reveal other exploits.

It is better to use use a UUID — a Universally Unique Identifier — which is supported by Django with the `UUIDField`.
```python
# models.py

import uuid
from django.db import models
from django.urls import reverse


class MyModel(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	
	def get_absolute_url(self):
		return reverse('detail_view', kwargs={"pk": self.pk})
		
```

Above we override the built in `id` field, and assign it to be a `UUIDField`. We then make this field the Primary Key for this model, generate a default `uuid4` value (a random 128-bit label), and make the field immutable.

The `reverse` function is passed the name of the view that is responsible for displaying a detailed view of the model object as an argument, as well as a `pk` argument which looks up the object's `pk` field, our new `id`.

We can now safely use the `pk` field for our URLs without giving sensitive information away to unfriendly visitors to the site.
```python
# urls.py

from django.urls import path
from .views import MyView

urlpatterns = [
	path('<uuid:pk>', MyView.as_view(), name='my_view'),
]
```