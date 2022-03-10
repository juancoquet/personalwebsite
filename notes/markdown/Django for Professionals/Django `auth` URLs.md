Note Type: #litnote
Source: [[📖 Django for Professionals]] ch5 p66

---
# Django `auth` URLs
The built-in `auth` app has a number of URLs for common actions. Assuming we have followed the convention of routing `/accounts` to the `auth` app within our project-level `urls.py` file, the URLs that come with `auth` are as follows:
```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_rest_confirm']
accounts/reset/done/ [name='password_reset_complete']
```