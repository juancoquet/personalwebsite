Note Type: #litnote
Source: [[📖 Django for Professionals]] ch9 p140

---
# Setting up an email service
- [x] sign up for a service
- [ ] Override/write `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`
- [ ] Configure `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_PORT`, `EMAIL_USE_TLS` according to service provider instructions.

---
The first step in setting up a third party email service is to sign up — use SendGrid, MailGun, Amazon, or any other, and set up an SMTP service on their site. You'll be given some credentials and configurations.

Next we configure our email client in `settings.py`""
```python
# settings.py
...

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
```

Note that `EMAIL_BACKEND` may already be defined to output to the console if previously set up for development purposes. Here we override it. All other configurations will be provided by your service once you set up an SMTP service.