Note Type: #litnote
Source: [[📖 Django for Professionals]] ch5 p66

---
# Setting up built-in `auth` app
The first step to setting up the built-in Django `auth` app is to check that it is included in `INSTALLED_APPS` within `settings.py`. This should be the case by default, but it's worth checking.

Next we must point a URL path to use the `auth` app from our project-level `urls.py` file. Django convention is to use `/accounts` to point to anything authentication-related.
```python
# urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
]
```

The `auth` app comes with a number of associated URLs — see [[ Django `auth` URLs]]. Each of these URL patterns invoke a built in view, meaning that much of the work when dealing with user authentication is done for us by Django.