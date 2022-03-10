Note Type: #litnote
Source: [[📖 Django for Professionals]] ch7 p105

---
# Configuring `django-allauth`
The third-party `django-allauth` extension can be pip installed to allow for more authentication options. As always, remember to install within Docker if using a container.
```bash
$ docker-compose exec {service_name} pipenv install django-allauth==0.42.0
$ docker-compose down
$ docker-compose up -d --build
```

Next be sure to include it in `INSTALLED_APPS` in `settings.py`, as well as Django's built-in sites framework and `allauth.account`. We must also specify that we will be using `allauth` as a secondary authentication back end.
```python
# settings.py

...

INSTALLED_APPS =[
	...
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	...
]

SITE_ID = 1
ACCOUNT_LOGOUT_REDIRECT = 'home'
ATUHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SESSION_REMEMBER = True
```

Django's sites framework allows one Django project to control multiple sites. Since we are using it on only one project, we set the `SITE_ID` to `1`. Each site we add would increment the ID for that site.

`ModelBackend` is the default authentication back end used by Django, which is always implicitly set. To use the `allauth` back end also, we specify `AUTENTICATION_BACKENDS` and include the default `ModelBackend` and add the `allauth` back end below it.

We also specify `ACCOUNT_LOGOUT_REDIRECT`. This is a setting that overrides Django's standard `LOGOUT_REDIRECT_URL`, and it exists implicitly in the `allauth` configuration, which defaults to `'/'`, the homepage. We specify it explicitly in `settings.py` for clarity, and to future-proof our app — this way we can make future changes to the URL where the user is redirected upon logout.

The `ACCOUNT_SESSION_REMEMBER` constant handles whether or not to display a 'Remember Me' checkbox in the login page. `True` means it will always remember, and removes the checkbox. `False` means never, and the default `None` (meaning we haven't specified any value) will display the checkbox to let the user decide. We set it to `True`.

Next we must tell our project-level `urls.py` to use `allauth`'s' URLs. If you have previously configured for Django's built in `auth` URLs, this setting replaces that. The template names for `allauth` as the template names for Django's standard `auth`, but with the `account_` prefix (e.g. `login` becomes `account_login`). Remember to update any references previously made to the `auth` URL names accordingly.
```python
# config/urls.py

from django.urls import path, include


urlpatterns = [
	...
	path('accounts/', include('allauth.urls')),
	...
]

```

`allauth` looks for template files inside `templates/account`, so you should create this directory and populate it with your `login.html` and `signup.html` templates.

The final thing to do is to run `migrate` to update the database.
```bash
$ docker-compose exec {service_name} python manage.py migrate
```