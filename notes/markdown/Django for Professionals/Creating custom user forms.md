Note Type: #litnote
Source: [[📖 Django for Professionals]] ch3 p45

---
# Creating custom user forms
When using a custom user model, we also need to define custom user creation and custom user change forms. We do so by first creating a `forms.py` file inside our `accounts` app.

In this file we define `CustomUserCreationForm`, which inherits from `UserCreationForm`, and `CustomUserChangeForm`, which inherits from `UserChangeForm`.
```python
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationform(UserCreationForm):

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')
		

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')
```

The `get_user_model` function looks up the user model defined at `AUTH_USER_MODEL` within `settings.py`. This is better than importing the model directly, as it means that we have one single direct reference to the user model rather than referring to it all over our project.

Inside each form class, we use the `Meta` class to tell Django to base this form on our custom user model, and tell it to show the fields `email` and `username` — password is always implicitly included.