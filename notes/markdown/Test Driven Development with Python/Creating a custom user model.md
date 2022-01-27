Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch18 p317

---
# Creating a custom user model
To override Django's default user model, first create a new `User` class in the usual way — by inheriting from `models.Model` — and specify the fields we want.
```python
# my_app/models.py
from django.db import models


class User(models.Model):
	email = models.EmailField(unique=True)
	
	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'email'
	is_anonymous = False
	is_authenticated = True
	
```

Here we created a new model that only requires an email field, and gave Django the required metadata about which field to use as the username (the only field we're specifying in this case, this is why `unique=True` is set) as well as what's required (username field is required by default). The last two attributes are more required Django boilerplate for user models.

To use this as our user model, we tell `settings.py` about it by specifying `AUTH_USER_MODEL`. You should also make sure that the app in which the model exists is included in `INSTALLED_APPS`:
```python
# settings.py
...

INSTALLED_APPS = [
	'django.contrib.admin',
	...
	'my_app',
]

AUTH_USER_MODEL = 'my_app.User'
```