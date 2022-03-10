Note Type: #litnote
Source: [[📖 Django for Professionals]] ch5 p76-80

---
# Handling sign up
In order to handle user sign ups, there are a few steps involved. In no particular order, since they are all required (follow TDD), they are as follows:

#### Update project-level `urls.py` to include `accounts/urls.py`
The built-in `auth` app has no standard URL path and view for signing users up — this is the part we must do ourselves. The project-level `urls.py` file should point to `accounts/urls.py`, where the sign up URL will be handled. To not interfere with the built-in `auth` URLs, make sure to point to `accounts/urls.py` *after* pointing to the built-in `auth`, as we will share the `accounts/` URL routing.
```pyhton
# config/urls.py	# project-level urls.py

from django import urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/', include('accounts.urls')),
]
```
We first route `accounts/` to the built in `auth` app's `urls.py` file, where all built in URLs will be handled (see [[Django `auth` URLs]]). Since there is no built in sign up URL, this will not be found in `auth/urls.py` so then we point to `accounts/urls.py`, where we will manually handle the request.

#### Create `accounts/urls.py`
In the `accounts` app you will need a `urls.py` file to catch the sign up request.
```python
# accounts/urls.py

from django.contrib import path
from .views import SignUpPageView


urlpatterns = [
	path('signup/', SignUpPageView.as_view(), name='signup'),
]
```

Here we catch the `/accounts/signup/` URL, and we use the class-based `SignUpPageView,` which we will create next.

#### Create sign up view
For the view, we will inherit from Django's `generic.CreateView` class. The generic views are commonly used views, such as creation forms, packaged into a class that we can inherit from for convenience.
```python
# accounts/views.py

from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
```

We define three attributes inside our class view. `form_class` informs the view as to which form to base the form fields on — we feed it `CustomUserCreationForm` (see [[Creating custom user forms]]). `success_url` tells the view where to go when a user successfully completes the sign up form — we use `reverse_lazy` to get the URL of the page named `login` (one of the `auth` app's built-ins). Finally, `template_name` tells the view which template to use.

#### Create sign up template
We must also create a sign up template for our view class to use. This is simple to do, just create a new template and extend your `base.html`, then create a form that references `{{ form }}`, as this is the context name given to the form used by the class view.
```HTML
...

<form method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<button type="submit">Sign Up</button>
</form>

...
```

All errors will be conveniently handled for us. The final step is to link to the sign up page's URL from another page.