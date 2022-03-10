Note Type: #litnote
Source: [[📖 Django for Professionals]] ch3 p43

---
# Creating a custom Django user model
To create a custom user model, it is a good idea to start by creating a designated `accounts` app with `python manage.py startapp accounts`. If using Docker, you can start this app within your container with `docker-compose exec {service_name} python manage.py startapp accounts`. Assuming you have a volume set up, the change will sync to your local computer.

Next go to the `models.py` file in the new app, and create a `CustomUser` class that inherits from Django's built-in `AbstractUser` or `AbstractBaseUser` (the latter affords more granular control over your custom user model, but is also trickier to implement).
```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	pass
```

New fields can be defined inside the class, but in this instance we just inherit the existing fields form `AbstractUser`.

Next we tell `settings.py` about our custom user model by adding `accounts` to `INSTALLED_APPS`  and creating a `AUTH_USER_MODEL` constant which points to our new model.
```python
# settings.py

...

INSTALLED_APPS = [
	...
	`accounts`,
]

...

AUTH_USER_MODEL = 'accounts.CustomUser'
```

Finally we can run `makemigrations accounts` and `migrate` (within Docker).

The next step is [[Creating custom user forms]]