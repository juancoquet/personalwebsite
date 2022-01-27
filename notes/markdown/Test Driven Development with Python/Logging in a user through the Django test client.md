Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch22 p395

---
# Logging in a user through the Django test client
If you need to log in a user for a test, use `client.force_login()`.
```python
from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class MyTest(TestCase):
	
	def test_login_user(self):
		user = User.objects.create(username='testaccount')
		self.client.force_login(user)
		...
```
