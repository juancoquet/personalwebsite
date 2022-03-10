Note Type: #litnote
Source: [[📖 Django for Professionals]] ch13 p196

---
# Adding permissions to user for testing
You can add permissions to a user in a test method with the following syntax, where `{user}` is a user object and `{permission}` is a permission object:

`{user}.user_permissions.add({permission})`

A user object can be created by importing `get_user_model` from `django.contrib.auth`, and instantiating a new user. You can access a particular permission object by importing `Permission` from `django.contrib.auth.models`, then using `Permission.objects.get(codename='permission_name')`.

Here is a test example that uses these techniques:
```python
# tests.py

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase

User = get_user_model()


class MyTest(TestCase):

	def test_permission(self):
		user = User.objects.xreate_user(
			username='testuser',
			email='testuser@email.com',
			password='testpass123'
		)
		my_permission = Permission.objects.get(codename='my_permission')
		
		user.user_permissions.add(permission)
		
		...		# test permission

```
