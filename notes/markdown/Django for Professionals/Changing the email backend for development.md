Note Type: #litnote
Source: [[📖 Django for Professionals]] ch7 p107

---
# Changing the email backend for development
When [[Configuring `django-allauth`]], it will attempt to send an email upon successful registration. To do this, an SMTP server needs to be set up for Django to use. However, if you're developing and are not yet ready to set up an SMTP server, you can output emails to the console by adding the following to `settings.py`:
```python
# settings.py
...

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

...
```
