Note Type: #litnote
Source: [[📖 Django for Professionals]] ch3 p46

---
# Creating a custom user admin
When using a custom user model, we should also create a custom user admin so that we can manipulate our user model within Django's admin page.

To do this, we need to add code that pulls together our custom user model and forms into the `admin.py` file inside our `accounts` app.
```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username']
	

admin.site.regist(CustomUser, CustomUserAdmin)
```

We create `CustomUserAdmin` which inherits from the built-in `UserAdmin`, then we use the `add_form` and `form` attributes to tell it which forms to use for creating and editing users. We also feed our our `CustomUser` model using the `model` attribute and tell it to display the fields `email` and `username`.

Finally, we register the custom user models with our admin app.