Note Type: #litnote
Source: [[📖 Django for Professionals]] ch5 p73

---
# Handling login
When adding log in functionality, much of the work is done for us if we use Django's built in `auth` app (see [[Setting up built-in `auth` app]]).

The `auth` app comes with all the URLs we need (see [[Django `auth` URLs]]), each of which invokes a view that Django also provides — we just have to handle the templates.

The built in `/accounts/login/` URL uses a view that expects a `login.html` template inside a `registration` folder. We can create `registration/login.html` inside our `templates` folder, and then populate this file so Django knows what to display on our page. Use `{{ form.as p }}` to display the login form, and extend the base template if you have one set up.

The final step is to tell Django where to redirect after login, which we can do by providing a `LOGIN_REDIRECT_URL` constant in `settings.py`. We can give this constant a view name rather than a direct URL.
```python
# settings.py

...

LOGIN_REDIRECT_URL = 'home'
```
