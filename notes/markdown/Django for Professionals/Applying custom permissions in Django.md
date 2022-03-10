Note Type: #litnote
Source: [[📖 Django for Professionals]] ch13 p189

---
# Applying custom permissions in Django
We can give different users custom permissions when interacting with different models by defining them inside a `Meta` class within the desired model. The `Meta` class is typically defined after the model fields but before any methods.
```python
# models.py

from django.db import models


class MyModel(models.Model):
	...
	
	class Meta:
		permissions = [
			('special_status', 'Can view all items'),
		]
	
	...
	
```

In the above example, we define a permission name of `special_status`, wit ha description that will be visible in the Django admin that says `Can view all items`.

After doing this, you need to run `makemigrations` and `migrate` since the model has been updated.

Next we go to the Django admin Users section, and select the user to whom we wish to apply our new permission. With the user window open, scroll down until you see `User permissions`, and there will be a table with the syntax:

`{app} | {model} | {permission description}`

Simply select our new permission, found by the description `Can view all items`, assign it to our user and save the changes. You'll also notice that there is a `Groups` section. This is a way of defining permissions for groups of users that fit into different categories — a group with specific permissions can be defined and then users can be moved in and out of this group. This is an easier way of applying permissions to large numbers of users.

Now we have a custom permission that applies to a model, and we have assigned this permission to a user. The last remaining thing to do is to inform `views.py`.
```python
# views.py

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

from .models import MyModel


class MyView(PermissionRequiredMixin, DetailView):
	model = MyModel
	context_object_name = 'my_object'
	template_name = 'object_detail.html'
	permission_required = 'my_app.special_status'
	
```

Above we have a class view that inherits from `DetailView`, which displays instances of `MyModel`. However — before inheriting from `DetailView`, we inherit `PermissionRequiredMixin` which tells the class to expect users accessing the page that invokes this view to have a particular permission, otherwise they will be given a `403 Forbidden` error. Finally we tell the class that the permission it should expect is `special_status`, with the syntax:

`permission_required = '{app_name}.{permission_name}'`

It is possible to specify multiple permissions for this field, but here we only specify one.