Note Type: #litnote
Source: [[📖 Django for Professionals]] ch5 p75

---
# Handling logout
Handling user logouts is extremely easy when using the built in `auth` app. It comes with a logout URL with the name `logout`, which we can use in a button or an `<a>` tag.
```HTML
<a href="{% url 'logout' %}">Log out</a>
```

Clicking the HTML element created above will invoke the view with the name 'logout', which is the `auth` app's `LogoutView`. Now all we need to do is tell `LogoutView` where to redirect upon logging the user out, which we do in `settings.py` by providing a `LOGOUT_REDIRECT_URL` constant.
```python
# settings.py

...

LOGOUT_REDIRECT_URL = 'home'
```

Now when the web element calls into action the `LogoutView`, the user will be logged out and redirected to `'home'`.

---
### See also:
- [[Handling login]]