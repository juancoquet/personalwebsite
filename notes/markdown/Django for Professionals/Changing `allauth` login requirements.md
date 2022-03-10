Note Type: #litnote
Source: [[📖 Django for Professionals]] ch7 p119

---
# Changing `allauth` login requirements
We can add a few configurations to `settings.py` to tell `allauth` to use email authentication instead of username authentication.
```python
# settings.py

...

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
```

Here we make `username` not a required field, but set `email` to required. We also tell `allauth` that we will be using `email` as our authentication method, and that all emails must be unique.